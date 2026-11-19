<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/adding_nodes_and_elements.html -->

# Adding nodes and elements

In MESH you can add to your mesh different elements such as:

- [Nodes](#adding-nodes-anchor)
- [0D Elements](#adding-0delems-anchor)
- [0D elements on Element Nodes](#adding-0delems-on-all-nodes-anchor)
- [Ball Elements](#adding-balls-anchor)
- [Edges](#adding-edges-anchor)
- [Triangles](#adding-triangles-anchor)
- [Quadrangles](#adding-quadrangles-anchor)
- [Polygons](#adding-polygons-anchor)
- [Tetrahedrons](#adding-tetrahedrons-anchor)
- [Hexahedrons](#adding-hexahedrons-anchor)
- [Hexagonal prism](#adding-octahedrons-anchor)
- [Polyhedrons](#adding-polyhedrons-anchor)

The convention of nodal connectivity of elements used in SALOME is the MED library convention. You can consult the description of nodal connectivity of elements in the documentation on MED library or [here](connectivity.md#connectivity-page).

*To add a node or an element to your mesh:*

1. Select your mesh in the Object Browser or in the 3D viewer.
2. From the **Modification** menu choose the **Add** item, the following associated sub-menu will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image152.png)

   From this sub-menu select the type of element which you would like to add to your mesh.

   Note

   All dialogs for new node or element adding to the mesh provide the possibility to automatically add a node or element to the specified group or to create it anew using **Add to group** box, that allows choosing an existing group for the created node or element or giving the name to a new group. By default, the **Add to group** check box is switched off. If the user switches this check box on, the combo box listing all currently existing groups of the corresponding type becomes available. By default, no group is selected. In this case, when the user presses **Apply** or **Apply & Close** button, the warning message box informs the user about the necessity to input new group name. The combo box lists groups of all the [three types](grouping_elements.md#grouping-elements-page): both [standalone groups](creating_groups.md#standalone-group), [groups on filter](creating_groups.md#group-on-filter), and [groups on geometry](creating_groups.md#group-on-geom). If the user chooses a group on geometry or on filter, he is warned and proposed to convert this group to standalone. If the user rejects conversion operation, it is cancelled and a new node/element is not created!

**See Also** sample TUI Scripts of [Adding Nodes and Elements](tui_modifying_meshes.md#tui-adding-nodes-and-elements) operations.

## Adding nodes

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/addnode.png)

In this dialog box set coordinates for your node in the **Coordinates** set of fields and click the **Apply** or **Apply and Close** button. Your node will be created:

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/add_node.png)

## Adding 0D elements

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/add0delement.png)

In this dialog box specify nodes which will form your 0D elements by selecting them in the 3D viewer. Activate **Allow duplicate elements**
to get several 0D elements on a node. Click the **Apply** or **Apply and Close** button. Your 0D elements will be created:

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/add_0delement.png)

## Making 0D elements on Element Nodes

There is another way to create 0D elements. It is possible to create 0D elements on all nodes of the selected mesh, sub-mesh, or a group of elements or nodes.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/dlg_0D_on_all_nodes.png)

In this dialog

- The radio-buttons allow choosing the type of object to create 0D elements on.

  > - **Mesh, sub-mesh, group** - this button allows selecting a mesh, a sub-mesh or a group to create 0D elements on the nodes of its elements. The name of the selected object is shown in the dialog.
  > - **Elements** - this button allows selecting elements in the VTK viewer or typing their IDs in the dialog.
  > - **Nodes** - this button allows selecting nodes to create 0D elements on in the VTK viewer or typing their IDs in the dialog.
- **Set Filter** button allows selecting elements or nodes by filtering mesh elements or nodes with different criteria (see [Filter usage](selection_filter_library.md#filtering-elements)).
- Activate **Allow duplicate elements** to get several 0D elements on a node.
- Switching on **Add to group** check-box allows specifying the name of the group to which all created or found (existing) 0D elements will be added. You can either select an existing group from a drop-down list, or enter the name of the group to be created. If a selected existing [group](grouping_elements.md#grouping-elements-page) is not Standalone (Group On Geometry or Group On Filter) it will be converted to Standalone.

Warning

If **Add to group** is activated it has to be filled in.

## Adding ball elements

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/addball.png)

In this dialog box specify the nodes, which will form your ball elements, either by selecting them in the 3D viewer or by manually entering their IDs, specify the ball diameter and click the **Apply** or **Apply and Close** button.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/add_ball.png)

## Adding edges

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/addedge.png)

In this dialog box specify the nodes which will form your edge by selecting them in the 3D viewer with pressed Shift button and click the **Apply** or **Apply and Close** button. Your edge will be created:

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/add_edge.png)

## Adding triangles

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/addtriangle.png)

In this dialog box specify the nodes which will form your triangle by selecting them in the 3D viewer with pressed Shift button and click the **Apply** or **Apply and Close** button. Your triangle will be created:

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/add_triangle.png)

## Adding quadrangles

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/addquadrangle.png)

In this dialog box specify the nodes which will form your quadrangle by selecting them in the 3D viewer with pressed Shift button and click the **Apply** or **Apply and Close** button. Your quadrangle will be created:

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/add_quadrangle.png)

## Adding polygons

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/addpolygon.png)

In this dialog box specify the nodes which will form your polygon by selecting them in the 3D viewer with pressed Shift button and click the **Apply** or **Apply and Close** button.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/add_polygone.png)

## Adding tetrahedrons

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/addtetrahedron.png)

In this dialog box specify the nodes which will form your tetrahedron by selecting them in the 3D viewer with pressed Shift button and click the **Apply** or **Apply and Close** button. Your tetrahedron will be created:

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image70.jpg)

## Adding hexahedrons

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/addhexahedron.png)

In this dialog box specify the nodes which will form your hexahedron by selecting them in the 3D viewer with pressed Shift button and click
the **Apply** or **Apply and Close** button. Your hexahedron will be created:

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image71.jpg)

## Adding hexagonal prism

In the Add Hexagonal Prism dialog box specify the nodes which will form your hexagonal prism by selecting them in the 3D viewer with pressed Shift button and click the **Apply** or **Apply and Close** button. Your hexagonal prism will be created:

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image_octa12.png)

## Adding polyhedrons

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/a-createpolyhedralvolume.png)

There are two different ways to add polyhedral volumes.

If you select **Node** as **Elements Type** you will specify the nodes which will form the faces of your polyhedron by selecting the nodes in the 3D viewer with pressed Shift button and clicking the **Add** button to add the face in the list of Faces by Nodes, which will form your polyhedron. Note, that it could be very useful to toggle Polyhedron Preview checkbox to see the results of your selection.
The second way is somewhat simpler, however, there are cases when it does not provide you with the necessary level of precision. If you select **Face** as **Elements Type**, you will be able to select the faces which will form your polyhedron in the 3D viewer with pressed Shift button. If you’ve managed to obtain the necessary result, click the **Apply** or **Apply and Close** button. Your polyhedron will be created:

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/add_polyhedron.png)
