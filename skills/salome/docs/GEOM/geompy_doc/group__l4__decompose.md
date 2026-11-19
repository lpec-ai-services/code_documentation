<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l4__decompose.html -->

# Decompose objects geomBuilder Python module » All package methods, grouped by their purpose » Creating geometrical objects » Creating Advanced Geometrical Objects

## Detailed Description

## Function Documentation

### GetExistingSubObjects()

```python
def GetExistingSubObjects(self, theShape, theGroupsOnly = False)
```

Get all sub-shapes and groups of *theShape*, that were created already by any other methods.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Any shape. |
    | theGroupsOnly | If this parameter is TRUE, only groups will be returned, else all found sub-shapes and groups. |

Returns
:   List of existing sub-objects of *theShape*.

[Example](../tui_test_all_page.md#swig_all_decompose)

### GetGroups()

```python
def GetGroups(self, theShape)
```

Get all groups of *theShape*, that were created already by any other methods.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Any shape. |

Returns
:   List of existing groups of *theShape*.

[Example](../tui_test_all_page.md#swig_all_decompose)

### SubShapeAll()

```python
def SubShapeAll(self, aShape, aType, theName = None)
```

Explode a shape on sub-shapes of a given type.

If the shape itself matches the type, it is also returned.

Parameters
:   |  |  |
    | --- | --- |
    | aShape | Shape to be exploded. |
    | aType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of sub-shapes of type theShapeType, contained in theShape.

[Example](../tui_test_all_page.md#swig_all_decompose)

### SubShapeAllIDs()

```python
def SubShapeAllIDs(self, aShape, aType)
```

Explode a shape on sub-shapes of a given type.

Parameters
:   |  |  |
    | --- | --- |
    | aShape | Shape to be exploded. |
    | aType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |

Returns
:   List of IDs of sub-shapes.

[Example](../tui_test_all_page.md#swig_all_decompose)

### SubShape()

```python
def SubShape(self, aShape, aType, ListOfInd, theName = None)
```

Obtain a compound of sub-shapes of *aShape*, selected by their indices in list of all sub-shapes of type *aType*.

Each index is in range [1, Nb_Sub-Shapes_Of_Given_Type]

Parameters
:   |  |  |
    | --- | --- |
    | aShape | Shape to get sub-shape of. |
    | ListOfInd | List of sub-shapes indices. |
    | aType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   A compound of sub-shapes of aShape.

[Example](../tui_test_all_page.md#swig_all_decompose)

### SubShapeAllSortedCentres()

```python
def SubShapeAllSortedCentres(self, aShape, aType, theName = None)
```

Explode a shape on sub-shapes of a given type.

Sub-shapes will be sorted taking into account their gravity centers, to provide stable order of sub-shapes. Please see [Description of Sorting Shapes Algorithm](../sorting_shapes_page.md). If the shape itself matches the type, it is also returned.

Parameters
:   |  |  |
    | --- | --- |
    | aShape | Shape to be exploded. |
    | aType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of sub-shapes of type theShapeType, contained in theShape.

[Example](../tui_test_spanner_page.md#swig_SubShapeAllSorted)

### SubShapeAllSortedCentresIDs()

```python
def SubShapeAllSortedCentresIDs(self, aShape, aType)
```

Explode a shape on sub-shapes of a given type.

Sub-shapes will be sorted taking into account their gravity centers, to provide stable order of sub-shapes. Please see [Description of Sorting Shapes Algorithm](../sorting_shapes_page.md).

Parameters
:   |  |  |
    | --- | --- |
    | aShape | Shape to be exploded. |
    | aType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |

Returns
:   List of IDs of sub-shapes.

[Example](../tui_test_all_page.md#swig_all_decompose)

### SubShapeSortedCentres()

```python
def SubShapeSortedCentres(self, aShape, aType, ListOfInd, theName = None)
```

Obtain a compound of sub-shapes of *aShape*, selected by they indices in sorted list of all sub-shapes of type *aType*.

Please see [Description of Sorting Shapes Algorithm](../sorting_shapes_page.md). Each index is in range [1, Nb_Sub-Shapes_Of_Given_Type]

Parameters
:   |  |  |
    | --- | --- |
    | aShape | Shape to get sub-shape of. |
    | ListOfInd | List of sub-shapes indices. |
    | aType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   A compound of sub-shapes of aShape.

[Example](../tui_test_all_page.md#swig_all_decompose)

### ExtractShapes()

```python
def ExtractShapes(self, aShape, aType, isSorted = False, theName = None)
```

Extract shapes (excluding the main shape) of given type.

Parameters
:   |  |  |
    | --- | --- |
    | aShape | The shape. |
    | aType | The shape type (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | isSorted | Boolean flag to switch sorting on/off. Please see [Description of Sorting Shapes Algorithm](../sorting_shapes_page.md). |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of sub-shapes of type aType, contained in aShape.

[Example](../tui_test_all_page.md#swig_FilletChamfer)

### SubShapes()

```python
def SubShapes(self, aShape, anIDs, theName = None)
```

Get a set of sub-shapes defined by their unique IDs inside *aShape*

Parameters
:   |  |  |
    | --- | --- |
    | aShape | Main shape. |
    | anIDs | List of unique IDs of sub-shapes inside *aShape*. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), corresponding to found sub-shapes.

[Example](../tui_test_all_page.md#swig_all_decompose)

### GetSubShapeEdgeSorted()

```python
def GetSubShapeEdgeSorted(self, theShape, theStartPoint, theName = None)
```

Explode a shape into edges sorted in a row from a starting point.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | the shape to be exploded on edges. |
    | theStartPoint | the starting point. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) that is actually an ordered list of edges sorted in a row from a starting point.

[Example](../tui_test_all_page.md#swig_GetSubShapeEdgeSorted)

### GetSubShapesWithTolerance()

```python
def GetSubShapesWithTolerance(self, theShape, theShapeType, theCondition, theTolerance, theName = None)
```

Return the list of subshapes that satisfies a certain tolerance criterion.

The user defines the type of shapes to be returned, the condition and the tolerance value. The operation is defined for faces, edges and vertices only. E.g. for theShapeType FACE, theCondition [GEOM::CC_GT](namespaceGEOM.md#a52c7cde4c3a1dbddbfbae07edcd7072daa26140c48e027923532afe48e84391e4) and theTolerance 1.e-7 this method returns all faces of theShape that have tolerances greater then 1.e7.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | the shape to be exploded |
    | theShapeType | the type of sub-shapes to be returned (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)). Can have the values FACE, EDGE and VERTEX only. |
    | theCondition | the condition type (see [GEOM::comparison_condition](namespaceGEOM.md#a52c7cde4c3a1dbddbfbae07edcd7072d)). |
    | theTolerance | the tolerance filter. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   the list of shapes that satisfy the conditions.

[Example](../tui_test_all_page.md#swig_GetSubShapesWithTolerance)

### IsSubShapeBelongsTo()

```python
def IsSubShapeBelongsTo(self, aSubObject, anObject, aSubObjectIndex = 0, anObjectIndex = 0)
```

Check if the object is a sub-object of another [GEOM](namespaceGEOM.md) object.

Parameters
:   |  |  |
    | --- | --- |
    | aSubObject | Checked sub-object (or its parent object, in case if *theSubObjectIndex* is non-zero). |
    | anObject | An object that is checked for ownership (or its parent object, in case if *theObjectIndex* is non-zero). |
    | aSubObjectIndex | When non-zero, specifies a sub-shape index that identifies a sub-object within its parent specified via *theSubObject*. |
    | anObjectIndex | When non-zero, specifies a sub-shape index that identifies an object within its parent specified via *theObject*. |

Returns
:   TRUE, if the given object contains sub-object.

### MakeExtraction()

```python
def MakeExtraction(self, theShape, theListOfID, theName = None)
```

Perform extraction of sub-shapes from the main shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | the main shape |
    | theListOfID | the list of sub-shape IDs to be extracted from the main shape. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the shape without extracted sub-shapes.

[Example](../tui_test_all_page.md#swig_MakeExtraction)
