<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/horizontalDistFeature.html -->

# Horizontal distance constraint

Horizontal Distance constraint fixes the distance between two points along the horizontal axis.

The constraint can be defined between two points such as point object, line or arc end point, center of circle or arc.

To create a Horizontal Distance constraint in the active Sketch:

1. select in the Main Menu *Sketch - > Horizontal Distance* item or
2. click ![distance_h.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/distance_h.png) **Horizontal Distance** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/HorizontalDistance_panel.png)

Input fields:

- **First point** is the first point selected in the view;
- **Second point** is the second point selected in the view;
- **Value** is a distance between the objects, can be modified to set the desirable value;
- **Text location** is a position of the distance value label relating to extension line (in the view):
  :   ![location_left](https://docs.salome-platform.org/latest/gui/SHAPER/_images/location_left.png) **Left** inserts text to the left of the distance extension line;

      ![location_auto](https://docs.salome-platform.org/latest/gui/SHAPER/_images/location_automatic.png) **Automatic** inserts text in the middle of the distance extension line if it has enough length, otherwise - to the left;

      ![location_right](https://docs.salome-platform.org/latest/gui/SHAPER/_images/location_right.png) **Right** inserts text to the right of the distance extension line.

When both objects are selected, the horizontal distance value is displayed in the property panel and in the view.

When creating the constraint, after selection of two objects for the first time:

- drag the horizontal distance presentation in the view to the desired position and click once;
- set desirable horizontal distance value in the input field in the view and press **Enter** or just press **Enter** to keep the current distance.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/HorizontalDistance_field_view.png)

Horizontal Distance input in the view

**TUI Command**:

Sketch_1.setHorizontalDistance(*FirstObject*, *SecondObject*, *Value*)
:   Parameters:
    :   - **object** – An object 1.
        - **object** – An object 2.
        - **real** – Value.

    Returns:
    :   Result object.

## Result

Created Horizontal Distance appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/HorizontalDistance_res.png)

Horizontal Distance created

**See Also** a sample TUI Script of [Create Horizontal Distance constraint](TUI_hdistance.md#tui-create-hdistance) operation.
