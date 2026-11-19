<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/create_groups_from_geometry.html -->

# Create Groups from Geometry

This operation allows creating groups on geometry on all selected shapes. Only the main shape of the mesh and its sub-shapes can be selected.

The type of each new group is defined automatically by the nature of the **Geometry**.
The group names will be the same as the names of geometrical objects.

To use this operation, select in the **Mesh** menu or in the contextual menu in the Object browser **Create Groups from Geometry** item.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/create_groups_from_geometry.png)

In this dialog **Elements** group contains a list of shapes, on which groups of elements will be created; **Nodes** group contains a list of shapes, on which groups of nodes will be created.

**See Also** a sample TUI Script of a [Create a Group on Geometry](tui_grouping_elements.md#tui-create-group-on-geometry) operation.
