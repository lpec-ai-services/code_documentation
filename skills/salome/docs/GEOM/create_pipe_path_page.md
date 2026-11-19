<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_pipe_path_page.html -->

# Restore Path

To generate a **Path** in the **Main Menu** select **New Entity - > Generation - > Restore Path**

![pipe_path_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/pipe_path_dlg.png)

To obtain the **Path** of a pipe-like shape, you should define the **Pipe-like shell or solid** and two pipe **Bases**, which can be defined by a wire, a face or a list of edges.  
  
**Select unpublished edges** checkbox - if checked, allows selecting in the viewer the edges, that are not published in the Object Browser.  
  
The **Result** of the operation will be a GEOM_Object (edge or wire).

**Advanced options**:

- [Preview](restore_presentation_parameters_page.md#preview_anchor)

Note
:   It is not always possible to obtain an exact or approximate copy of the Shape by applying the **Pipe** operation to the resulting "Path" wire with the first Base as the base; though in some particular cases it might work. Thus, Restore Path function should not be considered as an exact reverse operation of the Pipe.

**Example:**

![pipe_path.png](https://docs.salome-platform.org/latest/gui/GEOM/pipe_path.png)

Path (red) between two faces (green)

**TUI Command:** *geompy.RestorePath(aShape, aBase1, aBase2)*   
**Arguments:** Name + 1 pipe-like shape (shell or solid) + 1 shape (edge, wire or face) for the first base + 1 shape (edge, wire or face) for the last base.   
**TUI Command:** *geompy.RestorePathEdges(aShape, listEdges1, listEdges2)*   
**Arguments:** Name + 1 pipe-like shape (shell or solid) + 1 list of edges for the first base + 1 list of edges for the last base.

Our **TUI Scripts** provide you with useful examples of creation of [Complex Geometric Objects](tui_complex_objs_page.md#tui_creation_pipe_path).
