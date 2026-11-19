<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__ICurvesOperations.html -->

# GEOM_ICurvesOperations Interface Reference

Interface for curves creation.
[More...](interfaceGEOM_1_1GEOM__ICurvesOperations.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for curves creation.

Polyline, Circle, Spline (Bezier and Interpolation)

## Member Function Documentation

### MakeCirclePntVecR()

```python
GEOM_Object MakeCirclePntVecR(in GEOM_Object thePnt, in GEOM_Object theVec, in double theR)
```

Create a circle with given center, normal vector and radius.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Circle center. |
    | theVec | Vector, normal to the plane of the circle. |
    | theR | Circle radius. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created circle.

### MakeCircleThreePnt()

```python
GEOM_Object MakeCircleThreePnt(in GEOM_Object thePnt1, in GEOM_Object thePnt2, in GEOM_Object thePnt3)
```

Create a circle, passing through three given points.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1,thePnt2,thePnt3 | Points, defining the circle. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created circle.

### MakeCircleCenter2Pnt()

```python
GEOM_Object MakeCircleCenter2Pnt(in GEOM_Object thePnt1, in GEOM_Object thePnt2, in GEOM_Object thePnt3)
```

Create a circle with given center, with a radius equals the distance from center to Point1 and on a plane defined by all of three points.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1,thePnt2,thePnt3 | Points, defining the circle. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created circle.

### MakeEllipse()

```python
GEOM_Object MakeEllipse(in GEOM_Object thePnt, in GEOM_Object theVec, in double theRMajor, in double theRMinor)
```

Create an ellipse with given center, normal vector and radiuses.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Ellipse center. |
    | theVec | Vector, normal to the plane of the ellipse. |
    | theRMajor | Major ellipse radius. |
    | theRMinor | Minor ellipse radius. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created ellipse.

### MakeEllipseVec()

```python
GEOM_Object MakeEllipseVec(in GEOM_Object thePnt, in GEOM_Object theVec, in double theRMajor, in double theRMinor, in GEOM_Object theVecMaj)
```

Create an ellipse with given center, normal vector, main axis vector and radiuses.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Ellipse center. |
    | theVec | Vector, normal to the plane of the ellipse. |
    | theRMajor | Major ellipse radius. |
    | theRMinor | Minor ellipse radius. |
    | theVecMaj | Vector, direction of the ellipse's main axis. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created ellipse.

### MakeArc()

```python
GEOM_Object MakeArc(in GEOM_Object thePnt1, in GEOM_Object thePnt2, in GEOM_Object thePnt3)
```

Create an arc of circle, passing through three given points.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1 | Start point of the arc. |
    | thePnt2 | Middle point of the arc. |
    | thePnt3 | End point of the arc. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created arc.

### MakeArcCenter()

```python
GEOM_Object MakeArcCenter(in GEOM_Object theCenter, in GEOM_Object thePnt1, in GEOM_Object thePnt2, in boolean theSense)
```

Create an arc of circle of center C from one point to another.

Parameters
:   |  |  |
    | --- | --- |
    | theCenter | Center point of the arc. |
    | thePnt1 | Start point of the arc. |
    | thePnt2 | End point of the arc. |
    | theSense | Orientation of the arc |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created arc.

### MakeArcOfEllipse()

```python
GEOM_Object MakeArcOfEllipse(in GEOM_Object theCenter, in GEOM_Object thePnt1, in GEOM_Object thePnt2)
```

Create an arc of ellipse of center C and two points P1 P2.

Parameters
:   |  |  |
    | --- | --- |
    | theCenter | Center point of the arc. |
    | thePnt1 | Major radius is distance from center to Pnt1. |
    | thePnt2 | define a plane and Minor radius as a shortest distance from Pnt2 to vector Center->Pnt1. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created arc.

### MakePolyline()

```python
GEOM_Object MakePolyline(in ListOfGO thePoints, in boolean theIsClosed)
```

Create a polyline on the set of points.

Parameters
:   |  |  |
    | --- | --- |
    | thePoints | Sequence of points for the polyline. |
    | theIsClosed | If TRUE, build a closed wire. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created polyline.

### MakeSplineBezier()

```python
GEOM_Object MakeSplineBezier(in ListOfGO thePoints, in boolean theIsClosed)
```

Create bezier curve on the set of points.

Parameters
:   |  |  |
    | --- | --- |
    | thePoints | Sequence of points for the bezier curve. |
    | theIsClosed | If TRUE, build a closed curve. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created bezier curve.

### MakeSplineInterpolation()

```python
GEOM_Object MakeSplineInterpolation(in ListOfGO thePoints, in boolean theIsClosed, in boolean theDoReordering)
```

Create B-Spline curve on the set of points.

Parameters
:   |  |  |
    | --- | --- |
    | thePoints | Sequence of points for the B-Spline curve. |
    | theIsClosed | If TRUE, build a closed curve. |
    | theDoReordering | If TRUE, the algo does not follow the order of *thePoints* but searches for the closest vertex. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created B-Spline curve.

### MakeSplineInterpolWithTangents()

```python
GEOM_Object MakeSplineInterpolWithTangents(in ListOfGO thePoints, in GEOM_Object theFirstVec, in GEOM_Object theLastVec)
```

Create B-Spline curve on the set of points.

Parameters
:   |  |  |
    | --- | --- |
    | thePoints | Sequence of points for the B-Spline curve. |
    | theFirstVec | Vector object, defining the curve direction at its first point. |
    | theLastVec | Vector object, defining the curve direction at its last point. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created B-Spline curve.

### MakeCurveParametric()

```python
GEOM_Object MakeCurveParametric(in string thexExpr, in string theyExpr, in string thezExpr, in double theParamMin, in double theParamMax, in double theParamStep, in curve_type theCurveType)
```

Creates a curve using the parametric definition of the basic points.

Parameters
:   |  |  |
    | --- | --- |
    | thexExpr | parametric equation of the coordinates X. |
    | theyExpr | parametric equation of the coordinates Y. |
    | thezExpr | parametric equation of the coordinates Z. |
    | theParamMin | the minimal value of the parameter. |
    | theParamMax | the maximum value of the parameter. |
    | theParamStep | the step of the parameter. |
    | theCurveType | the type of the curve. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created curve.

### MakeCurveParametricNew()

```python
GEOM_Object MakeCurveParametricNew(in string thexExpr, in string theyExpr, in string thezExpr, in double theParamMin, in double theParamMax, in long theParamNbStep, in curve_type theCurveType)
```

Creates a curve using the parametric definition of the basic points.

Parameters
:   |  |  |
    | --- | --- |
    | thexExpr | parametric equation of the coordinates X. |
    | theyExpr | parametric equation of the coordinates Y. |
    | thezExpr | parametric equation of the coordinates Z. |
    | theParamMin | the minimal value of the parameter. |
    | theParamMax | the maximum value of the parameter. |
    | theParamNbStep | the number of steps of the parameter discretization. |
    | theCurveType | the type of the curve. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created curve.

### MakeIsoline()

```python
GEOM_Object MakeIsoline(in GEOM_Object theFace, in boolean IsUIsoline, in double theParameter)
```

Creates an isoline curve on a face.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | the face for which an isoline is created. |
    | IsUIsoline | True for U-isoline creation; False for V-isoline creation. |
    | theParameter | the U parameter for U-isoline or V parameter for V-isoline. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created isoline edge or a compound of edges.

### MakeSketcher()

```python
GEOM_Object MakeSketcher(in string theCommand, in ListOfDouble theWorkingPlane)
```

Create a sketcher (wire or face), following the textual description, passed through *theCommand* argument.

Edges of the resulting wire or face will be arcs of circles and/or linear segments.   
Format of the description string has to be the following:

"Sketcher[:F x1 y1]:CMD[:CMD[:CMD...]]"

Where:

- x1, y1 are coordinates of the first sketcher point (zero by default),
- CMD is one of
  - "R angle" : Set the direction by angle
  - "D dx dy" : Set the direction by DX & DY  
  - "TT x y" : Create segment by point at X & Y
  - "T dx dy" : Create segment by point with DX & DY
  - "L length" : Create segment by direction & Length
  - "IX x" : Create segment by direction & Intersect. X
  - "IY y" : Create segment by direction & Intersect. Y  
  - "C radius length" : Create arc by direction, radius and length(in degree)  
  - "WW" : Close Wire (to finish)
  - "WF" : Close Wire and build face (to finish)

Parameters
:   |  |  |
    | --- | --- |
    | theCommand | String, defining the sketcher in local coordinates of the working plane. |
    | theWorkingPlane | Nine double values, defining origin, OZ and OX directions of the working plane. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created wire or face.

### MakeSketcherOnPlane()

```python
GEOM_Object MakeSketcherOnPlane(in string theCommand, in GEOM_Object theWorkingPlane)
```

Create a sketcher (wire or face), following the textual description, passed through *theCommand* argument.

For format of the description string see the previous method.

Parameters
:   |  |  |
    | --- | --- |
    | theCommand | String, defining the sketcher in local coordinates of the working plane. |
    | theWorkingPlane | Planar Face or LCS(Marker) of the working plane. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created wire or face.

### Make3DSketcherCommand()

```python
GEOM_Object Make3DSketcherCommand(in string theCommand)
```

Create a 3D sketcher, following the textual description, passed through *theCommand* argument.

Format of the description string has to be the following:

"3DSketcher:CMD[:CMD[:CMD...]]"

Where CMD is one of

- "TT x y z" : Create segment by point at X & Y or set the first point
- "T dx dy dz" : Create segment by point with DX & DY

- "OXY angleX angle2 length" : Create segment by two angles and length
- "OYZ angleY angle2 length" : Create segment by two angles and length
- "OXZ angleX angle2 length" : Create segment by two angles and length

- "WW" : Close Wire (to finish)

Parameters
:   |  |  |
    | --- | --- |
    | theCommand | String, defining the sketcher in local coordinates of the working plane. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created wire.

### Make3DSketcher()

```python
GEOM_Object Make3DSketcher(in ListOfDouble theCoordinates)
```

Create a 3D sketcher, made of a straight segments, joining points with coordinates passed through *theCoordinates* argument.

Order of coordinates has to be the following: x1, y1, z1, x2, y2, z2, ..., xN, yN, zN

Parameters
:   |  |  |
    | --- | --- |
    | theCoordinates | List of double values. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created wire.

### MakePolyline2D()

```python
GEOM_Object MakePolyline2D(in ListOfListOfDouble theCoordsList, in string_array theNamesList, in short_array theTypesList, in ListOfBool theClosedList, in ListOfDouble theWorkingPlane)
```

Create a 2D polyline (wire or a compound of wires).

The polyline can have several sections. Each section represents a set of points in the form of list of coordinates of the following order: x1, y1, x2, y2, ..., xN, yN Each section has its own name, type of curve (can be either [GEOM::Polyline](namespaceGEOM.md#a9be4eee4ac6c9248a824d093f165839ead2644bf3c6a9f629a4ef9748db433513) or [GEOM::Interpolation](namespaceGEOM.md#a9be4eee4ac6c9248a824d093f165839eaec0e6acb2e6b6dca1c92c50c2a762470)) and Closed flag. For each section a wire is created. It represents either a polyline or interpolation BSpline either closed or not depending on the Closed flag. The result represents a wire if there is only one section is defined. Otherwise a compound of wires is returned.

Parameters
:   |  |  |
    | --- | --- |
    | theCoordsList | the list of coordinates list. theCoordsList[0] is the coordinates list of the first section. theCoordsList[1] is for the second section etc. |
    | theNamesList | the list of names. The order corresponds to theCoordsList. |
    | theTypesList | the list of curve types. The order corresponds to theCoordsList. |
    | theClosedList | the list of Closed flags. The order corresponds to theCoordsList. |
    | theWorkingPlane | 9 double values, defining origin, OZ and OX directions of the working plane. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created wire or a compound of wires.

### MakePolyline2DOnPlane()

```python
GEOM_Object MakePolyline2DOnPlane(in ListOfListOfDouble theCoordsList, in string_array theNamesList, in short_array theTypesList, in ListOfBool theClosedList, in GEOM_Object theWorkingPlane)
```

Create a 2D polyline (wire or a compound of wires).

The polyline can have several sections. Each section represents a set of points in the form of list of coordinates of the following order: x1, y1, x2, y2, ..., xN, yN Each section has its own name, type of curve (can be either [GEOM::Polyline](namespaceGEOM.md#a9be4eee4ac6c9248a824d093f165839ead2644bf3c6a9f629a4ef9748db433513) or [GEOM::Interpolation](namespaceGEOM.md#a9be4eee4ac6c9248a824d093f165839eaec0e6acb2e6b6dca1c92c50c2a762470)) and Closed flag. For each section a wire is created. It represents either a polyline or interpolation BSpline either closed or not depending on the Closed flag. The result represents a wire if there is only one section is defined. Otherwise a compound of wires is returned.

Parameters
:   |  |  |
    | --- | --- |
    | theCoordsList | the list of coordinates list. theCoordsList[0] is the coordinates list of the first section. theCoordsList[1] is for the second section etc. |
    | theNamesList | the list of names. The order corresponds to theCoordsList. |
    | theTypesList | the list of curve types. The order corresponds to theCoordsList. |
    | theClosedList | the list of Closed flags. The order corresponds to theCoordsList. |
    | theWorkingPlane | planar Face or LCS(Marker) of the working plane. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created wire or a compound of wires.

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
