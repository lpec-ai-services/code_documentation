<!-- source: reference/interpolation/intro-interp.dox -->

# Interpolation presentation

## Overview

The InterpKernel algorithms are part of the MED tool suite. They
answer to the following basic problem : given a source mesh $M_s$, a
source field $F_s$ and a target mesh $M_t$, reconstruct a field $F_t$
that uses $M_t$ as a support. The InterpKernel suite gives a number of
possibilities to compute the target field, depending on a variety of
user constraints.

*(figure: General interpolation scheme)* width=10cm

Two different APIs are available depending on whether you run sequentially or in parallel:
- the [remapper class](remapper.md) (based on the underlying [InterpKernel](appendix/interpkernel.md) library)
for sequential codes, which uses MEDCoupling [fields](reference/fields/fields.md) and other core data structures.
- the [ParaMEDMEM API](reference/distrib/parallel.md) for parallel MPI based codes using `ParaMEDMEM` distributed fields
(ParaFIELD), which is also based on the algorithms of the
[InterpKernel](appendix/interpkernel.md) library.

The following space/mesh dimensions are covered:
- 1D, 2D lines, 2D surfaces ([Special features of 2D intersectors](intersec-specifics.md)),
- 3D surfaces ([Special features of 3D surface intersectors](intersec-specifics.md))
- and 3D volumes ([Special features of 3D volumes intersectors](intersec-specifics.md))

The interpolation is performed either by:
- node localization ([PointLocator](intersec-specifics.md)), when for example a node field is projected to a cell field
- or via cell intersection ([Conservative interpolation](interptheory.md)), when for example a cell field is projected to another cell field.
For any given type of interpolation involving cell intersection computation, the computation of
interpolation matrix W is performed in two steps :
    -# A filtering process reduces the number of pairs of elements for which the calculation
must be carried out by eliminating the pairs whose bounding boxes do not intersect.
    -# For all remaining pairs, call the appropriate [cell intersector](intersectors.md)

More complex treatments are also available:
- treatment of extended polygons (where edges can be arcs or segments)
for 2D intersection computations, via the [Geometric2D intersector](Geometric2D.md),

Finally the following types of [spatial discretization](reference/fields/discretization.md) combinations are supported:
- management of fields with P0,P1 or P2 representations
- P0<->P0, P1<->P0, P1<->P1 and P2->P0 (non conservative) interpolators are available.

Remember that whatever the situation you face, you must always specify whether the field
represents an extensive or intensive physical quantity through
the [nature](NatureOfField.md) attribute of the [field](reference/fields/fields.md).

## Key elements of the API

TODO, list setOption, setIntersectionType, etc ...
