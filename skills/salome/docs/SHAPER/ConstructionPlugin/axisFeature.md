<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ConstructionPlugin/axisFeature.html -->

# Axis

Axis feature creates a new constructive axis line.

Axis is a construction object and it can be created in a part or in a partset. To create an axis:

1. select in the Main Menu *Construction - > Axis* item or
2. click ![axis_button.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/axis_button.png) **Axis** button in the toolbar

There are 6 algorithms for creation of an Axis:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/axis_dxyz_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/axis_dxyz_32x32.png)

**By three dimensions** creates an axis by dimensions along X, Y, Z axes starting form existing origin.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/by_two_points_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/by_two_points_32x32.png)

**By two points** creates an axis using existing points.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/axis_by_line_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/axis_by_line_32x32.png)

**By line** creates an axis using a line.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/cylindrical_face_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/cylindrical_face_32x32.png)

**As an axis of cylindrical face** creates an axis using a cylindrical face.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/axis_by_plane_and_point_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/axis_by_plane_and_point_32x32.png)

**By plane and point** creates an axis using a plane and point.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/axis_by_two_planes_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/axis_by_two_planes_32x32.png)

**By two planes** creates an axis as the intersection of two planes.

---

## By three dimensions

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Axis1.png)

**By dX, dY, dZ values**

An axis is defined by dX, dY and dZ values of a vector.

**TUI Commands**:

model.addAxis(*Part_doc*, *10*, *10*, *10*)
:   Parameters:
    :   - **part** – The current part object.
        - **real** – dX.
        - **real** – dY.
        - **real** – dZ.

    Returns:
    :   Result object.

### Result

The Result of the operation will be an axis defined by vector from origin:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedAxis1.png)

**Axis by three dimensions**

**See Also** a sample TUI Script of [Create Axis by dimensions](TUI_axis1Feature.md#tui-create-axis-xyz) operation.

## By two points

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Axis2.png)

**By two points**

An axis is defined by two points or vertices.

**TUI Commands**:

model.addAxis(*Part_doc*, *model.selection("VERTEX"*, *"Box_1_1/Back&Box_1_1/Left&Box_1_1/Top")*, *model.selection("VERTEX"*, *"Box_1_1/Front&Box_1_1/Right&Box_1_1/Bottom")*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – Vertex 1.
        - **object** – Vertex 2.

    Returns:
    :   Result object.

**See Also** a sample TUI Script of [Create Axis by points](TUI_axis2Feature.md#tui-create-axis-points) operation.

### Result

The Result of the operation will be an axis based on two points:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedAxis2.png)

**Axis by two points**

**See Also** a sample TUI Script of [Create Axis by points](TUI_axis2Feature.md#tui-create-axis-points) operation.

## By line

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Axis3.png)

**By a line**

An axis is defined by a linear edge.

**TUI Commands**:

model.addAxis(*Part_doc*, *model.selection("EDGE"*, *"Box_1_1/Left&Box_1_1/Top")*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – Edge.

    Returns:
    :   Result object.

### Result

The Result of the operation will be an axis based on the selected line:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedAxis3.png)

**Axis by line**

**See Also** a sample TUI Script of [Create Axis by line](TUI_axis3Feature.md#tui-create-axis-line) operation.

## As an axis of cylindrical face

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Axis4.png)

**By a cylinder**

An axis is defined by a cylindrical face. Axis of the cylinder will be an axis object.

**TUI Commands**:

model.addAxis(*Part_doc*, *model.selection("FACE"*, *"Cylinder_1_1/Face_1")*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – Cylindrical face.

    Returns:
    :   Result object.

### Result

The Result of the operation will be an axis of the selected cylinder:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedAxis4.png)

**Axis cylindrical face**

**See Also** a sample TUI Script of [Create Axis by cylinder](TUI_axis4Feature.md#tui-create-axis-cylinder) operation.

## By plane and point

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Axis5.png)

**By a plane and point**

An axis is defined by a point or vertex and plane (or planar face) as a normal from the point to the plane.

**TUI Commands**:

model.addAxis(*Part_doc*, *model.selection("FACE"*, *"Box_1_1/Front")*, *model.selection("VERTEX"*, *"Box_1_1/Back&Box_1_1/Right&Box_1_1/Top")*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – Plane.
        - **object** – Point.

    Returns:
    :   Result object.

### Result

The Result of the operation will be an axis:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedAxis5.png)

**Axis by plane and point**

**See Also** a sample TUI Script of [Create Axis by plane and point](TUI_axis5Feature.md#tui-create-axis-plane) operation.

## By two planes

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Axis6.png)

**By two planes**

An axis is defined by two planes. The intersection of the planes defines an axis. It is possible to define offset for axis definition from both planes.

**TUI Commands**:

model.addAxis(*Part_doc*, *model.selection("FACE"*, *"Box_1_1/Top")*, *5*, *False*, *model.selection("FACE"*, *"Box_1_1/Front")*, *3*, *False*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – Plane 1.
        - **real** – Offset value.
        - **boolean** – Is reversed.
        - **object** – Plane 2.
        - **real** – Offset value.
        - **boolean** – Is reversed.

    Returns:
    :   Result object.

### Result

The Result of the operation will be an axis:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedAxis6.png)

**Axis by two planes**

**See Also** a sample TUI Script of [Create Axis by two planes](TUI_axis6Feature.md#tui-create-axis-twoplanes) operation.
