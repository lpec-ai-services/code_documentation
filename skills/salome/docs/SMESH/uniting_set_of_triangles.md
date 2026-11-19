<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/uniting_set_of_triangles.html -->

# Uniting a set of triangles

It is possible to unite many neighboring triangles into
quadrangles by deletion of the common edge.

*To union several triangles:*

1. Select a mesh (and display it in the 3D Viewer if you are going to pick elements by mouse).
2. In the **Modification** menu select the **Union of triangles** item or click *“Union of triangles”* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image80.png) in the tool-bar.

   The following dialog box will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/a-unionoftriangles.png)
   > - **The main list** shall contain the triangles which will be united. You can click on a triangle in the 3D viewer and it will be highlighted. After that click the **Add** button and the ID of this triangle will be added to the list. To remove a selected element or elements from the list click the **Remove** button. The **Sort** button allows to sort the list of IDs. The **Filter** button allows to apply a definite [filter](selection_filter_library.md#filtering-elements) to selection of triangles.
   > - **Apply to all** radio button allows to apply the operation to all triangles of the selected mesh.
   > - **Preview** provides a preview in the viewer.
   > - **Criterion** menu allows to choose a quality criterion, which will be optimized to select triangles to unite.
   > - **Select from** set of fields allows to choose a sub-mesh or an existing group whose triangle elements then can be added to the list.
3. Click the **Apply** or **Apply and Close** button to confirm the operation.

If some selected triangle elements have no adjacent edges with one of
the others, the operation on these elements shall take no effect.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/uniting_a_set_of_triangles1.png)

**The chosen triangles**

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/uniting_a_set_of_triangles2.png)

**The union of several triangles - several quadrangular cells are created**

**See Also** a sample TUI Script of a
[Uniting a Set of Triangles](tui_modifying_meshes.md#tui-uniting-set-of-triangles) operation.
