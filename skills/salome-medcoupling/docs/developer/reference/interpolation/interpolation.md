<!-- source: reference/interpolation/interpolation.dox -->

# Interpolation

Interpolation (or projection) methods are a key feature of the MEDCoupling library.
It allows to "transfer" the values of a field on a given source mesh to another, newly created field
on a target mesh.

The two meshes/fields need not to have the same [mesh/spatial dimension](reference/meshes/meshes.md), nor do they need to have the same [discretization](reference/fields/discretization.md).

- [Interpolation presentation](intro-interp.md)
- [Detailed explanations for cell-based (P0) fields](interptheory.md)
- [Nature of a field](NatureOfField.md)
- [The remapper class.](remapper.md)
- [Intersectors and point locators](intersectors.md)

If you are looking for a parallel utilisation of the above, take a look at:

- [Parallelism](reference/distrib/parallel.md)

Some implementation details of the C++ code can be found in appendix:

- [Interpolation kernel - Implementation notes](appendix/interpkernel.md)
