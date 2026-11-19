<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/interactive.html -->

# Using HexaBlock with the Graphical User Interface (GUI)

HexaBlock is a component of SALOME with an interactive part and has:

- its own menus and toolboxes,
- its document zone to represent all kind of objects (vertices, hexahedral, etc.),
- its graphic zone to visualize the model and the mesh.

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/interactive.png)

It provides the toolset allowing to:

- Build a model of block:
  :   - create basic geometrical objects: point, edge, quadrangle, hexahedra,
      - create grid: cartesian, cylindrical, spherical,
      - create a cylinder, a pipe, two intersected cylinders, two intersected pipes, an hemisphere, a rind,
      - remove an hexahedron,
      - replace hexahedrons,
      - disconnect by a point, an edge, a quadrangle,
      - join quadrangles by hexahedra, merge quadrangles,
      - transform or modify by translation, rotation and other symmetries,
      - make quad revolution.
- Associate a model of block to a geometry:
  :   - associate vertices of the model of blocks to vertices of a geometry,
      - associate edges of the model of blocks to edges of a geometry,
      - associate quadrangles of the model of blocks to faces of a geometry,
      - associate lines.
- Generate a mesh:
  :   - define groups,
      - define laws on propagations,
      - generate an hexahedral mesh.

- [Component](gui_component.md)
- [Document](gui_document.md)
- [Vertex](gui_vertex.md)
- [Edge](gui_edge.md)
- [Quadrangle](gui_quadrangle.md)
  - [Create from vertices](gui_quadrangle.md#create-from-vertices)
  - [Create from edges](gui_quadrangle.md#create-from-edges)
- [Hexahedron](gui_hexahedron.md)
  - [Create from quadrangles](gui_hexahedron.md#create-from-quadrangles)
  - [Create from vertices](gui_hexahedron.md#create-from-vertices)
- [Vector](gui_vector.md)
  - [Create with dx, dy, dz](gui_vector.md#create-with-dx-dy-dz)
  - [Create with two vertices](gui_vector.md#create-with-two-vertices)
- [Cylinders and Pipes Construction](gui_blocks_for_cyl_pipe.md)
  - [Cylinder](gui_blocks_for_cyl_pipe.md#cylinder)
  - [Cylinders](gui_blocks_for_cyl_pipe.md#cylinders)
  - [Pipe](gui_blocks_for_cyl_pipe.md#pipe)
  - [Pipes](gui_blocks_for_cyl_pipe.md#pipes)
- [Create cartesian grids](creategrids.md)
  - [Simple cartesian grid](creategrids.md#simple-cartesian-grid)
  - [Uniform cartesian grid](creategrids.md#uniform-cartesian-grid)
  - [Custom cartesian grid](creategrids.md#custom-cartesian-grid)
- [Create Hemispherical Grid](gui_hemisphere.md)
  - [Simple Sphere and Simple Rind](gui_hemisphere.md#simple-sphere-and-simple-rind)
  - [Uniform Sphere](gui_hemisphere.md#uniform-sphere)
  - [Custom Sphere](gui_hemisphere.md#custom-sphere)
  - [Uniform Rind](gui_hemisphere.md#uniform-rind)
  - [Custom Rind](gui_hemisphere.md#custom-rind)
  - [Simple Concentric (Spherical)](gui_hemisphere.md#simple-concentric-spherical)
  - [Uniform Concentric (Spherical)](gui_hemisphere.md#uniform-concentric-spherical)
  - [Custom Concentric (Spherical)](gui_hemisphere.md#custom-concentric-spherical)
- [Remove hexahedra](gui_remove.md)
- [Cut hexahedra](gui_cut_hexa.md)
  - [Uniform Cut](gui_cut_hexa.md#uniform-cut)
  - [Custom Cut](gui_cut_hexa.md#custom-cut)
- [Extrude and join quadrangles](gui_prism_join_quad.md)
  - [Extrude Quadrangles](gui_prism_join_quad.md#extrude-quadrangles)
  - [Join Quadrangles](gui_prism_join_quad.md#join-quadrangles)
- [Quad revolution](gui_quad_revolution.md)
  - [Uniform Quad Revolution](gui_quad_revolution.md#uniform-quad-revolution)
  - [Custom Quad Revolution](gui_quad_revolution.md#custom-quad-revolution)
- [Replace hexahedron](gui_replace_hexa.md)
- [Merge elements](gui_merge_elmts.md)
  - [Merge two quadrangles](gui_merge_elmts.md#merge-two-quadrangles)
  - [Merge two edges](gui_merge_elmts.md#merge-two-edges)
  - [Merge two vertices](gui_merge_elmts.md#merge-two-vertices)
- [Disconnect elements](gui_disc_elmts.md)
  - [Disconnect a quadrangle](gui_disc_elmts.md#disconnect-a-quadrangle)
  - [Disconnect edges](gui_disc_elmts.md#disconnect-edges)
  - [Disconnect an edge](gui_disc_elmts.md#disconnect-an-edge)
  - [Disconnect a vertex](gui_disc_elmts.md#disconnect-a-vertex)
- [Make elements by transforming elements](gui_make_elmts.md)
  - [Make elements by translation](gui_make_elmts.md#make-elements-by-translation)
  - [Make elements by scaling](gui_make_elmts.md#make-elements-by-scaling)
  - [Make elements by rotation](gui_make_elmts.md#make-elements-by-rotation)
- [Make elements by symmetry](gui_make_symmetry.md)
  - [Make elements by point symmetry](gui_make_symmetry.md#make-elements-by-point-symmetry)
  - [Make elements by line symmetry](gui_make_symmetry.md#make-elements-by-line-symmetry)
  - [Make elements by plane symmetry](gui_make_symmetry.md#make-elements-by-plane-symmetry)
- [Modify elements by transforming elements](gui_modify_elmts.md)
  - [Modify elements by translation](gui_modify_elmts.md#modify-elements-by-translation)
  - [Modify elements by scaling](gui_modify_elmts.md#modify-elements-by-scaling)
  - [Modify elements by rotation](gui_modify_elmts.md#modify-elements-by-rotation)
- [Modify elements by symmetry](gui_modify_symmetry.md)
  - [Modify elements by point symmetry](gui_modify_symmetry.md#modify-elements-by-point-symmetry)
  - [Modify elements by line symmetry](gui_modify_symmetry.md#modify-elements-by-line-symmetry)
  - [Modify elements by plane symmetry](gui_modify_symmetry.md#modify-elements-by-plane-symmetry)
- [Associations](gui_association.md)
  - [Show associations](gui_association.md#show-associations)
  - [Remove all associations](gui_association.md#remove-all-associations)
  - [Remove an element’s association(s)](gui_association.md#remove-an-element-s-association-s)
- [Add a geometry to a document](gui_add_geometry.md)
- [Associate the model of blocks to the geometry](gui_asso_quad_to_geom.md)
  - [Vertex Association](gui_asso_quad_to_geom.md#vertex-association)
  - [Edge(s) Association](gui_asso_quad_to_geom.md#edge-s-association)
  - [Quadrangle Association](gui_asso_quad_to_geom.md#quadrangle-association)
- [GUI: Definition of point of the geometry](gui_asso_vertex_to_geom.md)
  - [By coordinates](gui_asso_vertex_to_geom.md#by-coordinates)
  - [By a reference](gui_asso_vertex_to_geom.md#by-a-reference)
  - [By an Edge and a Parameter](gui_asso_vertex_to_geom.md#by-an-edge-and-a-parameter)
  - [By an Edge and a Length](gui_asso_vertex_to_geom.md#by-an-edge-and-a-length)
  - [By an Edge and Coordinates](gui_asso_vertex_to_geom.md#by-an-edge-and-coordinates)
  - [By intersection of two Lines or Wires](gui_asso_vertex_to_geom.md#by-intersection-of-two-lines-or-wires)
  - [By a face and two parameters](gui_asso_vertex_to_geom.md#by-a-face-and-two-parameters)
  - [By a face and coordinates](gui_asso_vertex_to_geom.md#by-a-face-and-coordinates)
- [Manage groups on the model](gui_groups.md)
  - [Add group](gui_groups.md#add-group)
  - [Remove group](gui_groups.md#remove-group)
- [Manage discretization laws](gui_discret_law.md)
  - [Add law](gui_discret_law.md#add-law)
  - [Remove law](gui_discret_law.md#remove-law)
- [Discretize on the propagation edges](gui_propag.md)
- [Generate the mesh](gui_mesh.md)
