#!/usr/bin/env python3
"""Convert hand-written Doxygen pages (.dox / .doc files with \\page,
\\section, \\snippet, \\f$…\\f$ …) into agent-friendly Markdown.

- one .md per input file, same sub-folders
- \\page/\\section/\\subsection/\\subsubsection -> Markdown headings
- \\f$ x \\f$ -> $x$, \\f[ … \\f] -> $$ … $$ (LaTeX kept verbatim)
- \\code … \\endcode, \\verbatim … -> fenced code blocks
- \\snippet FILE TAG -> the code between the "[TAG]" markers of FILE,
  searched in the --snippets folders (Doxygen convention: //! [TAG] or # ! [TAG])
- \\ref ID "text" / \\subpage ID -> links to the file defining ID
- \\b \\c \\a \\em \\n \\li \\note \\warning \\image … -> Markdown equivalents
Also writes INDEX.md (pages and sections) and _meta.json.

Usage:
  python3 tools/dox2md.py --src doc/developer/doxygen/doxfiles --out skills/x/docs/developer \\
      --snippets src [--ext .dox --ext .doc] [--source-url URL]
"""
import argparse
import datetime as dt
import json
import re
from pathlib import Path

HEAD = {"mainpage": "#", "page": "#", "section": "##", "subsection": "###", "subsubsection": "####",
        "paragraph": "#####"}


def strip_comment(text):
    text = re.sub(r"/\*!|\*/", "", text)
    return re.sub(r"(?m)^\s?\* ?", "", text) if re.search(r"(?m)^\s\*", text) else text


def build_snippet_index(dirs):
    files = {}
    for d in dirs:
        for p in Path(d).rglob("*"):
            if p.is_file() and p.suffix in (".py", ".cxx", ".cpp", ".hxx", ".h", ".c", ".txt"):
                files.setdefault(p.name, p)
    return files


def snippet(files, name, tag):
    p = files.get(Path(name).name)
    if not p:
        return None
    lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
    marks = [i for i, l in enumerate(lines) if re.search(r"\[\s*" + re.escape(tag) + r"\s*\]", l)]
    if len(marks) < 2:
        return None
    body = [l for l in lines[marks[0] + 1:marks[1]]
            if not re.search(r"(//|#)\s*!\s*\[", l)]  # nested markers
    import textwrap
    return textwrap.dedent("\n".join(body)).strip("\n")


def collect_ids(text):
    """Page/section ids and titles, plus anchors."""
    ids = {}
    for kind, ident, title in re.findall(
            r"\\(page|section|subsection|subsubsection|paragraph)\s+(\S+)[ \t]*(.*)", text):
        ids[ident] = title.strip() or ident
    for ident in re.findall(r"\\anchor\s+(\S+)", text):
        ids.setdefault(ident, ident)
    return ids


def convert(text, here_rel, idmap, titles, snippets):
    keep = []

    def stash(s):
        keep.append(s)
        return f"\x00{len(keep) - 1}\x00"

    # code and math first, so their content is left untouched
    text = re.sub(r"\\code(?:\{\.?(\w+)\})?(.*?)\\endcode",
                  lambda m: stash(f"\n```{m.group(1) or ''}\n{m.group(2).strip(chr(10))}\n```\n"),
                  text, flags=re.S)
    text = re.sub(r"\\verbatim(.*?)\\endverbatim",
                  lambda m: stash(f"\n```\n{m.group(1).strip(chr(10))}\n```\n"), text, flags=re.S)

    def snip(m):
        name, tag = m.group(1), m.group(2)
        code = snippet(snippets, name, tag)
        lang = "python" if name.endswith(".py") else "cpp"
        if code is None:
            return stash(f"*(snippet {tag} from {name} not available)*")
        return stash(f"\n```{lang}\n{code}\n```\n")
    text = re.sub(r"\\snippet\s+(\S+)\s+(\S+)", snip, text)
    text = re.sub(r"\\f\[(.*?)\\f\]", lambda m: stash(f"\n$$\n{m.group(1).strip()}\n$$\n"),
                  text, flags=re.S)
    text = re.sub(r"\\f\$(.*?)\\f\$", lambda m: stash(f"${m.group(1).strip()}$"), text, flags=re.S)

    def link(ident, label=None):
        label = label or titles.get(ident, ident)
        target = idmap.get(ident)
        if not target:
            return label
        rel = Path(target).relative_to(Path(here_rel).parent) if Path(target).is_relative_to(
            Path(here_rel).parent) else Path("/") / target
        return f"[{label}]({rel.as_posix().lstrip('/')})"

    text = re.sub(r"\\(page|section|subsection|subsubsection|paragraph)\s+(\S+)[ \t]*(.*)",
                  lambda m: f"\n{HEAD[m.group(1)]} {m.group(3).strip() or m.group(2)}\n", text)
    text = re.sub(r"\\mainpage[ \t]*(.*)", lambda m: f"\n# {m.group(1).strip()}\n", text)
    text = re.sub(r"(?<![\w%])%(\w)", r"\1", text)  # Doxygen auto-link suppressor
    text = re.sub(r"\\subpage\s+(\S+)", lambda m: link(m.group(1)), text)
    text = re.sub(r'\\ref\s+(\S+?)\s+"([^"]*)"', lambda m: link(m.group(1), m.group(2)), text)
    text = re.sub(r"\\ref\s+([\w:.-]+)", lambda m: link(m.group(1)), text)
    text = re.sub(r"\\anchor\s+\S+", "", text)
    text = re.sub(r"\\image\s+html\s+(\S+)(?:\s+\"([^\"]*)\")?",
                  lambda m: f"*(figure: {m.group(2) or m.group(1)})*", text)
    text = re.sub(r"\\image\s+latex\s+\S+.*", "", text)
    text = re.sub(r"\\(b)\s+(\S+)", r"**\2**", text)
    text = re.sub(r"\\(c|p)\s+(\S+)", r"`\2`", text)
    text = re.sub(r"\\(a|e|em)\s+(\S+)", r"*\2*", text)
    text = re.sub(r"\\n\b", "  \n", text)
    text = re.sub(r"(?m)^(\s*)\\li\s+", r"\1- ", text)
    text = re.sub(r"\\(note|warning|remark|attention)\b", lambda m: f"\n> **{m.group(1).capitalize()}:**", text)
    text = re.sub(r"\\(if|ifnot|elseif)\s+\S+|\\(endif|else|cond|endcond|internal|endinternal)\b",
                  "", text)
    text = re.sub(r"\\(brief|details)\s*", "", text)
    text = re.sub(r"<br\s*/?>", "  \n", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], text)
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--snippets", action="append", default=[],
                    help="folder searched for \\snippet files (repeatable)")
    ap.add_argument("--ext", action="append", default=[], help="default: .dox and .doc")
    ap.add_argument("--source-url", default="")
    ap.add_argument("--version", default="")
    args = ap.parse_args()

    src, out = Path(args.src), Path(args.out)
    exts = tuple(args.ext or [".dox", ".doc"])
    files = sorted(p for p in src.rglob("*") if p.suffix in exts)
    raw = {p: strip_comment(p.read_text(encoding="utf-8", errors="replace")) for p in files}
    idmap, titles = {}, {}
    for p, t in raw.items():
        rel = p.relative_to(src).with_suffix(".md").as_posix()
        for ident, title in collect_ids(t).items():
            idmap.setdefault(ident, rel)
            titles.setdefault(ident, title)
    snippets = build_snippet_index(args.snippets)

    out.mkdir(parents=True, exist_ok=True)
    for old in out.rglob("*.md"):
        old.unlink()
    index, missing = [], 0
    for p, t in raw.items():
        rel = p.relative_to(src).with_suffix(".md").as_posix()
        md = convert(t, rel, idmap, titles, snippets)
        missing += md.count("not available)*")
        dest = out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(f"<!-- source: {p.relative_to(src).as_posix()} -->\n\n{md}", encoding="utf-8")
        heads = re.findall(r"(?m)^(#{1,3}) (.+)$", re.sub(r"```.*?```", "", md, flags=re.S))
        index.append((rel, [h for _, h in heads], len(md)))

    lines = ["# Index of pages\n", "Each entry: file — its page title(s) and sections.\n"]
    for rel, heads, size in sorted(index):
        lines.append(f"- `{rel}` — **{heads[0] if heads else rel}** ({max(1, size // 1000)} kB)")
        if len(heads) > 1:
            more = f" … (+{len(heads) - 11})" if len(heads) > 11 else ""
            lines.append(f"  - {' · '.join(heads[1:11])}{more}")
    (out / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (out / "_meta.json").write_text(json.dumps(
        {"source": args.source_url or str(src), "version": args.version,
         "generated": dt.date.today().isoformat(), "pages": len(index)}, indent=2))
    print(f"{len(index)} pages → {out} ({missing} snippets not found)")


if __name__ == "__main__":
    main()
