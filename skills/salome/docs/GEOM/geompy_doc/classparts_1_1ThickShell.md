<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classparts_1_1ThickShell.html -->

# ThickShell Class Reference structelem - Structural elements package » parts

This class defines a shell with a given thickness.
[More...](classparts_1_1ThickShell.md#details)

## Detailed Description

This class defines a shell with a given thickness.

It can be shifted from the base face. The valid parameters for thick shells are:

- "Epais": thickness of the shell.
- "Excentre": offset of the shell from the base face.
- "angleAlpha": angle used to build the markers (see class [salome.geom.structelem.orientation.Orientation2D](classorientation_1_1Orientation2D.md))
- "angleBeta": angle used to build the markers (see class [salome.geom.structelem.orientation.Orientation2D](classorientation_1_1Orientation2D.md))
- "Vecteur": vector used instead of the angles to build the markers (see [salome.geom.structelem.orientation.Orientation2D](classorientation_1_1Orientation2D.md))

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

Create the geometrical shapes corresponding to the thick shell.

### _buildThickShellForFace()

```python
def _buildThickShellForFace(self, face) private
```

Create the geometrical shapes corresponding to the thick shell for a given face.

### _removeCylinderExtraEdge()

```python
def _removeCylinderExtraEdge(self, wires) private
```

Remove the side edge in a cylinder.

### _buildMarkers()

```python
def _buildMarkers(self) private
```

Build the markers defining the orientation of the thick shell.

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
string DEFAULT_NAME = "ThickShell" static
```

### thickness

```python
thickness
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
