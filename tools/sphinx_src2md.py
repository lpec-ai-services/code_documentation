#!/usr/bin/env python3
"""Convert Sphinx *sources* of a Python project to agent-friendly Markdown,
without building the docs and without importing or running the project.

- .rst pages  -> Markdown with pandoc
- .ipynb      -> Markdown with pandoc (code cells and any stored outputs)
- `.. automodule:: pkg.mod` -> replaced by the module's API, read statically
  with `ast` from the source files: module docstring, public classes
  (signature, docstring, methods) and functions. Docstrings (reST) are
  converted with pandoc too.
Also writes INDEX.md (pages, titles, headings) and _meta.json.

Usage:
  python3 tools/sphinx_src2md.py --src repo/doc/src --pkg-root repo \
      --out skills/foo/docs [--source-url https://...] [--version X.Y]
Requires: pandoc on PATH.
"""
import argparse
import ast
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

MARK = "PANDOCSPLITMARKERZQX"
DROP_DIRECTIVES = ("figure", "image", "todolist", "only", "highlight")


def pandoc(text, fmt="rst", shift=0):
    cmd = ["pandoc", "-f", fmt, "-t", "gfm", "--wrap=none"]
    if shift:
        cmd.append(f"--shift-heading-level-by={shift}")
    r = subprocess.run(cmd, input=text, capture_output=True, text=True)
    if r.returncode != 0:
        return text  # keep the raw source rather than lose it
    return r.stdout


def strip_directives(rst, names):
    """Remove `.. name::` directives together with their indented body."""
    out, skip = [], False
    for line in rst.splitlines():
        if re.match(r"\.\. (%s)::" % "|".join(names), line):
            skip = True
            continue
        if skip and (line.startswith((" ", "\t")) or not line.strip()):
            continue
        skip = False
        out.append(line)
    return "\n".join(out)


def inline_literalincludes(rst, here):
    """`.. literalinclude:: file` -> code block with the file's content.

    Supports :start-after:, :end-before:, :lines: and :language:. Paths are
    relative to the .rst file; files that cannot be found are left as a note.
    """
    out, lines, i = [], rst.splitlines(), 0
    while i < len(lines):
        m = re.match(r"(\s*)\.\. literalinclude::\s*(\S+)", lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        indent, target = m.group(1), m.group(2)
        opts, i = {}, i + 1
        while i < len(lines) and re.match(r"\s+:([\w-]+):\s*(.*)", lines[i]):
            k, v = re.match(r"\s+:([\w-]+):\s*(.*)", lines[i]).groups()
            opts[k] = v.strip()
            i += 1
        path = (here / target).resolve()
        lang = opts.get("language") or {"py": "python", "cxx": "cpp", "cpp": "cpp",
                                        "c": "c", "h": "cpp"}.get(path.suffix[1:], "")
        if not path.exists():
            out += ["", f"{indent}*(code from {target} not available)*", ""]
            continue
        src = path.read_text(encoding="utf-8", errors="replace").splitlines()
        missing = None
        if "start-after" in opts:
            k = next((n for n, l in enumerate(src) if opts["start-after"] in l), None)
            if k is None:
                missing = opts["start-after"]
            src = src[k + 1:] if k is not None else []
        if "end-before" in opts and src:
            k = next((n for n, l in enumerate(src) if opts["end-before"] in l), None)
            src = src[:k] if k is not None else src
        if missing:
            out += ["", f"{indent}(example ``{missing}`` not found in {path.name}: "
                        "broken reference in the upstream docs)", ""]
            continue
        if "lines" in opts:
            keep = set()
            for part in opts["lines"].split(","):
                a, _, b = part.partition("-")
                keep.update(range(int(a), int(b or a) + 1))
            src = [l for n, l in enumerate(src, 1) if n in keep]
        while src and not src[0].strip():
            src.pop(0)
        while src and not src[-1].strip():
            src.pop()
        import textwrap
        body = textwrap.dedent("\n".join(src)).splitlines()
        out += ["", f"{indent}.. code-block:: {lang or 'text'}", ""]
        out += [f"{indent}   {l}" if l.strip() else "" for l in body] + [""]
    return "\n".join(out)


def toctrees_to_lists(rst):
    """`.. toctree::` -> bullet list of links to the converted pages."""
    out, inside = [], False
    for line in rst.splitlines():
        if re.match(r"\.\. toctree::", line):
            inside = True
            out.append("")
            continue
        if inside:
            entry = line.strip()
            if not line.strip():
                continue
            if line.startswith((" ", "\t")):
                if not entry.startswith(":"):
                    m = re.match(r"(.+?)\s*<(.+)>$", entry)
                    label, target = (m.group(1), m.group(2)) if m else (entry, entry)
                    out.append(f"- `{label}` (`{target}.md`)")
                continue
            inside = False
            out.append("")
        out.append(line)
    return "\n".join(out)


def roles_to_literals(rst):
    """:class:`~a.b.C` / :func:`x <a.b>` -> ``C`` / ``x`` (pandoc drops roles)."""
    def repl(m):
        target = m.group(2)
        label = re.match(r"(.+?)\s*<.+>$", target)
        text = label.group(1) if label else target.lstrip("~!")
        if target.startswith("~"):
            text = text.split(".")[-1]
        return f"``{text}``"
    rst = re.sub(r":(?:py:)?(\w+):`([^`]+)`", repl, rst)
    # default role `x` (not ``x``, not a `link <url>`_) -> ``x``
    return re.sub(r"(?<![`\w])`([^`\n<]+)`(?![`_\w])", r"``\1``", rst)


# ---------------------------------------------------------------- API (ast)

def module_file(pkg_root, modname):
    base = Path(pkg_root, *modname.split("."))
    for cand in (base.with_suffix(".py"), base / "__init__.py"):
        if cand.exists():
            return cand
    return None


def signature(node):
    args = ast.unparse(node.args)
    ret = f" -> {ast.unparse(node.returns)}" if node.returns else ""
    return f"({args}){ret}"


def public(name):
    return not name.startswith("_") or name == "__init__"


def module_api(pkg_root, modname, undoc):
    """List of (kind, heading, docstring) for a module, read with ast."""
    f = module_file(pkg_root, modname)
    if f is None:
        return [("missing", f"module {modname} not found", "")]
    tree = ast.parse(f.read_text(encoding="utf-8"), filename=str(f))
    items = [("module", modname, ast.get_docstring(tree) or "")]
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and public(node.name):
            init = next((n for n in node.body if isinstance(n, ast.FunctionDef)
                         and n.name == "__init__"), None)
            sig = signature(init).replace("(self, ", "(").replace("(self)", "()") \
                if init else ""
            bases = ", ".join(ast.unparse(b) for b in node.bases)
            doc = ast.get_docstring(node) or ""
            if doc or undoc:
                head = f"class {modname}.{node.name}{sig}" + \
                       (f"  — bases: {bases}" if bases else "")
                items.append(("class", head, doc))
            for m in node.body:
                if isinstance(m, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                        and public(m.name) and m.name != "__init__":
                    mdoc = ast.get_docstring(m) or ""
                    if mdoc or undoc:
                        deco = [ast.unparse(d) for d in m.decorator_list]
                        kind = "property" if "property" in deco else "method"
                        s = "" if kind == "property" else signature(m)
                        items.append((kind, f"{node.name}.{m.name}{s}", mdoc))
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                and public(node.name):
            doc = ast.get_docstring(node) or ""
            if doc or undoc:
                items.append(("function", f"{modname}.{node.name}{signature(node)}", doc))
    return items


def api_markdown(pkg_root, modname, undoc):
    items = module_api(pkg_root, modname, undoc)
    # convert every docstring in one pandoc call
    docs = [roles_to_literals(d) for _, _, d in items]
    joined = f"\n\n{MARK}\n\n".join(docs)
    conv = pandoc(joined, shift=1).split(MARK)
    if len(conv) != len(items):  # fall back to raw docstrings
        conv = docs
    out = []
    for (kind, head, _), body in zip(items, conv):
        body = body.strip()
        if kind == "module":
            out.append(body)
        elif kind == "missing":
            out.append(f"*({head})*")
        else:
            level = "###" if kind in ("class", "function") else "####"
            out.append(f"{level} `{head}`\n\n{body}" if body else f"{level} `{head}`")
    return "\n\n".join(x for x in out if x)


# ---------------------------------------------------------------- pages

def take_md_includes(rst, here):
    """`.. include:: file.md` (MyST parser) -> placeholder; returns (rst, [markdown])."""
    found = []

    def repl(m):
        target = (here / m.group(1)).resolve()
        found.append(target.read_text(encoding="utf-8", errors="replace")
                     if target.exists() else f"*(included file {m.group(1)} not available)*")
        return f"\nINCLUDEDMARKDOWNZQX{len(found) - 1}\n"
    rst = re.sub(r"^\.\. include:: *(\S+\.md)\n((?:[ \t]+.*\n|[ \t]*\n)*)", repl,
                 rst + "\n", flags=re.M)
    return rst, found


def convert_rst(path, pkg_root):
    rst = path.read_text(encoding="utf-8")
    rst, md_includes = take_md_includes(rst, path.parent)
    rst = inline_literalincludes(rst, path.parent)
    rst = toctrees_to_lists(strip_directives(rst, DROP_DIRECTIVES))
    autos = []

    def take(m):
        autos.append((m.group(1).strip(), ":undoc-members:" in m.group(0)))
        return f"\n{MARK}{len(autos) - 1}\n"
    rst = re.sub(r"^\.\. automodule:: *(\S+)\n((?:[ \t]+.*\n|[ \t]*\n)*)",
                 take, rst + "\n", flags=re.M)
    md = pandoc(roles_to_literals(rst))
    for i, (mod, undoc) in enumerate(autos):
        md = md.replace(f"{MARK}{i}", api_markdown(pkg_root, mod, undoc), 1)
    for i, text in enumerate(md_includes):
        md = md.replace(f"INCLUDEDMARKDOWNZQX{i}", text.strip(), 1)
    return md


def convert_ipynb(path):
    return pandoc(path.read_text(encoding="utf-8"), fmt="ipynb")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True, help="Sphinx source dir (has conf.py)")
    ap.add_argument("--pkg-root", required=True,
                    help="directory containing the Python package(s)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--exclude", action="append", default=[],
                    help="glob of source pages to skip, relative to --src (repeatable)")
    ap.add_argument("--source-url", default="", help="recorded in _meta.json")
    ap.add_argument("--version", default="", help="recorded in _meta.json")
    args = ap.parse_args()

    src, out = Path(args.src), Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for old in out.rglob("*.md"):
        old.unlink()

    pages = sorted(p for p in src.rglob("*")
                   if p.suffix in (".rst", ".ipynb", ".md")
                   and ".ipynb_checkpoints" not in p.parts
                   and not any(p.relative_to(src).match(g) for g in args.exclude))
    index = []
    for p in pages:
        rel = p.relative_to(src).with_suffix(".md")
        if p.suffix == ".rst":
            md = convert_rst(p, args.pkg_root)
        elif p.suffix == ".ipynb":
            md = convert_ipynb(p)
        else:
            md = p.read_text(encoding="utf-8")
        md = re.sub(r"(?m)^</?div[^>]*>\n?", "", md)  # notebook cell wrappers
        md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
        dest = out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(f"<!-- source: {p.relative_to(src).as_posix()} -->\n\n{md}",
                        encoding="utf-8")
        heads = re.findall(r"(?m)^(#{1,3}) (.+)$", md)
        title = next((h for l, h in heads if len(l) == 1), rel.stem)
        subs = [h.strip("`") for l, h in heads if len(l) > 1]
        index.append((rel.as_posix(), title, subs, len(md)))
        print(f"  {rel}")

    lines = ["# Index of pages\n", "Each entry: file — title, then its main headings.\n"]
    current = None
    def top_of(f):
        return f.split("/")[0] if "/" in f else "(root)"
    for f, title, subs, size in sorted(index, key=lambda i: (top_of(i[0]) != "(root)",
                                                              top_of(i[0]), i[0])):
        top = top_of(f)
        if top != current:
            lines.append(f"\n## {top}\n")
            current = top
        lines.append(f"- `{f}` — **{title}** ({max(1, size // 1000)} kB)")
        if subs:
            more = f" … (+{len(subs) - 10})" if len(subs) > 10 else ""
            lines.append(f"  - {' · '.join(subs[:10])}{more}")
    (out / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    meta = {"source": args.source_url or str(src), "version": args.version,
            "generated": dt.date.today().isoformat(), "pages": [i[0] for i in index]}
    (out / "_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Done → {out} ({len(index)} pages)")


if __name__ == "__main__":
    sys.exit(main())
