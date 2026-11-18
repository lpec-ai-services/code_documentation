<!-- source: start/intro-start.dox -->

# What can I do with MED?

Simulation studies require the manipulation of [meshes](reference/meshes/meshes.md) and [fields](reference/fields/fields.md) for data
pre-processing, in calculation schemes (including chaining and coupling
of codes), or even for results post-processing.

Corresponding computer codes can be viewed as software components accessing
input [meshes](reference/meshes/meshes.md) and [fields](reference/fields/fields.md) (with specific constraints) along with parameters
(datasets), and producing output [meshes](reference/meshes/meshes.md) and [fields](reference/fields/fields.md). Each code presents by
construction the specificities of its discipline.

The [MED module](library.md) aims at pooling operations on those items, facilitating
their use by various codes involved in a simulation process. This includes
making codes communicate while preserving as much as possible the integrity of
their content.

To fulfill its objective, the [MED module](library.md) includes:
- Handling [meshes](reference/meshes/meshes.md) and [fields](reference/fields/fields.md) to satisfy code input requirements.
- Extraction of field information to post-process computation results of
a code.
- [Projections](reference/interpolation/interpolation.md) and serialization to [exchange meshes and fields](reference/distrib/parallel.md) between codes.

In addition, the [MED module](library.md) offers several interfacing levels; users can thus
benefit from an interaction level adapted to their codes.

The main services offered by [MEDCoupling](library.md) are:
- Manipulation of [fields](reference/fields/fields.md) and their support [mesh](reference/meshes/meshes.md), serialized with the
[MED format](reference/medloader/medloader1.md).
- Operations on scalars, vectors, and second order tensors.
- 1D/2D/3D [interpolation](reference/interpolation/interpolation.md) on nodes, cells, Gauss points and nodes by element.

MEDCoupling thus considers:
- the [data dimension](reference/meshes/meshes.md).
- the [physical nature](reference/interpolation/NatureOfField.md) of the information stored in a field, as well as conservation laws.
- the field profiles and the mesh connectivity.

*(figure: projectionHQ_600.png)*
