<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classparts_1_1CircularBeam.html -->

# CircularBeam Class Reference structelem - Structural elements package » parts

This class defines a beam with a circular section.
[More...](classparts_1_1CircularBeam.md#details)

## Detailed Description

This class defines a beam with a circular section.

It can be full or hollow, and its radius and thickness can vary from one end of the beam to the other. The valid parameters for circular beams are:

- "R1" or "R": radius at the first end of the beam.
- "R2" or "R": radius at the other end of the beam.
- "EP1" or "EP" (optional): thickness at the first end of the beam. If not specified or equal to 0, the beam is considered full.
- "EP2" or "EP" (optional): thickness at the other end of the beam. If not specified or equal to 0, the beam is considered full.

See class [StructuralElementPart](classparts_1_1StructuralElementPart.md) for the description of the other parameters.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, groupName, groupGeomObj, parameters, name = Beam.DEFAULT_NAME, color = None)
```

## Member Function Documentation

### _makeSectionWires()

```python
def _makeSectionWires(self, fPoint, fNormal, lPoint, lNormal) private
```

Create the circular sections used to build the pipe.

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

### R1

```python
R1
```

### R2

```python
R2
```

### EP1

```python
EP1
```

### EP2

```python
EP2
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
