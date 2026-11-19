<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/add_node_on_segment.html -->

# Cutting triangles

This operation cuts triangles into two by adding a node on an edge bounding these triangles.

> ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/add_node_on_segment.png)

*To cut triangles:*

1. Select a mesh and display it in the 3D Viewer.
2. In the **Modification** menu select the **Add node on segment** item or click *“Add node on segment”* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/mesh_split_diag_interactive.png) in the toolbar.

   The following dialog box will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/add_node_on_segment-dlg.png)
3. Enter IDs of nodes forming the edge in the **Edge** field (the node IDs must be separated by a dash) or select the edge in the 3D viewer.
4. Enter location of a new node on the edge which is defined as a real number in the range between 0.0 and 1.0. You can define it

   > - by clicking with your mouse on the edge in the Viewer,
   > - by typing a number in a field,
   > - by setting a number using arrows of a spin box.
5. Activate **Preview** to see a result of the operation.
6. Click the **Apply** or **Apply and Close** button to confirm the operation.

**See Also** a sample TUI Script of a [Cutting Triangles](tui_modifying_meshes.md#tui-cutting-triangles) operation.
