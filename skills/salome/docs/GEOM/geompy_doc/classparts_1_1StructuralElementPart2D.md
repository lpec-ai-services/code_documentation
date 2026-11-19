<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classparts_1_1StructuralElementPart2D.html -->

# StructuralElementPart2D Class Reference structelem - Structural elements package » parts

This class is an "abstract" class for all 2D structural element parts.
[More...](classparts_1_1StructuralElementPart2D.md#details)

## Detailed Description

This class is an "abstract" class for all 2D structural element parts.

It should not be instantiated directly. See class [StructuralElementPart](classparts_1_1StructuralElementPart.md) for the description of the parameters.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, groupName, groupGeomObj, parameters, name = DEFAULT_NAME)
```

## Member Function Documentation

### _makeFaceOffset()

```python
def _makeFaceOffset(self, face, offset, epsilon = 1e-6) private
```

Create a copy of a face at a given offset.

### _buildMarkersWithOffset()

```python
def _buildMarkersWithOffset(self, offset) private
```

Build the markers for the structural element part with a given offset from the base face.

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

### DEFAULT_NAME

```python
string DEFAULT_NAME = "StructuralElementPart2D" static
```

### _orientation

```python
_orientation private
```

### offset

```python
offset
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
