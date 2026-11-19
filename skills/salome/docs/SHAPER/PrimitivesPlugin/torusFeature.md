<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/PrimitivesPlugin/torusFeature.html -->

# Torus

Torus feature creates a torus solid.

To create a Torus in the active part:

1. select in the Main Menu *Primitives - > Torus* item or
2. click ![Torus_button.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Torus_button.png) **Torus** button in the toolbar

The following property panel appears.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Torus.png)

Torus

Input fields:

- **Point** defines the center of the torus base selected in 3D OCC viewer or object browser;
- **Vector** defines the axis of the torus selected in 3D OCC viewer or object browser;
- Dimensions:
  :   - **Radius**;
      - **Ring radius**.

**TUI Command**:

model.addTorus(*Part_doc*, *Point*, *Axis*, *Radius1*, *Radius2*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – Vertex.
        - **object** – Axis.
        - **real** – Radius 1.
        - **real** – Radius 2.

    Returns:
    :   Result object.

## Result

An example is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Torus_res.png)

Torus created

**See Also** a sample TUI Script of [Create Torus](TUI_torusFeature.md#tui-create-torus) operation.
