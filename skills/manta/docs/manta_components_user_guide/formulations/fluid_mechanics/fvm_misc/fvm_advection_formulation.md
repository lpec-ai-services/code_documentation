<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_misc/fvm_advection_formulation.html -->

# FVM Advection formulation

## Introduction

This formulation handles the linear advection of a multi-component field with a
definite velocity, using the Finite Volumes Method. Two resolution methods are
available : Explicit or Implicit.

It solves the following equation:

\[\frac{\partial q}{\partial t} + \mathbf{a}(x) \cdot \nabla q = 0\]

with:

- \(q\) the field to advect, with an arbitrary number of components;
- \(a(x)\) the advection velocity, that can vary in space.

## Example of usage

- It is necessary to first define the advection velocity profile (constant here)

```c++
    auto advVelocity = [](ConstRowVectorRef<> &x) {
      Matrix<geoDim, 1> v;
      v(0) = 1.;
      v(1) = 1.;
      return v;
    };
```

- Definition of the explicit formulation

```c++
    auto &fluxForm = rm.make<
        AdvectionExplicitFormulation<geoDim,
                                     nVar,
                                     LeastSquaresLinearReconstructionOperator<geoDim, nVar, BarthJespersenLimitingOperator>>>(
        tube, U, Uvar, advVelocity);
```

- Definition of the implicit formulation

```c++
    auto &implicitAdvForm = rm.make<ImplicitAdvectionFormulation<geoDim, nVar, FVNewtonBEFeatures>>(surf, Q, Qvar, advFunc);
```

## Parameters

### Explicit formulation

`ExplicitAdvectionFormulation` has the following template parameters:

- `geoDim` is the space dimension of the formulation support ;
- `nVar` is the number of variables of field \(q\) ;
- `RecoOperator` specifies the order of reconstruction (PieceWiseConstant,
  Linear) - default = PieceWiseConstant;

`ExplicitAdvectionFormulation` constructor has the following arguments:

- `cells` is the *MeshSet* support of the formulation ;
- `Q` is the *DofVar* associated with the advected field variables ;
- `advFunc` is the lambda function describing the spatial evolution of the
  advection velocity. It returns a `Real` and takes as argument a `RowVector<geoDim>`;
- `limitingArguments` are arguments used for the construction of a limiting
  operator (see [documentation](../limiting_operators/limiting_operators.md#fvm-limiting-arguments)).

### Implicit formulation

`ImplicitAdvectionFormulation` has the following template parameters:

- `geoDim` is the space dimension of the formulation support ;
- `nVar` is the number of variables of field \(q\) ;
- `ImplicitFtrClass` type of implicit time integration algorithm - default = `FVOneStepBEFeatures`;

  Options:

> - `FVNewtonBEFeatures`: Backward Euler with Newton-Raphson algo (fully converged at each time step);
> - `FVNewtonFeatures`: Direct Newton-Raphson (no time marching);
> - `FVOneStepBEFeatures` (default): Backward-Euler for pseudo time marching (no convergency at each time-step)

- `RecoOperator` specifies the order of reconstruction (PieceWiseConstant,
  Linear) - default = PieceWiseConstant;

`ImplicitAdvectionFormulation` constructor has the following arguments:

- `cells` is the *MeshSet* support of the formulation ;
- `Q` is the *DofVar* associated with the advected field variables ;
- `advFunc` is the lambda function describing the spatial evolution of the
  advection velocity. It returns a `Real` and takes as argument a `RowVector<geoDim>`;
- `limitingArguments` are arguments used for the construction of a limiting
  operator (see [documentation](../limiting_operators/limiting_operators.md#fvm-limiting-arguments)).

## Description

Considering each finite volume \(V_i\), we can write the discretized form of the advection equation:

\[V_i (q_i^{n+1} - q_i^{n}) = - dt \sum_{f \in facets} \mathbf{F}(q).\mathbf{n}_f S_f\]

with:

- \(q_i\) the average of field \(q\) on cell i, n and n+1
  corresponding to the current and next time step;
- \(dt\) the time step, computed through the CFL condition;
- \(F(q)\) the flux at each facet f, \(\mathbf{n}_f\) its normal and \(S_f\) its area.

The flux is computed with a first-order upwind scheme, than can be written as:

\[\begin{split}F(q) = \mathbf{F}(q).\mathbf{n}_f = \begin{cases}
\left\vert a \right\vert q_R & if & a = \mathbf{a}(x_f).\mathbf{n}_f < 0 \\
\left\vert a \right\vert q_L & if & a = \mathbf{a}(x_f).\mathbf{n}_f > 0
\end{cases}\end{split}\]

with \(q_L\) and \(q_R\) the average value of \(q\) in respectively
the left and right cell connected to the facet f. The local normal
\(\mathbf{n}_f\) is oriented from the left to the right cell.
