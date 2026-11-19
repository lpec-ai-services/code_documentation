<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/lineFeature.html -->

# Line

Line feature creates a line segment by two points in the current Sketch.

To add a new Line to the Sketch:

1. select in the Main Menu *Sketch - > Line* item or
2. click ![line.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Line.png) **Line** button in Sketch toolbar:

The following property panel appears:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Line_panel.png)

Line

Pick 2 points (start and end) in the view to create a Line. If an existing object is clicked, a constraint for the point will be created automatically.

Start and end points coordinates are displayed in the property panel.

**TUI Command**:

Sketch_1.addLine(X1, Y1, X2, Y2)*
:   Parameters:
    :   - **real** – X1 value.
        - **real** – Y1 value.
        - **real** – X2 value.
        - **real** – Y2 value.

    Returns:
    :   Result object.

## Result

Created line appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Line_res.png)

Line created

**See Also** a sample TUI Script of [Create Sketch Line](TUI_lineFeature.md#tui-create-line) operation.
