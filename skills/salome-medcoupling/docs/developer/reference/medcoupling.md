<!-- source: reference/medcoupling.dox -->

# Core data structures (MEDCoupling)

<h1>Overview</h1>

The MEDCoupling library gather the core structures used everywhere in the MED world.

- [Arrays of data](arrays/arrays.md)
- [Array indexing and numbering](arrays/numbering.md)
- [Meshes](meshes/meshes.md)
- [Fields](fields/fields.md)

<h1>Design philosophy</h1>

The structures described above (arrays, meshes and fields), with the algorithms associated to it
form the core of the MEDCoupling library (**libmedcoupling.so** or **medcoupling.dll).**
It is fully written in C++ and wrapped in Python.

The MEDCoupling C++ library implements a data structure which is the result of the following tradeoff:
- compliant with [code coupling](appendix/glossary.md):
  - fields data structure containing enough information to perform a well defined interpolation
  - data structure exchangeable through processes, as well in [parallel](distrib/parallel.md) (SPMD paradigm -
  [sometimes called ParaMEDMEM](start/library.md)), as in a [distributed paradigm](distrib/corba-distrib.md) (using CORBA).
- minimize as much as possible the number of external software prerequisites needed to use it (the core of the
library, MEDCoupling, can be built as a standalone tool).
- light and agile enough to:
   - maximize the amount of possible algorithms being applied on it
   - ease the implementation of other projects using MEDCoupling as a prerequisite.
- large enough to be used for MED file I/O (thanks to the [MEDLoader](medloader/medloader1.md) part).
- compliant with VTK visualization data structures
- integrate HPC constraints (compact structures, limitation of copies and launching of CPU consuming algorithms only when absolutely needed ).
- compliant with the [ICoCo API](misc/icoco.md)

The MEDCoupling also implements a set of algorithms linked to this data structure. The
[functionalities](start/functionalities.md) section gives an insight of the avalaible algorithm.
