<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classgsketcher_1_1Sketcher2D.html -->

# Sketcher2D Class Reference gsketcher - Wrapper to help the creation of simple sketches

An interface to build a 2D Sketcher step-by-step.
[More...](classgsketcher_1_1Sketcher2D.md#details)

## Detailed Description

An interface to build a 2D Sketcher step-by-step.

Use geompy.Sketcher2D() method to obtain an instance of this class.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, geompyD)
```

## Member Function Documentation

### addPoint()

```python
def addPoint(self, x, y)
```

Add one point.

Used to set the starting point

Parameters
:   |  |  |
    | --- | --- |
    | x,y | - Coordinates of point |

### addAngle()

```python
def addAngle(self, angle)
```

Add angle.

Used to set the angle for further building

Parameters
:   |  |  |
    | --- | --- |
    | angle | - angle in a plane |

### addSegmentParalX()

```python
def addSegmentParalX(self, x)
```

Add segment, which sequentially connects the previous point with a point lying on a line parallel to the axis Ox and the value x = param x.

The current point will be the previous value to the coordinate y and new value to the coordinate x. Coordinate is considered relative to the previous point.

Parameters
:   |  |  |
    | --- | --- |
    | x | - Coordinate of point on axis Ox |

### addSegmentParalXToZero()

```python
def addSegmentParalXToZero(self)
```

Add segment, which sequentially connects the previous point with a point lying on a line parallel to the axis Ox and the value x = 0 The current point will be the previous value to the coordinate y.

### addSegmentParalY()

```python
def addSegmentParalY(self, y)
```

Add segment, which sequentially connects the previous point with a point lying on a line parallel to the axis Oy and the value y = param y.

The current point will be the previous value to the coordinate x and new value to the coordinate y. Coordinate is considered relative to the previous point.

Parameters
:   |  |  |
    | --- | --- |
    | y | - Coordinate of point on axis Oy |

### addSegmentParalYToZero()

```python
def addSegmentParalYToZero(self)
```

Add segment, which sequentially connects the previous point with a point lying on a line parallel to the axis Ox and the value x = 0 The current point will be the previous value to the coordinate y.

### addSegmentAbsolute()

```python
def addSegmentAbsolute(self, x, y)
```

Add segment, which sequentially connects the given point with previous point.

Coordinates are considered as absolute.

Parameters
:   |  |  |
    | --- | --- |
    | x,y | - Coordinates of point |

### addSegmentRelative()

```python
def addSegmentRelative(self, dx, dy)
```

Add segment, which sequentially connects the given point with previous point Coordinates are considered relative to the previous point.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point.

Parameters
:   |  |  |
    | --- | --- |
    | dx,dy | - Coordinates of point relative a previous point |

### addSegmentAngleLength()

```python
def addSegmentAngleLength(self, angle, length)
```

Add one straight segment, defined by angle and length.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point. The angle and length coordinates are defined in a local coordinate system which origin is the last point of the sketch

Parameters
:   |  |  |
    | --- | --- |
    | angle | - angle in a plane |
    | length | - length of the segment |

### addSegmentAngleX()

```python
def addSegmentAngleX(self, angle, x)
```

Add one straight segment, defined by angle and intersect straight x= param x.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point. The angle and point's coordinates are defined in a local coordinate system which origin is the last point of the sketch

Parameters
:   |  |  |
    | --- | --- |
    | angle | - angle in a plane |
    | x | - value on the axis Ox |

### addSegmentAngleY()

```python
def addSegmentAngleY(self, angle, y)
```

Add one straight segment, defined by angle and intersect straight y= param y.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point. The angle and point's coordinates are defined in a local coordinate system which origin is the last point of the sketch

Parameters
:   |  |  |
    | --- | --- |
    | angle | - angle in a plane |
    | y | - value on the axis Oy |

### addSegmentPerpLength()

```python
def addSegmentPerpLength(self, length)
```

Add one straight segment, defined by perpendicular(angle=90) and length.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point. The length coordinates are defined in a local coordinate system which origin is the last point of the sketch

Parameters
:   |  |  |
    | --- | --- |
    | length | - length of the segment |

### addSegmentPerpX()

```python
def addSegmentPerpX(self, x)
```

Add one straight segment, defined by perpendicular(angle=90) and intersect straight x= param x.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point. The point's coordinates are defined in a local coordinate system which origin is the last point of the sketch

Parameters
:   |  |  |
    | --- | --- |
    | x | - value on the axis Ox |

### addSegmentPerpY()

```python
def addSegmentPerpY(self, y)
```

Add one straight segment, defined by perpendicular(angle=90) and intersect straight y= param y.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point. The point's coordinates are defined in a local coordinate system which origin is the last point of the sketch

Parameters
:   |  |  |
    | --- | --- |
    | y | - value on the axis Oy |

### addSegmentLength()

```python
def addSegmentLength(self, length)
```

Add one straight segment, defined by previous direction and length.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point. The length coordinates are defined in a local coordinate system which origin is the last point of the sketch

Parameters
:   |  |  |
    | --- | --- |
    | length | - length of the segment |

### addSegmentX()

```python
def addSegmentX(self, x)
```

Add one straight segment, defined by previous direction and intersect straight x= param x.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point. The point's coordinates are defined in a local coordinate system which origin is the last point of the sketch

Parameters
:   |  |  |
    | --- | --- |
    | x | - value on the axis Ox |

### addSegmentY()

```python
def addSegmentY(self, y)
```

Add one straight segment, defined by previous direction and intersect straight y= param y.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point. The point's coordinates are defined in a local coordinate system which origin is the last point of the sketch

Parameters
:   |  |  |
    | --- | --- |
    | y | - value on the axis Oy |

### addSegmentDirectionLength()

```python
def addSegmentDirectionLength(self, dx, dy, length)
```

Add one straight segment, defined by direction and length.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point. The direction and length coordinates are defined in a local coordinate system which origin is the last point of the sketch

Parameters
:   |  |  |
    | --- | --- |
    | dx,dy | - direction of the segment |
    | length | - length of the segment |

### addSegmentDirectionX()

```python
def addSegmentDirectionX(self, dx, dy, x)
```

Add one straight segment, defined by direction and intersect straight x= param x.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point. The direction and point's coordinates are defined in a local coordinate system which origin is the last point of the sketch

Parameters
:   |  |  |
    | --- | --- |
    | dx,dy | - direction of the segment |
    | x | - value on the axis Ox |

### addSegmentDirectionY()

```python
def addSegmentDirectionY(self, dx, dy, y)
```

Add one straight segment, defined by direction and intersect straight y= param y.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point. The direction and point's coordinates are defined in a local coordinate system which origin is the last point of the sketch

Parameters
:   |  |  |
    | --- | --- |
    | dx,dy | - direction of the segment |
    | y | - value on the axis Oy |

### addArcAbsolute()

```python
def addArcAbsolute(self, x, y)
```

Add arc, which connects the given point with previous point Coordinates are considered as absolute.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point.

Parameters
:   |  |  |
    | --- | --- |
    | x,y | - Coordinates of second point of arc |

### addArcRelative()

```python
def addArcRelative(self, dx, dy)
```

Add arc, which connects the given point with previous point Coordinates are considered relative to the previous point.

Parameters
:   |  |  |
    | --- | --- |
    | dx,dy | - Coordinates of second point of arc relative to the previous point |

### addArcRadiusAbsolute()

```python
def addArcRadiusAbsolute(self, x, y, radius, flag)
```

Add arc, defined by radius and coordinates of next point.

Coordinates are considered as absolute. If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point.

Parameters
:   |  |  |
    | --- | --- |
    | x,y | - Coordinates of second point of arc |
    | radius | - radius of arc |
    | flag | - is 0 or 2 if 0 the drawn arc is the one of lower angle (<Pi) if 2 the drawn arc is the one of greater angle (>Pi) |

### addArcRadiusRelative()

```python
def addArcRadiusRelative(self, dx, dy, radius, flag)
```

Add arc, defined by radius and coordinates of next point.

Coordinates are considered relative to the previous point.

Parameters
:   |  |  |
    | --- | --- |
    | dx,dy | - Coordinates of second point of arc |
    | radius | - radius of arc |
    | flag | - is 0 or 2 if 0 the drawn arc is the one of lower angle (<Pi) if 2 the drawn arc is the one of greater angle (>Pi) |

### addArcCenterAbsolute()

```python
def addArcCenterAbsolute(self, x, y, xc, yc, flag1, flag2)
```

Add arc, defined by coordinates of next point and coordinates of center.

Coordinates are considered as absolute. If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point.

Parameters
:   |  |  |
    | --- | --- |
    | x,y | - Coordinates of second point of arc |
    | xc,yc | - Coordinates of center |
    | flag1 | - (reverse) is 0 or 2 if 0 the drawn arc is the one of lower angle (<Pi) if 2 the drawn arc is the one of greater angle (>Pi) |
    | flag2 | - (control tolerance) is 0 or 1 if 0 the specified end point can be at a distance of the arc |

### addArcCenterRelative()

```python
def addArcCenterRelative(self, dx, dy, xc, yc, flag1, flag2)
```

Add arc, defined by coordinates of next point and coordinates of center.

Coordinates are considered relative to the previous point.

Parameters
:   |  |  |
    | --- | --- |
    | dx,dy | - Coordinates of second point of arc |
    | xc,yc | - Coordinates of center |
    | flag1 | - (reverse) is 0 or 2 if 0 the drawn arc is the one of lower angle (<Pi) if 2 the drawn arc is the one of greater angle (>Pi) |
    | flag2 | - (control tolerance) is 0 or 1 if 0 the specified end point can be at a distance of the arc |

### addArcAngleRadiusLength()

```python
def addArcAngleRadiusLength(self, angle, radius, length)
```

Add arc, defined by angle, radius and length.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point.

Parameters
:   |  |  |
    | --- | --- |
    | angle | - angle in a plane |
    | radius | - radius of the arc |
    | length | - length of the arc |

### addArcPerpRadiusLength()

```python
def addArcPerpRadiusLength(self, radius, length)
```

Add arc, defined by perpendicular(angle=90), radius and length.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point.

Parameters
:   |  |  |
    | --- | --- |
    | radius | - radius of the arc |
    | length | - length of the arc |

### addArcRadiusLength()

```python
def addArcRadiusLength(self, radius, length)
```

Add arc, defined by previous direction, radius and length.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point.

Parameters
:   |  |  |
    | --- | --- |
    | radius | - radius of the arc |
    | length | - length of the arc |

### addArcDirectionRadiusLength()

```python
def addArcDirectionRadiusLength(self, dx, dy, radius, length)
```

Add arc, defined by direction, radius and length.

If the first point of sketcher is not yet defined, the origin (0, 0) will become the first sketcher point.

Parameters
:   |  |  |
    | --- | --- |
    | dx,dy | - direction of the arc |
    | radius | - radius of the arc |
    | length | - length of the arc |

### close()

```python
def close(self)
```

Set to close the wire.

### wire()

```python
def wire(self, WorkingPlane = [0, theName = None)
```

Obtain the sketcher result as a wire.

Parameters
:   |  |  |
    | --- | --- |
    | WorkingPlane | - current Working Plane used for this 2DSketcher |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New GEOM_Object, containing the created wire

### face()

```python
def face(self, WorkingPlane = [0, theName = None)
```

Obtain the sketcher result as a face.

Parameters
:   |  |  |
    | --- | --- |
    | WorkingPlane | - current Working Plane used for this 2DSketcher |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New GEOM_Object, containing the created face

## Field Documentation

### geompyD

```python
geompyD
```

### myCommand

```python
myCommand
```

### closed

```python
closed
```
