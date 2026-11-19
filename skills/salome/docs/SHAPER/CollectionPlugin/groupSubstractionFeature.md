<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/CollectionPlugin/groupSubstractionFeature.html -->

# Group Subtraction

Group subtraction produces a group containing all elements of the main groups but not present in the tool groups.
To create a Group Subtraction in the active part:

1. select in the Main Menu *Features - > Group Subtraction* item or
2. click ![group_substraction.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/group_substraction.png) **Group Subtraction** button in the toolbar:

The following property panel appears.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/group_substraction_property_panel.png)

Create a group subtraction operation

Input fields:

- **Name** defines the name of the group, by default, it is **GroupSubstraction_n**.
- The list of main groups. Multiple selection can be done manually in OCC 3D Viewer by mouse click with Shift button pressed or by rectangle selection. To delete entities from the list, select them and call pop-up menu *Delete* item.
- The list of tool groups. Selection approaches are the same as for the main groups.

Note, that operation is valid only if all the main groups and all the tool groups have the same type.

**TUI Command**:

model.addGroupSubstraction(Part_1_doc,

[model.selection("COMPOUND", "Group_1"), model.selection("COMPOUND", "Group_2")],

[model.selection("COMPOUND", "Group_3"), model.selection("COMPOUND", "Group_4")])
:   Parameters:
    :   - **part** – The current part object
        - **list** – A list of main groups
        - **list** – A list of tool groups

    Returns:
    :   Created group.

**See Also** a sample TUI Script of [Create Group Subtraction](TUI_groupSubstractionFeature.md#tui-create-group-substraction) operation.
