---
name: salome
description: SALOME platform user documentation (SALOME 9.16) for every module — desktop/GUI (study, object browser, viewers, Python console, notebook, salome.py), SHAPER parametric CAD (sketcher, features, model.* Python API), GEOM geometry (geompy/geomBuilder), SMESH meshing (smeshBuilder, hypotheses, algorithms, quality controls, filters, MED/UNV/CGNS import-export) with the Netgen, MG-CADSurf, MG-Tetra, MG-Hexa, MG-Hybrid and Gmsh plug-ins and blocFissure, HexaBlock, HOMARD mesh adaptation, YACS workflows/coupling (CALCIUM, YACSGEN), ADAO data assimilation and optimization (3DVAR, Kalman filters, BLUE…), EFICAS, JobManager, FIELDS/MEDCalc, CMake module build, HELLO/PYHELLO sample modules, GUI architecture. Use for any question on using or scripting SALOME; MEDCoupling/MEDLoader API is in salome-medcoupling.
---

# SALOME documentation

The user documentation shipped with SALOME 9.16.0 (the site docs.salome-platform.org/latest), converted to Markdown, one file per page, one folder per module. Paths are relative to this file's directory.

- `docs/INDEX.md` lists the module folders with page counts. Each module folder has its own `INDEX.md` (every page with its title and headings). **Start there.**
- Python examples (the "TUI scripts") are inlined as code blocks. Screenshots are not included: images link to the live site.
- Formulas are kept as LaTeX (`$…$`, `$$…$$`).
- Each page starts with `<!-- source: URL -->`: cite that URL.

This is a usage guide, so the skill has no physics/methods split.

## Modules

| Folder | Module | Start with |
|---|---|---|
| `docs/GUI/` | **Desktop**: study, object browser, viewers (OCC, VTK, Plot2D…), Python console, notebook, preferences, plugins manager, `salome.py`/`sg` | `salome_desktop.md`, `text_user_interface.md`, `working_with_python_scripts.md` |
| `docs/architecture/` | GUI architecture notes for module developers | |
| `docs/SHAPER/` | **SHAPER**: parametric CAD. Sub-folders per plug-in (`SketchPlugin`, `PrimitivesPlugin`, `FeaturesPlugin` for extrusion/booleans/fillets, `BuildPlugin`, `ConstructionPlugin`, `ExchangePlugin`, `CollectionPlugin` for groups and fields, `ParametersPlugin`…). `TUI_*.md` pages hold the `model.*` Python scripts | `index.md`, `General/` |
| `docs/GEOM/` | **GEOM**: geometry. `*_page.md` GUI pages; `tui_*_page.md` Python examples; `geompy_doc/` the geomBuilder Python reference (`group__l3__*`/`group__l4__*` = function families, with signatures and parameters) | `python_interface.md`, `geompy_doc/group__geomBuilder.md` |
| `docs/SMESH/` | **SMESH**: meshing. Concepts (`about_meshes`, `about_hypo`, `basic_meshing_algos`, `1d/2d/3d_meshing_hypo`), editing, quality controls (`aspect_ratio`, `skew`…), filters, `importing_exporting_meshes`; Python API `smeshBuilder.md`, `StdMeshersBuilder.md`, `smeshpy_interface.md`; examples `tui_*.md`. Tools: `blocFissure/` (cracks), `MGCleaner/`, `yams/` (MG-SurfOpt), `padder/`, `MacMesh/`, `TopIIVolMesh/`, `Verima/` | `smeshpy_interface.md`, `tui_creating_meshes.md` |
| `docs/NETGENPLUGIN/`, `BLSURFPLUGIN/` (MG-CADSurf), `GHS3DPLUGIN/` (MG-Tetra), `HexoticPLUGIN/` (MG-Hexa), `HYBRIDPLUGIN/` (MG-Hybrid), `GMSHPLUGIN/` | **Meshing plug-ins**: hypothesis parameters, Python interface; `*pluginpy_doc/` the Python classes | `*_hypo_page.md`, `*_python_interface_page.md` |
| `docs/HEXABLOCK/` | **HexaBlock**: block-structured hexahedral meshing | `general.md`, `gui.md` |
| `docs/HOMARD/` | **HOMARD**: mesh adaptation (refinement/coarsening); cases, iterations, hypotheses, zones, boundaries; `tui_*.md` Python | `intro.md`, `demarrage_rapide.md` (quick start) |
| `docs/YACS/` | **YACS**: calculation schemes/workflows, XML (`schemaxml.md`) and Python (`schemapy.md`) schemes, components, CALCIUM coupling (`calcium*.md`), YACSGEN (`yacsgen.md`), optimizer loops | `principes.md`, `using.md` |
| `docs/ADAO/` | **ADAO**: data assimilation and optimization. Theory and notations, the 35 algorithms (`ref_algorithm_*.md`: 3DVAR, 4DVAR, Blue, Kalman filters, EnsembleKalmanFilter, ParticleSwarmOptimization, tests…), required inputs (`ref_*_requirements.md`), output variables, textual interface (`tui.md`) | `theory.md`, `methodology.md`, `tui.md` |
| `docs/EFICAS/` | **EFICAS**: data-set (command file) editor and catalogue rules | `eficas_presentation.md` |
| `docs/JOBMANAGER/` | **JobManager**: running jobs on remote resources/batch | `intro.md`, `job.md` |
| `docs/dev/FIELDS/` | **FIELDS**: MED field visualisation (presentations) and MEDCalc field operations; architecture notes | `fields_introduction.md`, `medcalc-userguide-api.md` |
| `docs/dev/PARAVIS/` | PARAVIS overview only (ParaView's own documentation is not shipped) | |
| `docs/dev/cmake/`, `docs/dev/git/` | Building a SALOME module with CMake; git procedure | `dev/cmake/intro.md` |
| `docs/HELLO/`, `docs/PYHELLO/` | Sample C++/Python modules: how to write, build and load a SALOME module | `dev_steps.md` |

## How to answer

1. Pick the module from the table, open its `INDEX.md`, or grep across `docs/` for a function or dialog name (`grep -rn "MakeBoxDXDYDZ" docs/GEOM`, `grep -rln "NumberOfSegments" docs/SMESH`).
2. For scripting, prefer the reference page (signature and parameters) plus a `tui_*` example. Give the full script header the examples use (`salome.salome_init()` or `salome.salome_init_without_session()`, `geomBuilder.New()`, `smeshBuilder.New()`, `from salome.shaper import model`).
3. For GUI questions, give menu paths and dialog fields exactly as the page names them. Don't invent menu entries or parameters.
4. Cite the page (file and source URL).

The documentation is for SALOME 9.16.0: mention it if the user runs another version and the API may differ.

## Related skills

- **`salome-medcoupling`:** the MEDCoupling/MEDLoader library (meshes, fields, interpolation, MED files in Python/C++).
- **`c3po`**, **`icoco`:** code coupling outside YACS.
- **`uranie`:** uncertainty and sensitivity studies (ADAO covers data assimilation).
