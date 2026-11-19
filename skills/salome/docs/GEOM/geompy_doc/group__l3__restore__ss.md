<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l3__restore__ss.html -->

# Restore presentation parameters and a tree of sub-shapes geomBuilder Python module » All package methods, grouped by their purpose » Transforming geometrical objects

## Detailed Description

## Function Documentation

### RestoreSubShapes()

```python
def RestoreSubShapes(self, theObject, theArgs = [], theFindMethod = GEOM.FSM_GetInPlace, theInheritFirstArg = False, theAddPrefix = True)
```

Publish sub-shapes, standing for arguments and sub-shapes of arguments To be used from python scripts out of [addToStudy()](group__l1__publish__data.md#ga2df168cac27bab65dfb96e04b84a120d) (non-default usage)

Parameters
:   |  |  |
    | --- | --- |
    | theObject | published [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), arguments of which will be published |
    | theArgs | list of [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), operation arguments to be published. If this list is empty, all operation arguments will be published |
    | theFindMethod | method to search sub-shapes, corresponding to arguments and their sub-shapes. Value from enumeration [GEOM.find_shape_method](namespaceGEOM.md#a4d764798e5127e57ed43bd2da68a613e). |
    | theInheritFirstArg | set properties of the first argument for *theObject*. Do not publish sub-shapes in place of arguments, but only in place of sub-shapes of the first argument, because the whole shape corresponds to the first argument. Mainly to be used after transformations, but it also can be useful after partition with one object shape, and some other operations, where only the first argument has to be considered. If theObject has only one argument shape, this flag is automatically considered as True, not regarding really passed value. |
    | theAddPrefix | add prefix "from_" to names of restored sub-shapes, and prefix "from_subshapes_of_" to names of partially restored sub-shapes. |

Returns
:   list of published sub-shapes

[Example](../tui_basic_operations_page.md#tui_restore_prs_params)

### RestoreGivenSubShapes()

```python
def RestoreGivenSubShapes(self, theObject, theArgs = [], theFindMethod = GEOM.FSM_GetInPlace, theInheritFirstArg = False, theAddPrefix = True)
```

Publish sub-shapes, standing for arguments and sub-shapes of arguments To be used from python scripts out of [addToStudy()](group__l1__publish__data.md#ga2df168cac27bab65dfb96e04b84a120d) (non-default usage)

Parameters
:   |  |  |
    | --- | --- |
    | theObject | published [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), arguments of which will be published |
    | theArgs | list of [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), operation arguments to be published. If this list is empty, all operation arguments will be published |
    | theFindMethod | method to search sub-shapes, corresponding to arguments and their sub-shapes. Value from enumeration [GEOM::find_shape_method](namespaceGEOM.md#a4d764798e5127e57ed43bd2da68a613e). |
    | theInheritFirstArg | set properties of the first argument for *theObject*. Do not publish sub-shapes in place of arguments, but only in place of sub-shapes of the first argument, because the whole shape corresponds to the first argument. Mainly to be used after transformations, but it also can be useful after partition with one object shape, and some other operations, where only the first argument has to be considered. If theObject has only one argument shape, this flag is automatically considered as True, not regarding really passed value. |
    | theAddPrefix | add prefix "from_" to names of restored sub-shapes, and prefix "from_subshapes_of_" to names of partially restored sub-shapes. |

Returns
:   list of published sub-shapes

[Example](../tui_basic_operations_page.md#tui_restore_prs_params)
