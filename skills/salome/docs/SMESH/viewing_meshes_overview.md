<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/viewing_meshes_overview.html -->

# Viewing meshes

By default a just [computed](constructing_meshes.md#compute-anchor) mesh will be
automatically displayed in the **VTK 3D Viewer**. (You can switch
off [Automatic Update](mesh_preferences.md#automatic-update-pref) preference parameter
to prevent this.)
Click **Display only** to hide all other objects at the same time.

**VTK 3D Viewer** is described in detail in the documentation on **GUI module**.

Use the following [preference parameters](mesh_preferences.md#mesh-preferences-page)
to adjust how the mesh is displayed by default:

- [Automatic Update](mesh_preferences.md#automatic-update-pref)
- [Default display mode](mesh_preferences.md#display-mode-pref)
- [Representation of the 2D quadratic elements](mesh_preferences.md#quadratic-2d-mode-pref)
- All parameters of [Mesh](mesh_preferences.md#mesh-tab-preferences) tab page of Preferences dialog.

After the mesh has appeared in the Viewer, you can select it with
left mouse click and get information about it, change its
presentation parameters and access to other useful options by
right-clicking on the selected mesh.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/dialog.png)

- **Rename** - allows to rename the object in the Object browser.
- **Hide all** - allows to hide all objects in the viewer.
- **Update** - refreshes the presentation of your mesh in the 3D Viewer, applying all recent changes.
- [Mesh Information](mesh_infos.md#mesh-infos-page) - provides information about the mesh.
- [Find Element by Point](find_element_by_point.md#find-element-by-point-page) - allows to find all mesh elements, to which belongs a point with the given coordinates.
- **Auto Color** - switch on / off auto-assigning colors for the groups. If switched on, a default color of a new group in [Create Group](creating_groups.md#creating-groups-page) dialog is chosen randomly.
- [Numbering](numbering.md#numbering-page) - allows to display the ID numbers of all meshing elements or nodes composing your mesh in the viewer.
- [Display Mode](display_mode.md#display-mode-page) - allows to select between Wireframe, Shading and Nodes presentation.
- [Display Entity](display_entity.md#display-entity-page) - allows to display entities by types (Faces, Edges, Volumes etc.).

- **2D Quadratic** - allows to select between the representation of quadratic edges as broken **lines** or as **arcs**. A default representation can be set in [Preferences](mesh_preferences.md#quadratic-2d-mode-pref). Arc representation applies to 1D and 2D elements only.
- **Orientation of faces** - shows vectors of orientation of faces of the selected mesh. The orientation vector is shown for each 2D mesh element and for each free facet of a 3D mesh element. The vector direction is calculated by the first three nodes of the face produced by vectors n1-n2 and n1-n3.
- [Properties](colors_size.md#colors-size-page) - allows to define several visual properties, including color of elements, shrink size, …
- [Transparency](transparency.md#transparency-page) - allows to change the transparency of mesh elements.
- [Controls](about_quality_controls.md#quality-page) - graphically presents various information about the mesh.
- **Hide** - allows to hide the selected mesh from the viewer.
- **Show Only** - allows to display only the selected mesh, hiding all others from the viewer. If [Fit All upon Show Only](mesh_preferences.md#display-mode-pref) Preference option is active, *Fit All* command is additionally performed.
- [Clipping](clipping.md) - allows to create cross-sections of the displayed objects.
- **Dump view** - exports an object from the viewer in bmp, png or jpeg image format.
- **Change background** - allows to redefine the background color. By default it is black.
- **View Operations** - allows to show/hide the visualization toolbar in the Viewer window.
- **Recording Operations** - allows to show/hide the recording toolbar in the Viewer window.

**Table of Contents**

- [Mesh Information](mesh_infos.md)
- [Find Element by Point](find_element_by_point.md)
- [Numbering](numbering.md)
- [Display Mode](display_mode.md)
- [Display Entity](display_entity.md)
- [Properties](colors_size.md)
- [Transparency](transparency.md)
- [Clipping](clipping.md)
