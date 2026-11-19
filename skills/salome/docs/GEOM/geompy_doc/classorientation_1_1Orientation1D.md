<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classorientation_1_1Orientation1D.html -->

# Orientation1D Class Reference structelem - Structural elements package » orientation

This class is used to compute the orientation of 1D elements and to build the corresponding markers.
[More...](classorientation_1_1Orientation1D.md#details)

## Detailed Description

This class is used to compute the orientation of 1D elements and to build the corresponding markers.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self)
```

## Member Function Documentation

### __repr__()

```python
def __repr__(self)
```

### addParams()

```python
def addParams(self, params)
```

Add orientation parameters.

*params* is a dictionary containing one or several orientation parameters. The valid parameters are:

- "VECT_Y": Triplet defining the local Y axis (the X axis is the main direction of the 1D element).
- "ANGL_VRIL": Angle of rotation along the X axis to define the local coordinate system. The parameters can be specified several times. In this case, only the last "VECT_Y" or "ANGL_VRIL" is taken into account.

### _getDefaultVecYZ()

```python
def _getDefaultVecYZ(self, center, vecX) private
```

Get the vectors Y and Z for the default LCS, that use the main direction of the 1D object as the local X axis and the global Z axis to determine the local Z axis.

### buildMarker()

```python
def buildMarker(self, geom, center, vecX)
```

Create a marker with origin *center* and X axis *vecX*.

*geom* is the pseudo-geompy object used to build the geometric shapes.

### getVecYZ()

```python
def getVecYZ(self, geom, center, vecX)
```

Get the vectors Y and Z for the LCS with origin *center* and X axis *vecX*.

*geom* is the pseudo-geompy object used to build the geometric shapes.

## Field Documentation

### geom

```python
geom
```

### _vectorYCoords

```python
_vectorYCoords private
```

### _angle

```python
_angle private
```
