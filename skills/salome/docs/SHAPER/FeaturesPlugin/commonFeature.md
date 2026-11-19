<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/commonFeature.html -->

# Common

Common feature implements a Boolean operation for extraction of a common part from a set of selected shapes.

To perform a Common operation in the active part:

1. select in the Main Menu *Features - > Common* item or
2. click [![bool_common.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bool_common.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bool_common.png) **Common** button in the toolbar

There are 2 options for creation of a Common:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bool_common_simple.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bool_common_simple.png)

**Simple** common part between all selected objects.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bool_common_advanced.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bool_common_advanced.png)

**Advanced** common part for each object between this object and all tools.

---

## Simple

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/boolean_common_simple_property_panel.png)

**Simple**

- **Objects** contains a list of objects selected in the Object Browser or in the Viewer.
  If a subshape that belongs to a compsolid/compound was selected, other shapes of this compsolid/compound will be ignored.
- **Fuzzy Parameter** defines the additional tolerance value used to eliminate tiny results.
- **See preview** button shows a result of the operation.

**TUI Command**:

model.addCommon(*Part_doc*, *objects*, *fuzzy*)
:   Parameters:
    :   - **part** – The current part object
        - **list** – A list of objects.
        - **real** – Additional tolerance used to eliminate tiny results (optional).

    Returns:
    :   Created object

### Result

The Result of the operation will be a shape which is a common for all selected shapes:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedCommon.png)

**Common created**

**See Also** a sample TUI Script of [Create Common](TUI_commonFeature.md#tui-create-common) operation.

## Advanced

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/boolean_common_advanced_property_panel.png)

**Advanced**

- **Objects** contains a list of objects selected in the Object Browser or in the Viewer.
  If a subshape that belongs to a compsolid/compound was selected, other shapes of this compsolid/compound will be cut from
  other objects (to avoid self-intersection) and added to the result.
- **Tools** contains a list of objects selected in the Object Browser or in the Viewer, which will be intersected with tool objects.
  If a subshape that belongs to a compsolid/compound was selected, other shapes of this compsolid/compound will be ignored.
- **Fuzzy Parameter** defines the additional tolerance value used to eliminate tiny results.
- **See preview** button shows a result of the operation.

Any kind of shape is supported as an object or a tool of Common. Moreover, constructions planes can be selected as tools.

**TUI Command**:

model.addCommon(*Part_doc*, *objects*, *tools*, *fuzzy*)
:   Parameters:
    :   - **part** – The current part object
        - **list** – A list of objects.
        - **list** – A list of tools.
        - **real** – Additional tolerance used to eliminate tiny results (optional).

    Returns:
    :   Created object

### Result

For each selected object, the common part between this object and all tools will be found:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/boolean_common_result.png)

**Created common**

**See Also** a sample TUI Script of [Create Common](TUI_commonFeature.md#tui-create-common) operation.
