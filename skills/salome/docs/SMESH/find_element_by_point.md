<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/find_element_by_point.html -->

# Find Element by Point

This functionality allows you to find all mesh elements to which belongs a certain point.

*To find the elements:*

1. Select a mesh or a group
2. Select from the Mesh menu or from the context menu the Find Element by Point item ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/findelement3.png).

   The following dialog box will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/findelement2.png)
3. In this dialog box you should select:
   :   - the coordinates of the point;
       - the type of elements to be found; it is also possible to find elements of all types related to the reference point. Choose type “All” to find elements of any type except for nodes and 0D elements.
4. Click the **Find** button. IDs of found entities will be shown.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/findelement1.png)

**The reference point and the related elements.**

**See Also** a sample TUI Script of a [Find Element by Point](tui_viewing_meshes.md#tui-find-element-by-point) operation.
