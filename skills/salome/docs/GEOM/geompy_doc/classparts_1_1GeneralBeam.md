<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classparts_1_1GeneralBeam.html -->

# GeneralBeam Class Reference structelem - Structural elements package » parts

This class defines a beam with a generic section.
[More...](classparts_1_1GeneralBeam.md#details)

## Detailed Description

This class defines a beam with a generic section.

It is represented as a full rectangular beam with the following parameters:

- HY1 = sqrt(12 * IZ1 / A1)
- HZ1 = sqrt(12 * IY1 / A1)
- HY2 = sqrt(12 * IZ2 / A2)
- HZ2 = sqrt(12 * IY2 / A2)

See [StructuralElementPart](classparts_1_1StructuralElementPart.md) for the description of the other parameters.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, groupName, groupGeomObj, parameters, name = Beam.DEFAULT_NAME, color = None)
```

## Member Function Documentation

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

### IY1

```python
IY1
```

### IZ1

```python
IZ1
```

### IY2

```python
IY2
```

### IZ2

```python
IZ2
```

### A1

```python
A1
```

### A2

```python
A2
```

### HY1

```python
HY1 inherited
```

### HZ1

```python
HZ1 inherited
```

### HY2

```python
HY2 inherited
```

### HZ2

```python
HZ2 inherited
```

### EPY1

```python
EPY1 inherited
```

### EPZ1

```python
EPZ1 inherited
```

### EPY2

```python
EPY2 inherited
```

### EPZ2

```python
EPZ2 inherited
```

### filling

```python
filling inherited
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
