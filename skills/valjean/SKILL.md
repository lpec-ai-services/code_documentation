---
name: valjean
description: VALJEAN, CEA's Python framework for verification & validation test suites (built for TRIPOLI-4®). Use for any question about valjean, including parsing TRIPOLI-4 output (.res) or APOLLO3 rates files into datasets (eponine, Parser, Browser, Dataset), statistical tests comparing results (gavroche: Student, Holm-Bonferroni, chi2…), test reports and plots (javert), tasks and dependency graphs (cosette), the valjean executable and job files (cambronne), and writing V&V jobs or notebooks. For TRIPOLI-4 input syntax use the tripoli4 skill.
---

# VALJEAN documentation (v0.11.0)

The VALJEAN docs are in `docs/`, converted to Markdown, one file per page. Paths are relative to this file's directory.

- `docs/INDEX.md` lists every page with its title and headings. **Start here.**
- `docs/modules/<subpackage>/…md` is the API reference, one page per module: the module docstring (often a full tutorial), then every public class with its constructor signature and bases, its methods and properties, and every function.
- Each page starts with `<!-- source: … -->`, the original `.rst` or `.ipynb` path in `doc/src` of the repo.
- `docs/_meta.json` records the source and version.

The API pages were built by reading docstrings straight from the source files, not from a Sphinx build. Signatures are exact. Inherited members appear only on the base class, so check the `bases:` shown after each class name.

If `docs/` has only a `.gitkeep` file, the docs haven't been synced. Tell the user to run `./sync.sh valjean` at the root of the code_documentation repo.

## Subpackages

| Package | Role | Where |
|---|---|---|
| `eponine` | Parsing results: TRIPOLI-4 output (`tripoli4.parse.Parser`, `data_convertor`, depletion ROOT files), APOLLO3 rates (`apollo3`), `Dataset`, selecting responses with `Browser` | `docs/modules/eponine*` |
| `gavroche` | Tests on datasets: equality, approx-equality, statistical tests (Student, Bonferroni/Holm-Bonferroni, chi2…), diagnostics | `docs/modules/gavroche*` |
| `javert` | Test reports and representations: plots, tables, rst/reports (`TestReport`, `Representation`, `FullRepresenter`) | `docs/modules/javert*` |
| `cosette` | Task engine: tasks, dependency graphs, scheduling, running codes, checking out and building code | `docs/modules/cosette*` |
| `cambronne` | The `valjean` command-line executable (`run`, `graph`, `env`) and job files | `docs/modules/cambronne*` |

## Worked examples (in French)

`docs/examples/`:
- **Notebooks:** Godiva k_eff analysis, Livermore spheres, the REPLICA benchmark, sensitivities, mesh scores, APOLLO3 rates reader/picker.
- **Complete job:** `jobs/spherical_cows/job.md` (TRIPOLI-4 vs MCNP, from tasks to report).

## How to answer

1. For "how do I parse/compare/plot…", start from the closest notebook or the spherical-cows job, then check each call in `docs/modules/`.
2. Grep for class or function names (`grep -rn "class valjean.eponine.tripoli4.parse.Parser" docs/`). Every API heading has the form `` ### `class valjean.<module>.<Name>(…)` `` or `` ### `valjean.<module>.<func>(…)` ``.
3. Don't invent arguments. Use the signatures shown. The examples are in French, so answer in the user's language.
4. Cite the page path.
