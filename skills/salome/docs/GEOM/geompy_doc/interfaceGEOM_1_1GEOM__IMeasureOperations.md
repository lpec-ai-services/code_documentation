<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__IMeasureOperations.html -->

# GEOM_IMeasureOperations Interface Reference

Interface for measurement (distance, whatis) and properties calculation (like Centre of Mass, Inertia, etc.).
[More...](interfaceGEOM_1_1GEOM__IMeasureOperations.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for measurement (distance, whatis) and properties calculation (like Centre of Mass, Inertia, etc.).

## Member Typedef Documentation

### ShapeErrors

```python
typedef sequence< ShapeError > ShapeErrors
```

Sequence of all shape defects.

### SequenceOfPairOfShape

```python
typedef sequence< PairOfShape > SequenceOfPairOfShape
```

### CheckResults

```python
typedef sequence< CheckResult > CheckResults
```

## Member Enumeration Documentation

### ShapeErrorType

```python
enum ShapeErrorType
```

Enumeration of Shape defects coming from CheckShape algorithms.

| Enumerator | |
| --- | --- |
| InvalidPointOnCurve |  |
| InvalidPointOnCurveOnSurface |  |
| InvalidPointOnSurface |  |
| No3DCurve |  |
| Multiple3DCurve |  |
| Invalid3DCurve |  |
| NoCurveOnSurface |  |
| InvalidCurveOnSurface |  |
| InvalidCurveOnClosedSurface |  |
| InvalidSameRangeFlag |  |
| InvalidSameParameterFlag |  |
| InvalidDegeneratedFlag |  |
| FreeEdge |  |
| InvalidMultiConnexity |  |
| InvalidRange |  |
| EmptyWire |  |
| RedundantEdge |  |
| SelfIntersectingWire |  |
| NoSurface |  |
| InvalidWire |  |
| RedundantWire |  |
| IntersectingWires |  |
| InvalidImbricationOfWires |  |
| EmptyShell |  |
| RedundantFace |  |
| UnorientableShape |  |
| NotClosed |  |
| NotConnected |  |
| SubshapeNotInShape |  |
| BadOrientation |  |
| BadOrientationOfSubshape |  |
| InvalidToleranceValue |  |
| CheckFail |  |

## Member Function Documentation

### KindOfShape()

```python
GEOM_IKindOfShape::shape_kind KindOfShape(in GEOM_Object theShape, out ListOfLong theIntegers, out ListOfDouble theDoubles)
```

Get kind of theShape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to get a kind of. |
    | theIntegers | Output. Integer and enumerated shape's parameters (kind of surface, closed/unclosed, number of edges, etc.) |
    | theDoubles | Output. Double shape's parameters (coordinates, dimensions, etc.) |

Note
:   Concrete meaning of each value, returned via *theIntegers* or *theDoubles* list depends on the kind of the shape.

Returns
:   Returns a kind of shape in terms of *[GEOM_IKindOfShape.shape_kind](interfaceGEOM_1_1GEOM__IKindOfShape.md#a89b3365676a2806c547d5bc9bf4d9d7c)* enumeration.

### GetPosition()

```python
void GetPosition(in GEOM_Object theShape, out double Ox, out double Oy, out double Oz, out double Zx, out double Zy, out double Zz, out double Xx, out double Xy, out double Xz)
```

Get position (LCS) of theShape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to calculate position of. |
    | Ox,Oy,Oz | Output. Coordinates of shape's location origin. Origin of the LCS is situated at the shape's center of mass. |
    | Zx,Zy,Zz | Output. Coordinates of shape's location normal(main) direction. |
    | Xx,Xy,Xz | Output. Coordinates of shape's location X direction. Axes of the LCS are obtained from shape's location or, if the shape is a planar face, from position of its plane. |

Returns
:   Returns position of the shape through the last nine arguments.

### GetBasicProperties()

```python
void GetBasicProperties(in GEOM_Object theShape, in double theTolerance, out double theLength, out double theSurfArea, out double theVolume)
```

Get summarized length of all wires, area of surface and volume of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to define properties of. |
    | theTolerance | maximal relative error of area and volume computation. |
    | theLength | Output. Summarized length of all wires of the given shape. |
    | theSurfArea | Output. Area of surface of the given shape. |
    | theVolume | Output. Volume of the given shape. |

Returns
:   Returns shape properties through the last three arguments.

### GetCentreOfMass()

```python
GEOM_Object GetCentreOfMass(in GEOM_Object theShape)
```

Get a point, situated at the centre of mass of theShape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to define centre of mass of. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created point.

### GetVertexByIndex()

```python
GEOM_Object GetVertexByIndex(in GEOM_Object theShape, in long theIndex, in boolean theUseOri)
```

### GetNormal()

```python
GEOM_Object GetNormal(in GEOM_Object theFace, in GEOM_Object theOptionalPoint)
```

Get a vector, representing the normal of theFace. If the face is not planar, theOptionalPoint is obligatory.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | Shape (face) to define the normal of. |
    | theOptionalPoint | Shape (point) to define the normal at. Can be NULL in case of planar face. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created normal vector.

### GetInertia()

```python
void GetInertia(in GEOM_Object theShape, out double I11, out double I12, out double I13, out double I21, out double I22, out double I23, out double I31, out double I32, out double I33, out double Ix, out double Iy, out double Iz)
```

Get inertia matrix and moments of inertia of theShape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to calculate inertia of. |
    | I11,I12,I13,I21,I22,I23,I31,I32,I33 | Output. Components of the inertia matrix of the given shape. |
    | Ix,Iy,Iz | Output. Moments of inertia of the given shape. |

Returns
:   Returns inertia through the last twelve arguments.

### GetBoundingBox()

```python
void GetBoundingBox(in GEOM_Object theShape, in boolean precise, out double Xmin, out double Xmax, out double Ymin, out double Ymax, out double Zmin, out double Zmax)
```

Get parameters of bounding box of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to obtain bounding box of. |
    | precise | TRUE for precise computation; FALSE for fast one. |
    | Xmin,Xmax | Output. Limits of shape along OX axis. |
    | Ymin,Ymax | Output. Limits of shape along OY axis. |
    | Zmin,Zmax | Output. Limits of shape along OZ axis. |

Returns
:   Returns parameters of bounding box through the last six arguments.

### MakeBoundingBox()

```python
GEOM_Object MakeBoundingBox(in GEOM_Object theShape, in boolean precise)
```

Get bounding box of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to obtain bounding box of. |
    | precise | TRUE for precise computation; FALSE for fast one. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created bounding box.

### GetTolerance()

```python
void GetTolerance(in GEOM_Object theShape, out double FaceMin, out double FaceMax, out double EdgeMin, out double EdgeMax, out double VertMin, out double VertMax)
```

Get min and max tolerances of sub-shapes of theShape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to get tolerances of. |
    | FaceMin,FaceMax | Output. Min and max tolerances of the faces. |
    | EdgeMin,EdgeMax | Output. Min and max tolerances of the edges. |
    | VertMin,VertMax | Output. Min and max tolerances of the vertices. |

Returns
:   Returns shape tolerances through the last six arguments.

### CheckShape()

```python
boolean CheckShape(in GEOM_Object theShape, out ShapeErrors theErrors)
```

Check a topology of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to check validity of. |
    | theErrors | Structure, containing discovered errors and incriminated sub-shapes. |

Returns
:   TRUE, if the shape "seems to be valid" from the topological point of view.

### CheckShapeWithGeometry()

```python
boolean CheckShapeWithGeometry(in GEOM_Object theShape, out ShapeErrors theErrors)
```

Check a topology and a geometry of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to check validity of. |
    | theErrors | Structure, containing discovered errors and incriminated sub-shapes. |

Returns
:   TRUE, if the shape "seems to be valid".

### CheckShapeOpts()

```python
boolean CheckShapeOpts(in GEOM_Object theShape, in boolean theWithGeometry, in boolean theExact, out ShapeErrors theErrors)
```

Check a topology and a geometry of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to check validity of. |
    | theWithGeometry | If true, check also shape's geometry. |
    | theExact | If true, take into account exact tolerance of edges. It can take more time. Exact tolerance can be greater than the approximate one, which is calculated only in some points of edge. |
    | theErrors | Structure, containing discovered errors and incriminated sub-shapes. |

Returns
:   TRUE, if the shape "seems to be valid".

### PrintShapeErrors()

```python
string PrintShapeErrors(in GEOM_Object theShape, in ShapeErrors theErrors)
```

Convert sequence of shape errors, returned by *[CheckShape()](interfaceGEOM_1_1GEOM__IMeasureOperations.md#aa5a0d961603ca19cc518fbeefd8f3841)* or *[CheckShapeWithGeometry()](interfaceGEOM_1_1GEOM__IMeasureOperations.md#ad97eb40cd339b6c9592ded2e1fbcc255)*, into string.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | the invalid shape. |
    | theErrors | The sequence of *theShape* errors. |

Returns
:   String, describing all the errors in form, suitable for printing.

### ExtractBOPFailure()

```python
boolean ExtractBOPFailure(in ListOfGO theShapes, in boolean theUseTimer, in boolean theTopoOnly, in boolean theRunParallel, in boolean theDoExact, out GEOM_Object theResultShape, out ShapeErrors theErrors)
```

Extract and identify any problem in the source shapes used in a Boolean Operation.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Shapes being used in the Boolean Operation |
    | theUseTimer | Whether to chronometrize computation time |
    | theTopoOnly | Whether to check topology only |
    | theRunParallel | Whether to run the computations in parallel |
    | theDoExact | Whether to perform exact checking |
    | theResultShape | Output parameter. The result of BOP General Fuse. Indices of its sub-shapes are reported in theErrors structure. |
    | theErrors | Output parameter. Structure, containing discovered errors and incriminated sub-shapes. |

Returns
:   TRUE, if the input shapes "seem to be valid" for BOP.

### CheckSelfIntersections()

```python
boolean CheckSelfIntersections(in GEOM_Object theShape, in long theCheckLevel, out ListOfLong theIntersections)
```

Check a topology of the given shape on self-intersections presence.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to check validity of. |
    | theCheckLevel | the level of self-interference check. |
    | theIntersections | Output. List of intersected sub-shapes IDs, it contains pairs of IDs. |

Returns
:   TRUE, if the shape does not have any self-intersections.

### CheckSelfIntersectionsFast()

```python
boolean CheckSelfIntersectionsFast(in GEOM_Object theShape, in float theDeflection, in double theTolerance, out ListOfLong theIntersections)
```

Detect self-intersections of the given shape with algorithm based on mesh intersections.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to check validity of. |
    | theDeflection | Linear deflection coefficient that specifies quality of tessellation. |
    | theTolerance | Specifies a distance between sub-shapes used for detecting gaps:  - if *theTolerance* <= 0, algorithm detects intersections - if *theTolerance* > 0, algorithm detects gaps |
    | theIntersections | Output. List of intersected sub-shapes IDs, it contains pairs of IDs. |

Returns
:   TRUE, if the shape does not have any self-intersections.

### CheckBOPArguments()

```python
boolean CheckBOPArguments(in GEOM_Object theShape)
```

Check boolean and partition operations arguments.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | the argument of an operation to be checked. |

Returns
:   TRUE if the argument is valid for a boolean or partition operation; FALSE otherwise.

### FastIntersect()

```python
boolean FastIntersect(in GEOM_Object theShape1, in GEOM_Object theShape2, in double theTolerance, in float theDeflection, out ListOfLong theIntersections1, out ListOfLong theIntersections2)
```

Detect intersections of the given shapes with algorithm based on mesh intersections.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1 | First source object |
    | theShape2 | Second source object |
    | theTolerance | Specifies a distance between shapes used for detecting gaps:  - if *theTolerance* <= 0, algorithm detects intersections - if *theTolerance* > 0, algorithm detects gaps |
    | theDeflection | Linear deflection coefficient that specifies quality of tessellation:  - if *theDeflection* <= 0, default deflection 0.001 is used |
    | theIntersections1 | Output: contains list of sub-shapes IDs from 1st shape that localize intersection |
    | theIntersections2 | Output: contains list of sub-shapes IDs from 2nd shape that localize intersection |

Returns
:   TRUE, if the are intersections (gaps) between source shapes

### IsGoodForSolid()

```python
string IsGoodForSolid(in GEOM_Object theShape)
```

Check if the given shape can be an argument for MakeSolid operation.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be described. |

Returns
:   Empty string if a solid can be made on this shape, error code otherwise.

### WhatIs()

```python
string WhatIs(in GEOM_Object theShape)
```

btain description of the given shape

O

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be described. |

Returns
:   Description of the given shape.

### AreCoordsInside()

```python
ListOfBool AreCoordsInside(in GEOM_Object theShape, in ListOfDouble coords, in double tolerance)
```

Check if points defined by coords = [x1, y1, z1, x2, y2, z2, ...] are inside or on the shape theShape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to check. |
    | coords | list of coordinates. |
    | tolerance | tolerance. |

Returns
:   list of boolean.

### GetMinDistance()

```python
double GetMinDistance(in GEOM_Object theShape1, in GEOM_Object theShape2, out double X1, out double Y1, out double Z1, out double X2, out double Y2, out double Z2)
```

Get minimal distance between the given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1,theShape2 | Shapes to find minimal distance between. |
    | X1,Y1,Z1 | Output. Coordinates of point on theShape1, nearest to theShape2. |
    | X2,Y2,Z2 | Output. Coordinates of point on theShape2, nearest to theShape1. |

Returns
:   Value of the minimal distance between the given shapes.

### ClosestPoints()

```python
long ClosestPoints(in GEOM_Object theShape1, in GEOM_Object theShape2, out ListOfDouble theCoords)
```

Get closest points of the given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1,theShape2 | Shapes to find closest points of. |
    | theCoords | Output. List of (X, Y, Z) coordinates for all couples of points. |

Returns
:   The number of found solutions (-1 in case of infinite number of solutions).

### GetAngle()

```python
double GetAngle(in GEOM_Object theShape1, in GEOM_Object theShape2)
```

Get angle between the given lines or linear edges.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1,theShape2 | Shapes to find angle between. Lines or linear edges. |

Returns
:   Value of the angle between the given shapes.

### GetAngleBtwVectors()

```python
double GetAngleBtwVectors(in GEOM_Object theShape1, in GEOM_Object theShape2)
```

Get angle between the given vectors.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1,theShape2 | Vectors to find angle between. |

Returns
:   Value of the angle between the given vectors.

### PatchFace()

```python
ListOfGO PatchFace(in GEOM_Object theShape)
```

The function takes a single face with holes and returns a list of faces, first of them is the original face without holes, and the other faces are placed on the same surface as the original face but bounded by each hole wire. If the original face has no holes, it will be returned as an output.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | face, to perform operation. |

Returns
:   ListOfGO, containing the result original face and faces from holes.

### PointCoordinates()

```python
void PointCoordinates(in GEOM_Object theShape, out double X, out double Y, out double Z)
```

Get point coordinates.

### CurveCurvatureByParam()

```python
double CurveCurvatureByParam(in GEOM_Object theShape, in double theParam)
```

Get radius of curvature of curve in the point determinated by param.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | - curve. |
    | theParam | - parameter on curve |

Returns
:   Value of curvature.

### CurveCurvatureByPoint()

```python
double CurveCurvatureByPoint(in GEOM_Object theShape, in GEOM_Object thePoint)
```

Get radius of curvature of curve in the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | - curve. |
    | thePoint | - point |

Returns
:   Value of curvature.

### MaxSurfaceCurvatureByParam()

```python
double MaxSurfaceCurvatureByParam(in GEOM_Object theShape, in double theUParam, in double theVParam)
```

Get max radius of curvature of surface in the point determinated by params.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | - surface. |
    | theUParam | - U-parameter on surface |
    | theVParam | - V-parameter on surface |

Returns
:   Value of curvature.

### MaxSurfaceCurvatureByPoint()

```python
double MaxSurfaceCurvatureByPoint(in GEOM_Object theShape, in GEOM_Object thePoint)
```

Get max radius of curvature of surface in the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | - surface. |
    | thePoint | - point |

Returns
:   Value of curvature.

### MinSurfaceCurvatureByParam()

```python
double MinSurfaceCurvatureByParam(in GEOM_Object theShape, in double theUParam, in double theVParam)
```

Get min radius of curvature of surface in the point determinated by params.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | - surface. |
    | theUParam | - U-parameter on surface |
    | theVParam | - V-parameter on surface |

Returns
:   Value of curvature.

### MinSurfaceCurvatureByPoint()

```python
double MinSurfaceCurvatureByPoint(in GEOM_Object theShape, in GEOM_Object thePoint)
```

Get min radius of curvature of surface in the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | - surface. |
    | thePoint | - point |

Returns
:   Value of curvature.

### SurfaceCurvatureByPointAndDirection()

```python
GEOM_Object SurfaceCurvatureByPointAndDirection(in GEOM_Object theShape, in GEOM_Object thePoint, in GEOM_Object theDirection)
```

Get vector of curvature of surface in the given point along the given direction.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | - face. |
    | thePoint | - point. |
    | theDirection | - direction. |

Note
:   Before the calculation of curvature, the point and the direction are projected to the face, if the point does not lay on it or the direction is not tangent to it initially.

Returns
:   Vector of curvature. The returned vector is codirectional with the normal to the face in the given point in case of positive curvature value and opposite to the normal in case of negative curvature. The normal of the returned vector is equal to the absolute value of the curvature.

### XYZtoUV()

```python
ListOfDouble XYZtoUV(in GEOM_Object theSurf, in ListOfDouble theXYZlist, in boolean theIsNormalized)
```

Convert X,Y,Z points coordinates to UV parameters on the given surface.

Parameters
:   |  |  |
    | --- | --- |
    | theSurf | the given face. It can be also a shell or a compound with one face. |
    | theXYZlist | float list of size 3*N where N is the number of points for which we want their U,V coordinates. If the user enters a list of size not divisible by 3 an exception will be thrown. |
    | theIsNormalized | if True, the returned parameters will be in range [0, 1]. |

Returns
:   list of float of size 2*N.

### UVtoXYZ()

```python
ListOfDouble UVtoXYZ(in GEOM_Object theSurf, in ListOfDouble theUVlist, in boolean theIsNormalized)
```

Convert UV parameters on the given surface to 3D points coordinates.

Parameters
:   |  |  |
    | --- | --- |
    | theSurf | the given face. It can be also a shell or a compound with one face. |
    | theUVlist | float list of size 2*N where N is the number of points for which we want their X,Y,Z coordinates. If the user enters a list of non-even size an exception will be thrown. |
    | theIsNormalized | if True, the input parameters are expected to be in range [0, 1]. |

Returns
:   list of float of size 3*N.

### CheckConformityShape()

```python
CheckResults CheckConformityShape(in GEOM_Object theShape)
```

Perform analyse of shape and return all failed checks.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape for check. |

### SelfIntersected2D()

```python
SequenceOfPairOfShape SelfIntersected2D(in CheckResults theResults)
```

Find all self-intersected 2D curves.

Parameters
:   |  |  |
    | --- | --- |
    | theResults | result of check - list of failed checks and sub-shapes. |

### InterferingSubshapes()

```python
SequenceOfPairOfShape InterferingSubshapes(in CheckResults theResults, in long theShapeType1, in long theShapeType2)
```

Find pairs of interfering sub-shapes, by default all pairs of interfering shapes are returned. Avaliable types:

- vertices touched by tolerance;
- vertex touching an edge in the inner point;
- vertex lying on the inner point of a face;
- edges intersecting by inner points;
- edge touching/intersecting face in the inner point;
- faces intersection by inner point

Parameters
:   |  |  |
    | --- | --- |
    | theResults | result of check - list of failed checks and sub-shapes. |
    | theShapeType1 | Type of shape. |
    | theShapeType2 | Type of shape. |

### SmallEdges()

```python
ListOfGO SmallEdges(in CheckResults theResults)
```

Find edges, which are fully covered by tolerances of vertices.

Parameters
:   |  |  |
    | --- | --- |
    | theResults | result of check - list of failed checks and sub-shapes. |

### DistantShapes()

```python
SequenceOfPairOfShape DistantShapes(in CheckResults theResults, in long theShapeType, in long theSubShapeType, in double theTolerance)
```

find remote objects (sub-shape on a shape). Avaliable types:

- vertex far from edge;
- vertex far from face;
- edge far from face

Parameters
:   |  |  |
    | --- | --- |
    | theResults | result of check - list of failed checks and sub-shapes. |
    | theShapeType | Type of shape. |
    | theSubShapeType | Type of sub-shape. |
    | theTolerance | tolerance, by default used tolerance of sub-shape. |

### UpdateTolerance()

```python
double UpdateTolerance(in GEOM_Object theShape)
```

Compute possible tolerance for the shape, minimize tolerance of shape as well as tolerance of sub-shapes as much as possible.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape for update. |

### ShapeProximityCalculator()

```python
GEOM_Object ShapeProximityCalculator(in GEOM_Object theShape1, in GEOM_Object theShape2)
```

Get the calculator for the proximity value between the given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1,theShape2 | Shapes to find proximity. |

Returns
:   The calculator object.

### SetShapeSampling()

```python
void SetShapeSampling(in GEOM_Object theCalculator, in GEOM_Object theShape, in long theNbSamples)
```

Set number sample points to compute the coarse proximity.

Parameters
:   |  |  |
    | --- | --- |
    | theCalculator | Proximity calculator. |
    | theShape | Shape to be samples. |
    | theNbSamples | Number of samples points. |

### GetCoarseProximity()

```python
double GetCoarseProximity(in GEOM_Object theCalculator)
```

Compute coarse value of the proximity basing on the polygonal representation of shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theCalculator | Proximity calculator. |

Returns
:   Proximity value.

### GetPreciseProximity()

```python
double GetPreciseProximity(in GEOM_Object theCalculator)
```

Compute precise value of the proximity basing on the exact shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theCalculator | Proximity calculator. |

Returns
:   Proximity value.

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
