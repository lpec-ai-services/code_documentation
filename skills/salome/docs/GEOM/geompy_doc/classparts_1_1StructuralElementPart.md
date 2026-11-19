<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classparts_1_1StructuralElementPart.html -->

# StructuralElementPart Class Reference structelem - Structural elements package » parts

This class is the base class for all structural element parts.
[More...](classparts_1_1StructuralElementPart.md#details)

## Detailed Description

This class is the base class for all structural element parts.

It should not be instantiated directly (consider it as an "abstract" class).

Parameters
:   |  |  |
    | --- | --- |
    | groupName | (string) the name of the underlying geometrical primitive in the study. |
    | groupGeomObj | ([GEOM](namespaceGEOM.md) object) the underlying geometrical primitive. |
    | parameters | (dictionary) parameters defining the structural element (see subclasses for details). |
    | name | (string) name to use for the created object in the study. |

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, groupName, groupGeomObj, parameters, name = DEFAULT_NAME, color = None)
```

## Member Function Documentation

### _getParameter()

```python
def _getParameter(self, nameList, default = None) private
```

This method finds the value of a parameter in the parameters dictionary.

The argument is a list because some parameters can have several different names.

### _getParamUserName()

```python
def _getParamUserName(self, paramName) private
```

This method finds the user name for a parameter.

### __repr__()

```python
def __repr__(self)
```

### addOrientation()

```python
def addOrientation(self, orientParams)
```

Add orientation information to the structural element part.

See class salome.geom.structelem.orientation.Orientation1D for the description of the parameters.

### _checkSize()

```python
def _checkSize(self, value, mindim, expression) private
```

This method checks that some parameters or some expressions involving those parameters are greater than a minimum value.

### build()

```python
def build(self)
```

Build the geometric shapes and the markers corresponding to the structural element part in the study.

### _buildPart()

```python
def _buildPart(self) private
```

This abstract method must be implemented in subclasses and should create the geometrical shape(s) of the structural element part.

### _buildMarkers()

```python
def _buildMarkers(self) private
```

This abstract method must be implemented in subclasses and should create the markers defining the orientation of the structural element part.

### _getSubShapes()

```python
def _getSubShapes(self, minDim = MIN_LENGTH_FOR_EXTRUSION) private
```

Find and return the base sub-shapes in the structural element part.

## Field Documentation

### DEFAULT_NAME

```python
string DEFAULT_NAME = "StructElemPart" static
```

### _parameters

```python
_parameters private
```

### groupName

```python
groupName
```

### _groupGeomObj

```python
_groupGeomObj private
```

### _orientation

```python
_orientation private
```

### _paramUserName

```python
_paramUserName private
```

### name

```python
name
```

### geom

```python
geom
```

### baseShapesSet

```python
baseShapesSet
```

### isMainShape

```python
isMainShape
```

### color

```python
color
```
