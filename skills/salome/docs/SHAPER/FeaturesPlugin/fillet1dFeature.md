<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/fillet1dFeature.html -->

# 1D-fillet

**1D-fillet** feature creates fillets on the vertices of a wire.
The fillet may be performed on sharp corners of a wire, which are shared exactly between 2 edges, and which are placed ona single plane.

To create a 1D-fillet in the active part:

1. select in the Main Menu *Feature - > 1D-fillet* item or
2. click ![fillet1d.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/fillet1d.png) **1D-fillet** button in the toolbar

There are 2 types of fillet:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/fillet1d_wire.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/fillet1d_wire.png)

fillet all sharp corners on a wire

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/fillet1d_points.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/fillet1d_points.png)

fillet only the specified corners

## Fillet a wire

The property panel for this mode is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Fillet1DPanel_Wire.png)

**Property panel of an operation to fillet all sharp corners on a wire**

Input fields:

- **Wires** panel contains the list of wires for the operation. The fillet will be performed to the applicable corners. If the wire has no such corner, the error message will be shown;
- **Radius** defines the fillet radius.

**TUI Command**:

model.addFillet(*Part_doc*, *wires*, *radius*)
:   Parameters:
    :   - **Part_doc** (*document*) – The current part object.
        - **wires** (*list*) – A list of wires subject to fillet operation in format *model.selection(TYPE, shape)*.
        - **radius** (*double*) – Radius value.

    Returns:
    :   Created object.

### Result

Result of **Fillet a wire** is shown below. In this case all vertices were sharp, thus, filleted.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Fillet1DResult_Wire.png)

**Result of filleting a wire**

**See Also** a sample TUI Script of [Create 1D-fillet on a wire](TUI_fillet1DWire.md#tui-create-fillet1d-wire) operation.

## Fillet the specified vertices on a wire

Alternatively, there is a possibility to create a fillet on a special sharp corners of a wire.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Fillet1DPanel_Vertices.png)

**Property panel to fillet the specified vertices of a wire**

Input fields:

- **Vertices** panel contains list of vertices on a wires applicable for fillet operation;
- **Radius** defines the fillet radius.

**TUI Command**:

model.addFillet(*Part_doc*, *vertices*, *radius*)
:   > param document Part_doc:
    > :   The current part object.
    >
    > param list vertices:
    > :   A list of vertices subject to fillet operation in format *model.selection(TYPE, shape)*.
    >
    > param double radius:
    > :   Radius value.
    >
    > return:
    > :   Created object.

### Result

Result of **Fillet by vertices** is shown below. The only 2 corners of the wire become smooth.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Fillet1DResult_Vertices.png)

**Result of filleting the specified vertices of a wire**

**See Also** a sample TUI Script of [Create 1D-fillet for special vertices on a wire](TUI_fillet1DVertices.md#tui-create-fillet1d-vertices) operation.
