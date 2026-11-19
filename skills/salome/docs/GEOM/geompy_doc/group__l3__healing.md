<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l3__healing.html -->

# Repairing Operations geomBuilder Python module » All package methods, grouped by their purpose » Transforming geometrical objects

## Detailed Description

## Function Documentation

### ChangeOrientation()

```python
def ChangeOrientation(self, theShape, theName = None)
```

Reverses an orientation the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be reversed. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   The reversed copy of theShape.

[Example](../tui_test_all_page.md#swig_ChangeOrientation)

### OrientationChange()

```python
def OrientationChange(self, theShape, theName = None)
```

See [ChangeOrientation()](group__l3__healing.md#ga73c098d82703e790cb5cb75d531936a2) method for details.

[Example](../tui_test_others_page.md#swig_OrientationChange)

### ProcessShape()

```python
def ProcessShape(self, theShape, theOperators, theParameters, theValues, theName = None)
```

Apply a sequence of Shape Healing operators to the given object.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be processed. |
    | theOperators | List of names of operators ("FixShape", "SplitClosedFaces", etc.). |
    | theParameters | List of names of parameters ("FixShape.Tolerance3d", "SplitClosedFaces.NbSplitPoints", etc.). |
    | theValues | List of values of parameters, in the same order as parameters are listed in *theParameters* list. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

**Operators and Parameters:**

- **FixShape** - corrects invalid shapes.
- **FixShape.Tolerance3d** - work tolerance for detection of the problems and correction of them.
- **FixShape.MaxTolerance3d** - maximal possible tolerance of the shape after correction.
- **FixFaceSize** - removes small faces, such as spots and strips.
- **FixFaceSize.Tolerance** - defines minimum possible face size.
- **DropSmallEdges** - removes edges, which merge with neighbouring edges.
- **DropSmallEdges.Tolerance3d** - defines minimum possible distance between two parallel edges.
- **DropSmallSolids** - either removes small solids or merges them with neighboring ones.
- **DropSmallSolids.WidthFactorThreshold** - defines maximum value of *2V/S* of a solid which is considered small, where *V* is volume and *S* is surface area of the solid.
- **DropSmallSolids.VolumeThreshold** - defines maximum volume of a solid which is considered small. If the both tolerances are privided a solid is considered small if it meets the both criteria.
- **DropSmallSolids.MergeSolids** - if "1", small solids are removed; if "0" small solids are merged to adjacent non-small solids or left untouched if cannot be merged.
- **SplitAngle** - splits faces based on conical surfaces, surfaces of revolution and cylindrical surfaces in segments using a certain angle.
- **SplitAngle.Angle** - the central angle of the resulting segments (i.e. we obtain two segments if Angle=180, four if Angle=90, etc).
- **SplitAngle.MaxTolerance** - maximum possible tolerance among the resulting segments.
- **SplitClosedFaces** - splits closed faces in segments. The number of segments depends on the number of splitting points.
- **SplitClosedFaces.NbSplitPoints** - the number of splitting points.
- **SplitContinuity** - splits shapes to reduce continuities of curves and surfaces.
- **SplitContinuity.Tolerance3d** - 3D tolerance for correction of geometry.
- **SplitContinuity.SurfaceContinuity** - required continuity for surfaces.
- **SplitContinuity.CurveContinuity** - required continuity for curves.  
  This and the previous parameters can take the following values:  
  **Parametric** **Continuity**   
  **C0** (Positional Continuity): curves are joined (the end positions of curves or surfaces are coincidental. The curves or surfaces may still meet at an angle, giving rise to a sharp corner or edge).  
  **C1** (Tangential Continuity): first derivatives are equal (the end vectors of curves or surfaces are parallel, ruling out sharp edges).  
  **C2** (Curvature Continuity): first and second derivatives are equal (the end vectors of curves or surfaces are of the same magnitude).  
  **CN** N-th derivatives are equal (both the direction and the magnitude of the Nth derivatives of curves or surfaces (d/du C(u)) are the same at junction.   
  **Geometric** **Continuity**   
  **G1:** first derivatives are proportional at junction.  
  The curve tangents thus have the same direction, but not necessarily the same magnitude. i.e., C1'(1) = (a,b,c) and C2'(0) = (k*a, k*b, k*c).  
  **G2:** first and second derivatives are proportional at junction. As the names imply, geometric continuity requires the geometry to be continuous, while parametric continuity requires that the underlying parameterization was continuous as well. Parametric continuity of order n implies geometric continuity of order n, but not vice-versa.
- **BsplineRestriction** - converts curves and surfaces to Bsplines and processes them with the following parameters:
- **BSplineRestriction.SurfaceMode** - approximation of surfaces if restriction is necessary.
- **BSplineRestriction.Curve3dMode** - conversion of any 3D curve to BSpline and approximation.
- **BSplineRestriction.Curve2dMode** - conversion of any 2D curve to BSpline and approximation.
- **BSplineRestriction.Tolerance3d** - defines the possibility of surfaces and 3D curves approximation with the specified parameters.
- **BSplineRestriction.Tolerance2d** - defines the possibility of surfaces and 2D curves approximation with the specified parameters.
- **BSplineRestriction.RequiredDegree** - required degree of the resulting BSplines.
- **BSplineRestriction.RequiredNbSegments** - required maximum number of segments of resultant BSplines.
- **BSplineRestriction.Continuity3d** - continuity of the resulting surfaces and 3D curves.
- **BSplineRestriction.Continuity2d** - continuity of the resulting 2D curves.
- **ToBezier** - converts curves and surfaces of any type to Bezier curves and surfaces.
- **ToBezier.SurfaceMode** - if checked in, allows conversion of surfaces.
- **ToBezier.Curve3dMode** - if checked in, allows conversion of 3D curves.
- **ToBezier.Curve2dMode** - if checked in, allows conversion of 2D curves.
- **ToBezier.MaxTolerance** - defines tolerance for detection and correction of problems.
- **SameParameter** - fixes edges of 2D and 3D curves not having the same parameter.
- **SameParameter.Tolerance3d** - defines tolerance for fixing of edges.

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

[Example](../tui_repairing_operations_page.md#tui_shape_processing)

### SuppressFaces()

```python
def SuppressFaces(self, theObject, theFaces, theName = None)
```

Remove faces from the given object (shape).

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | theFaces | Indices of faces to be removed, if EMPTY then the method removes ALL faces of the given object. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

[Example](../tui_repairing_operations_page.md#tui_suppress_faces)

### MakeSewing()

```python
def MakeSewing(self, ListShape, theTolerance, AllowNonManifold = False, theName = None)
```

Sewing of faces into a single shell.

Parameters
:   |  |  |
    | --- | --- |
    | ListShape | Shapes to be processed. |
    | theTolerance | Required tolerance value. |
    | AllowNonManifold | Flag that allows non-manifold sewing. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing a result shell.

[Example](../tui_repairing_operations_page.md#tui_sewing)

### Sew()

```python
def Sew(self, ListShape, theTolerance, AllowNonManifold = False, theName = None)
```

Sewing of faces into a single shell.

Parameters
:   |  |  |
    | --- | --- |
    | ListShape | Shapes to be processed. |
    | theTolerance | Required tolerance value. |
    | AllowNonManifold | Flag that allows non-manifold sewing. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing a result shell.

### RemoveInternalFaces()

```python
def RemoveInternalFaces(self, theSolids, theName = None)
```

Rebuild the topology of theSolids by removing the faces that are shared by several solids.

Parameters
:   |  |  |
    | --- | --- |
    | theSolids | A compound or a list of solids to be processed. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

[Example](../tui_repairing_operations_page.md#tui_remove_webs)

### SuppressInternalWires()

```python
def SuppressInternalWires(self, theObject, theWires, theName = None)
```

Remove internal wires and edges from the given object (face).

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | theWires | Indices of wires to be removed, if EMPTY then the method removes ALL internal wires of the given object. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

[Example](../tui_repairing_operations_page.md#tui_suppress_internal_wires)

### SuppressHoles()

```python
def SuppressHoles(self, theObject, theWires, theName = None)
```

Remove internal closed contours (holes) from the given object.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | theWires | Indices of wires to be removed, if EMPTY then the method removes ALL internal holes of the given object |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

[Example](../tui_repairing_operations_page.md#tui_suppress_holes)

### CloseContour()

```python
def CloseContour(self, theObject, theWires, isCommonVertex, theName = None)
```

Close an open wire.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | theWires | Indexes of edge(s) and wire(s) to be closed within *theObject*'s shape, if [ ], then *theObject* itself is a wire. |
    | isCommonVertex | If True : closure by creation of a common vertex, If False : closure by creation of an edge between ends. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

[Example](../tui_repairing_operations_page.md#tui_close_contour)

### DivideEdge()

```python
def DivideEdge(self, theObject, theEdgeIndex, theValue, isByParameter, theName = None)
```

Addition of a point to a given edge object.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | theEdgeIndex | Index of edge to be divided within theObject's shape, if -1, then theObject itself is the edge. |
    | theValue | Value of parameter on edge or length parameter, depending on *isByParameter*. |
    | isByParameter | If TRUE : *theValue* is treated as a curve parameter [0..1],   if FALSE : *theValue* is treated as a length parameter [0..1] |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

[Example](../tui_repairing_operations_page.md#tui_add_point_on_edge)

### DivideEdgeByPoint()

```python
def DivideEdgeByPoint(self, theObject, theEdgeIndex, thePoints, theName = None)
```

Addition of points to a given edge of *theObject* by projecting other points to the given edge.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | theEdgeIndex | Index of edge to be divided within theObject's shape, if -1, then theObject itself is the edge. |
    | thePoints | List of points to project to theEdgeIndex-th edge. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

[Example](../tui_repairing_operations_page.md#tui_add_point_on_edge)

### FuseCollinearEdgesWithinWire()

```python
def FuseCollinearEdgesWithinWire(self, theWire, theVertices = [], theName = None)
```

Suppress the vertices in the wire in case if adjacent edges are C1 continuous.

Parameters
:   |  |  |
    | --- | --- |
    | theWire | Wire to minimize the number of C1 continuous edges in. |
    | theVertices | A list of vertices to suppress. If the list is empty, all vertices in a wire will be assumed. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) with modified wire.

[Example](../tui_repairing_operations_page.md#tui_fuse_collinear_edges)

### ChangeOrientationShell()

```python
def ChangeOrientationShell(self, theObject)
```

Change orientation of the given object.

Updates given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |

Returns
:   Updated *theObject*

Example

### ChangeOrientationShellCopy()

```python
def ChangeOrientationShellCopy(self, theObject, theName = None)
```

Change orientation of the given object.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

Example

### LimitTolerance()

```python
def LimitTolerance(self, theObject, theTolerance = 1e-07, theExactAdjust = False, theName = None)
```

Try to limit tolerance of the given object by value *theTolerance*.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | theTolerance | Required tolerance value. |
    | theExactAdjust | If TRUE, take into account exact tolerance of edges. In some cases, this may result in edge tolerances being increased to values greater than both the original and required ones. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

[Example](../tui_repairing_operations_page.md#tui_limit_tolerance)

### FuncToPythonDump()

```python
def FuncToPythonDump(self, theObject, result, imports, funcName, args)
```

Provides Python dump functionality for algorithms entirely implemented in Python.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | result | Shape of the algorithm execution. |
    | imports | module import for current functon.. |
    | funcName | name of a Python function that we need to put into dump. |
    | args | arguments of the Python function. |

### GetFreeBoundary()

```python
def GetFreeBoundary(self, theObject, theName = None)
```

Get a list of wires (wrapped in [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)-s), that constitute a free boundary of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to get free boundary of. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   [*status*, *theClosedWires*, *theOpenWires*]   
    *status:* FALSE, if an error(s) occurred during the method execution.   
    *theClosedWires:* Closed wires on the free boundary of the given shape.   
    *theOpenWires:* Open wires on the free boundary of the given shape.

[Example](../tui_free_boundaries_page.md)

### MakeGlueFaces()

```python
def MakeGlueFaces(self, theShapes, theTolerance, doKeepNonSolids = True, theName = None)
```

Replace coincident faces in *theShapes* by one face.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Initial shapes, either a list or compound of shapes. |
    | theTolerance | Maximum distance between faces, which can be considered as coincident. |
    | doKeepNonSolids | If FALSE, only solids will present in the result, otherwise all initial shapes. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing copies of theShapes without coincident faces.

[Example](../tui_repairing_operations_page.md#tui_glue_faces)

### GetGlueFaces()

```python
def GetGlueFaces(self, theShapes, theTolerance, theName = None)
```

Find coincident faces in *theShapes* for possible gluing.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Initial shapes, either a list or compound of shapes. |
    | theTolerance | Maximum distance between faces, which can be considered as coincident. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   [GEOM.ListOfGO](namespaceGEOM.md#ac39b0b590404baa7bae2974f34cfc067)

[Example](../tui_repairing_operations_page.md#tui_glue_faces)

### MakeGlueFacesByList()

```python
def MakeGlueFacesByList(self, theShapes, theTolerance, theFaces, doKeepNonSolids = True, doGlueAllEdges = True, theName = None)
```

Replace coincident faces in *theShapes* by one face in compliance with given list of faces.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Initial shapes, either a list or compound of shapes. |
    | theTolerance | Maximum distance between faces, which can be considered as coincident. |
    | theFaces | List of faces for gluing. |
    | doKeepNonSolids | If FALSE, only solids will present in the result, otherwise all initial shapes. |
    | doGlueAllEdges | If TRUE, all coincident edges of *theShape* will be glued, otherwise only the edges, belonging to *theFaces*. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing copies of theShapes without coincident faces.

[Example](../tui_repairing_operations_page.md#tui_glue_faces)

### MakeGlueEdges()

```python
def MakeGlueEdges(self, theShapes, theTolerance, theName = None)
```

Replace coincident edges in *theShapes* by one edge.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Initial shapes, either a list or compound of shapes. |
    | theTolerance | Maximum distance between edges, which can be considered as coincident. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing copies of theShapes without coincident edges.

[Example](../tui_repairing_operations_page.md#tui_glue_edges)

### GetGlueEdges()

```python
def GetGlueEdges(self, theShapes, theTolerance, theName = None)
```

Find coincident edges in *theShapes* for possible gluing.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Initial shapes, either a list or compound of shapes. |
    | theTolerance | Maximum distance between edges, which can be considered as coincident. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   [GEOM.ListOfGO](namespaceGEOM.md#ac39b0b590404baa7bae2974f34cfc067)

[Example](../tui_repairing_operations_page.md#tui_glue_edges)

### MakeGlueEdgesByList()

```python
def MakeGlueEdgesByList(self, theShapes, theTolerance, theEdges, theName = None)
```

Replace coincident edges in theShapes by one edge in compliance with given list of edges.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Initial shapes, either a list or compound of shapes. |
    | theTolerance | Maximum distance between edges, which can be considered as coincident. |
    | theEdges | List of edges for gluing. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing copies of theShapes without coincident edges.

[Example](../tui_repairing_operations_page.md#tui_glue_edges)
