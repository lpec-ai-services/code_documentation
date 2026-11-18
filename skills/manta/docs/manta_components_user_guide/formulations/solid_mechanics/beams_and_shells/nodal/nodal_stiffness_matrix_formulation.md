<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/beams_and_shells/nodal/nodal_stiffness_matrix_formulation.html -->

# NodalStiffnessMatrixFormulation

## Introduction

This formulation implements nodal stiffness. Concentrated springs can be added at
1-node elements.

Currently, there is no corresponding brick in the frontend.

It derives from the `NodalMatrixFormulation` base class documented
[here](nodal_matrix_formulation.md#formulation-nodal-matrix).

## Example of usage

```c++
    auto &springRotLeft   = rm.make<NodalStiffnessMatrixFormulation<hypothesis>>(left, Urotvar, kappa_theta);
    auto &springTranRight = rm.make<NodalStiffnessMatrixFormulation<hypothesis>>(right, Utranvar, kappa_u);
```

which calls the `NodalStiffnessMatrixFormulation` constructor:

```c++
  /**
     * @brief Constructor
     * @param meshSet Mesh set containing only poi1 elements
     * @param dofVar DofVar for assembling
     * @param stiffness Stiffness coefficient to be added at each node
     */
  NodalStiffnessMatrixFormulation(const MeshSet &meshSet, const DofVar &dofVar, Real stiffness);
```

with:

- `hypothesis` is the **structural hypothesis** template parameter
  (see `StructuralHypothesis`), here `hypothesis`;
- `meshSet` is the **mesh set** over which the formulation is applied
  (here `left` and `right`, each containing a single poi1 element);
- `dofVar` is the `DofVar` associated with the `NodeField` defined
  over `meshSet` on which the stiffness acts (here `Urotvar`
  for the rotational spring, `Utranvar` for the translational one);
- `stiffness` is the stiffness coefficient added at each node
  (here `kappa_theta` and `kappa_u`).

## Equations

> The computed matrix describes the mechanical force, so that:
>
> \[F = {K} \cdot U\]
>
> acting on a single node in all global directions (\(x, y, z\) for three-dimensional hypothesis),
> meaning that the expression is equivalent to:
>
> \[\begin{split}\begin{pmatrix} F_x \\ F_y \\ F_z \end{pmatrix}
> = \begin{bmatrix} k & 0 & 0 \\ 0 & k & 0 \\ 0 & 0 & k \end{bmatrix}
> \begin{pmatrix} U_x \\ U_y \\ U_z \end{pmatrix}\end{split}\]

## List of commented examples and verification tests

- [Nodal and springs verification tests - The beam_with_nodal_springs case](../../../../../verification_tests/manta_components_verification_tests/solid_mechanics/fem_eigenmodes/nodal_and_springs/beam_with_nodal_springs.md#beam-with-nodal-springs-verification-test)
