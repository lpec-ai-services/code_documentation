<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/end_user_formulations/euler_explicit_pipe_formulation.html -->

# Euler Explicit Pipe Formulation

## Introduction

`EulerExplicitPipeFormulation` is used to solve compressible inviscid
flows (Euler equations) in pipe systems or fully 1D systems, with the Finite
Volume method and an explicit or implicit time scheme.

Euler pipe formulations share most of the features of [Euler Explicit
Formulation](euler_explicit_formulation.md#euler-explicit-formulation), considering geoDim = 1. It adds
features to handle 3D orientation of the curvilinear mesh (pipe network, gravity
source terms...), as well as source terms managing a varying section of the pipe
(or a nozzle).

This formulation can be used with every fluid model currently available in MANTA:

- [Single constituent](../../fluid_models/single_fluid_model.md#single-fluid-model),
- [HEM model](../../fluid_models/hem_fluid_model.md#hem-fluid-model) for [steam/water](../../equations_of_state/steam_water.md#water-eos) mixture,
- 5-equations [multi-component](../../fluid_models/mcsg_fluid_model.md#mcsg-fluid-model) model

## Example of usage

to include (for both implicit and explicit formulations):

```c++
#include "manta/components-fvm_compressible_fluid_mechanics/pipe/end_user_formulations.h"
```

Here is the construction of an explicit formulation.

```c++
    PerfectGasEOS eos(gamma);
    using FluidModel = SingleFluidModel<1, 0, decltype(eos), HLLCRiemannSolver<geoDim, decltype(eos)>>;
    using Form       = EulerExplicitPipeFormulation<FluidModel>;
    auto &fluxForm   = rm.make<Form>(cells, eos, U, Uvar, W, leftBoundary, areaFunction);
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
  EulerExplicitPipeFormulation(const MeshSet &cells,
                               const EOS &eos,
                               FieldRef<ElementField<nVar, 1>> U,
                               const DofVar &Uvar,
                               FieldRef<ElementField<nVar, 1>> W,
                               std::function<Matrix<1, 1>(ConstRowVectorRef<> &x)> surfFunc,
                               LimitingArguments limitingArguments = LimitingArguments{})
    requires(!std::is_abstract_v<RecoOperatorType>)
```

```c++
  EulerExplicitPipeFormulation(const MeshSet &cells,
                               const EOS &eos,
                               FieldRef<ElementField<nVar, 1>> U,
                               const DofVar &Uvar,
                               FieldRef<ElementField<nVar, 1>> W,
                               std::shared_ptr<ReconstructionFacetFieldInterface<1, nVar>> facetField,
                               std::function<Matrix<1, 1>(ConstRowVectorRef<> &x)> surfFunc)
```

```c++
  EulerExplicitPipeFormulation(const MeshSet &cells,
                               const EOS &eos,
                               FieldRef<ElementField<nVar, 1>> U,
                               const DofVar &Uvar,
                               FieldRef<ElementField<nVar, 1>> W,
                               const MeshSet &pipeBeginnings,
                               std::function<Matrix<1, 1>(ConstRowVectorRef<> &x)> surfFunc,
                               LimitingArguments limitingArguments = LimitingArguments{})
    requires(!std::is_abstract_v<RecoOperatorType>)
```

```c++
  EulerExplicitPipeFormulation(const MeshSet &cells,
                               const EOS &eos,
                               FieldRef<ElementField<nVar, 1>> U,
                               const DofVar &Uvar,
                               FieldRef<ElementField<nVar, 1>> W,
                               std::shared_ptr<ReconstructionFacetFieldInterface<1, nVar>> facetField,
                               const MeshSet &pipeBeginnings,
                               std::function<Matrix<1, 1>(ConstRowVectorRef<> &x)> surfFunc)
```

## Parameters

`EulerExplicitPipeFormulation` has the following template parameters:

- `FluidModelType`: Type of the fluid model. Available options:

  - [SingleFluidModel](../../fluid_models/single_fluid_model.md#single-fluid-model)
  - [HEMFluidModel](../../fluid_models/hem_fluid_model.md#hem-fluid-model)
  - [MCSGFluidModel](../../fluid_models/mcsg_fluid_model.md#mcsg-fluid-model)
- `RecoOperatorType`: Type of the reconstruction operator. Available options:

  - [PieceWiseConstantReconstructionOperator](../../reconstruction_operators/reconstruction_operators.md#piecewise-constant-reconstruction-operator) (default)
  - [LeastSquaresLinearReconstructionOperator](../../reconstruction_operators/reconstruction_operators.md#linear-reconstruction-operator)

Note

The space dimension `geoDim` is necessarily `1`

### Constructor arguments

Two type constructors exist, with the same template parameters. They differentiate the
case of a full 1D mesh from a 1D mesh in 3D space (for pipe systems).

`EulerExplicitPipeFormulation` first constructor is used for a **fully 1D
mesh** (Only the x-coordinate matters). It has the following arguments:

- `cells` is the *MeshSet* support of the formulation ;
- `eos` is the equation of state (its type must match the fluid model) ;
- `stateCons` is the *DofVar* associated with the conservative
  variables ;
- `statePrim` is the *field* of primitive variables ;
- `surfFunc` is a `lambda function` describing the evolution of the
  pipe section along the coordinates (3D). The lambda return a `Real` and
  takes a `RowVector<geoDim>` (for the position in space) as input ;
- `facetField` is the shared pointer of the *ReconstructionFacetField*;
- `limitingArguments` are arguments used for the construction of a limiting
  operator (see [documentation](../../limiting_operators/limiting_operators.md#fvm-limiting-arguments)).

`EulerExplicitPipeFormulation` second constructor is needed for a **1D
mesh in 3D space** (Pipe system). It has the following arguments:

- `cells` is the *MeshSet* support of the formulation ;
- `eos` is the equation of state (its type must match the fluid model) ;
- `stateCons` is the *DofVar* associated with the conservative
  variables ;
- `statePrim` is the *field* of primitive variables ;
- `pipeBeginnings` is a meshSet regrouping every facet representing the
  beginning of a pipe chunk. This group can be created inside the mesh or
  through an union meshSet in MANTA.
- `surfFunc` is a `lambda function` describing the evolution of the
  pipe section along the coordinates (3D). The lambda return a `Real` and
  takes a `RowVector<geoDim>` (for the position in space) as input ;
- `facetField` is the shared pointer of the *ReconstructionFacetField*;
- `limitingArguments` are arguments used for the construction of a limiting
  operator (see [documentation](../../limiting_operators/limiting_operators.md#fvm-limiting-arguments)).

The number of variables of `stateCons` and `statePrim` is given by the
type of the fluid model (e.g. `geoDim + 2` for a single-component fluid).

Note

This last constructor is necessary to compute flows in a pipe system. Pipe
chunks are uninterrupted chain of segments linked together by boundary
conditions elements. The orientation of the pipe is independant of how the mesh
was constructed. The user has to define in which direction the flow velocity is
considered positive (from the beginning to the end of the pipe), by providing
the list (as a *meshSet*) of facets as pipe chunks beginnings. MANTA
handles then the consistency of the orientation along each chunk.

## List of commented examples and verification tests

*1D shocktube*

- [Liquid shocktube](../../../../../verification_tests/manta_components_verification_tests/compressible_fluid_mechanics/shocktube/liquid_shocktube/liquid_shocktube.md#verif-fvm-liquid-shocktube)
- [Air shocktube](../../../../../verification_tests/manta_components_verification_tests/compressible_fluid_mechanics/shocktube/air_shocktube/air_shocktube.md#verif-fvm-air-shocktube)

*Boundary conditions*

- [Tank boundary condition](../../../../../verification_tests/manta_components_verification_tests/compressible_fluid_mechanics/tank_bc/tank_bc.md#verif-fvm-tank-bc)

*source terms*

- [Liquid column with gravity](../../../../../verification_tests/manta_components_verification_tests/compressible_fluid_mechanics/gravity/gravity.md#verif-liquid-column-gravity)

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
