<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l2__testing.html -->

# Testing geomBuilder Python module » All package methods, grouped by their purpose

## Detailed Description

## Function Documentation

### Tesselate()

```python
def Tesselate(self, shape, linear_deflection = 0, is_relative = True, angular_deflection = 0)
```

Build a mesh on the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | shape | the source shape |
    | linear_deflection | linear deflection coefficient |
    | is_relative | says if given value of deflection is relative to shape's bounding box |
    | angular_deflection | angular deflection for edges in degrees |

Returns
:   True in case of success; otherwise False.

### CheckConformity()

```python
def CheckConformity(self, shape)
```

Obtain a shape checker.

Returns
:   An instance of [CheckConformity](classconformity_1_1CheckConformity.md) interface

Example

### ShapeProximity()

```python
def ShapeProximity(self)
```

Obtain a shape proximity calculator.

Returns
:   An instance of ShapeProximity interface

Example
