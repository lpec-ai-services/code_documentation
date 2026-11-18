<!-- source: reference/interpolation/intersectors.dox -->

# Intersectors and point locators

The various interpolation methods often require the computation of the intersection between
a cell of the source mesh and a cell of the target mesh, or the localization of a point
inside another mesh. The intersectors implemented in the
library take care of this job.

Before reading on, remember the definition of a [P0 and P1 field](appendix/glossary.md).

- [Specificities of 2D and 3D intersectors](intersec-specifics.md)
- [Geometric2D Intersector](Geometric2D.md)
- [Barycentric coordinates algorithm](barycoords.md) (used in some P1 intersectors/locators)
- [Mapped barycentric coordinates algorithm](mapped_bary.md) (used in some P1P1 intersectors)

Some implementation details of the C++ code can also be found here: [Interpolation kernel - Implementation notes](appendix/interpkernel.md)
