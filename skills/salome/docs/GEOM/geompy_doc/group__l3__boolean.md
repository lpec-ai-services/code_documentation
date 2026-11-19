<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l3__boolean.html -->

# Boolean Operations geomBuilder Python module » All package methods, grouped by their purpose » Transforming geometrical objects

## Detailed Description

## Function Documentation

### MakeBoolean()

```python
def MakeBoolean(self, theShape1, theShape2, theOperation, checkSelfInte = False, theName = None, theFuzzyParam = -1)
```

Perform one of boolean operations on two given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1 | First argument for boolean operation. |
    | theShape2 | Second argument for boolean operation. |
    | theOperation | Indicates the operation to be done:  1 - Common, 2 - Cut, 3 - Fuse, 4 - Section. |
    | checkSelfInte | The flag that tells if the arguments should be checked for self-intersection prior to the operation. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |
    | theFuzzyParam | The fuzzy parameter to be used for the boolean operation. If the value is not positive, no fuzzy tolerance will be considered for the boolean operation. |

Note
:   This algorithm doesn't find all types of self-intersections. It is tuned to detect vertex/vertex, vertex/edge, edge/edge, vertex/face and edge/face intersections. Face/face intersections detection is switched off as it is a time-consuming operation that gives an impact on performance. To find all self-intersections please use [CheckSelfIntersections()](group__l2__measure.md#gad7e7691bc06cb1f44dd1f308b899490f) method.

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example](../tui_boolean_operations_page.md#tui_fuse)

### MakeCommon()

```python
def MakeCommon(self, theShape1, theShape2, checkSelfInte = False, theName = None, theFuzzyParam = -1)
```

Perform Common boolean operation on two given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1 | First argument for boolean operation. |
    | theShape2 | Second argument for boolean operation. |
    | checkSelfInte | The flag that tells if the arguments should be checked for self-intersection prior to the operation. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |
    | theFuzzyParam | The fuzzy parameter to be used for the boolean operation. If the value is not positive, no fuzzy tolerance will be considered for the boolean operation. |

Note
:   This algorithm doesn't find all types of self-intersections. It is tuned to detect vertex/vertex, vertex/edge, edge/edge, vertex/face and edge/face intersections. Face/face intersections detection is switched off as it is a time-consuming operation that gives an impact on performance. To find all self-intersections please use [CheckSelfIntersections()](group__l2__measure.md#gad7e7691bc06cb1f44dd1f308b899490f) method.

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example 1](../tui_boolean_operations_page.md#tui_common)   
[Example 2](../tui_test_others_page.md#swig_MakeCommon)

### MakeCut()

```python
def MakeCut(self, theShape1, theShape2, checkSelfInte = False, theName = None, theFuzzyParam = -1)
```

Perform Cut boolean operation on two given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1 | First argument for boolean operation. |
    | theShape2 | Second argument for boolean operation. |
    | checkSelfInte | The flag that tells if the arguments should be checked for self-intersection prior to the operation. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |
    | theFuzzyParam | The fuzzy parameter to be used for the boolean operation. If the value is not positive, no fuzzy tolerance will be considered for the boolean operation. |

Note
:   This algorithm doesn't find all types of self-intersections. It is tuned to detect vertex/vertex, vertex/edge, edge/edge, vertex/face and edge/face intersections. Face/face intersections detection is switched off as it is a time-consuming operation that gives an impact on performance. To find all self-intersections please use [CheckSelfIntersections()](group__l2__measure.md#gad7e7691bc06cb1f44dd1f308b899490f) method.

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example 1](../tui_boolean_operations_page.md#tui_cut)   
[Example 2](../tui_test_others_page.md#swig_MakeCommon)

### MakeFuse()

```python
def MakeFuse(self, theShape1, theShape2, checkSelfInte = False, rmExtraEdges = False, theName = None, theFuzzyParam = -1)
```

Perform Fuse boolean operation on two given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1 | First argument for boolean operation. |
    | theShape2 | Second argument for boolean operation. |
    | checkSelfInte | The flag that tells if the arguments should be checked for self-intersection prior to the operation. |
    | rmExtraEdges | The flag that tells if Remove Extra Edges operation should be performed during the operation. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |
    | theFuzzyParam | The fuzzy parameter to be used for the boolean operation. If the value is not positive, no fuzzy tolerance will be considered for the boolean operation. |

Note
:   This algorithm doesn't find all types of self-intersections. It is tuned to detect vertex/vertex, vertex/edge, edge/edge, vertex/face and edge/face intersections. Face/face intersections detection is switched off as it is a time-consuming operation that gives an impact on performance. To find all self-intersections please use [CheckSelfIntersections()](group__l2__measure.md#gad7e7691bc06cb1f44dd1f308b899490f) method.

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example 1](../tui_boolean_operations_page.md#tui_fuse)   
[Example 2](../tui_test_others_page.md#swig_MakeCommon)

### MakeSection()

```python
def MakeSection(self, theShape1, theShape2, checkSelfInte = False, theName = None, theFuzzyParam = -1)
```

Perform Section boolean operation on two given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1 | First argument for boolean operation. |
    | theShape2 | Second argument for boolean operation. |
    | checkSelfInte | The flag that tells if the arguments should be checked for self-intersection prior to the operation. If a self-intersection detected the operation fails. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |
    | theFuzzyParam | The fuzzy parameter to be used for the boolean operation. If the value is not positive, no fuzzy tolerance will be considered for the boolean operation. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example 1](../tui_boolean_operations_page.md#tui_section)   
[Example 2](../tui_test_others_page.md#swig_MakeCommon)

### MakeFuseList()

```python
def MakeFuseList(self, theShapesList, checkSelfInte = False, rmExtraEdges = False, theName = None, theFuzzyParam = -1)
```

Perform Fuse boolean operation on the list of shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShapesList | Shapes to be fused. |
    | checkSelfInte | The flag that tells if the arguments should be checked for self-intersection prior to the operation. |
    | rmExtraEdges | The flag that tells if Remove Extra Edges operation should be performed during the operation. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |
    | theFuzzyParam | The fuzzy parameter to be used for the boolean operation. If the value is not positive, no fuzzy tolerance will be considered for the boolean operation. |

Note
:   This algorithm doesn't find all types of self-intersections. It is tuned to detect vertex/vertex, vertex/edge, edge/edge, vertex/face and edge/face intersections. Face/face intersections detection is switched off as it is a time-consuming operation that gives an impact on performance. To find all self-intersections please use [CheckSelfIntersections()](group__l2__measure.md#gad7e7691bc06cb1f44dd1f308b899490f) method.

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example 1](../tui_boolean_operations_page.md#tui_fuse)   
[Example 2](../tui_test_others_page.md#swig_MakeCommon)

### MakeCommonList()

```python
def MakeCommonList(self, theShapesList, checkSelfInte = False, theName = None, theFuzzyParam = -1)
```

Perform Common boolean operation on the list of shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShapesList | Shapes for Common operation. |
    | checkSelfInte | The flag that tells if the arguments should be checked for self-intersection prior to the operation. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |
    | theFuzzyParam | The fuzzy parameter to be used for the boolean operation. If the value is not positive, no fuzzy tolerance will be considered for the boolean operation. |

Note
:   This algorithm doesn't find all types of self-intersections. It is tuned to detect vertex/vertex, vertex/edge, edge/edge, vertex/face and edge/face intersections. Face/face intersections detection is switched off as it is a time-consuming operation that gives an impact on performance. To find all self-intersections please use [CheckSelfIntersections()](group__l2__measure.md#gad7e7691bc06cb1f44dd1f308b899490f) method.

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example 1](../tui_boolean_operations_page.md#tui_common)   
[Example 2](../tui_test_others_page.md#swig_MakeCommon)

### MakeCutList()

```python
def MakeCutList(self, theMainShape, theShapesList, checkSelfInte = False, theName = None, theFuzzyParam = -1)
```

Perform Cut boolean operation on one object and the list of tools.

Parameters
:   |  |  |
    | --- | --- |
    | theMainShape | The object of the operation. |
    | theShapesList | The list of tools of the operation. |
    | checkSelfInte | The flag that tells if the arguments should be checked for self-intersection prior to the operation. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |
    | theFuzzyParam | The fuzzy parameter to be used for the boolean operation. If the value is not positive, no fuzzy tolerance will be considered for the boolean operation. |

Note
:   This algorithm doesn't find all types of self-intersections. It is tuned to detect vertex/vertex, vertex/edge, edge/edge, vertex/face and edge/face intersections. Face/face intersections detection is switched off as it is a time-consuming operation that gives an impact on performance. To find all self-intersections please use [CheckSelfIntersections()](group__l2__measure.md#gad7e7691bc06cb1f44dd1f308b899490f) method.

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example 1](../tui_boolean_operations_page.md#tui_cut)   
[Example 2](../tui_test_others_page.md#swig_MakeCommon)
