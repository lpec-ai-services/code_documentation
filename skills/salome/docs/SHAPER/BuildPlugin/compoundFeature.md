<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/compoundFeature.html -->

# Compound

Compound feature creates a compound using shapes already existing in other objects.

To create a compound in the active part:

1. select in the Main Menu *Build - > Compound* item or
2. click ![feature_compound.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/feature_compound.png) **Compound** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CompoundPanel.png)

Create a compound

Select one or several shapes in the viewer. The selected shapes can be of any type (vertex, edge, face, etc.)

**Apply** button creates a compound.

**Cancel** button cancels the operation.

**TUI Command**:

model.addCompound(*Part_doc*, *Shapes*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes.

    Returns:
    :   Result object.

## Result

The result of the operation will be a compound created from the selected shapes:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreateCompound.png)

Result of the operation.

**See Also** a sample TUI Script of [Create Compound](TUI_compoundFeature.md#tui-create-compound) operation.
