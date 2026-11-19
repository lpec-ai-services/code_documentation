<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/grouping_elements.html -->

# Grouping elements

In Mesh module it is possible to create groups of mesh entities: nodes, edges, faces, volumes, 0D elements or balls. One group contains elements of only one type. Groups, unlike sub-meshes, are exported along with mesh entities into the files of following formats: MED, UNV, and CGNS. The group has a color attribute which is used for visualization only and is not exported.

There are three types of groups different by their internal organization:

1. **Standalone group** is a static set of mesh entities. Its contents can be explicitly controlled by the user. Upon removal of the entities included into the group, e.g. due to modification of meshing parameter, the group becomes empty and its content can be restored only manually. Hence it is reasonable to create standalone groups when the mesh generation is finished and mesh quality is verified.
   :   Warning

       Creation and edition of large standalone groups in [Create group](creating_groups.md#creating-groups-page) dialog using manual edition is problematic due to poor performance of the dialog.
2. **Group on geometry** is associated to a sub-shape or a group of sub-shapes of the main shape and includes mesh entities generated on these geometrical entities. The association to a geometry is established at group construction and cannot be changed. The group contents are always updated automatically, hence the group can be created even before mesh elements generation.
3. **Group on filter** encapsulates a [filter](about_filters.md#filters-page), which is used to select mesh entities composing the group from the whole mesh. Criteria of the filter can be changed at any time. The group contents are always updated automatically, hence the group can be created even before mesh elements generation.

The group on geometry and group on filter can be converted to a standalone group.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/groups_in_OB.png)

**Groups of different types look differently in the Object Browser**

The following ways of group creation are possible:

- [Create group](creating_groups.md#creating-groups-page) dialog allows creation of a group of any type: [Standalone group](creating_groups.md#standalone-group), [Group on geometry](creating_groups.md#group-on-geom) and [Group on filter](creating_groups.md#group-on-filter) using dedicated tabs.
- [Create Groups from Geometry](create_groups_from_geometry.md#create-groups-from-geometry-page) dialog allows creation of several groups on geometry at once.
- [Face Groups Separated By Sharp Edges](face_groups_by_sharp_edges.md) operation distributes all faces of the mesh among groups using sharp edges and/or existing 1D elements as group boundaries.
- Standalone groups of all nodes and elements of the chosen sub-mesh (type of elements depends on dimension of sub-mesh geometry) can be created using **Mesh -> Construct Group** menu item (available from the context menu as well).
- Standalone groups of any element type can be created basing on nodes of other groups - using [Group based on nodes of other groups](group_of_underlying_elements.md#group-of-underlying-elements-page) dialog.
- Standalone groups can be created by applying [Boolean operations](using_operations_on_groups.md#using-operations-on-groups-page) to other groups.
- Creation of standalone groups is an option of many [mesh modification](modifying_meshes.md#modifying-meshes-page) operations.

The created groups can be later:

- [Edited](editing_groups.md#editing-groups-page)
- [Deleted](deleting_groups.md#deleting-groups-page), either as an object or together with contained elements.
- The group on geometry and group on filter can be [converted into the standalone](editing_groups.md#convert-to-standalone) group.
- [Exported](importing_exporting_meshes.md#importing-exporting-meshes-page) into a file as a whole mesh.

In the Object Browser, if an item contains more than one child group, it is possible to sort the groups by name in ascending order using **Sort children** context menu item.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/smesh_sort_groups.png)

**Sorting groups**

An important tool, providing filters for creation of standalone groups and groups on filter is [Selection filter library](selection_filter_library.md#selection-filter-library-page).

**See Also** sample TUI Scripts of [Grouping Elements](tui_grouping_elements.md) operations.

**Table of Contents**

- [Creating groups](creating_groups.md)
  - [“Standalone Group”](creating_groups.md#standalone-group)
  - [“Group on Geometry”](creating_groups.md#group-on-geometry)
  - [“Group on Filter”](creating_groups.md#group-on-filter)
- [Create Groups from Geometry](create_groups_from_geometry.md)
- [Face Groups Separated By Sharp Edges](face_groups_by_sharp_edges.md)
- [Group Based on Nodes of Other Groups](group_of_underlying_elements.md)
- [Boolean operations on groups](using_operations_on_groups.md)
  - [Union of groups](using_operations_on_groups.md#union-of-groups)
  - [Intersection of groups](using_operations_on_groups.md#intersection-of-groups)
  - [Cut of groups](using_operations_on_groups.md#cut-of-groups)
- [Editing groups](editing_groups.md)
  - [Convert to standalone group](editing_groups.md#convert-to-standalone-group)
- [Deleting groups with content](deleting_groups.md)
