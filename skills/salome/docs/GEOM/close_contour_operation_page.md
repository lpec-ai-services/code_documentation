<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/close_contour_operation_page.html -->

# Close Contour

To produce a **Close Contour** operation in the **Main Menu** select **Repair - > Close Contour**.

This operation closes an open contour and modifies the underlying face (if needed) in accordance with user specified mode:

- By common vertex – a vertex is created between the end points of the contour and its tolerance is increased to a value of the gap between the ends of the contour;
- By new edge – a new edge is inserted between the end points of the contour.

This operation is available in **OCC Viewer** only.

The **Result** will be a **GEOM_Object**.

**TUI Command:** *geompy.CloseContour(Shape, Wires, IsCommonVertex),* where *Shape* is a shape to be processed, *Wires* is a list of edges or wires ID's which has to be closed within the shape (if the list contains only one element = -1, the shape itself is considered as a wire), *IsCommonVertex* if this parameter is True a closure has to be done by creation of a common vertex, otherwise an edge is added between the end vertices.   
**Arguments:** Name + 1 shape + contour (Wire, or a set of Edges) + mode of closure (by vertex or by edge)

![repair3.png](https://docs.salome-platform.org/latest/gui/GEOM/repair3.png)

Our **TUI Scripts** provide you with useful examples of the use of [Repairing Operations](tui_repairing_operations_page.md#tui_close_contour).
