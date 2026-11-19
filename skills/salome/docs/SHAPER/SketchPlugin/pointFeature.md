<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/pointFeature.html -->

# Point

Point feature creates a point in the current Sketch.

To add a new Point to the Sketch:

1. select in the Main Menu *Sketch - > Point* item or
2. click ![point.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Point.png) **Point** button in Sketch toolbar:

The following property panel appears:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Point_panel.png)

Point

Clicking in the view creates a point preview. If an existing object is clicked, a constraint for
the point will be created automatically.

The point coordinates are displayed in the property panel.

**TUI Command**:

Sketch_1.addPoint(*X*, *Y*)
:   Parameters:
    :   - **real** – X value.
        - **real** – Y value.

    Returns:
    :   Result object.

## Result

Created point appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Point_res.png)

Point created

**See Also** a sample TUI Script of [Create Sketch Point](TUI_pointFeature.md#tui-create-point) operation.
