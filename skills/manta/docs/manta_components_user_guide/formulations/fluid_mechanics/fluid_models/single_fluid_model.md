<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fluid_models/single_fluid_model.html -->

# SingleFluidModel

A `FluidModel` is a structure that defines the physical and mathematical
behavior of a fluid system within Finite Volume formulations for the Euler equations.
It acts as the bridge connecting the conservation laws, the equation of state
(`EOS`), and the numerical Riemann solver.

In particular, a fluid model is responsible for:

- Converting state variables between conservative and primitive forms
  (via the `cons2Prim` and `prim2Cons` methods) ;
- Evaluating quantities such as the local speed of sound ;
- Computing numerical fluxes across mesh facets by solving local Riemann problems.

The `SingleFluidModel` structure describes a compressible one-phase fluid.
That fluid may transport species in a passive way.

The system of equations is described in [Compressible Euler equations](../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-compressible-equations).

## Example of usage

To include:

```c++
#include "manta/components-fvm_compressible_fluid_mechanics/fluid_models/single_fluid_model.h"
```

Usage of the template to instantiate a finite volume formulation:

```c++
    using FluidModel = SingleFluidModel<geoDim, 0, IsothermalFluidEOS, HLLCRiemannSolver<geoDim, IsothermalFluidEOS>>;
    auto &fluxForm   = rm.make<EulerExplicitFormulation<FluidModel>>(tube, eos, U, Uvar, W);
```

## Constructor implementation

```c++
  SingleFluidModel(const EOS &eos,
                   const MeshSet &cells,
                   std::shared_ptr<ReconstructionFacetFieldInterface<geoDim, nVar>> facetField)
```

## Parameters

`SingleFluidModel` has the following template parameters:

- `geoDim`

  - Space dimension of the support of the formulation
  - Type: `Int`
  - Default value: None
  - Available options:

    - 1
    - 2
    - 3

- `nScalars`

  - number of passive scalars
  - Type: `Int`
  - Default value: None
  - Available options: \(\ge 0\)

- `EOS`

  - Type of the equation of state
  - Default value: None
  - Available options: any analytical EOS

    - `EOSInterface` (to represent any equation of state, but the given EOS
      should be of a type listed hereafter)
    - `PerfectGasEOS` (see [Perfect gas equation of state](../equations_of_state/perfect_gas.md#perfect-gas-eos))
    - `StiffenedGasEOS` (see [Stiffened gas equation of state](../equations_of_state/stiffened_gas.md#stiffened-gas-eos))
    - `IsothermalFluidEOS` (see [Isothermal fluid equation of state](../equations_of_state/isothermal_fluid.md#isothermal-fluid-eos))
    - `MieGruneisenEOS`

- `RiemannSolver`

  - Type of Riemann solver : How the flux at facets is computed from left and
    right states (see the documentation [here](../../../../theory_manual/fluid_mechanics/compressible_fluid_mechanics.md#euler-riemann-solvers))
  - Default value: None
  - Available options: any Riemann solver type

    - `RiemannSolverInterface` (to represent any Riemann solver, but the
      given solver should be of a type listed hereafter)
    - `HLLCRiemannSolver`
    - `EPXHLLCRiemannSolver`
    - `EPXHLLCLowMachRiemannSolver`
    - `RusanovRiemannSolver`
    - `PerfectGasExactRiemannSolver` (only with `PerfectGasEOS`)
    - `RoeRiemannSolver` (only with `PerfectGasEOS`)

`SingleFluidModel` constructor has the following parameters:

- `eos`: The equation of state, of the same type as the `EOS` template
  parameter ;
- `cells`: The mesh set containing the cells over which the fluid model is
  defined ;
- `facetField`: The facet field encapsulating the primitive variables.
