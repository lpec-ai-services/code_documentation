<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/fillingFeature.html -->

# Filling

Filling feature creates one or several faces using shapes already existing in other objects.

To create a filling in the active part:

1. select in the Main Menu *Build - > Filling* item or
2. click ![feature_filling.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/feature_filling.png) **Filling** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Filling.png)

Create a filling

Select two or more edges in the viewer.

**Advanced options** manage filling process.

**Apply** button creates a filling.

**Cancel** button cancels the operation.

**TUI Command**:

model.addFilling(*Part_doc*, *Edges*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes.

    Returns:
    :   Result object.

## Result

The result of the operation will be a set of faces created from the selected shapes:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreateFilling.png)

Result of the operation.

**See Also** a sample TUI Script of [Create Filling](TUI_fillingFeature.md#tui-create-filling) operation.
