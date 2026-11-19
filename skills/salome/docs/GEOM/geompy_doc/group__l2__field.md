<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l2__field.html -->

# Field on Geometry geomBuilder Python module » All package methods, grouped by their purpose

## Detailed Description

## Function Documentation

### CreateField()

```python
def CreateField(self, shape, name, type, dimension, componentNames)
```

Creates a field.

Parameters
:   |  |  |
    | --- | --- |
    | shape | the shape the field lies on |
    | name | the field name |
    | type | type of field data: 0 - bool, 1 - int, 2 - double, 3 - string |
    | dimension | dimension of the shape the field lies on 0 - VERTEX, 1 - EDGE, 2 - FACE, 3 - SOLID, -1 - whole shape |
    | componentNames | names of components |

Returns
:   a created field

### RemoveField()

```python
def RemoveField(self, field)
```

Removes a field from the [GEOM](namespaceGEOM.md) component.

Parameters
:   |  |  |
    | --- | --- |
    | field | the field to remove |

### CountFields()

```python
def CountFields(self, shape)
```

Returns number of fields on a shape.

### GetFields()

```python
def GetFields(self, shape)
```

Returns all fields on a shape.

### GetField()

```python
def GetField(self, shape, name)
```

Returns a field on a shape by its name.
