<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/beams_and_shells/nodal/nodal_mass_matrix_formulation.html -->

# NodalMassMatrixFormulation

## Introduction

This formulation implements nodal masses. Concentrated masses can be added at
1-node elements.

The [NodalMass brick](../../../../../manta_frontend_user_guide/bricks/solid_mechanics/nodal/nodal_mass_brick.md#brick-nodal-mass) found in MANTA's components
is built on this formulation.

It derives from the `NodalMatrixFormulation` base class documented
[here](nodal_matrix_formulation.md#formulation-nodal-matrix).

## Example of usage

```c++
    auto &nodalMassForm = rm.make<NodalMassMatrixFormulation<hypothesis>>(left, Utranvar, mass);
```

which calls the `NodalMassMatrixFormulation` constructor:

```c++
  /**
     * @brief Constructor
     * @param meshSet Mesh set containing only poi1 elements
     * @param dofVar DofVar for assembling
     * @param mass Mass to be added at each node (must be > 0)
     */
  NodalMassMatrixFormulation(const MeshSet &meshSet, const DofVar &dofVar, Real mass);
```

with:

- `hypothesis` is the **structural hypothesis** template parameter
  (see `StructuralHypothesis`), here `hypothesis`;
- `meshSet` is the **mesh set** over which the formulation is applied
  (here `left`, containing a single poi1 element);
- `dofVar` is the `DofVar` associated with the `NodeField` defined
  over `meshSet` on which the mass acts (here `Utranvar`);
- `mass` is the value of the **mass** added at each node, which
  **must be strictly positive** (here `mass`).

## Equations

> The computed matrix describes the mechanical force, so that:
>
> \[F = {M} \cdot \ddot{U}\]
>
> acting on a single node in all global directions (\(x, y, z\) for three-dimensional hypothesis),
> meaning that the expression is equivalent to:
>
> \[\begin{split}\begin{pmatrix} F_x \\ F_y \\ F_z \end{pmatrix}
> = \begin{bmatrix} m & 0 & 0 \\ 0 & m & 0 \\ 0 & 0 & m \end{bmatrix}
> \begin{pmatrix} \ddot{U}_x \\ \ddot{U}_y \\ \ddot{U}_z \end{pmatrix}\end{split}\]

## List of commented examples and verification tests

- [Euler beam verification tests - The beam_with_lumped_mass cases](../../../../../verification_tests/manta_components_verification_tests/solid_mechanics/fem_eigenmodes/beams/beam_with_lumped_mass.md#beam-lumped-mass-eigenmodes-verification-tests)

## Notes

- Masses cannot be negative.
