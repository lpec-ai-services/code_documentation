<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/about_meshes.html -->

# About meshes

**MESH** represents a discrete approximation of a subset of the three-dimensional space by [elementary geometrical elements](#elementary-geometrical-elements).

A SALOME study can contain multiple meshes, but they do not implicitly compose one super-mesh, and finally each of them can be used (e.g. exported) only individually.

Mesh module provides several ways to create the mesh:

- The main way is to [construct the mesh](constructing_meshes.md#constructing-meshes-page) on the basis of the geometrical shape produced in the Geometry module. This way implies selection of

  - a geometrical object (*main shape*) and
  - *meshing parameters* ([meshing algorithms](basic_meshing_algos.md#basic-meshing-algos-page) and characteristics (e.g. element size) of a required mesh encapsulated in [hypothesis](about_hypo.md#about-hypo-page) objects).

  Construction of [sub-meshes](constructing_submeshes.md#constructing-submeshes-page) allows to discretize some sub-shapes of the main shape, for example a face, using the meshing parameters that differ from those used for other sub-shapes.
  Meshing parameters of meshes and sub-meshes can be [edited](editing_meshes.md#editing-meshes-page). (Upon edition only mesh entities generated using changed meshing parameters are removed and will be re-computed).

  Note

  Algorithms and hypotheses used at mesh level are referred to as *global* ones and those used at sub-mesh level are referred to as *local* ones.
- Bottom-up way, using [mesh modification](modifying_meshes.md#modifying-meshes-page) operations, especially [extrusion](extrusion.md#extrusion-page) and [revolution](revolution.md#revolution-page). To create an empty mesh not based on geometry, use the same dialog as to [construct the mesh on geometry](constructing_meshes.md#constructing-meshes-page) but specify neither the geometry nor meshing algorithms.
- The mesh can be [imported](importing_exporting_meshes.md#importing-exporting-meshes-page) from (and exported to) the file in MED, UNV, STL, CGNS, DAT and GMF formats.
- The 3D mesh can be generated from the 2D mesh not based on geometry, which was either [imported](importing_exporting_meshes.md#importing-exporting-meshes-page) or created in other way. To setup the meshing parameters of a mesh not based on geometry, just invoke [Edit mesh / sub-mesh](editing_meshes.md#editing-meshes-page) command on your 2D mesh.
- Several meshes can be [combined](building_compounds.md#building-compounds-page) into a new mesh.
- The whole mesh or its part (sub-mesh or group) can be [copied](copy_mesh.md#copy-mesh-page) into a new mesh.
- A new mesh can be created from a transformed, e.g. [translated](translation.md#translation-page), part of the mesh.
- A new mesh can be created from the gernation of the [dual](create_dual_mesh.md#create-dual-mesh-page) of a Tetrahedron Mesh.

Meshes can be edited using the MESH functions destined for [modification](modifying_meshes.md#modifying-meshes-page) of meshes.

Attractive meshing capabilities include:

- 3D and 2D [Viscous Layers](additional_hypo.md#viscous-layers-anchor) (boundary layers of highly stretched elements beneficial for high quality viscous computations);
- automatic conformal transition between tetrahedral and hexahedral sub-meshes.

The **structure** of a SALOME mesh is described by nodes and elements based on these nodes. The geometry of an element is defined by the sequence of nodes constituting it and the [connectivity convention](connectivity.md#connectivity-page) (adopted from MED library). Definition of the element basing on the elements of a lower dimension is NOT supported.

The mesh can include the following entities:

- **Node** - a mesh entity defining a position in 3D space with coordinates (x, y, z).
- **Edge** (or segment) - 1D mesh element linking two nodes.
- **Face** - 2D mesh element representing a part of surface bound by links between face nodes. A face can be a triangle, quadrangle or polygon.
- **Volume** - 3D mesh element representing a part of 3D space bound by volume facets. Nodes of a volume describing each facet are defined by the [connectivity convention](connectivity.md#connectivity-page). A volume can be a tetrahedron, hexahedron, pentahedron, pyramid, hexagonal or polyhedron.
- **0D** element - mesh element defined by one node.
- **Ball** element - discrete mesh element defined by a node and a diameter.

Every mesh entity has an attribute associating it to a sub-shape it is generated on (if any). The node generated on the geometrical edge or surface in addition stores its position in parametric space of the associated geometrical entity. This attribute is set up by meshing algorithms generating elements and nodes.

Mesh entities are identified by integer IDs starting from 1.
Nodes and elements are counted separately, i.e. there can be a node and element with the same ID.

SALOME supports elements of second order, without a central node (quadratic triangle, quadrangle, polygon, tetrahedron, hexahedron,
pentahedron and pyramid) and with central nodes (bi-quadratic triangle and quadrangle and tri-quadratic hexahedron).

Quadratic mesh can be obtained in three ways:

- Using a global [Quadratic Mesh](additional_hypo.md#quadratic-mesh-anchor) hypothesis. (Elements with the central node are not generated in this way).
- Using [Convert to/from Quadratic Mesh](convert_to_from_quadratic_mesh.md#convert-to-from-quadratic-mesh-page) operation.
- Using an appropriate option of some meshing algorithms, which generate elements of several dimensions starting from mesh segments.

A work in progress allow you to compute your mesh in parralle Parallel Computing

**Table of Contents**

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
