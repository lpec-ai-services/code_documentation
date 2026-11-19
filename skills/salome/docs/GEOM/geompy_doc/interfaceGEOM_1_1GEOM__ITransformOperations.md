<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__ITransformOperations.html -->

# GEOM_ITransformOperations Interface Reference

Interface for shapes transforming.
[More...](interfaceGEOM_1_1GEOM__ITransformOperations.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for shapes transforming.

Translation, rotation, scaling, mirroring, offset, projection, recomputing.

## Member Function Documentation

### TranslateTwoPoints()

```python
GEOM_Object TranslateTwoPoints(in GEOM_Object theObject, in GEOM_Object thePoint1, in GEOM_Object thePoint2)
```

Translate the given object along the vector, specified by its end points.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | thePoint1 | Start point of translation vector. |
    | thePoint2 | End point of translation vector. |

Returns
:   theObject.

### TranslateTwoPointsCopy()

```python
GEOM_Object TranslateTwoPointsCopy(in GEOM_Object theObject, in GEOM_Object thePoint1, in GEOM_Object thePoint2)
```

Translate the given object along the vector, specified by its end points, creating its copy before the translation.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | thePoint1 | Start point of translation vector. |
    | thePoint2 | End point of translation vector. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the translated object.

### TranslateDXDYDZ()

```python
GEOM_Object TranslateDXDYDZ(in GEOM_Object theObject, in double theDX, in double theDY, in double theDZ)
```

Translate the given object along the vector, specified by its components.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | theDX,theDY,theDZ | Components of translation vector. |

Returns
:   theObject.

### TranslateDXDYDZCopy()

```python
GEOM_Object TranslateDXDYDZCopy(in GEOM_Object theObject, in double theDX, in double theDY, in double theDZ)
```

Translate the given object along the vector, specified by its components, creating its copy before the translation.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | theDX,theDY,theDZ | Components of translation vector. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the translated object.

### TranslateVector()

```python
GEOM_Object TranslateVector(in GEOM_Object theObject, in GEOM_Object theVector)
```

Translate the given object along the given vector.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | theVector | Translation vector, giving both direction and distance. |

Returns
:   theObject.

### TranslateVectorCopy()

```python
GEOM_Object TranslateVectorCopy(in GEOM_Object theObject, in GEOM_Object theVector)
```

Translate the given object along the given vector, creating its copy before the translation.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | theVector | Translation vector, giving both direction and distance. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the translated object.

### TranslateVectorDistance()

```python
GEOM_Object TranslateVectorDistance(in GEOM_Object theObject, in GEOM_Object theVector, in double theDistance, in boolean theCopy)
```

Translate the given object along the given vector on given distance, creating its copy before the translation.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | theVector | Translation vector, giving a direction. |
    | theDistance | Translation distance, giving a distance. |
    | theCopy | Translation copy, creating its copy if true. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the translated object.

### MultiTranslate1D()

```python
GEOM_Object MultiTranslate1D(in GEOM_Object theObject, in GEOM_Object theVector, in double theStep, in long theNbTimes)
```

Translate the given object along the given vector a given number times.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | theVector | Direction of the translation. DX if None. |
    | theStep | Distance to translate on. |
    | theNbTimes | Quantity of translations to be done. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing compound of all the shapes, obtained after each translation.

### MultiTranslate2D()

```python
GEOM_Object MultiTranslate2D(in GEOM_Object theObject, in GEOM_Object theVector1, in double theStep1, in long theNbTimes1, in GEOM_Object theVector2, in double theStep2, in long theNbTimes2)
```

Conseqently apply two specified translations to theObject specified number of times.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | theVector1 | Direction of the first translation. DX if None. |
    | theStep1 | Step of the first translation. |
    | theNbTimes1 | Quantity of translations to be done along theVector1. |
    | theVector2 | Direction of the second translation. DY if None. |
    | theStep2 | Step of the second translation. |
    | theNbTimes2 | Quantity of translations to be done along theVector2. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing compound of all the shapes, obtained after each translation.

### RotateThreePoints()

```python
GEOM_Object RotateThreePoints(in GEOM_Object theObject, in GEOM_Object theCentPoint, in GEOM_Object thePoint1, in GEOM_Object thePoint2)
```

Rotate given object around vector perpendicular to plane containing three points.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theCentPoint | central point - the axis is the vector perpendicular to the plane containing the three points. |
    | thePoint1,thePoint2 | - in a perpendicular plan of the axis. |

Returns
:   theObject.

### RotateThreePointsCopy()

```python
GEOM_Object RotateThreePointsCopy(in GEOM_Object theObject, in GEOM_Object theCentPoint, in GEOM_Object thePoint1, in GEOM_Object thePoint2)
```

Rotate given object around vector perpendicular to plane containing three points.

Creating its copy before the rotatation.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theCentPoint | central point - the axis is the vector perpendicular to the plane containing the three points. |
    | thePoint1,thePoint2 | - in a perpendicular plan of the axis. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the rotated object.

### Rotate()

```python
GEOM_Object Rotate(in GEOM_Object theObject, in GEOM_Object theAxis, in double theAngle)
```

Rotate the given object around the given axis on the given angle.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theAxis | Rotation axis. |
    | theAngle | Rotation angle in radians. |

Returns
:   theObject.

### RotateCopy()

```python
GEOM_Object RotateCopy(in GEOM_Object theObject, in GEOM_Object theAxis, in double theAngle)
```

Rotate the given object around the given axis on the given angle, creating its copy before the rotatation.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theAxis | Rotation axis. |
    | theAngle | Rotation angle in radians. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the rotated object.

### MultiRotate1D()

```python
GEOM_Object MultiRotate1D(in GEOM_Object theObject, in GEOM_Object theAxis, in long theNbObjects)
```

Rotate the given object around the given axis a given number times.

Rotation angle will be 2*PI/theNbObjects.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theAxis | The rotation axis. DZ if None. |
    | theNbObjects | Quantity of rotations to be done. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing compound of all the shapes, obtained after each rotation.

### MultiRotate1DByStep()

```python
GEOM_Object MultiRotate1DByStep(in GEOM_Object theObject, in GEOM_Object theAxis, in double theAngleStep, in long theNbSteps)
```

Rotate the given object around the given axis a given number times on the given angle.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theAxis | The rotation axis. DZ if None. |
    | theAngleStep | Rotation angle in radians. |
    | theNbSteps | Quantity of rotations to be done. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing compound of all the shapes, obtained after each rotation.

### MultiRotate2DNbTimes()

```python
GEOM_Object MultiRotate2DNbTimes(in GEOM_Object theObject, in GEOM_Object theAxis, in long theNbObjects, in double theRadialStep, in long theNbSteps)
```

Rotate the given object around the given axis a given number times and multi-translate each rotation result.

Rotation angle will be 2*PI/theNbObjects. Translation direction passes through center of gravity of rotated shape and its projection on the rotation axis.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theAxis | Rotation axis. DZ if None. |
    | theNbObjects | Quantity of rotations to be done. |
    | theRadialStep | Translation distance. |
    | theNbSteps | Quantity of translations to be done. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing compound of all the shapes, obtained after each transformation.

### MultiRotate2DByStep()

```python
GEOM_Object MultiRotate2DByStep(in GEOM_Object theObject, in GEOM_Object theAxis, in double theAngleStep, in long theNbSteps1, in double theRadialStep, in long theNbSteps2)
```

Rotate the given object around the given axis on the given angle a given number times and multi-translate each rotation result.

Translation direction passes through center of gravity of rotated shape and its projection on the rotation axis.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theAxis | Rotation axis. DZ if None. |
    | theAngleStep | Rotation angle in radians. |
    | theNbSteps1 | Quantity of rotations to be done. |
    | theRadialStep | Translation distance. |
    | theNbSteps2 | Quantity of translations to be done. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing compound of all the shapes, obtained after each transformation.

### MultiRotate2D()

```python
GEOM_Object MultiRotate2D(in GEOM_Object theObject, in GEOM_Object theAxis, in double theAngleStep, in long theNbSteps1, in double theRadialStep, in long theNbSteps2)
```

Rotate the given object around the given axis on the given angle a given number times and multi-translate each rotation result.

Translation direction passes through center of gravity of rotated shape and its projection on the rotation axis.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theAxis | Rotation axis. DZ if None. |
    | theAngleStep | Rotation angle in degrees. |
    | theNbSteps1 | Quantity of rotations to be done. |
    | theRadialStep | Translation distance. |
    | theNbSteps2 | Quantity of translations to be done. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing compound of all the shapes, obtained after each transformation.

### MirrorPlane()

```python
GEOM_Object MirrorPlane(in GEOM_Object theObject, in GEOM_Object thePlane)
```

Replace the given object by an object, symmetrical to it relatively the given plane.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be mirrored. |
    | thePlane | Plane of symmetry. |

### MirrorPlaneCopy()

```python
GEOM_Object MirrorPlaneCopy(in GEOM_Object theObject, in GEOM_Object thePlane)
```

Create an object, symmetrical to the given one relatively the given plane.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be mirrored. |
    | thePlane | Plane of symmetry. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the mirrored shape.

### MirrorAxis()

```python
GEOM_Object MirrorAxis(in GEOM_Object theObject, in GEOM_Object theAxis)
```

Replace the given object by an object, symmetrical to it relatively the given axis.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be mirrored. |
    | theAxis | Axis of symmetry. |

Returns
:   theObject.

### MirrorAxisCopy()

```python
GEOM_Object MirrorAxisCopy(in GEOM_Object theObject, in GEOM_Object theAxis)
```

Create an object, symmetrical to the given one relatively the given axis.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be mirrored. |
    | theAxis | Axis of symmetry. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the mirrored object.

### MirrorPoint()

```python
GEOM_Object MirrorPoint(in GEOM_Object theObject, in GEOM_Object thePoint)
```

Replace the given object by an object, symmetrical to it relatively the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be mirrored. |
    | thePoint | Point of symmetry. |

Returns
:   theObject.

### MirrorPointCopy()

```python
GEOM_Object MirrorPointCopy(in GEOM_Object theObject, in GEOM_Object thePoint)
```

Create an object, symmetrical to the given one relatively the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be mirrored. |
    | thePoint | Point of symmetry. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the mirrored object.

### OffsetShape()

```python
GEOM_Object OffsetShape(in GEOM_Object theObject, in double theOffset, in boolean theJoinByPipes)
```

Replace the given object by its offset.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The base object for the offset. |
    | theOffset | Offset value. |
    | theJoinByPipes | To join offset surfaces by pipes or by intersection. |

Returns
:   theObject.

### OffsetShapeCopy()

```python
GEOM_Object OffsetShapeCopy(in GEOM_Object theObject, in double theOffset, in boolean theJoinByPipes)
```

Create new object as offset of the given one.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The base object for the offset. |
    | theOffset | Offset value. |
    | theJoinByPipes | To join offset surfaces by pipes or by intersection. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the offset object.

### OffsetShapePartialCopy()

```python
GEOM_Object OffsetShapePartialCopy(in GEOM_Object theObject, in double theOffset, in ListOfLong theFacesIDs)
```

Create new object as offset of the given one. Only indexed faces are offset, others keep they original location.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The base object for the offset. |
    | theOffset | Offset value. |
    | theFacesIDs | The list of face IDs indicating faces to be offset. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the offset object.

### ProjectShapeCopy()

```python
GEOM_Object ProjectShapeCopy(in GEOM_Object theSource, in GEOM_Object theTarget)
```

Create new object as projection of the given one on a 2D surface.

Parameters
:   |  |  |
    | --- | --- |
    | theSource | The source object for the projection. It can be a point, edge or wire. |
    | theTarget | The target object. It can be planar or cylindrical face. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the projection.

### ProjectPointOnWire()

```python
double ProjectPointOnWire(in GEOM_Object thePoint, in GEOM_Object theWire, out GEOM_Object thePointOnEdge, out long theEdgeInWireIndex)
```

Create a projection projection of the given point on a wire or an edge.

If there are no solutions or there are 2 or more solutions It throws an exception.

Parameters
:   |  |  |
    | --- | --- |
    | thePoint | the point to be projected. |
    | theWire | the wire. The edge is accepted as well. |
    | thePointOnEdge | the projection point. |
    | theEdgeInWireIndex | the index of an edge in a wire. |

Returns
:   the parameter of projection point on edge.

### ScaleShape()

```python
GEOM_Object ScaleShape(in GEOM_Object theObject, in GEOM_Object thePoint, in double theFactor)
```

Scale the given object by the factor.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be scaled. |
    | thePoint | Center point for scaling. |
    | theFactor | Scaling factor value. |

Returns
:   theObject.

### ScaleShapeCopy()

```python
GEOM_Object ScaleShapeCopy(in GEOM_Object theObject, in GEOM_Object thePoint, in double theFactor)
```

Scale the given object by the factor, creating its copy before the scaling.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be scaled. |
    | thePoint | Center point for scaling. |
    | theFactor | Scaling factor value. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the scaled shape.

### ScaleShapeAlongAxes()

```python
GEOM_Object ScaleShapeAlongAxes(in GEOM_Object theObject, in GEOM_Object thePoint, in double theFactorX, in double theFactorY, in double theFactorZ)
```

Scale the given object by different factors along coordinate axes.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be scaled. |
    | thePoint | Center point for scaling. |
    | theFactorX,theFactorY,theFactorZ | Scaling factors along each axis. |

Returns
:   theObject.

### ScaleShapeAlongAxesCopy()

```python
GEOM_Object ScaleShapeAlongAxesCopy(in GEOM_Object theObject, in GEOM_Object thePoint, in double theFactorX, in double theFactorY, in double theFactorZ)
```

Scale the given object by different factors along coordinate axes, creating its copy before the scaling.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be scaled. |
    | thePoint | Center point for scaling. |
    | theFactorX,theFactorY,theFactorZ | Scaling factors along each axis. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the scaled shape.

### PositionShape()

```python
GEOM_Object PositionShape(in GEOM_Object theObject, in GEOM_Object theStartLCS, in GEOM_Object theEndLCS)
```

Modify the Location of the given object by LCS.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be displaced. |
    | theStartLCS | Coordinate system to perform displacement from it. If *theStartLCS* is NULL, displacement will be performed from global CS. If *theObject* itself is used as *theStartLCS*, its location will be changed to *theEndLCS*. |
    | theEndLCS | Coordinate system to perform displacement to it. |

Returns
:   theObject.

### PositionShapeCopy()

```python
GEOM_Object PositionShapeCopy(in GEOM_Object theObject, in GEOM_Object theStartLCS, in GEOM_Object theEndLCS)
```

Modify the Location of the given object by LCS, creating its copy before the setting.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be displaced. |
    | theStartLCS | Coordinate system to perform displacement from it. If *theStartLCS* is NULL, displacement will be performed from global CS. If *theObject* itself is used as *theStartLCS*, its location will be changed to *theEndLCS*. |
    | theEndLCS | Coordinate system to perform displacement to it. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the displaced shape.

### PositionAlongPath()

```python
GEOM_Object PositionAlongPath(in GEOM_Object theObject, in GEOM_Object thePath, in double theDistance, in boolean theCopy, in boolean theReverse)
```

Modify the Location of the given object by Path,.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be displaced. |
    | thePath | Wire or Edge along that the object will be translated. |
    | theDistance | progress of Path (0 = actual location, 1 = end of path location). |
    | theCopy | is a true or false parameter. true is to create a copy, false to move the object. |
    | theReverse | is a true or false parameter. True is to reverse direction, false is to move normal direction. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the displaced shape.

### RecomputeObject()

```python
GEOM_Object RecomputeObject(in GEOM_Object theObject)
```

Recompute the shape from its arguments.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be recomputed. |

Returns
:   theObject.

### MakeProjectionOnCylinder()

```python
GEOM_Object MakeProjectionOnCylinder(in GEOM_Object theObject, in double theRadius, in double theStartAngle, in double theAngleLength, in double theAngleRotation)
```

Compute the projection of a wire or a face on a cylinder.

This method computes a wire or a face or a compound of faces that represents a projection of the source shape onto cylinder. The cylinder's coordinate system is the same as the global coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be projected. It can be either a planar wire or a face. |
    | theRadius | The radius of the cylinder. |
    | theStartAngle | The starting angle from the cylinder's X axis around Z axis. The angle from which the projection is started. |
    | theAngleLength | The projection length angle. The angle in which to project the total length of the wire. If it is negative the projection is not scaled and natural wire length is kept for the projection. |
    | theAngleRotation | the desired angle between the tangent vector to the first curve at the first point of the theObject's projection in 2D space and U-direction of cylinder's 2D space. |

Returns
:   A wire or a face or a compound of faces that represents a projection of the source shape onto a cylinder.

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
