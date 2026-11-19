<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/offset_elements.html -->

# Offset mesh

Offset 2D elements in mesh, submesh, group or elements from filter.

*To offset all elements from mesh, sub-mesh or group:*

1. In the **Modification** menu, select the **Transformations** then click *Offset* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image81.png) or click directly in the same button in the toolbar.

   The following dialog box will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/offset_mesh.png)
   > - Check the option **Select whole mesh, sub-mesh or group** if it is not set.
   > - Set the name of the mesh, sub-mesh or created group.
   > - Set the **Offset** value (negative offsets are allowed).
   > - Select **Move Elements** to offset the current mesh, **Copy Elements** to offset and duplicate them, or **Create a new mesh** to create a new mesh from the offset elements.
2. Click the **Apply** or **Apply and Close** button to confirm the operation.

*To offset all elements ids from a filter:*

1. In the **Modification** menu, select the **Transformations** then click *Offset* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image81.png) or click directly in the same button from the toolbar.

   > - Uncheck the option **Select whole mesh, sub-mesh or group**.![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/offset_mesh_from_filter.png)
   > - Then click on **Set_Filter** button
   >
   > The dialog for filter for faces will appear:
   >
   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/offset_filter_for_faces_gui.png)
   > - Define the desired criteria and then click the **Apply and Close** button to confirm the selection of elements.
   > - Set **Offset** value and mesh creation **options** as done for the first case.
2. Click the **Apply** or **Apply and Close** button to confirm the operation.

**See also:** A sample TUI Script of a [Offset 2D mesh](tui_transforming_meshes.md#tui-offset-elements) transformation.
