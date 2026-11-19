<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classparts_1_1Beam.html -->

# Beam Class Reference structelem - Structural elements package » parts

This class is an "abstract" class for all 1D structural element parts.
[More...](classparts_1_1Beam.md#details)

## Detailed Description

This class is an "abstract" class for all 1D structural element parts.

It should not be instantiated directly. See class [StructuralElementPart](classparts_1_1StructuralElementPart.md) for the description of the parameters.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, groupName, groupGeomObj, parameters, name = DEFAULT_NAME, color = None)
```

## Member Function Documentation

### _isReversed()

```python
def _isReversed(self, path) private
```

This method checks if a 1D object is "reversed", i.e.

if its orientation is different than the orientation of the underlying OCC object.

### _getVertexAndTangentOnOrientedWire()

```python
def _getVertexAndTangentOnOrientedWire(self, path, param) private
```

Get a vertex and the corresponding tangent on a wire by parameter.

This method takes into account the "real" orientation of the wire (i.e. the orientation of the underlying OCC object).

### _makeSolidPipeFromWires()

```python
def _makeSolidPipeFromWires(self, wire1, wire2, point1, point2, path) private
```

Create a solid by the extrusion of section *wire1* to section *wire2* along *path*.

### _buildPart()

```python
def _buildPart(self) private
```

Build the structural element part.

### _buildMarkers()

```python
def _buildMarkers(self) private
```

Build the markers defining the orientation of the structural element part.

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
string DEFAULT_NAME = "Beam" static
```

### _orientation

```python
_orientation private
```

### filling

```python
filling
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
