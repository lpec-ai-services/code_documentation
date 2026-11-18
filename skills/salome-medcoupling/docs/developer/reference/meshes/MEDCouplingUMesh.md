<!-- source: reference/meshes/MEDCouplingUMesh.dox -->

# Unstructured mesh

An unstructured mesh in [Core data structures (MEDCoupling)](reference/medcoupling.md) MEDCoupling is defined by :

  - a point cloud where the explicit coordinates of each point must be specified (inherited from [MEDCouplingPointSet class](MEDCouplingPointSet.md)).
  - nodal connectivity that specifies for each cell, the points in the previous point cloud that constitutes the cell.

As unstructured mesh is dynamically defined enough, this class is also used by MEDCoupling to instantiate degenerated meshes as :

- point cloud only meshes. This type of mesh will have mesh dimension 0.
- abstract meshes containing only one cell that covers a potentially
  infinite space. This abstract mesh is used as support of fields
  containing only one integrated value. This is typically used to
  represent fields used by system code. This type of mesh will have
  mesh dimension equal to -1.

The norm used for cells connectivity of different types, is the same as specified in MED file except
that connectivities are represented in **C** **format** and **not** **in** **FORTRAN** **format** !

The class that incarnates the described concept is : MEDCoupling::MEDCouplingUMesh.
  
 This class inherits from MEDCoupling::MEDCouplingPointSet abstract class.
  
 So [MEDCouplingUMesh](MEDCouplingUMesh.md) inherits from all [point set features](MEDCouplingPointSet.md).

## Standard building of an unstructured mesh  from scratch

The described method here is called standard, because no special knowledge of underneath nodal connectivity is needed here.
This method of building unstructured mesh is easiest but not the most CPU/memory efficient one.

All of examples given here make the assumption that the ParaMEDMEM namespace is visible ( by calling for example `using` `namespace` `ParaMEDMEM;` ).

Here we will create a mesh with spacedim==3 and meshdim==2. **mesh** contains 5 cells (with geometric type INTERP_KERNEL::NORM_TRI3, INTERP_KERNEL::NORM_QUAD4)
and 9 nodes.

You can notice that it is possible to mix cell types as long as the dimension of the cell is exactly
equal to meshDim to respect [this rule](meshes.md).

Here is the C++ implementation.

Here is the Python implementation.

## How MEDCouplingUMesh stores its nodal connectivity

MEDCouplingUMesh class stores its nodal connectivity into 2 arrays.

- The first one, the biggest is MEDCoupling::MEDCouplingUMesh::_nodal_connectivity.
- The second one, the less big is MEDCoupling::MEDCouplingUMesh::_nodal_connectivity_index.

*(figure: Nodal connectivity storage into MEDCouplingUMesh class)*

> **Note:** The last value of the nodal connectivity index points to an invalid memory place. It is not an error, simply as for standard C++, all ranges
are given in format [**begin,\b** end) where **begin** is included and **end** excluded.

## Advanced building of an unstructured mesh  from scratch

Here we are going to build the mesh in a more advanced manner. This method expects that the user knows the storage format underlying MEDCoupling::MEDCouplingUMesh.

The same mesh than [in the standard section above](MEDCouplingUMesh.md) is going to be implemented using advanced method.

Here the C++ implementation.

Here the Python implementation.
