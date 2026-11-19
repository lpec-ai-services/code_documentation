<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l3__basic__go.html -->

# Creating Basic Geometric Objects geomBuilder Python module » All package methods, grouped by their purpose » Creating geometrical objects

## Detailed Description

## Function Documentation

### MakeVertex()

```python
def MakeVertex(self, theX, theY, theZ, theName = None)
```

Create point by three coordinates.

Parameters
:   |  |  |
    | --- | --- |
    | theX | The X coordinate of the point. |
    | theY | The Y coordinate of the point. |
    | theZ | The Z coordinate of the point. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

[Example](../tui_basic_geom_objs_page.md#tui_creation_point)

### MakeVertexWithRef()

```python
def MakeVertexWithRef(self, theReference, theX, theY, theZ, theName = None)
```

Create a point, distant from the referenced point on the given distances along the coordinate axes.

Parameters
:   |  |  |
    | --- | --- |
    | theReference | The referenced point. |
    | theX | Displacement from the referenced point along OX axis. |
    | theY | Displacement from the referenced point along OY axis. |
    | theZ | Displacement from the referenced point along OZ axis. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

[Example](../tui_basic_geom_objs_page.md#tui_creation_point)

### MakeVertexOnCurve()

```python
def MakeVertexOnCurve(self, theRefCurve, theParameter, takeOrientationIntoAccount = False, theName = None)
```

Create a point, corresponding to the given parameter on the given curve.

Parameters
:   |  |  |
    | --- | --- |
    | theRefCurve | The referenced curve. |
    | theParameter | Value of parameter on the referenced curve. |
    | takeOrientationIntoAccount | flag that tells if it is necessary to take the curve's orientation into account for the operation. I.e. if this flag is set, the results for the same parameters (except the value 0.5) is different for forward and reversed curves. If it is not set the result is the same. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

[Example](../tui_basic_geom_objs_page.md#tui_creation_point)

### MakeVertexOnCurveByCoord()

```python
def MakeVertexOnCurveByCoord(self, theRefCurve, theX, theY, theZ, theName = None)
```

Create a point by projection give coordinates on the given curve.

Parameters
:   |  |  |
    | --- | --- |
    | theRefCurve | The referenced curve. |
    | theX | X-coordinate in 3D space |
    | theY | Y-coordinate in 3D space |
    | theZ | Z-coordinate in 3D space |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

[Example](../tui_basic_geom_objs_page.md#tui_creation_point)

### MakeVertexOnCurveByLength()

```python
def MakeVertexOnCurveByLength(self, theRefCurve, theLength, theStartPoint = None, theName = None)
```

Create a point, corresponding to the given length on the given curve.

Parameters
:   |  |  |
    | --- | --- |
    | theRefCurve | The referenced curve. |
    | theLength | Length on the referenced curve. It can be negative. |
    | theStartPoint | Point allowing to choose the direction for the calculation of the length. If None, start from the first point of theRefCurve. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

[Example](../tui_basic_geom_objs_page.md#tui_creation_point)

### MakeVertexOnSurface()

```python
def MakeVertexOnSurface(self, theRefSurf, theUParameter, theVParameter, theName = None)
```

Create a point, corresponding to the given parameters on the given surface.

Parameters
:   |  |  |
    | --- | --- |
    | theRefSurf | The referenced surface. |
    | theUParameter | Value of U-parameter on the referenced surface. |
    | theVParameter | Value of V-parameter on the referenced surface. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

[Example](../tui_test_all_page.md#swig_MakeVertexOnSurface)

### MakeVertexOnSurfaceByCoord()

```python
def MakeVertexOnSurfaceByCoord(self, theRefSurf, theX, theY, theZ, theName = None)
```

Create a point by projection give coordinates on the given surface.

Parameters
:   |  |  |
    | --- | --- |
    | theRefSurf | The referenced surface. |
    | theX | X-coordinate in 3D space |
    | theY | Y-coordinate in 3D space |
    | theZ | Z-coordinate in 3D space |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

[Example](../tui_test_all_page.md#swig_MakeVertexOnSurfaceByCoord)

### MakeVertexInsideFace()

```python
def MakeVertexInsideFace(self, theFace, theNumberOfPnts = 1, theName = None)
```

Create a point, which lays on the given face.

The point will lay in arbitrary place of the face. The only condition on it is a non-zero distance to the face boundary. Such point can be used to uniquely identify the face inside any shape in case, when the shape does not contain overlapped faces.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | The referenced face. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

[Example](../tui_test_all_page.md#swig_MakeVertexInsideFace)

### MakeVertexOnLinesIntersection()

```python
def MakeVertexOnLinesIntersection(self, theRefLine1, theRefLine2, theName = None)
```

Create a point on intersection of two lines.

Parameters
:   |  |  |
    | --- | --- |
    | theRefLine1,theRefLine2 | The referenced lines. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

[Example](../tui_test_all_page.md#swig_MakeVertexOnLinesIntersection)

### MakeTangentOnCurve()

```python
def MakeTangentOnCurve(self, theRefCurve, theParameter, theName = None)
```

Create a tangent, corresponding to the given parameter on the given curve.

Parameters
:   |  |  |
    | --- | --- |
    | theRefCurve | The referenced curve. |
    | theParameter | Value of parameter on the referenced curve. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created tangent.

[Example](../tui_test_all_page.md#swig_MakeTangentOnCurve)

### MakeTangentPlaneOnFace()

```python
def MakeTangentPlaneOnFace(self, theFace, theParameterU, theParameterV, theTrimSize, theName = None)
```

Create a tangent plane, corresponding to the given parameter on the given face.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | The face for which tangent plane should be built. |
    | theParameterV | vertical value of the center point (0.0 - 1.0). |
    | theParameterU | horisontal value of the center point (0.0 - 1.0). |
    | theTrimSize | the size of plane. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created tangent.

[Example](../tui_test_all_page.md#swig_MakeTangentPlaneOnFace)

### MakeVectorDXDYDZ()

```python
def MakeVectorDXDYDZ(self, theDX, theDY, theDZ, theName = None)
```

Create a vector with the given components.

Parameters
:   |  |  |
    | --- | --- |
    | theDX | X component of the vector. |
    | theDY | Y component of the vector. |
    | theDZ | Z component of the vector. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created vector.

[Example](../tui_basic_geom_objs_page.md#tui_creation_vector)

### MakeVector()

```python
def MakeVector(self, thePnt1, thePnt2, theName = None)
```

Create a vector between two points.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1 | Start point for the vector. |
    | thePnt2 | End point for the vector. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created vector.

[Example](../tui_basic_geom_objs_page.md#tui_creation_vector)

### MakeLine()

```python
def MakeLine(self, thePnt, theDir, theName = None)
```

Create a line, passing through the given point and parallel to the given direction.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Point. The resulting line will pass through it. |
    | theDir | Direction. The resulting line will be parallel to it. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created line.

[Example](../tui_basic_geom_objs_page.md#tui_creation_line)

### MakeLineTwoPnt()

```python
def MakeLineTwoPnt(self, thePnt1, thePnt2, theName = None)
```

Create a line, passing through the given points.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1 | First of two points, defining the line. |
    | thePnt2 | Second of two points, defining the line. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created line.

[Example](../tui_basic_geom_objs_page.md#tui_creation_line)

### MakeLineTwoFaces()

```python
def MakeLineTwoFaces(self, theFace1, theFace2, theName = None)
```

Create a line on two faces intersection.

Parameters
:   |  |  |
    | --- | --- |
    | theFace1 | First of two faces, defining the line. |
    | theFace2 | Second of two faces, defining the line. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created line.

[Example](../tui_test_all_page.md#swig_MakeLineTwoFaces)

### MakePlane()

```python
def MakePlane(self, thePnt, theVec, theTrimSize, theName = None)
```

Create a plane, passing through the given point and normal to the given vector.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Point, the plane has to pass through. |
    | theVec | Vector, defining the plane normal direction. |
    | theTrimSize | Half size of a side of quadrangle face, representing the plane. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created plane.

[Example](../tui_basic_geom_objs_page.md#tui_creation_plane)

### MakePlaneThreePnt()

```python
def MakePlaneThreePnt(self, thePnt1, thePnt2, thePnt3, theTrimSize, theName = None)
```

Create a plane, passing through the three given points.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1 | First of three points, defining the plane. |
    | thePnt2 | Second of three points, defining the plane. |
    | thePnt3 | Third of three points, defining the plane. |
    | theTrimSize | Half size of a side of quadrangle face, representing the plane. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created plane.

[Example](../tui_basic_geom_objs_page.md#tui_creation_plane)

### MakePlaneFace()

```python
def MakePlaneFace(self, theFace, theTrimSize, theName = None)
```

Create a plane, similar to the existing one, but with another size of representing face.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | Referenced plane or LCS(Marker). |
    | theTrimSize | New half size of a side of quadrangle face, representing the plane. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created plane.

[Example](../tui_basic_geom_objs_page.md#tui_creation_plane)

### MakePlane2Vec()

```python
def MakePlane2Vec(self, theVec1, theVec2, theTrimSize, theName = None)
```

Create a plane, passing through the 2 vectors with center in a start point of the first vector.

Parameters
:   |  |  |
    | --- | --- |
    | theVec1 | Vector, defining center point and plane direction. |
    | theVec2 | Vector, defining the plane normal direction. |
    | theTrimSize | Half size of a side of quadrangle face, representing the plane. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created plane.

[Example](../tui_basic_geom_objs_page.md#tui_creation_plane)

### MakePlaneLCS()

```python
def MakePlaneLCS(self, theLCS, theTrimSize, theOrientation, theName = None)
```

Create a plane, based on a Local coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | theLCS | coordinate system, defining plane. |
    | theTrimSize | Half size of a side of quadrangle face, representing the plane. |
    | theOrientation | OXY, OYZ or OZX orientation - (1, 2 or 3) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created plane.

[Example](../tui_basic_geom_objs_page.md#tui_creation_plane)

### MakeMarker()

```python
def MakeMarker(self, OX, OY, OZ, XDX, XDY, XDZ, YDX, YDY, YDZ, theName = None)
```

Create a local coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | OX,OY,OZ | Three coordinates of coordinate system origin. |
    | XDX,XDY,XDZ | Three components of OX direction |
    | YDX,YDY,YDZ | Three components of OY direction |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created coordinate system.

[Example](../tui_test_all_page.md#swig_MakeMarker)

### MakeMarkerFromShape()

```python
def MakeMarkerFromShape(self, theShape, theName = None)
```

Create a local coordinate system from shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | The initial shape to detect the coordinate system. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created coordinate system.

[Example](../tui_basic_geom_objs_page.md#tui_creation_lcs)

### MakeMarkerPntTwoVec()

```python
def MakeMarkerPntTwoVec(self, theOrigin, theXVec, theYVec, theName = None)
```

Create a local coordinate system from point and two vectors.

Parameters
:   |  |  |
    | --- | --- |
    | theOrigin | Point of coordinate system origin. |
    | theXVec | Vector of X direction |
    | theYVec | Vector of Y direction |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created coordinate system.

[Example](../tui_basic_geom_objs_page.md#tui_creation_lcs)

### MakeEdge()

```python
def MakeEdge(self, thePnt1, thePnt2, theName = None)
```

Create a linear edge with specified ends.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1 | Point for the first end of edge. |
    | thePnt2 | Point for the second end of edge. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created edge.

[Example](../tui_topological_geom_objs_page.md#tui_creation_edge)

### MakeEdgeOnCurveByLength()

```python
def MakeEdgeOnCurveByLength(self, theRefCurve, theLength, theStartPoint = None, theName = None)
```

Create a new edge, corresponding to the given length on the given curve.

Parameters
:   |  |  |
    | --- | --- |
    | theRefCurve | The referenced curve (edge). |
    | theLength | Length on the referenced curve. It can be negative. |
    | theStartPoint | Any point can be selected for it, the new edge will begin at the end of *theRefCurve*, close to the selected point. If None, start from the first point of *theRefCurve*. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created edge.

[Example](../tui_topological_geom_objs_page.md#tui_creation_edge)

### MakeEdgeWire()

```python
def MakeEdgeWire(self, theWire, theLinearTolerance = 1e-07, theAngularTolerance = 1e-12, theName = None)
```

Create an edge from specified wire.

Parameters
:   |  |  |
    | --- | --- |
    | theWire | source Wire |
    | theLinearTolerance | linear tolerance value (default = 1e-07) |
    | theAngularTolerance | angular tolerance value (default = 1e-12) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created edge.

[Example](../tui_topological_geom_objs_page.md#tui_creation_edge)

### MakeWire()

```python
def MakeWire(self, theEdgesAndWires, theTolerance = 1e-07, theName = None)
```

Create a wire from the set of edges and wires.

To close a gap, enlarges wire tolerance.

Parameters
:   |  |  |
    | --- | --- |
    | theEdgesAndWires | List of edges and/or wires. |
    | theTolerance | Maximum distance between vertices, that will be merged. Values less than 1e-07 are equivalent to 1e-07 (Precision::Confusion()) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created wire.

[Example](../tui_topological_geom_objs_page.md#tui_creation_wire)

### MakeWireConstCurveType()

```python
def MakeWireConstCurveType(self, theEdgesAndWires, theTolerance = 1e-07, theName = None)
```

Create a wire from the set of edges and wires.

To close a gap, replaces curves, neighbour to the gap, with new curves of the same type and close parameters, connecting in the middle of the gap.

Parameters
:   |  |  |
    | --- | --- |
    | theEdgesAndWires | List of edges and/or wires. |
    | theTolerance | Maximum distance between vertices, that will be merged. Values less than 1e-07 are equivalent to 1e-07 (Precision::Confusion()) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created wire.

[Example](../tui_topological_geom_objs_page.md#tui_creation_wire)

### MakeWireWithMode()

```python
def MakeWireWithMode(self, theEdgesAndWires, theTolerance = 1e-07, theMode = GEOM.WBM_Approximation, theName = None)
```

Create a wire from the set of edges and wires.

Possible gaps are closed according to theMode.

Parameters
:   |  |  |
    | --- | --- |
    | theEdgesAndWires | List of edges and/or wires. |
    | theTolerance | Maximum distance between vertices, that will be merged. Values less than 1e-07 are equivalent to 1e-07 (Precision::Confusion()) |
    | theMode | [GEOM.wire_build_mode](namespaceGEOM.md#aec4432b39384cbf7ca216262e19eee86) Mode of gaps closing. Possible values are [GEOM.WBM_FixTolerance](namespaceGEOM.md#aec4432b39384cbf7ca216262e19eee86a5055371e45790cb3a13255088f4a504b), [GEOM.WBM_KeepCurveType](namespaceGEOM.md#aec4432b39384cbf7ca216262e19eee86ad7bd1eaed3d7c12ee74702a03b79699f) and [GEOM.WBM_Approximation](namespaceGEOM.md#aec4432b39384cbf7ca216262e19eee86abdd49cb89f70797979b05a1ffd4d3df9). |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created wire.

[Example](../tui_topological_geom_objs_page.md#tui_creation_wire)

### MakeFace()

```python
def MakeFace(self, theWire, isPlanarWanted, theName = None, raiseException = False)
```

Create a face on the given wire.

Parameters
:   |  |  |
    | --- | --- |
    | theWire | closed Wire or Edge to build the face on. |
    | isPlanarWanted | If TRUE, the algorithm tries to build a planar face. If the tolerance of the obtained planar face is less than 1e-06, this face will be returned, otherwise the algorithm tries to build any suitable face on the given wire and prints a warning message. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face (compound of faces).

[Example](../tui_topological_geom_objs_page.md#tui_creation_face)

### MakeFaceWires()

```python
def MakeFaceWires(self, theWires, isPlanarWanted, theName = None, raiseException = False)
```

Create a face on the given wires set.

Parameters
:   |  |  |
    | --- | --- |
    | theWires | List of closed wires or edges to build the face on. |
    | isPlanarWanted | If TRUE, the algorithm tries to build a planar face. If the tolerance of the obtained planar face is less than 1e-06, this face will be returned, otherwise the algorithm tries to build any suitable face on the given wire and prints a warning message. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face (compound of faces).

[Example](../tui_topological_geom_objs_page.md#tui_creation_face)

### MakeFaces()

```python
def MakeFaces(self, theWires, isPlanarWanted, theName = None)
```

See [MakeFaceWires()](group__l3__basic__go.md#ga1f035f4587dba2d4e4466aebf5f085b2) method for details.

[Example 1](../tui_topological_geom_objs_page.md#tui_creation_face)   
[Example 2](../tui_test_others_page.md#swig_MakeFaces)

### MakeFaceFromSurface()

```python
def MakeFaceFromSurface(self, theFace, theWire, theName = None)
```

Create a face based on a surface from given face bounded by given wire.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | the face whose surface is used to create a new face. |
    | theWire | the wire that will bound a new face. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

[Example](../tui_topological_geom_objs_page.md#tui_creation_face)

### MakeWrappedFace()

```python
def MakeWrappedFace(self, theEdges, theVertices, theTolerance, theName = None)
```

Create a bounded face with list of edges and list of vertices.

The list of edges defines the boundary of the desired face and all vertices should lie on it. The result can be a COMPOUND shape with multiple faces, if the underlying surface is somehow split within the given boundary, e.g. by the seam edge of a sphere.

Parameters
:   |  |  |
    | --- | --- |
    | theEdges | list of Edges defining the boundary of the result face (must be closed but not nesessarily belong to the same plane). |
    | theVertices | list of vertices through which the result face must pass (within the given tolerance). |
    | theTolerance | tolerance. |

Returns
:   New GEOM_Object, containing the created shape (FACE or COMPOUND).

[Example](../tui_topological_geom_objs_page.md#tui_creation_face)

### MakeFaceWithConstraints()

```python
def MakeFaceWithConstraints(self, theConstraints, theName = None)
```

Create a face from a set of edges with the given constraints.

Parameters
:   |  |  |
    | --- | --- |
    | theConstraints | List of edges and constraint faces (as a sequence of a Edge + Face couples):  - edges should form a closed wire; - for each edge, constraint face is optional: if a constraint face is missing for some edge, this means that there no constraint associated with this edge. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

[Example](../tui_topological_geom_objs_page.md#tui_creation_face)

### MakeShell()

```python
def MakeShell(self, theFacesAndShells, theName = None)
```

Create a shell from the set of faces, shells and/or compounds of faces.

Parameters
:   |  |  |
    | --- | --- |
    | theFacesAndShells | List of faces, shells and/or compounds of faces. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created shell (compound of shells).

[Example](../tui_topological_geom_objs_page.md#tui_creation_shell)

### MakeSolid()

```python
def MakeSolid(self, theShells, theName = None)
```

Create a solid, bounded by the given shells.

Parameters
:   |  |  |
    | --- | --- |
    | theShells | Sequence of bounding shells. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created solid.

[Example](../tui_topological_geom_objs_page.md#tui_creation_solid)

### MakeCompound()

```python
def MakeCompound(self, theShapes, theName = None)
```

Create a compound of the given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | List of shapes to put in compound. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created compound.

[Example](../tui_topological_geom_objs_page.md#tui_creation_compound)

### MakeSolidFromConnectedFaces()

```python
def MakeSolidFromConnectedFaces(self, theFacesOrShells, isIntersect = False, theName = None)
```

Create a solid (or solids) from the set of faces and/or shells.

Parameters
:   |  |  |
    | --- | --- |
    | theFacesOrShells | List of faces and/or shells. |
    | isIntersect | If TRUE, forces performing intersections between arguments; otherwise (default) intersection is not performed. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created solid (or compound of solids).

[Example](../tui_topological_geom_objs_page.md#tui_creation_solid_from_faces)
