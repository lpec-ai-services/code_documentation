<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/end_user_formulations/euler_implicit_formulation.html -->

# Euler Implicit Formulation

## Introduction

`EulerImplicitFormulation` is used to solve compressible inviscid flows
(Euler equations) with the Finite Volume method and an *implicit* time scheme.
It is typically used to determine a steady-state solution of the equations.

This formulation can be used with every fluid model currently available in MANTA:

- [Single constituent](../../fluid_models/single_fluid_model.md#single-fluid-model),
- [HEM model](../../fluid_models/hem_fluid_model.md#hem-fluid-model) for [steam/water](../../equations_of_state/steam_water.md#water-eos) mixture,
- 5-equations [multi-component](../../fluid_models/mcsg_fluid_model.md#mcsg-fluid-model) model

## Example of usage

to include:

```c++
#include "manta/components-fvm_compressible_fluid_mechanics/euler_implicit_formulation.h"
```

Here is an example for constructing an Euler implicit formulation:

```c++
  // equation of state
  PerfectGasEOS eos{gamma};
  // End-user formulation constructor
  using FluidModel = SingleFluidModel<geoDim, 0, PerfectGasEOS, RiemannSolver_<geoDim, PerfectGasEOS>>;
  // tag::reconstructionOp
  using RecoOp = PieceWiseConstantReconstructionOperator<geoDim, nVar>;
  // end::reconstructionOp
  using Form     = EulerImplicitFormulation<FluidModel, RecoOp, JacobianIntegrand_>;
  auto &fluxForm = rm.make<Form>(surf, eos, U, Uvar, W);
```

## Constructors implementation

Here are the different possible calls to the constructors:

```c++
  EulerImplicitFormulation(const MeshSet &cells,
                           const EOS &eos,
                           FieldRef<ElementField<nVar, 1>> stateCons,
                           const DofVar &stateConsVar,
                           FieldRef<ElementField<nVar, 1>> statePrim,
                           std::shared_ptr<RecoFieldType> facetField)
```

```c++
  EulerImplicitFormulation(const MeshSet &cells,
                           Int facetQuadOrder,
                           const EOS &eos,
                           FieldRef<ElementField<nVar, 1>> stateCons,
                           const DofVar &stateConsVar,
                           FieldRef<ElementField<nVar, 1>> statePrim,
                           LimitingArguments limitingArguments = LimitingArguments{})
```

```c++
  EulerImplicitFormulation(const MeshSet &cells,
                           const EOS &eos,
                           FieldRef<ElementField<nVar, 1>> stateCons,
                           const DofVar &stateConsVar,
                           FieldRef<ElementField<nVar, 1>> statePrim,
                           LimitingArguments limitingArguments = LimitingArguments{})
```

## Parameters

`EulerImplicitFormulation` has the following template parameters:

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

### Constructors

The `EulerImplicitFormulation` constructors accept the following arguments:

- `cells` is the *MeshSet* support of the formulation ;
- `facetQuadOrder` quadrature order for integrating on the facet ;
- `eos` is the equation of state (its type must match the fluid model) ;
- `stateCons` is the *DofVar* associated with the conservative
  variables ;
- `statePrim` is the *field* of primitive variables ;
- `limitingArguments` are arguments used for the construction of a limiting
  operator (see [documentation](../../limiting_operators/limiting_operators.md#fvm-limiting-arguments)) ;
- `facetField` is the shared pointer of the *ReconstructionFacetField*.

The number of variables of `stateCons` and `statePrim` is given by the
type of the fluid model (e.g. `geoDim + 2` for a single-component fluid).

## List of commented examples and verification tests

*Subsonic bump*

- [Subsonic bump](../../../../../verification_tests/manta_components_verification_tests/compressible_fluid_mechanics/subsonic_bump/subsonic_bump.md#verif-subsonic-bump)

## Description

This formulation manages the resolution of a compressible inviscid flow (Euler
equations) with a Finite Volume scheme and an implicit time integration scheme.
The purpose is to find the steady-state solution of the equations:

\[\frac {\partial \mathbf{U}}{\partial t} + \nabla \cdot \mathbf{F(U)} = 0\]

\[\mathbf{L(U)} = 0\]

With :

- \(\mathbf{U} = {[{\rho}, {\rho} \mathbf{u}, {\rho} E]}^T\) the conservative state
- \(\mathbf{L(U)} = \nabla \cdot \mathbf{F(U)}\), with \(\mathbf{F(U)}\) the associated fluxes.

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
