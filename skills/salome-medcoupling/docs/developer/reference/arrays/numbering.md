<!-- source: reference/arrays/numbering.dox -->

# Array indexing and numbering

The MED library make constant use of arrays of integer or double to represent the various
data it needs. The arrays of integer (DataArrayInt) are of special importance as they
often constitutes the return value of the functions provided by the API. This can be
a list of nodes, a list of cells, a way to rearrange the cell in a mesh (a permutation), a part of the
domain when doing parallel computation, etc ...

This page tries to cover all the form such a data can take and points to the most important
functions available to convert from one format to the other.

Formally a "renumbering" is a mathematical application that can be surjective, injective or bijective.
This application is defined using an instance of
DataArrayInt. There are different ways to define this application.

## Old-to-new mode

The old to new mode is particularly recommended for surjective and bijective applications. This
is typically the case of MEDCouplingUMesh::mergeNodes method.
Let's consider a call to mergeNodes that reduces the
number of nodes from 5 nodes to 3 nodes.  

In old to new mode the array **MySurjection** that specifies this surjection will have 5 tuples
and 1 component. The content of the 5*1 values will be in {0,1,2}.  

If **MySujection** equals [2,1,0,1,2], it means that :

- old id #0 will have new id equal to 2
- old id #1 will have new id equal to 1
- old id #2 will have new id equal to 0
- old id #3 will have new id equal to 1 like old id #1
- old id #4 will have new id equal to 2 like old id #0

This is the most common mode of renumbering in MEDCoupling because there is more methods
implying renumbering that reduce the number of entities than method that increase number of entities.

Method in old to new mode that works on bijective applications :

- DataArrayDouble::renumber
- DataArrayDouble::renumberInPlace

Method in old to new mode that works on surjective applications :

- DataArrayDouble::renumberAndReduce

Sometimes the format old to new for surjections can be replaced by another format with 2 arrays.
Less compact in memory. The DataArrayInt::changeSurjectiveFormat method performs that.

## New-to-old mode

The new-to-old mode is particularly recommended for strictly injective and bijective permutations.
This is particularly useful for methods that increase the number of entities like for example
MEDCouplingUMesh::simplexize.  

All non static methods in DataArrayDouble
or DataArrayInt having as last letter **R** (meaning Reversed) in
capital works with the mode new to old.
Let's consider a call to simplexize that increases
the number of cell from 4 cells to 6 cells.  

In new-to-old mode the array **MyInjection** that specifies this injection will have 6 tuples
and 1 component. The content of the 5*1 values will be in {0,1,2,3}.  

If **MyInjection** equals [2,0,1,1,3,0] it means that :

- new id #0 comes from old id 2
- new id #1 comes from old id 0
- new id #2 comes from old id 1
- new id #3 comes from old id 1
- new id #4 comes from old id 3
- new id #5 comes from old id 0

Method in new-to-old mode that works on bijective applications :

- DataArrayDouble::renumberR
- DataArrayDouble::renumberInPlaceR

Method in new-to-old mode that works on surjective applications :

- DataArrayDouble::selectByTupleId
- DataArrayDouble::selectByTupleIdSafe
- DataArrayDouble::selectByTupleIdSafeSlice
- DataArrayDouble::selectByTupleRanges

## Indirect indexing

The indirect indexing format is made of two [arrays of int (DataArrayInt)](arrays.md) and
is used to describe a set of groups (a group being here understood as a simple pack of int identifiers).
Each group of identifier can for example represent a set of coincident nodes, or a set of nodes belonging
to the same cell, etc ...

*(figure: Indirect indexing principle)*

Denoting `tab` and `tabI` the two arrays of the indirect indexing format,
we see at the top in the picture above the `tab` array, which contains n packs of identifiers
(first pack is 3,1,4,6, second pack is 4,3,2,6,5, etc ...), and below the array `tabI`
which provides the necessary offsets to extract a given pack from `tab.`

This format is widely used internally (this is how the connectivity of
[unstructured cells](reference/meshes/MEDCouplingUMesh.md) is stored for example), and is also returned by
many functions, e.g.:
- MEDCouplingPointSet::findCommonCells
- MEDCouplingPointSet::findCommonNodes
- MEDCouplingPointSet::getNodeIdsNearPoints
- MEDCouplingUMesh::buildDescendingConnectivity
- MEDCouplingUMesh::computeNeighborsOfNodes
- MEDCouplingUMesh::convertNodalConnectivityToDynamicGeoTypeMesh
- MEDCouplingUMesh::setConnectivity
- MEDCouplingUMesh::split2DCells

Some functions in the API to manipulate this format:
- DataArrayInt::changeSurjectiveFormat
- (static) MEDCouplingUMesh::ExtractFromIndexedArrays
- (static) MEDCouplingUMesh::ExtractFromIndexedArraysSlice
