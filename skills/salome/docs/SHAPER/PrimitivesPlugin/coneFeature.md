<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/PrimitivesPlugin/coneFeature.html -->

# Cone

Cone feature creates a cone solid.

To create a Cone in the active part:

1. select in the Main Menu *Primitives - > Cone* item or
2. click ![Cone_button.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Cone_button.png) **Cone** button in the toolbar

The following property panel appears.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Cone.png)

Cone property panel

Input fields:

- **Point** defines the center of the cone base selected in 3D OCC viewer or object browser;
- **Vector** defines the axis of the cone selected in 3D OCC viewer or object browser;
- Dimensions:
  :   - **Base Radius**;
      - **Top radius**;
      - **Height**.

**TUI Command**:

model.addCone(*Part_doc*, *Point*, *Axis*, *Radius1*, *Radius2*, *Height*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – Vertex.
        - **object** – Axis.
        - **real** – Radius 1.
        - **real** – Radius 2.
        - **real** – Height.

    Returns:
    :   Result object.

## Result

If both radii are non-zero, then the cone will be truncated.

If the radii are equal, the Cylinder will be created instead of cone.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Cone_res.png)

Cone created

**See Also** a sample TUI Script of [Create Cone](TUI_coneFeature.md#tui-create-cone) operation.
