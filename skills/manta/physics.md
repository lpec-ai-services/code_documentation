# Physics branch: models and equations

Pages are in `docs/`. **T** = `theory_manual/`, **C** = `manta_components_user_guide/formulations/`, **F** = `manta_frontend_user_guide/`.

## Solid mechanics

| Topic | Theory | Formulations / bricks |
|---|---|---|
| Solid mechanics overview | T `solid_mechanics/solid_mechanics.md` | F `models/solid_mechanics/` |
| Linearized elasticity, thermal expansion | | C `solid_mechanics/elasticity/linearized_elasticity_finite_element_formulation.md`, `thermalExpansionFormulation.md`; F `bricks/solid_mechanics/isotropic_linear_elastic_material.md` |
| Non-linear behaviour (MFront laws), finite strain | | C `solid_mechanics/non_linear_behaviour/solid_finite_element_formulation.md`; F `bricks/solid_mechanics/implicit_mechanics_solid_material.md` |
| **Beams: Euler–Bernoulli and Timoshenko**; rods | T `solid_mechanics/beams/beam_theory.md` | C `solid_mechanics/beams_and_shells/` (euler_beams, timoshenko_beams, rods, nodal); F `bricks/solid_mechanics/beams/` |
| Shells (MITC4, doc marked deprecated) | T `solid_mechanics/mitc4.md` | |
| **Contact and impact** (analytical contact, friction) | | C `solid_mechanics/contact_and_impact/`; components guide `algorithms_and_numerics/contact/contact.md` |
| Loadings: pressure, resulting force, gravity, body/surface forces, nodal forces, Dirichlet, glue, multiple-point constraints | | C `constraints_and_bcs/`; F `loadings.md`, `bricks/solid_mechanics/imposed_*.md` |

## Damage and fracture

| Topic | Where |
|---|---|
| **Phase-field damage**, explicit and implicit | C `damage_and_fracture/phasefieldexplicit.md`, `phasefieldimplicit.md`; phase-field time integrators: components guide `algorithms_and_numerics/time_integrators/pf_time_integrators.md` |
| **Micromorphic damage** (model and bricks) | F `models/micromorphic_damage/`, `bricks/micromorphic_damage/` |
| Linear elastic fracture mechanics, **G-theta** | components guide `algorithms_and_numerics/gtheta_method_2D.md` |

## Heat transfer in solids

| Topic | Where |
|---|---|
| Heat equation in solids | T `solid_heat_transfer/solid_heat_transfer.md` |
| Conduction, capacity, heat sources, imposed flux, **linear and non-linear convection** | F `models/solid_heat_transfer/`, `bricks/solid_heat_transfer/`; C `heat_transfer/boundary_conditions/` |

## Compressible fluid mechanics

| Topic | Where |
|---|---|
| **Compressible inviscid (Euler) equations** | T `fluid_mechanics/compressible_fluid_mechanics.md` |
| Quasi-1D flow in a varying-section pipe | T `fluid_mechanics/varying_section_1d.md` |
| **Critical flow** at a break (isentropic expansion, Barré de Saint-Venant relation) | T `fluid_mechanics/critical_flow.md`; boundary condition C `fluid_mechanics/fvm_compressible_fluid_mechanics/boundary_conditions/critical_flow.md` |
| **Equations of state**: perfect gas, stiffened gas, isothermal fluid, steam/water | C `fluid_mechanics/equations_of_state/` |
| **Fluid models**: single fluid, **HEM**, MCSG | C `fluid_mechanics/fluid_models/` |
| Source terms: gravity, regular head loss, energy injection | C `fluid_mechanics/fvm_compressible_fluid_mechanics/source_terms/` |
| Boundary conditions: wall, tank, prescribed outflow, copied | C `fluid_mechanics/fvm_compressible_fluid_mechanics/boundary_conditions/` |

## Generic PDEs

| Topic | Where |
|---|---|
| Scalar and vector Laplacian | C `general_models/` |
| Advection, Burgers (FVM test problems) | C `fluid_mechanics/fvm_misc/` |
