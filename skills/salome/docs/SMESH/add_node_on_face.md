<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/add_node_on_face.html -->

# Cutting a face into triangles

This operation cuts a face into triangles by adding a node on the face and connecting the new node with face nodes.

> ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/add_node_on_face.png)

*To cut a face:*

1. Select a mesh and display it in the 3D Viewer.
2. In the **Modification** menu select the **Add node to triangle** item or click *“Add node to triangle”* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/mesh_split_face_interactive.png) in the toolbar.

   The following dialog box will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/add_node_on_face-dlg.png)
3. Enter an **ID** of the face to split either by picking it in the 3D viewer or by typing its ID.
4. Press *Selection* button in **Node location by mouse click** group to activate specifying location of a new node. You can specify it

   > - by clicking with your mouse on the face in the Viewer,
   > - by typing coordinates in **X, Y, Z** fields,
   > - by setting coordinates using arrows of spin boxes.
5. Activate **Preview** to see a result of the operation.
6. Click the **Apply** or **Apply and Close** button to confirm the operation.

**See Also** a sample TUI Script of a [Cutting Triangles](tui_modifying_meshes.md#tui-cutting-triangles) operation.
