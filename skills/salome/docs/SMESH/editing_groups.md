<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/editing_groups.html -->

# Editing groups

*To edit an existing group of elements:*

1. Select your group in the Object Browser and in the **Mesh** menu click the **Edit Group** item or *“Edit Group”* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image74.gif) in the toolbar.

   The following dialog box will appear for **standalone group**:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/editgroup.png)

   In this dialog box you can modify the name and the color of your group. And you can add or remove the elements composing the group.

   The following dialog box will appear for **group on geometry**:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/editgroup_on_geom.png)

   In this dialog box you can modify only the name and the color of your group.

   The following dialog box will appear for **group on filter**:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/editgroup_on_filter.png)

   In this dialog box you can modify the name, the color and the criteria of the filter of your group.

   For more information see [Creating groups](creating_groups.md#creating-groups-page) page.
2. Click the **Apply** or **Apply and Close** button to confirm modification of the group.

## Convert to standalone group

*To convert an existing group on geometry or a group on filer into a standalone group and modify its contents:*

1. Select your group on geometry or on filter in the Object Browser and in the **Mesh** menu click the **Edit Group as Standalone** item ![edit](https://docs.salome-platform.org/latest/gui/SMESH/_images/image74.gif).

   The selected group will be converted into a standalone group and its contents can be modified.
2. Click the **Apply** or **Apply and Close** button to confirm modification of the group.

**See also:** A sample TUI Script of an [Edit a Group](tui_grouping_elements.md#tui-edit-group) operation.
