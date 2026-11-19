<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/propagate_operation_page.html -->

# Propagate

To produce a **Propagate** operation in the **Main Menu** select **Operations - > Blocks - > Propagate**

This operation breaks a multitude of edges of a shape into groups (builds all possible propagation groups).   
The **Result** will be a **List of GEOM_Objects**. Each Geom Object will contain a group of edges.

**TUI Command:** *geompy.Propagate(Shape),* where *Shape* is a shape to build propagation groups on.   
**Arguments:** 1 Shape.

![mtransf4.png](https://docs.salome-platform.org/latest/gui/GEOM/mtransf4.png)

**Example:**

![image15.png](https://docs.salome-platform.org/latest/gui/GEOM/image15.png)

The initial box

![image16.png](https://docs.salome-platform.org/latest/gui/GEOM/image16.png)

The resulting edges

Our **TUI Scripts** provide you with useful examples of the use of [Blocks Operations](tui_blocks_operations_page.md#tui_propagate).
