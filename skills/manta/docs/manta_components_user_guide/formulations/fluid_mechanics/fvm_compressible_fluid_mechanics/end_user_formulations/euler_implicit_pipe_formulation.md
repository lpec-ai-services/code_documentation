<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/end_user_formulations/euler_implicit_pipe_formulation.html -->

# Euler Implicit Pipe Formulation

## Introduction

`EulerImplicitPipeFormulation` is used to solve compressible inviscid
flows (Euler equations) in pipe systems or fully 1D systems, with the Finite
Volume method and an explicit or implicit time scheme.

Euler pipe formulations share most of the features of [Euler Implicit
Formulation](euler_implicit_formulation.md#euler-implicit-formulation), considering geoDim = 1. It adds source
terms managing a varying section of the pipe (or a nozzle).

This formulation can be used with every fluid model currently available in MANTA:

- [Single constituent](../../fluid_models/single_fluid_model.md#single-fluid-model),
- [HEM model](../../fluid_models/hem_fluid_model.md#hem-fluid-model) for [steam/water](../../equations_of_state/steam_water.md#water-eos) mixture,
- 5-equations [multi-component](../../fluid_models/mcsg_fluid_model.md#mcsg-fluid-model) model

The implicit Euler pipe formulation is only available for a **full 1D mesh** (only
along the x-coordinate).

## Example of usage

to include:

```c++
#include "manta/components-fvm_compressible_fluid_mechanics/pipe/end_user_formulations.h"
```

Here is the construction of an implicit formulation (nozzle).

```c++
    const PerfectGasEOS eos(gamma);

    using FluidModel = SingleFluidModel<1, 0, PerfectGasEOS, HLLCRiemannSolver<1, PerfectGasEOS>>;
    using RecoOp     = PieceWiseConstantReconstructionOperator<1, 3>;
    using Form       = EulerImplicitPipeFormulation<FluidModel, RecoOp, HLLCExactJacobianIntegrand>;
    auto &fluxForm   = rm.make<Form>(cells, eos, U, Uvar, W, areaFunction);
```

The variable *areaFunction* designates a lambda which gives \(S(x)\),
the section value depending on the mean path coordinate.

```c++
    // This lambda defines the geometry of the nozzle by defining the area as a function of the distance to pipe extremity
    auto areaFunction = [&L](const RowVector<3> &x) {
      const Real s = norm(x) / L;    // assume mesh lives on the straight-axis, intersecting (0,0), and is of length L.
      Real area;
      if (s < 0.5) {
        area = 1.75 - 0.75 * std::cos((2. * s - 1.) * std::numbers::pi);
      }
      else {
        area = 1.25 - 0.25 * std::cos((2. * s - 1.) * std::numbers::pi);
      }
      return Matrix<1, 1>(area);
    };
```

## Constructors implementation

Here are the different possible calls to the constructors:

```c++
  EulerImplicitPipeFormulation(const MeshSet &cells,
                               const EOS &eos,
                               FieldRef<ElementField<nVar, 1>> U,
                               const DofVar &Uvar,
                               FieldRef<ElementField<nVar, 1>> W,
                               std::function<Matrix<1, 1>(ConstRowVectorRef<> &x)> surfFunc,
                               LimitingArguments limitingArguments = LimitingArguments{})
    requires(!std::is_abstract_v<RecoOperatorType>)
```

```c++
  EulerImplicitPipeFormulation(const MeshSet &cells,
                               const EOS &eos,
                               FieldRef<ElementField<nVar, 1>> U,
                               const DofVar &Uvar,
                               FieldRef<ElementField<nVar, 1>> W,
                               std::shared_ptr<ReconstructionFacetFieldInterface<1, nVar>> facetField,
                               std::function<Matrix<1, 1>(ConstRowVectorRef<> &x)> surfFunc)
```

## Parameters

`EulerImplicitPipeFormulation` has the following template parameters:

### `FluidModelType`

Type of the fluid model. Available options:

- [SingleFluidModel](../../fluid_models/single_fluid_model.md#single-fluid-model)
- [HEMFluidModel](../../fluid_models/hem_fluid_model.md#hem-fluid-model)
- [MCSGFluidModel](../../fluid_models/mcsg_fluid_model.md#mcsg-fluid-model)

### `RecoOperatorType`

Type of the reconstruction operator. Available options:

- [PieceWiseConstantReconstructionOperator](../../reconstruction_operators/reconstruction_operators.md#piecewise-constant-reconstruction-operator) (default)
- [LeastSquaresLinearReconstructionOperator](../../reconstruction_operators/reconstruction_operators.md#linear-reconstruction-operator)

### `JacobianIntegrand`

- specifies how the terms of the Jacobian matrices are computed (derivatives of
  the fluxes with respect to the left and right states)
  ([details](../../../../../theory_manual/fluid_mechanics/jacobian_computation.md#euler-jacobian))
- Default value: `HLLCExactJacobianIntegrand`
- Available options:

  - `RoeJacobianIntegrand`: computes the Jacobians using Roe RiemannSolver;
  - `RusanovJacobianIntegrand`: computes the Jacobians using Rusanov RiemannSolver;
  - `HLLCJacobianIntegrand`: computes the Jacobians using HLLC RiemannSolver;
  - `HLLCExactJacobianIntegrand` (default): exactly computes the Jacobians using HLLC RiemannSolver;
  - `FiniteDifferencesJacobianIntegrand`: computes the Jacobians by perturbation;

### `ImplicitFtrClass`

- Type of implicit time integration algorithm
- Default value: `FVOneStepBEFeatures`
- Available options:

> - `FVNewtonBEFeatures`: Backward Euler with Newton-Raphson algo (fully converged at each time step);
> - `FVNewtonFeatures`: Direct Newton-Raphson (no time marching);
> - `FVOneStepBEFeatures` (default): Backward-Euler for pseudo time marching (no convergency at each time-step)

Note

The space dimension `geoDim` is necessarily `1`

### Constructors

The `EulerImplicitPipeFormulation` constructors accept the following arguments:

- `cells` is the *MeshSet* support of the formulation ;
- `eos` is the equation of state (its type must match the fluid model) ;
- `stateCons` is the *DofVar* associated with the conservative
  variables ;
- `statePrim` is the *field* of primitive variables ;
- `surfFunc` is a `lambda function` describing the evolution of the
  pipe section along the coordinates (3D). The lambda return a `Real` and
  takes a `RowVector<geoDim>` (for the position in space) as input ;
- `facetField` is the shared pointer of the *ReconstructionFacetField* ;
- `limitingArguments` are arguments used for the construction of a limiting
  operator (see [documentation](../../limiting_operators/limiting_operators.md#fvm-limiting-arguments)).

The number of variables of `stateCons` and `statePrim` is given by the
type of the fluid model (e.g. `geoDim + 2` for a single-component fluid).

## List of commented examples and verification tests

*Nozzle (steady solution)*

- [Converging-diverging Nozzle](../../../../../verification_tests/manta_components_verification_tests/compressible_fluid_mechanics/nozzle/nozzle.md#verif-nozzle)

## Description

Details on Euler equations and the FV numerical scheme can be found
[here](../../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#compressible-fluid-mechanics). Additional information on varying
section features and Euler pipe formulations can be found in the [theory
manual](../../../../../theory_manual/fluid_mechanics/varying_section_1d.md#euler-varying-section-1d).

The model for Euler 1D formulation with varying section can be derived from the
3D Euler equations, under the following assumptions:

- The flow has an unambiguous single locally dominant characteristic length:
  typically a pipe with small section.
- The section varies smoothly (no edge, no drastic change in section)
- The pipe is rigid. Namely, the pipe's section is fixed over time
- The model behaves as if the pipe was straight. If the pipe is curved, the
  deviation of the fluid do not exert any force on the pipe.

Let \(\mathbf{U} = {[{\rho}, {\rho} u, {\rho} E]}^T\) be the mean
conservative state (density, momentum, total energy) of a cell of the 1D mesh
(all quantities below are related to this same cell).

\[\frac {d}{dt} \mathbf{U} = \frac 1 V \left( S_L \mathbf{F_L} - S_R \mathbf{F_R} + \mathbf{C} \right)\]

with :

- \(S_L\) and \(S_R\) the left and right section areas.
- \(\mathbf{F_L}\) and \(\mathbf{F_R}\) the left and right 1D fluxes (estimated through Riemann solvers).
- \(\mathbf{C}\) the momentum source term due to varying sections (with p the average pressure in the cell)

\[\begin{split}\mathbf{C} =
\begin{pmatrix}
0 \\
p (S_R - S_L) \\
0
\end{pmatrix}\end{split}\]

- and \(V\) as the volume of the cells:

\[V = \int_a^b S(x) dx = \frac {\Delta x}{3} (S_L + S_R + \sqrt{S_L S_R})\]

The volume \(V\) is fixed in an Eulerian grid. It uses the section at each
facet to compute the volume of the truncated cone corresponding to each pipe
segment.

In order to find the steady state solution of the previous equation, if we call
\(\mathbf{L(U)}\) the RHS of this equation, we need to solve:

\[\mathbf{L(U)} = 0\]

Three implicit time integration schemes are available:

### `FVNewtonFeatures`

We directly solve \(\mathbf{L(U)} = 0\) with a Newton-Raphson algorithm, no
time-stepping. It implies the computation of the Jacobian \(A =\frac{\partial \mathbf{L(U)}}{\partial \mathbf{U}}\)

### `FVOneStepBEFeatures`

We solve:

\[\frac{\mathbf{U}^{n+1} - \mathbf{U}^{n}}{dt} + \mathbf{L}(\mathbf{U}^{n+1}) = 0\]

by doing a linearization at each time step.

\[\frac{1}{dt} + \frac{\partial \mathbf{L}(\mathbf{U}^{n})}{\partial \mathbf{U}} \Delta \mathbf{U}^{n+1} = - \mathbf{L}(\mathbf{U}^{n})\]

### `FVNewtonBEFeatures`

We solve:

\[\frac{\mathbf{U}^{n+1} - \mathbf{U}^n}{dt} + \mathbf{L}(\mathbf{U}^{n+1}) = 0\]

by doing a Newton algorithm at each time step.

\[\frac{1}{dt} + \frac{\partial \mathbf{L}(\mathbf{U}^{k})}{\partial \mathbf{U}} \Delta \mathbf{U}^{k+1} = - \frac{1}{dt} (\mathbf{U}^{k} - \mathbf{U}^{n}) - \mathbf{L}(\mathbf{U}^{k})\]

k being the Newton iteration. \(\mathbf{U}^{k=0} = \mathbf{U}^{n}\)

Stop criterion: \(|| \frac{1}{dt} (\mathbf{U}^{k} - \mathbf{U}^{n}) + \mathbf{L}(\mathbf{U}^{k}) || < \epsilon\)
