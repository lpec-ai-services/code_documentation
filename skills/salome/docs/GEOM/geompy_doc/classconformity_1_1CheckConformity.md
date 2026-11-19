<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classconformity_1_1CheckConformity.html -->

# CheckConformity Class Reference CheckConformity - Wrapper to find imperfections in the shape

An interface to find imperfections in the shape.
[More...](classconformity_1_1CheckConformity.md#details)

## Detailed Description

An interface to find imperfections in the shape.

Use geompy.CheckConformity(shape) method to obtain an instance of this class

[Example](../tui_check_conformity_page.md)

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, shape, geompyD)
```

## Member Function Documentation

### __checkShape()

```python
def __checkShape(self) private
```

Perform analyse of shape.

Returns
:   New List, which contains pair: type of check and single of pair failed sub-shapes.

### isValid()

```python
def isValid(self)
```

Check whether the shape is applicable for Boolean Operations.

Returns
:   Boolean value True if shape is applicable for Boolean Operations, otherwise - False

### selfIntersected2D()

```python
def selfIntersected2D(self)
```

Find all self-intersected 2D curves.

Returns
:   New List, of pair sub-shape, which has self-intersected in 2D

### interferingSubshapes()

```python
def interferingSubshapes(self, shapeType1 = AUTO, shapeType2 = AUTO)
```

Find pairs of interfering sub-shapes:

- vertices touched by tolerance;
- vertex touching an edge in the inner point;
- vertex lying on the inner point of a face;
- edges intersecting by inner points;
- edge touching/intersecting face in the inner point;
- faces intersection by inner point

Types of interfering shapes could be specified, by default all pairs of interfering shapes are returned.

Parameters
:   |  |  |
    | --- | --- |
    | shapeType1 | first type of shape |
    | shapeType2 | second type of shape |

Returns
:   New List, of pairs of interfering shapes with given types (if they was specified)

### smallEdges()

```python
def smallEdges(self)
```

Find edges, which are fully covered by tolerances of vertices.

Returns
:   New List of edges, which are fully covered by tolerances of vertices

### distantShapes()

```python
def distantShapes(self, shapeType = AUTO, subShapeType = AUTO, tolerance = -1.0)
```

Find remote objects (sub-shape on a shape):

- vertex far from edge;
- vertex far from face;
- edge far from face

Sub-shape which are lying far from its parent shape more than the given tolerance.

Parameters
:   |  |  |
    | --- | --- |
    | shapeType | type of shape |
    | subShapeType | type of sub-shape |
    | tolerance | available tolerance, by default used tolerance of sub-shape. |

Returns
:   New List, of pair of sub-shape with given types, that lying far from its parent shape more than the given tolerance.

### updateTolerance()

```python
def updateTolerance(self)
```

Compute possible tolerance for the shape, minimize tolerance of shape as well as tolerance of sub-shapes as much as possible .

Returns
:   New value of tolerance.

## Field Documentation

### AUTO

```python
int AUTO = -1 static
```

### geompyD

```python
geompyD
```

### myShape

```python
myShape
```

### myIsChecked

```python
myIsChecked
```

### myResults

```python
myResults
```
