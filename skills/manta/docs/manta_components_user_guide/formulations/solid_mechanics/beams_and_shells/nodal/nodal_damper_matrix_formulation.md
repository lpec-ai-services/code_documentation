<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/beams_and_shells/nodal/nodal_damper_matrix_formulation.html -->

# NodalDamperMatrixFormulation

## Introduction

This formulation implements nodal damper. Concentrated dashpot can be added at
1-node elements.

Currently, there is no corresponding brick in the frontend.

It derives from the `NodalMatrixFormulation` base class documented
[here](nodal_matrix_formulation.md#formulation-nodal-matrix).

## Example of usage

The `NodalDamperMatrixFormulation` constructor is:

```c++
  /**
     * @brief Constructor
     * @param meshSet Mesh set containing only poi1 elements
     * @param dofVar DofVar for assembling
     * @param damping Damping coefficient to be added at each node
     */
  NodalDamperMatrixFormulation(const MeshSet &meshSet, const DofVar &dofVar, Real damping);
```

## Equations

> The computed matrix describes the mechanical force, so that:
>
> \[F = {C} \cdot \dot{U}\]
>
> acting on a single node in all global directions (\(x, y, z\) for three-dimensional hypothesis),
> meaning that the expression is equivalent to:
>
> \[\begin{split}\begin{pmatrix} F_x \\ F_y \\ F_z \end{pmatrix}
> = \begin{bmatrix} c & 0 & 0 \\ 0 & c & 0 \\ 0 & 0 & c \end{bmatrix}
> \begin{pmatrix} \dot{U}_x \\ \dot{U}_y \\ \dot{U}_z \end{pmatrix}\end{split}\]

### Constructors implementation

### Note

Currently not used in the code.
