<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/coincedentFeature.html -->

# Coincident constraint

Coincident constraint forces two points to be coincident, or one point to lie on a line, a circle or an arc.

To create a Coincident constraint in the active Sketch:

1. select in the Main Menu *Sketch - > Coincident* item or
2. click ![coincedence.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/coincedence.png) **Coincident** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Coincident_panel.png)

Input fields:

- **First object** is a point, a line, a circle or an arc selected in the view.
- **Second object** is a point, a line, a circle or an arc selected in the view.

Note that one of two objects should be a point (i.e. a point, a line or an arc end point, a center of a circle or an arc).

After the objects are selected, the point is highlighted in yellow in the view.

**TUI Command**:

Sketch_1.setCoincident(*Object1*, *Object2*)
:   Parameters:
    :   - **object** – First object.
        - **object** – Second object.

    Returns:
    :   Result object.

## Result

Created Coincident constraint appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Coincident_res.png)

Created coincident constraint

**See Also** a sample TUI Script of [Create Coincident constraint](TUI_coincident.md#tui-create-coincident) operation.
