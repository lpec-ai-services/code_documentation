#!/usr/bin/env python3
"""Convert a whole folder of PDFs (papers, theses, reports) to Markdown, one
.md file per PDF, for grep or a RAG index.

Built for the PDFs downloaded by hal_harvest.py, but works on any folder.
  - every *.pdf under --in (recursive) -> same relative path under --out, .md
  - if a HAL catalogue (hal.sqlite) is found, each file starts with YAML front
    matter (title, authors, year, halId, DOI, URL, type, domains, keywords,
    licence) and the abstract; otherwise the PDF's own metadata is used
  - page markers <!-- page N -->, running headers/footers removed, ligatures
    and end-of-line hyphenation fixed
  - resumable: a PDF whose .md is newer is skipped, so re-running after an
    interruption or a new harvest converts only what is new (--force: all)
  - each PDF is converted in its own process with a time limit, so a broken
    or huge PDF cannot block the run; failures are listed, not fatal
  - PDFs without a text layer (scans) are reported as "no-text" (no OCR here)
  - writes _status.jsonl (one line per PDF) and INDEX.csv

Usage:
  python3 tools/pdfs2md.py --in ~/hal/pdf --out ~/hal/md --workers 8
  python3 tools/pdfs2md.py --in pdfs_hal --out pdfs_hal_md            # any folder
  python3 tools/pdfs2md.py --in ~/hal/pdf --out ~/hal/md --markdown   # headings/tables, ~10x slower
Requires: pip install pymupdf  (and pymupdf4llm for --markdown)
"""
import argparse
import csv
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIGATURES = {"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi",
             "ﬄ": "ffl", "ﬅ": "st", "ﬆ": "st"}
STEM = re.compile(r"^(?P<halid>[a-z]+-\d+)(v(?P<v>\d+))?$")


# ------------------------------------------------------------ one PDF (child)

def norm(t):
    return re.sub(r"\s+", " ", t).strip().lower()


def running_lines(texts):
    """Lines repeated at the top/bottom of many pages (headers, footers)."""
    from collections import Counter
    count = Counter()
    for t in texts:
        lines = [l for l in t.splitlines() if l.strip()]
        for l in set(lines[:2] + lines[-2:]):
            if len(l.strip()) <= 100:  # headers/footers are short lines
                count[re.sub(r"\d+", "#", norm(l))] += 1
    n = len(texts)
    return {k for k, c in count.items() if n >= 4 and c >= max(3, n * 0.3)}


def clean(text, running):
    for k, v in LIGATURES.items():
        text = text.replace(k, v)
    text = text.replace("\x00", "")
    lines = [l.rstrip() for l in text.splitlines()
             if re.sub(r"\d+", "#", norm(l)) not in running]
    text = "\n".join(lines)
    text = re.sub(r"([a-zà-öø-ÿ])-\n([a-zà-öø-ÿ]+)([ \t]*)", r"\1\2\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def yaml_str(v):
    return json.dumps(v, ensure_ascii=False)  # JSON strings are valid YAML


def front_matter(meta):
    keys = ["title", "authors", "year", "halId", "version", "doi", "url", "docType",
            "language", "journal", "conference", "domains", "keywords", "licence", "source_pdf"]
    out = ["---"]
    for k in keys:
        v = meta.get(k)
        if v in (None, "", []):
            continue
        out.append(f"{k}: {yaml_str(v)}")
    out.append("---\n")
    return "\n".join(out)


def convert_one(pdf, dest, meta, markdown, max_pages):
    import pymupdf
    doc = pymupdf.open(pdf)
    n = doc.page_count if not max_pages else min(doc.page_count, max_pages)
    if markdown:
        import pymupdf4llm
        chunks = pymupdf4llm.to_markdown(doc, pages=list(range(n)), page_chunks=True,
                                         show_progress=False)
        texts = [c["text"] for c in chunks]
    else:
        texts = [doc[i].get_text() for i in range(n)]
    chars = sum(len(t.strip()) for t in texts)
    pdfmeta = doc.metadata or {}
    if not meta.get("title") and pdfmeta.get("title"):
        meta["title"] = pdfmeta["title"]
    if not meta.get("authors") and pdfmeta.get("author"):
        meta["authors"] = [pdfmeta["author"]]
    status = "ok" if chars >= 30 * max(1, n) else "no-text"  # scans: ~0 chars/page
    run = running_lines(texts)
    parts = [front_matter(meta)]
    if meta.get("title"):
        parts.append(f"# {meta['title']}\n")
    if meta.get("abstract"):
        parts.append(f"**Abstract.** {meta['abstract']}\n")
    if status == "no-text":
        parts.append("<!-- no text layer: scanned PDF, needs OCR -->\n")
    for i, t in enumerate(texts):
        body = clean(t, run)
        if body:
            parts.append(f"<!-- page {i + 1} -->\n\n{body}\n")
    if max_pages and doc.page_count > n:
        parts.append(f"<!-- truncated: {doc.page_count - n} more pages in the PDF -->\n")
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(".md.part")
    tmp.write_text("\n".join(parts), encoding="utf-8")
    os.replace(tmp, dest)
    return {"status": status, "pages": doc.page_count, "chars": chars}


def child(argv):
    a = json.loads(argv)
    r = convert_one(Path(a["pdf"]), Path(a["dest"]), a["meta"], a["markdown"], a["max_pages"])
    print(json.dumps(r))


# ------------------------------------------------------------ catalogue

def load_catalogue(path):
    """halId -> metadata, from hal_harvest.py's hal.sqlite."""
    if not path or not Path(path).exists():
        return {}
    db = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    cat = {}
    for halid, js in db.execute("SELECT halid, json FROM records"):
        try:
            r = json.loads(js)
        except (TypeError, ValueError):
            continue
        first = lambda k: (r.get(k) or [None])[0] if isinstance(r.get(k), list) else r.get(k)
        date = r.get("publicationDate_tdate") or r.get("producedDate_tdate") or ""
        cat[halid] = {
            "title": first("title_s"), "authors": r.get("authFullName_s"),
            "year": int(date[:4]) if date[:4].isdigit() else None,
            "halId": r.get("halId_s"), "version": r.get("version_i"),
            "doi": r.get("doiId_s"), "url": r.get("uri_s"), "docType": r.get("docType_s"),
            "language": first("language_s"), "journal": r.get("journalTitle_s"),
            "conference": r.get("conferenceTitle_s"),
            "domains": r.get("domainAllCode_s"), "keywords": r.get("keyword_s"),
            "licence": r.get("licence_s"), "abstract": first("abstract_s"),
        }
    return cat


def find_catalogue(inp, given):
    if given:
        return given
    for d in [inp, *inp.parents][:3]:
        if (d / "hal.sqlite").exists():
            return d / "hal.sqlite"
    return None


# ------------------------------------------------------------ main

def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--one":
        return child(sys.argv[2])
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--in", dest="inp", required=True, help="folder of PDFs (searched recursively)")
    ap.add_argument("--out", required=True, help="output folder for the .md files")
    ap.add_argument("--catalog", help="hal.sqlite (default: looked for in --in and its parents)")
    ap.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) - 1))
    ap.add_argument("--timeout", type=int, default=300, help="seconds per PDF (default 300)")
    ap.add_argument("--max-pages", type=int, default=0, help="convert only the first N pages")
    ap.add_argument("--max-mb", type=float, default=0, help="skip PDFs larger than this")
    ap.add_argument("--markdown", action="store_true",
                    help="pymupdf4llm: Markdown headings, tables, bold (much slower)")
    ap.add_argument("--force", action="store_true", help="reconvert even if the .md is up to date")
    ap.add_argument("--retry-failed", action="store_true",
                    help="only retry PDFs that failed or timed out in earlier runs")
    a = ap.parse_args()

    inp, out = Path(a.inp).expanduser(), Path(a.out).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    cat_path = find_catalogue(inp, a.catalog)
    cat = load_catalogue(cat_path)
    print(f"catalogue: {cat_path} ({len(cat)} records)" if cat else "no HAL catalogue: PDF metadata only")

    status_file = out / "_status.jsonl"
    previous = {}
    if status_file.exists():
        for line in status_file.read_text(encoding="utf-8").splitlines():
            try:
                r = json.loads(line)
                previous[r["pdf"]] = r
            except (ValueError, KeyError):
                pass

    pdfs = sorted(p for p in inp.rglob("*") if p.suffix.lower() == ".pdf" and p.is_file())
    todo = []
    for p in pdfs:
        rel = p.relative_to(inp).as_posix()
        dest = out / Path(rel).with_suffix(".md")
        if a.retry_failed:
            if previous.get(rel, {}).get("status") in ("failed", "timeout"):
                todo.append((p, rel, dest))
            continue
        if not a.force and dest.exists() and dest.stat().st_mtime >= p.stat().st_mtime:
            continue
        if not a.force and previous.get(rel, {}).get("status") in ("failed", "timeout", "too-big") \
                and previous[rel].get("mtime") == int(p.stat().st_mtime):
            continue  # known bad, unchanged: use --retry-failed
        todo.append((p, rel, dest))
    print(f"{len(pdfs)} PDFs, {len(todo)} to convert, {a.workers} workers")

    def meta_for(p, rel):
        m = STEM.match(p.stem)
        meta = dict(cat.get(m.group("halid"), {})) if m else {}
        if m and not meta:
            meta = {"halId": m.group("halid"), "url": f"https://hal.science/{m.group('halid')}"}
        meta["source_pdf"] = rel
        return meta

    def work(item):
        p, rel, dest = item
        rec = {"pdf": rel, "md": dest.relative_to(out).as_posix(), "mtime": int(p.stat().st_mtime)}
        if a.max_mb and p.stat().st_size > a.max_mb * 1e6:
            return {**rec, "status": "too-big"}
        meta = meta_for(p, rel)
        rec.update(halId=meta.get("halId"), title=meta.get("title"), year=meta.get("year"))
        job = json.dumps({"pdf": str(p), "dest": str(dest), "meta": meta,
                          "markdown": a.markdown, "max_pages": a.max_pages})
        try:
            r = subprocess.run([sys.executable, "-I", str(HERE / "pdfs2md.py"), "--one", job],
                               capture_output=True, text=True, timeout=a.timeout)
        except subprocess.TimeoutExpired:
            return {**rec, "status": "timeout"}
        if r.returncode != 0:
            err = (r.stderr.strip().splitlines() or ["?"])[-1][:300]
            return {**rec, "status": "failed", "error": err}
        try:
            return {**rec, **json.loads(r.stdout.strip().splitlines()[-1])}
        except (ValueError, IndexError):
            return {**rec, "status": "failed", "error": r.stdout[-300:]}

    t0, done, counts = time.time(), 0, {}
    with status_file.open("a", encoding="utf-8") as log, ThreadPoolExecutor(a.workers) as ex:
        futures = [ex.submit(work, it) for it in todo]
        for f in as_completed(futures):
            r = f.result()
            previous[r["pdf"]] = r
            log.write(json.dumps(r, ensure_ascii=False) + "\n")
            log.flush()
            done += 1
            counts[r["status"]] = counts.get(r["status"], 0) + 1
            if done % 50 == 0 or done == len(todo):
                rate = done / max(1e-9, time.time() - t0)
                left = (len(todo) - done) / rate if rate else 0
                print(f"  {done}/{len(todo)}  {counts}  ~{left / 60:.0f} min left", flush=True)

    with (out / "INDEX.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["md", "halId", "year", "title", "pages", "status", "pdf"])
        for r in sorted(previous.values(), key=lambda r: r["pdf"]):
            w.writerow([r.get("md"), r.get("halId"), r.get("year"), r.get("title"),
                        r.get("pages"), r.get("status"), r["pdf"]])
    bad = [r for r in previous.values() if r.get("status") != "ok"]
    print(f"Done → {out}  ({len(previous) - len(bad)} ok, {len(bad)} not ok: see INDEX.csv)")


if __name__ == "__main__":
    main()
