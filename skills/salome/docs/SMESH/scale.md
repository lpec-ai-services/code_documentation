<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/scale.html -->

# Scale

This geometrical operation allows to scale in space your mesh or some of its elements.

*To scale a mesh:*

1. From the **Modification** menu choose **Transformation** -> **Scale Transform** item.

   The following dialogs will appear, where you can select how to scale:

   > - with one scale factor:![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scale01.png)
   > - or with different scale factors for axes:![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scale02.png)
2. In the dialog:
   :   - specify the IDs of the translated elements:
         :   - **Select the whole mesh, submesh or group** activating this checkbox; or
             - choose mesh elements with the mouse in the 3D Viewer. It is possible to select a whole area with a mouse frame; or
             - input the element IDs directly in **ID Elements** field. The selected elements will be highlighted in the viewer; or
             - apply Filters. **Set filter** button allows to apply a filter to the selection of elements. See more about filters in the [Selection filter library](selection_filter_library.md#selection-filter-library-page) page.
       - specify the base point for scale
       - specify the scale factor
       - specify the conditions of scale:

         > - activate **Move elements** radio button to scale the selected mesh (or elements) without creating a copy;
         > - activate **Copy elements** radio button to duplicate the selected mesh (or elements) and to apply scaling to the copy within the same mesh;
         > - activate **Create as new mesh** radio button to leave the selected mesh (or elements) at its previous location and create a new mesh of the scaled copy of the selected elements; the new mesh appears in the Object Browser with the default name MeshName_scaled (it is possible to change this name in the adjacent box);
         > - activate **Copy groups** checkbox to copy the groups of elements existing in the source mesh to the newly created mesh.
       - activate **Preview** checkbox to show the result of transformation in the viewer
       - click **Apply** or **Apply and Close** button to confirm the operation.

**Example of using:**

1. Create quandrangle mesh 3x3 on a simple planar face (200x200)

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scaleinit01.png)

   and union 3 faces (along axis Z) to group “gr_faces”

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scaleinit02.png)
2. Perform scale operation for the whole mesh and create a new mesh:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scale03.png)

   result after operation:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scaleres03.png)
3. Perform scale operation for the whole mesh and copy elements:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scale04.png)

   result after operation:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scaleres04.png)
4. Perform scale operation for a group of faces and copy elements:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scale06.png)

   result after operation:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scaleres06.png)
5. Perform scale operation for two edges and move elements:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scale07.png)

   result after operation:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scaleres07.png)
6. Perform scale operation for one face and move elements:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scale09.png)

   result after operation:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/scaleres09.png)

**See Also** a sample TUI Script of a [Scale](tui_transforming_meshes.md#tui-scale) operation.
