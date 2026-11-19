<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_groups_page.html -->

# Generation of Groups

This option is available in some dialogs. To activate it please check **Generate Groups** check box. When it is checked, it is possible to define the prefix for generated groups names using **Group Names Prefix** input field.

![gen_group_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/gen_group_dlg.png)

Generate groups option in a dialog

The groups are created along with the result of the operation when **Apply** or **Apply and Close** button is clicked. Each generated group represents a set of sub-shapes of the result that satisfies certain conditions. The groups of the following types can be generated:

- **Down** - sub-shapes starting the result, e.g. bottom lid for the pipe creation operation.
- **Up** - sub-shapes ending the result, e.g. top lid for the pipe creation operation.
- **Side1**, **Side2** - sub-shapes corresponding to each side of the result.
- **Other** - faces generated from the bounding edges of **Down** group.

The groups are named according to the following naming rule: If **Group Names Prefix** is set **<Prefix>_<Type>**, otherwise the name is  <Type>. The following figure shows group names created with the prefix **Group:**

![gen_group_tree.png](https://docs.salome-platform.org/latest/gui/GEOM/gen_group_tree.png)

Group_Down, Group_Up, Group_Side1 and Group_Side2 are generated

The general behavior of this functionality is the following:

- If **Generate Groups** option is not set, the groups are not generated.
- If starting and ending sub-shapes of the result are the same, e.g. if there is a closed path for pipe construction, **Generate Groups** option is disabled in the dialog box:

  ![gen_group_disabled.png](https://docs.salome-platform.org/latest/gui/GEOM/gen_group_disabled.png)

  Disabled option in the Pipe Construction dialog if the path is closed
- Otherwise If the path is not closed edge/wire, the groups are created depending on the profile:
  - Profile is unclosed edge or wire: **Down**, **Up**, **Side1**, **Side2:**

    ![gen_group_sides.png](https://docs.salome-platform.org/latest/gui/GEOM/gen_group_sides.png)

    Pipe with created groups Down(Red), Up(Green), Side1(Blue) and Side2(Yellow)
  - Profile is closed edge or wire, face or shell: **Down**, **Up**, **Other:**

    ![gen_group_other.png](https://docs.salome-platform.org/latest/gui/GEOM/gen_group_other.png)

    Created groups Down(Red), Up(Green) and Other(Yellow)

**Down** and **Up** groups contain:

- Edges if the profile is edge or wire;
- Faces if the profile is face or shell.

**Side1** and **Side2** groups contain edges generated from the first and last vertices of the profile edge or wire correspondingly. The first and last vertices are determined taking into account edge/wire orientation.

**Other** group represents faces generated from the bounding edges of profile.

The behavior in TUI is the following:

- Each Python function that supports groups generation has a flag **IsGenerateGroups** which is equal to **False** by default.
- If **IsGenerateGroups** is not set the groups are not created; the returned value is GEOM_Object that represents a result of the operation.
- If **IsGenerateGroups** is set the operation returns a list of GEOM_Object. Its first element is a result, the remaining ones are the groups in the order: **Down**, **Up**, **Side1**, **Side2** for opened profile or **Down**, **Up**, **Other** for closed profile.
- If **IsGenerateGroups** is set and the path is closed an error occurs.
