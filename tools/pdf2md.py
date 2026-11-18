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


CONTROL = re.compile(r"[\x00-\x08\x0b-\x1f]")


def span_text(span, gmap):
    """Span text with font-specific glyph fixes; unknown control glyphs -> □."""
    m = gmap.get(span["font"]) or gmap.get(span["font"].split("+")[-1]) or {}
    text = "".join(m.get(c, c) for c in span["text"]) if m else span["text"]
    return CONTROL.sub("□", text)


def font_page(page, chap_sizes, sec_sizes, footer_y=None, tol=0.3, sub_sizes=(),
              gmap=None, regexes=(), code_fonts=(), code_lang="", drop=None):
    """Page text where lines set in heading font sizes become headings.

    For PDFs without bookmarks. Returns (text, [(level, title)]).
    Consecutive heading lines of the same level are merged.
    """
    out, heads = [], []
    gmap = gmap or {}
    pending = None  # (level, [parts])
    code = []  # (x0, char_width, text) of consecutive monospace lines

    def flush_code():
        if not code:
            return
        left = min(x for x, _, _ in code)
        body = [" " * max(0, round((x - left) / w)) + t for x, w, t in code]
        out.append(f"\n```{code_lang}\n" + "\n".join(body) + "\n```\n")
        code.clear()

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
            text = "".join(span_text(sp, gmap) for sp in l["spans"])
            if drop is not None and drop.search(text.strip()):
                continue
            if code_fonts and all(any(c in sp["font"] for c in code_fonts) for sp in spans):
                flush()
                first = spans[0]
                w = (first["bbox"][2] - first["bbox"][0]) / max(1, len(first["text"]))
                lead = len(first["text"]) - len(first["text"].lstrip(" "))
                code.append((first["bbox"][0] - lead * w, w or 1, text.strip()))
                continue
            flush_code()
            size = max(sp["size"] for sp in spans)
            level = 1 if any(abs(size - c) < tol for c in chap_sizes) else \
                2 if any(abs(size - c) < tol for c in sec_sizes) else 0
            # sub-sections: whole line bold, in one of the given sizes
            if not level and sub_sizes and all("Bold" in sp["font"] for sp in spans) \
                    and any(abs(spans[0]["size"] - c) < tol for c in sub_sizes):
                level = 3
            for lvl_re, rx in regexes:
                if rx.match(text.strip()):
                    level = lvl_re
                    text = re.sub(r"\s+", " ", text)
            # a title has words; big symbols and diagram labels do not
            if level and not (pending and pending[0] == level) \
                    and not re.search(r"[A-Za-zÀ-ÿ]{3,}", text) \
                    and not re.fullmatch(r"\s*\d+(\.\s*\d+)*\.?\s*", text):
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
    flush_code()
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


def build_chapters(doc, split_level=None, front_pages=0, toc=None):
    """Split the document by outline entries of the chapter level.

    Returns (chapters, toc, level): chapters are dicts {title, start, end}
    with 0-based inclusive pages. Falls back to fixed 25-page parts when the
    PDF has no outline.
    """
    n = doc.page_count
    toc = [e for e in (toc if toc is not None else doc.get_toc(simple=True)) if e[2] >= 1]
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


def split_large(chapters, toc, level, max_pages):
    """Split chapters longer than max_pages at the next outline level.

    Consecutive sub-sections are grouped while the group stays within
    max_pages; a sub-section that is itself too long is split further.
    """
    if not max_pages:
        return chapters
    out = []
    for ch in chapters:
        n = ch["end"] - ch["start"] + 1
        lvl = ch.get("level", level)
        kids = [(t.strip(), p - 1) for l, t, p in toc
                if l == lvl + 1 and ch["start"] <= p - 1 <= ch["end"]]
        uniq = []
        for t, p in kids:
            if not uniq or p > uniq[-1][1]:
                uniq.append((t, p))
        if n <= max_pages or len(uniq) < 2:
            out.append(ch)
            continue
        parts = []
        if uniq[0][1] > ch["start"]:
            parts.append({"title": ch["title"], "start": ch["start"], "end": uniq[0][1] - 1,
                          "level": lvl + 1, "short": ch.get("short", ch["title"]),
                          "root": ch.get("root", ch["title"])})
        for i, (t, p) in enumerate(uniq):
            end = uniq[i + 1][1] - 1 if i + 1 < len(uniq) else ch["end"]
            parts.append({"title": f"{ch['title']} — {t}", "start": p, "end": max(p, end),
                          "level": lvl + 1, "short": t, "root": ch.get("root", ch["title"])})
        # group small consecutive parts
        groups = []
        for part in parts:
            size = part["end"] - part["start"] + 1
            g = groups[-1] if groups else None
            if g and size <= max_pages and g["end"] - g["start"] + 1 + size <= max_pages \
                    and g.get("groupable") and part["start"] <= g["end"] + 1:
                g["end"] = part["end"]
                g["members"].append(part["short"])
                continue
            groups.append(dict(part, members=[part["short"]], groupable=size <= max_pages))
        for g in groups:
            if len(g["members"]) > 1:
                g["title"] = f"{ch['title']} — {g['members'][0]} … {g['members'][-1]}"
                g["short"] = g["members"][0]
            g.pop("groupable")
            g.pop("members")
        out.extend(split_large(groups, toc, level, max_pages))
    return out


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
    ap.add_argument("--heading-regex", action="append", default=[],
                    help="LEVEL:REGEX, lines matching REGEX become headings of LEVEL "
                         "(no-bookmarks mode), e.g. '2:^\\d+\\.\\d+\\.\\s+[A-Z ]+$'")
    ap.add_argument("--glyph-map",
                    help="JSON {font: {glyph: replacement}} fixing symbol fonts "
                         "(e.g. tools/glyphmaps/elsevier-advp.json)")
    ap.add_argument("--code-fonts", action="append", default=[],
                    help="font name fragment of code (e.g. Mono): such lines become fenced "
                         "code blocks with indentation rebuilt from their x-position")
    ap.add_argument("--code-lang", default="", help="language tag for those code blocks")
    ap.add_argument("--drop-regex", help="drop text lines matching this regex "
                                         "(e.g. 'continued from previous page')")
    ap.add_argument("--footer-y", type=float,
                    help="drop text lines starting below this y (page footers)")
    ap.add_argument("--page-offset", type=int, default=0,
                    help="printed page = PDF page + offset (used in page markers)")
    ap.add_argument("--max-pages", type=int, default=0,
                    help="split chapter files longer than this at the next outline level")
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
    gmap = json.loads(Path(args.glyph_map).read_text()) if args.glyph_map else {}
    regexes = [(int(r.split(":", 1)[0]), re.compile(r.split(":", 1)[1]))
               for r in args.heading_regex]
    drop = re.compile(args.drop_regex) if args.drop_regex else None
    fp_opts = dict(code_fonts=tuple(args.code_fonts), code_lang=args.code_lang, drop=drop)
    font_texts = {}
    synth_toc = None
    if chap_sizes:
        # build an outline from heading fonts, then reuse the normal splitting
        synth = []
        for i, page in enumerate(doc):
            text, heads = font_page(page, chap_sizes, sec_sizes, args.footer_y,
                                    sub_sizes=parse_sizes(args.subsection_sizes),
                                    gmap=gmap, regexes=regexes, **fp_opts)
            font_texts[i] = text
            synth += [[lvl, t, i + 1] for lvl, t in heads]
        synth_toc = synth
    elif gmap or args.code_fonts or drop:
        # bookmarks exist: font-aware text, headings inserted from the outline
        for i, page in enumerate(doc):
            font_texts[i] = None
    chapters, toc, level = build_chapters(doc, args.split_level, args.front_matter_pages,
                                          synth_toc)
    chapters = split_large(chapters, toc, level, args.max_pages)
    print(f"{doc.page_count} pages, {len(chapters)} chapter files (outline level {level})")

    page_to_file = {}
    for i, ch in enumerate(chapters):
        num = f"{i:02d}" if len(chapters) < 100 else f"{i:03d}"
        root, short = ch.get("root"), ch.get("short", ch["title"])
        if root and slugify(short) != slugify(root):
            root_slug = re.sub(r"^(the|a|an)-|-(module|chapter)$", "", slugify(root, 30))
            ch["file"] = f"{num}-{root_slug}--{slugify(short, 40)}.md"
        else:
            ch["file"] = f"{num}-{slugify(short)}.md"
        for p in range(ch["start"], ch["end"] + 1):
            page_to_file[p] = ch["file"]

    running = set() if args.markdown else find_running_lines(doc)
    heads_by_page = {}
    for lvl, title, page in toc:
        if lvl > level:  # chapter titles are the file's own "# " heading
            heads_by_page.setdefault(page - 1, []).append((lvl - level + 1, title))

    for ch in chapters:
        pages = range(ch["start"], ch["end"] + 1)
        if chap_sizes:  # headings already in place
            texts = {p: clean_text(font_texts[p], running, []) for p in pages}
        elif gmap or args.code_fonts or drop:
            texts = {p: clean_text(font_page(doc[p], [], [], args.footer_y, gmap=gmap, **fp_opts)[0],
                                   running, heads_by_page.get(p, []))
                     for p in pages}
        else:
            texts = page_texts(doc, pages, args.markdown, parse_pages(args.table_pages))
            if not args.markdown:
                texts = {p: clean_text(t, running, heads_by_page.get(p, []))
                         for p, t in texts.items()}
        parts = [f"# {ch['title']}\n",
                 f"<!-- source PDF pages {ch['start'] + 1}-{ch['end'] + 1} -->\n"]
        for p in pages:
            printed = doc[p].get_label() if not args.page_offset else str(p + 1 + args.page_offset)
            label = f"page {printed} (PDF {p + 1})" if printed else f"page {p + 1}"
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
        printed = str(page + args.page_offset) if args.page_offset else \
            (doc[page - 1].get_label() if 0 < page <= doc.page_count else "")
        where = f"p. {printed}, PDF {page}" if printed else f"p. {page}"
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
