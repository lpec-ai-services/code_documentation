<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l3__basic__op.html -->

# Basic Operations geomBuilder Python module » All package methods, grouped by their purpose » Transforming geometrical objects

## Detailed Description

## Function Documentation

### MakePartition()

```python
def MakePartition(self, ListShapes, ListTools = [], ListKeepInside = [], ListRemoveInside = [], Limit = ShapeType ["AUTO"], RemoveWebs = 0, ListMaterials = [], KeepNonlimitShapes = 0, theName = None, theFuzzyParam = -1)
```

Perform partition operation.

Parameters
:   |  |  |
    | --- | --- |
    | ListShapes | Shapes to be intersected. |
    | ListTools | Shapes to intersect theShapes. |
    | Limit | Type of resulting shapes (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)).  If this parameter is set to -1 ("Auto"), most appropriate shape limit type will be detected automatically. |
    | KeepNonlimitShapes | if this parameter == 0, then only shapes of target type (equal to Limit) are kept in the result, else standalone shapes of lower dimension are kept also (if they exist). |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |
    | theFuzzyParam | The fuzzy parameter to be used for the partition operation. If the value is not positive, no fuzzy tolerance will be considered for the partition operation. |

Note
:   Each compound from ListShapes and ListTools will be exploded in order to avoid possible intersection between shapes from this compound.

After implementation new version of PartitionAlgo (October 2006) other parameters are ignored by current functionality. They are kept in this function only for support old versions.

Parameters
:   |  |  |
    | --- | --- |
    | ListKeepInside | Shapes, outside which the results will be deleted. Each shape from theKeepInside must belong to theShapes also. |
    | ListRemoveInside | Shapes, inside which the results will be deleted. Each shape from theRemoveInside must belong to theShapes also. |
    | RemoveWebs | If TRUE, perform Glue 3D algorithm. |
    | ListMaterials | Material indices for each shape. Make sense, only if theRemoveWebs is TRUE. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shapes.

[Example](../tui_basic_operations_page.md#tui_partition)

### MakePartitionNonSelfIntersectedShape()

```python
def MakePartitionNonSelfIntersectedShape(self, ListShapes, ListTools = [], ListKeepInside = [], ListRemoveInside = [], Limit = ShapeType ["AUTO"], RemoveWebs = 0, ListMaterials = [], KeepNonlimitShapes = 0, checkSelfInte = False, theName = None, theFuzzyParam = -1)
```

Perform partition operation.

This method may be useful if it is needed to make a partition for compound contains nonintersected shapes. Performance will be better since intersection between shapes from compound is not performed.

Description of all parameters as in previous method [MakePartition()](group__l3__basic__op.md#ga4a2f396e7ccee76f0a92ac3b53eebfeb). One additional parameter is provided:

Parameters
:   |  |  |
    | --- | --- |
    | checkSelfInte | The flag that tells if the arguments should be checked for self-intersection prior to the operation. |
    | theFuzzyParam | The fuzzy parameter to be used for the partition operation. If the value is not positive, no fuzzy tolerance will be considered for the partition operation. |

Note
:   This algorithm doesn't find all types of self-intersections. It is tuned to detect vertex/vertex, vertex/edge, edge/edge, vertex/face and edge/face intersections. Face/face intersections detection is switched off as it is a time-consuming operation that gives an impact on performance. To find all self-intersections please use [CheckSelfIntersections()](group__l2__measure.md#gad7e7691bc06cb1f44dd1f308b899490f) method.
:   Passed compounds (via ListShapes or via ListTools) have to consist of nonintersecting shapes.

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shapes.

Example

### Partition()

```python
def Partition(self, ListShapes, ListTools = [], ListKeepInside = [], ListRemoveInside = [], Limit = ShapeType ["AUTO"], RemoveWebs = 0, ListMaterials = [], KeepNonlimitShapes = 0, theName = None, theFuzzyParam = -1)
```

See method [MakePartition()](group__l3__basic__op.md#ga4a2f396e7ccee76f0a92ac3b53eebfeb) for more information.

[Example 1](../tui_basic_operations_page.md#tui_partition)   
[Example 2](../tui_test_others_page.md#swig_Partition)

### MakeHalfPartition()

```python
def MakeHalfPartition(self, theShape, thePlane, theName = None, theFuzzyParam = -1)
```

Perform partition of the Shape with the Plane.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be intersected. |
    | thePlane | Tool shape, to intersect theShape. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |
    | theFuzzyParam | The fuzzy parameter to be used for the partition operation. If the value is not positive, no fuzzy tolerance will be considered for the partition operation. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

Note
:   This operation is a shortcut to the more general [MakePartition](group__l3__basic__op.md#ga4a2f396e7ccee76f0a92ac3b53eebfeb) operation, where *theShape* specifies single "object" (shape being partitioned) and *thePlane* specifies single "tool" (intersector shape). Other parameters of [MakePartition](group__l3__basic__op.md#ga4a2f396e7ccee76f0a92ac3b53eebfeb) operation have default values:

    - *Limit:* [GEOM::SHAPE](namespaceGEOM.md#a82a00e336c65dad4cc04b65563b26eb5a20f1b6e28cd67b9244936ffc716e5611) (shape limit corresponds to the type of *theShape*)
    - *KeepNonlimitShapes:* 0
    - *KeepInside*, *RemoveInside*, *RemoveWebs*, *Materials* (obsolete parameters): empty
:   I.e. the following two operations are equivalent:
    ```python
    Result = geompy.MakeHalfPartition(Object, Plane)
    Result = geompy.MakePartition([Object], [Plane])
    ```

See also
:   [MakePartition](group__l3__basic__op.md#ga4a2f396e7ccee76f0a92ac3b53eebfeb), [MakePartitionNonSelfIntersectedShape](group__l3__basic__op.md#ga864d4dc75b64f919b2a1632ee03cd04b)

[Example](../tui_basic_operations_page.md#tui_partition)

### Archimede()

```python
def Archimede(self, theShape, theWeight, theWaterDensity, theMeshDeflection, theName = None)
```

Perform an Archimde operation on the given shape with given parameters.

The object presenting the resulting face is returned.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be put in water. |
    | theWeight | Weight of the shape. |
    | theWaterDensity | Density of the water. |
    | theMeshDeflection | Deflection of the mesh, using to compute the section. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing a section of *theShape* by a plane, corresponding to water level.

[Example](../tui_basic_operations_page.md#tui_archimede)
