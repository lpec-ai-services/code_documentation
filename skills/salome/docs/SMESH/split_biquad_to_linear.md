<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/split_biquad_to_linear.html -->

# Split bi-quadratic into linear

This functionality allows to split bi-quadratic elements into
linear ones without creation of additional nodes.

So that

- bi-quadratic triangle will be split into 3 linear quadrangles;
- bi-quadratic quadrangle will be split into 4 linear quadrangles;
- tri-quadratic hexahedron will be split into 8 linear hexahedra;
- quadratic segments adjacent to the split bi-quadratic element will be split into 2 linear segments.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/split_biquad_to_linear_mesh.png)

**Mesh before and after splitting**

*To split bi-quadratic elements into linear:*

1. From the **Modification** menu choose the **Split bi-quadratic into linear** item or click *“Split bi-quadratic into linear”* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/split_biquad_to_linear_icon.png) in the toolbar.

   The following dialog box shall appear:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/split_biquad_to_linear_dlg.png)
2. Select a mesh, groups or sub-meshes in the Object Browser or in the Viewer.
3. Click the **Apply** or **Apply and Close** button.

**See Also** a sample TUI Script of a [Split bi-quadratic into linear](tui_modifying_meshes.md#tui-split-biquad) operation.
