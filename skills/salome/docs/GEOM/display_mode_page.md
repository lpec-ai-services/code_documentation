<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/display_mode_page.html -->

# Display Mode

This option is relevant for viewing 3D objects. Wireframe mode means that you can see only edges of the object, while its shells remain transparent. Shading mode means that the shells are filled with color.

To change the display mode right-click on this geometrical object in the viewer and from the pop-up menu select **Display mode –> Wireframe** or **Shading**.

**TUI Command:** *gg.setDisplayMode(ID, Short)*

![disp_mode1sn.png](https://docs.salome-platform.org/latest/gui/GEOM/disp_mode1sn.png)

*Wireframe*

![disp_mode2sn.png](https://docs.salome-platform.org/latest/gui/GEOM/disp_mode2sn.png)

*Shading*

It is possible to show the direction of edges of the selected shape. For this, choose in the context menu of the shape **Display mode -> Show Edge Direction**, or apply this functionality for all objects in the current view via the main menu  **View -> Display Mode -> Show/Hide Edge Direction.**

![vectors_mode.png](https://docs.salome-platform.org/latest/gui/GEOM/vectors_mode.png)

*Vectors Mode (Show Edge Direction)*

**TUI Command:** *gg.setVectorsMode(ID, Bool)*

It is possible to show the vertices of the selected shape. For this, choose in the context menu of the shape **Display mode -> Show Vertices**, or apply this functionality for all objects in the current view via the main menu  **View -> Display Mode -> Show/Hide Vertices.**

![vertices_mode.png](https://docs.salome-platform.org/latest/gui/GEOM/vertices_mode.png)

*Vertices Mode (Show Vertices)*

**TUI Command:** *gg.setVerticesMode(ID, Bool)*

To show the name of the selected shape, choose in its context menu **Display mode -> Show Name**, or apply this functionality for all objects in the current view via the main menu option  **View -> Display Mode -> Show/Hide Name.**

![name_mode.png](https://docs.salome-platform.org/latest/gui/GEOM/name_mode.png)

*Name Mode (Show Name)*

**TUI Command:** *gg.setNameMode(ID, Bool)*

Our **TUI Scripts** provide you with useful examples of [Changing Display Parameters](tui_viewing_geom_objs_page.md#tui_change_disp_mode).
