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
└── neutronics/            # knowledge skill (not a code): physics vs simulation methods
    ├── SKILL.md           # router: physics question or methods question?
    ├── physics.md         # topic map: equations, criticality, kinetics, phenomena
    ├── methods.md         # topic map: deterministic, Monte Carlo, depletion, kinetics solvers, schemes
    ├── equations.md       # key equations in LaTeX, transcribed from the source pages
    └── sources/           # one folder per document (generated text + TOC)
tools/
├── pdf2md.py              # PDF manual  → chapter Markdown + TOC (uses the PDF bookmarks)
├── sphinx2md.py           # published Sphinx site → page Markdown + INDEX (searchindex.js or a local copy)
└── sphinx_src2md.py       # Sphinx *sources* of a Python project → Markdown, API read with ast (no build, no import)
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
- Commit the regenerated `docs/` so colleagues get them with a `git pull`, without having to sync themselves.

## Knowledge skills

`neutronics` is a topic skill, not a code skill. Its maps (`physics.md`, `methods.md`) and `equations.md` are written by hand, and only `sources/` is generated. To add a document: convert it with `tools/pdf2md.py` into `sources/<name>/` (PDFs without bookmarks: use `--chapter-sizes/--section-sizes`, the heading font sizes). Then add its topics to the maps. The source PDF is not stored here. Regenerate with `NEUTRONICS_METHODES_PDF=/path/to.pdf ./sync.sh neutronics`.

## Adding a code

1. `mkdir -p skills/<name>/docs && cp templates/SKILL.md skills/<name>/`. The folder name must equal `name:` in the frontmatter.
2. Write the `description` carefully. It is the only thing the agent sees when choosing a skill, so put in the code name, its aliases, the main topics, and which other codes it must not be confused with.
3. Add a `sync_<name>()` function to `sync.sh`, using `tools/pdf2md.py` (PDF), `tools/sphinx2md.py` (published Sphinx site) or `tools/sphinx_src2md.py` (Python repo with Sphinx sources, see `sync_valjean`). Other formats (Doxygen, MkDocs, LaTeX) need a new converter in `tools/`. Plain Markdown docs can just be copied into `docs/`.
4. `./sync.sh <name> && ./install.sh`.

## Design notes

- **No vector database.** Agents search `docs/` with grep and read files directly, which is more precise for keyword and API lookups. If a code's docs become too large for that, add a search script inside its skill folder and mention it in `SKILL.md`. Nothing else has to change.
- **Not tied to a model.** Skills are plain Markdown, so any model used in opencode can use them.
- The converted documents remain the property of their authors (CEA, ASNR). Keep this repository's visibility consistent with their distribution terms.
