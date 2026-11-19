<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/add_point_on_edge_operation_page.html -->

# Add Point on Edge

To **Add Point on Edge** in the **Main Menu** select **Repair - > Add Point on Edge**.

This operation splits an edge in two or more new edges. This operation is available in **OCC Viewer** only.

The **Result** will be a **GEOM_Object**.

The location of a new vertex on the selected edge can be defined in two ways:

1. By specifying the position (ranging from 0.0 to 1.0) by length or by parameter.

   **TUI Command:** *geompy.DivideEdge(Shape, EdgeID, Value, IsByParameter)*

   - *Shape* is a shape, which contains an edge to be divided;
   - *EdgeID* is the ID of the edge to be divided, if it is = -1, then *Shape* should be an edge itself;
   - *Value* is a value of parameter on edge or length parameter, depending on *IsByParameter*;
   - *IsByParameter* is a boolean flag, specifying the operation mode:
     - `True:` *Value* is treated as a curve parameter; [0..1]
     - `False:` *Value* is treated as a length parameter. [0..1]

   **Arguments:** Name + 1 Edge + 1 Value setting the position of the point according to the selected mode.

   The difference between "by parameter" and "by length" modes becomes apparent on the edges with irregular parametrization (for example, b-splines which usually have irregular density by the length). For example, value 0.5 "by length" on such edge will produce the point in the middle of this edge (equidistant from both its ends); the same 0.5 value "by parameter" will result in the point situated closer to one of the ends (depending on the actual parametrization).

   ![repair8.png](https://docs.salome-platform.org/latest/gui/GEOM/repair8.png)
2. By selecting several points that will be projected to the selected edge to find the location of new vertices.

   **TUI Command:** *geompy.DivideEdgeByPoint(Shape, Edge, Points):*

   - *Shape* is a shape, which contains an edge to be divided;
   - *Edge* is an edge to be divided (or its ID, if it is = -1, then *Shape* should be an edge itself);
   - *Points* is a list of points to be projected to the *Edge*.

   **Arguments:** Name + 1 Edge + 1 or more Points.

   ![divedgebypoint.png](https://docs.salome-platform.org/latest/gui/GEOM/divedgebypoint.png)

**Example:**

![image167.png](https://docs.salome-platform.org/latest/gui/GEOM/image167.png)

The initial edge

![image168.png](https://docs.salome-platform.org/latest/gui/GEOM/image168.png)

The edge split in two segments

Our **TUI Scripts** provide you with useful examples of the use of [Repairing Operations](tui_repairing_operations_page.md#tui_add_point_on_edge).
