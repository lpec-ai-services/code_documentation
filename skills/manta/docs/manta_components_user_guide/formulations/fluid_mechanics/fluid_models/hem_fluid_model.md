<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fluid_models/hem_fluid_model.html -->

# HEMFluidModel

A `FluidModel` is a structure that defines the physical and mathematical
behavior of a fluid system within Finite Volume formulations for the Euler equations.
It acts as the bridge connecting the conservation laws, the equation of state
(`EOS`), and the numerical Riemann solver.

In particular, a fluid model is responsible for:

- Converting state variables between conservative and primitive forms
  (via the `cons2Prim` and `prim2Cons` methods) ;
- Evaluating quantities such as the local speed of sound ;
- Computing numerical fluxes across mesh facets by solving local Riemann problems.

The `HEMFluidModel` structure describes a model characterizing the fluid via
the Homogeneous EquilibriumModel (HEM) for steam / water mixture. See
[here](../equations_of_state/steam_water.md#epx-tabulated-water-eos) for details on the steam/water equation-of-state.

## Example of usage

To include:

```c++
#include "manta/components-fvm_compressible_fluid_mechanics/fluid_models/hem_fluid_model.h"
```

Usage of the template to instantiate a finite volume formulation:

```c++
  using FluidModel = HEMFluidModel<geoDim, EPXHLLCRiemannSolver<geoDim, EPXTabulatedWaterEOS>>;
  auto &eulerForm  = rm.make<EulerExplicitPipeFormulation<FluidModel>>(tube, eos, U, Uvar, W, areaFunction);
```

## Constructor implementation

```c++
  HEMFluidModel(const EPXTabulatedWaterEOS &eos,
                const MeshSet &cells,
                std::shared_ptr<ReconstructionFacetFieldInterface<geoDim, nVar>> facetField)
    requires(!std::is_abstract_v<RiemannSolverType>)
```

## Parameters

- `geoDim`

  - Space dimension of the support of the formulation
  - Type: `Int`
  - Default value: None
  - Available options:

    - 1
    - 2
    - 3

- `RiemannSolver`

  - Type of Riemann solver : How the flux at facets is computed from left and
    right states ([details](../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-riemann-solvers))
  - Default value: `EPXHLLCRiemannSolver`
  - Available options:

    - `HLLCRiemannSolver`
    - `EPXHLLCRiemannSolver`
    - `RusanovRiemannSolver`

`HEMFluidModel` constructor has the following parameters:

- `eos`: The equation of state, must be of the type `EPXTabulatedWaterEOS` ;
- `cells`: The mesh set containing the cells over which the fluid model is
  defined ;
- `facetField`: The facet field encapsulating the primitive variables.

## Description

This model assumes that steam and water are homogeneous and at equilibrium.
Steam and liquid water have the same temperature, pressure and velocity.
Additional variables such as the vapor mass fraction characterizes the phase
repartition between vapor and liquid water.

As for the single fluid model (see [SingleFluidModel](single_fluid_model.md#single-fluid-model)), it implies the
computation, on each control volume \(V\), of the evolution of the
Conservative state \(\mathbf{U} = {[{\rho}, {\rho} \mathbf{u}, {\rho} E]}^T\).
