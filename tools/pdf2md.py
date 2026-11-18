#!/usr/bin/env python3
"""Convert a PDF manual into agent-friendly Markdown files.

One Markdown file per top-level chapter of the PDF outline (bookmarks), with
`<!-- page N -->` markers so agents can cite PDF pages, plus:
  - TOC.md   : the full outline, every entry pointing to its file and PDF page
  - _meta.json : source URL / file, date, page count

Usage:
  python3 tools/pdf2md.py --url https://.../manual.pdf --out skills/foo/docs
  python3 tools/pdf2md.py --pdf manual.pdf --out skills/foo/docs [--markdown]

Default: cleaned plain text (keeps the line layout of syntax blocks, outline
titles become headings, ligatures/hyphenation/running headers fixed).
--markdown: pymupdf4llm output instead (needs pymupdf4llm).
Requires: pip install pymupdf requests [pymupdf4llm]
"""
import argparse
import datetime as dt
import json
import re
import sys
import tempfile
from pathlib import Path

import pymupdf

try:
    import pymupdf4llm
except ImportError:  # fall back to plain text
    pymupdf4llm = None


def slugify(text, maxlen=50):
    import unicodedata
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^\w\s-]", "", text.lower(), flags=re.ASCII)
    return re.sub(r"[\s_-]+", "-", text).strip("-")[:maxlen].strip("-") or "section"


def download(url, dest):
    import requests

    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(1 << 20):
                f.write(chunk)
    return dest


LIGATURES = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi",
             "\ufb04": "ffl", "\ufb05": "st", "\ufb06": "st"}


def norm(t):
    return re.sub(r"\s+", " ", t).strip().lower()


def find_running_lines(doc, sample=60):
    """Lines repeated at the top/bottom of many pages (headers, footers)."""
    from collections import Counter
    count, n = Counter(), 0
    step = max(1, doc.page_count // sample)
    for i in range(0, doc.page_count, step):
        lines = [l for l in doc[i].get_text().splitlines() if l.strip()]
        for l in lines[:3] + lines[-3:]:
            count[re.sub(r"\d+", "#", norm(l))] += 1
        n += 1
    return {k for k, c in count.items() if c >= max(3, n * 0.3)}


def clean_text(text, running, headings):
    """Plain page text -> Markdown-ish text that greps well.

    headings: [(level, title)] outline entries starting on this page.
    """
    for k, v in LIGATURES.items():
        text = text.replace(k, v)
    lines = [l.rstrip() for l in text.splitlines()]
    lines = [l for l in lines
             if re.sub(r"\d+", "#", norm(l)) not in running]
    # outline titles -> Markdown headings (section number may sit on the line above)
    for lvl, title in headings:
        t = norm(title)
        pat = re.compile(r"(([\dA-Z]+\.)*[\dA-Z]+\.? )?" + re.escape(t), re.I)
        for i, l in enumerate(lines):
            span = 1
            if not pat.fullmatch(norm(l)):
                # title wrapped onto the next line
                if i + 1 < len(lines) and pat.fullmatch(norm(l + " " + lines[i + 1])):
                    span = 2
                else:
                    continue
            num = ""
            if i > 0 and re.fullmatch(r"(\d+|[A-Z])(\.\d+)*\.?", lines[i - 1].strip()):
                num = lines[i - 1].strip() + " "
                lines[i - 1] = ""
            joined = " ".join(x.strip() for x in lines[i:i + span])
            lines[i] = "\n" + "#" * min(lvl, 6) + " " + num + joined + "\n"
            if span == 2:
                lines[i + 1] = ""
            break
    text = "\n".join(lines)
    # words hyphenated across lines: "renormal-\nizes" -> "renormalizes"
    text = re.sub(r"([a-zà-öø-ÿ])-\n([a-zà-öø-ÿ]+)([ \t]*)", r"\1\2\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def row_text(page, gap=12):
    """Text rebuilt line by line from word positions, cells joined by ' | '.

    For keyword tables, where plain extraction puts every cell on its own line.
    """
    rows = {}
    for x0, y0, x1, y1, w, *_ in page.get_text("words"):
        rows.setdefault(round(y1), []).append((x0, x1, w))
    out = []
    for y in sorted(rows):
        ws = sorted(rows[y])
        cells = [[ws[0]]]
        for a, b in zip(ws, ws[1:]):
            (cells[-1].append(b) if b[0] - a[1] < gap else cells.append([b]))
        out.append(" | ".join(" ".join(w[2] for w in c) for c in cells))
    return "\n".join(out)


def parse_pages(spec):
    """'552-562,600' -> {551..561, 599} (0-based)."""
    pages = set()
    for part in filter(None, (spec or "").split(",")):
        a, _, b = part.partition("-")
        pages.update(range(int(a) - 1, int(b or a)))
    return pages


def page_texts(doc, pages, markdown, row_pages=frozenset()):
    """Return {page_index: text} for the given 0-based pages."""
    if not markdown or pymupdf4llm is None:
        return {p: row_text(doc[p]) if p in row_pages else doc[p].get_text()
                for p in pages}
    chunks = pymupdf4llm.to_markdown(doc, pages=list(pages), page_chunks=True,
                                     show_progress=False)
    out = {}
    for c in chunks:
        p = c["metadata"].get("page_number", c["metadata"].get("page", 0)) - 1
        out[p] = c["text"]
    return out


def parse_sizes(spec):
    return [float(x) for x in (spec or "").split(",") if x.strip()]


def font_page(page, chap_sizes, sec_sizes, footer_y=None, tol=0.3, sub_sizes=()):
    """Page text where lines set in heading font sizes become headings.

    For PDFs without bookmarks. Returns (text, [(level, title)]).
    Consecutive heading lines of the same level are merged.
    """
    out, heads = [], []
    pending = None  # (level, [parts])

    def flush():
        nonlocal pending
        if pending:
            title = re.sub(r"\s+", " ", " ".join(pending[1])).strip()
            out.append("\n" + "#" * pending[0] + " " + title + "\n")
            heads.append((pending[0], title))
            pending = None

    for b in page.get_text("dict", flags=pymupdf.TEXTFLAGS_TEXT)["blocks"]:
        for l in b.get("lines", []):
            if footer_y is not None and l["bbox"][1] > footer_y:
                continue
            spans = [sp for sp in l["spans"] if sp["text"].strip()]
            if not spans:
                continue
            text = "".join(sp["text"] for sp in l["spans"])
            size = max(sp["size"] for sp in spans)
            level = 1 if any(abs(size - c) < tol for c in chap_sizes) else \
                2 if any(abs(size - c) < tol for c in sec_sizes) else 0
            # sub-sections: whole line bold, in one of the given sizes
            if not level and sub_sizes and all("Bold" in sp["font"] for sp in spans) \
                    and any(abs(spans[0]["size"] - c) < tol for c in sub_sizes):
                level = 3
            # a title has words; big symbols and diagram labels do not
            if level and not (pending and pending[0] == level) \
                    and not re.search(r"[a-zà-ÿ]{3,}", text):
                level = 0
            if level:
                if pending and pending[0] == level:
                    pending[1].append(text)
                else:
                    flush()
                    pending = (level, [text])
            else:
                flush()
                out.append(text)
    flush()
    return "\n".join(out), heads


def pick_split_level(toc, wanted=None):
    """Outline level whose entries are the chapters.

    Some PDFs are merges whose level-1 bookmarks are file names; the chapters
    are then one level deeper. Take the shallowest level with >= 3 entries.
    """
    if wanted:
        return wanted
    for lvl in sorted({e[0] for e in toc}):
        if sum(1 for e in toc if e[0] == lvl) >= 3:
            return lvl
    return 1


def build_chapters(doc, split_level=None, front_pages=0):
    """Split the document by outline entries of the chapter level.

    Returns (chapters, toc, level): chapters are dicts {title, start, end}
    with 0-based inclusive pages. Falls back to fixed 25-page parts when the
    PDF has no outline.
    """
    n = doc.page_count
    toc = [e for e in doc.get_toc(simple=True) if e[2] >= 1]
    level = pick_split_level(toc, split_level)
    tops = []
    for lvl, t, p in toc:
        if lvl != level or p <= front_pages:
            continue
        if tops and tops[-1][1] == p - 1:  # same start page: keep the first
            continue
        tops.append((t.strip(), p - 1))
    chapters = []
    if not tops:
        for i, s in enumerate(range(0, n, 25)):
            chapters.append({"title": f"Part {i + 1}", "start": s,
                             "end": min(s + 24, n - 1)})
        return chapters, toc, level
    if front_pages:
        tops = [t for t in tops if t[1] >= front_pages]
    if tops[0][1] > 0:
        chapters.append({"title": "Front matter", "start": 0, "end": tops[0][1] - 1})
    for i, (title, start) in enumerate(tops):
        end = tops[i + 1][1] - 1 if i + 1 < len(tops) else n - 1
        chapters.append({"title": title, "start": start, "end": max(start, end)})
    return chapters, toc, level


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--url")
    src.add_argument("--pdf")
    ap.add_argument("--out", required=True)
    ap.add_argument("--markdown", action="store_true",
                    help="use pymupdf4llm (bold/italic/tables) instead of cleaned "
                         "plain text; it flattens line-based syntax blocks")
    ap.add_argument("--front-matter-pages", type=int, default=0,
                    help="pages 1..N form one front-matter file (title pages, contents)")
    ap.add_argument("--table-pages", default="",
                    help="pages (e.g. 552-562) whose lines are rebuilt as table rows")
    ap.add_argument("--chapter-sizes", default="",
                    help="no bookmarks: font sizes of chapter titles, e.g. 16,18")
    ap.add_argument("--section-sizes", default="",
                    help="no bookmarks: font sizes of section titles, e.g. 11.5")
    ap.add_argument("--subsection-sizes", default="",
                    help="no bookmarks: sizes of all-bold lines that are sub-section titles")
    ap.add_argument("--footer-y", type=float,
                    help="drop text lines starting below this y (page footers)")
    ap.add_argument("--page-offset", type=int, default=0,
                    help="printed page = PDF page + offset (used in page markers)")
    ap.add_argument("--split-level", type=int,
                    help="outline level of chapters (default: auto)")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.md"):
        old.unlink()

    if args.url:
        tmp = Path(tempfile.mkdtemp()) / "source.pdf"
        print(f"Downloading {args.url}")
        pdf_path = download(args.url, tmp)
    else:
        pdf_path = Path(args.pdf)

    doc = pymupdf.open(pdf_path)
    chap_sizes, sec_sizes = parse_sizes(args.chapter_sizes), parse_sizes(args.section_sizes)
    font_texts = {}
    if chap_sizes:
        # build an outline from heading fonts, then reuse the normal splitting
        synth = []
        for i, page in enumerate(doc):
            text, heads = font_page(page, chap_sizes, sec_sizes, args.footer_y,
                                    sub_sizes=parse_sizes(args.subsection_sizes))
            font_texts[i] = text
            synth += [[lvl, t, i + 1] for lvl, t in heads]
        doc.set_toc(synth)
    chapters, toc, level = build_chapters(doc, args.split_level, args.front_matter_pages)
    print(f"{doc.page_count} pages, {len(chapters)} chapter files (outline level {level})")

    page_to_file = {}
    for i, ch in enumerate(chapters):
        ch["file"] = f"{i:02d}-{slugify(ch['title'])}.md"
        for p in range(ch["start"], ch["end"] + 1):
            page_to_file[p] = ch["file"]

    running = set() if args.markdown else find_running_lines(doc)
    heads_by_page = {}
    for lvl, title, page in toc:
        if lvl > level:  # chapter titles are the file's own "# " heading
            heads_by_page.setdefault(page - 1, []).append((lvl - level + 1, title))

    for ch in chapters:
        pages = range(ch["start"], ch["end"] + 1)
        if font_texts:  # headings already in place
            texts = {p: clean_text(font_texts[p], running, []) for p in pages}
        else:
            texts = page_texts(doc, pages, args.markdown, parse_pages(args.table_pages))
            if not args.markdown:
                texts = {p: clean_text(t, running, heads_by_page.get(p, []))
                         for p, t in texts.items()}
        parts = [f"# {ch['title']}\n",
                 f"<!-- source PDF pages {ch['start'] + 1}-{ch['end'] + 1} -->\n"]
        for p in pages:
            label = f"page {p + 1 + args.page_offset} (PDF {p + 1})" if args.page_offset \
                else f"page {p + 1}"
            parts.append(f"\n<!-- {label} -->\n")
            parts.append(texts.get(p, "").strip() + "\n")
        (out / ch["file"]).write_text("".join(parts), encoding="utf-8")
        print(f"  {ch['file']}  (pp. {ch['start'] + 1}-{ch['end'] + 1})")

    lines = ["# Table of contents\n",
             "Each entry: title → file (PDF page). Grep the file for the title, "
             "or for `<!-- page N -->`.\n"]
    for lvl, title, page in toc:
        if lvl < level:  # wrapper bookmarks above the chapters
            continue
        f = page_to_file.get(page - 1, "?")
        where = f"p. {page + args.page_offset}, PDF {page}" if args.page_offset else f"p. {page}"
        lines.append(f"{'  ' * (lvl - level)}- {title.strip()} → `{f}` ({where})")
    if not toc:
        lines += [f"- {c['title']} → `{c['file']}`" for c in chapters]
    (out / "TOC.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    meta = {"source": args.url or str(pdf_path), "generated": dt.date.today().isoformat(),
            "pages": doc.page_count, "chapters": [c["file"] for c in chapters],
            "converter": "pymupdf4llm" if args.markdown and pymupdf4llm else "pymupdf text"}
    (out / "_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Done → {out}")


if __name__ == "__main__":
    sys.exit(main())
