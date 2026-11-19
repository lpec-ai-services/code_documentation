<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/rotationFeature.html -->

# Angular copy

Angular copy operation creates one or multiple copies of the sketch entities by rotation relative to a specified center point.

To create an Angular copy in the active Sketch:

1. select in the Main Menu *Sketch - > Angular copy* item or
2. click ![rotate.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/rotate.png) **Angular copy** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Rotation_panel.png)

Angular copy

Input fields:

- **Segments** is the list of segments (lines, circles, arcs) selected in the view;
- **Center of rotation** is the center point selected in the view;
- **Full angle/Single angle** option:
  :   ![full_angle](https://docs.salome-platform.org/latest/gui/SHAPER/_images/angle_up_full_32x32.png) **Full angle**: angle step of rotation is equal to the defined angle divided by the number of copies (total number minus one).

      ![single_angle](https://docs.salome-platform.org/latest/gui/SHAPER/_images/angle_up_32x32.png) **Single angle**: angle step of rotation is equal to the defined angle.
- **Angle** is the angle of rotation.
- **Reversed** defines rotation direction. If checked - in a clockwise direction, otherwise - in a counterclockwise direction.
- **Total number of objects** is the total number of objects including the original one.

**TUI Command**:

Sketch_1.addRotation(*Objects*, *CenterPoint*, *Angle*, *NumberOfObjects*, *FullValue*, *Reversed*)
:   Parameters:
    :   - **list** – A list of objects.
        - **object** – Center point.
        - **real** – Angle.
        - **integer** – Number of objects.
        - **boolean** – Full value flag.
        - **boolean** – Reversed flag.

    Returns:
    :   Result object.

## Result

Created Angular copy appears in the view.

The original and an angular copy objects are marked with a special sign.

Copy objects are drawn with a thinner line.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Rotation_res.png)

Created angular copy

**See Also** a sample TUI Script of [Create Angular copy](TUI_rotation.md#tui-create-rotation) operation.
