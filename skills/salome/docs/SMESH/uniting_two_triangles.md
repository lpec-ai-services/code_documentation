<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/uniting_two_triangles.html -->

# Uniting two triangles

In MESH you can union two neighboring triangles by deletion of the common edge.

*To unite two triangles:*

1. From the **Modification** menu choose the **Union of two triangles** item or click *“Union of two triangles”* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image71.png) in the tool-bar.

   The following dialog box shall appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/unionoftwotriangles.png)
2. Enter IDs of nodes forming the required edge in the **Edge** field (a couple of node IDs separated by a dash) or select this edge in the 3D viewer.
3. Click the **Apply** or **Apply and Close** button.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/uniting_two_triangles1.png)

**“The selected triangles”**

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/uniting_two_triangles2.png)

**“The union of two triangles”**

**See Also** a sample TUI Script of a
[Uniting two Triangles](tui_modifying_meshes.md#tui-uniting-two-triangles) operation.
