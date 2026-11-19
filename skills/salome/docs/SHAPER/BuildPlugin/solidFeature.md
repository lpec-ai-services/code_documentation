<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/solidFeature.html -->

# Solid

Solid feature creates a solid using faces already existing in other objects.

To create a solid in the active part:

1. select in the Main Menu *Build - > Solid* item or
2. click ![feature_solid.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/feature_solid.png) **Solid** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Solid.png)

Create a solid

Select one or several faces in the viewer. The selected faces have to define a closed volume.

**Apply** button creates a solid.

**Cancel** button cancels the operation.

**TUI Command**:

model.addSolid(*Part_doc*, *Shapes*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes.

    Returns:
    :   Result object.

## Result

The result of the operation will be a solid created from the selected shapes:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreateSolid.png)

Result of the operation.

**See Also** a sample TUI Script of [Create Solid](TUI_solidFeature.md#tui-create-solid) operation.
