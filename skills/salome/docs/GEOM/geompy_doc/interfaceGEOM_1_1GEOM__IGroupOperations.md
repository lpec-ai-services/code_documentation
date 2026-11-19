<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__IGroupOperations.html -->

# GEOM_IGroupOperations Interface Reference

Interface for groups creation.
[More...](interfaceGEOM_1_1GEOM__IGroupOperations.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for groups creation.

## Member Function Documentation

### CreateGroup()

```python
GEOM_Object CreateGroup(in GEOM_Object theMainShape, in long theShapeType)
```

Creates a new group which will store sub-shapes of theMainShape.

Parameters
:   |  |  |
    | --- | --- |
    | theMainShape | is a [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) on which the group is selected |
    | theShapeType | defines a shape type of the group |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group

### AddObject()

```python
void AddObject(in GEOM_Object theGroup, in long theSubShapeId)
```

Adds a sub-object with ID theSubShapeId to the group.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group to which the new sub-shape is added |
    | theSubShapeId | is a sub-shape ID in the main object. |

Note
:   Use method *[GEOM_IShapesOperations.GetSubShapeIndex()](interfaceGEOM_1_1GEOM__IShapesOperations.md#a2f6aa8ddf89ba64785607a7eb137ec2b)* to get an ID by the sub-shape

### RemoveObject()

```python
void RemoveObject(in GEOM_Object theGroup, in long theSubShapeId)
```

Removes a sub-object with ID *theSubShapeId* from the group.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group from which the sub-shape is removed. |
    | theSubShapeId | is a sub-shape ID in the main object. |

Note
:   Use method *[GEOM_IShapesOperations.GetSubShapeIndex()](interfaceGEOM_1_1GEOM__IShapesOperations.md#a2f6aa8ddf89ba64785607a7eb137ec2b)* to get an ID by the sub-shape

### UnionList()

```python
void UnionList(in GEOM_Object theGroup, in ListOfGO theSubShapes)
```

Adds to the group all the given shapes. No errors, if some shapes are already included.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group to which the new sub-shapes are added. |
    | theSubShapes | is a list of sub-shapes to be added. |

### DifferenceList()

```python
void DifferenceList(in GEOM_Object theGroup, in ListOfGO theSubShapes)
```

Removes from the group all the given shapes. No errors, if some shapes are not included.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group from which the sub-shapes are removed. |
    | theSubShapes | is a list of sub-shapes to be removed. |

### UnionIDs()

```python
void UnionIDs(in GEOM_Object theGroup, in ListOfLong theSubShapes)
```

Adds to the group all the given shapes. No errors, if some shapes are already included.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group to which the new sub-shapes are added. |
    | theSubShapes | is a list of IDs of sub-shapes to be added. |

### DifferenceIDs()

```python
void DifferenceIDs(in GEOM_Object theGroup, in ListOfLong theSubShapes)
```

Removes from the group all the given shapes. No errors, if some shapes are not included.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group from which the sub-shapes are removed. |
    | theSubShapes | is a list of IDs of sub-shapes to be removed. |

### UnionGroups()

```python
GEOM_Object UnionGroups(in GEOM_Object theGroup1, in GEOM_Object theGroup2)
```

Union of two groups. New group is created. It will contain all entities which are present in groups theGroup1 and theGroup2.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup1,theGroup2 | are the initial [GEOM](namespaceGEOM.md) groups to create the united group from. |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group.

### IntersectGroups()

```python
GEOM_Object IntersectGroups(in GEOM_Object theGroup1, in GEOM_Object theGroup2)
```

Intersection of two groups. New group is created. It will contain only those entities which are present in both groups theGroup1 and theGroup2.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup1,theGroup2 | are the initial [GEOM](namespaceGEOM.md) groups to get common part of. |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group.

### CutGroups()

```python
GEOM_Object CutGroups(in GEOM_Object theGroup1, in GEOM_Object theGroup2)
```

Cut of two groups. New group is created. It will contain entities which are present in group theGroup1 but are not present in group theGroup2.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup1 | is a [GEOM](namespaceGEOM.md) group to include elements of. |
    | theGroup2 | is a [GEOM](namespaceGEOM.md) group to exclude elements of. |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group.

### UnionListOfGroups()

```python
GEOM_Object UnionListOfGroups(in ListOfGO theGList)
```

Union of list of groups. New group is created. It will contain all entities that are present in groups listed in theGList.

Parameters
:   |  |  |
    | --- | --- |
    | theGList | is a list of [GEOM](namespaceGEOM.md) groups to create the united group from. |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group.

### IntersectListOfGroups()

```python
GEOM_Object IntersectListOfGroups(in ListOfGO theGList)
```

Intersection of list of groups. New group is created. It will contain only entities which are simultaneously present in the groups listed in theGList.

Parameters
:   |  |  |
    | --- | --- |
    | theGList | is a list of [GEOM](namespaceGEOM.md) groups to get common part of. |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group.

### CutListOfGroups()

```python
GEOM_Object CutListOfGroups(in ListOfGO theGList1, in ListOfGO theGList2)
```

Cut of lists of groups. New group is created. It will contain only entities which are present in groups listed in theGList1 but are not present in groups from theGList2.

Parameters
:   |  |  |
    | --- | --- |
    | theGList1 | is a list of [GEOM](namespaceGEOM.md) groups to include elements of. |
    | theGList2 | is a list of [GEOM](namespaceGEOM.md) groups to exclude elements of. |

Returns
:   a newly created [GEOM](namespaceGEOM.md) group.

### GetType()

```python
long GetType(in GEOM_Object theGroup)
```

Returns a type of sub-objects stored in the group.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group which type is returned. |

### GetMainShape()

```python
GEOM_Object GetMainShape(in GEOM_Object theGroup)
```

Returns a main shape associated with the group.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group for which a main shape object is requested |

Returns
:   a [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) which is a main shape for theGroup

### GetObjects()

```python
ListOfLong GetObjects(in GEOM_Object theGroup)
```

Returns a list of sub-objects ID stored in the group.

Parameters
:   |  |  |
    | --- | --- |
    | theGroup | is a [GEOM](namespaceGEOM.md) group for which a list of IDs is requested |

### IsDone()

```python
boolean IsDone() inherited
```

To know, if the operation was successfully performed.

### SetErrorCode()

```python
void SetErrorCode(in string theErrorID) inherited
```

Set the operation error code.

Parameters
:   |  |  |
    | --- | --- |
    | theErrorID | is a string describing the error occurred |

Note
:   This method is supposed to be used only by interfaces inheriting from IOperations.

### GetErrorCode()

```python
string GetErrorCode() inherited
```

Get the operation error code.

### StartOperation()

```python
void StartOperation() inherited
```

Opens a new transaction.

### FinishOperation()

```python
void FinishOperation() inherited
```

Closes the previously opened transaction.

### AbortOperation()

```python
void AbortOperation() inherited
```

Aborts the previously opened transaction.
