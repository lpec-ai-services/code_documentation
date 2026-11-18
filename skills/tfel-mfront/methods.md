# Methods branch: implementing, integrating, testing, using

Pages are in `docs/`.

## Getting started

| Topic | Pages |
|---|---|
| Overview, first behaviour, workflow | `index.md`, `getting-started.md`, `documentations.md` |
| Tutorials: French (Norton), Spanish (with Salome-Meca) | `tutorial.md`, `tutorial-spanish.md` |
| Installation (Linux, Windows MSYS2 / Visual Studio / Cast3M MinGW, FreeBSD), packages | `install*.md`, `packages.md` |
| FAQ | `faq.md` |

## Domain-specific languages and keywords

| Topic | Pages |
|---|---|
| **Implicit DSL**: unknowns, residual $F$, Jacobian $J$, Newton/Broyden/Levenberg–Marquardt, θ-scheme | `implicit-dsl.md`, `Implicit-keywords.md`, `ImplicitII-keywords.md` |
| Implicit variants: finite strain, generic behaviours, CZM, models | `ImplicitFiniteStrain-keywords.md`, `ImplicitGenericBehaviour-keywords.md`, `ImplicitCZM-keywords.md`, `ImplicitModel-keywords.md` |
| **Default DSL** (write your own integration) and variants | `Default-keywords.md`, `DefaultFiniteStrain-keywords.md`, `DefaultGenericBehaviour-keywords.md`, `DefaultCZM-keywords.md`, `DefaultModel-keywords.md` |
| **Runge–Kutta DSLs** (explicit integration with time-step control) | `RungeKutta-keywords.md`, `RungeKuttaFiniteStrain-keywords.md`, `RungeKuttaGenericBehaviour-keywords.md`, `RungeKuttaModel-keywords.md` |
| Specialized isotropic DSLs (radial return): creep, plastic flow, strain-hardening creep, multiple flows | `IsotropicMisesCreep-keywords.md`, `IsotropicMisesPlasticFlow-keywords.md`, `IsotropicPlasticMisesFlow-keywords.md`, `IsotropicStrainHardeningMisesCreep-keywords.md`, `MultipleIsotropicMisesFlows-keywords.md` |
| Material properties and models DSLs | `MaterialProperty-keywords.md`, `MaterialLaw-keywords.md`, `Model-keywords.md` |
| Types and aliases (`stress`, `strain`, `StressStensor`…); Unicode identifiers | `mfront-types.md`, `unicode.md` |
| Parameters; initializers; post-processings | `parameters.md`, `initializers.md`, `post-processings.md` |
| Calling behaviours inside behaviours (`@BehaviourVariable`) | `behaviour-variable.md` |
| Compatibility modes | `mfront-compatibility-modes.md`, `tfel-compatibility-modes.md` |

## Bricks

| Topic | Pages |
|---|---|
| Bricks overview, `@Brick` | `BehaviourBricks.md` |
| **StandardElastoViscoPlasticity**: stress criteria, flow rules, isotropic and kinematic hardening, porosity; extending it | `StandardElastoViscoPlasticityBrick.md`, `StandardElastoViscoPlasticityBrick-PorousPlasticity.md`, `ExtendingStandardElastoViscoPlasticityBrick-StressCriterion.md`, `ExtendingStandardElastoViscoPlasticityBrick-PorousStressCriterion.md` |
| StandardElasticity (Hooke stress potential, plane stress, tangent operator) | `HookeStressPotential.md` |
| FiniteStrainSingleCrystal, DDIF2 | `finitestrainsinglecrystal.md`, `DDIF2Brick.md` |

## Interfaces to solvers

| Solver | Page |
|---|---|
| Cast3M (English / French) | `castem.md`, `castem-fr.md` |
| code_aster | `aster.md` |
| Abaqus Standard / Explicit (UMAT/VUMAT) | `abaqus.md` |
| ANSYS APDL (usermat) | `ansys.md` |
| CalculiX | `calculix.md` |
| ZeBuLoN / Z-set | `zmat.md` |
| Cyrano3 (fuel performance) | `cyrano.md` |
| ElmerFEM | `elmerfem.md` |
| AMITEX_FFTP (FFT) | `amitex.md` |
| **Generic interface** (MGIS: FEniCS, MFEM, OpenGeoSys, MoFEM…) | `generic-behaviours-interface.md`, `associated-projects.md` |
| Material-property interfaces (generic, generic-parallel) | `generic-material-property-interface.md`, `generic-parallel-material-property-interface.md` |
| Overview of all interfaces | `interfaces.md` |

## Testing and validation

| Topic | Pages |
|---|---|
| **MTest**: material-point simulations, imposed strains and stresses, comparison with references | `mtest.md`, `MTest-keywords.md` |
| Pipes (PTest); nonlinear constraints (Lagrange multipliers) | `ptest.md`, `mtest-nonlinear-constraints.md` |
| MTest Python API | `mtest-python.md` |
| tfel-check (test automation); test generation for solvers | `tfel-check.md`, `mfm-test-generator.md` |
| Performance benchmarks (PLEIADES, Cyrano3, code_aster) | `benchmark.md` |

## Tools, Python, libraries

| Topic | Pages |
|---|---|
| `mfront-query`, `mfront-doc`, `mfm`, madnex files | `mfront-query.md`, `mfront-doc.md`, `mfm.md`, `madnex.md` |
| Compilation of generated libraries | `compiling-mfront-shared-libraries.md` |
| Python modules: tfel, mfront, mtest | `tfel-python.md`, `mfront-python.md`, `mtest-python.md` |
| TFEL/Math: tensors, solvers, numerical integration, interpolation | `math.md`, `tfel-math.md`, `tensors.md`, `tfel-math-numerical-integration.md`, `tfel-math-data-interpolation.md` |
| TFEL/Material, PhysicalConstants, System, Config, MFrontDataBase; using the libraries in C++ | `tfel-material.md`, `tfel-physical-constants.md`, `physical-constants.md`, `TFELSystem.md`, `tfel-config.md`, `tfel-mfront-database.md`, `libraries_usage.md` |
| Contributing, coding guidelines, unit tests, sanitizers, fuzzing | `contributing.md`, `coding-guidelines.md`, `TFELTests.md`, `sanitizers.md`, `testing-fuzzing.md` |
| What changed, by version | `release-notes.md`, `release-notes/` |
