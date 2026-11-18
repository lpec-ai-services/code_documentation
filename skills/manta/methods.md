# Methods branch: numerics and how to use MANTA

Pages are in `docs/`. **T** = `theory_manual/`, **CG** = `manta_components_user_guide/`, **F** = `manta_frontend_user_guide/`.

## Getting started

| Topic | Where |
|---|---|
| Installation (CMake options, dependencies, compilers) | `get_started/installation_guide.md` |
| **Containers** (Apptainer image, MANTA in `/opt/manta`) | `get_started/containerized_usage.md` |
| Running the examples | `get_started/run_examples.md` |
| Searching the demos by keyword | `demos/search_tool.md` |

## Frontend (high-level API, Python)

| Topic | Where |
|---|---|
| **Main concepts**: simulation, physical system, materials, models, bricks, coupling schemes, sequences and steps | F `main_concepts.md` |
| Physical system: mesh, geometric and structural hypotheses | F `physical_system/` |
| Properties; loadings | F `properties.md`, `loadings.md` |
| Models: generalities, implicit/explicit mechanics, heat transfer, micromorphic damage, MFront point-wise models, explicit compressible fluid | F `models/` |
| Bricks: solid mechanics, beams, heat transfer, point-wise, micromorphic damage | F `bricks/` |
| **Solvers** for implicit models | F `solvers/implicit_model_solvers.md` |
| Simulation class, **time-increment computers** | F `simulation/` |
| Auxiliary tasks (L2 projection) | F `auxiliary_tasks/` |
| Post-processing: curves, line curves, **VTK export** | F `post_processings/` |
| Constraints on unknowns; command-line arguments; monitors; profiling; tools | F `miscellaneous/` |
| **MFront in MANTA**: behaviour bricks, managing material knowledge, post-processed fields | F `miscellaneous/mfront_behaviors_bricks.md`, `mfront_material_knowledge_management.md`, `mfront_postprocessed_fields.md` |
| GPU: PETSc with CUDA | F `miscellaneous/petsc_cuda.md` |

## Components (low-level API, C++)

| Topic | Where |
|---|---|
| C++ outline and steps of a computation | CG `main_user_concepts/general_outline/` |
| Mesh, fields, readers, **linear-solver interface**, MFrontBehaviorComponent | CG `main_user_concepts/user_guide_objects/` |
| Formulations catalogue (by physics) | CG `formulations/`; catalogs `catalogs/components/physics_catalog_theme.md` |
| Module system: available modules, enabling/disabling, creating a module | CG `the_module_system/` |
| User-defined extensions, plug-ins | CG `user_defined_extensions/` |
| VTK output | CG `post_processings/vtk_output.md` |

## Numerical methods

| Topic | Where |
|---|---|
| **Non-linear implicit resolution**; a Cast3M-like Newton algorithm | T `nonlinear_resolution/`; CG `algorithms_and_numerics/newton.md` |
| **Time integrators** (general, phase-field specific) | CG `algorithms_and_numerics/time_integrators/` |
| Eigenproblem solver | CG `algorithms_and_numerics/eigen_problem.md` |
| Contact algorithms | CG `algorithms_and_numerics/contact/contact.md` |
| G-theta method (2D) | CG `algorithms_and_numerics/gtheta_method_2D.md` |
| FVM for compressible flow: explicit/implicit Euler formulations (general and pipes), **Chimera**, reconstruction and limiting operators | CG `formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/end_user_formulations/`, `reconstruction_operators/`, `limiting_operators/` |
| **Jacobian** for implicit Euler formulations | T `fluid_mechanics/jacobian_computation.md` |
| **CFL** stability factor estimate (explicit) | T `fluid_mechanics/cfl_stability_factor_estimate.md` |
| L2 projection of integration-point values (plain and regularized) | CG `formulations/utilities/finite_elements/` |
| Beam matrices: stiffness (also exact), lumped mass, internal forces | CG `formulations/solid_mechanics/beams_and_shells/` |

## Demos (commented, with full code)

| Demo | Where |
|---|---|
| 2D elastic plate with a hole: C++ and Python versions | `demos/components_examples/elasticity/`, `demos/frontend_examples/elasticity/` |
| Charpy impact test (3D notched beam, contact) | `demos/components_examples/contact_and_impact/charpy.md` |
| LEFM, inclined crack, G-theta | `demos/components_examples/fracture_mechanics/gtheta_example.md` |
| Euler beam, explicit dynamics | `demos/components_examples/structural_elements/euler_beam_explicit.md` |
| Finite-strain, strain-rate-sensitive plasticity (Swift–Voce hardening, Cowper–Symonds rate effect): notched bar in tension | `demos/frontend_examples/non_linear_behaviour/plasticity/` |
| Damage and fracture: Engelen double-notched plate (implicit gradient-enhanced damage), ductile rupture of a notched bar (gradient-regularized Gurson–Tvergaard–Needleman, `mealor2-tp8`), micromorphic damage (fibre-reinforced matrix), bounded-constraint optimization | `demos/frontend_examples/damage_and_fracture/` |
| Nuclear fuel pellet heat transfer (multi-material) | `demos/frontend_examples/solid_heat_transfer/fuel_rod/` |
| Norms for a linear thermal problem (numerical analysis) | `demos/frontend_examples/numerical_analysis/` |
| Catalogues of formulations, pre- and post-processing tutorials | `catalogs/components/` |
