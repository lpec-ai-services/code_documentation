<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/verticalFeature.html -->

# Vertical constraint

Vertical constraint fixes lines as parallel to the vertical axis.

To create a Vertical constraint in the active Sketch:

1. select in the Main Menu *Sketch - > Vertical* item or
2. click ![vertical.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Vertical.png) **Vertical** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Vertical_panel.png)

Input fields:

- **Line** is the line selected in the view.

After the line is selected it becomes parallel to the vertical axis in the view.

**V** sign is added above the line.

**TUI Command**:

Sketch_1.setVertical(*LineObject*)
:   Parameters:
    :   **object** – A line.

    Returns:
    :   Result object.

## Result

Created Vertical constraint appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Vertical_res.png)

Vertical constraint created

**See Also** a sample TUI Script of [Create Vertical constraint](TUI_vertical.md#tui-create-vertical) operation.
