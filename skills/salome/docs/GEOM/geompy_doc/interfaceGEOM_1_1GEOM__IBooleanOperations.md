<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__IBooleanOperations.html -->

# GEOM_IBooleanOperations Interface Reference

Interface for boolean operations (Cut, Fuse, Common)
[More...](interfaceGEOM_1_1GEOM__IBooleanOperations.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for boolean operations (Cut, Fuse, Common)

## Member Function Documentation

### MakeBoolean()

```python
GEOM_Object MakeBoolean(in GEOM_Object theShape1, in GEOM_Object theShape2, in long theOperation, in boolean IsCheckSelfInte)
```

Perform one of boolean operations on two given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1 | First argument for boolean operation. |
    | theShape2 | Second argument for boolean operation. |
    | theOperation | Indicates the operation to be done: 1 - Common, 2 - Cut, 3 - Fuse, 4 - Section. |
    | IsCheckSelfInte | If TRUE, perform check self intersection of arguments before an operation. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeFuse()

```python
GEOM_Object MakeFuse(in GEOM_Object theShape1, in GEOM_Object theShape2, in boolean IsCheckSelfInte, in boolean IsRmExtraEdges)
```

Perform fusion boolean operation on two given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1 | First argument for fuse operation. |
    | theShape2 | Second argument for fuse operation. |
    | IsCheckSelfInte | If TRUE, perform check self intersection of arguments before an operation. |
    | IsRmExtraEdges | If TRUE, perform removal of extra edges during an operation. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeFuseList()

```python
GEOM_Object MakeFuseList(in ListOfGO theShapes, in boolean IsCheckSelfInte, in boolean IsRmExtraEdges)
```

Perform fusion boolean operation on list of objects.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Shapes to be fused. |
    | IsCheckSelfInte | If TRUE, perform check self intersection of arguments before an operation. |
    | IsRmExtraEdges | If TRUE, perform removal of extra edges during an operation. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeCommonList()

```python
GEOM_Object MakeCommonList(in ListOfGO theShapes, in boolean IsCheckSelfInte)
```

Perform common boolean operation on list of objects.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Shapes for common operation. |
    | IsCheckSelfInte | If TRUE, perform check self intersection of arguments before an operation. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeCutList()

```python
GEOM_Object MakeCutList(in GEOM_Object theMainShape, in ListOfGO theShapes, in boolean IsCheckSelfInte)
```

Perform cutting of list of objects from theMainShape.

Parameters
:   |  |  |
    | --- | --- |
    | theMainShape | the object for cut operation. |
    | theShapes | Shapes to be cut from theMainShape (tools). |
    | IsCheckSelfInte | If TRUE, perform check self intersection of arguments before an operation. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakePartition()

```python
GEOM_Object MakePartition(in ListOfGO theShapes, in ListOfGO theTools, in ListOfGO theKeepInside, in ListOfGO theRemoveInside, in short theLimit, in boolean theRemoveWebs, in ListOfLong theMaterials, in short theKeepNonlimitShapes)
```

Perform partition operation.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Shapes to be intersected. |
    | theTools | Shapes to intersect theShapes. |

Note
:   Each compound from ListShapes and ListTools will be exploded in order to avoid possible intersection between shapes from this compound.

Parameters
:   |  |  |
    | --- | --- |
    | theLimit | Type of resulting shapes (corresponding to TopAbs_ShapeEnum). |
    | theKeepNonlimitShapes | if this parameter == 0, then only shapes of target type (equal to Limit) are kept in the result, else standalone shapes of lower dimension are kept also (if they exist). |

After implementation new version of PartitionAlgo (October 2006) other parameters are ignored by current functionality. They are kept in this function only for supporting old versions. Ignored parameters:

Parameters
:   |  |  |
    | --- | --- |
    | theKeepInside | Shapes, outside which the results will be deleted. Each shape from theKeepInside must belong to theShapes also. |
    | theRemoveInside | Shapes, inside which the results will be deleted. Each shape from theRemoveInside must belong to theShapes also. |
    | theRemoveWebs | If TRUE, perform Glue 3D algorithm. |
    | theMaterials | Material indices for each shape. Make sense, only if theRemoveWebs is TRUE. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shapes.

### MakePartitionNonSelfIntersectedShape()

```python
GEOM_Object MakePartitionNonSelfIntersectedShape(in ListOfGO theShapes, in ListOfGO theTools, in ListOfGO theKeepInside, in ListOfGO theRemoveInside, in short theLimit, in boolean theRemoveWebs, in ListOfLong theMaterials, in short theKeepNonlimitShapes, in boolean IsCheckSelfInte)
```

Perform partition operation.

This method may be useful if it is needed to make a partition for a compound containing nonintersected shapes. Performance will be better since intersection between shapes from compound is not performed.

Description of all parameters as in previous method [MakePartition()](interfaceGEOM_1_1GEOM__IBooleanOperations.md#a4e60098799fbcf12b04d67ba1c3d9e3f). One additional parameter is provided:

Parameters
:   |  |  |
    | --- | --- |
    | IsCheckSelfInte | If TRUE, perform check self intersection of arguments before an operation. |

Note
:   Passed compounds (via ListShapes or via ListTools) have to consist of nonintersecting shapes.

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shapes.

### MakeHalfPartition()

```python
GEOM_Object MakeHalfPartition(in GEOM_Object theShape, in GEOM_Object thePlane)
```

Perform partition of the Shape with the Plane.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be intersected. |
    | thePlane | Tool shape, to intersect theShape. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

Note
:   This operation is a shortcut to the more general [MakePartition](interfaceGEOM_1_1GEOM__IBooleanOperations.md#a4e60098799fbcf12b04d67ba1c3d9e3f) operation, where *theShape* specifies single "object" (shape being partitioned) and *thePlane* specifies single "tool" (intersector shape). Other parameters of [MakePartition](interfaceGEOM_1_1GEOM__IBooleanOperations.md#a4e60098799fbcf12b04d67ba1c3d9e3f) operation have default values:

    - *theLimit:* [GEOM::SHAPE](namespaceGEOM.md#a82a00e336c65dad4cc04b65563b26eb5a20f1b6e28cd67b9244936ffc716e5611) (shape limit corresponds to the type of *theShape*)
    - *theKeepNonlimitShapes:* 0
    - *theKeepInside*, *theRemoveInside*, *theRemoveWebs*, *theMaterials* (obsolete parameters): empty

See also
:   [MakePartition](interfaceGEOM_1_1GEOM__IBooleanOperations.md#a4e60098799fbcf12b04d67ba1c3d9e3f), [MakePartitionNonSelfIntersectedShape](interfaceGEOM_1_1GEOM__IBooleanOperations.md#a98a61962999c881cf13a9aeed2795c22)

### MakeBooleanWithFuzzy()

```python
GEOM_Object MakeBooleanWithFuzzy(in GEOM_Object theShape1, in GEOM_Object theShape2, in long theOperation, in boolean IsCheckSelfInte, in double theFuzzyParam)
```

Perform one of boolean operations on two given shapes.

[bos#40619] [CEA] Add Fuzzy parameter to partition and boolean operators New interface methods were added to support a fuzzy parameter in all boolean and partition operations:

- MakeBooleanWithFuzzy
- MakeFuseWithFuzzy
- MakeFuseListWithFuzzy
- MakeCommonListWithFuzzy
- MakeCutListWithFuzzy
- MakePartitionWithFuzzy
- MakePartitionNonSelfIntersectedShapeWithFuzzy
- MakeHalfPartitionWithFuzzy

Parameters
:   |  |  |
    | --- | --- |
    | theShape1 | First argument for boolean operation. |
    | theShape2 | Second argument for boolean operation. |
    | theOperation | Indicates the operation to be done: 1 - Common, 2 - Cut, 3 - Fuse, 4 - Section. |
    | IsCheckSelfInte | If TRUE, perform check self intersection of arguments before an operation. |
    | theFuzzyParam | The fuzzy tolerance to be used in the boolean algorithm, if the value is positive. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeFuseWithFuzzy()

```python
GEOM_Object MakeFuseWithFuzzy(in GEOM_Object theShape1, in GEOM_Object theShape2, in boolean IsCheckSelfInte, in boolean IsRmExtraEdges, in double theFuzzyParam)
```

Perform fusion boolean operation on two given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1 | First argument for fuse operation. |
    | theShape2 | Second argument for fuse operation. |
    | IsCheckSelfInte | If TRUE, perform check self intersection of arguments before an operation. |
    | IsRmExtraEdges | If TRUE, perform removal of extra edges during an operation. |
    | theFuzzyParam | The fuzzy tolerance to be used in the boolean algorithm, if the value is positive. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeFuseListWithFuzzy()

```python
GEOM_Object MakeFuseListWithFuzzy(in ListOfGO theShapes, in boolean IsCheckSelfInte, in boolean IsRmExtraEdges, in double theFuzzyParam)
```

Perform fusion boolean operation on list of objects.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Shapes to be fused. |
    | IsCheckSelfInte | If TRUE, perform check self intersection of arguments before an operation. |
    | IsRmExtraEdges | If TRUE, perform removal of extra edges during an operation. |
    | theFuzzyParam | The fuzzy tolerance to be used in the boolean algorithm, if the value is positive. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeCommonListWithFuzzy()

```python
GEOM_Object MakeCommonListWithFuzzy(in ListOfGO theShapes, in boolean IsCheckSelfInte, in double theFuzzyParam)
```

Perform common boolean operation on list of objects.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Shapes for common operation. |
    | IsCheckSelfInte | If TRUE, perform check self intersection of arguments before an operation. |
    | theFuzzyParam | The fuzzy tolerance to be used in the boolean algorithm, if the value is positive. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeCutListWithFuzzy()

```python
GEOM_Object MakeCutListWithFuzzy(in GEOM_Object theMainShape, in ListOfGO theShapes, in boolean IsCheckSelfInte, in double theFuzzyParam)
```

Perform cutting of list of objects from theMainShape.

Parameters
:   |  |  |
    | --- | --- |
    | theMainShape | the object for cut operation. |
    | theShapes | Shapes to be cut from theMainShape (tools). |
    | IsCheckSelfInte | If TRUE, perform check self intersection of arguments before an operation. |
    | theFuzzyParam | The fuzzy tolerance to be used in the boolean algorithm, if the value is positive. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakePartitionWithFuzzy()

```python
GEOM_Object MakePartitionWithFuzzy(in ListOfGO theShapes, in ListOfGO theTools, in ListOfGO theKeepInside, in ListOfGO theRemoveInside, in short theLimit, in boolean theRemoveWebs, in ListOfLong theMaterials, in short theKeepNonlimitShapes, in double theFuzzyParam)
```

Perform partition operation.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Shapes to be intersected. |
    | theTools | Shapes to intersect theShapes. |

Note
:   Each compound from ListShapes and ListTools will be exploded in order to avoid possible intersection between shapes from this compound.

Parameters
:   |  |  |
    | --- | --- |
    | theLimit | Type of resulting shapes (corresponding to TopAbs_ShapeEnum). |
    | theKeepNonlimitShapes | if this parameter == 0, then only shapes of target type (equal to Limit) are kept in the result, else standalone shapes of lower dimension are kept also (if they exist). |
    | theFuzzyParam | The fuzzy tolerance to be used in the partition algorithm, if the value is positive. |

After implementation new version of PartitionAlgo (October 2006) other parameters are ignored by current functionality. They are kept in this function only for supporting old versions. Ignored parameters:

Parameters
:   |  |  |
    | --- | --- |
    | theKeepInside | Shapes, outside which the results will be deleted. Each shape from theKeepInside must belong to theShapes also. |
    | theRemoveInside | Shapes, inside which the results will be deleted. Each shape from theRemoveInside must belong to theShapes also. |
    | theRemoveWebs | If TRUE, perform Glue 3D algorithm. |
    | theMaterials | Material indices for each shape. Make sense, only if theRemoveWebs is TRUE. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shapes.

### MakePartitionNonSelfIntersectedShapeWithFuzzy()

```python
GEOM_Object MakePartitionNonSelfIntersectedShapeWithFuzzy(in ListOfGO theShapes, in ListOfGO theTools, in ListOfGO theKeepInside, in ListOfGO theRemoveInside, in short theLimit, in boolean theRemoveWebs, in ListOfLong theMaterials, in short theKeepNonlimitShapes, in boolean IsCheckSelfInte, in double theFuzzyParam)
```

Perform partition operation.

This method may be useful if it is needed to make a partition for a compound containing nonintersected shapes. Performance will be better since intersection between shapes from compound is not performed.

Description of all parameters as in previous method [MakePartition()](interfaceGEOM_1_1GEOM__IBooleanOperations.md#a4e60098799fbcf12b04d67ba1c3d9e3f). One additional parameter is provided:

Parameters
:   |  |  |
    | --- | --- |
    | IsCheckSelfInte | If TRUE, perform check self intersection of arguments before an operation. |
    | theFuzzyParam | The fuzzy tolerance to be used in the partition algorithm, if the value is positive. |

Note
:   Passed compounds (via ListShapes or via ListTools) have to consist of nonintersecting shapes.

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shapes.

### MakeHalfPartitionWithFuzzy()

```python
GEOM_Object MakeHalfPartitionWithFuzzy(in GEOM_Object theShape, in GEOM_Object thePlane, in double theFuzzyParam)
```

Perform partition of the Shape with the Plane.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be intersected. |
    | thePlane | Tool shape, to intersect theShape. |
    | theFuzzyParam | The fuzzy tolerance to be used in the partition algorithm, if the value is positive. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

Note
:   This operation is a shortcut to the more general [MakePartition](interfaceGEOM_1_1GEOM__IBooleanOperations.md#a4e60098799fbcf12b04d67ba1c3d9e3f) operation, where *theShape* specifies single "object" (shape being partitioned) and *thePlane* specifies single "tool" (intersector shape). Other parameters of [MakePartition](interfaceGEOM_1_1GEOM__IBooleanOperations.md#a4e60098799fbcf12b04d67ba1c3d9e3f) operation have default values:

    - *theLimit:* [GEOM::SHAPE](namespaceGEOM.md#a82a00e336c65dad4cc04b65563b26eb5a20f1b6e28cd67b9244936ffc716e5611) (shape limit corresponds to the type of *theShape*)
    - *theKeepNonlimitShapes:* 0
    - *theKeepInside*, *theRemoveInside*, *theRemoveWebs*, *theMaterials* (obsolete parameters): empty

See also
:   [MakePartition](interfaceGEOM_1_1GEOM__IBooleanOperations.md#a4e60098799fbcf12b04d67ba1c3d9e3f), [MakePartitionNonSelfIntersectedShape](interfaceGEOM_1_1GEOM__IBooleanOperations.md#a98a61962999c881cf13a9aeed2795c22)

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
