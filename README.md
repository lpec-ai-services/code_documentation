# code_documentation

Documentation of simulation codes, packaged as **agent skills** for [opencode](https://opencode.ai/docs/skills) (they also work with Claude Code and any tool that reads `SKILL.md`).

Each code is one skill. The agent sees only the skill's name and description, and loads the skill (then reads its docs) when a question is about that code.

```
skills/
├── tripoli4/              # TRIPOLI-4® v12 user guide (CEA-R-6599, PDF)
│   ├── SKILL.md           # when to use + how to navigate + topic → chapter map
│   └── docs/              # generated: one .md per chapter, TOC.md, _meta.json
├── tripoli5/              # TRIPOLI-5® docs (tripoli5.asnr.dev, Sphinx site)
│   ├── SKILL.md
│   └── docs/              # generated: one .md per page, INDEX.md, _meta.json
├── valjean/               # VALJEAN V&V framework (github.com/valjean-framework/valjean)
│   ├── SKILL.md
│   └── docs/              # generated from the Sphinx sources + docstrings
├── neutronics/            # knowledge skill (not a code): physics vs simulation methods
│   ├── SKILL.md           # router: physics question or methods question?
│   ├── physics.md         # topic map: equations, criticality, kinetics, phenomena
│   ├── methods.md         # topic map: deterministic, Monte Carlo, depletion, kinetics solvers, schemes
│   ├── equations.md       # key equations in LaTeX, transcribed from the source pages
│   └── sources/           # one folder per document (generated text + TOC)
├── thermal-hydraulics/    # knowledge skill, same layout (water-cooled + fast reactors)
├── tfel-mfront/           # TFEL/MFront code skill (docs from the GitHub repo, exact LaTeX)
│   ├── SKILL.md, physics.md, methods.md
│   ├── docs/              # 266 pages + INDEX.md, release-notes/
│   └── examples/          # gallery .mfront / .mtest implementations
├── manta/                 # MANTA code skill (Sphinx site, user docs + demos, no Doxygen)
│   ├── SKILL.md, physics.md, methods.md
│   └── docs/              # 200 pages + INDEX.md
├── salome-medcoupling/    # MEDCoupling/MEDLoader: developer guide (with all snippets), user guide, tutorial
├── salome/                # SALOME 9.16 user docs, all modules: GUI, SHAPER, GEOM, SMESH + plug-ins, YACS, ADAO, HOMARD…
├── scivianna/             # CEA visualizer: AGENTS.md, tutorials, API (static), runnable examples
├── vtk/                   # VTK in Python: 900 examples (classic + Pythonic API), VTK Textbook, user docs
├── uranie/                # Uranie user manual (Python): modules + 985 runnable code blocks
├── icoco/                 # ICoCo v2 coupling norm (C++ header contract) + official Python implementation
└── c3po/                  # C3PO coupling platform: overview, code integration, API, example couplings
tools/
├── pdf2md.py              # PDF manual  → chapter Markdown + TOC (uses the PDF bookmarks)
├── sphinx2md.py           # published Sphinx site → page Markdown + INDEX (searchindex.js or a local copy; Doxygen HTML too)
├── salome_index.py        # top-level module index of the salome skill
├── sphinx_src2md.py       # Sphinx *sources* of a Python project → Markdown, API read with ast (no build, no import)
├── pdfbook2md.py          # book delivered as one PDF per chapter → one folder per chapter + book TOC
├── mdtree2md.py           # Markdown docs kept in a repo → skill docs + INDEX (links .html → .md)
├── dox2md.py              # hand-written Doxygen pages (.dox/.doc) → Markdown, \snippet resolved from sources
├── cppdoc2md.py           # Doxygen comments in C/C++ headers → Markdown API reference (no Doxygen needed)
├── glyphmaps/             # per-font symbol fixes for publisher PDFs (e.g. Elsevier AdvP fonts)
├── hal_harvest.py         # incremental harvester of HAL metadata + open-access PDFs (see below)
└── pdfs2md.py             # a whole folder of PDFs → one .md each (HAL metadata as front matter), resumable
templates/SKILL.md         # starting point for a new code
sync.sh                    # (re)generate docs/ for one or all codes
install.sh                 # symlink the skills into ~/.config/opencode/skills
```

## Setup

```bash
git clone https://github.com/lpec-ai-services/code_documentation
cd code_documentation
pip install -r requirements.txt     # + pandoc and git on PATH (used for valjean)

./sync.sh               # download + convert all docs (the TRIPOLI-4 PDF takes a few minutes)
./install.sh            # make the skills available to opencode globally
```

Check the result in opencode: ask "which skills do you have?" — `tripoli4`, `tripoli5` and `valjean` should be listed.

**Alternative to install.sh** (opencode v2): list the folder in your config instead of symlinking:

```json
{ "skills": ["~/path/to/code_documentation/skills"] }
```

**Per project only:** symlink or copy a skill into `<project>/.opencode/skills/<name>/`.

## Updating

- New TRIPOLI-5 release: `./sync.sh tripoli5` (or `T5_VERSION=v0.3.0 ./sync.sh tripoli5`, `T5_VERSION=dev …`).
  From a downloaded copy of the site (`wget -m -np https://tripoli5.asnr.dev/documentation/latest-release/`):
  `python3 tools/sphinx2md.py --base https://tripoli5.asnr.dev/documentation/latest-release/ --local tripoli5.asnr.dev/documentation/latest-release --out skills/tripoli5/docs`.
  Update the version line in `skills/tripoli5/SKILL.md`.
- New TRIPOLI-4 guide: update the URL in `sync.sh`, then `./sync.sh tripoli4`. From a local copy: `python3 tools/pdf2md.py --pdf guide.pdf --out skills/tripoli4/docs --front-matter-pages 20 --table-pages 552-562` (page options are specific to the v12 guide, so check them for a new edition).
- New SALOME version: the HTML docs shipped in a binary install (`…/BINARIES-*/DOCUMENTATION/share/doc/salome`, holding `gui/ dev/ main/`) or a wget mirror of `https://docs.salome-platform.org/latest/` (its `latest/` folder):
  `SALOME_DOC_DIR=/path/to/doc/salome SALOME_VERSION=9.16.0 ./sync.sh salome_docs`, then update the version in `skills/salome/SKILL.md`. Doxygen listing pages (file lists, member indexes, source listings) are skipped; class, namespace and group pages are kept. `./sync.sh salome` regenerates `salome-medcoupling` and `salome/docs/architecture` from GitHub.
- Commit the regenerated `docs/` so colleagues get them with a `git pull`, without having to sync themselves.

## Knowledge skills

`neutronics` and `thermal-hydraulics` are topic skills, not code skills. Its maps (`physics.md`, `methods.md`) and `equations.md` are written by hand, and only `sources/` is generated. To add a document: convert it with `tools/pdf2md.py` into `sources/<name>/` (PDFs without bookmarks: use `--chapter-sizes/--section-sizes`, the heading font sizes). Then add its topics to the maps. The source PDF is not stored here. Regenerate with `NEUTRONICS_METHODES_PDF=… NEUTRONICS_STACEY_PDF=… NEUTRONICS_MARGUET_PDF=… ./sync.sh neutronics` (each optional) and `TH_BOOK_DIR=… TH_IAEA_TRS498_PDF=… ./sync.sh thermal_hydraulics`.

Uranie: `URANIE_MANUAL_PDF=/path/to/userManual_Py.pdf ./sync.sh uranie`.

`pdf2md.py` options for difficult PDFs: `--code-fonts Mono` (monospace lines become fenced code with indentation rebuilt from x-positions), `--drop-regex` (repeated noise lines), `--header-y` + `--printed-pages` (books without page labels: running headers dropped, printed numbers read from them), `--glyph-map` (symbol fonts that decode to wrong characters; check against rendered pages before adding a font), `--max-pages` (split oversized sections), `--heading-regex` (headings not set in a distinct font). Undecodable symbols are written as "□".

## Harvesting HAL

`tools/hal_harvest.py` downloads HAL (hal.science) metadata and open-access PDFs through the public HAL API, into a folder **outside this repo** (it can reach terabytes). The catalogue is a SQLite file, so runs can be interrupted and resumed. Each later run fetches only what was added or modified since the previous complete run with the same filters.

```bash
# 1. size it first: nothing is saved
python3 tools/hal_harvest.py count --since 1900-01-01 --with-file

# 2. first run from a date (all of HAL with an open-access PDF)
python3 tools/hal_harvest.py run --out ~/hal --since 1900-01-01 --with-file --mailto you@lab.fr

# 3. later updates: run the same command again (only what changed is fetched)
python3 tools/hal_harvest.py run --out ~/hal --since 1900-01-01 --with-file --mailto you@lab.fr

# in batches: each invocation stops after ~5000 records, the next one continues
python3 tools/hal_harvest.py run --out ~/hal --since 1900-01-01 --with-file --max-docs 5000

# narrower scopes combine: --portal cea, --domain phys.nucl, --type THESE, --lang fr, --query '...'
python3 tools/hal_harvest.py stats  --out ~/hal
python3 tools/hal_harvest.py export --out ~/hal      # catalogue.jsonl (metadata + local PDF path)
```

- Dates filter `modifiedDate_tdate` by default, so new versions are caught. A new version is saved next to the old one (`<halId>v2.pdf`).
- `--rows` is only the page size of each API request. A run goes on page after page until the whole scope is harvested, and progress is saved after every page: an interrupted run (Ctrl-C, crash, `--max-docs`) continues when you run the same command again. `--restart` forces a fresh full pass (already downloaded PDFs are kept).
- `--no-pdf` harvests metadata only. The PDFs are fetched by a later run.
- Failed downloads are kept and retried with `--retry-failed`. Embargoed files are skipped.
- Defaults are polite: one request every 0.5 s and 2 download workers. Licences vary per document (`licence_s` in the catalogue).

### Converting the PDFs to Markdown

```bash
python3 tools/pdfs2md.py --in ~/hal/pdf --out ~/hal/md --workers 8
```

- One `.md` per PDF, same sub-folders. With the HAL catalogue (`hal.sqlite`, found next to the PDF folder or given with `--catalog`), each file starts with YAML front matter (title, authors, year, halId, DOI, URL, type, domains, keywords, licence) and the abstract. Without it, the PDF's own title/author are used, so it works on any folder of PDFs.
- Text keeps `<!-- page N -->` markers. Running headers/footers, ligatures and end-of-line hyphens are fixed.
- Re-running converts only new or changed PDFs: run it after each harvest. Each PDF has a time limit (`--timeout`, 300 s). Broken PDFs are listed, not fatal: `--retry-failed` tries them again.
- `INDEX.csv` lists every file with its status: `ok`, `no-text` (scanned PDF without a text layer, needs OCR), `failed`, `timeout`, `too-big` (`--max-mb`).
- `--markdown` uses pymupdf4llm for headings, tables and bold. It is much slower: try it on a sample first. `--max-pages N` keeps the first N pages (long theses).

## Adding a code

1. `mkdir -p skills/<name>/docs && cp templates/SKILL.md skills/<name>/`. The folder name must equal `name:` in the frontmatter.
2. Write the `description` carefully. It is the only thing the agent sees when choosing a skill, so put in the code name, its aliases, the main topics, and which other codes it must not be confused with.
3. Add a `sync_<name>()` function to `sync.sh`, using `tools/pdf2md.py` (PDF), `tools/sphinx2md.py` (published Sphinx site) or `tools/sphinx_src2md.py` (Python repo with Sphinx sources, see `sync_valjean`). Other formats (Doxygen, MkDocs, LaTeX) need a new converter in `tools/`. Plain Markdown docs can just be copied into `docs/`.
4. `./sync.sh <name> && ./install.sh`.

## Design notes

- **No vector database.** Agents search `docs/` with grep and read files directly, which is more precise for keyword and API lookups. If a code's docs become too large for that, add a search script inside its skill folder and mention it in `SKILL.md`. Nothing else has to change.
- **Not tied to a model.** Skills are plain Markdown, so any model used in opencode can use them.
- The converted documents remain the property of their authors (CEA, ASNR). Keep this repository's visibility consistent with their distribution terms.
