<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/about_quality_controls.html -->

# About quality controls

**Mesh quality control** in MESH is destined for visual control of the generated mesh.

Application of a definite quality control consists of usage of the corresponding algorithm, which calculates a value of a definite geometric characteristic (Area, Length of edges, etc) for all meshing elements, composing your mesh. Then all meshing elements are colored according the calculated values. The reference between the coloring of the meshing elements and these calculated values is shown with the help of a scalar bar, which is displayed near the presentation of your mesh.

There are four types of quality controls, corresponding to node, edge, face and volume entity type.

Node quality controls:

- [Free nodes](free_nodes.md#free-nodes-page)
- [Double nodes](double_nodes_control.md#double-nodes-control-page)

Edge quality controls:

- [Free borders](free_borders.md#free-borders-page)
- [Length](length.md#length-page)
- [Borders at multi-connection](borders_at_multi_connection.md#borders-at-multi-connection-page)
- [Double edge, Double faces and Double volumes](double_elements_control.md#double-elements-page)

Face quality controls:

- [Free edges](free_edges.md#free-edges-page)
- [Free faces](free_faces.md#free-faces-page)
- [Bare border faces](bare_border_face.md#bare-border-faces-page)
- [Over-constrained faces](over_constrained_faces.md#over-constrained-faces-page)
- [Length 2D](length_2d.md#length-2d-page)
- [Deflection 2D](deflection_2d.md#deflection-2d-page)
- [Borders at multi-connection 2D](borders_at_multi_connection_2d.md#borders-at-multi-connection-2d-page)
- [Area](area.md#area-page)
- [Taper](taper.md#taper-page)
- [Aspect Ratio](aspect_ratio.md#aspect-ratio-page)
- [Minimum angle](minimum_angle.md#minimum-angle-page)
- [Warping](warping.md#warping-page)
- [Skew](skew.md#skew-page)
- [Element Diameter 2D](max_element_length_2d.md#max-element-length-2d-page)
- [Double edge, Double faces and Double volumes](double_elements_control.md#double-elements-page)

Volume quality controls:

- [Aspect ratio 3D](aspect_ratio_3d.md#aspect-ratio-3d-page)
- [Volume](volume.md#volume-page)
- [Warping 3D](warping_3d.md#warping-3d-page)
- [Element Diameter 3D](max_element_length_3d.md#max-element-length-3d-page)
- [Scaled Jacobian](scaled_jacobian.md#scaled-jacobian-page)
- [Bare border volumes](bare_border_volumes.md#bare-border-volumes-page)
- [Over-constrained volumes](over_constrained_volumes.md#over-constrained-volumes-page)
- [Double edge, Double faces and Double volumes](double_elements_control.md#double-elements-page)

To manage the quality controls call pop-up in the VTK viewer and select “Controls” sub-menu

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/controls_popup.png)

- **Reset** switches off quality controls;
- **Node Controls** provides access to the node quality controls;
- **Edge Controls** provides access to the edge quality controls;
- **Face Controls** provides access to the face quality controls;
- **Volume Controls** provides access to the volume quality controls;
- **Scalar Bar Properties** allows setting [Scalar Bar properties](scalar_bar.md#scalar-bar-dlg);
- **Distribution -> Export …** allows saving the distribution of quality control values in the text file;
- **Distribution -> Show** Shows/Hides the distribution histogram of the quality control values in the VTK Viewer.
- **Distribution -> Plot** Plots the distribution histogram of the quality control values in the Plot 2D Viewer.

**Table of Contents**

- [Free nodes](free_nodes.md)
- [Double nodes](double_nodes_control.md)
- [Free borders](free_borders.md)
- [Length](length.md)
- [Borders at multi-connection](borders_at_multi_connection.md)
- [Double edge, Double faces and Double volumes](double_elements_control.md)
- [Free edges](free_edges.md)
- [Free faces](free_faces.md)
- [Bare border faces](bare_border_face.md)
- [Over-constrained faces](over_constrained_faces.md)
- [Length 2D](length_2d.md)
- [Deflection 2D](deflection_2d.md)
- [Borders at multi-connection 2D](borders_at_multi_connection_2d.md)
- [Area](area.md)
- [Taper](taper.md)
- [Aspect Ratio](aspect_ratio.md)
- [Minimum angle](minimum_angle.md)
- [Warping](warping.md)
- [Skew](skew.md)
- [Element Diameter 2D](max_element_length_2d.md)
- [Aspect ratio 3D](aspect_ratio_3d.md)
- [Volume](volume.md)
- [Element Diameter 3D](max_element_length_3d.md)
- [Warping 3D](warping_3d.md)
- [Bare border volumes](bare_border_volumes.md)
- [Over-constrained volumes](over_constrained_volumes.md)
- [Scalar Bar properties](scalar_bar.md)
- [Scaled Jacobian](scaled_jacobian.md)
