---
name: tripoli5
description: TRIPOLI-5® Monte Carlo neutron transport code (ASNR/CEA, HPC with MPI/OpenMP/CUDA) — official documentation. Use for any question about TRIPOLI-5 / T5 — its Python API (CORE, AGORA, DELOS, PATMOS, geoplotter), building simulations (geometry, materials and compositions, media, sources, scores, physical quantities), the examples (criticality, PWR/hexagonal/CANDU/Superphénix assemblies), the validation suite, the theory (collision physics, SVT, TSL, geometry, scores), the changelog and known bugs. Not for TRIPOLI-4, which has its own skill.
---

# TRIPOLI-5® documentation

The published TRIPOLI-5 documentation is in `docs/`, converted to Markdown, one file per page. Paths are relative to this file's directory.

- `docs/INDEX.md` lists every page with its title and section headings. **Start here.**
- `docs/_meta.json` records the version synced (the source URL contains `latest-release`, `vX.Y.Z` or `dev`) and the date. Mention the version when it matters.
- Each page starts with `<!-- source: URL -->`. Give that URL as a citation.

If `docs/` has only a `.gitkeep` file, the docs haven't been synced. Tell the user to run `./sync.sh tripoli5` at the root of the code_documentation repo. Don't answer API questions from memory.

## Layout of docs/

| Folder | Content | Use it for |
|---|---|---|
| `examples/features/` | Short examples, one feature each (geometry with AGORA, materials, mixtures, media, sources, scores, simulation, plotter…) | "How do I…?" questions. Start from these. |
| `examples/criticality/`, `examples/geometries/` | Complete cases (Jezebel, pin cell, PWR/hexagonal/CANDU/Superphénix assemblies) | Full working inputs |
| `api/` | Python API reference (core, agora, delos, patmos, geoplotter) | Exact class and function names, arguments, defaults |
| `theory/` | Physics and algorithms (collision physics, SVT, TSL, geometry, scores, moments) | "Why" and "how is it computed" |
| `validation/` | Validation benchmarks | Accuracy and reference comparisons |
| `release/` | Changelog, known bugs | Version differences, "is this a bug?" |

## How to answer

1. Find candidate pages in `docs/INDEX.md`, or grep for the class or function name (`grep -rn "class_name" docs/`).
2. For code, start from the closest example, then check every call against `docs/api/`. Don't invent classes, arguments or defaults.
3. Check `docs/release/known_bugs.md` and `changelog.md` when behaviour looks wrong or differs between versions.
4. TRIPOLI-5 is driven through Python and is a different code from TRIPOLI-4. Never reuse TRIPOLI-4 keyword syntax.
5. Cite the page (file path or source URL).
