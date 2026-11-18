<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fluid_models/mcsg_fluid_model.html -->

# MCSGFluidModel

A `FluidModel` is a structure that defines the physical and mathematical
behavior of a fluid system within Finite Volume formulations for the Euler equations.
It acts as the bridge connecting the conservation laws, the equation of state
(`EOS`), and the numerical Riemann solver.

In particular, a fluid model is responsible for:

- Converting state variables between conservative and primitive forms
  (via the `cons2Prim` and `prim2Cons` methods) ;
- Evaluating quantities such as the local speed of sound ;
- Computing numerical fluxes across mesh facets by solving local Riemann problems.

The `MCSGFluidModel` structure describes the fluid is multi-component, and
each component is characterized by a `StiffenedGasEOS`. It corresponds to a
5-equation model with isobaric closure. This model is non-conservative.

## Example of usage

To include:

```c++
#include "manta/components-fvm_compressible_fluid_mechanics/fluid_models/mcsg_fluid_model.h"
```

Usage of the template to instantiate a finite volume formulation:

```c++
  using FluidModel = MCSGFluidModel<geoDim, nComp, variant>;
  auto &eulerForm  = rm.make<EulerExplicitFormulation<FluidModel>>(tube, eos, U, Uvar, W);
```

## Constructor implementation

```c++
  MCSGFluidModel(const EOS &eos,
                 const MeshSet &cells,
                 std::shared_ptr<ReconstructionFacetFieldInterface<geoDim, nVar>> facetField)
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

- `nComp`

  - Number of components
  - Default value: \(2\)
  - Available options: \(\ge 2\)
- `MCSGvariant`

  - Variant of the 5-equation multi-component model (Computation of the mixture
    sound speed and source term on the volume fraction equation)
  - Default value: `MCSGvariant::allaire`
  - Available options :

    - `MCSGvariant::allaire` (model from Allaire et al. [[ACK02](../../../../references/references.md#id70)])
    - `MCSGvariant::kapila` (model from Kapila et al. [[KMB+01](../../../../references/references.md#id71)])

`MCSGFluidModel` constructor has the following parameters:

- `eos`: The equation of state, which must be of type `Array<StiffenedGasEOS, nComp>`,
  where `nComp` is the same as the template parameter ;
- `cells`: The mesh set containing the cells over which the fluid model is
  defined ;
- `facetField`: The facet field encapsulating the primitive variables.

## Description

This model corresponds to a 5-equation model with isobaric
closure, i.e. mass conservation of each component, momentum conservation and
energy conservation of the mixture, and transport of the volume fraction.

The number of conservative and primitive variables is `geoDim + 2 + 2 * nComp`.

The Riemann solver used to compute fluxes is enforced and is set to `HLLCRiemannSolver`.

It implies the computation, on each control volume \(V\), of the evolution
of the Conservative state
\(\mathbf{U} = {[{\rho}, {\rho} \mathbf{u}, {\rho} E,
{\rho}_1 {\alpha}_1, ... , {\rho}_k {\alpha}_k, {\alpha}_1, ... , {\alpha}_k]}^T\),
where:

- \({\alpha}_k\) is the volume fraction of component k
- \({\rho}_k\) is the density of component k

### Variants

Two variants are available:

- `MCSGvariant::allaire`, the model from Allaire et al. (from
  [[ACK02](../../../../references/references.md#id70)]). This model is especially relevant for interface
  models. The mixture sound speed \(c\) is the often called "frozen" sound
  speed, where, for k components:

  \[c^2 = \frac{1}{\rho} \sum_{k} {\rho}_k {\beta}_k {c^2}_k\]

  and:

  \[{\beta}_k = \frac{ \frac{ { \alpha}_k }{ {\gamma}_k - 1 } }{ \sum_{k} \frac{ {\alpha}_k }{ {\gamma}_k - 1 }}\]

  where \({\gamma}_k\) is the adiabatic coefficient in Stiffened Gas EOS for component k.
- `MCSGvariant::kapila` the model from Kapila et al. (from
  [[KMB+01](../../../../references/references.md#id71)]). This model is more suited for multi-phase mixtures,
  such as bubbly flows. It may be unstable around interfaces. In this case, the
  mixture sound speed \(c\) for k components follows Wood formula:

  \[\frac{1}{\rho c^2} = \sum_{k} \frac{ {\alpha}_k }{ {\rho}_k {c^2}_k }\]
