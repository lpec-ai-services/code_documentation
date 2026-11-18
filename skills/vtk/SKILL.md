---
name: vtk
description: VTK (Visualization Toolkit, Kitware) in Python — 900 commented Python examples (classic API and the newer "Pythonic" API with >> pipelines), the full VTK Textbook (visualization pipeline, data representation, algorithms, rendering, image processing) and the VTK user documentation (installing and using VTK in Python/Jupyter/C++/WebAssembly, VTK file formats — legacy .vtk, XML .vtu/.vtp/.vti…, VTKHDF —, Python wrappers, building VTK and wheels). Use for any question about writing VTK/vtkmodules Python code, reading/writing VTK files, filters, mappers, rendering, widgets, volume rendering, picking, or visualization concepts. For PyVista or ParaView-specific APIs, say they are not covered.
---

# VTK (Python) documentation

The docs are in `docs/` (paths are relative to this file's directory):

| Part | Content | Source |
|---|---|---|
| `docs/site/Python/` | **421 Python examples**, classic VTK API. Each page has a description, links to the VTK classes used and the **complete code** | examples.vtk.org |
| `docs/site/PythonicAPI/` | **480 examples** in the newer **Pythonic API** (properties as keyword arguments, `>>` pipelines; needs VTK ≥ 9.3.20240428). Same topics, more examples | examples.vtk.org |
| `docs/site/PythonicAPIComments.md` | **How the Pythonic API works**: initialization, properties, pipelines, multiple ports and outputs | examples.vtk.org |
| `docs/site/Python.md`, `docs/site/PythonicAPI.md` | **Example indexes** by topic, with one-line descriptions. **Start here for "how do I…"** | |
| `docs/site/Python/Coverage/PythonVTKClassesUsed.md` | **Class → examples table**: which examples use a given VTK class | |
| `docs/site/PythonHowTo.md` | Python how-tos | |
| `docs/site/VTKBook/` | **The VTK Textbook** (3rd edition, published by Kitware), chapters 1–12 + glossary | examples.vtk.org |
| `docs/user/` | **VTK user documentation** (VTK 9.7 master): getting started (Python, Jupyter, C++, JS, WebAssembly), file formats, Python wrappers, build instructions, wheels, design documents, migration guides | VTK repo, `Documentation/docs` |

- `docs/site/INDEX.md` and `docs/user/INDEX.md` list every page with its headings.
- Figures and screenshots link to the live site. Class names link to the online C++ Doxygen reference, which is not included.

## Concepts or code?

| The question is about… | Where |
|---|---|
| **Concepts and algorithms**: pipeline and execution model, data model (dataset types, cells, attributes), contouring, cutting, glyphs, streamlines, decimation, implicit modelling, image processing, volume rendering, graphics primitives, lighting, cameras, transparency | `docs/site/VTKBook/`: ch. 3 graphics primer, ch. 4 **pipeline**, ch. 5 **data representation**, ch. 6 fundamental algorithms, ch. 7 advanced graphics (volume rendering, transparency, textures), ch. 8 advanced data representation, ch. 9 advanced algorithms, ch. 10 image processing, ch. 11 web, ch. 12 applications |
| **Writing code**: which classes, how to chain them, reading and writing files, rendering, interaction, widgets | The example indexes (`Python.md`, `PythonicAPI.md`), then the example pages. `PythonicAPIComments.md` for the new syntax |
| **Files**: legacy `.vtk`, XML (`.vtu`, `.vtp`, `.vti`, `.vtr`, `.vts`, `.vtm`…), **VTKHDF** | `docs/user/vtk_file_formats/` |
| **Installing and environment**: pip wheels, Jupyter, offscreen, building, C++ projects | `docs/user/getting_started/`, `docs/user/advanced/`, `docs/user/build_instructions/` |

## How to answer

1. **For code**, find the closest example via the indexes, or grep for a class (`grep -rln "vtkContourFilter" docs/site/Python docs/site/PythonicAPI`). Adapt its code rather than writing VTK from memory: class names, module paths (`from vtkmodules.vtkFiltersCore import …`) and method names must match the examples.
2. **Match the user's style.** Classic API (`SetInputConnection`/`GetOutputPort`) or Pythonic API (`>>`, keyword properties, VTK ≥ 9.3.20240428). If unspecified, the Pythonic examples are the more modern choice, but say which you used.
3. **Import from `vtkmodules.<module>`** as the examples do (not `import vtk`, which loads everything). Keep the `import vtkmodules.vtkRenderingOpenGL2` (and `vtkInteractionStyle`) lines: they register the OpenGL implementations of the `vtkRenderingCore` classes (`docs/user/advanced/PythonWrappers.md`, "Factories and Implementation Modules").
4. **For a class's full method list**, which isn't in these docs, suggest `help(vtkClass)` in Python or the Doxygen link on the example page.
5. Cite the example or chapter path.

## Related skills

- **`scivianna`:** CEA's visualizer, which has a VTK plotter.
- **`salome-medcoupling`:** MED ↔ VTU conversion.
- **`manta`:** VTK export.
