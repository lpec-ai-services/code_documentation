<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/wireFeature.html -->

# Wire

Wire feature creates a wire using edges already existing in other objects.

To create a wire in the active part:

1. select in the Main Menu *Build - > Wire* item or
2. click ![feature_wire.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/feature_wire.png) **Wire** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Wire.png)

Create a wire

Select one or several edges in the viewer. For automatic selection of a closed contour starting from the selected edge it is necessary to press **Add contour** button.

Moreover, the full sketch can be selected. In this case, a set of wires is composed using edges of the sketch.
Checkbox **Compute intersections** forces to split sketch edges in the points of intersection.

**Apply** button creates a wire.

**Cancel** button cancels the operation.

**TUI Command**:

model.addWire(*Part_doc*, *Shapes*, *Intersect*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes.
        - **bool** – Split edges by intersection points. False by default.

    Returns:
    :   Result object.

## Result

The result of the operation will be a wire created from the selected shapes:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreateWire.png)

Result of the operation.

**See Also** a sample TUI Script of [Create Wire](TUI_wireFeature.md#tui-create-wire) operation.
