<!-- source: https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/netgen_2d_3d_hypo_page.html -->

# NETGEN 2D and 3D hypotheses

**NETGEN 2D Parameters** and **NETGEN 3D Parameters** hypotheses work only with NETGEN algorithm in it's different forms:

- **NETGEN 1D-2D**
- **NETGEN 2D**
- **NETGEN 1D-2D-3D**
- **NETGEN 3D**.

**NETGEN 1D-2D** and **NETGEN 1D-2D-3D** algorithms do not require definition of lower-level hypotheses and algorithms (2D and 1D for meshing 3D objects and 1D for meshing 2D objects).

**NETGEN 1D-2D-3D** algorithm has maximal number of options. The rest forms have less options as they construct elements of less number of dimensions. All options are distributed among following tabs:

- [Arguments](netgen_2d_3d_hypo_page.md#arguments_anchor) - basic options.
- [Local Sizes](netgen_2d_3d_hypo_page.md#local_sizes_anchor) - local element size.
- [Advanced](netgen_2d_3d_hypo_page.md#advanced_anchor) - advanced options.
- [STL](netgen_2d_3d_hypo_page.md#stl_anchor) - specific Remesher options.

[NETGEN 2D/3D simple parameters](netgen_2d_3d_hypo_page.md#simple_anchor) hypotheses allow defining the size of elements for each dimension separately.

## Arguments tab

**Arguments** tab defines basic mesh parameters.

![netgen2d3d.png](https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/netgen2d3d.png)

*Main tab of hypothesis dialog box **NETGEN 1D-2D-3D** algorithm*

- **Name** - allows to define the name for the algorithm (NETGEN 2D (or 3D) Parameters by default).
- **Max Size** - maximum linear dimensions for mesh cells.
- **Min Size** - minimum linear dimensions for mesh cells. It is ignored if it is more than **Max Size**.
- **Fineness** - ranging from *Very Coarse* to *Very Fine* allows to set the level of meshing detalization using the three parameters below. You can select *Custom* to define them manually.
- **Growth rate** - allows to define how much the linear dimensions of two adjacent cells can differ (e.g. 0.3 means 30%).
- **Nb. Segs per Edge** - allows to define the minimum number of mesh segments in which edges will be split. Size of elements computed using this value is trimmed between **Min Size** and **Max Size** bounds. This parameter is used only if **Limit Size by Surface Curvature** is checked.
- **Nb Segs per Radius** - allows to define the size of mesh segments and mesh faces in which curved edges and surfaces will be split. A radius of local curvature divided by this value gives an element size at a given point. Element size computed this way is then trimmed between **Min Size** and **Max Size** bounds. This parameter is used only if **Limit Size by Surface Curvature** is checked.
- **Chordal Error** - allows to define the maximum distance between the generated 2D element and the surface. Size of elements computed using this criterion is trimmed between **Min Size** and **Max Size** bounds.
- **Limit Size by Surface Curvature** - if this box is checked in, then size of mesh segments and mesh faces on curved edges and surfaces is defined using value of **Nb Segs per Radius** parameter, and number of segments on straight edges is defined by values of **Nb. Segs per Edge** parameter. (**Growth rate** is also taken into account.) If this box is not checked in, then size of elements is defined by three parameters only: **Max Size**, **Min Size** and **Growth rate**.
- **Quad-dominated** - if this box is checked in, the mesher tries to generate quadrangle 2D mesh. Triangle elements are created where quadrangles are not possible.
- **Second Order** - if this box is checked in, the algorithm will create second order mesh.
- **Optimize** - if this box is checked in, the algorithm will modify initially created mesh in order to improve quality of elements. Optimization process is rather time consuming comparing to creation of initial mesh.

Remesher has two additional basic options:

- **Keep existing edges** - if activated, all edges present in the initial mesh are kept and used to separate STL surfaces.
- **Create groups of surfaces**  if activated, all new surface elements are distributed among groups corresponding to STL surfaces the Remesher detects.

## Local sizes tab

**Local sizes** tab allows to define size of elements on and around specified geometrical objects.

![netgen3d_local_size.png](https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/netgen3d_local_size.png)

- To define the local size it is necessary to select a geometrical objects in the object browser or in the viewer, and to click a button corresponding to the type of the geometrical objects: **On Vertex**, **On Edge** etc. **Name** of the geometrical object and a default **Value** will be added in the table where the **Value** can be changed.
- **Remove** - deletes a selected row from the table.
- **Mesh-size File** - opens a dialog to select a file defining size of elements. The file includes two obligatory sections. The first section defines the size at points. The second section defines the size along lines. Sizes defined in the file are trimmed between **Min Size** and **Max Size** bounds. Let's consider the following sample size file.
  ```python
  2
  92.5 92.5 92.5 0.05
  42.5 42.5 42.5 0.04
  1
  25 25 0 25 25 200  0.3
  ```
   "2" at the first line means that there are two points in the first section.  
  "92.5 92.5 92.5 0.05" at the second line means that at the point with coordinates (92.5, 92.5, 92.5) size of elements should be 0.05.  
  "1" at the fourth line means that there is one line in the second section.  
  "25 25 0 25 25 200 0.3" means that along the line between points (25, 25, 0) and (25, 25, 200) size of elements should be 0.3.

## Advanced tab

**Advanced** tab allows advance controlling meshing algorithm.

![netgen_advanced.png](https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/netgen_advanced.png)

- **Element size weight** - weight of triangle size badness with respect to triangle shape badness. Total triangle badness is evaluated as  *shape_badness + size_weight * size_mismatch*.
- **Nb. surface optimization steps** - number of loops when optimizing surface mesh.
- **Nb. volume optimization steps** - number of loops when optimizing volume mesh.
- **Worst element measure** - power of error, used to approximate max error optimization.
- **Use Delaunay** - if activated, use Delaunay approach to construct volume elements, otherwise use Advancing front method.
- **Check overlapping** - check overlapping surfaces during surface meshing.
- **Check chart boundary** - to check chart boundary.
- **Fuse Coincident Nodes on Edges and Vertices** - allows merging mesh nodes on vertices and edges which are geometrically coincident but are topologically different.

## STL tab

**STL**  tab holds option of Remesher (NETGEN 2D working w/o geometry).

![netgen2d_remesher.png](https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/netgen2d_remesher.png)

*Options specific to **NETGEN 2D** remesher algorithms*

- **Ridge angle** - defines minimum angle in degrees between normals of adjacent triangles at which the remesher considers the edge between these triangles as a feature edge. Feature edges bound charts of triangles that are re-meshed as separate surfaces.
- **Edge corner angle**  - defines minimum angle in degrees between adjacent edges of chart boundary, above which a point shared by the edges is considered as an end point of chart boundary curve.
- **Chart angle**  - angle between normals of adjacent triangles under which a shared sharp edge is *not* considered as chart boundary, provided that this edge is not classified as chart boundary due to **Ridge angle** and **Keep existing edges** options.
- **Outer chart angle**  - angle for overlapping parts of chart.
- **Chart distance**  - defines a factor used to limit element size by distance to neighbor chart.
- **Line length**  - defines a factor used to limit size of elements located near ends of chart boundary curves by length of a chart boundary curve.
- **Close edges**  - defines a factor used to limit size of elements located near chart boundary curves by distance to other chart boundary curves.
- **Surface curvature**  - defines a factor used to limit size of elements by surface curvature.
- **Edge angle**  - defines a factor used to limit size of elements by chart boundary curve curvature.
- **Surface mesh curvature** - defines a number of elements per curvature radius.

## NETGEN 2D/3D simple parameters

**NETGEN 2D simple parameters** and **NETGEN 3D simple parameters** hypotheses allow defining the size of elements for each dimension.

![netgen2d3d_simple.png](https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/netgen2d3d_simple.png)

**1D** group allows defining the size of 1D elements in either of two ways:

- **Number of Segments** allows specifying number of segments, that will split each edge, with equidistant distribution.
- **Local Length** defines length of segments.

**2D** group allows defining the size of 2D elements

- **Length from edges** if checked in, size of 2D mesh elements is defined as an average mesh segment length for a given wire, else
- **Max. Element Area** specifies expected maximum element area for each 2d element.
- **Allow Quadrangles** - allows to generate quadrangle elements wherever possible.

**3D** groups allows defining the size of 3D elements.

- **Length from faces** if checked in, the area of sides of volumic elements will be equal to an average area of 2D elements, else
- **Max. Element Volume** specifies expected maximum element volume of 3d elements.

Note
:   NETGEN algorithm does not strictly follow the input parameters. The actual mesh can be more or less dense than required. There are several factors in it:

    - NETGEN does not actually use **Number of Segments** parameter for discretization of edge. This parameter is used only to define the local element size (size at the given point), so local sizes of close edges influence each other.
    - NETGEN additionally restricts the element size according to edge curvature.
    - The local size of segments influences the size of close triangles.
    - The order of elements and their size in the 1D mesh generated by NETGEN differ from those in the 1D mesh generated by Regular_1D algorithm, which results in different 2D and 3D meshes at the same 1D input parameters.
