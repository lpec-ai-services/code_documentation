<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/index.html -->

# Introduction to Mesh module

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/a-viewgeneral.png)

**Mesh** module of SALOME is destined for:

- [creating meshes](about_meshes.md#about-meshes-page) in different ways:

  - by meshing geometrical models previously created or imported by the Geometry component;
  - bottom-up, using [mesh edition](modifying_meshes.md#modifying-meshes-page), especially [extrusion](extrusion.md#extrusion-page) and [revolution](revolution.md#revolution-page);
  - by generation of the 3D mesh from the 2D mesh not based on the geometry ([imported](importing_exporting_meshes.md#importing-exporting-meshes-page) for example);
- [importing and exporting meshes](importing_exporting_meshes.md#importing-exporting-meshes-page) in various formats;
- [modifying meshes](modifying_meshes.md#modifying-meshes-page) with a vast array of dedicated operations;
- [creating groups](grouping_elements.md#grouping-elements-page) of mesh elements;
- filtering mesh entities (nodes or elements) using [Filters](about_filters.md#filters-page) functionality for [creating groups](grouping_elements.md#grouping-elements-page) and applying [mesh modifications](modifying_meshes.md#modifying-meshes-page);
- [viewing meshes](viewing_meshes_overview.md#viewing-meshes-overview-page) in the VTK viewer and [getting info](mesh_infos.md#mesh-infos-page) on mesh and its sub-objects;
- [remeshing meshes](adaptation.md#adaptation-page);
- applying to meshes [Quality Controls](about_quality_controls.md#quality-page), allowing to highlight important elements;
- taking various [measurements](measurements.md#measurements-page) of the mesh objects.

There is a set of [tools](tools.md#tools-page) plugged-in the module to extend the basic functionality listed above.

Almost all mesh module functionalities are accessible via [Python interface](smeshpy_interface.md#smeshpy-interface-page).

It is possible to use the variables predefined in [Salome notebook](using_notebook_smesh_page.md#using-notebook-mesh-page) to set parameters of operations.

Mesh module preferences are described in the [Mesh preferences](mesh_preferences.md#mesh-preferences-page) section of SALOME Mesh Help.

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image7.jpg)

**Example of MESH module usage for engineering tasks**

**Table of Contents**

- [About meshes](about_meshes.md)
  - [Constructing meshes](constructing_meshes.md)
    - [Basic meshing algorithms](basic_meshing_algos.md)
    - [About Hypotheses](about_hypo.md)
  - [Constructing sub-meshes](constructing_submeshes.md)
  - [Editing Meshes](editing_meshes.md)
  - [Importing and exporting meshes](importing_exporting_meshes.md)
  - [Building Compound Meshes](building_compounds.md)
  - [Copy Mesh](copy_mesh.md)
  - [Create Dual Mesh](create_dual_mesh.md)
  - [Nodal connectivity of elements](connectivity.md)
  - [Parallel Computing](parallel_compute.md)
- [Modifying meshes](modifying_meshes.md)
  - [Adding nodes and elements](adding_nodes_and_elements.md)
  - [Adding Quadratic Elements](adding_quadratic_elements.md)
  - [Removing nodes and elements](removing_nodes_and_elements.md)
  - [Translation](translation.md)
  - [Rotation](rotation.md)
  - [Scale](scale.md)
  - [Offset mesh](offset_elements.md)
  - [Symmetry](symmetry.md)
  - [Duplicate Nodes or/and Elements](double_nodes_page.md)
  - [Sewing meshes](sewing_meshes.md)
  - [Merging nodes](merging_nodes.md)
  - [Merging Elements](merging_elements.md)
  - [Moving nodes](mesh_through_point.md)
  - [Diagonal inversion of two triangles](diagonal_inversion_of_elements.md)
  - [Uniting two triangles](uniting_two_triangles.md)
  - [Uniting a set of triangles](uniting_set_of_triangles.md)
  - [Changing orientation of elements](changing_orientation_of_elements.md)
  - [Orient faces](reorient_faces.md)
  - [Cutting quadrangles](cutting_quadrangles.md)
  - [Cutting triangles](add_node_on_segment.md)
  - [Cutting a face into triangles](add_node_on_face.md)
  - [Splitting volumes](split_to_tetra.md)
  - [Split bi-quadratic into linear](split_biquad_to_linear.md)
  - [Smoothing](smoothing.md)
  - [Extrusion](extrusion.md)
  - [Extrusion along Path](extrusion_along_path.md)
  - [Revolution](revolution.md)
  - [Pattern mapping](pattern_mapping.md)
  - [Convert to/from Quadratic Mesh](convert_to_from_quadratic_mesh.md)
  - [Generate boundary elements](make_2dmesh_from_3d.md)
  - [Generate 2D mesh from 3D elements](make_2dmesh_from_3d_elements.md)
  - [Generate flat elements on group boundaries or on faces](generate_flat_elements.md)
  - [Cut a tetrahedron mesh by a plane](cut_mesh_by_plane.md)
- [Grouping elements](grouping_elements.md)
  - [Creating groups](creating_groups.md)
  - [Create Groups from Geometry](create_groups_from_geometry.md)
  - [Face Groups Separated By Sharp Edges](face_groups_by_sharp_edges.md)
  - [Group Based on Nodes of Other Groups](group_of_underlying_elements.md)
  - [Boolean operations on groups](using_operations_on_groups.md)
  - [Editing groups](editing_groups.md)
  - [Deleting groups with content](deleting_groups.md)
- [About filters](about_filters.md)
- [About quality controls](about_quality_controls.md)
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
- [Adaptation](adaptation.md)
- [Measurements](measurements.md)
- [Viewing meshes](viewing_meshes_overview.md)
  - [Mesh Information](mesh_infos.md)
  - [Find Element by Point](find_element_by_point.md)
  - [Numbering](numbering.md)
  - [Display Mode](display_mode.md)
  - [Display Entity](display_entity.md)
  - [Properties](colors_size.md)
  - [Transparency](transparency.md)
  - [Clipping](clipping.md)
- [Python interface](smeshpy_interface.md)
  - [Creating Meshes](tui_creating_meshes.md)
  - [Defining Hypotheses and Algorithms](tui_defining_hypotheses.md)
  - [Grouping Elements](tui_grouping_elements.md)
  - [Filters usage](tui_filters.md)
  - [Modifying Meshes](tui_modifying_meshes.md)
  - [Transforming Meshes](tui_transforming_meshes.md)
  - [Viewing Meshes](tui_viewing_meshes.md)
  - [Quality Controls](tui_quality_controls.md)
  - [Adaptation](tui_adaptation.md)
  - [Measurements](tui_measurements.md)
  - [How to work with objects from the GUI ?](tui_work_on_objects_from_gui.md)
  - [Using SALOME NoteBook](tui_notebook_smesh.md)
- [Plugins](tools.md)
- [Mesh preferences](mesh_preferences.md)
- [Using SALOME NoteBook](using_notebook_smesh_page.md)
