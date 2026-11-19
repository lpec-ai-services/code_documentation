<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/work_with_groups_page.html -->

# Working with groups

Creation and editing groups of sub-shapes of a geometrical object makes handling sub-shapes much easier. Boolean operations on groups are also available.

- [Create a Group](work_with_groups_page.md#create_groups_anchor)
- [Edit a Group](work_with_groups_page.md#edit_groups_anchor)
- [Union Groups](work_with_groups_page.md#union_groups_anchor)
- [Intersect Groups](work_with_groups_page.md#intersect_groups_anchor)
- [Cut Groups](work_with_groups_page.md#cut_groups_anchor)

## Create a group

![image56.png](https://docs.salome-platform.org/latest/gui/GEOM/image56.png)

This functionality is available in OCC viewer only.

To create a group of sub-shapes of a geometrical object in the main menu select **New entity > Group > Create**   
The following dialog box will appear:

![geomcreategroup.png](https://docs.salome-platform.org/latest/gui/GEOM/geomcreategroup.png)

In this Menu:

- **Shape Type** radio button defines the type of elements for the group (points, wires, faces, shells or solids).
- **Group Name** - allows defining the name of the group, by default, it is Group_n.
- Then, using the "Select" button, select the **Main Shape** (a geometrical object on which the group will be created).
- **Main Shape Selection restriction** button group allows limiting the range of available group elements,
  - **No restriction** button enables all sub-shapes of the Main Shape.
  - **Geometrical parts of the Second Shape** restricts the range of accessible elements to the sub-shapes of the Main Shape that geometrically coincide with the **Second Shape**.
  - **Only Sub-shapes of the Second Shape** restricts the range of accessible elements to the sub-shapes of the Main Shape that are sub-shapes of the **Second Shape**. This is useful because sometimes purely geometrical coincidence is not enough and it is necessary to work with shapes, which actually belong both to the main and the second shape.
- You can selectively display the selected elements using the following buttons:
  - **Show only selected** - displays only the sub-shapes selected in the list box.
  - **Hide selected** - hides the sub-shapes selected in the list box.
  - **Show all sub-shapes** - displays only the sub-shapes of the Main Shape.
- You can select the elements of your group in several ways:
  - You can select them manually in the 3D Viewer, and add to the group by clicking the **Add** button (keep down the Shift button on the keyboard to select several elements and add all them together). The indexes of the selected elements will be displayed in the list. To delete elements from the list, select them and click **Remove** button.
  - Clicking **Select All** button you can add all object's elements of a certain type in the list of the elements of the group. If the **Second Shape** is used, the elements are added according to **Main Shape Selection restriction** settings. To delete elements from the list, select them and click **Remove** button.
  - Filtering out some entities according to the specified threshold value or values (see below).
- Finally, confirm your selection by clicking **Apply and Close**  (also closes the Menu) or **Apply** (leaves the Menu open for creation of other groups), or skip it by clicking **Close** button.

The Result of the operation will be a **GEOM_Object**.

The **Filter** controls allow to automatically pick up entities, which satisfy specified threshold value(s). The numerical functor for each sub-shape that is compared with threshold value(s) is computed according to the shape's topological properties:

- length for edges and wires;
- area for faces and shells;
- volume for solids, compounds, compsolids.

Filtering capabilities are not available for vertices.

In order to filter out some entities:

- Activate one or two filtering controls by switching on the corresponding check boxes;
- Select the required threshold comparator type; the following choices are available:
  - **Less Than** or **Equal or Less Than** for the first comparator;
  - **Greater Than** or **Equal or Greater Than** for the second comparator;
- Enter the required threshold value (values);
- Press **Apply** button in the **Filter** group.

The entities, which satisfy the entered filtering parameters, will be automatically highlighted in the 3D viewer.

**Plot** button gives access to the [Shape Statistics](shape_statistics_operation_page.md) functionality with a simplified look-and-feel:

![shape_statistics_simple.png](https://docs.salome-platform.org/latest/gui/GEOM/shape_statistics_simple.png)

**TUI Command:** *geompy.CreateGroup(MainShape, ShapeType),* where MainShape is a shape for which the group is created, ShapeType is a type of shapes in the created group.   
**Arguments:** 1 Shape + Type of sub-shape.

Our **TUI Scripts** provide you with useful examples of [Create a Group](tui_working_with_groups_page.md#tui_create_groups_anchor) operation.

**Example:**

![image193.png](https://docs.salome-platform.org/latest/gui/GEOM/image193.png)

Groups on a cylinder

## Edit a group

![image57.png](https://docs.salome-platform.org/latest/gui/GEOM/image57.png)

This functionality is available in OCC viewer only.

To **Edit** an existing group in the main menu select **New entity > Group > Edit**. This menu is designed in the same way as the **Create a group** menu.

When a [GEOM](../GEOM/geompy_doc/namespaceGEOM.md) group is edited, the main shape appears in the 3D viewer in the same mode as it is displayed in the viewer. If the main shape was not displayed in the viewer, then the default mode defined in the preferences will be used.

**Working with Dialog Box:**

![editgroup.png](https://docs.salome-platform.org/latest/gui/GEOM/editgroup.png)

The subshapes already in the group are displayed in the 3D viewer with a specific color, defined via preferences. The IDs of the subshapes already in the group are also displayed in a specific color in the dialog box. When the user adds some subshapes, the new IDs are displayed in the other color.

The **Result** of the operation will be a **GEOM_Object**.

**TUI Command:**

- *geompy.AddObject(Group, SubShapeID),* where Group is a group to which a sub-shape has to be added, SubShapeID is an ID of the sub-shape to be added to the group.
- *geompy.RemoveObject(Group, SubShapeID),* where Group is a group from which a sub-shape has to be removed, SubShapeID is an ID of the sub-shape to be removed from the group.
- *geompy.GetObjectIDs(Group),* where Group is a group for which its object's are returned.   
  Returns: List of IDs.

**Arguments:** 1 Shape + its sub-shapes.

Our **TUI Scripts** provide you with useful examples of [Edit a Group](tui_working_with_groups_page.md#tui_edit_groups_anchor) operation.

## Union of groups

This operation allows to create a new group in such a way that all sub-shapes that are present in the initial groups will be added to the new one.

*To union groups:*

1. In the **New Entity** menu select the **Group** - **Union Groups** item. The following dialog box will appear:

   ![groups_union_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/groups_union_dlg.png)

   In this dialog box you should specify the name of the resulting group and select the groups, which will be united.
2. Click the **Apply** or **Apply and Close** button to confirm creation of the group.

**See Also** a sample TUI Script of a [Union of Groups](tui_working_with_groups_page.md#tui_union_groups_anchor) operation.

## Intersection of groups

This operation allows to create a new group in such a way that only the sub-shapes that are present in all initial groups are added to the new one.

*To intersect groups:*

1. In the **New Entity** menu select the **Group** - **Intersect Groups** item. The following dialog box will appear:

   ![groups_intersect_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/groups_intersect_dlg.png)

   In this dialog box you should specify the name of the resulting group and select the groups, which will be intersected.
2. Click the **Apply** or **Apply and Close** button to confirm creation of the group.

**See Also** a sample TUI Script of an   
[Intersection of Groups](tui_working_with_groups_page.md#tui_intersect_groups_anchor) operation.

## Cut of groups

This operation allows to create a new group in such a way that all sub-shapes that are present in the main groups but are absent in the tool groups are added to the new one.

*To cut groups:*

1. In the **New Entity** menu select the **Group** - **Cut Groups** item. The following dialog box will appear:

   ![groups_cut_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/groups_cut_dlg.png)

   In this dialog box you should specify the name of the resulting group and the groups which will be cut.
2. Click the **Apply** or **Apply and Close** button to confirm creation of the group.

Our **TUI Scripts** provide you with useful examples of [Cut of Groups](tui_working_with_groups_page.md#tui_cut_groups_anchor) operation.
