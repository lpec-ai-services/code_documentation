<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/distanceFeature.html -->

# Distance constraint

Distance constraint fixes the distance between two objects.

The constraint can be defined between such objects as point, line, line or arc end point, center of circle or arc.

To create a Distance constraint in the active Sketch:

1. select in the Main Menu *Sketch - > Distance* item or
2. click ![distance.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Distance.png) **Distance** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Distance_panel.png)

Input fields:

- **First object** is the first object selected in the view;
- **Second object** is the second object selected in the view;
- **Value** is a distance between the objects, can be modified to set the desirable value;
- **Text location** is a position of the distance value label relating to extension line (in the view):
  :   ![location_left](https://docs.salome-platform.org/latest/gui/SHAPER/_images/location_left.png) **Left** inserts text to the left of the distance extension line;

      ![location_auto](https://docs.salome-platform.org/latest/gui/SHAPER/_images/location_automatic.png) **Automatic** inserts text in the middle of the distance extension line if it has enough length, otherwise - to the left;

      ![location_right](https://docs.salome-platform.org/latest/gui/SHAPER/_images/location_right.png) **Right** inserts text to the right of the distance extension line;
- **Keep orientation** fixes the relative position between selected objects.

When both objects are selected, the distance value is displayed in the property panel and in the view.

When creating a constraint after selection of two objects for the first time:

- drag the distance presentation in the view to the desired position and click once;
- set the desirable distance value in the input field and press **Enter** or just press **Enter** to keep the current distance.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Distance_field_view.png)

Distance input in the view

**TUI Command**:

Sketch_1.setDistance(*FirstObject*, *SecondObject*, *Value*, *KeepOrientation*)
:   Parameters:
    :   - **object** – First object.
        - **object** – Second object.
        - **real** – Value.
        - **boolean** – Keep orientation flag.

    Returns:
    :   Result object.

## Result

Created Distance appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Distance_res.png)

Distance created

**See Also** a sample TUI Script of [Create Distance constraint](TUI_distance.md#tui-create-distance) operation.
