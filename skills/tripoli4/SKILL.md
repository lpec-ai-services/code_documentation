---
name: tripoli4
description: TRIPOLI-4® (version 12) Monte Carlo particle transport code from CEA — user guide CEA-R-6599. Use for any question about TRIPOLI-4 / T4 input files (keyword data sets), geometry (combinatorial or surface-based, lattices, SMASH/VMINUS operators), compositions, sources, responses, scores, variance reduction (INIPOND, AMS, weight windows, CADIS), simulation parameters, criticality, perturbations, depletion, activation, parallelism, T4G visualizer, output files and couplings (ROOT, GEANT4, MORET, DARWIN). Not for TRIPOLI-5, which has its own skill.
---

# TRIPOLI-4® user guide (v12)

The full user guide is in `docs/`, converted from the PDF, with one Markdown file per chapter. Paths are relative to this file's directory.

- `docs/TOC.md` has the complete outline, with every section mapped to its file and PDF page. **Start here.**
- `docs/NN-<chapter>.md` holds the chapter text. `<!-- page N -->` markers give the PDF page.
- `docs/_meta.json` records the source PDF and the date it was converted.

If `docs/` has only a `.gitkeep` file, the docs haven't been synced. Tell the user to run `./sync.sh tripoli4` at the root of the code_documentation repo. Don't answer syntax questions from memory.

## How to answer

1. Find the section in `docs/TOC.md`, or grep `docs/` for the exact keyword (they are UPPERCASE, e.g. `grep -rn "VOLSURF" docs/`).
2. Read the surrounding text and its examples before writing any input deck. Keyword spelling, block order and terminators matter.
3. Copy syntax from the guide, and don't invent keywords. If something isn't in the guide, say so.
4. Cite the chapter and PDF page, e.g. "(ch. 12 *Defining sources*, p. 141)".
5. TRIPOLI-4 and TRIPOLI-5 have different input models (keyword data set vs Python API). Never mix them.

## Where to look (by chapter title, find the file in TOC.md)

| Topic | Chapters / appendices |
|---|---|
| Running the code, nuclear data, path & dictionary files | Generalities · Cross-sections · Defining path and dictionary files |
| Units, conventions, frames, **list of commands** | General considerations: data, conventions, units, frames |
| A complete small input | Example · Appendix A *Example of geometry* |
| **Order of blocks in an input file** | Appendix B *Data entry sequence* |
| French ↔ English keywords | Appendix C *Translation keywords* |
| Geometry, lattices, operators, geometry checks, 2D views | Geometry definitions · The VOLSURF command · Boundary conditions |
| Materials | Defining compositions · Defining volume-composition associations |
| Sources | Defining sources |
| Tallies | Defining response types · Defining grids · Defining scores · scores on spherical harmonics |
| Variance reduction | Variance reduction techniques (biasing) · adaptive multilevel splitting · weight windows · CADIS |
| Run control, criticality, kinetics, DYNAMIC, MULTIPLE mode | Defining numerical simulation parameters · Scheduler · KIJ matrix calculation |
| Perturbations and sensitivities | Defining perturbations · Standard / Generalized perturbation theory |
| Outputs | The output file · Storing particles · Special outputs · Display of collision sites |
| Depletion and activation | Depletion calculation · Activation calculation · Connection with DARWIN/PEPIN2 |
| HPC | Parallelism · Collision files · Green's function files |
| Tools and couplings | Visualizer T4G · T4toMED · ROOT · GEANT4 · MORET · CASTOR stochastic geometries |
