<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classparts_1_1RectangularBeam.html -->

# RectangularBeam Class Reference structelem - Structural elements package » parts

This class defines a beam with a rectangular section.
[More...](classparts_1_1RectangularBeam.md#details)

## Detailed Description

This class defines a beam with a rectangular section.

It can be full or hollow, and its dimensions can vary from one end of the beam to the other. The valid parameters for rectangular beams are:

- "HY1", "HY", "H1" or "H": width at the first end of the beam.
- "HZ1", "HZ", "H1" or "H": height at the first end of the beam.
- "HY2", "HY", "H2" or "H": width at the other end of the beam.
- "HZ2", "HZ", "H2" or "H": height at the other end of the beam.
- "EPY1", "EPY", "EP1" or "EP" (optional): thickness in the width direction at the first end of the beam. If not specified or equal to 0, the beam is considered full.
- "EPZ1", "EPZ", "EP1" or "EP" (optional): thickness in the height direction at the first end of the beam. If not specified or equal to 0, the beam is considered full.
- "EPY2", "EPY", "EP2" or "EP" (optional): thickness in the width direction at the other end of the beam. If not specified or equal to 0, the beam is considered full.
- "EPZ2", "EPZ", "EP2" or "EP" (optional): thickness in the height direction at the other end of the beam. If not specified or equal to 0, the beam is considered full.

  See class [StructuralElementPart](classparts_1_1StructuralElementPart.md) for the description of the other parameters.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, groupName, groupGeomObj, parameters, name = Beam.DEFAULT_NAME, color = None)
```

## Member Function Documentation

### _makeRectangle()

```python
def _makeRectangle(self, HY, HZ, lcs) private
```

Create a rectangle in the specified plane.

### _makeSectionRectangles()

```python
def _makeSectionRectangles(self, point, vecX, HY, HZ, EPY, EPZ) private
```

Create one side of the rectangular sections used to build the pipe.

### _makeSectionWires()

```python
def _makeSectionWires(self, fPoint, fNormal, lPoint, lNormal) private
```

Create the rectangular sections used to build the pipe.

### __repr__()

```python
def __repr__(self) inherited
```

### addOrientation()

```python
def addOrientation(self, orientParams) inherited
```

Add orientation information to the structural element part.

See class salome.geom.structelem.orientation.Orientation1D for the description of the parameters.

### build()

```python
def build(self) inherited
```

Build the geometric shapes and the markers corresponding to the structural element part in the study.

## Field Documentation

### HY1

```python
HY1
```

### HZ1

```python
HZ1
```

### HY2

```python
HY2
```

### HZ2

```python
HZ2
```

### EPY1

```python
EPY1
```

### EPZ1

```python
EPZ1
```

### EPY2

```python
EPY2
```

### EPZ2

```python
EPZ2
```

### filling

```python
filling
```

### DEFAULT_NAME

```python
string DEFAULT_NAME = "Beam" static inherited
```

### groupName

```python
groupName inherited
```

### name

```python
name inherited
```

### geom

```python
geom inherited
```

### baseShapesSet

```python
baseShapesSet inherited
```

### isMainShape

```python
isMainShape inherited
```

### color

```python
color inherited
```
