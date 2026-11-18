<!-- source: start/terminology.dox -->

# Terminology - Meshes, fields, interpolation

## Meshes and fields

This section covers at a very high level the concepts used overall in the MED world.
More precise definitions can be found in the [Glossary, concepts and definitions](appendix/glossary.md), or in the dedicated pages for the
[meshes](reference/meshes/meshes.md) and the [fields](reference/fields/fields.md).

Many physical simulation codes (try to) solve a given set of equations on a given geometrical domain.
This domain can be anything from the representation of a building to the description of the
molecular network found in a small piece of concrete.

The geometrical domain is provided to the machine as a CAO modelisation (what you can build with the
GEOM module of SALOME for example).

*(figure: Example geometry (CAO) of a cylinder)*

The numerical codes (e.g. FEM-based codes)
are usually unable to work directly with such a format, and a spatial discretization of the domain has
to be performed: the **meshing**. A **mesh** can hence roughly be seen as a discrete version of a continuous input geometry.
The module SMESH in SALOME is typically dedicated to performing this task.

*(figure: Example meshing of the above geometry)*

A mesh is made of **cells** (the elementary spatial unit), which are typically simple polygons or polyhedrons.

On this support, the code can read/store values in form of a **field**. A **field** is hence an
array of data, where each cell (or node, or ... etc) has
one (or more) values associated to it. A code simulating the heat equation will for example produce a temperature
field assigning a single temperature value to each cell of the mesh.

Taking the vocabulary of the finite-element world, a field with values stored at the cell level is often
called a **P0 field**, and a field where values are stored at node level a **P1 field**.

More on this subject:
- [Meshes](reference/meshes/meshes.md)
- [Fields](reference/fields/fields.md)

## Interpolation

When working with different codes, or when coupling codes, it is often the case that the initial problem
has been modelised in two different ways. For example a thermic code might use a mesh made of tetrahedron
and a CFD code might use a mesh made of hexaedrons. The <b>interpolation mechanisms</b> provided in the MED library
allow the user to easily **transfer** field data from one representation to the other.

In all its generality it is a complex task, covering many different use cases (do the two meshes overlap? do
we want to conserve the total amount represented by the field?, etc...), justifying a dedicated section in
the documentation: [Interpolation](reference/interpolation/interpolation.md)

In this documentation you will sometime read the words "projection", or "transfer" or "interpolation" for this
process.

More on this subject:
- [Interpolation](reference/interpolation/interpolation.md)
