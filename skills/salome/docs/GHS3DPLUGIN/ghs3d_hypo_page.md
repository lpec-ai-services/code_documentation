<!-- source: https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/ghs3d_hypo_page.html -->

# MG-Tetra Parameters hypothesis

### Table of Contents

- [General parameters](#ghs3d_general_parameters)
- [Advanced parameters](#ghs3d_advanced_parameters)
  - [Advanced meshing options for MG-Tetra algorithm](#advanced_meshing_options)
  - [Advanced meshing options for MG-Tetra and MG-Tetra HPC algorithms](#advanced_meshing_options_HPC)
  - [Memory settings (disable when MG-Tetra HPC is selected)](#memory_settings)
  - [Logs and debug](#log)
- [Enforced vertices](#ghs3d_enforced_vertices)
- [Enforced Meshes](#ghs3d_enforced_meshes)

MG-Tetra Parameters hypothesis works only with **MG-Tetra** algorithm. This algorithm is a commercial software.

To get a license, visit <http://www.meshgems.com/meshgems-products.html>

# General parameters

![ghs3d_parameters_basic.png](https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/ghs3d_parameters_basic.png)

- **Name** - allows to define the name of the hypothesis (MG-Tetra Parameters by default).
- **Algorithm Selection** - allows to select the version of MG-Tetra algorithm to be used.
- **Optimization level** - allows choosing the required optimization level (higher level of optimization provides better mesh, but can be time-consuming):
  - none
  - light
  - medium (standard)
  - standard+ (not available whem MG-Tetra HPC is selected)
  - strong
- **Minimal size** - sets the minimum edge size in the generated mesh.
- **Maximal size** - sets the maximum edge size in the generated mesh.
- **Maximal number of threads** - define the maximal number of threads to be used by the meshing algorithm. On selection of this box the Pthread mode is activated when MG-Tetra is selected and Parallel mode is activated if the MG-Tetra HPC algorithm is selected.
- **Pthread mode** - define the parallel strategy used by the mesher when MG-Tetra is selected.
  - none
  - aggresive - is faster than the sequential mode, but the quality of the resulting mesh may altered compared to the sequential mode.
  - safe - is slower than the sequential mode, but the quality of the mesh can only improve;
- **Paralle strategy (HPC)** - define the parallel strategy used by the mesher when MG-Tetra HPC is selected.
  - none
  - reproducible_given_max_number_of_threads
  - reproducible
  - aggressive
- **Volumic gradation** - Defines the volumic ratio between 2 consecutive elements. WARNING: Changing the default value of this parameter may dramatically decrease the quality of the resulting mesh.
- **Use volume proximity** - activates consideration of distance between opposite surfaces.
  - **Number of layers** - asks for at least given number of layers of tets between opposite surfaces.
- **Mesh holes** - if checked, the algorithm will create mesh in the holes inside a solid shape, else only the outermost shape will be meshed. Volumic elements created within holes are bound to the solid.
- **Make groups of domains** - if checked, the algorithm will create groups of just generated elements corresponding to each mesh domain.

[Back to top](ghs3d_hypo_page.md#ghs3d_top)

# Advanced parameters

![ghs3d_parameters_advanced.png](https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/ghs3d_parameters_advanced.png)

## Advanced meshing options for MG-Tetra algorithm

Advanced page tab expose mostly useful advanced options. Initially, default values of the options are displayed and they are not modifiable. If an option is activated using a check-box, its value becomes modifiable.

**Add option** button adds a line to the table where you can type an option and its value as text. A check box in the first column activates/deactivates the option of the current row. A deactivated option will be erased upon pressing *Ok*.

- **Gradation on skin** - This option set or not the gradation value on the initial size of the skin vertices.
  - **no** the gradation is not applied on the skin vertices. In this case the initial size of a vertex is the average edges lenght which belong the vertex.
  - **yes** the gradation is applied on the skin vertices. In this case the initial size of a vertex is the average edges lenght which belong the vertex multiplied by the gradation.
- **Boundary regeneration** - defines the boundary regeneration mode. MeshGems-Tetra uses alternative strategies for boundary regeneration.
  - **standard** means that the standard boundary regeneration algorithm is used.
  - **safe** means that various methods are tried as long as the regeneration phase fails (including the alternate boundary recovery mode), can be time consuming and can fail in very difficult cases.
  - **recovery** means that the alternate boundary recovery version is activated. Check **Using MeshGems-Tetra with the boundary recovery module** chapter of MG-Tetra User Manual.
- **Force maximum edge size** - This option can be used to force the desired maximum edge size in the generated mesh given by the **Max Size** parameter. The default value is no, meaning that the maximum edge length can be greater than the given value of the **Max Size** parameter.
- **Force quadratic mesh** - This option permits to write or not an output mesh file in case of negative Jacobians when generating a quadratic mesh. Refer to section 4.6.3 for more details.
  - **no** means that no output is written (this is the default);
  - **yes** means that an output is written even in case of negative Jacobians.
- **Respect surface mesh** - This option forbids or not the correction of input triangles and enforced edges mid-nodes to make the element Jacobian strictly positive when generating a quadratic mesh.
  - **yes** means that the input triangles and edges mid-nodes are unchanged, the correction of nodes is only applied in the volume.
  - **no** means that the input triangles and edges mid-nodes can be moved. The correction of nodes is applied in the volume and the mid-nodes correction can be applied on the input triangles and edges mid-nodes. The corrected surface mid-nodes are approximated on the surface first, or put on the linear edges; The corrected edges mid-nodes can be put on the linear edges.
- **Max number of errors** - the error messages will be printed up to a given maximum number of errors. At least 1 error is printed and at most 100 errors are printed to prevent infinite loops.
- **No central point** - **yes** prevents adding an internal point at the centre of gravity of the bounding box that MeshGems-Tetra uses by default in order to speed up and to simplify the meshing process. This option can be particularly useful to:
  - generate a volume mesh without internal points at all;
  - in some rare cases, help the boundary regeneration phase when it failed with the standard options (for example when one dimension of the domain is large compared to the other two with a ratio of 20 or more). Use this option when the boundary regeneration failed with the standard parameters and before using the recovery version.
- **Optimise worst elements** - Applies an optimization processing to improve the worst quality elements whenever possible.
- **Rectify jacobian** - This option activates correction of some nodes so as to make the Jacobian of element strictly positive when generating a quadratic mesh.
- **Sliver angle** - This options can be used to specify to MeshGems-Tetra what is considered as a sliver and what is not. The user has the possibility to specify an angle (in degrees), which caracterizes a sliver : any tetrahedron which has at least an angle below this value will be considered as a sliver.
- **Target quality** - Sets the desired maximum target of worst quality acceptable for the volume mesh used during optimisation phase. When defined, an optimization processing is applied to improve the quality until the given target is reached whenever possible. By default, this option is not activated which means that only the standard optimisations are performed (the quality target is the target quality computed by the program).

## Advanced meshing options for MG-Tetra and MG-Tetra HPC algorithms

This option is common to both algorithms. When MG-Tetra HPC algorithm is selected on the General Parameters view, all advanced options are disabled except the follow ones:

- **Remove overconstrained tetrahedra** - This option can be used to only split the tetrahadra which have at least two facets that belong to the surface mesh. It will not split the overconstrained edges in the mesh. The overconstrained tetrahedra are splitting, whenever possible, which ensures that no tetrahedron has no more than one boundary facet.
  - **no** means that no correction is applied;
  - **yes** means that the correction is applied after mesh generation;
  - **only** means only correction is applied to an existing mesh.

## Memory settings (disable when MG-Tetra HPC is selected)

- **Maximum memory size** - launches MG-Tetra software with work space limited to the specified amount of RAM, in Mbytes. If this option is checked off, the software will be launched with 7O% of the total RAM space.
- **Initial memory size** - starts MG-Tetra software with the specified amount of work space, in Mbytes. If this option is checked off, the software will be started with 100 Megabytes of working space.

## Logs and debug

- **Working directory** - allows defining the folder for input and output files of MG-Tetra software, which are the files starting with "GHS3D_" prefix.
- **Verbose level** - to choose verbosity level in the range from 0 to 10.
  - 0, no standard output,
  - 2, prints the data, quality statistics of the skin and final meshes and indicates when the final mesh is being saved. In addition the software gives indication regarding the CPU time.
  - 10, same as 2 plus the main steps in the computation, quality statistics histogram of the skin mesh, quality statistics histogram together with the characteristics of the final mesh.
- **Print log in a file** - if this option is checked on the log is printed in a file placed in the working directory, otherwise it is printed on the standard output.
- **Remove log on success** - if this option is checked on the log file is kept only if an error occurs during the computation. This option is only available if **Print log in a file** is enabled (there must be a log file to delete it) and **Keep all working files** is disabled (in this case the log file is always kept).
- **Keep all working files** - allows checking input and output files of MG-Tetra software, while usually these files are removed after the launch of the mesher. The log file (if any) is also kept if this option is checked.

[Back to top](ghs3d_hypo_page.md#ghs3d_top)

# Enforced vertices

![ghs3d_enforced_vertices.png](https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/ghs3d_enforced_vertices.png)

MG-Tetra algorithm can locally make the mesh finer. It is possible to define enforced vertices in the volume where the mesh will be detailed. A node will be created at the enforced vertex coordinates.

An enforced vertex is defined by:

- A vertex
  - from GEOM (Vertex, Compound) - only available on meshes with no geometry attached
  - or from (x,y,z) Cartesian coordinates
- A constant physical size. If this size is zero, then the mesh size is not affected.
- If a group name is given, the created node will be added to the group. If the group does not exist, it is created.

[Back to top](ghs3d_hypo_page.md#ghs3d_top)

# Enforced Meshes

![ghs3d_enforced_meshes.png](https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/ghs3d_enforced_meshes.png)

MG-Tetra algorithm can be forced by other meshes, sub-meshes or groups. The constraint elements should be contained entirely into the solid mesh.

- The constraint element types are:
  - NODE
  - EDGE
  - FACE
- If a group name is given, the enforced elements will be added to the group. If the group does not exist, it is created.

**See Also** a sample TUI Script of the [creation of a MG-Tetra hypothesis](ghs3dplugin_python_interface_page.md#tui_ghs3d), including enforced vertices and meshes.

[Back to top](ghs3d_hypo_page.md#ghs3d_top)
