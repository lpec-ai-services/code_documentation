<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/dependency_tree_page.html -->

# Dependency Tree

- [General description](dependency_tree_page.md#dependency_tree_general_description_anchor)
- [Nodes](dependency_tree_page.md#dependency_tree_nodes_anchor)
- [Links](dependency_tree_page.md#dependency_tree_links_anchor)
- [Operations](dependency_tree_page.md#dependency_tree_operations_anchor)
- [Navigation](dependency_tree_page.md#dependency_tree_navigation_anchor)
- [Context menu](dependency_tree_page.md#dependency_tree_popup_menu_anchor)

## General description

You can display the ascendants and descendants of object(s) in a tree structure to better understand the relations between the GEOM objects in a study .

To build the dependency tree, select the necessary object or objects (multiple selection is supported) in the Object Browser or OCC Viewer and call "Show dependency tree" context menu item.

![tree_example.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_example.png)

"Dependency Tree" view window will display the dependency tree for the selected object. It is also possible to select an object(s) directly in the "Dependency Tree" view and to rebuild the tree by selecting "Rebuild the tree" context menu item.

All necessary parameters of Dependency Tree Viewer can be edited in the [Preferences](geometry_preferences_page.md#pref_dependency_tree).

Note
:   This functionality is available only if the GUI module is built with Graphics view (option SALOME_USE_GRAPHICSVIEW is ON when building GUI module).

---

## Nodes

Tree nodes in the Dependency Viewer are named according to the study names of the corresponding objects.

All nodes have fixed size, so long names are cut; the full object name can be seen in the tool-tip when the cursor is hovered over the node.

"Dependency Tree" view supports the following states of nodes:

- **Main node** - corresponds to the main object(s) selected in Object Browser, OCC Viewer or Dependency Tree Viewer;

![tree_main_node.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_main_node.png)

- **Default node** - ascendant or descendant node of the dependency tree corresponding to an object published in the study;

![tree_default_node.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_default_node.png)

- **Unpublished node** - corresponds to an object that was not published in the study;

![tree_unpublished_node.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_unpublished_node.png)

- **Highlighted node** - the state of a node when the mouse cursor is hovered over it;

![tree_highlighted_node.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_highlighted_node.png)

- **Selected node** - the state of node when the user clicks the left mouse button it.

![tree_selected_node.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_selected_node.png)

---

## Links

Dependency Tree Viewer shows oriented links between nodes to represent the dependency direction. The viewer supports the following states of links:

- **Unidirectional link** - shows that object **B** depends on object **A**;

![tree_unidir_link.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_unidir_link.png)

- **Bidirectional link** - shows that object **B** depends on object **A** and, at the same time, object **A** depends on object **B**;

![tree_bidir_link.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_bidir_link.png)

- **Self-dependency link** - shows that an object depends on itself;

![tree_selfdep_link.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_selfdep_link.png)

- **Cyclic dependency links** - shows cyclic dependency of some nodes.

![tree_cycldep_link.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_cycldep_link.png)

---

## Viewer Operations

The dependency tree of a chosen GEOM object is displayed in the dedicated 2D view window.   
The functionalities of 2D viewer are available via its Viewer Toolbar.

Buttons marked with small downward triangles have extended functionality which can be accessed by locking on them with left mouse button.

![tree_tool_bar.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_tool_bar.png)

**Dump View** - exports the current scene in bmp, png or jpeg image format.

![tree_view_dump.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_view_dump.png)

**Fit all** - scales the presentation so that it could fit within the Viewer boundaries.

![tree_view_fitall.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_view_fitall.png)

**Fit area** - resizes the view to place in the visible area only the contents of a frame drawn with pressed left mouse button.

![tree_view_fitarea.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_view_fitarea.png)

**Fit selection** - resizes the view to fit in the visible area only currently selected objects.

![tree_view_fitselect.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_view_fitselect.png)

**Zoom** - allows to zoom in and out.

![tree_view_zoom.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_view_zoom.png)

**Panning** - if the represented objects are greater that the visible area and you don't wish to use **Fit all** functionality, click on this button and you'll be able to drag the scene to see its remote parts.

![tree_view_pan.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_view_pan.png)

**Global panning** - allows to select a point to be the center of the presentation showing all displayed objects in the visible ares.

![tree_view_glpan.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_view_glpan.png)

**Hierarchy depth** - allows to change the number of hierarchy levels to be shown in the dependency tree.

![tree_hierarchy_type.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_hierarchy_type.png)

- Level 1 corresponds to the parents and children of the selected object(s);
- Level 2 adds the grand-parents and grand-children of the selected object(s);
- etc...

**Display ascendants** - allows showing/hiding the ascendants.

![tree_disp_ascendants.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_disp_ascendants.png)

**Display descendants** - allows showing/hiding the descendants.

![tree_disp_descendants.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_disp_descendants.png)

**Move nodes** -if checked, it is possible to move nodes in the viewer.

![tree_move_nodes.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_move_nodes.png)

**Update** - updates the dependency tree view, reflecting changes introduced in the hierarchy.

![tree_button_update.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_button_update.png)

---

## Selection and Shortcuts

- It is possible to select multiple nodes in the view by rectangle selection or by clicking nodes when **Shift** button is pressed.

Holding **Ctrl** key with pressed mouse buttons performs the following view transformations:

- Ctrl + left mouse button - zooming;
- Ctrl + middle mouse button - panning;

---

## Context Menu

The following operations are available from the context menu of the selected object.

![tree_popup_menu1.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_popup_menu1.png)

- **Show** - shows the selected object(s) in OCC 3D Viewer;
- **Show Only** - shows only the selected object(s) in OCC 3D Viewer;
- **Rebuild the tree** - rebuilds the dependency tree for selected object(s);
- [Reduce study](reduce_study_page.md) - allows reducing the study.

  ![tree_popup_menu2.png](https://docs.salome-platform.org/latest/gui/GEOM/tree_popup_menu2.png)
- It is also possible to customize the background of Dependency Tree 2D Viewer using the corresponding context menu command.
