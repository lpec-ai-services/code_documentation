<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__I3DPrimOperations.html -->

# GEOM_I3DPrimOperations Interface Reference

Interface for 3D primitives creation.
[More...](interfaceGEOM_1_1GEOM__I3DPrimOperations.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for 3D primitives creation.

Box, Cylinder, Cone, Sphere, Prism (extrusion), Pipe (extrusion along contour), Revolution, Solid (from shell).

## Member Function Documentation

### MakeBoxDXDYDZ()

```python
GEOM_Object MakeBoxDXDYDZ(in double theDX, in double theDY, in double theDZ)
```

Create a box with specified dimensions along the coordinate axes and with edges, parallel to the coordinate axes.

Center of the box will be at point (DX/2, DY/2, DZ/2).

Parameters
:   |  |  |
    | --- | --- |
    | theDX | Length of Box edges, parallel to OX axis. |
    | theDY | Length of Box edges, parallel to OY axis. |
    | theDZ | Length of Box edges, parallel to OZ axis. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created box.

### MakeBoxTwoPnt()

```python
GEOM_Object MakeBoxTwoPnt(in GEOM_Object thePnt1, in GEOM_Object thePnt2)
```

Create a box with two specified opposite vertices, and with edges, parallel to the coordinate axes.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1 | First of two opposite vertices. |
    | thePnt2 | Second of two opposite vertices. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created box.

### MakeFaceHW()

```python
GEOM_Object MakeFaceHW(in double theH, in double theW, in short theOrientation)
```

Create a face specified dimensions along OX-OY coordinate axes, with edges parallel to the coordinate axes.

Center of the face will be at point (0, 0, 0).

Parameters
:   |  |  |
    | --- | --- |
    | theH | Height of the Face. |
    | theW | Width of the Face. |
    | theOrientation | Orientation belong axis OXY OYZ OZX |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

### MakeFaceObjHW()

```python
GEOM_Object MakeFaceObjHW(in GEOM_Object theObj, in double theH, in double theW)
```

Create a face by normale vector or edge and two specified sizes, vertical (H) and horisontal (W).

Parameters
:   |  |  |
    | --- | --- |
    | theObj | defines plane. |
    | theH | vertical size (height). |
    | theW | horisontal size (width). |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

### MakeDiskPntVecR()

```python
GEOM_Object MakeDiskPntVecR(in GEOM_Object thePnt, in GEOM_Object theVec, in double theR)
```

Create a Disk (circular face) with given center, normal vector and radius.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | disk center. |
    | theVec | Vector, normal to the plane of the disk. |
    | theR | Disk radius. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created disk.

### MakeDiskThreePnt()

```python
GEOM_Object MakeDiskThreePnt(in GEOM_Object thePnt1, in GEOM_Object thePnt2, in GEOM_Object thePnt3)
```

Create a disk (circular face), passing through three given points.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1,thePnt2,thePnt3 | Points, defining the disk. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created disk.

### MakeDiskR()

```python
GEOM_Object MakeDiskR(in double theR, in short theOrientation)
```

Create a disk specified dimensions along OX-OY coordinate axes.

Center of the disk at point (0, 0, 0).

Parameters
:   |  |  |
    | --- | --- |
    | theR | of the Disk. |
    | theOrientation | Orientation belong axis OXY OYZ OZX |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created disk.

### MakeCylinderRH()

```python
GEOM_Object MakeCylinderRH(in double theR, in double theH)
```

Create a cylinder with given radius and height at the origin of coordinate system.

Axis of the cylinder will be collinear to the OZ axis of the coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | theR | Cylinder radius. |
    | theH | Cylinder height. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created cylinder.

### MakeCylinderRHA()

```python
GEOM_Object MakeCylinderRHA(in double theR, in double theH, in double theA)
```

Create a portion of cylinder with given radius, height and angle at the origin of coordinate system.

Axis of the cylinder will be collinear to the OZ axis of the coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | theR | Cylinder radius. |
    | theH | Cylinder height. |
    | theA | Cylinder angle. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created cylinder.

### MakeCylinderPntVecRH()

```python
GEOM_Object MakeCylinderPntVecRH(in GEOM_Object thePnt, in GEOM_Object theAxis, in double theR, in double theH)
```

Create a cylinder with given base point, axis, radius and height.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Central point of cylinder base. |
    | theAxis | Cylinder axis. |
    | theR | Cylinder radius. |
    | theH | Cylinder height. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created cylinder.

### MakeCylinderPntVecRHA()

```python
GEOM_Object MakeCylinderPntVecRHA(in GEOM_Object thePnt, in GEOM_Object theAxis, in double theR, in double theH, in double theA)
```

Create a portion of cylinder with given base point, axis, radius, height and angle.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Central point of cylinder base. |
    | theAxis | Cylinder axis. |
    | theR | Cylinder radius. |
    | theH | Cylinder height. |
    | theA | Cylinder angle. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created cylinder.

### MakeConeR1R2H()

```python
GEOM_Object MakeConeR1R2H(in double theR1, in double theR2, in double theH)
```

Create a cone with given height and radiuses at the origin of coordinate system.

Axis of the cone will be collinear to the OZ axis of the coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | theR1 | Radius of the first cone base. |
    | theR2 | Radius of the second cone base. |

Note
:   If both radiuses are non-zero, the cone will be truncated.
:   If the radiuses are equal, a cylinder will be created instead.

Parameters
:   |  |  |
    | --- | --- |
    | theH | Cone height. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created cone.

### MakeConePntVecR1R2H()

```python
GEOM_Object MakeConePntVecR1R2H(in GEOM_Object thePnt, in GEOM_Object theAxis, in double theR1, in double theR2, in double theH)
```

Create a cone with given base point, axis, height and radiuses.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Central point of the first cone base. |
    | theAxis | Cone axis. |
    | theR1 | Radius of the first cone base. |
    | theR2 | Radius of the second cone base. |

Note
:   If both radiuses are non-zero, the cone will be truncated.
:   If the radiuses are equal, a cylinder will be created instead.

Parameters
:   |  |  |
    | --- | --- |
    | theH | Cone height. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created cone.

### MakeTorusRR()

```python
GEOM_Object MakeTorusRR(in double theRMajor, in double theRMinor)
```

Create a torus with given radiuses at the origin of coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | theRMajor | Torus major radius. |
    | theRMinor | Torus minor radius. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created torus.

### MakeTorusPntVecRR()

```python
GEOM_Object MakeTorusPntVecRR(in GEOM_Object thePnt, in GEOM_Object theVec, in double theRMajor, in double theRMinor)
```

Create a torus with given center, normal vector and radiuses.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Torus central point. |
    | theVec | Torus axis of symmetry. |
    | theRMajor | Torus major radius. |
    | theRMinor | Torus minor radius. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created torus.

### MakeSphereR()

```python
GEOM_Object MakeSphereR(in double theR)
```

Create a sphere with given radius at the origin of coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | theR | Sphere radius. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created sphere.

### MakeSpherePntR()

```python
GEOM_Object MakeSpherePntR(in GEOM_Object thePnt, in double theR)
```

Create a sphere with given center and radius.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Sphere center. |
    | theR | Sphere radius. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created .

### MakePrismVecH()

```python
GEOM_Object MakePrismVecH(in GEOM_Object theBase, in GEOM_Object theVec, in double theH)
```

Create a shape by extrusion of the base shape along the vector.

All the space, transfixed by the base shape during its translation along the vector on the given distance.

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be extruded. |
    | theVec | Direction of extrusion. |
    | theH | Prism dimension along theVec. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created prism.

### MakePrismVecH2Ways()

```python
GEOM_Object MakePrismVecH2Ways(in GEOM_Object theBase, in GEOM_Object theVec, in double theH)
```

### MakePrismVecHWithScaling()

```python
GEOM_Object MakePrismVecHWithScaling(in GEOM_Object theBase, in GEOM_Object theVec, in double theH, in double theScaleFactor)
```

### MakePrismTwoPnt()

```python
GEOM_Object MakePrismTwoPnt(in GEOM_Object theBase, in GEOM_Object thePoint1, in GEOM_Object thePoint2)
```

Create a shape by extrusion of the base shape along a vector, defined by two points.

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be extruded. |
    | thePoint1 | First end of extrusion vector. |
    | thePoint2 | Second end of extrusion vector. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created prism.

### MakePrismTwoPnt2Ways()

```python
GEOM_Object MakePrismTwoPnt2Ways(in GEOM_Object theBase, in GEOM_Object thePoint1, in GEOM_Object thePoint2)
```

### MakePrismTwoPntWithScaling()

```python
GEOM_Object MakePrismTwoPntWithScaling(in GEOM_Object theBase, in GEOM_Object thePoint1, in GEOM_Object thePoint2, in double theScaleFactor)
```

### MakePrismDXDYDZ()

```python
GEOM_Object MakePrismDXDYDZ(in GEOM_Object theBase, in double theDX, in double theDY, in double theDZ)
```

Create a shape by extrusion of the base shape along a vector, defined by DX DY DZ.

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be extruded. |
    | theDX,theDY,theDZ | end of extrusion vector. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created prism.

### MakePrismDXDYDZ2Ways()

```python
GEOM_Object MakePrismDXDYDZ2Ways(in GEOM_Object theBase, in double theDX, in double theDY, in double theDZ)
```

### MakePrismDXDYDZWithScaling()

```python
GEOM_Object MakePrismDXDYDZWithScaling(in GEOM_Object theBase, in double theDX, in double theDY, in double theDZ, in double theScaleFactor)
```

### MakeDraftPrism()

```python
GEOM_Object MakeDraftPrism(in GEOM_Object theInitShape, in GEOM_Object theBase, in double theHeight, in double theAngle, in boolean theFuse, in boolean theInvert)
```

Add / Remove material to / from a solid by extrusion of the base shape on the given distance.

Parameters
:   |  |  |
    | --- | --- |
    | theInitShape | Initial shape on which to perform the feature.It has to be a solid or a compound made of a single solid |
    | theBase | Edge or wire defining the base shape to be extruded. |
    | theHeight | Prism dimension along the normal of the face. |
    | theAngle | Draft angel in degrees |
    | theFuse | If true material is added else material is removed |
    | theInvert | If true material changes the direction |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the modified shape

### MakePipe()

```python
ListOfGO MakePipe(in GEOM_Object theBase, in GEOM_Object thePath, in boolean IsGenerateGroups)
```

Create a shape by extrusion of the base shape along the path shape. The path shape can be a wire or an edge.

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be extruded. |
    | thePath | Path shape to extrude the base shape along it. |
    | IsGenerateGroups | flag that tells if it is necessary to return groups (true) or not (false). |

Returns
:   The list of objects. The first one is a result pipe, the other ones are the created groups. If *IsGenerateGroups* is not set the returned list contains a single object, which is the operation result.

### MakeRevolutionAxisAngle()

```python
GEOM_Object MakeRevolutionAxisAngle(in GEOM_Object theBase, in GEOM_Object theAxis, in double theAngle)
```

Create a shape by revolution of the base shape around the axis on the given angle.

All the space, transfixed by the base shape during its rotation around the axis on the given angle.

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be rotated. |
    | theAxis | Rotation axis. |
    | theAngle | Rotation angle in radians. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created revolution.

### MakeRevolutionAxisAngle2Ways()

```python
GEOM_Object MakeRevolutionAxisAngle2Ways(in GEOM_Object theBase, in GEOM_Object theAxis, in double theAngle)
```

### MakeFilling()

```python
GEOM_Object MakeFilling(in ListOfGO theContours, in long theMinDeg, in long theMaxDeg, in double theTol2D, in double theTol3D, in long theNbIter, in filling_oper_method theMethod, in boolean theApprox)
```

Create a face from a given set of contours.

Parameters
:   |  |  |
    | --- | --- |
    | theContours | either a list or a compound of edges/wires. |
    | theMinDeg | a minimal degree of BSpline surface to create. |
    | theMaxDeg | a maximal degree of BSpline surface to create. |
    | theTol2D | a 2d tolerance to be reached. |
    | theTol3D | a 3d tolerance to be reached. |
    | theNbIter | a number of iteration of approximation algorithm. |
    | theMethod | Kind of method to perform filling operation. |
    | theApprox | Boolean indicating if result should be approximated. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) (face), containing the created filling surface.

### MakeThruSections()

```python
GEOM_Object MakeThruSections(in ListOfGO theSeqSections, in boolean theModeSolid, in double thePreci, in boolean theRuled)
```

Create a shell or solid passing through set of sections.Sections should be wires,edges or vertices.

Parameters
:   |  |  |
    | --- | --- |
    | theSeqSections | - set of specified sections. |
    | theModeSolid | - mode defining building solid or shell |
    | thePreci | - precision 3D used for smoothing by default 1.e-6 |
    | theRuled | - mode defining type of the result surfaces (ruled or smoothed). |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created shell or solid.

### MakePipeWithDifferentSections()

```python
ListOfGO MakePipeWithDifferentSections(in ListOfGO theSeqBases, in ListOfGO theLocations, in GEOM_Object thePath, in boolean theWithContact, in boolean theWithCorrection, in boolean IsBySteps, in boolean IsGenerateGroups)
```

Create a shape by extrusion of the profile shape along the path shape.

The path shape can be a wire or an edge. the several profiles can be specified in the several locations of path.

Parameters
:   |  |  |
    | --- | --- |
    | theSeqBases | - list of Bases shape to be extruded. |
    | theLocations | - list of locations on the path corresponding specified list of the Bases shapes. Number of locations should be equal to number of bases or list of locations can be empty. |
    | thePath | - Path shape to extrude the base shape along it. |
    | theWithContact | - the mode defining that the section is translated to be in contact with the spine. Ignored if IsBySteps is set. |
    | theWithCorrection | - defining that the section is rotated to be orthogonal to the spine tangent in the correspondent point. Ignored if IsBySteps is set. |
    | IsBySteps | - flag that tells if the result should be created step by step or as a whole. If IsBySteps is set no correction of bases is allowed. |
    | IsGenerateGroups | flag that tells if it is necessary to return groups (true) or not (false). |

Returns
:   The list of objects. The first one is a result pipe, the other ones are the created groups. If *IsGenerateGroups* is not set the returned list contains a single object, which is the operation result.

### MakePipeWithShellSections()

```python
ListOfGO MakePipeWithShellSections(in ListOfGO theSeqBases, in ListOfGO theSeqSubBases, in ListOfGO theLocations, in GEOM_Object thePath, in boolean theWithContact, in boolean theWithCorrection, in boolean IsGenerateGroups)
```

Create a shape by extrusion of the profile shape along the path shape.

The path shape can be a shell or a face. the several profiles can be specified in the several locations of path.

Parameters
:   |  |  |
    | --- | --- |
    | theSeqBases | - list of Bases shape to be extruded. |
    | theSeqSubBases | - list of corresponding sub-shapes of section shapes. |
    | theLocations | - list of locations on the path corresponding specified list of the Bases shapes. Number of locations should be equal to number of bases. |
    | thePath | - Path shape to extrude the base shape along it. |
    | theWithContact | - the mode defining that the section is translated to be in contact with the spine. |
    | theWithCorrection | - defining that the section is rotated to be orthogonal to the spine tangent in the correspondent point |
    | IsGenerateGroups | flag that tells if it is necessary to return groups (true) or not (false). |

Returns
:   The list of objects. The first one is a result pipe, the other ones are the created groups. If *IsGenerateGroups* is not set the returned list contains a single object, which is the operation result.

### MakePipeShellsWithoutPath()

```python
ListOfGO MakePipeShellsWithoutPath(in ListOfGO theSeqBases, in ListOfGO theLocations, in boolean IsGenerateGroups)
```

Create solids between given sections.

Parameters
:   |  |  |
    | --- | --- |
    | theSeqBases | - list of sections (shell or face). |
    | theLocations | - list of corresponding vertexes |
    | IsGenerateGroups | flag that tells if it is necessary to return groups (true) or not (false). |

Returns
:   The list of objects. The first one is a result pipe, the other ones are the created groups. If *IsGenerateGroups* is not set the returned list contains a single object, which is the operation result.

### MakePipeBiNormalAlongVector()

```python
ListOfGO MakePipeBiNormalAlongVector(in GEOM_Object theBase, in GEOM_Object thePath, in GEOM_Object theVec, in boolean IsGenerateGroups)
```

Create a shape by extrusion of the base shape along the path shape with constant bi-normal direction along the given vector.

The path shape can be a wire or an edge.

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be extruded. |
    | thePath | Path shape to extrude the base shape along it. |
    | theVec | Vector defines a constant binormal direction to keep the same angle between the Direction and the sections along the sweep surface. |
    | IsGenerateGroups | flag that tells if it is necessary to return groups (true) or not (false). |

Returns
:   The list of objects. The first one is a result pipe, the other ones are the created groups. If *IsGenerateGroups* is not set the returned list contains a single object, which is the operation result.

### MakeThickening()

```python
GEOM_Object MakeThickening(in GEOM_Object theObject, in ListOfLong theFacesIDs, in double theThickness, in boolean isCopy, in boolean isInside)
```

Make a thick solid from a shape.

If the input is a surface shape (face or shell) the result is a thick solid. If an input shape is a solid the result is a hollowed solid with removed faces.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | face or shell to get thick solid or solid to get hollowed solid. |
    | theFacesIDs | the list of face IDs to be removed from the result. It can be empty. |
    | theThickness | Value of the thickness |
    | isCopy | To make a copy of *theObject* or to modify *theObject* |
    | isInside | If true the thickness is applied towards inside |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created pipe if isCopy = true or the modified object if isCopy = false

### RestorePath()

```python
GEOM_Object RestorePath(in GEOM_Object theShape, in GEOM_Object theBase1, in GEOM_Object theBase2)
```

Build a middle path of a pipe-like shape.

The path shape can be a wire or an edge.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | It can be closed or unclosed pipe-like shell or a pipe-like solid. |
    | theBase1,theBase2 | Two bases of the supposed pipe. This should be wires or faces of *theShape*. |

Note
:   It is not assumed that exact or approximate copy of *theShape* can be obtained by applying existing Pipe operation on the resulting "Path" wire taking *theBase1* as the base - it is not always possible; though in some particular cases it might work it is not guaranteed. Thus, RestorePath function should not be considered as an exact reverse operation of the Pipe.

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing an edge or wire that represent source pipe's "path".

### RestorePathEdges()

```python
GEOM_Object RestorePathEdges(in GEOM_Object theShape, in ListOfGO theBase1, in ListOfGO theBase2)
```

Build a middle path of a pipe-like shape.

The path shape can be a wire or an edge.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | It can be closed or unclosed pipe-like shell or a pipe-like solid. |
    | theBase1,theBase2 | Two bases of the supposed pipe. This should be lists of edges of *theShape*. |

Note
:   It is not assumed that exact or approximate copy of *theShape* can be obtained by applying existing Pipe operation on the resulting "Path" wire taking *theBase1* as the base - it is not always possible; though in some particular cases it might work it is not guaranteed. Thus, RestorePath function should not be considered as an exact reverse operation of the Pipe.

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing an edge or wire that represent source pipe's "path".

### IsDone()

```python
boolean IsDone() inherited
```

To know, if the operation was successfully performed.

### SetErrorCode()

```python
void SetErrorCode(in string theErrorID) inherited
```

Set the operation error code.

Parameters
:   |  |  |
    | --- | --- |
    | theErrorID | is a string describing the error occurred |

Note
:   This method is supposed to be used only by interfaces inheriting from IOperations.

### GetErrorCode()

```python
string GetErrorCode() inherited
```

Get the operation error code.

### StartOperation()

```python
void StartOperation() inherited
```

Opens a new transaction.

### FinishOperation()

```python
void FinishOperation() inherited
```

Closes the previously opened transaction.

### AbortOperation()

```python
void AbortOperation() inherited
```

Aborts the previously opened transaction.
