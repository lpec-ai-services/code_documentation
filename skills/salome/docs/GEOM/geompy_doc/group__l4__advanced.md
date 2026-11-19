<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l4__advanced.html -->

# Advanced objects creation functions geomBuilder Python module » All package methods, grouped by their purpose » Creating geometrical objects » Creating Advanced Geometrical Objects

## Detailed Description

## Function Documentation

### MakeDividedCylinder()

```python
def MakeDividedCylinder(self, theR, theH, thePattern, theName = None)
```

Builds a cylinder prepared for hexa meshes.

Parameters
:   |  |  |
    | --- | --- |
    | theR | Radius of the cylinder |
    | theH | Height of the cylinder |
    | thePattern | Division pattern. It can be GEOM.SQUARE or GEOM.HEXAGON |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New GEOM_Object, containing the created shape.

[Example](../tui_advanced_geom_objs_page.md#tui_creation_dividedcylinder)

### MakeDividedDisk()

```python
def MakeDividedDisk(self, theR, theOrientation, thePattern, theName = None)
```

This function allows creating a disk already divided into blocks.

It can be used to create divided pipes for later meshing in hexaedra.

Parameters
:   |  |  |
    | --- | --- |
    | theR | Radius of the disk |
    | theOrientation | Orientation of the plane on which the disk will be built 1 = XOY, 2 = OYZ, 3 = OZX |
    | thePattern | Division pattern. It can be GEOM.SQUARE or GEOM.HEXAGON |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New GEOM_Object, containing the created shape.

[Example](../tui_advanced_geom_objs_page.md#tui_creation_divideddisk)

### MakeDividedDiskPntVecR()

```python
def MakeDividedDiskPntVecR(self, theCenter, theVector, theRadius, thePattern, theName = None)
```

This function allows creating a disk already divided into blocks.

It can be used to create divided pipes for later meshing in hexaedra.

Parameters
:   |  |  |
    | --- | --- |
    | theCenter | Center of the disk |
    | theVector | Normal vector to the plane of the created disk |
    | theRadius | Radius of the disk |
    | thePattern | Division pattern. It can be GEOM.SQUARE or GEOM.HEXAGON |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New GEOM_Object, containing the created shape.

[Example](../tui_advanced_geom_objs_page.md#tui_creation_divideddisk)

### MakePipeTShape()

```python
def MakePipeTShape(self, theR1, theW1, theL1, theR2, theW2, theL2, theHexMesh = True, theP1 = None, theP2 = None, theP3 = None, theRL = 0, theWL = 0, theLtransL = 0, theLthinL = 0, theRR = 0, theWR = 0, theLtransR = 0, theLthinR = 0, theRI = 0, theWI = 0, theLtransI = 0, theLthinI = 0, theName = None)
```

Create a T-shape object with specified caracteristics for the main and the incident pipes (radius, width, half-length).

The extremities of the main pipe are located on junctions points P1 and P2. The extremity of the incident pipe is located on junction point P3. If P1, P2 and P3 are not given, the center of the shape is (0,0,0) and the main plane of the T-shape is XOY.

Parameters
:   |  |  |
    | --- | --- |
    | theR1 | Internal radius of main pipe |
    | theW1 | Width of main pipe |
    | theL1 | Half-length of main pipe |
    | theR2 | Internal radius of incident pipe (R2 < R1) |
    | theW2 | Width of incident pipe (R2+W2 < R1+W1) |
    | theL2 | Half-length of incident pipe |
    | theHexMesh | Boolean indicating if shape is prepared for hex mesh (default=True) |
    | theP1 | 1st junction point of main pipe |
    | theP2 | 2nd junction point of main pipe |
    | theP3 | Junction point of incident pipe |
    | theRL | Internal radius of left thickness reduction |
    | theWL | Width of left thickness reduction |
    | theLtransL | Length of left transition part |
    | theLthinL | Length of left thin part |
    | theRR | Internal radius of right thickness reduction |
    | theWR | Width of right thickness reduction |
    | theLtransR | Length of right transition part |
    | theLthinR | Length of right thin part |
    | theRI | Internal radius of incident thickness reduction |
    | theWI | Width of incident thickness reduction |
    | theLtransI | Length of incident transition part |
    | theLthinI | Length of incident thin part |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created shape and propagation groups.

[Example](../tui_advanced_geom_objs_page.md#tui_creation_pipetshape)

### MakePipeTShapeChamfer()

```python
def MakePipeTShapeChamfer(self, theR1, theW1, theL1, theR2, theW2, theL2, theH, theW, theHexMesh = True, theP1 = None, theP2 = None, theP3 = None, theRL = 0, theWL = 0, theLtransL = 0, theLthinL = 0, theRR = 0, theWR = 0, theLtransR = 0, theLthinR = 0, theRI = 0, theWI = 0, theLtransI = 0, theLthinI = 0, theName = None)
```

Create a T-shape object with chamfer and with specified caracteristics for the main and the incident pipes (radius, width, half-length).

The chamfer is created on the junction of the pipes. The extremities of the main pipe are located on junctions points P1 and P2. The extremity of the incident pipe is located on junction point P3. If P1, P2 and P3 are not given, the center of the shape is (0,0,0) and the main plane of the T-shape is XOY.

Parameters
:   |  |  |
    | --- | --- |
    | theR1 | Internal radius of main pipe |
    | theW1 | Width of main pipe |
    | theL1 | Half-length of main pipe |
    | theR2 | Internal radius of incident pipe (R2 < R1) |
    | theW2 | Width of incident pipe (R2+W2 < R1+W1) |
    | theL2 | Half-length of incident pipe |
    | theH | Height of the chamfer. |
    | theW | Width of the chamfer. |
    | theHexMesh | Boolean indicating if shape is prepared for hex mesh (default=True) |
    | theP1 | 1st junction point of main pipe |
    | theP2 | 2nd junction point of main pipe |
    | theP3 | Junction point of incident pipe |
    | theRL | Internal radius of left thickness reduction |
    | theWL | Width of left thickness reduction |
    | theLtransL | Length of left transition part |
    | theLthinL | Length of left thin part |
    | theRR | Internal radius of right thickness reduction |
    | theWR | Width of right thickness reduction |
    | theLtransR | Length of right transition part |
    | theLthinR | Length of right thin part |
    | theRI | Internal radius of incident thickness reduction |
    | theWI | Width of incident thickness reduction |
    | theLtransI | Length of incident transition part |
    | theLthinI | Length of incident thin part |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created shape and propagation groups.

[Example](../tui_advanced_geom_objs_page.md#tui_creation_pipetshape)

### MakePipeTShapeFillet()

```python
def MakePipeTShapeFillet(self, theR1, theW1, theL1, theR2, theW2, theL2, theRF, theHexMesh = True, theP1 = None, theP2 = None, theP3 = None, theRL = 0, theWL = 0, theLtransL = 0, theLthinL = 0, theRR = 0, theWR = 0, theLtransR = 0, theLthinR = 0, theRI = 0, theWI = 0, theLtransI = 0, theLthinI = 0, theName = None)
```

Create a T-shape object with fillet and with specified caracteristics for the main and the incident pipes (radius, width, half-length).

The fillet is created on the junction of the pipes. The extremities of the main pipe are located on junctions points P1 and P2. The extremity of the incident pipe is located on junction point P3. If P1, P2 and P3 are not given, the center of the shape is (0,0,0) and the main plane of the T-shape is XOY.

Parameters
:   |  |  |
    | --- | --- |
    | theR1 | Internal radius of main pipe |
    | theW1 | Width of main pipe |
    | theL1 | Half-length of main pipe |
    | theR2 | Internal radius of incident pipe (R2 < R1) |
    | theW2 | Width of incident pipe (R2+W2 < R1+W1) |
    | theL2 | Half-length of incident pipe |
    | theRF | Radius of curvature of fillet. |
    | theHexMesh | Boolean indicating if shape is prepared for hex mesh (default=True) |
    | theP1 | 1st junction point of main pipe |
    | theP2 | 2nd junction point of main pipe |
    | theP3 | Junction point of incident pipe |
    | theRL | Internal radius of left thickness reduction |
    | theWL | Width of left thickness reduction |
    | theLtransL | Length of left transition part |
    | theLthinL | Length of left thin part |
    | theRR | Internal radius of right thickness reduction |
    | theWR | Width of right thickness reduction |
    | theLtransR | Length of right transition part |
    | theLthinR | Length of right thin part |
    | theRI | Internal radius of incident thickness reduction |
    | theWI | Width of incident thickness reduction |
    | theLtransI | Length of incident transition part |
    | theLthinI | Length of incident thin part |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created shape and propagation groups.

[Example](../tui_advanced_geom_objs_page.md#tui_creation_pipetshape)

### MakeSmoothingSurface()

```python
def MakeSmoothingSurface(self, thelPoints, theNbMax = 2, theDegMax = 8, theDMax = 0.0, theName = None)
```

Create a surface from a cloud of points.

Parameters
:   |  |  |
    | --- | --- |
    | thelPoints | list of points. Compounds of points are accepted as well. |
    | theNbMax | maximum number of Bezier pieces in the resulting surface. |
    | theDegMax | maximum degree of the resulting BSpline surface. |
    | theDMax | 3D tolerance of initial approximation. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New GEOM_Object, containing the created shape.

Note
:   3D tolerance of initial approximation represents a tolerance of initial plate surface approximation. If this parameter is equal to 0 (default value) it is computed. In this case an error of initial plate surface computation is used as the approximation tolerance. This error represents a maximal distance between computed plate surface and given points.

[Example](../tui_advanced_geom_objs_page.md#tui_creation_smoothingsurface)
