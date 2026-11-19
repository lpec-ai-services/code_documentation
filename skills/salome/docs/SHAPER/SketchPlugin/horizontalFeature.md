<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/horizontalFeature.html -->

# Horizontal constraint

Horizontal constraint fixes lines as parallel to the horizontal axis.

To create a Horizontal constraint in the active Sketch:

1. select in the Main Menu *Sketch - > Horizontal* item or
2. click ![horisontal.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/horisontal.png) **Horizontal** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Horizontal_panel.png)

Input fields:

- **Line** is the line selected in the view.

After the line is selected it becomes parallel to the horizontal axis in the view.

**H** sign is added above the line.

**TUI Command**:

Sketch_1.setHorizontal(*LineObject*)
:   Parameters:
    :   **object** – A line.

    Returns:
    :   Result object.

## Result

Created Horizontal constraint appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Horizontal_res.png)

Horizontal constraint created

**See Also** a sample TUI Script of [Create Horizontal constraint](TUI_horizontal.md#tui-create-horizontal) operation.
