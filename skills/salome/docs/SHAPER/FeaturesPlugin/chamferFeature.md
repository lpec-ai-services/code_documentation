<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/chamferFeature.html -->

# Chamfer

**Chamfer** feature creates chamfers on the edges or on the faces of a shape.

To create a Chamfer in the active part:

1. select in the Main Menu *Feature - > Chamfer* item or
2. click ![chamfer.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/chamfer.png) **Chamfer** button in the toolbar

There are 2 types of chamfer:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/chamfer_distances.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/chamfer_distances.png)

chamfer by two distances

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/chamfer_dist_angle.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/chamfer_dist_angle.png)

chamfer by a distance and an angle

---

## Chamfer by two distances

The property panel is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/ChamferDistances.png)

Chamfer by two distances property panel

Input fields:

- **Faces or/and edges** panel contains chamfered faces and edges. All edges of a face are subject to chamfer operation. Faces and edges are selected in 3D OCC viewer;
- **D1** define the first chamfer distance;
- **D2** define the second chamfer distance;

**TUI Command**:

model.addChamfer(*Part_doc*, [*face*, *edge*, ]*perfomDistances*, *D1*, *D2*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of faces and edges subject to fillet operation in format *model.selection(TYPE, shape)*.
        - **boolean** – A “True” flag to indicate that the type of chamfer is by two distances.
        - **number** – D1 value.
        - **number** – D2 value.

    Returns:
    :   Created object.

### Result

Result of **Chamfer by two distances** is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/chamfer_res_distances.png)

Chamfer by two distances

**See Also** a sample TUI Script of [Create Chamfer by distances](TUI_chamferDistances.md#tui-create-chamfer1) operation.

## Chamfer by a distance and an angle

Alternatively, there is a possibility to create a chamfer with a distance and an angle.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/ChamferDistAngle.png)

Chamfer by a distance and an angle

Input fields:

- **Faces or/and edges** panel contains filleted faces and edges. All edges of a face are subject to fillet operation. Faces and edges are selected in 3D OCC viewer;
- **D** defines the chamfer distance;
- **Angle** defines the chamfer angle.

**TUI Command**:

model.addChamfer(*Part_doc*, [*face*, *edge*, ]*perfomDistances*, *D*, *Angle*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of faces and edges subject to fillet operation in format *model.selection(TYPE, shape)*.
        - **boolean** – A “False” flag to indicate that the type of chamfer is by a distance and an angle.
        - **number** – D value.
        - **number** – Angle value.

    Returns:
    :   Created object.

### Result

Result of **Chamfer by a distance and an angle** is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/chamfer_res_dist_angle.png)

Chamfer by a distance and an angle

**See Also** a sample TUI Script of [Create Chamfer by a distance and an angle](TUI_chamferDistAngle.md#tui-create-chamfer2) operation.
