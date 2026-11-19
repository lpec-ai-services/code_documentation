<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_shell_page.html -->

# Shell

To create a **Shell** in the **Main Menu** select **New Entity - > Build - > Shell**

You can create a **Shell** from a compound of faces or a list of faces or shells.   
The **Result** will be a **GEOM_Object**. It can be either a single shell or, in specific cases, a compound of shells.

**TUI Command:** *geompy.MakeShell(ListOfShape)*   
**Arguments:** Name + Compound of faces or List of faces having connected edges.

![neo-obj5.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-obj5.png)

**Example:**

![shellsn.png](https://docs.salome-platform.org/latest/gui/GEOM/shellsn.png)

Shell

Our **TUI Scripts** provide you with useful examples of creation of [Advanced Geometric Objects](tui_topological_geom_objs_page.md#tui_creation_shell).
