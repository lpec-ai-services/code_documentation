<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/angleFeature.html -->

# Angle constraint

Angle constraint fixes the angle between two lines.

Angle between two lines is seen as an angle between two vectors.

Each line is treated as a vector with start and end points equal to those of the line.

To create an Angle constraint in the active Sketch:

1. select in the Main Menu *Sketch - > Angle* item or
2. click ![angle_constr.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/angle_constr.png) **Angle** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Angle_panel.png)

Input fields:

- **Line 1** is the first line selected in the view;
- **Line 2** is the second line selected in the view;
- **Value** is an angle between the lines, can be modified to set the desirable value;
- **Angle type** is a type of angle measurement:
  :   ![angle_direct](https://docs.salome-platform.org/latest/gui/SHAPER/_images/angle_direct.png) **Direct** is the least angle between two lines;

      ![angle_complement](https://docs.salome-platform.org/latest/gui/SHAPER/_images/angle_complementary.png) **Complementary** is 180°- Direct angle between two lines;

      ![angle_backward](https://docs.salome-platform.org/latest/gui/SHAPER/_images/angle_backward.png) **Backward** is 360°- Direct angle between two lines.
- **Text location** is the position of the angle value label relatively to the angle line (in the view):
  :   ![loc_left](https://docs.salome-platform.org/latest/gui/SHAPER/_images/location_left.png) **Left** inserts text to the left of the angle line;

      ![loc_auto](https://docs.salome-platform.org/latest/gui/SHAPER/_images/location_automatic.png) **Automatic** inserts text it the middle of the angle line if it has enough length, otherwise - to the left;

      ![loc_right](https://docs.salome-platform.org/latest/gui/SHAPER/_images/location_right.png) **Right** inserts text to the right of the angle line.

When both lines are selected, the angle value is displayed in the property panel and in the view.

When creating the constraint, after selection of two lines at the first time:

- drag the angle presentation in the view to the desired position and click once;
- set desirable angle value in the input field in the view and press **Enter** or just press **Enter** to keep the current angle

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Angle_field_view.png)

Angle input in the view

**TUI Commands**:

Sketch_1.setAngle(*Line1*, *Line2*, *Value*)

Sketch_1.setAngleComplementary(*Line1*, *Line2*, *Value*)

Sketch_1.setAngleBackward(*Line1*, *Line2*, *Value*)
:   Parameters:
    :   - **object** – Line 1.
        - **object** – Line 2.
        - **real** – Value.

    Returns:
    :   Result object.

## Result

Created Angle appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Angle_res.png)

Angle created

**See Also** a sample TUI Script of [Create Angle constraint](TUI_angle.md#tui-create-angle) operation.
