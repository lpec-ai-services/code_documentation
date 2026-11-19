<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/suppress_faces_operation_page.html -->

# Suppress Faces

To produce a **Suppress Faces** operation in the **Main Menu** select **Repair - > Suppress Faces**.

This operation suppresses a face of a shape. This operation is available in **OCC Viewer** only.

The **Result** will be a **GEOM_Object** (ListOfGeomShapes).

**TUI Command:** *geompy.SuppressFaces(Shape, ListOfID),* where *Shape* is a shape to be processed, *ListOfID* is a list of faces ID's to be removed.   
**Arguments:** Name + 1 shape + Faces which should be removed (you can select them in the 3D viewer).

![repair2.png](https://docs.salome-platform.org/latest/gui/GEOM/repair2.png)

**Example:**

![suppress_faces1.png](https://docs.salome-platform.org/latest/gui/GEOM/suppress_faces1.png)

The initial box

![suppress_faces2.png](https://docs.salome-platform.org/latest/gui/GEOM/suppress_faces2.png)

The box with suppressed faces

Our **TUI Scripts** provide you with useful examples of the use of [Repairing Operations](tui_repairing_operations_page.md#tui_suppress_faces).
