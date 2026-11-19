<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_solid_page.html -->

# Solid

To create a **Solid** in the **Main Menu** select **New Entity - > Build - > Solid**.

Firstly, you can create a **Solid** from a list of shells.

The **Result** will be a **GEOM_Object** (SOLID).

**TUI Command:** *geompy.MakeSolid(ListOfShape),* where `ListOfShape` is a list of shells from which the solid is constructed.

**Arguments:** Name + A closed shell or a list of closed shells.

![neo-obj6.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-obj6.png)

**Example:**

![solidsn.png](https://docs.salome-platform.org/latest/gui/GEOM/solidsn.png)

Solid

Secondly, it is possible to create a **Solid** (or a compound of solids) from a list of connected faces or shells.

The **Result** will be a **GEOM_Object** (SOLID or COMPOUND).

**TUI Command:** *geompy.MakeSolidFromConnectedFaces(ListOfShape, isIntersect),* where `ListOfShape` is a list of faces and/or shells from which the solid is constructed and `isIntersect` is a boolean flag which, when set to `True`, forces performing intersection/sewing between arguments

**Arguments:** Name + A set of connected faces and/or shells + Boolean flag.

![neo-obj6_2.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-obj6_2.png)

Our **TUI Scripts** provide you with useful examples of creation of [Solid from shell](tui_topological_geom_objs_page.md#tui_creation_solid) and [Solid from connected faces](tui_topological_geom_objs_page.md#tui_creation_solid_from_faces).
