<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/perpendicularFeature.html -->

# Perpendicular constraint

Perpendicular constraint fixes two lines at 90 degrees to one another.
For a line and a circle/arc the perpendicular constraint fixes the center of circle/arc to be on a line.

To create a Perpendicular constraint in the active Sketch:

1. select in the Main Menu *Sketch - > Perpendicular* item or
2. click ![Perpendicular.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Perpendicular.png) **Perpendicular** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Perpendicular_panel.png)

Input fields:

- **First object** is the first line, circle or arc selected in the view.
- **Second object** is the second line, circle or arc selected in the view.

After the objects are selected, a special sign will be added to each of them in the view.

If one of selected objects is circular, then another has to be a straight line.

**TUI Command**:

Sketch_1.setPerpendicular(*Line1*, *Line2*)
:   Parameters:
    :   - **object** – Line 1.
        - **object** – Line 2.

    Returns:
    :   Result object.

## Result

Created Perpendicular constraint appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Perpendicular_res.png)

Created perpendicular constraint

**See Also** a sample TUI Script of [Create Perpendicular constraint](TUI_perpendicular.md#tui-create-perpendicular) operation.
