<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/suppress_internal_wires_operation_page.html -->

# Suppress Internal Wires

To **Suppress Internal Wires** in the **Main Menu** select **Repair - > Suppress Internal Wires**.

This operation removes all internal wires or specified internal wires from user specified shapes. This operation is available in **OCC Viewer** only.

The **Result** will be a **GEOM_Object**.

**TUI Command:** *geompy.SuppressInternalWires(Shape, Wires),*  where *Shape* is a shape where wires are to be removed, *Wires* is a list of wires ID's to be removed; if the list is empty then all internal wires are removed.

**Arguments:**

- Name of the resulting object
- User specified shape
- User specified internal wires (lying on this shape except for its boundary), or all internal wires if **Remove all internal wires** box is checked

![repair4.png](https://docs.salome-platform.org/latest/gui/GEOM/repair4.png)

**Example:**

![supp_int_wires1.png](https://docs.salome-platform.org/latest/gui/GEOM/supp_int_wires1.png)

The box with internal wires

![supp_int_wires2.png](https://docs.salome-platform.org/latest/gui/GEOM/supp_int_wires2.png)

The internal wires have been suppressed

Our **TUI Scripts** provide you with useful examples of the use of [Repairing Operations](tui_repairing_operations_page.md#tui_suppress_internal_wires).
