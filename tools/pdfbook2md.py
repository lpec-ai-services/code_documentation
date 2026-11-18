#!/usr/bin/env python3
"""Convert a book delivered as one PDF per chapter (publisher downloads).

Each chapter PDF goes through pdf2md.py into its own folder NN-<title>
(NN = chapter number read from the file name, e.g. "7---Heat-transfer…pdf").
Unnumbered PDFs whose name starts with one of --extra (e.g. Preface,
Subject-Index) get a lowercase folder name. Writes TOC.md for the whole
book: chapter → folder → section files with printed pages.

Usage:
  python3 tools/pdfbook2md.py --dir chapters/ --out skills/x/sources/book \
      [--extra Preface --extra Subject-Index] [-- <extra pdf2md.py options>]
"""
import argparse
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import pymupdf

HERE = Path(__file__).resolve().parent


def slug(text, maxlen=45):
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:maxlen].strip("-")


def main():
    argv = sys.argv[1:]
    passthru = []
    if "--" in argv:
        i = argv.index("--")
        argv, passthru = argv[:i], argv[i + 1:]
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--extra", action="append", default=[],
                    help="file-name prefix of an unnumbered PDF to include")
    ap.add_argument("--title", default="", help="book title for TOC.md")
    args = ap.parse_args(argv)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    jobs = []
    for pdf in sorted(Path(args.dir).glob("*.pdf")):
        m = re.match(r"(\d+)-", pdf.name)
        if m:
            title = (pymupdf.open(pdf).get_toc() or [[1, pdf.stem]])[0][1]
            jobs.append((int(m.group(1)), f"{int(m.group(1)):02d}-{slug(title)}", title, pdf))
        elif any(pdf.name.startswith(e) for e in args.extra):
            name = pdf.name.split("_")[0]
            jobs.append((1000 + len(jobs), slug(name), name.replace("-", " "), pdf))
    jobs.sort()

    lines = [f"# {args.title or 'Table of contents'}\n",
             "Chapter → folder; inside each folder, TOC.md maps every section to its file "
             "and printed page.\n"]
    for num, folder, title, pdf in jobs:
        cmd = [sys.executable, "-I", str(HERE / "pdf2md.py"), "--pdf", str(pdf),
               "--out", str(out / folder)] + passthru
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode:
            sys.exit(f"{pdf.name}: {r.stderr}")
        doc = pymupdf.open(pdf)
        first, last = doc[0].get_label(), doc[-1].get_label()
        pages = f"pp. {first}–{last}" if first else f"{doc.page_count} pages"
        lines.append(f"\n## {title} — `{folder}/` ({pages})\n")
        for f in sorted((out / folder).glob("[0-9]*.md")):
            head = f.read_text(encoding="utf-8").split("\n", 1)[0].lstrip("# ")
            lines.append(f"- `{folder}/{f.name}` — {head}")
        print(f"{folder}: {r.stdout.splitlines()[0] if r.stdout else ''}")
    (out / "TOC.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
