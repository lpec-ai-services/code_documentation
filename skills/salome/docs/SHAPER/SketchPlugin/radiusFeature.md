<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/radiusFeature.html -->

# Radius constraint

Radius constraint fixes the radius of circle or arc.

To create a Radius constraint in the active Sketch:

1. select in the Main Menu *Sketch - > Radius* item or
2. click ![radius_constr.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/radius_constr.png) **Radius** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Radius_panel.png)

Input fields:

- **Circle or Arc** is the circle or arc selected in the view;
- **Value** is a radius of the selected object, could be modified to set the desirable value
- **Text location** is a position of the radius value label relating to extension line (in the view)
  :   ![loc_left](https://docs.salome-platform.org/latest/gui/SHAPER/_images/location_left.png) **Left** inserts text at the left of the radius extension line.

      ![loc_auto](https://docs.salome-platform.org/latest/gui/SHAPER/_images/location_automatic.png) **Automatic** inserts text at the middle of the radius extension line if it has enough length, otherwise - to the left.

      ![loc_right](https://docs.salome-platform.org/latest/gui/SHAPER/_images/location_right.png) **Right** inserts text to the right of the radius extension line.

When circle or arc is selected, the radius value is displayed in the property panel and in the view.

When creating the constraint, after selection of the circle or arc at the first time :

- drag the radius presentation in the view to the desired position and click once;
- set desirable radius value in the input field in the view and press **Enter** or just press **Enter** to keep the current radius.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Radius_field_view.png)

Radius input in the view

**TUI Command**:

Sketch_1.setRadius(*CircleOrArc*, *Value*)
:   Parameters:
    :   - **object** – Circle or arc.
        - **real** – Radius.

    Returns:
    :   Result object.

## Result

Created Radius appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Radius_res.png)

Radius created

**See Also** a sample TUI Script of [Create Radius constraint](TUI_radius.md#tui-create-radius) operation.
