<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/polylineFeature.html -->

# Polyline

Polyline feature creates a wire.

To create a Polyline in the active part:

1. select in the Main Menu *Build - > Polyline* item or
2. click ![feature_polyline.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/feature_polyline.png) **Polyline** button in the toolbar

The following property panel appears.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Polyline.png)

Polyline property panel

Input fields:

- **Points and vertices** panel contains a list of points and vertices selected in 3D OCC viewer. The Polyline consequently connects points;
- **Closed** check-box turns on/off connection of the start and end points to make polyline closed/opened.

**TUI Commands**:

model.addPolyline3D(*Part_1_doc*, *Polyline_objects*, *Key*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – list of vertices selected in format *model.selection(“VERTEX”, “Point”)*.
        - **boolean** – Is closed.

    Returns:
    :   Result object.

## Result

The result of the operation is a closed or open Polyline.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatePolyline.png)

Polyline

**See Also** a sample TUI Script of [Create Polyline](TUI_polylineFeature.md#tui-create-polyline) operation.
