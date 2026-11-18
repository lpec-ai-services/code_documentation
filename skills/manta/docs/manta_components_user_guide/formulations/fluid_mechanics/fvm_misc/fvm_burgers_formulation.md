<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_misc/fvm_burgers_formulation.html -->

# FVM Burgers formulation

## Introduction

This formulation aims at solving the Burgers equation, a classical PDE in
applied mathematics. We consider the non-viscous form, with no diffusion term.
It is written, in conservative form:

\[\frac{\partial q}{\partial t} + \frac{\partial }{\partial x} \left( \frac{1}{2} q^2 \right) = 0\]

with:

- \(q\) a scalar field.

The Finite Volume Method is used for the resolution. An explicit formulation as
well as an implicit one are available.

## Example of usage

- Definition of the explicit formulation

```c++
    auto &U = rm.make<ElementField<nVar, 1>>(tube, "U");
    DofVar Uvar(nVar, "U");
    auto &fluxForm = rm.make<ExplicitBurgersFormulation<>>(tube, U, Uvar);
```

- Definition of the implicit formulation

```c++
    auto &U = rm.make<ElementField<nVar, 1>>(tube, "U");
    DofVar Uvar(nVar, "U");
    auto &fluxForm = rm.make<ImplicitBurgersFormulation<FVNewtonBEFeatures>>(tube, U, Uvar);
```

## Parameters

### Explicit formulation

`ExplicitBurgersFormulation` has the following template parameters:

- `RecoOperator` specifies the order of reconstruction (PieceWiseConstant,
  Linear) - default = PieceWiseConstant;

`ExplicitBurgersFormulation` constructor has the following arguments:

- `cells` is the *MeshSet* support of the formulation ;
- `Q` is the *DofVar* associated with the field \(q\) ;
- `limitingArguments` are arguments used for the construction of a limiting
  operator (see [documentation](../limiting_operators/limiting_operators.md#fvm-limiting-arguments)).

### Implicit formulation

`ImplicitBurgersFormulation` has the following template parameters:

- `ImplicitFtrClass` type of implicit time integration algorithm - default = `FVOneStepBEFeatures`;

  Options:

> - `FVNewtonBEFeatures`: Backward Euler with Newton-Raphson algo (fully converged at each time step);
> - `FVNewtonFeatures`: Direct Newton-Raphson (no time marching);
> - `FVOneStepBEFeatures` (default): Backward-Euler for pseudo time marching (no convergency at each time-step)

- `RecoOperator` specifies the order of reconstruction (PieceWiseConstant,
  Linear) - default = PieceWiseConstant;

`ImplicitBurgersFormulation` constructor has the following arguments:

- `cells` is the *MeshSet* support of the formulation ;
- `Q` is the *DofVar* associated with the field \(q\) ;
- `limitingArguments` are arguments used for the construction of a limiting
  operator (see [documentation](../limiting_operators/limiting_operators.md#fvm-limiting-arguments)).

## Description

Considering each finite volume V_i, we can write the discretized form of the equation:

\[V_i (q_i^{n+1} - q_i^{n}) = - dt \sum_{f \in facets} \mathbf{F}(q).\mathbf{n}_f S_f\]

with:

- \(q_i\) the average of field \(q\) on cell i, n and n+1
  corresponding to the current and next time step;
- \(dt\) the time step, computed through the CFL condition;
- \(F(q)\) the flux at each facet f, \(\mathbf{n}_f\) its normal and \(S_f\) its area.

The flux is computed with Rusanov-like scheme, than can be written as:

\[F(q) = \mathbf{F}(q).\mathbf{n}_f = \frac{1}{2} (F_L + F_R) - \frac{1}{2} \max (\left\vert q_L \right\vert, \left\vert q_R \right\vert) (q_R - q_L)\]

with:

- \(F_L = \frac{1}{2} q_L^2\) and \(F_R = \frac{1}{2} q_R^2\);
- \(q_L\) and \(q_R\) the average value of \(q\) in respectively the left and right cell connected to the facet f. The local normal \(\mathbf{n}_f\) is oriented from the left to the right cell.
