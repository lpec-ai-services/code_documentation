<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/tangentFeature.html -->

# Tangent constraint

Tangent constraint fixes a circle (or an arc) and a line so that a line is tangent to a circle (or an arc).

To create a Tangent in the active Sketch:

1. select in the Main Menu *Sketch - > Tangent* item or
2. click ![tangent.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Tangent.png) **Tangent** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Tangent_panel.png)

Input fields:

- **First object** is a line, a circle or an arc selected in the view.
- **Second object** is a line, a circle or an arc selected in the view.

Note that one of two objects should be a line.

After the objects are selected, a special sign will be added close to the tangency point in the view.

**TUI Command**:

Sketch_1.setTangent(*Line*, *CircleOrArc*)
:   Parameters:
    :   - **object** – A line.
        - **object** – A circle or an arc.

    Returns:
    :   Result object.

## Result

Created Tangent constraint appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Tangent_res.png)

Created tangent constraint

**See Also** a sample TUI Script of [Create Tangent constraint](TUI_tangent.md#tui-create-tangent) operation.
