<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/changing_orientation_of_elements.html -->

# Changing orientation of elements

Orientation of an element is changed by changing the [order](connectivity.md) of its nodes.

*To change orientation of elements:*

1. Select a mesh (and display it in the 3D Viewer if you are going to pick elements by mouse).
2. In the **Modification** menu select the **Orientation** item or click *Orientation* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image79.png) in the toolbar.

   The following dialog box will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/orientaation1.png)
   > - Select type of elements to reorient: **Face** or **Volume**.
   > - **The main list** shall contain the elements which will be reoriented. You can click on an element in the 3D viewer and it will be highlighted. After that click the **Add** button and the ID of this element will be added to the list. To remove a selected element or elements from the list click the **Remove** button. The **Sort** button allows to sort the list of elements IDs. The **Set filter** button allows to apply a definite [filter](selection_filter_library.md#filtering-elements) to the selection of elements.
   > - **Apply to all** radio button allows to modify the orientation of all elements of the selected mesh.
   > - *Select from** set of fields allows to choose a sub-mesh or an existing group whose elements can be added to the list.
3. Click the **Apply** or **Apply and Close** button to confirm the operation.

**See Also** a sample TUI Script of a [Orientation](tui_modifying_meshes.md#tui-orientation) operation.
