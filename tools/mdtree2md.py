#!/usr/bin/env python3
"""Turn a folder of Markdown documentation (as kept in many repos and
rendered by pandoc / static-site generators) into skill docs.

- copies every .md (keeping sub-folders), skipping --exclude globs
- rewrites relative links  page.html[#x] -> page.md[#x]
- trims build-only YAML front-matter keys (keeps title, author, date, lang)
- writes INDEX.md: every page with its title and headings, by folder
- writes _meta.json (source, version, date)
Optionally copies example files (--examples DIR --examples-glob '*.mfront').

Usage:
  python3 tools/mdtree2md.py --src repo/docs/web --out skills/x/docs \
      [--exclude 'release-notes/*'] [--source-url URL] [--version V]
"""
import argparse
import datetime as dt
import json
import re
import shutil
from pathlib import Path

KEEP_YAML = {"title", "author", "date", "lang", "description", "subtitle"}


def trim_front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, flags=re.S)
    if not m:
        return text, None
    kept, title = [], None
    for line in m.group(1).splitlines():
        key = line.split(":", 1)[0].strip()
        if key in KEEP_YAML:
            kept.append(line)
            if key == "title":
                title = line.split(":", 1)[1].strip().strip('"\'')
    head = "---\n" + "\n".join(kept) + "\n---\n" if kept else ""
    return head + text[m.end():], title


def rewrite_links(text):
    # [label](page.html#frag) -> [label](page.md#frag); leave absolute URLs alone
    def repl(m):
        target = m.group(2)
        if re.match(r"[a-z]+://", target) or not re.search(r"\.html(#|$)", target):
            return m.group(0)
        return f"{m.group(1)}({re.sub(r'\.html(?=#|$)', '.md', target)})"
    return re.sub(r"(\[[^\]]*\])\(([^)\s]+)\)", repl, text)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--exclude", action="append", default=[])
    ap.add_argument("--examples", help="folder with example files to copy into OUT/../examples")
    ap.add_argument("--examples-glob", action="append", default=[])
    ap.add_argument("--source-url", default="")
    ap.add_argument("--version", default="")
    args = ap.parse_args()

    src, out = Path(args.src), Path(args.out)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    index = []
    for p in sorted(src.rglob("*.md")):
        rel = p.relative_to(src)
        if any(rel.match(g) for g in args.exclude):
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        text, title = trim_front_matter(text)
        text = rewrite_links(text)
        dest = out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        body = re.sub(r"```.*?```", "", text, flags=re.S)  # no '#' from code blocks
        heads = [h.strip() for h in re.findall(r"(?m)^#{1,2} (.+)$", body)]
        heads = [re.sub(r"\s*\{[^}]*\}\s*$", "", h) for h in heads]  # pandoc {#id}
        index.append((rel.as_posix(), title or (heads[0] if heads else rel.stem), heads, len(text)))

    lines = ["# Index of pages\n", "Each entry: file — title, then its main headings.\n"]
    current = None
    for f, title, heads, size in sorted(index, key=lambda i: ("/" in i[0], i[0].lower())):
        top = f.split("/")[0] if "/" in f else "(root)"
        if top != current:
            lines.append(f"\n## {top}\n")
            current = top
        lines.append(f"- `{f}` — **{title}** ({max(1, size // 1000)} kB)")
        if heads:
            more = f" … (+{len(heads) - 8})" if len(heads) > 8 else ""
            lines.append(f"  - {' · '.join(heads[:8])}{more}")
    (out / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    n_ex = 0
    if args.examples:
        ex_out = out.parent / "examples"
        if ex_out.exists():
            shutil.rmtree(ex_out)
        for g in args.examples_glob:
            for p in Path(args.examples).rglob(g):
                d = ex_out / p.relative_to(args.examples)
                d.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(p, d)
                n_ex += 1
    meta = {"source": args.source_url or str(src), "version": args.version,
            "generated": dt.date.today().isoformat(), "pages": len(index), "examples": n_ex}
    (out / "_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"{len(index)} pages, {n_ex} example files → {out}")


if __name__ == "__main__":
    main()
