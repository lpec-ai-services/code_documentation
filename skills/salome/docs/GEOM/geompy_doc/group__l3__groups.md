<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l3__groups.html -->

# Working with groups geomBuilder Python module » All package methods, grouped by their purpose » Creating geometrical objects

## Detailed Description

## Function Documentation

### CreateGroup()

```python
def CreateGroup(self, theMainShape, theShapeType, theName = None)
```

Creates a new group which will store sub-shapes of theMainShape.

Parameters
:   |  |  |
    | --- | --- |
    | theMainShape | is a [GEOM](namespaceGEOM.md) object on which the group is selected |
    | theShapeType | defines a shape type of the group (see [GEOM::shape_type](namespaceGEOM.md#a82a00e336c65dad4cc04b65563b26eb5)) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group ([GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md))

[Example 1](../tui_working_with_groups_page.md)   
[Example 2](../tui_test_others_page.md#swig_CreateGroup)

### AddObject()

```python
def AddObject(self, theGroup, theSubShapeID)
```

Adds a sub-object with ID theSubShapeId to the group.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group to which the new sub-shape is added |
    | theSubShapeID | is a sub-shape ID in the main object. |

Note
:   Use method [GetSubShapeID()](group__l4__access.md#gab8920ca3c07df6afcff7386821a2eccc) to get an unique ID of the sub-shape

[Example](../tui_working_with_groups_page.md)

### RemoveObject()

```python
def RemoveObject(self, theGroup, theSubShapeID)
```

Removes a sub-object with ID *theSubShapeId* from the group.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group from which the new sub-shape is removed |
    | theSubShapeID | is a sub-shape ID in the main object. |

Note
:   Use method [GetSubShapeID()](group__l4__access.md#gab8920ca3c07df6afcff7386821a2eccc) to get an unique ID of the sub-shape

[Example](../tui_working_with_groups_page.md)

### UnionList()

```python
def UnionList(self, theGroup, theSubShapes)
```

Adds to the group all the given shapes.

No errors, if some shapes are already included.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group to which the new sub-shapes are added. |
    | theSubShapes | is a list of sub-shapes to be added. |

[Example](../tui_working_with_groups_page.md)

### UnionIDs()

```python
def UnionIDs(self, theGroup, theSubShapes)
```

Adds to the group all the given shapes.

No errors, if some shapes are already included.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group to which the new sub-shapes are added. |
    | theSubShapes | is a list of indices of sub-shapes to be added. |

[Example](../tui_test_others_page.md#swig_UnionIDs)

### DifferenceList()

```python
def DifferenceList(self, theGroup, theSubShapes)
```

Removes from the group all the given shapes.

No errors, if some shapes are not included.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group from which the sub-shapes are removed. |
    | theSubShapes | is a list of sub-shapes to be removed. |

[Example](../tui_working_with_groups_page.md)

### DifferenceIDs()

```python
def DifferenceIDs(self, theGroup, theSubShapes)
```

Removes from the group all the given shapes.

No errors, if some shapes are not included.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group from which the sub-shapes are removed. |
    | theSubShapes | is a list of indices of sub-shapes to be removed. |

[Example](../tui_test_others_page.md#swig_DifferenceIDs)

### UnionGroups()

```python
def UnionGroups(self, theGroup1, theGroup2, theName = None)
```

Union of two groups.

New group is created. It will contain all entities which are present in groups theGroup1 and theGroup2.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup1,theGroup2 | are the initial [GEOM](namespaceGEOM.md) groups to create the united group from. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group.

[Example](../tui_working_with_groups_page.md#tui_union_groups_anchor)

### IntersectGroups()

```python
def IntersectGroups(self, theGroup1, theGroup2, theName = None)
```

Intersection of two groups.

New group is created. It will contain only those entities which are present in both groups theGroup1 and theGroup2.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup1,theGroup2 | are the initial [GEOM](namespaceGEOM.md) groups to get common part of. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group.

[Example](../tui_working_with_groups_page.md#tui_intersect_groups_anchor)

### CutGroups()

```python
def CutGroups(self, theGroup1, theGroup2, theName = None)
```

Cut of two groups.

New group is created. It will contain entities which are present in group theGroup1 but are not present in group theGroup2.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup1 | is a [GEOM](namespaceGEOM.md) group to include elements of. |
    | theGroup2 | is a [GEOM](namespaceGEOM.md) group to exclude elements of. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group.

[Example](../tui_working_with_groups_page.md#tui_cut_groups_anchor)

### UnionListOfGroups()

```python
def UnionListOfGroups(self, theGList, theName = None)
```

Union of list of groups.

New group is created. It will contain all entities that are present in groups listed in theGList.

Parameters
:   |  |  |
    | --- | --- |
    | theGList | is a list of [GEOM](namespaceGEOM.md) groups to create the united group from. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group.

[Example](../tui_working_with_groups_page.md#tui_union_groups_anchor)

### IntersectListOfGroups()

```python
def IntersectListOfGroups(self, theGList, theName = None)
```

Cut of lists of groups.

New group is created. It will contain only entities which are present in groups listed in theGList.

Parameters
:   |  |  |
    | --- | --- |
    | theGList | is a list of [GEOM](namespaceGEOM.md) groups to include elements of. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group.

[Example](../tui_working_with_groups_page.md#tui_intersect_groups_anchor)

### CutListOfGroups()

```python
def CutListOfGroups(self, theGList1, theGList2, theName = None)
```

Cut of lists of groups.

New group is created. It will contain only entities which are present in groups listed in theGList1 but are not present in groups from theGList2.

Parameters
:   |  |  |
    | --- | --- |
    | theGList1 | is a list of [GEOM](namespaceGEOM.md) groups to include elements of. |
    | theGList2 | is a list of [GEOM](namespaceGEOM.md) groups to exclude elements of. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group.

[Example](../tui_working_with_groups_page.md#tui_cut_groups_anchor)

### GetObjectIDs()

```python
def GetObjectIDs(self, theGroup)
```

Returns a list of sub-objects ID stored in the group.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group for which a list of IDs is requested |

[Example](../tui_test_others_page.md#swig_GetObjectIDs)

### GetType()

```python
def GetType(self, theGroup)
```

Returns a type of sub-objects stored in the group.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group which type is returned. |

[Example](../tui_test_others_page.md#swig_GetType)

### ShapeIdToType()

```python
def ShapeIdToType(self, theId)
```

Convert a type of geom object from id to string value.

Parameters
:   |  |  |
    | --- | --- |
    | theId | is a [GEOM](namespaceGEOM.md) object type id. |

Returns
:   type of geom object (POINT, VECTOR, PLANE, LINE, TORUS, ... ) [Example](../tui_test_others_page.md#swig_GetType)

### GetMainShape()

```python
def GetMainShape(self, theGroup)
```

Returns a main shape associated with the group.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group for which a main shape object is requested |

Returns
:   a [GEOM](namespaceGEOM.md) object which is a main shape for theGroup

[Example](../tui_test_others_page.md#swig_GetMainShape)

### GetEdgesByLength()

```python
def GetEdgesByLength(self, theShape, min_length, max_length, include_min = 1, include_max = 1, theName = None)
```

Create group of edges of theShape, whose length is in range [min_length, max_length].

If include_min/max == 0, edges with length == min/max_length will not be included in result.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | given shape (see [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md)) |
    | min_length | minimum length of edges of theShape |
    | max_length | maximum length of edges of theShape |
    | include_max | indicating if edges with length == max_length should be included in result, 1-yes, 0-no (default=1) |
    | include_min | indicating if edges with length == min_length should be included in result, 1-yes, 0-no (default=1) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group of edges

@ref swig_todo "Example"

### SelectEdges()

```python
def SelectEdges(self, min_length, max_length, include_min = 1, include_max = 1)
```

Create group of edges of selected shape, whose length is in range [min_length, max_length].

If include_min/max == 0, edges with length == min/max_length will not be included in result.

Parameters
:   |  |  |
    | --- | --- |
    | min_length | minimum length of edges of selected shape |
    | max_length | maximum length of edges of selected shape |
    | include_max | indicating if edges with length == max_length should be included in result, 1-yes, 0-no (default=1) |
    | include_min | indicating if edges with length == min_length should be included in result, 1-yes, 0-no (default=1) |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group of edges Example
