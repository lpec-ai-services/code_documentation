<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/pointCoordinatesFeature.html -->

# Point Coordinates

The **Points coordinates** feature displays the coordinates of a selected point.

The coordinates are displayed in the property panel.

**Apply** button does not generate any result and has the same effect as **Cancel** for this feature.

To display Point coordinates in the active part:

1. select in the Main Menu *Inspection - > Point coordinates* item or
2. click ![point_coord.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/point_coord.png) **Points coordinates** button in the toolbar

The coordinates can be displayed for a selected point in the property panel :

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/pointCoordinatesPropertyPanel.png)

Point coordinates

Input fields:

- Input field contains a point selected in 3D OCC viewer or object browser.

Note, the coordinates displayed can be selected.

**TUI Command**:

model.getPointCoordinates(*Part_doc*, *point*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – A point in format *model.selection(“VERTEX”, shape)*.

    Returns:
    :   list of coordinates.

**See Also** a sample TUI Script of [Get point coordinates](TUI_pointCoordinates.md#tui-point-coordinates) operation.
