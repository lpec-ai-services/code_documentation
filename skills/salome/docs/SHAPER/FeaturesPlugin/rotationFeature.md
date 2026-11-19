<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/rotationFeature.html -->

# Rotation

**Rotation** feature makes rotation of a selected shape.

To create a Rotation in the active part:

1. select in the Main Menu *Part - > Rotation* item or
2. click ![rotation.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/rotation.png) **Rotation** button in the toolbar

Two rotation algorithms are:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/rotation_axis_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/rotation_axis_32x32.png)

by axis and angle

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/rotation_3pt_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/rotation_3pt_32x32.png)

by center and 2 points

---

## Rotation by axis and angle

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Rotation1.png)

Rotation by axis and angle property panel

Input fields:

- **Main objects** panel contains shapes to be rotated. Shapes are selected in 3D OCC viewer or object browser; [Transformation of COMPSOLID subshapes is prohibited.](translationFeature.md#transformation-subshapes)
- **Axis** defines the axis of rotation. The vector is an edge or axis selected in 3D OCC viewer or object browser;
- **Angle** defines the angle by which the object is rotated.

**TUI Command**:

model.addRotation(*Part_doc*, [*shape*, ]*axis*, *angle*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes in format *model.selection(TYPE, shape)*.
        - **object** – An axis in format *model.selection(TYPE, shape)*.
        - **real** – An angle.

    Returns:
    :   Rotated object.

### Result

Result of operation is a rotated initial shape.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/rotation_axis.png)

Rotation by axis and angle

**See Also** a sample TUI Script of [Rotation by axis and angle](TUI_rotationaxisFeature.md#tui-rotation-axis) operation.

## Rotation by center and points

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Rotation2.png)

Rotation by center and 2 points property panel

Input fields:

- **Main objects** panel contains shapes to be rotated. Shapes are selected in 3D OCC viewer or object browser; [Transformation of COMPSOLID subshapes is prohibited.](translationFeature.md#transformation-subshapes)
- **Center point**, **Start point**, **End point** define 3 points or vertices selected in 3D OCC viewer or object browser. Rotation axis will pass through the **Center point** and will be orthogonal to a plane defined by three points. Rotation Angle is the angle between two vectors directed from the **Center point** to **Start point** and **End point**.

**TUI Command**:

model.addRotation(Part_doc, [shape], point1, point2, point3)*
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes in format *model.selection(TYPE, shape)*.
        - **object** – An axis in format *model.selection(TYPE, shape)*.
        - **object** – Center vertex.
        - **object** – Start vertex.
        - **object** – End vertex.

    Returns:
    :   Rotated object.

### Result

Result of operation is a rotated initial shape.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/rotation_3points.png)

Rotation by center and 2 points

**See Also** a sample TUI Script of [Rotation by center and points](TUI_rotation3pointsFeature.md#tui-rotation-3points) operation.
