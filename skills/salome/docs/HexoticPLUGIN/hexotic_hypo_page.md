<!-- source: https://docs.salome-platform.org/latest/gui/HexoticPLUGIN/hexotic_hypo_page.html -->

# MG-Hexa Parameters hypothesis

MG-Hexa Parameters hypothesis works only with **MG-Hexa** algorithm. This algorithm is a commercial software.   
To get a license, visit <http://www.meshgems.com/meshgems-products.html>

# General parameters

![hexotic_parameters.png](https://docs.salome-platform.org/latest/gui/HexoticPLUGIN/hexotic_parameters.png)

- **Name** - allows to define the name of the hypothesis (MG-Hexa Parameters by default).
- **Physical size** - defines size of elements

  - **Type** - *Global* activates and *None* deactivates this option
  - **Min size** - allows defining the minimal size of the elements (overrides **Nb. Hexes Max Level** value).
  - **Max size** - allows defining the maximal size of the elements (overrides **Nb. Hexes Min Level** value).
- **Geometric size** - defines size of elements depending on curvature

  - **Type** - *Global* activates and *None* deactivates this option
  - **Mesh angle** - specifies the angle (in degrees) between two triangles for the curvature based refinement. This angle should be in a range between **ridge angle** and 180. This angle is a threshold that will trigger the refinement: during the octree building, each octant containing triangles that make an angle greater than the threshold will be split. The process will be repeated until every octants contain portion of the geometry smoother than the threshold angle.
- **Sub-domains mesh mode** - This option allows the user to mesh or not mesh internal subdomains (such as holes), or to mesh non-manifold domains.
  - sd 1 : meshes in inside/out mode: the internal cavities are ignored, the whole domain is meshed into a single domain;
  - sd 2 : meshes only the internal main component. Internal holes (cavities) will not be meshed;
  - sd 3 : meshes all cavities and generates subdomains accordingly;
  - sd 4 : meshes non-manifold geometries as such and generates subdomains accordingly.

Note
:   If MG-CADSurf is used as 2D algo, and if a GMF file is defined as output file (using SetGMFFile(my2Dmesh.mesh)), then MG-Hexa will use this file as input. This allows to avoid the reconstruction of the GMF file from the SMESH structure and can improve the global computation time.

**See Also** a sample TUI Script of the [creation of a MG-Hexa mesh](hexoticplugin_python_interface_page.md#tui_hexotic)

# Advanced parameters

![hexotic_advanced_options.png](https://docs.salome-platform.org/latest/gui/HexoticPLUGIN/hexotic_advanced_options.png)

In **Advanced** tab page you can specify advanced options of MG-Hexa not exposed in other pages.

**Add option** adds a line to the table where you can type an option and its value as text. A check box in the first column activates/deactivates the option of the current row. A deactivated option will be erased upon pressing *Ok*.

- **Allow invalid elements** - specifies that the mesher must conform as much as possible to the geometry (especially the sharp edges). The resulting meshes may contain invalid elements (but with positive volumes: for example, three vertices of an hexahedron on the same edge), for the benefit of better geometry accuracy.
- **Compute ridges** - Enables the computation of ridges. If set to no, smooth meshes (without ridges) will be generated. A ridge is a geometrical entity (a sharp edge). The resulting meshes will have better quality elements, at the price of "smoothing" out the geometry.
- **Element order** - determines the order of the mesh elements to be generated: *linear* or *quadratic*
- **Enforce constant layer size** - force the first physical layer to have the same size throughout the mesh.
- **Flatten hexa sides** - activates specific optimization process to flatten the sides of hexahedra.
- **Nb. Hexes Min Level** - allows defining the minimal level of recursive partitioning on the initial octree cube.
- **Nb. Hexes Max Level** - allows defining the maximal level of recursive partitioning on the initial octree cube.
- **Maximal memory (MB)** - specifies the maximum allocatable memory in MegaBytes.
- **Maximal number of threads** - specifies the number of threads to be used (this should be the number of cores or processors of a shared memory parallel architecture).
- **Recover sharp angles** - subdivides elements around sharp angles up to **Nb. Hexes Max Level**.
- **Ridge angle (degrees)** - specifies the angle between two triangles above which the hex mesher will consider the edge common to these two triangles as being a "ridge". A ridge is a geometrical entity (a sharp edge) which has to be kept as it is in the final hex mesh.The default value is 60 (degrees).  
  If you raise this value, the hex mesher will detect less ridges, and the final solid mesh will therefore be smoother. On the other hand, if you reduce this value, more ridges will be detected and the algorithm will face harder situations to conform to.
- **Size map level** - when using a sizemap, sets the octree's maximum subdivision level to apply to the sizemap.
- **Tags** - sets how surface attributes must be considered.

  - *respect:* preserve surface attributes
  - *clear:* clear surface attributes
- **Working directory** - specifies the directory where the input/output files will be created.
- **Verbosity** - specifies the verbose level to print information on meshing steps.
- **Print log in a file** - if this option is checked on the log is printed in a file placed in the working directory, otherwise it is printed on the standard output.
- **Remove log on success** - if this option is checked on the log file is kept only if an error occurs during the computation. This option is only available if **Print log in a file** is enabled (there must be a log file to delete it) and **Keep all working files** is disabled (in this case the log file is always kept).
- **Keep working files** - allows checking input and output files of MG-Hexa software, while usually these files are removed after the launch of the mesher. The log file (if any) is also kept if this option is checked.

# Local size

The local size allows you to drive locally the density of the 3D mesh. The area where the mesh has to be refined is given as a geometrical shape.

![hexotic_local_size_parameters.png](https://docs.salome-platform.org/latest/gui/HexoticPLUGIN/hexotic_local_size_parameters.png)

- **Selection field (Shape)** - Area where the hexahedral mesh has to be refined. You can select any kind of shape (vertex, edge, face, solid, ...). The shape can be a sub-shape of the main shape or not.
- **Local size** - Expected size of the hexahedral mesh in (Solid) or near the given shape
- **Add button** - Add the local size to the list of local sizes (showed on the left)
- **Remove button** - Remove a local size from the list, select the local size in the list and press *Remove*

Note
:   The local size will only influence the density towards a locally denser mesh. If the required density is coarser than the one determined automatically by the global size parameters (min size, max size, min level, max level), it will be ignored and the default density will be used.

# Viscous layers

The viscous layers allows you to set up parameters of Viscous Layers supported by MG_Hexa mesher.

![hexotic_vl_parameters.png](https://docs.salome-platform.org/latest/gui/HexoticPLUGIN/hexotic_vl_parameters.png)

- **Number of layers** - number of boundary layers.
- **Size of the first layer** - height of the first layer.
- **Direction of the layers** - describes whether the layers grow inwards or outwards.
- **Growth** - geometric progression for the boundary layer growth.
- **Faces with layers** - list of surface references from which the boundary layers should be grown.
- **Imprinted faces** - list of surface references that can be imprinted by boundary layers.
