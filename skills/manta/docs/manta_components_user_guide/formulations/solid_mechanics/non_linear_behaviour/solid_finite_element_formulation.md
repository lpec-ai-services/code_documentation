<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/non_linear_behaviour/solid_finite_element_formulation.html -->

# `SolidFiniteElementFormulation` (implicit and explicit solid mechanics)

## Introduction

This formulation computes the contribution of the internal forces of a solid material to
the residual and jacobian terms of a finite-element problem. It relies on an external
MFront behavior (see [MFrontBehaviorComponent](../../../main_user_concepts/user_guide_objects/mfront_behavior_component.md#mfront-behavior-component)).

The same class is used both for the implicit (Newton) resolution and, assembled on the
right-hand side only, for explicit dynamics.

## Example of usage

The following includes are required:

```c++
#include "manta/components-modeling/mechanics/solid_finite_element_formulation.h"
#include "manta/components-behavior/mfront_behavior_component.h"
```

It is constructed with:

```c++
    auto &solidImplicitForm = rm.make<SolidFiniteElementFormulation<planeStrain, MFrontBehaviorComponent, cellShapeId, true>>(
        beam, cellQuadId, Uvar, U, behaviorConcrete);
```

## Parameters

`SolidFiniteElementFormulation` has four template parameters:

- `planeStrain`, the geometric (structural) hypothesis,
- `MFrontBehaviorComponent`, the behavior type,
- `cellShapeId`, the shape ID,
- `true`, the `fs` (*finite strain*) switch: `true` selects a finite strain behavior while `false` uses small strain hypothesis.

`SolidFiniteElementFormulation` has five parameters:

- `beam`, the meshSet on which the formulation is defined,
- `cellQuadId`, the quadrature rule used to integrate the formulation,
- `Uvar`, the dofVar associated with the unknown (displacement for the
  implicit scheme, acceleration for the explicit one),
- `U`, the displacement nodeField
- `behaviorConcrete`, the `MFrontBehaviorComponent` instance.

## Defining a non-linear material

Here is an example of behavior declaration:

```c++
    // > create the behavior
    OMap<std::string, Vector<Real>> matp;

    matp["YoungModulus"]   = {YoungModulusCharpy};
    matp["PoissonRatio"]   = {PoissonRatioCharpy};
    matp["HardeningSlope"] = {HCharpy};
    matp["YieldStrength"]  = {sy0Charpy};
    matp["H"]              = {HCharpy};
    matp["sy0"]            = {sy0Charpy};
    MFrontBehaviorComponent behaviorCharpy(
        charpy, GeoType::hex8, QuadId::hex8, "./libCharpyBehaviours-generic.so", behaviorCharpyName, "Tridimensional", matp);
    // <
```

The number of behavior and material parameters depends on the specific behavior. More
details can be found [in this section](../../../main_user_concepts/user_guide_objects/mfront_behavior_component.md#mfront-behavior-component).

Note that the behavior state must be updated when the user wants to
confirm the convergence of a given time-step by calling
`update()` on the formulation.

## Specificities for Implicit mechanics

### Description

This formulation is used in the context of the non-linear resolution of the behavior of a
solid material. It aims at solving for the displacement field \(\v{u}\) by reaching a
null residual of the form:

\[\mathbb{R}\paren{\ets{\v{u}}} = \mathbb{F}_{e}\paren{\ets{\v{u}}} - \mathbb{F}_{i}\paren{\ets{\v{u}}}\]

usually solved with a Newton algorithm:

\[\v{u}^{(n+1)} = \v{u}^{(n)}-\left(\pdfrac{\mathbb{R}}{\v{u}}\right)^{-1}\,\mathbb{R}\paren{\v{u}^{(n)}}\]

This formulation computes the contribution of the internal forces \(\mathbb{F}_{i}\)
to the residual \(\mathbb{R}\) and to the jacobian \(\pdfrac{\mathbb{R}}{\v{u}}\).

## Specificities for Explicit dynamics

For explicit dynamics the formulation is assigned to the **right-hand side** of the linear
system (`assignFormulationToRHSOfLinearSystem`). The formulation is usually used along
with two classes

- `HRZMassMatrixFormulation<hypothesis, ShapeId>`, to compute the mass matrix term
- `CriticalTimeStepComputer(meshSet, rho, youngModulus)`, to use
  `getCriticalTimeStep()`

Here is an example of the declaration and assignation of formulations of solid mechanics in a dynamic explicit context:

```c++
    MFrontBehaviorComponent behavior(beam, GeoType::hex8, QuadId::hex8, libBehavior, "plasticity_gl", "Tridimensional", matp);

    auto &solidExplicitForm =
        rm.make<SolidFiniteElementFormulation<tridimensional, MFrontBehaviorComponent, ShapeId::hex8, true>>(
            beam, QuadId::hex8, Gvar, U, behavior);

    auto &massMatrixForm = rm.make<HRZMassMatrixFormulation<tridimensional, ShapeId::hex8>>(beam, Gvar, rho);

    auto &feSystem = rm.make<DiagonalLinearSystem>("FESystem", mesh);

    rm.assignFormulationToRHSOfLinearSystem(solidExplicitForm, feSystem);
    rm.assignFormulationToLinearSystem(massMatrixForm, feSystem);
```

### Description

This formulation allows to compute the contribution to the LHS and RHS of a
solid mechanics mass matrix, and its
behavior dependant internal force vector. In a solid mechanics
explicit context the system to solve can be thought of as:

\[\boldsymbol{M} \boldsymbol{\ddot{U}} = \boldsymbol{F}_e - \boldsymbol{F}_i\]

where,

\[\boldsymbol{M} = \int_{\Omega} \rho \transpose{\boldsymbol{N}} \boldsymbol{N} dV\]

\[\boldsymbol{F}_i = \int_{\Omega} \transpose{\boldsymbol{B}} \dfrac{\psi}{\transpose{\boldsymbol{F}}} dV\]

with \(\boldsymbol{N}\), defined as the shape functions along with their gradient \(\boldsymbol{B}\),
\(\rho\) the mass density, \(\psi\) the strain energy density and \(\boldsymbol{F}\) the deformation gradient.

\(\boldsymbol{F}_e\), the external force vector, is not computed using this formulation.

In the end, the computes the `HRZMassMatrixFormulation<hypothesis, ShapeId>` computes the
contribution of \(\boldsymbol{M}\) the mass matrix term,
andthe `SolidFiniteElementFormulation` computes \(\boldsymbol{F}_i\), the internal force vector term.

### Time-integration

Explicit dynamics usually need a numerical time-integration scheme. A description of
`TimeIntegrators` can be found in [this catalog](../../../../catalogs/components/physics_catalog_theme.md#physics-catalog-theme). Note that,
as a result, three field should generally be initialized to work with solid explicit mechanics:
\(U\), \(V\), \(G\), respectively displacement, velocity, and acceleration.

### `CriticalTimeStepComputer`

Before the call to `rm.init()`, one can declare one, or several `CriticalTimeStepComputer`.
They are mesh and material dependant. As such they are constructed as:

```c++
    CriticalTimeStepComputer criticalTimeStepComputer(beam, rho, YoungModulus);
```

With the following three parameters:

- `beam`, the meshSet on which the step is computed,
- `rho`, the material's density,
- `YoungModulus`, the material's Young Modulus.

The critical time step is therefore estimated as

\[\Delta t_{\mathrm{crit}}
\;=\; \min_{l_c}\; \sqrt{\dfrac{E}{\rho}}\]

with

- \(l_c\) the characteristic length of element \(e\) (its
  shortest edge),
  \(E\) the Young modulus and \(\rho\) the mass density.

The time step can be computed during the simulation

```c++
        dtCrit = criticalTimeStepComputer.getCriticalTimeStep();
```

Note

At the moment, \(\Delta t_{\mathrm{crit}}\) is evaluated once, at initialisation,
from the undeformed mesh and the constant elastic modulus and density.

## List of examples and tests

- the [Charpy commented example](../../../../demos/components_examples/contact_and_impact/charpy.md#example-3d-charpy),
- `examples/implicit/damage_mazars/notched_beam/` and most implicit and explicit
  examples,
- the phase-field tests,
- `src/components/modeling/tests/e2e/nr` (`plasticube`, `rev`, `strip2D`, ...).

## Notes

Developer details about this formulations are available in a blueprint page dedicated
to the solid mechanics formulations, in [this page](../../../../developer_guide/blueprints/solid_mechanics_formulations_blueprint.md#solid-mechanics-formulations-blueprint) of the developer guide.
