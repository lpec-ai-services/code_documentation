<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/CollectionPlugin/groupShapeFeature.html -->

# Group Shape

Group shape produces a new shape from union of all the elements of the selected groups.
To create a Group Shape in the active part:

1. select in the Main Menu *Features - > Group Shape* item or
2. click ![group_shape.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/group_shape.png) **Group Shape** button in the toolbar:

The following property panel appears.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/group_shape_property_panel.png)

Create a group shape operation

Input fields:

- **Name** defines the name of the group, by default, it is **GroupShape_n**.
- The list of selected groups of the same type. Multiple selection can be done manually in OCC 3D Viewer by mouse click with Shift button pressed or by rectangle selection. To delete entities from the list, select them and call pop-up menu *Delete* item.

Note, that operation is valid only for the groups of the same type.

**TUI Command**:

model.addGroupShape(Part_1_doc,

[model.selection("COMPOUND", "Group_1"), model.selection("COMPOUND", "Group_2")])
:   Parameters:
    :   - **part** – The current part object
        - **list** – A list of selected groups

    Returns:
    :   Created shape.

**See Also** a sample TUI Script of [Create Group Shape](TUI_groupShapeFeature.md#tui-create-group-shape) operation.
