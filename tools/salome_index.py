#!/usr/bin/env python3
"""Write the top-level INDEX.md of the salome skill: one line per module
folder (pages, size, title of its index page), pointing to each folder's own
INDEX.md. Run by sync.sh after the modules are converted."""
import argparse
import datetime as dt
import json
import re
from pathlib import Path

LABELS = {
    "GUI": "SALOME desktop (GUI module)", "SHAPER": "SHAPER — parametric CAD",
    "GEOM": "GEOM — geometry", "SMESH": "SMESH — mesh",
    "NETGENPLUGIN": "Netgen meshing plug-in", "BLSURFPLUGIN": "MG-CADSurf plug-in",
    "GHS3DPLUGIN": "MG-Tetra plug-in", "HexoticPLUGIN": "MG-Hexa plug-in",
    "HYBRIDPLUGIN": "MG-Hybrid plug-in", "GMSHPLUGIN": "Gmsh plug-in",
    "YACS": "YACS — workflows / supervision", "HEXABLOCK": "HexaBlock — block meshing",
    "EFICAS": "EFICAS — data-set editor", "JOBMANAGER": "JobManager — remote jobs",
    "HOMARD": "HOMARD — mesh adaptation", "ADAO": "ADAO — data assimilation / optimization",
    "HELLO": "HELLO sample module (C++)", "PYHELLO": "PYHELLO sample module (Python)",
    "dev/FIELDS": "FIELDS — MED fields module", "dev/PARAVIS": "PARAVIS — ParaView in SALOME",
    "dev/cmake": "CMake build procedure for modules", "dev/git": "Git workflow for SALOME",
    "main": "Documentation portal", "architecture": "GUI architecture (developer notes)",
}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--docs", required=True)
    ap.add_argument("--version", default="")
    a = ap.parse_args()
    docs = Path(a.docs)
    rows = []
    for key in LABELS:
        d = docs / key
        if not d.is_dir():
            continue
        pages = [p for p in d.rglob("*.md") if p.name != "INDEX.md"]
        kb = sum(p.stat().st_size for p in pages) // 1000
        rows.append(f"| `{key}/` | {LABELS[key]} | {len(pages)} | {kb} kB |")
    lines = ["# SALOME documentation — modules\n",
             f"SALOME {a.version}. Each folder has its own `INDEX.md` "
             "(every page with its title and headings).\n",
             "| Folder | Module | Pages | Size |", "|---|---|---|---|", *rows]
    (docs / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (docs / "_meta.json").write_text(json.dumps(
        {"source": "https://docs.salome-platform.org/latest/", "version": a.version,
         "generated": dt.date.today().isoformat()}, indent=2), encoding="utf-8")
    print("\n".join(rows))


if __name__ == "__main__":
    main()
