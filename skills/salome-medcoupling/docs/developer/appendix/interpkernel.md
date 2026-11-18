<!-- source: appendix/interpkernel.dox -->

# Interpolation kernel - Implementation notes

## Introduction

The main purpose of this module is to propose a set of algorithms for
mesh interpolation **fully** **independent** **of** **the** **mesh** **data** structure to
support several type of format. This component is parametrized as
much as possible using C++ templates.
For the moment only interpolators for unstructured meshes are present in
the interpolation kernel.

## Main architecture of interpolation kernel.

In the interpolation kernel, algorithms that computes the intersection $T_i\cap S_j$ given the locations and geometries of source cell $S_j$
and target cell $T_i$ are called InterpKerIntersectors.

As can be seen in [the theory of interpolation](reference/interpolation/interptheory.md), all the proposed interpolators aim at
filling the interpolation matrix W (which is generally sparse). For each pair (i,j), $W_{ij}$ is obtained
by calling the desired intersector. The problem is that each call to this algorithm
is CPU-expensive.
To reduce the computational time, a first filtering is done to detect
pairs (i,j) $W_{ij}$ is obviously equal to 0. It is typically the case when a cell in the source mesh
is too far from an another cell in the target mesh each.

So for a given type of interpolation, the computation of W is
performed in two steps :

-# A filtering process reduces the number of pairs of elements for which the calculation
must be carried out by eliminating the pairs whose bounding boxes do not intersect.
-# For all remaining pairs, call the appropriate [cell intersector](reference/interpolation/intersectors.md)

Whatever its dimension and type, each interpolator inherits from INTERP_KERNEL::Interpolation which is a
template (CRTP) class than enable an easy access to the main API without useless CPU cost.

### class MeshType

Each Interpolators and Intersectors are parametrized (templated in
C++ language) with `class` `MeshType` . This type of generalization
has been chosen to reduce at maximum overhead.   

Thanks to this principle intersectors and interpolators are usable
with **several** **mesh** **formats** such as `MED` or `VTK,` **without** **performance** **loss.**
`MeshType` is a concept that should strictly fulfilled the following
rules :

- Const values / Types
  - MyConnType : represents type of connectivity index. This is typically `int` or `long` `int` .
  - MY_SPACEDIM : space dimension. Dimension relative to coordinates.
  - MY_MESHDIM : the dimension of all cells in meshes.
  - My_numPol : policy of numbering. C Format ( $[0,n-1]$ ) or FORTRAN ( $[1,n]$ ).
- Methods
  -# 
```
 void getBoundingBox(double *boundingBox) const 
```

  -# 
```
 INTERP_KERNEL::NormalizedCellType getTypeOfElement(MyConnType eltId) const 
```

  -# 
```
 unsigned char getNumberOfNodesOfElement(MyConnType eltId) const 
```

  -# 
```
 unsigned long getNumberOfNodes() const 
```

  -# 
```
 unsigned long getNumberOfElements() const 
```

  -# 
```
 const MyConnType *getConnectivityPtr() const 
```

  -# 
```
 const double *getCoordinatesPtr() const 
```

  -# 
```
 const MyConnType *getConnectivityIndexPtr() const 
```

  -# 
```
 void releaseTempArrays() 
```

- Formats of arrays
  - the array returned by `getCoordinatesPtr` must be a **full** **interlace** array.
  - the arrays returned by `getConnectivityPtr` and `getConnectivityIndexPtr` must be with the same principle as it is [implemented in MEDCouplingUMesh](reference/meshes/MEDCouplingUMesh.md). Of course the numbering format may change according to *My_numPol* policy.

Note that the array format for connectivity is kept close to MED. It is
close to VTK format too but slightly different. So it may require for the VTK side a copy
on wrap. To avoid this copy of a part of the connectivity structure, an iterator should be used.

### class MatrixType

As already said, the matrix returned by interpolator is typically a sparse matrix. Instances of
`class` `MatrixType` are used to store the resulting interpolation matrix. To be able to be filled by the interpolator the `MatrixType` class has to match the following concept :

- Methods
  -# 
```
 void resize(uint nbrows) 
```

  -# 
```
 Row &operator [] (uint irow) 
```

`class` `Row` has to match at least the following concept :

- Methods
  - 
```
 void insert(const std::pair<int,T>& myPair) 
```

Note that `std::vector\c` < `std::map<int,double>` > is a candidate for `MatrixType.`
