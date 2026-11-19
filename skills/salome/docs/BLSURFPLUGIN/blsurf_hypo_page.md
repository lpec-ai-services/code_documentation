<!-- source: https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurf_hypo_page.html -->

# MG-CADSurf Parameters hypothesis

### Table of Contents

- [General parameters](#blsurf_general_parameters)
- [Advanced parameters](#blsurf_advanced_parameters)
- [Local size](#blsurf_local_size)
  - [Computation of the physical size](#blsurf_sizemap_computation)
  - [Advanced maps](#blsurf_attractor)
  - [Computation of attractors](#blsurf_attractor_computation)
- [Enforced vertices](#blsurf_enforced_elements)
- [Enforced Meshes](#blsurf_enforced_meshes)
- [Periodicity](#blsurf_periodicity)
  - [Introduction](#periodicity_introduction)
  - [GUI usage](#periodicity_gui_usage)
  - [TUI PreCAD usage](#periodicity_tui_precad_usage)
- [Hyper-patch](#blsurf_hyperpatch)

# General parameters

![blsurf_parameters.png](https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurf_parameters.png)

- **Name** - allows defining the name of the hypothesis (MG-CADSurf Parameters_n by default).
- **Physical Size** group defines a *physical* sizemap.
- **Type** of the physical sizemap can be set to *None*, *Global size* or *Local size*
  - if set to *Global size*, only the **User size**, **Max Size** and **Min Size** fields are taken into account.
  - if set to *Local size*, behaves like *Custom* mode and takes into account the "Gradation" parameter and the custom elements sizes given in the "Local size" tab.
- **Geometrical Size** group defines a *geometrical* sizemap.
- **Type** of the geometrical sizemap can be set to *None*, *Global size*
  - if set to *Global size*, allows user input in **Mesh angle**, **Mesh distance** and **Gradation** fields. These fields control computation of the element size, so called *geometrical size*, conform to the surface geometry considering local curvatures. If both the **User size** and the *geometrical parameters* are defined, the eventual element size corresponds to the least of the two.
- **User size** - defines the size of the generated mesh elements. If "Relative value" is checked, the value is relative to the diagonal of the shape.
- **Max Size** - defines the upper limit of mesh element size. If "Relative value" is checked, the value is relative to the diagonal of the shape.
- **Min Size** - defines the lower limit of mesh element size. If "Relative value" is checked, the value is relative to the diagonal of the shape.
- **Mesh angle** - Limiting angle (in degree) between the plane of a triangle of the mesh and each of the tangent planes at the three vertices. The smaller this angle is, the closer the mesh is to the exact surface, and the denser the resulting mesh is.
- **Mesh distance** - Maximum desired distance between a triangle and its supporting CAD surface. The smaller this distance is, the closer the mesh is to the exact surface (only available in isotropic meshing).
- **Quadratic mesh** - if checked, quadratic elements will be generated.
- **Gradation** - maximum ratio between the lengths of two adjacent edges.
- **Mesh optimisation** - if checked, the mesh will be optimized in order to get better shaped elements.
- **Elements type** - Type of the elements to generate the mesh with:
  - Triangles: generate a mesh with only triangles.
  - Quadrangle dominant: generate a mesh with a majority of quadrangles and a few triangles.
  - Quadrangles: generate a mesh with only quadrangles.
- **Surface proximity** - activates surface proximity based refinement.
  - **Number of layers** - number of surface element layers to be generated.
  - **Ratio** - a multiplicative coefficient which will be used to scale the size computed by the surface proximity detection.
- **Volume proximity** - activates volume proximity based refinement.
  - **Number of layers** - number of surface element layers to be generated.
  - **Ratio** - a multiplicative coefficient which will be used to scale the size computed by the volume proximity detection.
- **Anisotropic** - if checked, this parameter defines the maximum anisotropic ratio of the metric governing the anisotropic meshing process. The default value (0) means that the metric (and thus the generated elements) can be arbitrarily stretched.
- **Optimize tiny edges** - if checked, the tiny (nano) edges are removed from the generated mesh during local mesh optimization. The tiny edge will be removed only if the local quality is improved by the deletion. The tiny edge value defines the minimal length under which an edge is considered to be a tiny one.
- **Remove tiny edges** - if checked, the tiny (nano) edges are removed from the generated mesh *without* taking into account the local quality around the edge. The tiny edge value defines the minimal length under which an edge is considered to be a tiny one.
- **Remove bad elements** - if checked, the bad elements (slivers) are removed from the generated mesh. The bad element value defines the aspect ratio triggering the "bad element” classification.
- **Correct surface intersections** - if checked, the mesher will try to prevent all surface intersections, which is useful for future volume mesh generation. The value defines the time that will be spent in the intersection prevention process. For example, the value 3 means that the time of the intersection removal process won't be more than 3 times the time required to mesh without processing the intersections.
- **Volume Gradation** - maximum ratio between the lengths of two adjacent edges affecting quality of a future volume mesh, specially in thin volume areas. The volume gradation parameter must be greater than 1, and should be greater or equal to the value of the classic surface gradation (at the risk of increasing the time of convergence of the gradation process). The closer it is to 1, the smoother the final volume mesh you will build should be.

[Back to top](blsurf_hypo_page.md#blsurf_top)

# Advanced parameters

The notion of *diag* used in the descriptions means the diagonal of the bounding box of the geometrical object to mesh.

![blsurf_parameters_advanced.png](https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurf_parameters_advanced.png)

**Advanced** page tab expose mostly useful advanced options. Initially, default values of the options are displayed and they are not modifiable. If an option is activated using a check-box, its value becomes modifiable.

- **Meshing** options
  - **Independent patches** - This parameter can be used to activate the more complete patch independent meshing, by generating the mesh on global user-defined hyperpatches.
  - **Enforce CAD edge sizes** - Relaxes the given sizemap constraint around CAD edges to allow a better element quality and a better geometric approximation. It is only useful in combination with the gradation option.
  - **Priority of geometry over Jacobian** - This parameter determines whether or not the geometry accuracy is more important than the negative Jacobian correction. When this parameter is set to 0, MeshGems-CADSurf is allowed to lose the CAD-mesh associativity in order to correct the last negative Jacobians.
  - **Maximal number of points per patch** - This parameter controls the maximum amount of points MeshGems-CADSurf is allowed to generate on a single CAD patch. For an automatic gestion of the memory, you can set this parameter to ”0”.
  - **Rectify Jacobian** - The quadratic elements generation is a processing of the MeshGems-CADSurf meshing process which inserts the extra nodes on the CAD. This parameter determines whether MeshGems-CADSurf will try to correct or not all the elements of the surface mesh with negative Jacobians by moving the internal nodes of the mesh.
  - **Respect geometry** - This patch independent option can be deactivated to allow MeshGems-CADSurf to lower the geometry accuracy in its patch independent process.
  - **Tiny edges avoid surface intersections** - This option defines the priority between the tiny feature suppression and the surface intersection prevention. By default, MeshGems-CADSurf gives the priority to the surface intersection prevention rather than to tiny edge or bad surface element removal. These mesh features are then removed only if it does not lead to surface intersections. This behaviour can be deactivated by setting this parameter to 0, giving priority to the tiny edge or bad surface element removal.
  - **use deprecated patch mesher** - This option reproduces the mesher behaviour of previous MG-CADSurf versions (MeshGems before 2.3, i.e. before SALOME 8.2). This has proved useful on some particular cases such as very small local size on a vertex situated on a border curve.
- **CAD preprocessor** options. The CAD preprocessor (formerly known as PreCAD) has two main goals:

  - Complete missing or inadequate CAD descriptions.
  - Perform topology reconstruction and specific geometry enhancement for mesh generation.

  All options are unchecked by default. No cleanup is made by default so that the mesh matches the shape. If the user has a bad shape (e.g. imported shape), he can activate some options to improve the mesh.

  - **Compute ridges** - If this option is deactivated, MeshGems-CADSurf will not try to preserve lines defined by a sharp angle in the input discrete geometry. Only input ridges, free edges, non manifold edges and separation betwen zones with different attributes will be respected (if tags is set to respect).
  - **Closed geometry** - describes whether the working geometry should be closed or not. When activated, this option helps PreCAD to process the dirtiest geometries.
  - **Debug** - If debug = yes PreCAD will be very verbose and will output some intermediate files in the working directory.
  - **Discard input topology** - compute the CAD topology from scratch, without considering the topological information contained in the original CAD (useful for iges files). This option is unchecked by default.
  - **Merge Edges** - optimize the geometry by merging some edges.
  - **Periodic tolerance** - This parameter defines the maximum size difference between two periodic edges and also the maximum distance error between two periodic entities.
  - **Remove duplicate CAD faces** - optimize the geometry by merging the duplicate CAD faces. This option is unchecked by default.
  - **Required entities** - The required entities control the correction operations. Accepted values for this parameter are:
    - respect : MeshGems-CADSurf is not allowed to alter any required entity, even for correction purposes,
    - ignore : MeshGems-CADSurf will ignore the required entities in its processing,
    - clear : MeshGems-CADSurf will clear any required status for the entities. There will not be any entity marked as required in the generated mesh.
  - **Sewing tolerance** - tolerance of the assembly. It rarely requires to be tuned.
  - **Tags** - controls the optimisation process. Possible values are:
    - "respect" - PreCAD is not allowed to cross the CAD attributes boundaries for optimisation purpose.
    - "ignore" - PreCAD is allowed to cross the CAD attributes boundaries for optimisation.
    - "clear" - PreCAD will erase each tgas of each entities, and will thus be allowed to cross the CAD attributes boundaries in its optimisation purpose.
- **Add option** - adds a new line in **Other options** section where you can type an option name and value. The following advanced MG-CADSurf options can be used:
  - **create_tag_on_collision** (bool) - If this option is activated, MeshGems-CADSurf will create new tags to describe tag collisions (when it locally changes the topology, depending on the patch independent options). When this option is not activated, only one tag is preserved while the other one is dropped. By default this option is 1.
  - **tiny_edge_respect_geometry** (bool) - This option defines the behaviour of the tiny edge removal algorithm regarding volume collapse. By default, all tiny edges will be removed, regardless of any potential volume collapse. When this option is activated, it will prevent volume from being collapsed during the tiny edge removal process. By default this option is 0.
  - **manifold_geometry** (int) - describes whether the working geometry should be manifold or not. When activated, this option helps PreCAD to process the dirtiest geometries. By default this option is 0.
- **Verbosity level** - defines the percentage of "verbosity" of MeshGems-CADSurf [0-10].
- **ExportGMF** - saves the computed mesh into a GMF file (.mesh or .meshb).

[Back to top](blsurf_hypo_page.md#blsurf_top)

# Local size

Local sizes can be defined on faces, edges or vertices:

- The faces, edges and vertices should belong to the meshed geometrical object or to its sub-shapes (created using **Explode** command).
- Groups of faces, edges and vertices are also handled.
- It is possible to attribute the same size to several geometries using multi-selection.
- The sizes are constant values or python functions.
- In case of a python function, the following rules must be respected:
  - The name of the function is f.
  - If geometry is a face or a group of faces, the function is f(u,v).
  - If geometry is an edge or a group of edges, the function is f(t).
  - If geometry is a vertex or a group of vertices, the function is f().
  - The function must return a double.

3 different types of size maps can be defined:

1. [Computation of the physical size](blsurf_hypo_page.md#blsurf_sizemap_computation)
2. [Advanced maps](blsurf_hypo_page.md#blsurf_attractor)
3. [Computation of attractors](blsurf_hypo_page.md#blsurf_attractor_computation)

[Back to top](blsurf_hypo_page.md#blsurf_top)

## Computation of the physical size

![blsurf_parameters_sizemap1.png](https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurf_parameters_sizemap1.png)

The physical size is obtained by querying sizemap functions associated to the input CAD object for surfaces, curves and points. Each function can either return a value h (which is then trimmed between the two bounds hphymin and hphymax), or "no answer" (by not assigning a value to h), thus providing great flexibility in the specification of the sizes. The computation depends on whether point P is internal to a surface, internal to a curve, or at the end of several curves:

- If point P is internal to a surface, the CAD surface size function is queried. If no answer is returned, one interpolates with the values at the vertices of the discretized interface curves.
- If point P is internal to a curve, the CAD curve size function is queried first. If no answer is returned, the surface size function is queried for every adjacent surface and the mean value of the returned values is computed. If no answer is returned, sizes h1 and h2 at both ends of the curve are considered (see next item) and the interpolated value is computed.
- If point P is at the extremity of several curves, the CAD point size function is queried first. If no answer is returned, the curve size function is queried for every adjacent curve and the mean value of the returned values is computed. If no answer is returned, the surface size function is queried for every adjacent surface and the mean value of the returned values is computed. If there is still no answer returned, the default value hphydef is kept.

In order to compute the mean of several values, the arithmetic mean is used by default, but this can be modified by the parameter hmean flag. In the same way, in order to interpolate two values, a linear interpolation is used by default, but this can be modified by hinterpol flag.

**Note:** on some particular configurations, the mesher behaviour is not the same as before (SALOME versions before 8.2 i.e. MeshGems before 2.3). For a small local size defined on a point situated on a border curve, the previous mesher behaviour may be prefered: see "use deprecated patch mesher" on advanced tag.

[Back to "Local size"](blsurf_hypo_page.md#blsurf_local_size)  
[Back to top](blsurf_hypo_page.md#blsurf_top)

## Advanced maps

![blsurf_parameters_sizemap2.png](https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurf_parameters_sizemap2.png)

More specific size maps can be defined on faces.

- *Attractors*  allow to define the size of the mesh elements on a face so that the mesh is the finest on the attractor shape and becomes coarser when getting far from this shape.
  - The selected attractor can be a Vertex, an Edge, a Wire or a Compound mixing several entities of those types.
  - The attractor doesn't have to be a sub-shape of the shape to mesh.
  - The size will grow exponentially (see the formula below) but is bounded by gradation,   
    so if you want the formula to be strictly respected, you should set the *gradation* to its maximum (2.5) in the *arguments* tab.
- Furthermore you can choose to  *keep the size constant*  until a certain distance from a shape. This option can be combined or not with an *attractor* size map described above.
  - If the two options are combined the size will remain constant until the distance specified in "constant over" and grow then as prescribed by the attractor function.
  - Else the growing is only controled by the standard arguments of MG-CADSurf (gradation ...).

![blsurf_const_size_near_shape2.png](https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurf_const_size_near_shape2.png)

Example of size map with constant size option, the size is kept constant on the left side of the surface until a certain distance

Note
:   The validation of the hypothesis might take a few seconds if attractors are defined or the "constant size" option is used because a map of distances has to be built on the whole surface for each face where such a hypothesis has been defined.

See also
:   Sample TUI Script of the [creation of a MG-CADSurf hypothesis](blsurfplugin_python_interface_page.md#tui_blsurf), including size map.

[Back to "Local size"](blsurf_hypo_page.md#blsurf_local_size)  
[Back to top](blsurf_hypo_page.md#blsurf_top)

## Computation of attractors

The size grows exponentially following the equation : $h(d) = \mathrm{User Size} + (\mathrm{h\_start} - \mathrm{User Size}) \times e ^ { - \left( \frac{d}{R} \right) ^ {2} }$

Where :

- h_start is the desired size on the given attractor shape
- d is the distance of the current point from the attractor shape. The distance is the geodesic distance (i.e. calculated by following the surface to be meshed)
- R is called the distance of influence and allows controlling the growth rate of the mesh

![blsurf_attractors2.png](https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurf_attractors2.png)

Example of mesh created using attractors, the attractors here are the side edges and the size grows from the side of the surface towards the apex

[Back to "Local size"](blsurf_hypo_page.md#blsurf_local_size)  
[Back to top](blsurf_hypo_page.md#blsurf_top)

# Enforced vertices

![blsurf_parameters_enforced_vertices.png](https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurf_parameters_enforced_vertices.png)

It is possible to define some enforced vertices to MG-CADSurf algorithm. An enforced vertex is defined by

- selecting an existing Vertex or Compound,
- or by its coordinates.

The enforced vertex is the projection of a point defined by its (x,y,z) coordinates on the closest face found by the application.

- It is possible to define several enforced vertices.
- If the projected point is on the boundary or outside of the face, it will be ignored.
- If a group name is specified : if the group exists, the enforced nodes will be added in the existing group, if the group does not exist it will be created.

All the internal vertices of faces can be considered as enforced vertices if the corresponding checkbox is checked. A group can optionnaly be defined on those enforced vertices.

See also
:   Sample TUI Script of the [creation of a MG-CADSurf hypothesis](blsurfplugin_python_interface_page.md#tui_blsurf), including enforced vertices.

[Back to top](blsurf_hypo_page.md#blsurf_top)

# Enforced Meshes

![blsurf_enforced_meshes.png](https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurf_enforced_meshes.png)

MG-CADSurf algorithm can be forced by other 1D meshes, sub-meshes or groups. 1D meshes are allowed to pass over face boundaries and to intersect other enforced meshes. If a group name is given, the enforced 1D elements will be added to the group. If the group does not exist, it is created.

See also
:   Sample TUI Script of the [creation of a MG-CADSurf hypothesis](blsurfplugin_python_interface_page.md#tui_blsurf), including enforced meshes.

[Back to top](blsurf_hypo_page.md#blsurf_top)

# Periodicity

## Introduction

Periodicity is used to have the same discretization on two faces (in 3D) or two edges (in 2D). This is useful for instance for a Representative Volume Element so that the translated meshes share the same nodes on the common faces.

Periodicity association uses PreCAD (MG-CADSurf preprocessor). You don't need an extra PreCAD license. It is included in MG-CADSurf since MeshGems V2.2.

![blsurf_periodicity_translation.png](https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurf_periodicity_translation.png)

Two periodic faces (translation)

![blsurf_periodicity_reflexion.png](https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurf_periodicity_reflexion.png)

Two periodic faces (reflexion)

![blsurf_periodicity_2D.png](https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurf_periodicity_2D.png)

Associations of edges in 2D (both red edges are associated with each other)

## GUI usage

![blsurf_parameters_periodicity.png](https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurf_parameters_periodicity.png)

The periodicity association can be defined:

- on 2 groups of faces (in 3D)
- on 2 groups of edges (in 2D)

If the transformation is a translation, PreCAD makes the periodicity association with only this information.

Otherwise, for instance a rotation, the user has to define 3 non-colinear vertices and their image by the transformation.

## TUI PreCAD usage

The two methods to define periodicity with PreCAD are (the former name of *MG-CADSurf* is *BLSURF* and names of the corresponding classes and modules still include *"BLSURF"*):

- [BLSURFPluginBuilder.BLSURF_Algorithm.AddPreCadFacesPeriodicity](../BLSURFPLUGIN/blsurfpluginpy_doc/classBLSURFPluginBuilder_1_1BLSURF__Algorithm.md#a96e7f2b81a9c4403a6cf66e0424b0e54)
- [BLSURFPluginBuilder.BLSURF_Algorithm.AddPreCadEdgesPeriodicity](../BLSURFPLUGIN/blsurfpluginpy_doc/classBLSURFPluginBuilder_1_1BLSURF__Algorithm.md#ada3746459c72a1e68b4dcf95cfcd3cdd)

List of source and target vertices to define a transformation are optional.

See also
:   Sample TUI Script of the definition of MG-CADSurf periodicity [using preCAD](blsurfplugin_python_interface_page.md#tui_blsurf_periodicity_preCAD).

# Hyper-patch

![blsurf_parameters_hyperpatch.png](https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurf_parameters_hyperpatch.png)

Hyper-patch tab page allows defining faces that will be meshes together as part of a global hyper-patch.

- **Hyper-patch IDs** table - shows IDs of faces of defined hyper-patches.
- **Face selection** - activates selection of faces in the VTK Viewer.
- **Group selection** - activates selection of faces and groups of faces in the Object Browser.
- **IDs** - allows typing IDs of faces composing a hyper-patch and shows IDs of faces selected in the Viewer or the Object Browser.
- **Add** - adds a new row to the table and moves **IDs** there.
- **Remove** - removes selected hyper-patches from the table.

[Back to top](blsurf_hypo_page.md#blsurf_top)

For more information on MeshGems-CADSurf, you can read its documentation at $MESHGEMS_ROOT_DIR/Docs/mg-cadsurf_user_manual.pdf
