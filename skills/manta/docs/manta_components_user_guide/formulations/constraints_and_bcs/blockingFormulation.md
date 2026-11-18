<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/constraints_and_bcs/blockingFormulation.html -->

# BlockingFormulation

## Introduction

This formulation aims at blocking some degrees of freedom of your problem at 0.

## Example of usage

Usage of this formulation requires the following include:

```c++
#include "manta/components-fem_tools/constraints/blocking_formulation.h"
```

Here is the constructor of the formulation:

```c++
    auto &bcFormulationTop = rm.make<BlockingFormulation<true>>(resultVar, top);
```

## Parameters

`BlockingFormulation` has the following template parameter:

- `true`, boolean, if true eliminate the constraint to reduce the size of the system.

`BlockingFormulation` has the following parameters:

- `resultVar`, the dof variable linked to the primal field which is blocked,
- `top`, the `MeshSet` which is constrained,
- `components`, a `Vector` of `Int` designating the components of the primal to constrain (*optional*).

## How to use

A `BlockingFormulation` requires the construction of a
`ConstraintSet` which acts as the contribution of
the constraint to the `LinearSystem`

In the previous example those steps were nescessary:

```c++
    auto &bcSystem = rm.make<ConstraintSet>(scalarLaplacianSystem, "bcSystem");
    rm.assignFormulationToLinearSystem(bcFormulationTop, bcSystem);
```

where the `ScalarLaplacianSystem` is the main `LinearSystem` that is built.

## List of commented examples and verification tests

- Example : in examples/scalar_laplacian, 2D result on a grid mesh
