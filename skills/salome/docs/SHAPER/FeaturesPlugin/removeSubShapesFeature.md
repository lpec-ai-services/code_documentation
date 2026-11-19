<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/removeSubShapesFeature.html -->

# Remove Sub-Shapes

Remove Sub-Shapes allows removing sub shapes from wires, shells, compsolids and compounds.

To Remove Sub-Shapes in the active part:

1. select in the Main Menu *Features - > Remove Sub-Shapes* item or
2. click ![remove_subshapes_btn.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/remove_subshapes_btn.png) **Remove Sub-Shapes** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/RemoveSubShapes.png)

Remove Sub-Shapes

- **Shape** shape from which sub-shapes should be removed. Only wires, shells, compsolids or compounds are allowed for selection.

There are 2 options for removing sub-shapes:

![by_removing](https://docs.salome-platform.org/latest/gui/SHAPER/_images/remove_subshapes_32x32.png) **By removing** allows selecting sub-shapes to be removed.

- **Sub-Shapes to remove** the list of sub-shapes which should be removed.

**TUI Command**:

model.addRemoveSubShapes(*Part_1_doc*, *object*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – The object.

    Returns:
    :   Created object.

Remove_SubShapes_1.setSubShapesToRemove(*subShapes*)
:   Parameters:
    :   **list** – A list of objects.

![by_keeping](https://docs.salome-platform.org/latest/gui/SHAPER/_images/keep_subshapes_32x32.png) **By keeping** allows select sub-shapes to be kept.

- **Sub-Shapes to keep** the list of sub-shapes which should be kept.

**TUI Command**:

model.addRemoveSubShapes(*Part_1_doc*, *object*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – The object.

    Returns:
    :   Created object.

Remove_SubShapes_1.setSubShapesToKeep(*subShapes*)
:   Parameters:
    :   **list** – A list of sub-shapes to keep.

## Result

The Result of the operation will be a shape without removed sub-shapes:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/remove_subshapes_result.png)

**Remove Sub-Shapes**

**See Also** a sample TUI Script of [Remove Sub-Shapes](TUI_removeSubShapesFeature.md#tui-create-remove-subshapes) operation.
