<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_wire_page.html -->

# Wire

To create a **Wire** in the **Main Menu** select **New Entity - > Build - > Wire**

You can create a **Wire** from several connected edges or wires by selecting them in the object browser or in the viewer holding Shift button.

It is possible to select wires or edges from objects. To specify sub-shape type, use the **Object Type** radio buttons.

Select **Tolerance** which will be used to check the connections. If the **Tolerance** value is more than 1e-07, and a gap within this tolerance is detected, the corresponding edges will be modified to connect in the middle of the gap.   
The **Result** will be a **GEOM_Object** (WIRE).

**TUI Command:** *geompy.MakeWire(ListOfShape, Tolerance)*

**Arguments:** Name + List of connected wires or edges + Tolerance.

**Dialog Box:**

![neo-obj3.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-obj3.png)

**Example:**

![wiresn.png](https://docs.salome-platform.org/latest/gui/GEOM/wiresn.png)

Wire

Our **TUI Scripts** provide you with useful examples of [Creation of a Wire](tui_topological_geom_objs_page.md#tui_creation_wire).
