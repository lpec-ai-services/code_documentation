---
name: thermal-hydraulics
description: Nuclear reactor thermal-hydraulics knowledge base, split into PHYSICS (single- and two-phase flow, void fraction/quality/slip, flow regimes, heat conduction, convection, boiling, CHF/DNB/dryout, condensation, pressure drops, critical/choked flow, CCFL, reflood, natural circulation, stratification, accident phenomena — LOCA, SBO, SGTR, MSLB, RIA, TMI/Chernobyl/Fukushima —, liquid-metal and fast-reactor coolants) and SIMULATION METHODS (balance equations, two-fluid 6-equation, HEM and drift-flux models, constitutive/closure laws, flow regime maps, system codes RELAP5/CATHARE/TRACE and nodalization, subchannel, CFD, multiscale/multiphysics coupling, V&V, scaling, uncertainty and BEPU, safety analysis). Water-cooled reactors and fast reactors (sodium, lead, LBE, helium, molten salt). Use for conceptual, theoretical or methodological questions independent of a specific code input.
---

# Thermal-hydraulics: physics and simulation methods

This skill has two branches. First decide which one the question belongs to:

| The question is about… | Branch | Open |
|---|---|---|
| **What happens and why.** Flow and heat-transfer phenomena, two-phase parameters, boiling crisis, pressure drops, critical flow, accident phenomenology, coolant properties | **Physics** | `physics.md` |
| **How it is computed.** Equation systems and averaging, closure laws in codes, system codes and nodalization, subchannel, CFD, coupling, V&V, scaling, uncertainty / BEPU | **Methods** | `methods.md` |

Correlations sit on the boundary. Their physical basis and data are in the physics branch (heat transfer, pressure drops). How codes use them as closure laws (flow-regime maps, interfacial and wall terms) is in the methods branch.

## Files

- `physics.md` / `methods.md`: topic → source folder/file → printed page, plus what each source covers.
- `equations.md`: key equations in LaTeX, transcribed from the source pages. **Use this for equations.** In the extracted text, display equations are broken across lines.
- `sources/<document>/`: full text of each source. Each has a `TOC.md` (section → file → printed page). Each chapter folder of the book has its own `TOC.md`.

## Sources

| Key | Folder | Document | Scope |
|---|---|---|---|
| **B** | `sources/th-water-cooled-reactors-2017/` | *Thermal Hydraulics of Water-Cooled Nuclear Reactors*, F. D'Auria (ed.), Woodhead/Elsevier, 2017. 16 chapters, ~1150 pages. Folders `NN-…` = chapter NN; `subject-index/` = the book's index | LWR, VVER, BWR, SCWR; two-phase flow; system codes; safety |
| **F** | `sources/iaea-trs-498-fast-reactors/` | IAEA Technical Reports Series No. 498, *Review of State of the Art Thermal Hydraulics of Fast Reactors* (2026), 11 chapters | Fast reactors: Na, Pb/LBE, He, chloride salt; liquid-metal heat transfer; pool TH; CFD, coupling, VVUQ, licensing |

## How to answer

1. Pick the branch, then find the topic in its map. Otherwise grep `sources/` for English terms (`dryout`, `drift flux`, `CCFL`, `reflood`, `Prandtl`). The book's `subject-index/` lists printed pages for most terms.
2. Read the passage. In the text, "□" marks a symbol that could not be decoded, and display equations are split across lines. Take formulas from `equations.md`, or say they're not transcribed and cite the page.
3. Cite the source and its **printed page** (`<!-- page N (PDF M) -->` markers give both), e.g. "(D'Auria 2017, p. 226)" or "(IAEA TRS-498, p. 29)".
4. Water vs liquid metal: don't carry water correlations or two-phase concepts over to sodium or lead without saying so. Liquid metals have low Prandtl numbers, and F §3 discusses why the usual correlations and turbulence models fail.
5. Point to related skills. Neutronics feedback and coupled physics are in `neutronics`. Comparing code results to experiments (V&V statistics) is in `valjean`.

## Adding a document

A book delivered as one PDF per chapter: `tools/pdfbook2md.py`. A single PDF: `tools/pdf2md.py`. If it has no bookmarks, add `--chapter-sizes`, `--section-sizes` and `--heading-regex`. For Elsevier symbol fonts, add `--glyph-map tools/glyphmaps/elsevier-advp.json`. See `sync.sh` (`sync_thermal_hydraulics`). Then add the document to the Sources table and its topics to the maps.
