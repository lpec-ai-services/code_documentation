<!-- source: reference/fields/MEDCouplingFields.dox -->

# Fields

[TOC]

## Field concept

A field in MEDCoupling point of view, is a structure that allows to
store a discretization of a physical value on a defined discretized spatial and
possibly temporal support.

The spatial support is a [mesh](reference/meshes/meshes.md).
A field is lying on an entity that will be specified by the spatial
discretization of the field. For example a field on node will lie on
all nodes of its mesh.

A field on cell will lie on all cells of its mesh.

Fields in MEDCoupling follow the two following rules :

- A field will lie on **ALL** entities of its spatial support ([mesh](reference/meshes/meshes.md)).
- A field has **only** **one** spatial support ([mesh](reference/meshes/meshes.md)) on its temporal support.

The main properties of a field are :

- name
- spatial support which is a [mesh](reference/meshes/meshes.md)
- a [spatial discretization](MEDCouplingFields.md)
- a description of intrinsic nature of the values of field (see [Nature of a field](reference/interpolation/NatureOfField.md)). This is important for conservative interpolation (see [Summary](reference/interpolation/interptheory.md)).
- a temporal discretization that specifies, if it exists, the time interval on which the field is covering, and how.
- number of components

This definition of field in MEDCoupling allows an instance of field to
know at any point inside its spatial-temporal support the value.

The class that incarnates the concept described above is : MEDCoupling::MEDCouplingFieldDouble.

Some of most important implemented methods are :

- getNumberOfComponents
- getValueOn
- applyFunc
- cross instances operations

## Spatial discretization concept

This is the concept that makes the link, independently from temporal
discretization, between the field and its spatial support ([mesh](reference/meshes/meshes.md)). This
concept allows the field to make a check and interpretation of an
array of values given a spatial support ([mesh](reference/meshes/meshes.md)).

The abstract class that incarnates the concept is : MEDCoupling::MEDCouplingFieldDiscretization.

The most important pure virtual methods are :

- getnumberOfTuples
- getValueOn
- getMeasureField

## Temporal discretization concept

This information allows, independently from spatial discretization, to
associate a time interval, if it exists, on which the field will be
defined. This concept is able to give the value at any time of
the definition interval (if any).

The abstract class MEDCoupling::MEDCouplingTimeDiscretization
incarnates this described concept.

This classes and its subclasses are responsible in storing the arrays
of the aggregating field.

The most important methods are :

- setTime and getTime
- getArray and setArray
- getArraysForTime
- getValueForTime

## Building a field from scratch

Here we will make the assumption that an instance of `MEDCouplingMesh` called `mesh` has been created ( to know more about mesh creation [click here](reference/meshes/MEDCouplingUMesh.md) ).

### Create a tensor field with 9 components on cells with no time step

Here the C++ implementation.

Here the Python implementation.

### Create a scalar field on nodes with no time step

Here the C++ implementation.

Here the Python implementation.

### Create a 2 components-vector field on cells with one time step and no interval

Here the C++ implementation.

Here the Python implementation.

### Create a 3 components-vector field on nodes with a time interval where field remains constant on this time interval

Here the C++ implementation.

Here the Python implementation.

## Operations on Fields

Here we will make the assumption that an instance of MEDCouplingMesh
called `mesh` has been created with spaceDim==2.

Here a C++ example of more advanced use of MEDCouplingFieldDouble instances.

Here a Python example of more advanced use of MEDCouplingFieldDouble instances.

 LocalWords:  discretization
