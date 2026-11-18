<!-- source: reference/distrib/parallel.dox -->

# Parallelism

## Building blocks

Several classes and methods are available in the MED library to ease the exchange of information
in a parallel context. The DECs ([detailed further down](parallel.md)) then use those classes to enable
the parallel remapping (projection) of a field.
For historical reasons, all those items are in the same namespace as the non-parallel MEDCoupling functionalities,
<b>ParaMEDMEM</b>.

The core elements of the API are:
- CommInterface, this is the wrapper around the MPI library, and an instance
of this object is required in many constructors of the following objects.
- ParaMESH, the parallel instantiation of a [MEDCoupling mesh](reference/meshes/meshes.md)
- ParaFIELD, the parallel instantiation of a [MEDCoupling field](reference/fields/fields.md)
- MPIProcessorGroup (which inherits from the abstract
ProcessorGroup), a group of processors (typically MPI nodes)

In an advanced usage, the topology of the nodes in the computation is accessed through the following elements:
- BlockTopology, specification of a topology based on the (structured) mesh.
The mesh is divided in block (typically a split along the first axis) which are allocated on the various
processors.
- <b> ExplicitTopology </b> (not fully supported yet and only used internally), specification of user-defined
topology, still based on the mesh.
- ComponentTopology, specification of a topology allowing the split of
several field *components* among different processors. The mesh is not the support of the topology anymore.

## Data Exchange Channel - DEC

A Data Exchange Channel (DEC) allows the transfer and/or the interpolation (remapping) of field data between several
processors in a parallel (MPI) context.
Some DECs perform a simple renumbering and copy of the data, and some are capable of functionalities similar to the
[sequential remapper](reference/interpolation/remapper.md).

We list here the main characteristics of the DECs, the list being structured in the same
way as the class hierarchy:

- DisjointDEC, works with two disjoint groups of processors. This is an abstract class.
    - InterpKernelDEC, inherits the properties of the `DisjointDEC.` The projection
    methodology is based on the algorithms of INTERP_KERNEL, that is to say, they work in a similar fashion than
    what the [sequential remapper](reference/interpolation/remapper.md) does. The following [projection methods](reference/fields/discretization.md)
    are supported: P0->P0 (the most common case), P1->P0, P0->P1.
    - StructuredCoincidentDEC, also inherits the properties
    of the `DisjointDEC,` but this one is **not** based on the INTERP_KERNEL algorithms.
    This DEC does a simple data transfer between two fields having a common (coincident) structured support,
    but different topologies (i.e. the structured domain is split differently among the processors for the
    two fields). Only the cell identifiers are handled, and no kind of interpolation (in the sense of the
    computation of a weight matrix) is performed. It is a "mere" reallocation of data from one domain
    partitioning to another.
    - **ExplicitCoincidentDEC** : as above, but based on an explicit topology. This DEC is used internally but
    rarely directly in the public API.
- OverlapDEC, works with a single processor group, but each processor detains
both (part of) the source and target fields. This DEC can really be seen as the true parallelisation of the
[sequential remapper](reference/interpolation/remapper.md). Similarly to the InterpKernelDEC
the projection methodology is based on the algorithms of INTERP_KERNEL, that is to say,
it works in a similar fashion than what the [sequential remapper](reference/interpolation/remapper.md) does.
- **NonCoincidentDEC** (deprecated for now)

Besides, all the DECs inherit from the class DECOptions which provides
the necessary methods to adjust the parameters used in the transfer/remapping.

The most commonly used DEC is the `InterpKernelDEC,` and here is a simple example to of its usage:

 
```
...
InterpKernelDEC dec(groupA, groupB);   // groupA and groupB are two MPIProcessorGroup
dec.attachLocalField(field);           // field is a ParaFIELD, a MEDCouplingField or an ICoCo::MEDField
dec.synchronize();                     // compute the distributed interpolation matrix
if (groupA.containsMyRank())
dec.recvData();                        // effectively transfer the field (receiving side)
else if (groupB.containsMyRank())
dec.sendData();                        // effectively transfer the field (sending side)
...
```
