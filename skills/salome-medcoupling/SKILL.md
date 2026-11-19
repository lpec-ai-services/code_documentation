---
name: salome-medcoupling
description: MEDCoupling / MEDLoader (SALOME MED module, CEA/EDF) — library to build, manipulate, read and write meshes and fields (MED file format, .med) in Python or C++. Use for any question about MEDCoupling or MEDLoader, including DataArrayDouble/Int, MEDCouplingUMesh/CMesh/extruded meshes, fields (ON_CELLS, ON_NODES, Gauss points, time discretizations), reading and writing MED files (basic and advanced APIs, MEDFileUMesh, MEDFileField…), mesh/field interpolation and remapping (MEDCouplingRemapper, P0/P1, intensive vs extensive, conservative interpolation, intersectors), mesh conversion, renumbering, partitioning and merging, parallelism (ParaMEDMEM, MPI), ICoCo coupling, NumPy interop.
---

# MEDCoupling / MEDLoader documentation

The MEDCoupling documentation from the SALOME repository (master branch) is in `docs/`, converted to Markdown. Paths are relative to this file's directory. It has three parts:

| Part | Content | Start with |
|---|---|---|
| `docs/developer/` | **Developer guide / reference** (the site at docs.salome-platform.org/…/MEDCoupling/developer): concepts, arrays, meshes, fields, interpolation theory, MEDLoader, parallelism, FAQ. All **302 code snippets are included** (Python and C++) | `docs/developer/INDEX.md`, `start/terminology.md` |
| `docs/user/` | **User's manual** by task: data movement (building meshes and fields), analysis, conversion and projection, optimization (renumbering). Code examples inlined from the official test files | `docs/user/basic_concepts.md` |
| `docs/tutorial/` | **Tutorial** (English versions): DataArrays, meshes, fields, MEDLoader basic/advanced, split and merge, remapper, NumPy/SciPy, full examples (agitator, RJH). The `atest*.md` pages are the exercise solutions | `docs/tutorial/index.md` |

- Formulas are exact LaTeX (`$…$`, `$$…$$`).
- Each page starts with `<!-- source: … -->`, the original file in the repository.
- Three examples in `user/data_optimization.md` are missing upstream (the markers they point to don't exist in the test file). The page says so where they would be.
- `docs/*/_meta.json` records the source commit.

## Concepts or usage?

| The question is about… | Where |
|---|---|
| **Concepts and algorithms.** Mesh/field terminology, spatial discretizations (P0, P1, Gauss points), **nature of a field** (intensive/extensive, conservative vs maximum principle), interpolation theory, intersectors and point locators, barycentric and mapped barycentric coordinates, 2D/3D intersection specifics, MED file model, numbering | `developer/start/terminology.md`, `developer/reference/fields/discretization.md`, `developer/reference/interpolation/` (`intro-interp`, `interptheory`, `NatureOfField`, `intersectors`, `intersec-specifics`, `barycoords`, `mapped_bary`, `Geometric2D`), `developer/appendix/interpkernel.md`, `developer/appendix/med-file.md`, `developer/appendix/glossary.md` |
| **Usage.** Building and modifying arrays, meshes and fields; reading and writing MED files; projecting fields (`MEDCouplingRemapper`); conversion, renumbering, splitting and merging; MPI and ICoCo; porting old scripts | `developer/reference/arrays/`, `meshes/`, `fields/`, `medloader/`, `interpolation/remapper.md`, `distrib/`, `misc/` (ICoCo, MPI from SWIG, tools), `developer/faq.md`, `developer/appendix/porting*.md`, plus the user guide and tutorial |

## How to answer

1. **For code**, find the closest tutorial or user-guide example, then check each method in the developer reference. Grep for exact names (`grep -rn "getMeasureField" docs/`). Never invent methods or arguments: MEDCoupling's API is large and many names look alike.
2. **Python is the main entry point** (`import medcoupling as mc`, see `developer/start/python-api.md`). C++ specifics are in `developer/reference/cpp/`. The developer guide often gives both versions of each snippet.
3. **For interpolation**, always state the field's nature (`IntensiveMaximum`, `ExtensiveConservation`…) and the discretization (P0/P1), because they change the result. See `NatureOfField.md` and `interptheory.md`.
4. Old scripts (`MEDCoupling` v7 or ICoCo before 9.7) need porting: see `developer/appendix/porting.md` and `porting_icoco.md`.
5. Cite the page path.

## Related skills

- **`salome`:** the SALOME user documentation (desktop, GEOM, SMESH, SHAPER, YACS, ADAO…).
- **`manta`:** reads MED meshes.
- **`tfel-mfront`:** materials.
