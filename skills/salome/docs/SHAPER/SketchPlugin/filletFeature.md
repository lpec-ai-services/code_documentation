<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/filletFeature.html -->

# Fillet

The Fillet operation rounds the corner formed by intersection of two sketch elements in a coincident point.

The operation trims the elements at the intersection and creates a tangent arc between them.

To create a Fillet in the active Sketch:

1. select in the Main Menu *Sketch - > Fillet* item or
2. click ![fillet.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Fillet.png) **Fillet** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Fillet_panel.png)

Fillet

Input fields:

- **Point** is the coincident point of two intersecting lines (or a line and an arc) selected in the view.

After the point is selected, Fillet preview appears in the view.

**TUI Command**:

Sketch_1.setFillet(*Point*)
:   Parameters:
    :   **object** – Coincident point.

    Returns:
    :   Result object.

Sketch_1.setFilletWithRadius(*Point*, *Radius*)
:   Parameters:
    :   - **object** – Coincident point.
        - **real** – Radius.

    Returns:
    :   Result object.

## Result

Created Fillet appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Fillet_res.png)

Created fillet

**See Also** a sample TUI Script of [Create Fillet](TUI_fillet.md#tui-create-fillet) operation.
