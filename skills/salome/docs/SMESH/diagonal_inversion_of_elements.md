<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/diagonal_inversion_of_elements.html -->

# Diagonal inversion of two triangles

In MESH you can inverse the diagonal (edge) of a pseudo-quadrangle
formed by two neighboring triangles with one common edge.

*To inverse the diagonal:*

1. From the **Modification** menu choose the **Diagonal inversion** item or click *“Diagonal Inversion”* ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image70.png) button in the toolbar.

The following dialog box shall appear:

> ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/diagonalinversion.png)

1. Enter IDs of nodes forming the required edge in the **Edge** field (the node IDs must be separated by dashes) or select this edge in the 3D viewer.
2. Click the **Apply** or **Apply and Close** button.

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image38.jpg)
   >
   > **The selected edge**
   >
   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image36.jpg)
   >
   > **The inverted edge**

**See Also** a sample TUI Script of a [Diagonal Inversion](tui_modifying_meshes.md#tui-diagonal-inversion) operation.
