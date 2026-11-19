<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/extrusion_along_path.html -->

# Extrusion along Path

In principle, **Extrusion along Path** works in the same way as [Extrusion](extrusion.md#extrusion-page), the main difference is that we define not a vector, but a path of extrusion which must be an 1D mesh or 1D sub-mesh.
To get an idea of how this algorithm works, examine several examples, starting from the most simple case of extrusion along a straight edge.
In the examples the sample mesh will be extruded along different paths and with different parameters.
This 2D mesh has two quadrangle faces and seven edges. Look at the picture, where white digits are the node numbers and green are the element numbers:

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/mesh_for_extr_along_path.png)

## Extrusion along a straight edge

(not using base point or angles)

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/straight_before.png)

**The image shows a 1D path mesh, built on a linear edge, and the initial 2D mesh.**

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/straight_after.png)

**The image shows the result of extrusion of two edges (#1 and #2) of the initial mesh along the path.**

Note

Node #1 of path mesh has been selected as Start node.

### Extrusion along a curvilinear edge

(with and without angles)

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/curvi_simple_before.png)

**The image shows a 1D path mesh, built on curvilinear edge, and the initial 2D mesh.**

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/curvi_simple_after.png)

**The central image shows the result of extrusion of one edge (#2) of the initial mesh along the path.**

Note

Node #1 of path mesh has been selected as **Start node**.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/curvi_angles_after.png)

**The same, but using angles {45, 45, 45, 0, -45, -45, -45}**

### Extrusion of a 2D face along a mesh built on a wire

In this example the path mesh has been built on a wire containing 3 edges. Node 1 is a start node. Linear angle variation by 180 degrees has also been applied.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/extr_along_wire_before.png)

**Meshed wire**

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/extr_along_wire_after.png)

**The resulting extrusion**

### Extrusion of 2d elements along a closed path

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/circle_simple_before.png)

**The image shows a path mesh built on a closed edge (circle).**

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/circle_simple_after.png)

**The central image shows the result of extrusion of both faces of the initial mesh.**

Note

Note, that no sewing has been done, so, there are six coincident nodes and two coincident faces in the resulting mesh.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/circle_angles_after.png)

**The same, but using angles {45, -45, 45, -45, 45, -45, 45, -45}**

*To use Extrusion along Path:*

1. From the **Modification** menu choose the **Extrusion along a path** item or click *“Extrusion along a path”* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image101.png) in the toolbar.

   The following dialog will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/extrusion_along_path_dlg.png)
2. In this dialog:

   > - Use *Selection* button ![sel](https://docs.salome-platform.org/latest/gui/SMESH/_images/image120.png) to specify what you are going to select at a given moment, **Nodes**, **Edges** or **Faces**.
   > - Specify **Nodes**, **Edges** and **Faces**, which will be extruded, by one of following means:
   >
   >   > - **Select the whole mesh, sub-mesh or group** activating this check-box.
   >   > - Choose mesh elements with the mouse in the 3D Viewer. It is possible to select a whole area with a mouse frame.
   >   > - Input the element IDs directly in **Node IDs**, **Edge IDs** and **Face IDs** fields. The selected elements will be highlighted in the viewer, if the mesh is shown there.
   >   > - Apply Filters. **Set filter** button allows to apply a filter to the selection of elements. See more about filters in the [Filter Dialog](selection_filter_library.md#filtering-elements) page.
   > - Define the **Path** along which the elements will be extruded.Path definition consists of several elements:
   >
   >   > - **Mesh or sub-mesh** - 1D mesh or sub-mesh, along which proceeds the extrusion.
   >   > - **Start node** - the start node of the Path. It is used to define the direction of extrusion.
   > - If you activate **Generate groups** check-box, the *result elements* created from *selected elements* contained in groups will be included into new groups named by pattern “<old group name>_extruded” and “<old group name>_top”. For example if a selected quadrangle is included in *g_Faces* group (see figures below) then result hexahedra will be included in *g_Faces_extruded* group and a quadrangle created at the “top” of extruded mesh will be included in *g_Faces_top group*.![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/extrusion_groups.png)
   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/extrusion_groups_res.png)
   >
   > This check-box is active only if there are some groups in the mesh.
3. There are two optional parameters, which can be very useful:

   - If the path of extrusion is curvilinear, at each iteration the extruded elements are rotated to keep its initial angularity to the curve. By default, the **Base point** around which the elements are rotated is the mass center of the elements (note that it can differ from the gravity center computed by *Geometry* module for the underlying shape), however, you can specify any point as the **Base point** and the elements will be rotated with respect to this point. Note that only the displacement of the **Base point** exactly equals to the path, and all other extruded elements simply keep their position relatively to the **Base point** at each iteration.
   - The elements can also be rotated around the path with rotation center at the **Base point** to get the resulting mesh in a helical fashion. You can set the values of angles at the right, add them to **Rotation angles** list at the left by pressing the *“Add”* button ![add](https://docs.salome-platform.org/latest/gui/SMESH/_images/add.png) and remove them from the list by pressing the *“Remove”* button ![rem](https://docs.salome-platform.org/latest/gui/SMESH/_images/remove.png).

     **Linear variation of angles** option allows defining the angle of gradual rotation for the whole path. At each step the elements will be rotated by *( angle / nb. of steps )*.
   - Each of optional **Scale factors** in the list is applied to nodes of a corresponding extrusion step unless **Linear variation of factors** is checked, is which case the scale factors are spread over all extrusion steps. **Base point** serves as a scaling canter.
     :   - *“Add”* button ![add](https://docs.salome-platform.org/latest/gui/SMESH/_images/add.png) adds a scale factor to the list.
         - *“Remove”* button ![rem](https://docs.salome-platform.org/latest/gui/SMESH/_images/remove.png) removes selected scale factors from the list.
4. Click **Apply** or **Apply and Close** button to confirm the operation. Mesh edges will be extruded into faces, faces into volumes. The external surface of the resulting 3d mesh (if faces have been extruded) is covered with faces, and corners with edges. If the path is closed, the resulting mesh can contain duplicated nodes and faces, because no sewing is done.

**See Also** a sample TUI Script of an [Extrusion along a Path](tui_modifying_meshes.md#tui-extrusion-along-path) operation.
