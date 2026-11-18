#!/usr/bin/env python3
"""Convert a PDF manual into agent-friendly Markdown files.

One Markdown file per top-level chapter of the PDF outline (bookmarks), with
`<!-- page N -->` markers so agents can cite PDF pages, plus:
  - TOC.md   : the full outline, every entry pointing to its file and PDF page
  - _meta.json : source URL / file, date, page count

Usage:
  python3 tools/pdf2md.py --url https://.../manual.pdf --out skills/foo/docs
  python3 tools/pdf2md.py --pdf manual.pdf --out skills/foo/docs [--fast]

--fast uses plain text extraction (much quicker, no Markdown tables/headings).
Requires: pip install pymupdf pymupdf4llm requests
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


def page_texts(doc, pages, fast):
    """Return {page_index: markdown_or_text} for the given 0-based pages."""
    if fast or pymupdf4llm is None:
        return {p: doc[p].get_text() for p in pages}
    chunks = pymupdf4llm.to_markdown(doc, pages=list(pages), page_chunks=True,
                                     show_progress=False)
    out = {}
    for c in chunks:
        # metadata page numbers are 1-based in pymupdf4llm
        p = c["metadata"].get("page_number", c["metadata"].get("page", 0)) - 1
        out[p] = c["text"]
    return out


def build_chapters(doc):
    """Split the document by level-1 outline entries.

    Returns a list of dicts: {title, start, end} with 0-based inclusive pages.
    Falls back to fixed 25-page parts when the PDF has no outline.
    """
    n = doc.page_count
    toc = [e for e in doc.get_toc(simple=True) if e[2] >= 1]
    tops = [(t, p - 1) for lvl, t, p in toc if lvl == 1]
    chapters = []
    if not tops:
        for i, s in enumerate(range(0, n, 25)):
            chapters.append({"title": f"Part {i + 1}", "start": s,
                             "end": min(s + 24, n - 1)})
        return chapters, toc
    if tops[0][1] > 0:
        chapters.append({"title": "Front matter", "start": 0, "end": tops[0][1] - 1})
    for i, (title, start) in enumerate(tops):
        end = tops[i + 1][1] - 1 if i + 1 < len(tops) else n - 1
        chapters.append({"title": title.strip(), "start": start, "end": max(start, end)})
    return chapters, toc


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--url")
    src.add_argument("--pdf")
    ap.add_argument("--out", required=True)
    ap.add_argument("--fast", action="store_true")
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
    chapters, toc = build_chapters(doc)
    print(f"{doc.page_count} pages, {len(chapters)} chapter files")

    page_to_file = {}
    for i, ch in enumerate(chapters):
        ch["file"] = f"{i:02d}-{slugify(ch['title'])}.md"
        for p in range(ch["start"], ch["end"] + 1):
            page_to_file[p] = ch["file"]

    for ch in chapters:
        pages = range(ch["start"], ch["end"] + 1)
        texts = page_texts(doc, pages, args.fast)
        parts = [f"# {ch['title']}\n",
                 f"<!-- source PDF pages {ch['start'] + 1}-{ch['end'] + 1} -->\n"]
        for p in pages:
            parts.append(f"\n<!-- page {p + 1} -->\n")
            parts.append(texts.get(p, "").strip() + "\n")
        (out / ch["file"]).write_text("".join(parts), encoding="utf-8")
        print(f"  {ch['file']}  (pp. {ch['start'] + 1}-{ch['end'] + 1})")

    lines = ["# Table of contents\n",
             "Each entry: title → file (PDF page). Grep the file for the title, "
             "or for `<!-- page N -->`.\n"]
    for lvl, title, page in toc:
        f = page_to_file.get(page - 1, "?")
        lines.append(f"{'  ' * (lvl - 1)}- {title.strip()} → `{f}` (p. {page})")
    if not toc:
        lines += [f"- {c['title']} → `{c['file']}`" for c in chapters]
    (out / "TOC.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    meta = {"source": args.url or str(pdf_path), "generated": dt.date.today().isoformat(),
            "pages": doc.page_count, "chapters": [c["file"] for c in chapters],
            "converter": "pymupdf (fast)" if args.fast or pymupdf4llm is None else "pymupdf4llm"}
    (out / "_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Done → {out}")


if __name__ == "__main__":
    sys.exit(main())
