#!/usr/bin/env python3
"""Mirror a published Sphinx documentation site as agent-friendly Markdown.

Reads the site's searchindex.js to get every page, downloads each rendered
HTML page (so autodoc API pages and executed notebooks are included),
keeps only the main content and converts it to Markdown. Internal links are
rewritten to the local .md files. Also writes:
  - INDEX.md   : every page with its title and section headings
  - _meta.json : source URL, date, page list

Usage:
  python3 tools/sphinx2md.py --base https://host/docs/latest/ --out skills/foo/docs
  python3 tools/sphinx2md.py --base https://host/docs/latest/ --local mirror/docs/latest \
      --out skills/foo/docs        # from a downloaded copy (wget -m)
Requires: pip install requests beautifulsoup4 markdownify
"""
import argparse
import datetime as dt
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

MAX_OUTPUT_LINES = 60
SKIP = re.compile(r"(^|/)(CMakeLists|sphinx_build_warnings|genindex|search|py-modindex)$")


class Converter(MarkdownConverter):
    def convert_pre(self, el, text, *args, **kwargs):
        lang = ""
        for parent in el.parents:
            for c in parent.get("class", []) or []:
                if c.startswith("highlight-") and c != "highlight-default":
                    lang = c[len("highlight-"):]
                    break
            if lang or parent.name in ("section", "body"):
                break
        code = el.get_text()
        return f"\n```{lang}\n{code.rstrip()}\n```\n"


def fetch(session, url, retries=3):
    for i in range(retries):
        try:
            r = session.get(url, timeout=60)
            if r.status_code == 404:
                return None
            r.raise_for_status()
            r.encoding = r.encoding or "utf-8"
            return r.text
        except requests.RequestException:
            if i == retries - 1:
                raise
            time.sleep(2 * (i + 1))


def load_docnames(session, base):
    js = fetch(session, urljoin(base, "searchindex.js"))
    if js is None:
        sys.exit("searchindex.js not found — is --base the root of a Sphinx site?")
    payload = js[js.index("(") + 1: js.rindex(")")]
    return json.loads(payload)["docnames"]


def main_content(soup):
    for sel in ['div[role="main"]', "article", "div.body", "main"]:
        node = soup.select_one(sel)
        if node:
            return node
    return soup.body or soup


def convert_page(html, docname, page_url):
    soup = BeautifulSoup(html, "html.parser")
    node = main_content(soup)
    for junk in node.select("a.headerlink, script, style, div.rst-footer-buttons, "
                            "nav, footer, .prompt, .copybtn, "
                            "span.linenos, td.linenos"):  # code line numbers
        junk.decompose()
    # notebook outputs (run logs) can be thousands of lines: keep head and tail
    for pre in node.select("div.nboutput pre, div.cell_output pre, div.output pre"):
        lines = pre.get_text().splitlines()
        if len(lines) > MAX_OUTPUT_LINES:
            keep = lines[:20] + [f"… [{len(lines) - 30} lines of output omitted] …"] + lines[-10:]
            pre.string = "\n".join(keep)
    # images are not copied: link them to the published site
    for img in node.find_all("img", src=True):
        img["src"] = urljoin(page_url, img["src"])
        if not img.get("alt") or "/" in img.get("alt", ""):
            img["alt"] = "figure"
    # API signatures: drop the cross-reference links on every type name
    for dt_el in node.find_all("dt"):
        for a in dt_el.find_all("a"):
            a.unwrap()
    # numpydoc "name<span class=classifier>type</span>" -> "name : type"
    for c in node.select("span.classifier"):
        c.insert_before(" : ")
    for a in node.find_all("a", title=True):
        del a["title"]
    # relative links between pages: foo/bar.html#x -> foo/bar.md#x
    for a in node.find_all("a", href=True):
        href = a["href"]
        if urlparse(href).scheme or href.startswith("#"):
            continue
        path, _, frag = href.partition("#")
        if path.endswith(".html"):
            a["href"] = path[:-5] + ".md" + (f"#{frag}" if frag else "")
    title_el = node.find(["h1", "h2"])
    title = title_el.get_text(" ", strip=True) if title_el else docname
    headings = [h.get_text(" ", strip=True) for h in node.find_all(["h2", "h3"])]
    # no escaping: agents must be able to grep set_output_file, k_B, *args…
    md = Converter(heading_style="ATX", bullets="-", escape_underscores=False,
                   escape_asterisks=False, escape_misc=False).convert_soup(node)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    return title, headings, md


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", required=True,
                    help="root URL of the Sphinx site (also used in citations)")
    ap.add_argument("--local", help="convert a downloaded copy of the site in this "
                                    "folder instead of fetching --base")
    ap.add_argument("--out", required=True)
    ap.add_argument("--delay", type=float, default=0.2, help="seconds between requests")
    args = ap.parse_args()

    base = args.base if args.base.endswith("/") else args.base + "/"
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for old in out.rglob("*.md"):
        old.unlink()

    if args.local:
        # offline mode: a downloaded copy of the site (e.g. wget -m)
        root = Path(args.local)
        docnames = sorted(p.relative_to(root).with_suffix("").as_posix()
                          for p in root.rglob("*.html") if "_static" not in p.parts)
        docnames = [d for d in docnames if not SKIP.search(d)]

        def get(d):
            f = root / f"{d}.html"
            return f.read_text(encoding="utf-8", errors="replace") if f.exists() else None
        args.delay = 0
        print(f"{len(docnames)} pages from {root} (cited as {base})")
    else:
        s = requests.Session()
        s.headers["User-Agent"] = "code-docs-skills sync"
        docnames = [d for d in load_docnames(s, base) if not SKIP.search(d)]

        def get(d):
            return fetch(s, urljoin(base, d + ".html"))
        print(f"{len(docnames)} pages from {base}")

    index = []
    for d in docnames:
        html = get(d)
        if html is None:
            print(f"  skip (404) {d}")
            continue
        title, headings, md = convert_page(html, d, urljoin(base, d + ".html"))
        dest = out / f"{d}.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(f"<!-- source: {urljoin(base, d + '.html')} -->\n\n{md}",
                        encoding="utf-8")
        index.append((d, title, headings, len(md)))
        print(f"  {d}.md")
        time.sleep(args.delay)

    lines = ["# Index of pages\n",
             "Each entry: file — title, then its section headings.\n"]
    current = None
    for d, title, headings, size in sorted(index):
        top = d.split("/")[0] if "/" in d else "(root)"
        if top != current:
            lines.append(f"\n## {top}\n")
            current = top
        lines.append(f"- `{d}.md` — **{title}** ({max(1, size // 1000)} kB)")
        if headings:
            shown = headings[:12]
            more = f" … (+{len(headings) - 12})" if len(headings) > 12 else ""
            lines.append(f"  - {' · '.join(shown)}{more}")
    (out / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    meta = {"source": base, "generated": dt.date.today().isoformat(),
            "pages": [i[0] for i in index]}
    (out / "_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Done → {out}")


if __name__ == "__main__":
    main()
