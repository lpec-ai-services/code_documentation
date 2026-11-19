<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classparts_1_1Grid.html -->

# Grid Class Reference structelem - Structural elements package » parts

This class defines a grid.
[More...](classparts_1_1Grid.md#details)

## Detailed Description

This class defines a grid.

A grid is represented by a 2D face patterned with small lines in the main direction of the grid frame. The valid parameters for grids are:

- "Excentre": offset of the grid from the base face.
- "angleAlpha": angle used to build the markers (see class [salome.geom.structelem.orientation.Orientation2D](classorientation_1_1Orientation2D.md))
- "angleBeta": angle used to build the markers (see class [salome.geom.structelem.orientation.Orientation2D](classorientation_1_1Orientation2D.md))
- "Vecteur": vector used instead of the angles to build the markers (see [salome.geom.structelem.orientation.Orientation2D](classorientation_1_1Orientation2D.md))
- "origAxeX": X coordinate of the origin of the axis used to determine the orientation of the frame in the case of a cylindrical grid.
- "origAxeY": Y coordinate of the origin of the axis used to determine the orientation of the frame in the case of a cylindrical grid.
- "origAxeZ": Z coordinate of the origin of the axis used to determine the orientation of the frame in the case of a cylindrical grid.
- "axeX": X coordinate of the axis used to determine the orientation of the frame in the case of a cylindrical grid.
- "axeY": Y coordinate of the axis used to determine the orientation of the frame in the case of a cylindrical grid.
- "axeZ": Z coordinate of the axis used to determine the orientation of the frame in the case of a cylindrical grid.

  See class [StructuralElementPart](classparts_1_1StructuralElementPart.md) for the description of the other parameters.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, groupName, groupGeomObj, parameters, name = DEFAULT_NAME)
```

## Member Function Documentation

### _buildPart()

```python
def _buildPart(self) private
```

Create the geometrical shapes representing the grid.

### _buildGridForNormalFace()

```python
def _buildGridForNormalFace(self, face) private
```

Create the geometrical shapes representing the grid for a given non-cylindrical face.

### _buildGridForCylinderFace()

```python
def _buildGridForCylinderFace(self, face) private
```

Create the geometrical shapes representing the grid for a given cylindrical face.

### _buildMarkers()

```python
def _buildMarkers(self) private
```

Create the markers defining the orientation of the grid.

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
string DEFAULT_NAME = "Grid" static
```

### xr

```python
xr
```

### yr

```python
yr
```

### zr

```python
zr
```

### vx

```python
vx
```

### vy

```python
vy
```

### vz

```python
vz
```

### offset

```python
offset inherited
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
