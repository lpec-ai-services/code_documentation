<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/convert_to_from_quadratic_mesh.html -->

# Convert to/from Quadratic Mesh

This functionality allows transforming linear meshes (or sub-meshes) to quadratic and vice versa.

Note

that conversion of a sub-mesh most probably will produce a non-conformal mesh. Elements on the boundary between quadratic and linear sub-meshes become (or remain) quadratic.

See [Adding Quadratic Elements](adding_quadratic_elements.md#adding-quadratic-elements-page) for more information about quadratic meshes.

*To produce a conversion:*

1. Select a mesh or a sub-mesh in the Object Browser or in the Viewer.
2. From the Modification menu or from the contextual menu in the Object Browser choose **Convert to/from Quadratic Mesh** item, or click *“Convert to/from quadratic”* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image154.png) in the toolbar.

   The following dialog box will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/convert.png)
3. In this dialog box specify:

   - If it is necessary to convert a linear mesh to quadratic or a quadratic mesh to linear. **Convert to bi-quadratic** creates some types of quadratic elements with additional central nodes: TRIA7, QUAD9 and HEXA27 elements instead of TRIA6, QUAD8, and HEXA20 elements respectively.
   - If it is necessary to place **medium nodes** of the quadratic mesh **on the geometry** (meshed shape). This option is relevant for conversion to quadratic provided that the mesh is based on a geometry (not imported from file).

     > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image156.gif)
     >
     > **Linear mesh (coarse mesh on a torus)**
     >
     > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image155.gif)
     >
     > **Quadratic mesh**
4. Click the **Apply** or **Apply and Close** button.

**See Also** a sample TUI Script of a [Convert mesh to/from quadratic](tui_modifying_meshes.md#tui-quadratic) operation.
