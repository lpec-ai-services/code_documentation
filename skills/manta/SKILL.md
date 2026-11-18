---
name: manta
description: MANTA — HPC multiphysics simulation platform (finite elements, finite volumes, HHO; MPI, PETSc; material behaviours via MFront/MGIS) with a Python frontend (PyManta, high-level API) and C++ components (low-level API). Use for any question about MANTA or pyManta, including setting up a simulation (physical system, mesh, geometric hypothesis, models, bricks, loadings, coupling schemes, solvers, time steps, post-processing/VTK), solid mechanics (implicit/explicit, beams Euler/Timoshenko, contact and impact, damage, phase-field and micromorphic fracture, G-theta), solid heat transfer, compressible inviscid fluid mechanics (Euler FVM, HEM, critical flow, equations of state), installation and containers, and the commented demos. Also covers its theory manual.
---

# MANTA documentation

The published MANTA documentation is in `docs/`, converted to Markdown, one file per page. The Doxygen API reference was left out on purpose: this skill is for user-level work, through examples and guides. Paths are relative to this file's directory.

- `docs/INDEX.md` lists every page with its title and headings. **Start here.**
- Each page starts with `<!-- source: URL -->`. Give that URL as a citation.
- **Equations are exact LaTeX** (`\( … \)` inline, `\[ … \]` display, with the source's equation numbers).
- **Code in the demos is complete** (Python and C++, line numbers removed). Downloadable inputs (`_downloads/…`: meshes, `CMakeLists.txt`) are not in the mirror. When the full file is shown inline, use that.

## Two APIs, two user guides

| Layer | Use it when | Docs |
|---|---|---|
| **High-level API: MANTA/PyManta frontend** (Python): simulation, physical system, models, bricks, loadings, coupling schemes, solvers, post-processing | The user writes a simulation script. **Default for most users.** | `docs/manta_frontend_user_guide/` (start with `main_concepts.md`), demos in `docs/demos/frontend_examples/` |
| **Low-level API: MANTA components** (C++): formulations, fields, mesh, readers, linear solvers, Newton, time integrators, modules, plug-ins | Writing C++ components or new formulations, or the user mentions C++/`main.cpp` | `docs/manta_components_user_guide/`, demos in `docs/demos/components_examples/` |

## Physics or methods?

| The question is about… | Open |
|---|---|
| **The physical models and equations.** Elasticity, beams, contact, damage and fracture, heat transfer, compressible flow, critical flow, equations of state | `physics.md` |
| **How MANTA solves and how to use it.** Discretization, time integration, Newton, solvers, coupling, frontend objects, bricks, components, HPC, post-processing, installation | `methods.md` |

## How to answer

1. **For a simulation script**, start from the closest demo (see the Demos table in `methods.md`, or the catalogs in `docs/catalogs/components/`, which index formulations by theme). Then check each class and option in the frontend user guide. Don't invent class names, brick names or parameters: grep for them (`grep -rn "ImplicitMechanicsSolidMaterial" docs/`).
2. **For material behaviour**, MANTA uses MFront. See the frontend pages `miscellaneous/mfront_behaviors_bricks.md` and `miscellaneous/mfront_material_knowledge_management.md`. For writing the `.mfront` law itself, use the `tfel-mfront` skill.
3. **For theory**, cite the theory manual page and its equation numbers.
4. Cite the page (file path or source URL).

## Related skills

- **`tfel-mfront`:** material behaviours used by MANTA bricks.
- **`thermal-hydraulics`:** physics of two-phase and critical flow.
- **`valjean`:** comparing results.
