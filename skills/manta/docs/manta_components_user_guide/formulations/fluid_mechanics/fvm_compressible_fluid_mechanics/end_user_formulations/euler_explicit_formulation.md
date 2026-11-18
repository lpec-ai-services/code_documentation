<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/end_user_formulations/euler_explicit_formulation.html -->

# Euler Explicit Formulation

## Introduction

`EulerExplicitFormulation` is used to solve compressible inviscid flows (Euler equations)
with the Finite Volume method and an *explicit* time scheme.

This formulation can be used with every fluid model currently available in MANTA:

- [Single constituent](../../fluid_models/single_fluid_model.md#single-fluid-model),
- [HEM model](../../fluid_models/hem_fluid_model.md#hem-fluid-model) for [steam/water](../../equations_of_state/steam_water.md#water-eos) mixture,
- 5-equations [multi-component](../../fluid_models/mcsg_fluid_model.md#mcsg-fluid-model) model

## Example of usage

to include:

```c++
#include "manta/components-fvm_compressible_fluid_mechanics/euler_explicit_formulation.h"
```

Here is an example for a 2D shocktube with a single fluid (Perfect gas) - second
order in space

```c++
    // eqauation of state
    PerfectGasEOS eos(gamma);
    // formulation constructor
    using FluidModel = SingleFluidModel<geoDim, 0, PerfectGasEOS, HLLCRiemannSolver<geoDim, PerfectGasEOS>>;
    using RecoOp     = LeastSquaresLinearReconstructionOperator<geoDim, nVar, DuboisLimitingOperator>;

    auto &eulerForm =
        rm.make<EulerExplicitFormulation<FluidModel, RecoOp>>(tube, eos, U, Uvar, W, LimitingArguments{.k = 0.75});
```

## Constructors implementation

Here are the different possible calls to the constructors:

```c++
  EulerExplicitFormulation(const MeshSet &cells,
                           Int facetQuadOrder,
                           const EOS &eos,
                           FieldRef<ElementField<nVar, 1>> stateCons,
                           const DofVar &stateConsVar,
                           FieldRef<ElementField<nVar, 1>> statePrim,
                           LimitingArguments limitingArguments = LimitingArguments{})
```

```c++
  EulerExplicitFormulation(const MeshSet &cells,
                           const EOS &eos,
                           FieldRef<ElementField<nVar, 1>> stateCons,
                           const DofVar &stateConsVar,
                           FieldRef<ElementField<nVar, 1>> statePrim,
                           LimitingArguments limitingArguments = LimitingArguments{})
```

```c++
  EulerExplicitFormulation(const MeshSet &cells,
                           const EOS &eos,
                           FieldRef<ElementField<nVar, 1>> stateCons,
                           const DofVar &stateConsVar,
                           FieldRef<ElementField<nVar, 1>> statePrim,
                           std::shared_ptr<RecoFieldType> facetField)
```

## Parameters

`EulerExplicitFormulation` has the following template parameters:

- `FluidModelType`: Type of the fluid model. Available options:

  - [SingleFluidModel](../../fluid_models/single_fluid_model.md#single-fluid-model)
  - [HEMFluidModel](../../fluid_models/hem_fluid_model.md#hem-fluid-model)
  - [MCSGFluidModel](../../fluid_models/mcsg_fluid_model.md#mcsg-fluid-model)
- `RecoOperatorType`: Type of the reconstruction operator. Available options:

  - [PieceWiseConstantReconstructionOperator](../../reconstruction_operators/reconstruction_operators.md#piecewise-constant-reconstruction-operator) (default)
  - [LeastSquaresLinearReconstructionOperator](../../reconstruction_operators/reconstruction_operators.md#linear-reconstruction-operator)

### Constructors

The `EulerExplicitFormulation` constructors accept the following arguments:

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

- [Multi-D shocktube](../../../../../verification_tests/manta_components_verification_tests/compressible_fluid_mechanics/shocktube/multi_d_shocktube.md#verif-multid-shocktube)
- [Sod shocktube](../../../../../verification_tests/manta_components_verification_tests/compressible_fluid_mechanics/shocktube/sod_shocktube.md#verif-sod-shocktube)

## Description

This formulation manages the resolution of compressible inviscid flows (Euler
equations) with a Finite Volume scheme, for a single-component fluid.

It implies the computation, on each control volume \(V\), of the evolution
of the Conservative state \(\mathbf{U} = {[{\rho}, {\rho} \mathbf{u}, {\rho} E]}^T\).

\[\mathbf{U}^{n+1} = \mathbf{U}^{n} - \frac{dt}{V} \sum_{f \in facets} \mathbf{F}(\mathbf{U}_f^{n}).\mathbf{n}_f S_f\]

Details on equations and the FV numerical scheme can be found [here](../../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#compressible-fluid-mechanics).

Such a formulation combines every term of the equation, containing components to:

- compute the volume \(V\) of the cells (fixed in an Eulerian grid)
- compute the fluxes \(\mathbf{F}(\mathbf{U}_f).\mathbf{n}_f S_f\) exchanged between the cells
- provide the critical time step \(dt\), for the explicit time scheme.
