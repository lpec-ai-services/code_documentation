<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/sewing_operation_page.html -->

# Sewing

**Sewing** operation allows uniting several faces (possibly contained in a shell, solid or compound) into one shell. Geometrically coincident (within a specified tolerance) edges (or parts of edges) of different faces are replaced by one edge thus producing a shell of faces with shared boundaries.

This operation is similar to **New Entity - > Build - > Shell** operation, the difference is that with **Sewing** you can specify the tolerance and get a non-manifold result.

The possibility to create a non-manifold shell can be used e.g. to create a shell forming several closed domains and then to create several solids with shared boundaries from this shell.

Note
:   Geometrically coincident faces (or parts of faces) will not be replaced by one face during **Sewing**.

To produce a **Sewing** operation in the **Main Menu** select **Repair - > Sewing**.

The **Result** will be a **GEOM_Object** (shell).

![repair6.png](https://docs.salome-platform.org/latest/gui/GEOM/repair6.png)

In this dialog:

- Click on the "Arrow" button and select in the Object Browser or in the viewer one or more **Shapes** (faces or shells) to be sewn.
- Activate **Allow Non Manifold**  check-box to produce non-manifold sewing, if required.
- Define precision for sewing in **Tolerance** field.
- Activate  **Detect Free boundaries** button to display the number of free boundaries in the shape:

  ![neo-detect2.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-detect2.png)
- Click **Apply** or **Apply and Close** button.

This operation can be also launched using a **TUI Command:**

*geompy.MakeSewing(ListOfShape, Precision, AllowNonManifold=False),*

where *ListOfShape* is a list of faces or shells to be sewn, *Precision* is a precision for sewing, *AllowNonManifold* is a flag that allows non-manifold sewing.

**Example:**

![image112.png](https://docs.salome-platform.org/latest/gui/GEOM/image112.png)

The initial faces

![image113.png](https://docs.salome-platform.org/latest/gui/GEOM/image113.png)

The sewn faces

Our **TUI Scripts** provide you with useful examples of the use of [Repairing Operations](tui_repairing_operations_page.md#tui_sewing).
