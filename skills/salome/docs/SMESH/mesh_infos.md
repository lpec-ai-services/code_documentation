<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/mesh_infos.html -->

# Mesh Information

The user can obtain information about the selected mesh object (mesh, sub-mesh or group) using **Mesh Information** dialog box.

To view the **Mesh Information**, select your mesh, sub-mesh or group in the **Object Browser** and invoke **Mesh Information** item from the **Mesh** menu or from the context menu, or click *“Mesh Information”* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image49.png) in the toolbar.

The **Mesh Information** dialog box provides three tab pages:

- [Base Info](#advanced-mesh-infos-anchor) - to show base and quantitative information about the selected mesh object.
- [Element Info](#mesh-element-info-anchor) - to show detailed information about the selected mesh nodes or elements.
- [Additional Info](#mesh-addition-info-anchor) - to show additional information available for the selected mesh, sub-mesh or group object.
- [Quality Info](#mesh-quality-info-anchor) - to show overall quality information about the selected mesh, sub-mesh or group object.

## Dump Mesh Infos

The button **Dump** allows printing the information displayed in the dialog box to a .txt file. The dialog for choosing a file also allows to select which tab pages to dump via four check-boxes. The default state of the check-boxes can be changed via [Mesh information](mesh_preferences.md#mesh-information-pref) preferences.

## Base Information

The **Base Info** tab page of the dialog box provides general information on the selected object - mesh, sub-mesh or mesh group: name, type, total number of nodes and elements separately for each type: 0D elements, edges, faces, volumes, balls.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/advanced_mesh_infos.png)

***“Base Info”* page**

## Mesh Element Information

The **Element Info** tab page of the dialog box gives detailed information about the selected mesh node(s) or element(s), namely:

- For a node:
  :   - Node ID;
      - Coordinates (X, Y, Z);
      - Connectivity information (connected elements); double click in this line reveals information about these elements;
      - Position on a shape (for meshes built on a geometry);
      - Groups information (names of groups the node belongs to).![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/eleminfo1.png)

      ***“Element Info”* page, node information**
- For an element:
  :   - Element ID;
      - Type (triangle, quadrangle, etc.);
      - Gravity center (X, Y, Z coordinates);
      - Connectivity information (connected nodes); double click in a line of a node reveals the information about this node;
      - Quality controls (area, aspect ratio, volume, etc.);
      - Position on a shape (for meshes built on a geometry);
      - Groups information (names of groups the element belongs to).![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/eleminfo2.png)

      ***“Element Info”* page, element information**

The user can either input the ID of a node or element he wants to analyze directly in the dialog box or select the node(s) or element(s) in the 3D viewer.

If **Show IDs** is activated, IDs of selected nodes or elements are displayed in the 3D viewer.

Note

The information about the groups, to which the node or element belongs, can be shown in a short or in a detailed form. By default, for performance reasons, this information is shown in a short form (group names only). The detailed information on groups can be switched on via [Show details on groups in element information tab](mesh_preferences.md#group-detail-info-pref) option of [Mesh preferences](mesh_preferences.md#mesh-preferences-page).

## Additional Information

The **Additional Info** tab page of the dialog box provides an additional information on the selected object: mesh, sub-mesh or group.

For a mesh object, the following information is shown:

- Name
- Type: based on geometry, imported, standalone
- Shape (if mesh is based on geometry)
- File (if mesh is imported from the file)
- Groups
- Sub-meshes

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/addinfo_mesh.png)

***“Additional Info”* page, mesh information**

For a sub-mesh object, the following information is shown:

- Name
- Parent mesh
- Shape

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/addinfo_submesh.png)

***“Additional Info”* page, sub-mesh information**

### Additional info for Group

For a group object, the following information is shown:

- Name
- Parent mesh
- Type: standalone, group on geometry, group on filter
- Entity type: node, edge, face, volume
- Size
- Color
- Number of underlying nodes (for non-nodal groups)

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/addinfo_group.png)

***“Additional Info”* page, group information**

Note

For the performance reasons, the number of underlying nodes is computed only by demand. For this, the user should press the “Compute” button (see picture). Also, the number of underlying nodes is automatically calculated if the size of the group does not exceed the [Automatic nodes compute limit](mesh_preferences.md#nb-nodes-limit-pref) preference value (zero value means no limit).

## Quality Information

The **Quality Info** tab provides overall information about mesh quality controls on the selected object - mesh, sub-mesh or mesh group:

- Name;
- Nodes information:
  :   - Number of free nodes;
      - Maximal number of elements connected to a node;
      - Number of double nodes;
- Edges information:
  :   - Number of double edges;
- Faces information:
  :   - Number of double faces;
      - Number of over-constrained faces;
      - Aspect Ratio histogram;
- Volume information:
  :   - Number of double volumes;
      - Number of over-constrained volumes;
      - Aspect Ratio 3D histogram.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/ctrlinfo.png)

***“Quality Info”* page**

Note

It is possible to change **Double nodes tolerance**, which will be used upon consequent pressing *Compute* button. The default value of the tolerance can be set via the [Quality controls](mesh_preferences.md#dbl-nodes-tol-pref) preferences.

Note

For performance reasons, all quality control values for big meshes are computed only by demand. For this, press the *Compute* button. Also, values are automatically computed if the number of nodes / elements does not exceed the [Automatic controls compute limit](mesh_preferences.md#auto-control-limit-pref) set via the [Mesh information](mesh_preferences.md#mesh-information-pref) preferences (zero value means that there is no limit).

Note

The plot functionality is available only if the GUI module is built with Plot 2D Viewer (option SALOME_USE_PLOT2DVIEWER is ON when building GUI module).

See the [TUI Example](tui_viewing_meshes.md#tui-viewing-mesh-infos) for basic mesh information and [TUI Example](tui_viewing_meshes.md#tui-node-element-mesh-infos).
