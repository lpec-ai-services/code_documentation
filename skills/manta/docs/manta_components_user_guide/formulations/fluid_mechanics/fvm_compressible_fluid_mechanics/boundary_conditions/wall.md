<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/fluid_mechanics/fvm_compressible_fluid_mechanics/boundary_conditions/wall.html -->

# `Wall` boundary condition

The `Wall` boundary condition characterizes a rigid wall. Waves are
reflected along the normal direction of the facet. Scalar variables in the
outside state are copied from the inside state, whereas the velocity is
(\(\mathbf{n}\) is the facet normal):

\[\mathbf{u}_{out} = \mathbf{u}_{in} - 2 ( \mathbf{u}_{in} \cdot \mathbf{n} ) \mathbf{n}\]

With \(\mathbf{u}_{in}\) the velocity in the inside cell and
\(\mathbf{u}_{out}\) the one in the outside ghost cell.

## Example of usage

Include:

```c++
#include "manta/components-fvm_compressible_fluid_mechanics/euler_boundary_conditions.h"
```

The boundary condition is added to the Euler formulation through the
`addBc` method. It takes the Boundary condition type as template parameter
and takes as arguments the BC parameters.

```c++
    fluxForm.addBc<WallBoundaryCondition<geoDim, nVar>>(ctx, l_bot);
```

## Input parameters

The only parameter taken by the `WallBoundaryCondition` is the
*meshSet* which is the support of the boundary condition.
