<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l4__access.html -->

# Access to sub-shapes by their unique IDs inside the main shape geomBuilder Python module » All package methods, grouped by their purpose » Creating geometrical objects » Creating Advanced Geometrical Objects

## Detailed Description

## Function Documentation

### GetSubShape()

```python
def GetSubShape(self, aShape, ListOfID, theName = None)
```

Obtain a composite sub-shape of *aShape*, composed from sub-shapes of aShape, selected by their unique IDs inside *aShape*

Parameters
:   |  |  |
    | --- | --- |
    | aShape | Shape to get sub-shape of. |
    | ListOfID | List of sub-shapes indices. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   Found sub-shape.

[Example](../tui_test_all_page.md#swig_all_decompose)

### GetSubShapeID()

```python
def GetSubShapeID(self, aShape, aSubShape)
```

Obtain unique ID of sub-shape *aSubShape* inside *aShape* of aShape, selected by their unique IDs inside *aShape*

Parameters
:   |  |  |
    | --- | --- |
    | aShape | Shape to get sub-shape of. |
    | aSubShape | Sub-shapes of aShape. |

Returns
:   ID of found sub-shape.

[Example](../tui_test_all_page.md#swig_all_decompose)

### GetSubShapesIDs()

```python
def GetSubShapesIDs(self, aShape, aSubShapes)
```

Obtain unique IDs of sub-shapes *aSubShapes* inside *aShape* This function is provided for performance purpose.

The complexity is O(n) with n the number of subobjects of aShape

Parameters
:   |  |  |
    | --- | --- |
    | aShape | Shape to get sub-shape of. |
    | aSubShapes | Sub-shapes of aShape. |

Returns
:   list of IDs of found sub-shapes.

[Example](../tui_test_all_page.md#swig_all_decompose)
