<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l3__transform.html -->

# Transformation Operations geomBuilder Python module » All package methods, grouped by their purpose » Transforming geometrical objects

## Detailed Description

## Function Documentation

### TranslateTwoPoints()

```python
def TranslateTwoPoints(self, theObject, thePoint1, thePoint2, theCopy = False)
```

Translate the given object along the vector, specified by its end points.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | thePoint1 | Start point of translation vector. |
    | thePoint2 | End point of translation vector. |
    | theCopy | Flag used to translate object itself or create a copy. |

Returns
:   Translated *theObject* ([GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)) if *theCopy* flag is `False` (default) or new [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the translated object if *theCopy* flag is `True`.

### MakeTranslationTwoPoints()

```python
def MakeTranslationTwoPoints(self, theObject, thePoint1, thePoint2, theName = None)
```

Translate the given object along the vector, specified by its end points, creating its copy before the translation.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | thePoint1 | Start point of translation vector. |
    | thePoint2 | End point of translation vector. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the translated object.

[Example 1](../tui_transformation_operations_page.md#tui_translation)   
[Example 2](../tui_test_spanner_page.md#swig_MakeTranslationTwoPoints)

### TranslateDXDYDZ()

```python
def TranslateDXDYDZ(self, theObject, theDX, theDY, theDZ, theCopy = False)
```

Translate the given object along the vector, specified by its components.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | theDX,theDY,theDZ | Components of translation vector. |
    | theCopy | Flag used to translate object itself or create a copy. |

Returns
:   Translated *theObject* ([GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)) if *theCopy* flag is `False` (default) or new [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the translated object if *theCopy* flag is `True`.

[Example](../tui_transformation_operations_page.md#tui_translation)

### MakeTranslation()

```python
def MakeTranslation(self, theObject, theDX, theDY, theDZ, theName = None)
```

Translate the given object along the vector, specified by its components, creating its copy before the translation.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | theDX,theDY,theDZ | Components of translation vector. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the translated object.

[Example](../tui_transformation_operations_page.md#tui_translation)

### TranslateVector()

```python
def TranslateVector(self, theObject, theVector, theCopy = False)
```

Translate the given object along the given vector.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | theVector | The translation vector. |
    | theCopy | Flag used to translate object itself or create a copy. |

Returns
:   Translated *theObject* ([GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)) if *theCopy* flag is `False` (default) or new [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the translated object if *theCopy* flag is `True`.

### MakeTranslationVector()

```python
def MakeTranslationVector(self, theObject, theVector, theName = None)
```

Translate the given object along the given vector, creating its copy before the translation.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | theVector | The translation vector. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the translated object.

[Example](../tui_transformation_operations_page.md#tui_translation)

### TranslateVectorDistance()

```python
def TranslateVectorDistance(self, theObject, theVector, theDistance, theCopy = False)
```

Translate the given object along the given vector on given distance.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | theVector | The translation vector. |
    | theDistance | The translation distance. |
    | theCopy | Flag used to translate object itself or create a copy. |

Returns
:   Translated *theObject* ([GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)) if *theCopy* flag is `False` (default) or new [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the translated object if *theCopy* flag is `True`.

[Example](../tui_transformation_operations_page.md#tui_translation)

### MakeTranslationVectorDistance()

```python
def MakeTranslationVectorDistance(self, theObject, theVector, theDistance, theName = None)
```

Translate the given object along the given vector on given distance, creating its copy before the translation.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | theVector | The translation vector. |
    | theDistance | The translation distance. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the translated object.

[Example](../tui_transformation_operations_page.md#tui_translation)

### Rotate()

```python
def Rotate(self, theObject, theAxis, theAngle, theCopy = False)
```

Rotate the given object around the given axis on the given angle.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theAxis | Rotation axis. |
    | theAngle | Rotation angle in radians. |
    | theCopy | Flag used to rotate object itself or create a copy. |

Returns
:   Rotated *theObject* ([GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)) if *theCopy* flag is `False` (default) or new [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the rotated object if *theCopy* flag is `True`.

[Example](../tui_transformation_operations_page.md#tui_rotation)

### MakeRotation()

```python
def MakeRotation(self, theObject, theAxis, theAngle, theName = None)
```

Rotate the given object around the given axis on the given angle, creating its copy before the rotation.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theAxis | Rotation axis. |
    | theAngle | Rotation angle in radians. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the rotated object.

[Example](../tui_transformation_operations_page.md#tui_rotation)

### RotateThreePoints()

```python
def RotateThreePoints(self, theObject, theCentPoint, thePoint1, thePoint2, theCopy = False)
```

Rotate given object around vector perpendicular to plane containing three points.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theCentPoint | central point the axis is the vector perpendicular to the plane containing the three points. |
    | thePoint1,thePoint2 | points in a perpendicular plane of the axis. |
    | theCopy | Flag used to rotate object itself or create a copy. |

Returns
:   Rotated *theObject* ([GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)) if *theCopy* flag is `False` (default) or new [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the rotated object if *theCopy* flag is `True`.

### MakeRotationThreePoints()

```python
def MakeRotationThreePoints(self, theObject, theCentPoint, thePoint1, thePoint2, theName = None)
```

Rotate given object around vector perpendicular to plane containing three points, creating its copy before the rotatation.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theCentPoint | central point the axis is the vector perpendicular to the plane containing the three points. |
    | thePoint1,thePoint2 | in a perpendicular plane of the axis. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the rotated object.

[Example](../tui_transformation_operations_page.md#tui_rotation)

### Scale()

```python
def Scale(self, theObject, thePoint, theFactor, theCopy = False)
```

Scale the given object by the specified factor.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be scaled. |
    | thePoint | Center point for scaling. Passing None for it means scaling relatively the origin of global CS. |
    | theFactor | Scaling factor value. |
    | theCopy | Flag used to scale object itself or create a copy. |

Returns
:   Scaled *theObject* ([GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)) if *theCopy* flag is `False` (default) or new [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the scaled object if *theCopy* flag is `True`.

### MakeScaleTransform()

```python
def MakeScaleTransform(self, theObject, thePoint, theFactor, theName = None)
```

Scale the given object by the factor, creating its copy before the scaling.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be scaled. |
    | thePoint | Center point for scaling. Passing None for it means scaling relatively the origin of global CS. |
    | theFactor | Scaling factor value. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the scaled shape.

[Example](../tui_transformation_operations_page.md#tui_scale)

### ScaleAlongAxes()

```python
def ScaleAlongAxes(self, theObject, thePoint, theFactorX, theFactorY, theFactorZ, theCopy = False)
```

Scale the given object by different factors along coordinate axes.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be scaled. |
    | thePoint | Center point for scaling. Passing None for it means scaling relatively the origin of global CS. |
    | theFactorX,theFactorY,theFactorZ | Scaling factors along each axis. |
    | theCopy | Flag used to scale object itself or create a copy. |

Returns
:   Scaled *theObject* ([GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)) if *theCopy* flag is `False` (default) or new [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the scaled object if *theCopy* flag is `True`.

### MakeScaleAlongAxes()

```python
def MakeScaleAlongAxes(self, theObject, thePoint, theFactorX, theFactorY, theFactorZ, theName = None)
```

Scale the given object by different factors along coordinate axes, creating its copy before the scaling.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be scaled. |
    | thePoint | Center point for scaling. Passing None for it means scaling relatively the origin of global CS. |
    | theFactorX,theFactorY,theFactorZ | Scaling factors along each axis. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the scaled shape.

[Example](../tui_test_all_page.md#swig_scale)

### MirrorByPlane()

```python
def MirrorByPlane(self, theObject, thePlane, theCopy = False)
```

Mirror an object relatively the given plane.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be mirrored. |
    | thePlane | Plane of symmetry. |
    | theCopy | Flag used to mirror object itself or create a copy. |

Returns
:   Mirrored *theObject* ([GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)) if *theCopy* flag is `False` (default) or new [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the mirrored object if *theCopy* flag is `True`.

### MakeMirrorByPlane()

```python
def MakeMirrorByPlane(self, theObject, thePlane, theName = None)
```

Create an object, symmetrical to the given one relatively the given plane.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be mirrored. |
    | thePlane | Plane of symmetry. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the mirrored shape.

[Example](../tui_transformation_operations_page.md#tui_mirror)

### MirrorByAxis()

```python
def MirrorByAxis(self, theObject, theAxis, theCopy = False)
```

Mirror an object relatively the given axis.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be mirrored. |
    | theAxis | Axis of symmetry. |
    | theCopy | Flag used to mirror object itself or create a copy. |

Returns
:   Mirrored *theObject* ([GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)) if *theCopy* flag is `False` (default) or new [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the mirrored object if *theCopy* flag is `True`.

### MakeMirrorByAxis()

```python
def MakeMirrorByAxis(self, theObject, theAxis, theName = None)
```

Create an object, symmetrical to the given one relatively the given axis.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be mirrored. |
    | theAxis | Axis of symmetry. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the mirrored shape.

[Example](../tui_transformation_operations_page.md#tui_mirror)

### MirrorByPoint()

```python
def MirrorByPoint(self, theObject, thePoint, theCopy = False)
```

Mirror an object relatively the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be mirrored. |
    | thePoint | Point of symmetry. |
    | theCopy | Flag used to mirror object itself or create a copy. |

Returns
:   Mirrored *theObject* ([GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)) if *theCopy* flag is `False` (default) or new [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the mirrored object if *theCopy* flag is `True`.

### MakeMirrorByPoint()

```python
def MakeMirrorByPoint(self, theObject, thePoint, theName = None)
```

Create an object, symmetrical to the given one relatively the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be mirrored. |
    | thePoint | Point of symmetry. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the mirrored shape.

[Example](../tui_transformation_operations_page.md#tui_mirror)

### Position()

```python
def Position(self, theObject, theStartLCS, theEndLCS, theCopy = False)
```

Modify the location of the given object.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be displaced. |
    | theStartLCS | Coordinate system to perform displacement from it.  If *theStartLCS* is NULL, displacement will be performed from global CS.  If *theObject* itself is used as *theStartLCS*, its location will be changed to *theEndLCS*. |
    | theEndLCS | Coordinate system to perform displacement to it. |
    | theCopy | Flag used to displace object itself or create a copy. |

Returns
:   Displaced *theObject* ([GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)) if *theCopy* flag is `False` (default) or new [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the displaced object if *theCopy* flag is `True`.

### MakePosition()

```python
def MakePosition(self, theObject, theStartLCS, theEndLCS, theName = None)
```

Modify the Location of the given object by LCS, creating its copy before the setting.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be displaced. |
    | theStartLCS | Coordinate system to perform displacement from it.  If *theStartLCS* is NULL, displacement will be performed from global CS.  If *theObject* itself is used as *theStartLCS*, its location will be changed to *theEndLCS*. |
    | theEndLCS | Coordinate system to perform displacement to it. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the displaced shape.

[Example](../tui_transformation_operations_page.md#tui_modify_location)

### PositionAlongPath()

```python
def PositionAlongPath(self, theObject, thePath, theDistance, theCopy, theReverse)
```

Modify the Location of the given object by Path.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be displaced. |
    | thePath | Wire or Edge along that the object will be translated. |
    | theDistance | progress of Path (0 = start location, 1 = end of path location). |
    | theCopy | is to create a copy objects if true. |
    | theReverse | 0 - for usual direction, 1 - to reverse path direction. |

Returns
:   Displaced *theObject* ([GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)) if *theCopy* is `False` or new [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the displaced shape if *theCopy* is `True`.

[Example](../tui_transformation_operations_page.md#tui_modify_location)

### MakePositionAlongPath()

```python
def MakePositionAlongPath(self, theObject, thePath, theDistance, theReverse, theName = None)
```

Modify the Location of the given object by Path, creating its copy before the operation.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be displaced. |
    | thePath | Wire or Edge along that the object will be translated. |
    | theDistance | progress of Path (0 = start location, 1 = end of path location). |
    | theReverse | 0 - for usual direction, 1 - to reverse path direction. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the displaced shape.

### Offset()

```python
def Offset(self, theObject, theOffset, theCopy = False)
```

Offset given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The base object for the offset. |
    | theOffset | Offset value. |
    | theCopy | Flag used to offset object itself or create a copy. |

Returns
:   Modified *theObject* ([GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)) if *theCopy* flag is `False` (default) or new [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result of offset operation if *theCopy* flag is `True`.

### MakeOffset()

```python
def MakeOffset(self, theObject, theOffset, theName = None)
```

Create new object as offset of the given one.

Gap between two adjacent offset surfaces is filled by a pipe.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The base object for the offset. |
    | theOffset | Offset value. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the offset object.

See also
:   [MakeOffsetIntersectionJoin](group__l3__transform.md#gae7f3c32a7e1926d4229c3196b6318c73) [Example](../tui_transformation_operations_page.md#tui_offset)

### MakeOffsetIntersectionJoin()

```python
def MakeOffsetIntersectionJoin(self, theObject, theOffset, theName = None)
```

Create new object as offset of the given one.

Gap between adjacent offset surfaces is filled by extending and intersecting them.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The base object for the offset. |
    | theOffset | Offset value. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the offset object.

See also
:   [MakeOffset](group__l3__transform.md#ga8817771054c22d85e74d910ba1e330db) [Example](../tui_transformation_operations_page.md#tui_offset)

### MakeOffsetPartial()

```python
def MakeOffsetPartial(self, theObject, theOffset, theFacesIDs, theName = None)
```

Create new object as partial offset of the given one.

Only indexed faces are offset, others keep they original location. Gap between adjacent offset surfaces is filled by extending and intersecting them.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The base object for the offset. |
    | theOffset | Offset value. |
    | theFacesIDs | The list of face IDs indicating faces to be offset. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the offset object.

[Example](../tui_transformation_operations_page.md#tui_offset)

### MakeProjection()

```python
def MakeProjection(self, theSource, theTarget, theName = None)
```

Create new object as projection of the given one on another.

Parameters
:   |  |  |
    | --- | --- |
    | theSource | The source object for the projection. It can be a point, edge or wire. Edge and wire are acceptable if *theTarget* is a face. |
    | theTarget | The target object. It can be planar or cylindrical face, edge or wire. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the projection.

[Example](../tui_transformation_operations_page.md#tui_projection)

### MakeProjectionOnWire()

```python
def MakeProjectionOnWire(self, thePoint, theWire, theName = None)
```

Create a projection of the given point on a wire or an edge.

If there are no solutions or there are 2 or more solutions It throws an exception.

Parameters
:   |  |  |
    | --- | --- |
    | thePoint | the point to be projected. |
    | theWire | the wire. The edge is accepted as well. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   [*u*, *PointOnEdge*, *EdgeInWireIndex*]   
    *u:* The parameter of projection point on edge.   
    *PointOnEdge:* The projection point.   
    *EdgeInWireIndex:* The index of an edge in a wire.

[Example](../tui_transformation_operations_page.md#tui_projection)

### MakeMultiTranslation1D()

```python
def MakeMultiTranslation1D(self, theObject, theVector, theStep, theNbTimes, theName = None)
```

Translate the given object along the given vector a given number times.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be translated. |
    | theVector | Direction of the translation. DX if None. |
    | theStep | Distance to translate on. |
    | theNbTimes | Quantity of translations to be done. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing compound of all the shapes, obtained after each translation.

[Example](../tui_transformation_operations_page.md#tui_multi_translation)

### MakeMultiTranslation2D()

```python
def MakeMultiTranslation2D(self, theObject, theVector1, theStep1, theNbTimes1, theVector2, theStep2, theNbTimes2, theName = None)
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
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing compound of all the shapes, obtained after each translation.

[Example](../tui_transformation_operations_page.md#tui_multi_translation)

### MultiRotate1DNbTimes()

```python
def MultiRotate1DNbTimes(self, theObject, theAxis, theNbTimes, theName = None)
```

Rotate the given object around the given axis a given number times.

Rotation angle will be 2*PI/theNbTimes.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theAxis | The rotation axis. DZ if None. |
    | theNbTimes | Quantity of rotations to be done. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing compound of all the shapes, obtained after each rotation.

[Example](../tui_transformation_operations_page.md#tui_multi_rotation)

### MultiRotate1DByStep()

```python
def MultiRotate1DByStep(self, theObject, theAxis, theAngleStep, theNbTimes, theName = None)
```

Rotate the given object around the given axis a given number times on the given angle.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theAxis | The rotation axis. DZ if None. |
    | theAngleStep | Rotation angle in radians. |
    | theNbTimes | Quantity of rotations to be done. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing compound of all the shapes, obtained after each rotation.

[Example](../tui_transformation_operations_page.md#tui_multi_rotation)

### MultiRotate2DNbTimes()

```python
def MultiRotate2DNbTimes(self, theObject, theAxis, theNbTimes1, theRadialStep, theNbTimes2, theName = None)
```

Rotate the given object around the given axis a given number times and multi-translate each rotation result.

Rotation angle will be 2*PI/theNbTimes1. Translation direction passes through center of gravity of rotated shape and its projection on the rotation axis.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theAxis | Rotation axis. DZ if None. |
    | theNbTimes1 | Quantity of rotations to be done. |
    | theRadialStep | Translation distance. |
    | theNbTimes2 | Quantity of translations to be done. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing compound of all the shapes, obtained after each transformation.

[Example](../tui_transformation_operations_page.md#tui_multi_rotation)

### MultiRotate2DByStep()

```python
def MultiRotate2DByStep(self, theObject, theAxis, theAngleStep, theNbTimes1, theRadialStep, theNbTimes2, theName = None)
```

Rotate the given object around the given axis on the given angle a given number times and multi-translate each rotation result.

Translation direction passes through center of gravity of rotated shape and its projection on the rotation axis.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be rotated. |
    | theAxis | Rotation axis. DZ if None. |
    | theAngleStep | Rotation angle in radians. |
    | theNbTimes1 | Quantity of rotations to be done. |
    | theRadialStep | Translation distance. |
    | theNbTimes2 | Quantity of translations to be done. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing compound of all the shapes, obtained after each transformation.

[Example](../tui_transformation_operations_page.md#tui_multi_rotation)

### MakeMultiRotation1DNbTimes()

```python
def MakeMultiRotation1DNbTimes(self, aShape, aDir, aPoint, aNbTimes, theName = None)
```

The same, as [MultiRotate1DNbTimes()](group__l3__transform.md#ga5dd61e4b7dd05412cce7815629629c56), but axis is given by direction and point.

[Example](../tui_test_others_page.md#swig_MakeMultiRotation)

### MakeMultiRotation1DByStep()

```python
def MakeMultiRotation1DByStep(self, aShape, aDir, aPoint, anAngle, aNbTimes, theName = None)
```

The same, as [MultiRotate1DByStep()](group__l3__transform.md#gaabc28cf1e4f2dc55a9bd273c3e9acb34), but axis is given by direction and point.

[Example](../tui_test_others_page.md#swig_MakeMultiRotation)

### MakeMultiRotation2DNbTimes()

```python
def MakeMultiRotation2DNbTimes(self, aShape, aDir, aPoint, nbtimes1, aStep, nbtimes2, theName = None)
```

The same, as [MultiRotate2DNbTimes()](group__l3__transform.md#ga5a0929047e92675f9b89756eb223fab5), but axis is given by direction and point.

[Example](../tui_test_others_page.md#swig_MakeMultiRotation)

### MakeMultiRotation2DByStep()

```python
def MakeMultiRotation2DByStep(self, aShape, aDir, aPoint, anAngle, nbtimes1, aStep, nbtimes2, theName = None)
```

The same, as [MultiRotate2DByStep()](group__l3__transform.md#gaeb16678a6ec2aaa88013f1281f02bfb9), but axis is given by direction and point.

[Example](../tui_test_others_page.md#swig_MakeMultiRotation)

### MakeProjectionOnCylinder()

```python
def MakeProjectionOnCylinder(self, theObject, theRadius, theStartAngle = 0.0, theAngleLength = -1.0, theAngleRotation = 0.0, theName = None)
```

Compute a wire or a face that represents a projection of the source shape onto cylinder.

The cylinder's coordinate system is the same as the global coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object to be projected. It can be either a planar wire or a face. |
    | theRadius | The radius of the cylinder. |
    | theStartAngle | The starting angle in radians from the cylinder's X axis around Z axis. The angle from which the projection is started. |
    | theAngleLength | The projection length angle in radians. The angle in which to project the total length of the wire. If it is negative the projection is not scaled and natural wire length is kept for the projection. |
    | theAngleRotation | The desired angle in radians between the tangent vector to the first curve at the first point of the theObject's projection in 2D space and U-direction of cylinder's 2D space. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape. The result represents a wire or a face that represents a projection of the source shape onto a cylinder.

[Example](../tui_transformation_operations_page.md#tui_projection)
