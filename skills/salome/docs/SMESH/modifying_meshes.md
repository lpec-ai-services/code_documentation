<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/modifying_meshes.html -->

# Modifying meshes

Salome provides a vast specter of mesh modification and transformation operations, giving the possibility to:

- [Add](adding_nodes_and_elements.md#adding-nodes-and-elements-page) mesh elements from nodes to polyhedrons at an arbitrary place in the mesh.
- [Add quadratic](adding_quadratic_elements.md#adding-quadratic-elements-page) mesh elements from quadratic segments to quadratic hexahedrons at an arbitrary place in the mesh.
- [Remove](removing_nodes_and_elements.md#removing-nodes-and-elements-page) any existing mesh elements and nodes.
- [Convert linear mesh to quadratic](convert_to_from_quadratic_mesh.md#convert-to-from-quadratic-mesh-page), or vice versa.
- [Generate boundary elements](make_2dmesh_from_3d.md#make-2dmesh-from-3d-page).
- [Generate 2D mesh from 3D elements](make_2dmesh_from_3d_elements.md#make-2dmesh-from-3d-elements-page).
- [Translate](translation.md#translation-page) in the indicated direction the mesh or some of its elements.
- [Rotate](rotation.md#rotation-page) by the indicated axis and angle the mesh or some of its elements.
- [Scale](scale.md#scale-page) the mesh or some of its elements.
- [Offset](offset_elements.md#offset-elements-page) the entire mesh, the sub-mesh or a selection of elements based on filters.
- [Mirror](symmetry.md#symmetry-page) the mesh through a point, a vector or a plane of symmetry.
- [Duplicate Nodes or/and Elements](double_nodes_page.md#double-nodes-page). Duplication of nodes can be useful to emulate a crack in the model.
- [Merge Nodes](merging_nodes.md#merging-nodes-page) coincident within the indicated tolerance.
- [Merge Elements](merging_elements.md#merging-elements-page) based on the same nodes.
- Create an [extrusion](extrusion.md#extrusion-page) along a vector or by normal to a discretized surface.
- Create an [extrusion along a path](extrusion_along_path.md#extrusion-along-path-page).
- Create elements by [revolution](revolution.md#revolution-page) of the selected nodes and elements.
- [Move Nodes](mesh_through_point.md#mesh-through-point-page) to an arbitrary location with consequent transformation of all adjacent elements.
- [Change orientation](changing_orientation_of_elements.md#changing-orientation-of-elements-page) of the selected elements.
- [Orient faces](reorient_faces.md#reorient-faces-page) by several means.
- Unite meshes by [sewing](sewing_meshes.md#sewing-meshes-page) free borders, border to side or side elements.
- [Invert an edge](diagonal_inversion_of_elements.md#diagonal-inversion-of-elements-page) between neighboring triangles.
- [Unite two triangles](uniting_two_triangles.md#uniting-two-triangles-page).
- [Unite several adjacent triangles](uniting_set_of_triangles.md#uniting-set-of-triangles-page).
- [Cut a quadrangle](cutting_quadrangles.md#cutting-quadrangles-page) into two triangles.
- [Cut triangles](add_node_on_segment.md#add-node-on-segment-page) into two by adding a node on edge.
- [Cut a face](add_node_on_face.md#add-node-on-face-page) into triangles by adding a node on it.
- [Split](split_to_tetra.md#split-to-tetra-page) volumic elements into tetrahedra or prisms.
- [Split bi-quadratic](split_biquad_to_linear.md#split-biquad-to-linear-page) elements into linear ones without creation of additional nodes.
- [Smooth](smoothing.md#smoothing-page) elements, reducung distortions in them by adjusting the locations of nodes.
- Apply [pattern mapping](pattern_mapping.md#pattern-mapping-page).
- [Generate flat elements on group boundaries or on faces](generate_flat_elements.md#generate-flat-elements-page).
- [Cut a tetrahedron mesh by a plane](cut_mesh_by_plane.md#cut-mesh-by-plane-page).

Note

You can use these operations to [modify the mesh](constructing_meshes.md#edit-anchor) of a lower dimension before generation of the mesh of a higher dimension.

Note

It is possible to use the variables defined in the SALOME **NoteBook** to specify the numerical parameters used for modification of any object.

**Table of Contents**

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
