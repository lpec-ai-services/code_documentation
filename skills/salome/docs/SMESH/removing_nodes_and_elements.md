<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/removing_nodes_and_elements.html -->

# Removing nodes and elements

In MESH you can remove nodes and all types of cells of your mesh.

- [Removing nodes](#removing-nodes-anchor)
- [Removing node with reconnection](#removing-nodes-reconnect-anchor)
- [Removing orphan nodes](#removing-orphan-nodes-anchor)
- [Removing elements](#removing-elements-anchor)
- [Clearing Mesh Data](#clear-mesh-anchor)

## Removing nodes

**To remove a node:**

1. Select your mesh in the Object Browser or in the 3D viewer.
2. From the **Modification** menu choose **Remove** and from the associated submenu select the **Nodes**, or just click *“Remove nodes”* button ![rmn](https://docs.salome-platform.org/latest/gui/SMESH/_images/remove_nodes_icon.png) in the toolbar.
   The following dialog box will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/removenodes.png)

   In this dialog box you can specify one or several nodes:

   - choose mesh nodes with the mouse in the 3D Viewer. It is possible to select a whole area with a mouse frame; or
   - input the node IDs directly in **Node IDs** field. The selected nodes will be highlighted in the viewer; or
   - apply Filters. **Set filter** button allows to apply a filter to the selection of nodes. See more about filters in the [Selection filter library](selection_filter_library.md#selection-filter-library-page) page.
3. Click **Apply** or **Apply and Close** to confirm deletion of the specified nodes.

Note

Be careful while removing nodes because if you remove a definite node of your mesh all adjacent elements will be also deleted.

## Removing node with reconnection

This operation removes a node and changes surrounding faces in order to cover a hole appearing in the mesh. This operation applies to 2D triangle mesh only.

> ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/remove_node_reconnection.png)

**To remove a node:**

1. Select your mesh in the Object Browser or in the 3D viewer.
2. From the **Modification** menu choose **Remove** and from the associated submenu select the **Node with reconnection**, or just click *“Remove node with reconnection”* button ![rmnr](https://docs.salome-platform.org/latest/gui/SMESH/_images/remove_node_reconnection_icon.png) in the toolbar.
   The following dialog box will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/remove_node_reconnection_dlg.png)

   In this dialog box you can specify one node to remove:

   - choose a mesh node with the mouse in the 3D Viewer or
   - input the node ID directly in **ID** field. The selected node will be highlighted in the viewer.

   Activate **Preview** to see how faces will change.
3. Click **Apply** or **Apply and Close** to confirm deletion of the specified node.

## Removing orphan nodes

There is a quick way to remove all orphan (free) nodes.

*To remove orphan nodes:*

1. Select your mesh in the Object Browser or in the 3D viewer.
2. From the **Modification** menu choose **Remove** and from the associated submenu select **Orphan Nodes**, or just click *“Remove orphan nodes”* button ![rmon](https://docs.salome-platform.org/latest/gui/SMESH/_images/remove_orphan_nodes_icon.png) in the toolbar.
   The following Warning message box will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/removeorphannodes.png)
3. Confirm nodes removal by pressing “Yes” button.

## Removing elements

*To remove an element:*

1. Select your mesh in the Object Browser or in the 3D viewer.
2. From the **Modification** menu choose **Remove** and from the associated submenu select the **Elements**, or just click *“Remove elements”* button ![rme](https://docs.salome-platform.org/latest/gui/SMESH/_images/remove_elements_icon.png) in the toolbar.

   The following dialog box will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/removeelements.png)

   In this dialog box you can specify one or several elements:

   - choose mesh elements with the mouse in the 3D Viewer. It is possible to select a whole area with a mouse frame; or
   - input the element IDs directly in **ID Elements** field. The selected elements will be highlighted in the viewer; or
   - apply Filters. **Set filter** button allows to apply a filter to the selection of elements. See more about filters in the [Selection filter library](selection_filter_library.md#selection-filter-library-page) page.
3. Click **Apply** or **Apply and Close** to confirm deletion of the specified elements.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/remove_nodes1.png)

**The initial mesh**

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/remove_nodes2.png)

**The mesh with some elements removed**

## Clearing Mesh Data

*To remove all nodes and all types of cells in your mesh at once:*

1. Select your mesh in the Object Browser or in the 3D viewer.
2. From the **Modification** menu choose **Remove** and from the associated submenu select the **Clear Mesh Data**, or just click *“Clear Mesh Data”* button ![clr](https://docs.salome-platform.org/latest/gui/SMESH/_images/mesh_clear.png) in the toolbar. You can also right-click on the mesh in the Object Browser and select **Clear Mesh Data** in the pop-up menu.

Note

This command works in a different way in different situations:
:   - if the mesh is computed on a geometry, then *Clear Mesh Data* removes all elements and nodes.
    - if the mesh is not based on a geometry (imported, compound, created from scratch etc.), then *Clear Mesh Data* removes only the elements and nodes computed by algorithms. If no such elements or nodes have been created, can remove nothing.

**See Also** a sample TUI Script of a [Removing Nodes and Elements](tui_modifying_meshes.md#tui-removing-nodes-and-elements) operation.
