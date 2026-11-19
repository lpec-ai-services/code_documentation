<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classgsketcher_1_1Sketcher3D.html -->

# Sketcher3D Class Reference gsketcher - Wrapper to help the creation of simple sketches

An interface to build a 3D Sketcher step-by-step.
[More...](classgsketcher_1_1Sketcher3D.md#details)

## Detailed Description

An interface to build a 3D Sketcher step-by-step.

Use geompy.Sketcher3D() method to obtain an instance of this class.

[Example](../tui_3dsketcher_page.md)

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, geompyD)
```

## Member Function Documentation

### addPointsAbsolute()

```python
def addPointsAbsolute(self, listCoords)
```

Add one or more points, sequentially connected with straight segments.

Coordinates are considered as absolute. If the first point of sketcher is not yet defined, the first point from the listCoords will become the first sketcher point.

Parameters
:   |  |  |
    | --- | --- |
    | listCoords | X1, Y1, Z1, X2, Y2, Z2, ... Coordinates of points |

### addPointsRelative()

```python
def addPointsRelative(self, listCoords)
```

Add one or more points, sequentially connected with straight segments.

Coordinates are considered relative to the previous point. If the first point of sketcher is not yet defined, the origin (0, 0, 0) will become the first sketcher point.

Parameters
:   |  |  |
    | --- | --- |
    | listCoords | X1, Y1, Z1, X2, Y2, Z2, ... Coordinates of points |

### addPointRadiusAnglesRelative()

```python
def addPointRadiusAnglesRelative(self, length, angle1, angle2, axes = "OXY")
```

Add one straight segment, defined by two angles and length.

If the first point of sketcher is not yet defined, the origin (0, 0, 0) will become the first sketcher point. The radius and angles coordinates are defined in a local coordinate system which origin is the last point of the sketch

Parameters
:   |  |  |
    | --- | --- |
    | length | length of the segment |
    | angle1 | angle in a plane, defined by the *axes* |
    | angle2 | angle from the plane, defined by the *axes* |
    | axes | can be: "OXY", "OYZ" or "OXZ" |

### addPointRadiusAnglesAbsolute()

```python
def addPointRadiusAnglesAbsolute(self, radius, angle1, angle2, axes = "OXY")
```

Add one straight segment, defined by two angles and radius.

If the first point of sketcher is not yet defined, the origin (0, 0, 0) will become the first sketcher point. The radius and angles coordinates are defined in a coordinate system which origin is the global coordinate system origin

Parameters
:   |  |  |
    | --- | --- |
    | radius | distance to the coordinate system origin |
    | angle1 | angle in a plane, defined by the *axes* |
    | angle2 | angle from the plane, defined by the *axes* |
    | axes | can be: "OXY", "OYZ" or "OXZ" |

### addPointRadiusAngleHRelative()

```python
def addPointRadiusAngleHRelative(self, length, angle, height, axes = "OXY")
```

Add one straight segment, defined by an angle, a height and a radius.

If the first point of sketcher is not yet defined, the origin (0, 0, 0) will become the first sketcher point. The radius height and angle coordinates are defined in a local coordinate system which origin is the last point of the sketch

Parameters
:   |  |  |
    | --- | --- |
    | axes | can be: "OXY", "OYZ" or "OXZ" |
    | angle | angle in a plane, defined by the *axes* |
    | height | height from the plane, defined by the *axes* |
    | length | distance to the coordinate system origin |

### addPointRadiusAngleHAbsolute()

```python
def addPointRadiusAngleHAbsolute(self, radius, angle, height, axes = "OXY")
```

Add one straight segment, defined by an angle, a height and a radius.

If the first point of sketcher is not yet defined, the origin (0, 0, 0) will become the first sketcher point. The radius height and angle coordinates are defined in a coordinate system which origin is the global coordinate system origin

Parameters
:   |  |  |
    | --- | --- |
    | radius | distance to the coordinate system origin |
    | angle | angle in a plane, defined by the *axes* |
    | height | height from the plane, defined by the *axes* |
    | axes | can be: "OXY", "OYZ" or "OXZ" |

### close()

```python
def close(self)
```

Set to close the wire.

### wire()

```python
def wire(self, theName = None)
```

Obtain the sketcher result.

Parameters
:   |  |  |
    | --- | --- |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New GEOM_Object, containing the created wire

## Field Documentation

### geompyD

```python
geompyD
```

### myCommand

```python
myCommand
```
