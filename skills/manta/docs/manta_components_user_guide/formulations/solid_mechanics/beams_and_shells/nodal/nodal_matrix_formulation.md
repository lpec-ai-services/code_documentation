<!-- source: https://manta-project.gitlab.io/manta/manta_components_user_guide/formulations/solid_mechanics/beams_and_shells/nodal/nodal_matrix_formulation.html -->

# NodalMatrixFormulation

## Introduction

The `NodalMatrixFormulation` is a generic class
designed to represent local (or condensed) linear effect applied to a single node.

The following classes derive from this base class:

- the `NodalStiffnessMatrixFormulation` documented [here](nodal_stiffness_matrix_formulation.md#formulation-nodal-stiffness),
- the `NodalDamperMatrixFormulation` documented [here](nodal_damper_matrix_formulation.md#formulation-nodal-damper),
- and the `NodalMassMatrixFormulation` documented [here](nodal_mass_matrix_formulation.md#formulation-nodal-mass).

## Usage

Its constructor is:

```c++
  /**
     * @brief Constructor
     * @param meshSet Mesh set containing only poi1 elements
     * @param dofVar DofVar for assembling
     * @param value Value to be added at each node (mass, stiffness, or damping coefficient)
     */
  NodalMatrixFormulation(const MeshSet &meshSet, const DofVar &dofVar, Real value);
```

## Equations

The computed matrix describes the mechanical force, so that:

Stiffness (K)

\[F = {K} \cdot U\]

Damper (C)

\[F = {C} \cdot \dot{U}\]

Mass (M)

\[F = {M} \cdot \ddot{U}\]

acting on a single node in all global directions (\(x, y, z\) for three-dimensional hypothesis),
meaning that the expression is equivalent to:

Stiffness (K)

\[\begin{split}\begin{pmatrix} F_x \\ F_y \\ F_z \end{pmatrix}
= \begin{bmatrix} k & 0 & 0 \\ 0 & k & 0 \\ 0 & 0 & k \end{bmatrix}
\begin{pmatrix} U_x \\ U_y \\ U_z \end{pmatrix}\end{split}\]

Damper (C)

\[\begin{split}\begin{pmatrix} F_x \\ F_y \\ F_z \end{pmatrix}
= \begin{bmatrix} c & 0 & 0 \\ 0 & c & 0 \\ 0 & 0 & c \end{bmatrix}
\begin{pmatrix} \dot{U}_x \\ \dot{U}_y \\ \dot{U}_z \end{pmatrix}\end{split}\]

Mass (M)

\[\begin{split}\begin{pmatrix} F_x \\ F_y \\ F_z \end{pmatrix}
= \begin{bmatrix} m & 0 & 0 \\ 0 & m & 0 \\ 0 & 0 & m \end{bmatrix}
\begin{pmatrix} \ddot{U}_x \\ \ddot{U}_y \\ \ddot{U}_z \end{pmatrix}\end{split}\]

Todo

Other options will be soon available to take into account anisotropy.
