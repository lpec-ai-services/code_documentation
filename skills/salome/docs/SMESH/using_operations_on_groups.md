<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/using_operations_on_groups.html -->

# Boolean operations on groups

In MESH you can perform some Boolean operations on groups, which belong to one and the same mesh.

- [Union of groups](#union-anchor)
- [Intersection of groups](#intersection-anchor)
- [Cut of groups](#cut-anchor)

## Union of groups

This operation allows to create a new group in such a way that all
mesh elements that are present in the initial groups will be added to
the new one.

*To union groups:*

1. In the **Mesh** menu select the **Union Groups** item. The following dialog box will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/uniongroups.png)

   In this dialog box you should specify the name of the resulting group and set of groups which will be united.

   For example, we have two groups Group1 and Group2.
   The result of their **Union** will be Group12:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image133.gif)
   >
   > **Group1**
   >
   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image134.gif)
   >
   > **Group2**
   >
   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image135.gif)
   >
   > **Group12**
2. Click the **Apply** or **Apply and Close** button to confirm creation of the group.

**See Also** a sample TUI Script of a [Union of groups](tui_grouping_elements.md#tui-union-of-groups) operation.

## Intersection of groups

This operation allows to create a new group in such a way that all
mesh elements that are present in all initial groups together are added to the
new one.

*To intersect groups:*

1. In the **Mesh** menu select the **Intersect Groups** item. The following dialog box will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/intersectgroups.png)

   In this dialog box you should specify the name of the resulting group and set of groups which will be intersected.

   For example, we have two groups Group1 and Group2.
   The result of their **Intersection** will be Group12a:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image133.gif)
   >
   > **Group1**
   >
   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image134.gif)
   >
   > **Group2**
   >
   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image136.gif)
   >
   > **Group12a**
2. Click the **Apply** or **Apply and Close** button to confirm creation of the group.

**See Also** a sample TUI Script of an [Intersection of groups](tui_grouping_elements.md#tui-intersection-of-groups) operation.

## Cut of groups

This operation allows to create a new group in such a way that all
mesh elements that are present in the main groups but are absent in the
tool groups are added to the new one.

*To cut groups:*

1. In the **Mesh** menu select the **Cut Groups** item. The following dialog box will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/cutgroups.png)

   In this dialog box you should specify the name of the resulting group and groups which will be cut.

   For example, we have two groups Group1 and Group2.
   The result of their **Cut** will be Group12b:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image133.gif)
   >
   > **Group1**
   >
   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image134.gif)
   >
   > **Group2**
   >
   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image137.gif)
   >
   > **Group12b**
2. Click the **Apply** or **Apply and Close** button to confirm creation of the group.

**See Also** a sample TUI Script of a [Cut of groups](tui_grouping_elements.md#tui-cut-of-groups) operation.
