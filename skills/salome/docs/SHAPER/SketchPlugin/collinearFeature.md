<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/collinearFeature.html -->

# Collinear constraint

Collinear constraint forces lines to be collinear.

To create a Collinear constraint in the active Sketch:

1. select in the Main Menu *Sketch - > Collinear* item or
2. click ![collinear.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/collinear.png) **Collinear** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Collinear_panel.png)

Input fields:

- **First line** is the first line selected in the view.
- **Second line** is the second line selected in the view.

After the lines are selected, they are translated to become collinear.

The lines are marked with a special sign.

**TUI Command**:

Sketch_1.setCollinear(*Line1*, *Line2*)
:   Parameters:
    :   - **object** – First object.
        - **object** – Second object.

    Returns:
    :   Result object.

## Result

Created Collinear constraint appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Collinear_res.png)

Created collinear constraint

**See Also** a sample TUI Script of [Create Collinear constraint](TUI_collinear.md#tui-create-collinear) operation.
