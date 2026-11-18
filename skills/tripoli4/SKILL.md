---
name: tripoli4
description: TRIPOLI-4® (version 12) Monte Carlo particle transport code from CEA — user guide CEA-R-6599. Use for any question about TRIPOLI-4 / T4 input files (keyword data sets), geometry (combinatorial or surface-based, lattices, SMASH/VMINUS operators), compositions, sources, responses, scores, variance reduction (INIPOND, AMS, weight windows, CADIS), simulation parameters, criticality, perturbations, depletion, activation, parallelism, T4G visualizer, output files and couplings (ROOT, GEANT4, MORET, DARWIN). Not for TRIPOLI-5, which has its own skill.
---

# TRIPOLI-4® user guide (v12, CEA-R-6599)

The full user guide is in `docs/`, converted from the PDF, with one Markdown file per chapter. Paths are relative to this file's directory.

- **Files `01`–`45` are chapters 1–45.** Files `46`–`50` are appendices A–E. `00` is the front matter (title pages, contents, changes since v11.1).
- `docs/TOC.md` has the complete outline, with every section mapped to its file and PDF page.
- Section titles are Markdown headings (`## 12.1 DEFINING A SOURCE`). `<!-- page N -->` markers give the **PDF** page, which is one more than the page number printed in the guide.
- Syntax blocks keep the guide's line layout. Keywords are plain UPPERCASE text, so grep finds them: `grep -rn "SOURCES_LIST" docs/`.

If `docs/` has only a `.gitkeep` file, the docs haven't been synced. Tell the user to run `./sync.sh tripoli4` at the root of the code_documentation repo. Don't answer syntax questions from memory.

## How to answer

1. Find the chapter in the table below or in `docs/TOC.md`, or grep `docs/` for the exact keyword.
2. Read the syntax block and the notes after it before writing any input deck. Keyword spelling, block order and `END_…` terminators matter. `47-data-entry-sequence.md` gives the order of everything in an input file.
3. Copy syntax from the guide, and don't invent keywords. If something isn't in the guide, say so.
4. Keywords exist in English and French (`SOURCES_LIST` = `LISTE_SOURCES`). Use the language of the user's existing deck, and translate with `48-translation-keywords.md` (table: English | French | Default (old)).
5. Cite the chapter and PDF page, e.g. "(ch. 12 *Defining sources*, PDF p. 141)".
6. TRIPOLI-4 and TRIPOLI-5 have different input models (keyword data set vs Python API). Never mix them.

## Where to look

| Topic | Files |
|---|---|
| Running the code, nuclear data, path & dictionary files | `01` generalities · `02` cross-sections · `03` path and dictionary files |
| Units, conventions, frames, **list of calculation commands** | `04` general considerations |
| A complete small input; comments and `#include`-style file insertion | `05` example · `06` comments and inserting files · `46` example of geometry (App. A) |
| **Order of all blocks and keywords** | `47` data entry sequence (App. B) |
| English ↔ French keywords | `48` translation keywords (App. C) |
| Geometry: types, surfaces, volumes, SMASH/VMINUS/INTE/UNION, lattices, 2D views, checks | `07` geometry definitions · `08` VOLSURF · `09` boundary conditions |
| Materials | `10` compositions · `11` volume-composition associations |
| Sources (spatial, angular, energy, time, files, external, multi-particle) | `12` sources |
| Tallies | `13` response types · `14` grids · `15` scores · `16` spherical-harmonics scores |
| Variance reduction | `17` biasing (INIPOND, importance maps) · `18` AMS · `19` weight windows · `20` CADIS |
| Run control: SIMULATION, criticality, kinetics, adjoint, boron/albedo search, DYNAMIC, MULTIPLE mode | `22` simulation parameters · `24` KIJ matrix · `44` scheduler |
| Homogenization; volume, density and mass checks | `21` homogenization · `23` calculation verification |
| Outputs | `26` output file · `27` storing particles · `31` special outputs · `25` display of collision sites |
| Perturbations and sensitivities | `28` perturbations · `29` standard perturbation theory · `30` generalized perturbation theory |
| Depletion and activation | `40` depletion · `41` activation · `32` DARWIN/PEPIN2 |
| HPC and reuse | `33` parallelism · `34` collision files · `35` Green's function files · `37` energy cut per volume |
| Tools and couplings | `38` T4G visualizer · `39` T4toMED · `36` ROOT · `42` GEANT4 · `43` MORET · `45` CASTOR stochastic geometries |
| References, alphabetical index | `49` bibliography · `50` index |
