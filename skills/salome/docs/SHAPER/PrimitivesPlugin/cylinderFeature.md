<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/PrimitivesPlugin/cylinderFeature.html -->

# Cylinder

Cylinder feature creates a cylinder solid.

To create a Cylinder in the active part:

1. select in the Main Menu *Primitives - > Cylinder* item or
2. click ![Cylinder_button.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Cylinder_button.png) **Cylinder** button in the toolbar

There are 2 algorithms for creation of a Cylinder:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/cylinder_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/cylinder_32x32.png)

**Cylinder** creates a cylinder.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/cylinder_portion_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/cylinder_portion_32x32.png)

**Portion of cylinder** creates one segment of a cylinder.

---

## Cylinder

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Cylinder.png)

**Cylinder** property panel

Input fields:

- **Point** defines the center of the cylinder base selected in 3D OCC viewer or object browser;
- **Vector** defines the axis of the cylinder selected in 3D OCC viewer or object browser;
- Dimensions:
  :   - **Radius**;
      - **Height**.

**TUI Commands**:

model.addCylinder(*Part_doc*, *Point*, *Axis*, *Radius*, *Height*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – Vertex.
        - **object** – Axis.
        - **real** – Radius.
        - **real** – Height.

    Returns:
    :   Result object.

### Result

An example is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Cylinder1.png)

Cylinder

**See Also** a sample TUI Script of [Create Cylinder](TUI_cylinderFeature.md#tui-create-cylinder) operation.

## Portion of cylinder

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Portion_cylinder.png)

**Portion of cylinder** property panel

Input fields for ***Portion of cylinder** tab include **Angle** defining a portion of cylinder.

**TUI Commands**:

model.addCylinder(*Part_doc*, *Point*, *Axis*, *Radius*, *Height*, *Angle*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – Vertex.
        - **object** – Axis.
        - **real** – Radius.
        - **real** – Height.
        - **real** – Angle.

    Returns:
    :   Result object.

### Result

An example is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Cylinder2.png)

Portion of cylinder

**See Also** a sample TUI Script of [Create Portion of cylinder](TUI_cylinderPortion.md#tui-create-cylportion) operation.
