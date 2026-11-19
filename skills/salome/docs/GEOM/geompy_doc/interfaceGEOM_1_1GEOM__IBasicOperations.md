<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__IBasicOperations.html -->

# GEOM_IBasicOperations Interface Reference

Interface for basic geometry creation.
[More...](interfaceGEOM_1_1GEOM__IBasicOperations.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for basic geometry creation.

(Point, Vector, Plane, Marker)

## Member Function Documentation

### MakePointXYZ()

```python
GEOM_Object MakePointXYZ(in double theX, in double theY, in double theZ)
```

Create point by three coordinates.

Parameters
:   |  |  |
    | --- | --- |
    | theX | The X coordinate of the point. |
    | theY | The Y coordinate of the point. |
    | theZ | The Z coordinate of the point. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

### MakePointWithReference()

```python
GEOM_Object MakePointWithReference(in GEOM_Object theReference, in double theX, in double theY, in double theZ)
```

Create a point, distant from the referenced point on the given distances along the coordinate axes.

Parameters
:   |  |  |
    | --- | --- |
    | theReference | The referenced point. |
    | theX | Displacement from the referenced point along OX axis. |
    | theY | Displacement from the referenced point along OY axis. |
    | theZ | Displacement from the referenced point along OZ axis. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

### MakePointOnCurve()

```python
GEOM_Object MakePointOnCurve(in GEOM_Object theRefCurve, in double theParameter, in boolean takeOrientationIntoAccount)
```

Create a point, corresponding to the given parameter on the given curve.

Parameters
:   |  |  |
    | --- | --- |
    | theRefCurve | The referenced curve. |
    | theParameter | Value of parameter on the referenced curve. |
    | takeOrientationIntoAccount | flag that tells if it is necessary to take the curve's orientation into account. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

### MakePointOnCurveByLength()

```python
GEOM_Object MakePointOnCurveByLength(in GEOM_Object theRefCurve, in double theLength, in GEOM_Object theStartPoint)
```

Create a point, corresponding to the given length on the given curve.

Parameters
:   |  |  |
    | --- | --- |
    | theRefCurve | The referenced curve. |
    | theLength | Length on the referenced curve. It can be negative. |
    | theStartPoint | Any vertex close to one of edge's ends to select start point among them. If NULL, fist vertex is used. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

### MakePointOnCurveByCoord()

```python
GEOM_Object MakePointOnCurveByCoord(in GEOM_Object theRefCurve, in double theXParameter, in double theYParameter, in double theZParameter)
```

Create a point on the given curve, projecting given point.

Parameters
:   |  |  |
    | --- | --- |
    | theRefCurve | The referenced curve. |
    | theXParameter | X co-ordinate of point to project on curve |
    | theYParameter | Y co-ordinate of point to project on curve |
    | theZParameter | Z co-ordinate of point to project on curve |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

### MakePointOnSurface()

```python
GEOM_Object MakePointOnSurface(in GEOM_Object theRefSurf, in double theUParameter, in double theVParameter)
```

Create a point, corresponding to the given parameters on the given surface.

Parameters
:   |  |  |
    | --- | --- |
    | theRefSurf | The referenced surface. |
    | theUParameter | Value of U-parameter on the referenced surface. |
    | theVParameter | Value of V-parameter on the referenced surface. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

### MakePointOnSurfaceByCoord()

```python
GEOM_Object MakePointOnSurfaceByCoord(in GEOM_Object theRefSurf, in double theXParameter, in double theYParameter, in double theZParameter)
```

Create a point on the given surface, projecting given point.

Parameters
:   |  |  |
    | --- | --- |
    | theRefSurf | The referenced surface. |
    | theXParameter | X co-ordinate of point to project on curve |
    | theYParameter | Y co-ordinate of point to project on curve |
    | theZParameter | Z co-ordinate of point to project on curve |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

### MakePointOnFace()

```python
GEOM_Object MakePointOnFace(in GEOM_Object theFace, in long theNumberOfPnts)
```

Create a point, which lays on the given face. The point will lay in arbitrary place of the face. The only condition on it is a non-zero distance to the face boundary. Such point can be used to uniquely identify the face inside any shape in case, when the shape does not contain overlapped faces.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | The referenced face. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

### MakePointOnLinesIntersection()

```python
GEOM_Object MakePointOnLinesIntersection(in GEOM_Object theRefLine1, in GEOM_Object theRefLine2)
```

Create a point, on two lines intersection.

Parameters
:   |  |  |
    | --- | --- |
    | theRefLine1,theRefLine2 | The referenced lines. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

### MakeTangentOnCurve()

```python
GEOM_Object MakeTangentOnCurve(in GEOM_Object theRefCurve, in double theParameter)
```

Create a vector, corresponding to tangent to the given parameter on the given curve.

Parameters
:   |  |  |
    | --- | --- |
    | theRefCurve | The referenced curve. |
    | theParameter | Value of parameter on the referenced curve.This value should be have value between 0. and 1.. Value of 0. corresponds first parameter of curve; value  1. corresponds last parameter of curve. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

### MakeVectorDXDYDZ()

```python
GEOM_Object MakeVectorDXDYDZ(in double theDX, in double theDY, in double theDZ)
```

Create a vector with the given components.

Parameters
:   |  |  |
    | --- | --- |
    | theDX | X component of the vector. |
    | theDY | Y component of the vector. |
    | theDZ | Z component of the vector. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created vector.

### MakeVectorTwoPnt()

```python
GEOM_Object MakeVectorTwoPnt(in GEOM_Object thePnt1, in GEOM_Object thePnt2)
```

Create a vector between two points.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1 | Start point for the vector. |
    | thePnt2 | End point for the vector. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created vector.

### MakeLine()

```python
GEOM_Object MakeLine(in GEOM_Object thePnt, in GEOM_Object theDir)
```

Create a line, passing through the given point and parallel to the given direction.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Point. The resulting line will pass through it. |
    | theDir | Direction. The resulting line will be parallel to it. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created line.

### MakeLineTwoPnt()

```python
GEOM_Object MakeLineTwoPnt(in GEOM_Object thePnt1, in GEOM_Object thePnt2)
```

Create a line, passing through the given points.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1 | First of two points, defining the line. |
    | thePnt2 | Second of two points, defining the line. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created line.

### MakeLineTwoFaces()

```python
GEOM_Object MakeLineTwoFaces(in GEOM_Object theFace1, in GEOM_Object theFace2)
```

Create a line, given by two faces intersection.

Parameters
:   |  |  |
    | --- | --- |
    | theFace1 | First of two faces, defining the line. |
    | theFace2 | Second of two faces, defining the line. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created line.

### MakePlaneThreePnt()

```python
GEOM_Object MakePlaneThreePnt(in GEOM_Object thePnt1, in GEOM_Object thePnt2, in GEOM_Object thePnt3, in double theTrimSize)
```

Create a plane, passing through the three given points.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1 | First of three points, defining the plane. |
    | thePnt2 | Second of three points, defining the plane. |
    | thePnt3 | Third of three points, defining the plane. |
    | theTrimSize | Half size of a side of quadrangle face, representing the plane. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created plane.

### MakePlanePntVec()

```python
GEOM_Object MakePlanePntVec(in GEOM_Object thePnt, in GEOM_Object theVec, in double theTrimSize)
```

Create a plane, passing through the given point and normal to the given vector.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Point, the plane has to pass through. |
    | theVec | Vector, defining the plane normal direction. |
    | theTrimSize | Half size of a side of quadrangle face, representing the plane. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created plane.

### MakePlaneFace()

```python
GEOM_Object MakePlaneFace(in GEOM_Object theFace, in double theTrimSize)
```

Create a plane, similar to the existing one, but with another size of representing face.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | Referenced plane or LCS(Marker). |
    | theTrimSize | New half size of a side of quadrangle face, representing the plane. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created plane.

### MakePlane2Vec()

```python
GEOM_Object MakePlane2Vec(in GEOM_Object theVec1, in GEOM_Object theVec2, in double theTrimSize)
```

Create a plane, by two vectors.

Parameters
:   |  |  |
    | --- | --- |
    | theVec1 | Vector1, the plane has to pass through first point of this vector. |
    | theVec2 | Vector2, defining the plane normal direction. |
    | theTrimSize | Half size of a side of quadrangle face, representing the plane. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created plane.

### MakePlaneLCS()

```python
GEOM_Object MakePlaneLCS(in GEOM_Object theLCS, in double theTrimSize, in double theOrientation)
```

Create a plane, defined by local coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | theLCS | Referenced LCS(Marker). |
    | theTrimSize | Half size of a side of quadrangle face, representing the plane. |
    | theOrientation | OXY, OYZ or OZX orientation = (1, 2 or 3). |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created plane.

### MakeMarker()

```python
GEOM_Object MakeMarker(in double theOX, in double theOY, in double theOZ, in double theXDX, in double theXDY, in double theXDZ, in double theYDX, in double theYDY, in double theYDZ)
```

Create a local coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | theOX,theOY,theOZ | Three coordinates of coordinate system origin. |
    | theXDX,theXDY,theXDZ | Three components of OX direction |
    | theYDX,theYDY,theYDZ | Three components of OY direction |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created coordinate system.

### MakeMarkerFromShape()

```python
GEOM_Object MakeMarkerFromShape(in GEOM_Object theShape)
```

Create a local coordinate system from shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | The initial shape to detect the coordinate system. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created coordinate system.

### MakeMarkerPntTwoVec()

```python
GEOM_Object MakeMarkerPntTwoVec(in GEOM_Object theOrigin, in GEOM_Object theXVec, in GEOM_Object theYVec)
```

Create a local coordinate system from point and two vectors (DX, DY).

Parameters
:   |  |  |
    | --- | --- |
    | theOrigin | Point of coordinate system origin. |
    | theXVec | Vector of X direction. |
    | theYVec | Vector of Y direction. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created coordinate system.

### MakeTangentPlaneOnFace()

```python
GEOM_Object MakeTangentPlaneOnFace(in GEOM_Object theFace, in double theParameterU, in double theParameterV, in double theTrimSize)
```

Create a tangent plane to specified face in the point with specified parameters.

Values of parameters should be between 0. and 1.0

Parameters
:   |  |  |
    | --- | --- |
    | theFace | - face for which tangent plane shuold be built. |
    | theParameterU | - value of parameter by U |
    | theParameterV | - value of parameter Vthe |
    | theTrimSize | - defines sizes of created face |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the face built on tangent plane.

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
