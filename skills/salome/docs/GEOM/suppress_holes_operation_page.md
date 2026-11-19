<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/suppress_holes_operation_page.html -->

# Suppress Holes

To **Suppress Holes** in the **Main Menu** select **Repair - > Suppress Holes**.

This operation removes holes with free boundaries on a selected shell or face. This operation is available in **OCC Viewer** only.

The **Result** will be a **GEOM_Object**.

**TUI Command:** *geompy.SuppressHoles(Shape, ListOfWireID),* where *Shape* is a shell or face, where holes with free boundaries must be removed, *ListOfWireID* is a list of wire sub-shapes ID's. If it is empty, then all holes are removed.

![repair5.png](https://docs.salome-platform.org/latest/gui/GEOM/repair5.png)

**Arguments:** Name + 1 shape + Wires which should be removed.   
**Remove all holes** checkbox allows to fill all holes of a definite shape.   
**Detect** button allows to display the number of free boundaries in your shape:

![neo-detect2.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-detect2.png)

**Example:**

![image109.png](https://docs.salome-platform.org/latest/gui/GEOM/image109.png)

The cone with a hole

![image110.png](https://docs.salome-platform.org/latest/gui/GEOM/image110.png)

The hole has been suppressed

Our **TUI Scripts** provide you with useful examples of the use of [Repairing Operations](tui_repairing_operations_page.md#tui_suppress_holes).
