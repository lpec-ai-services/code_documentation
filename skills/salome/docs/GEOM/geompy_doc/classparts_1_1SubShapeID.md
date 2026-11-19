<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classparts_1_1SubShapeID.html -->

# SubShapeID Class Reference structelem - Structural elements package » parts

This class enables the use of sub-shapes in sets or as dictionary keys.
[More...](classparts_1_1SubShapeID.md#details)

## Detailed Description

This class enables the use of sub-shapes in sets or as dictionary keys.

It implements **eq** and **hash** methods so that sub-shapes with the same CORBA object *mainShape* and the same *id* are considered equal.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, mainShape, id)
```

## Member Function Documentation

### getObj()

```python
def getObj(self, geom)
```

Return the sub-shape ([GEOM](namespaceGEOM.md) object).

*geom* is a pseudo-geompy object used to find the geometrical object.

### __eq__()

```python
def __eq__(self, other)
```

### __hash__()

```python
def __hash__(self)
```

## Field Documentation

### _mainShape

```python
_mainShape private
```

### _id

```python
_id private
```
