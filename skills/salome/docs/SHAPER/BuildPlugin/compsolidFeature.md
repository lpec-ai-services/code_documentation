<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/compsolidFeature.html -->

# CompSolid

Compsolid feature creates a compsolid using shapes already existing in other objects.

To create a compsolid in the active part:

1. select in the Main Menu *Build - > CompSolid* item or
2. click ![feature_compsolid.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/feature_compsolid.png) **CompSolid** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Compsolid.png)

Create a compsolid

Select one or several shapes in the viewer.

**Apply** button creates a compsolid.

**Cancel** button cancels the operation.

**TUI Command**:

model.addCompSolid(*Part_doc*, *Shapes*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes.

    Returns:
    :   Result object.

## Result

The result of the operation will be a compsolid created from the selected shapes:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreateCompsolid.png)

Result of the operation.

**See Also** a sample TUI Script of [Create CompSolid](TUI_compsolidFeature.md#tui-create-compsolid) operation.
