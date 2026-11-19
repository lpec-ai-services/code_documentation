#!/usr/bin/env python3
"""Turn Doxygen comments in C/C++ headers into a Markdown API reference,
without running Doxygen.

For every documentation comment (/*! … */, /** … */, or a run of ///, //!
lines) the following declaration (up to ';' or '{') is taken as its
signature. Classes and namespaces become headings; @brief, @param,
@return, @throws, @warning, @note, @pre are rendered as Markdown.
Comments that are not followed by a declaration (file or group notes) are
kept as plain text. One .md per header, plus INDEX.md.

Usage:
  python3 tools/cppdoc2md.py --src include --out skills/x/docs/api [--glob '*.hxx']
"""
import argparse
import datetime as dt
import json
import re
from pathlib import Path

# block comments /*! … */ or /** … */, or runs of /// or //! lines; "<" forms
# (///< trailing member docs) are skipped
DOC = re.compile(r"/\*[!*](?![/<])(.*?)\*/|((?:^[ \t]*//[/!](?![/<])[^\n]*\n)+)", re.S | re.M)


def clean_comment(raw):
    lines = []
    for l in raw.splitlines():
        l = re.sub(r"^\s*(//[/!]|\*(?!/))?\s?", "", l)
        lines.append(l.rstrip())
    return "\n".join(lines).strip()


def render_doc(text):
    text = re.sub(r"[@\\]brief\s*", "", text)
    text = re.sub(r"(?m)^[@\\]param(?:\[[a-z,]+\])?\s+(\w+)\s*", r"- **\1**: ", text)
    text = re.sub(r"(?m)^[@\\](?:return|returns)\s*", "**Returns:** ", text)
    text = re.sub(r"(?m)^[@\\](?:throws?|exception)\s+(\S+)\s*", r"**Throws** `\1`: ", text)
    text = re.sub(r"(?m)^[@\\](warning|note|pre|post|remark|see|sa)\b\s*",
                  lambda m: f"**{m.group(1).capitalize()}:** ", text)
    text = re.sub(r"[@\\]c\s+(\S+)", r"`\1`", text)
    text = re.sub(r"[@\\](?:b)\s+(\S+)", r"**\1**", text)
    text = re.sub(r"[@\\](?:a|e|em)\s+(\S+)", r"*\1*", text)
    text = re.sub(r"[@\\](?:ref)\s+(\S+)", r"`\1`", text)
    text = re.sub(r"</?code>", "`", text)
    # keep each tagged item on its own line in Markdown
    text = re.sub(r"\n(?=- \*\*|\*\*(Returns|Throws|Warning|Note|Pre|Post|Remark|See|Sa)\b)", "\n\n", text)
    return text.strip()


def next_declaration(src, pos):
    """Declaration text following a comment, or '' if another comment/blank block comes first."""
    rest = src[pos:]
    m = re.match(r"\s*", rest)
    rest = rest[m.end():]
    if rest.startswith(("/*", "//", "#")) or not rest:
        return ""
    end = min([i for i in (rest.find(";"), rest.find("{")) if i >= 0] or [len(rest)])
    decl = rest[:end].strip()
    return re.sub(r"\s+", " ", decl)


def heading_for(decl):
    if re.match(r"(class|struct)\s+\w+", decl.replace("ICOCO_EXPORT ", "")):
        name = re.search(r"(class|struct)\s+(?:\w+_EXPORT\s+)?(\w+)", decl).group(2)
        return f"## {decl.split()[0]} `{name}`", decl
    if decl.startswith("namespace"):
        return f"## namespace `{decl.split()[1]}`", None
    return None, decl


def convert(path):
    src = path.read_text(encoding="utf-8", errors="replace")
    out = [f"# `{path.name}`\n"]
    for m in DOC.finditer(src):
        body = clean_comment(m.group(1) if m.group(1) is not None else m.group(2))
        if not body or body.startswith("@{") or body.startswith("@}"):
            continue
        decl = next_declaration(src, m.end())
        head, sig = heading_for(decl) if decl else (None, None)
        if head:
            out.append(f"\n{head}\n")
            if sig:
                out.append(f"```cpp\n{sig}\n```\n")
        elif sig:
            name = re.search(r"([~\w:]+)\s*\(", sig)
            out.append(f"\n### `{name.group(1) if name else sig[:60]}`\n")
            out.append(f"```cpp\n{sig};\n```\n")
        out.append(render_doc(body) + "\n")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--glob", action="append", default=[], help="default: *.hxx, *.hpp, *.h")
    ap.add_argument("--source-url", default="")
    ap.add_argument("--version", default="")
    a = ap.parse_args()
    src, out = Path(a.src), Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    files = sorted({p for g in (a.glob or ["*.hxx", "*.hpp", "*.h"]) for p in src.rglob(g)})
    index = ["# API reference (from header comments)\n"]
    for p in files:
        md = convert(p)
        n = md.count("\n### ")
        if n == 0 and md.count("\n## ") == 0:
            continue  # no documented declarations
        dest = out / p.relative_to(src).with_suffix(".md")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(md, encoding="utf-8")
        names = re.findall(r"(?m)^### `([^`]+)`", md)
        index.append(f"- `{dest.relative_to(out).as_posix()}` — {n} documented members: "
                     + ", ".join(names[:40]) + (" …" if len(names) > 40 else ""))
    (out / "INDEX.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    (out / "_meta.json").write_text(json.dumps({"source": a.source_url or str(src), "version": a.version,
                                                "generated": dt.date.today().isoformat()}, indent=2))
    print(f"{len(index) - 1} headers → {out}")


if __name__ == "__main__":
    main()
