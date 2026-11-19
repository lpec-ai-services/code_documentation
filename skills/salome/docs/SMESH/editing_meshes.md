<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/editing_meshes.html -->

# Editing Meshes

After you have created a mesh or sub-mesh with definite applied meshing algorithms and hypotheses you can edit your mesh by **assigning** other algorithms and/or hypotheses or **unassigning** the applied hypotheses and algorithms. The editing proceeds in the same way as
[Mesh Creation](constructing_meshes.md#create-mesh-anchor).

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/createmesh-inv3.png)

You can also change values for the current hypothesis by clicking the
*“Edit Hypothesis”* ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image122.png) button.

Mesh entities generated before using changed hypotheses are automatically removed.

See how the mesh constructed on a geometrical object
changes if we apply different meshing parameters to it.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/edit_mesh1.png)

**Example of a mesh with Max. Element area 2D hypothesis roughly corresponding to 1D hypotheses on edges**

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/edit_mesh_change_value_hyp.png)

**And now the Max Element area is greatly reduced**

**See Also** a sample TUI Script of an [Edit Mesh](tui_creating_meshes.md#tui-editing-mesh) operation.
