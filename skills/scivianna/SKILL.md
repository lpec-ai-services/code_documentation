---
name: scivianna
description: scivianna (SCIentific VIsualizer for simulAtioN aNAlysis, CEA) — Python module built on Holoviz Panel/Bokeh to visualize simulation geometries and results: 2D slices of meshes and fields (MED/MEDCoupling, VTK, structured grids, polygons), 1D plots, 3D (VTK/pyvista), graphs and dataframes, in multi-panel layouts with linked interactions, a static matplotlib API, code-coupling views (ICoCo/C3PO), an LLM agent, and an extension system for new code interfaces. Use for any question about using scivianna or writing interfaces/extensions for it.
---

# scivianna documentation (v0.9.2)

The docs come from the scivianna repository (CEA, `github.com/cea-code-coupling/scivianna`, master branch). Paths are relative to this file's directory.

| Part | Content |
|---|---|
| `docs/AGENTS.md` | **Developer onboarding guide** (written for AI agents): architecture (UI process + multiprocessing worker for code-specific I/O), tech stack, directory map, key abstractions. **Read first for any development task** |
| `docs/readme.md` | Project readme: features, install |
| `docs/tutorials/` | **Tutorial notebooks**: `0_introduction`, `1_simple_2d_panel`, `2_multiview_panels`, `3_panel_2d_1d_interactions` (users); `4_develop_interface`, `5_develop_extension` (developers); `6_matplotlib_api` (static figures) |
| `docs/api/scivianna.*.md` | **API reference** per subpackage: its readme (role, files, key classes), then every class with signature, bases, methods and docstrings, read from the source |
| `docs/agent_instructions.md` | Instructions used by scivianna's built-in LLM agent |
| `examples/` | **Runnable demos** with descriptions: `med/` (MED files, 2D and 3D), `vtk_example/`, `c3po_coupling/` (code coupling), `graph/`, `europe_grid/`, `mandelbrot/`, `demo.py` |

## Main concepts (see `AGENTS.md` and the tutorials)

- **Panels** display data: `Panel1D`, `Panel2D`, `Panel3D`, `PanelGraph`, `PanelDataFrame` (`docs/api/scivianna.panel.md`). **Layouts** arrange them in grids or splits with linked events (`scivianna.layout`).
- **Interfaces** read a code's data (geometry, fields) in a separate worker process. MED, structured mesh and VTK interfaces are built in (`scivianna.interface`). New codes are supported by writing an interface (tutorial 4).
- **Plotters** render: `plotter_1d`, `plotter_2d` (grid and polygon backends, Bokeh or matplotlib), `plotter_3d` (VTK), `plotter_graph`, `plotter_dataframe`.
- **Extensions** add GUI features (tutorial 5, `scivianna.extension`). **Coupling** shows live results from coupled codes (`scivianna.coupling`, ICoCo/C3PO).
- Optional extras: `pip install scivianna[medcoupling]`, `[3d]` (pyvista + scivianna-vtk), `[graph]`, `[coupling]`, `[agent]`, `[gmsh]`, `[grid]`.

## How to answer

1. **To use it**, start from the closest tutorial or example, then check every class and argument in `docs/api/`. Grep (`grep -rn "set_field" docs/api`). Don't invent API: scivianna is young and changes quickly.
2. **To write an interface or extension**, read `AGENTS.md`, tutorial 4 or 5, and the base classes in `docs/api/scivianna.interface.md` / `scivianna.extension.md`.
3. Cite the page or example path.

## Related skills

- **`salome-medcoupling`:** MED files and fields.
- **`vtk`:** VTK data.
- **`thermal-hydraulics`, `neutronics`:** the physics being visualized.
