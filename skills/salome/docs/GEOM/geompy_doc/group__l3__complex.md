<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l3__complex.html -->

# Creating Complex Objects geomBuilder Python module » All package methods, grouped by their purpose » Creating geometrical objects

## Detailed Description

## Function Documentation

### MakePrism()

```python
def MakePrism(self, theBase, thePoint1, thePoint2, theScaleFactor = -1.0, theName = None)
```

Create a shape by extrusion of the base shape along a vector, defined by two points.

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be extruded. |
    | thePoint1 | First end of extrusion vector. |
    | thePoint2 | Second end of extrusion vector. |
    | theScaleFactor | Use it to make prism with scaled second base. Nagative value means not scaled second base. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created prism.

[Example](../tui_complex_objs_page.md#tui_creation_prism)

### MakePrism2Ways()

```python
def MakePrism2Ways(self, theBase, thePoint1, thePoint2, theName = None)
```

Create a shape by extrusion of the base shape along a vector, defined by two points, in 2 Ways (forward/backward).

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be extruded. |
    | thePoint1 | First end of extrusion vector. |
    | thePoint2 | Second end of extrusion vector. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created prism.

[Example](../tui_complex_objs_page.md#tui_creation_prism)

### MakePrismVecH()

```python
def MakePrismVecH(self, theBase, theVec, theH, theScaleFactor = -1.0, theName = None)
```

Create a shape by extrusion of the base shape along the vector, i.e.

all the space, transfixed by the base shape during its translation along the vector on the given distance.

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be extruded. |
    | theVec | Direction of extrusion. |
    | theH | Prism dimension along theVec. |
    | theScaleFactor | Use it to make prism with scaled second base. Negative value means not scaled second base. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created prism.

[Example](../tui_complex_objs_page.md#tui_creation_prism)

### MakePrismVecH2Ways()

```python
def MakePrismVecH2Ways(self, theBase, theVec, theH, theName = None)
```

Create a shape by extrusion of the base shape along the vector, i.e.

all the space, transfixed by the base shape during its translation along the vector on the given distance in 2 Ways (forward/backward).

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be extruded. |
    | theVec | Direction of extrusion. |
    | theH | Prism dimension along theVec in forward direction. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created prism.

[Example](../tui_complex_objs_page.md#tui_creation_prism)

### MakePrismDXDYDZ()

```python
def MakePrismDXDYDZ(self, theBase, theDX, theDY, theDZ, theScaleFactor = -1.0, theName = None)
```

Create a shape by extrusion of the base shape along the dx, dy, dz direction.

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be extruded. |
    | theDX,theDY,theDZ | Directions of extrusion. |
    | theScaleFactor | Use it to make prism with scaled second base. Nagative value means not scaled second base. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created prism.

[Example](../tui_complex_objs_page.md#tui_creation_prism)

### MakePrismDXDYDZ2Ways()

```python
def MakePrismDXDYDZ2Ways(self, theBase, theDX, theDY, theDZ, theName = None)
```

Create a shape by extrusion of the base shape along the dx, dy, dz direction i.e.

all the space, transfixed by the base shape during its translation along the vector on the given distance in 2 Ways (forward/backward).

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be extruded. |
    | theDX,theDY,theDZ | Directions of extrusion. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created prism.

[Example](../tui_complex_objs_page.md#tui_creation_prism)

### MakeRevolution()

```python
def MakeRevolution(self, theBase, theAxis, theAngle, theName = None)
```

Create a shape by revolution of the base shape around the axis on the given angle, i.e.

all the space, transfixed by the base shape during its rotation around the axis on the given angle.

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be rotated. |
    | theAxis | Rotation axis. |
    | theAngle | Rotation angle in radians. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created revolution.

[Example](../tui_complex_objs_page.md#tui_creation_revolution)

### MakeRevolution2Ways()

```python
def MakeRevolution2Ways(self, theBase, theAxis, theAngle, theName = None)
```

Create a shape by revolution of the base shape around the axis on the given angle, i.e.

all the space, transfixed by the base shape during its rotation around the axis on the given angle in both directions (forward/backward)

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be rotated. |
    | theAxis | Rotation axis. |
    | theAngle | Rotation angle in radians. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created revolution.

[Example](../tui_complex_objs_page.md#tui_creation_revolution)

### MakeFilling()

```python
def MakeFilling(self, theContours, theMinDeg = 2, theMaxDeg = 5, theTol2D = 0.0001, theTol3D = 0.0001, theNbIter = 0, theMethod = GEOM.FOM_Default, isApprox = 0, theName = None)
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
    | theMethod | Kind of method to perform filling operation (see [GEOM.filling_oper_method](namespaceGEOM.md#af527e5423e25f5de7b7d1bb66a3eafba) enum). |
    | isApprox | if True, BSpline curves are generated in the process of surface construction. By default it is False, that means the surface is created using given curves. The usage of Approximation makes the algorithm work slower, but allows building the surface for rather complex cases. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) (face), containing the created filling surface.

[Example](../tui_complex_objs_page.md#tui_creation_filling)

### MakeFillingNew()

```python
def MakeFillingNew(self, theContours, theMinDeg = 2, theMaxDeg = 5, theTol3D = 0.0001, theName = None)
```

Create a face from a given set of contours.

This method corresponds to [MakeFilling()](group__l3__complex.md#gadef0a598131001912724bb979c67c596) with isApprox=True.

Parameters
:   |  |  |
    | --- | --- |
    | theContours | either a list or a compound of edges/wires. |
    | theMinDeg | a minimal degree of BSpline surface to create. |
    | theMaxDeg | a maximal degree of BSpline surface to create. |
    | theTol3D | a 3d tolerance to be reached. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) (face), containing the created filling surface.

[Example](../tui_complex_objs_page.md#tui_creation_filling)

### MakeThruSections()

```python
def MakeThruSections(self, theSeqSections, theModeSolid, thePreci, theRuled, theName = None)
```

Create a shell or solid passing through set of sections.Sections should be wires,edges or vertices.

Parameters
:   |  |  |
    | --- | --- |
    | theSeqSections | - set of specified sections. |
    | theModeSolid | - mode defining building solid or shell |
    | thePreci | - precision 3D used for smoothing |
    | theRuled | - mode defining type of the result surfaces (ruled or smoothed). |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created shell or solid.

Example

### MakePipe()

```python
def MakePipe(self, theBase, thePath, IsGenerateGroups = False, theName = None)
```

Create a shape by extrusion of the base shape along the path shape.

The path shape can be a wire or an edge. It is possible to generate groups along with the result by means of setting the flag *IsGenerateGroups*.  
If *thePath* is a closed edge or wire and *IsGenerateGroups* is set, an error is occurred. If *thePath* is not closed edge/wire, the following groups are returned:

- If *theBase* is unclosed edge or wire: "Down", "Up", "Side1", "Side2";
- If *theBase* is closed edge or wire, face or shell: "Down", "Up", "Other".

"Down" and "Up" groups contain:

- Edges if *theBase* is edge or wire;
- Faces if *theBase* is face or shell.

"Side1" and "Side2" groups contain edges generated from the first and last vertices of *theBase*. The first and last vertices are determined taking into account edge/wire orientation.  
"Other" group represents faces generated from the bounding edges of *theBase*.

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be extruded. |
    | thePath | Path shape to extrude the base shape along it. |
    | IsGenerateGroups | flag that tells if it is necessary to create groups. It is equal to False by default. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created pipe if *IsGenerateGroups* is not set. Otherwise it returns a list of [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md). Its first element is the created pipe, the remaining ones are created groups.

[Example](../tui_complex_objs_page.md#tui_creation_pipe)

### MakePipeWithDifferentSections()

```python
def MakePipeWithDifferentSections(self, theSeqBases, theLocations, thePath, theWithContact, theWithCorrection, IsGenerateGroups = False, theName = None)
```

Create a shape by extrusion of the profile shape along the path shape.

The path shape can be a wire or an edge. the several profiles can be specified in the several locations of path. It is possible to generate groups along with the result by means of setting the flag *IsGenerateGroups*. For detailed information on groups that can be created please see the method [MakePipe()](group__l3__complex.md#ga57e3ba48ad97013b1db1082149be2aac).

Parameters
:   |  |  |
    | --- | --- |
    | theSeqBases | - list of Bases shape to be extruded. |
    | theLocations | - list of locations on the path corresponding specified list of the Bases shapes. Number of locations should be equal to number of bases or list of locations can be empty. |
    | thePath | - Path shape to extrude the base shape along it. |
    | theWithContact | - the mode defining that the section is translated to be in contact with the spine. |
    | theWithCorrection | - defining that the section is rotated to be orthogonal to the spine tangent in the correspondent point |
    | IsGenerateGroups | - flag that tells if it is necessary to create groups. It is equal to False by default. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created pipe if *IsGenerateGroups* is not set. Otherwise it returns new [GEOM.ListOfGO](namespaceGEOM.md#ac39b0b590404baa7bae2974f34cfc067). Its first element is the created pipe, the remaining ones are created groups.

[Example](../tui_complex_objs_page.md#tui_creation_pipe_with_diff_sec)

### MakePipeWithDifferentSectionsBySteps()

```python
def MakePipeWithDifferentSectionsBySteps(self, theSeqBases, theLocations, thePath, IsGenerateGroups = False, theName = None)
```

Create a shape by extrusion of the profile shape along the path shape.

This function is a version of [MakePipeWithDifferentSections()](group__l3__complex.md#ga85ff837d5a5f3e535889324ce3f323bb) with the same parameters, except eliminated theWithContact and theWithCorrection. So it is possible to find the description of all parameters is in this method. The difference is that this method performs the operation step by step, i.e. it creates pipes between each pair of neighbor sections and fuses them into a single shape.

[Example](../tui_complex_objs_page.md#tui_creation_pipe_with_diff_sec)

### MakePipeWithShellSections()

```python
def MakePipeWithShellSections(self, theSeqBases, theSeqSubBases, theLocations, thePath, theWithContact, theWithCorrection, IsGenerateGroups = False, theName = None)
```

Create a shape by extrusion of the profile shape along the path shape.

The path shape can be a wire or an edge. the several profiles can be specified in the several locations of path. It is possible to generate groups along with the result by means of setting the flag *IsGenerateGroups*. For detailed information on groups that can be created please see the method [MakePipe()](group__l3__complex.md#ga57e3ba48ad97013b1db1082149be2aac).

Parameters
:   |  |  |
    | --- | --- |
    | theSeqBases | - list of Bases shape to be extruded. Base shape must be shell or face. If number of faces in neighbour sections aren't coincided result solid between such sections will be created using external boundaries of this shells. |
    | theSeqSubBases | - list of corresponding sub-shapes of section shapes. This list is used for searching correspondences between faces in the sections. Size of this list must be equal to size of list of base shapes. |
    | theLocations | - list of locations on the path corresponding specified list of the Bases shapes. Number of locations should be equal to number of bases. First and last locations must be coincided with first and last vertexes of path correspondingly. |
    | thePath | - Path shape to extrude the base shape along it. |
    | theWithContact | - the mode defining that the section is translated to be in contact with the spine. |
    | theWithCorrection | - defining that the section is rotated to be orthogonal to the spine tangent in the correspondent point |
    | IsGenerateGroups | - flag that tells if it is necessary to create groups. It is equal to False by default. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created solids if *IsGenerateGroups* is not set. Otherwise it returns new [GEOM.ListOfGO](namespaceGEOM.md#ac39b0b590404baa7bae2974f34cfc067). Its first element is the created solids, the remaining ones are created groups.

[Example](../tui_complex_objs_page.md#tui_creation_pipe_with_shell_sec)

### MakePipeWithShellSectionsBySteps()

```python
def MakePipeWithShellSectionsBySteps(self, theSeqBases, theSeqSubBases, theLocations, thePath, theWithContact, theWithCorrection, IsGenerateGroups = False, theName = None)
```

Create a shape by extrusion of the profile shape along the path shape.

This function is used only for debug pipe functionality - it is a version of function [MakePipeWithShellSections()](group__l3__complex.md#gac4100c42b06f65b2c5a00618fd817e94) which give a possibility to receive information about creating pipe between each pair of sections step by step.

### MakePipeShellsWithoutPath()

```python
def MakePipeShellsWithoutPath(self, theSeqBases, theLocations, IsGenerateGroups = False, theName = None)
```

Create solids between given sections.

It is possible to generate groups along with the result by means of setting the flag *IsGenerateGroups*. For detailed information on groups that can be created please see the method [MakePipe()](group__l3__complex.md#ga57e3ba48ad97013b1db1082149be2aac).

Parameters
:   |  |  |
    | --- | --- |
    | theSeqBases | - list of sections (shell or face). |
    | theLocations | - list of corresponding vertexes |
    | IsGenerateGroups | - flag that tells if it is necessary to create groups. It is equal to False by default. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created solids if *IsGenerateGroups* is not set. Otherwise it returns new [GEOM.ListOfGO](namespaceGEOM.md#ac39b0b590404baa7bae2974f34cfc067). Its first element is the created solids, the remaining ones are created groups.

[Example](../tui_complex_objs_page.md#tui_creation_pipe_without_path)

### MakePipeBiNormalAlongVector()

```python
def MakePipeBiNormalAlongVector(self, theBase, thePath, theVec, IsGenerateGroups = False, theName = None)
```

Create a shape by extrusion of the base shape along the path shape with constant bi-normal direction along the given vector.

The path shape can be a wire or an edge. It is possible to generate groups along with the result by means of setting the flag *IsGenerateGroups*. For detailed information on groups that can be created please see the method [MakePipe()](group__l3__complex.md#ga57e3ba48ad97013b1db1082149be2aac).

Parameters
:   |  |  |
    | --- | --- |
    | theBase | Base shape to be extruded. |
    | thePath | Path shape to extrude the base shape along it. |
    | theVec | Vector defines a constant binormal direction to keep the same angle between the direction and the sections along the sweep surface. |
    | IsGenerateGroups | flag that tells if it is necessary to create groups. It is equal to False by default. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created pipe if *IsGenerateGroups* is not set. Otherwise it returns new [GEOM.ListOfGO](namespaceGEOM.md#ac39b0b590404baa7bae2974f34cfc067). Its first element is the created pipe, the remaining ones are created groups.

[Example](../tui_complex_objs_page.md#tui_creation_pipe)

### MakeThickSolid()

```python
def MakeThickSolid(self, theShape, theThickness, theFacesIDs = [], theInside = False, theName = None)
```

Makes a thick solid from a shape.

If the input is a surface shape (face or shell) the result is a thick solid. If an input shape is a solid the result is a hollowed solid with removed faces.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Face or Shell to get thick solid or solid to get hollowed solid. |
    | theThickness | Thickness of the resulting solid |
    | theFacesIDs | the list of face IDs to be removed from the result. It is ignored if *theShape* is a face or a shell. It is empty by default. |
    | theInside | If true the thickness is applied towards inside |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created solid

[Example](../tui_complex_objs_page.md#tui_creation_thickness)

### Thicken()

```python
def Thicken(self, theShape, theThickness, theFacesIDs = [], theInside = False)
```

Modifies a shape to make it a thick solid.

If the input is a surface shape (face or shell) the result is a thick solid. If an input shape is a solid the result is a hollowed solid with removed faces.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Face or Shell to get thick solid or solid to get hollowed solid. |
    | theThickness | Thickness of the resulting solid |
    | theFacesIDs | the list of face IDs to be removed from the result. It is ignored if *theShape* is a face or a shell. It is empty by default. |
    | theInside | If true the thickness is applied towards inside |

Returns
:   The modified shape

[Example](../tui_complex_objs_page.md#tui_creation_thickness)

### RestorePath()

```python
def RestorePath(self, theShape, theBase1, theBase2, theName = None)
```

Build a middle path of a pipe-like shape.

The path shape can be a wire or an edge.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | It can be closed or unclosed pipe-like shell or a pipe-like solid. |
    | theBase1,theBase2 | Two bases of the supposed pipe. This should be wires or faces of theShape. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Note
:   It is not assumed that exact or approximate copy of theShape can be obtained by applying existing Pipe operation on the resulting "Path" wire taking theBase1 as the base - it is not always possible; though in some particular cases it might work it is not guaranteed. Thus, RestorePath function should not be considered as an exact reverse operation of the Pipe.

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing an edge or wire that represent source pipe's "path".

[Example](../tui_complex_objs_page.md#tui_creation_pipe_path)

### RestorePathEdges()

```python
def RestorePathEdges(self, theShape, listEdges1, listEdges2, theName = None)
```

Build a middle path of a pipe-like shape.

The path shape can be a wire or an edge.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | It can be closed or unclosed pipe-like shell or a pipe-like solid. |
    | listEdges1,listEdges2 | Two bases of the supposed pipe. This should be lists of edges of theShape. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Note
:   It is not assumed that exact or approximate copy of theShape can be obtained by applying existing Pipe operation on the resulting "Path" wire taking theBase1 as the base - it is not always possible; though in some particular cases it might work it is not guaranteed. Thus, RestorePath function should not be considered as an exact reverse operation of the Pipe.

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing an edge or wire that represent source pipe's "path".

[Example](../tui_complex_objs_page.md#tui_creation_pipe_path)
