<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/CollectionPlugin/groupIntersectionFeature.html -->

# Group Intersection

Group intersection produces a group of elements present in all the selected groups.
To create a Group Intersection in the active part:

1. select in the Main Menu *Features - > Group Intersection* item or
2. click ![group_intersection.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/group_intersection.png) **Group Intersection** button in the toolbar:

The following property panel appears.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/group_intersection_property_panel.png)

Create a group intersection operation

Input fields:

- **Name** defines the name of the group, by default, it is **GroupIntersection_n**.
- The list of selected groups of the same type. Multiple selection can be done manually in OCC 3D Viewer by mouse click with Shift button pressed or by rectangle selection. To delete entities from the list, select them and call pop-up menu *Delete* item.

Note, that operation is valid only for the groups of the same type.

**TUI Command**:

model.addGroupIntersection(Part_1_doc,

[model.selection("COMPOUND", "Group_1"), model.selection("COMPOUND", "Group_2")])
:   Parameters:
    :   - **part** – The current part object
        - **list** – A list of selected groups

    Returns:
    :   Created group.

**See Also** a sample TUI Script of [Create Group Intersection](TUI_groupIntersectionFeature.md#tui-create-group-intersection) operation.
