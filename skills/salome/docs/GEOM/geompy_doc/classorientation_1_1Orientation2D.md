<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classorientation_1_1Orientation2D.html -->

# Orientation2D Class Reference structelem - Structural elements package » orientation

This class is used to compute the orientation of 2D elements and to build the corresponding markers.
[More...](classorientation_1_1Orientation2D.md#details)

## Detailed Description

This class is used to compute the orientation of 2D elements and to build the corresponding markers.

Angles *alpha* and *beta* are used to determine the local coordinate system for the 2D element. If *vect* is not **None**, it is used instead of *alpha* and *beta*.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, alpha, beta, vect)
```

## Member Function Documentation

### __repr__()

```python
def __repr__(self)
```

### _buildDefaultMarker()

```python
def _buildDefaultMarker(self, center, normal, warnings = True) private
```

Create the default marker, that use the normal vector of the 2D object as the local Z axis and the global X axis to determine the local X axis.

*warnings* can be used to enable or disable the logging of warning messages.

### _buildMarkerRefVecX()

```python
def _buildMarkerRefVecX(self, center, normal, refVecX) private
```

Create a marker using *normal* as Z axis and *refVecX* to determine the X axis.

### buildMarker()

```python
def buildMarker(self, geom, center, normal, warnings = True)
```

Create a marker with origin *center* and *normal* as Z axis.

The other axes are computed using the parameters alpha and beta of the [Orientation2D](classorientation_1_1Orientation2D.md) instance. *geom* is the pseudo-geompy object used to build the geometric shapes. *warnings* can be used to enable or disable the logging of warning messages.

## Field Documentation

### geom

```python
geom
```

### _alpha

```python
_alpha private
```

### _beta

```python
_beta private
```

### _vect

```python
_vect private
```
