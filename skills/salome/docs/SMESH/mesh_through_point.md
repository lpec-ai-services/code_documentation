<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/mesh_through_point.html -->

# Moving nodes

In mesh you can define a node at a certain point either

- by movement of the node closest to the point or
- by movement of a selected node to the point.
- by movement of a selected node to the point specified by mouse click.

*To displace a node:*

1. From the **Modification** menu choose the **Move node** item or click *“Move Node”* button in the toolbar.

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image67.png)
   >
   > ***“Move Node”* button**

   The following dialog will appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/meshtopass1.png)
   >
   > **Manual node selection**
   >
   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/meshtopass2.png)
   >
   > **Automatic node selection**
   >
   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/meshtopass3.png)
   >
   > **Manual node selection with mouse location**
2. Specify the way of node selection: manually (the first radio button) or automatically (the second radio button).
3. If the manual method is selected, select a node to move (X, Y, Z fields show the original coordinates of the node) or type the node ID.
4. Enter the coordinates of the destination point. You can click **Update Destination** button to set the coordinates of the destination point equal to the coordinates of the node to move.
5. Activate **Preview** check-box to show the result of move in the viewer.
6. Click the **Apply** or **Apply and Close** button to confirm the operation.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/moving_nodes1.png)

**The initial mesh**

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/moving_nodes2.png)

**The modified mesh**

**See Also** a sample TUI Script of a [Moving Nodes](tui_modifying_meshes.md#tui-moving-nodes) operation.
