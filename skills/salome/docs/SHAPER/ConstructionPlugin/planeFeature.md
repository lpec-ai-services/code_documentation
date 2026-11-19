<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ConstructionPlugin/planeFeature.html -->

# Plane

Plane feature creates a new constructive plane.

Plane is a construction object that can be created in a part or in a partset. To create a plane:

1. select in the Main Menu *Construction - > Plane* item or
2. click ![plane_button.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/plane_button.png) **Point** button in the toolbar

There are 4 algorithms for creation of a Plane:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/plane_by_three_points_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/plane_by_three_points_32x32.png)

**By three points** creates a plane by three points.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/plane_by_line_and_point_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/plane_by_line_and_point_32x32.png)

**By line and point** creates a plane by a line and a point.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/plane_by_other_plane_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/plane_by_other_plane_32x32.png)

**By other plane** creates a plane or planes(if the number of copies is more than one) parallel to another plane.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/plane_by_two_parallel_planes_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/plane_by_two_parallel_planes_32x32.png)

**By two parallel planes** creates a plane between two parallel planes.

---

## By three points

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Plane1.png)

**By three points**

A plane is created by selecting three points in a viewer.

**TUI Commands**:

model.addPlane(*Part_doc*, *model.selection("VERTEX"*, *"Box_1_1/Back&Box_1_1/Left&Box_1_1/Top")*, *model.selection("VERTEX"*, *"Box_1_1/Front&Box_1_1/Right&Box_1_1/Top")*, *model.selection("VERTEX"*, *"Box_1_1/Front&Box_1_1/Left&Box_1_1/Bottom")*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – Vertex 1.
        - **object** – Vertex 2.
        - **object** – Vertex 3.

    Returns:
    :   Result object.

### Result

The Result of the operation will be a plane:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedPlane1.png)

**A plane by three points**

**See Also** a sample TUI Script of [Create Plane by points](TUI_plane1Feature.md#tui-create-plane-points) operation.

## By line and point

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Plane2.png)

**Line and point**

A plane is created by selecting a linear edge and point. It is possible to create a new plane perpendicular to the selected edge.

**TUI Commands**:

model.addPlane(*Part_doc*, *model.selection("EDGE"*, *"Box_1_1/Left&Box_1_1/Top")*, *model.selection("VERTEX"*, *"Box_1_1/Front&Box_1_1/Right&Box_1_1/Bottom")*, *False*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – A line.
        - **object** – A point.
        - **boolean** – Is perpendicular to line.

    Returns:
    :   Result object.

### Result

The Result of the operation will be a plane:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedPlane2.png)

Plane created

**See Also** a sample TUI Script of [Create Plane by line and point](TUI_plane2Feature.md#tui-create-plane-line) operation.

## By other plane

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Plane3.png)

**By other plane**

A plane is created by selecting an already existing plane (planar face). There are following possibilities to define a new plane:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/plane_by_distance_from_other_24x24.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/plane_by_distance_from_other_24x24.png)

By distance from the selected plane.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/plane_by_coincident_to_point_24x24.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/plane_by_coincident_to_point_24x24.png)

By coincidence with a point.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/plane_by_rotation_24x24.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/plane_by_rotation_24x24.png)

By rotation around an edge by a specified angle.

**TUI Commands**:

model.addPlane(*Part_doc*, *model.selection("FACE"*, *"Box_1_1/Front")*, *10*, *False*, *1*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – A plane.
        - **real** – An offset.
        - **boolean** – Is reverse.
        - **integer** – Number of copies

    Returns:
    :   Result object.

### Result

The Result of the operation will be a plane (or planes at equal distance from each other, if the number of copies is more than one) parallel to already existing one:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedPlane3.png)

**Plane parallel to a planar face**

**See Also** a sample TUI Script of [Create Plane by other plane](TUI_plane3Feature.md#tui-create-plane-plane) operation.

## By two parallel planes

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Plane4.png)

**By two parallel planes**

A plane is created by selecting two parallel planes. A new plane will be defined between them.

**TUI Commands**:

model.addPlane(*Part_doc*, *model.selection("FACE"*, *"Box_1_1/Left")*, *model.selection("FACE"*, *"Box_1_1/Right")*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – A plane 1.
        - **object** – A plane 2.

    Returns:
    :   Result object.

### Result

The Result of the operation will be a plane created between two selected planes:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedPlane4.png)

**Plane created between others**

**See Also** a sample TUI Script of [Create Plane by two parallel planes](TUI_plane4Feature.md#tui-create-plane-parallel) operation.
