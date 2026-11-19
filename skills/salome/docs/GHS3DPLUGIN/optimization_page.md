<!-- source: https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/optimization_page.html -->

# MG-Tetra Optimization Parameters hypothesis

### Table of Contents

- [General parameters](#mgtetra_optim_gen_params)
- [Advanced parameters](#mgtetra_optim_advanced_parameters)
  - [Memory settings](#mgtetra_optim_memory_settings)
  - [Logs and debug](#mgtetra_optim_log)
  - [Advanced meshing options](#mgtetra_optim_advanced_meshing_options)

MG-Tetra Optimization Parameters hypothesis works only with **MG-Tetra Optimization** algorithm. This algorithm is a commercial software.

To get a license, visit <http://www.meshgems.com/meshgems-products.html>

# General parameters

![mgtetra_optim_gen_params.png](https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/mgtetra_optim_gen_params.png)

- **Name** - allows to define the name of the hypothesis (MG-Tetra Parameters by default).
- **Optimization** - sets the optimisation type. If **Optimization** is:
  - No : no optimisation is applied
  - Yes (default): optimisation is performed upon mesh generation using the **Optimisation level** parameter
  - Only : only optimisation is performed to an existing mesh.
- **Optimization level** - allows choosing the required optimization level (higher level of optimization provides better mesh, but can be time-consuming):
  - none
  - light
  - medium (standard)
  - standard+
  - strong
- **Split overconstrained elements** - sets treatment of element having all their vertices on the input surface. If **Split overconstrained elements** is:
  - No (default): no correction is applied
  - Yes : correction is applied upon mesh generation
  - Only : only correction is applied to an existing mesh.
- **PThreads mode** - sets optimization mode when using multithread capabilities. Valid values are:
  - Safe : slower but quality can only get better
  - Aggressive : faster but quality may be altered
  - None (default): not activated.
- **Max number of threads** - sets the maximum number of threads to be used in parallel.
- **Smooth off sliver elements** - activates elimination of sliver elements as much as possible.
- **Create new nodes** - allows insertion of new nodes.

[Back to top](optimization_page.md#optimization_top)

# Advanced parameters

![mgtetra_optim_adv_params.png](https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/mgtetra_optim_adv_params.png)

## Memory settings

- **Initial memory size** - starts MG-Tetra software with the specified amount of work space, in Mbytes. If this option is checked off, the software will be started with 100 Megabytes of working space.
- **Maximum memory size** - launches MG-Tetra software with work space limited to the specified amount of RAM, in Mbytes. If this option is checked off, the software will be launched with 7O% of the total RAM space.

## Logs and debug

- **Working directory** - allows defining the folder for input and output files of MG-Tetra software, which are the files starting with "GHS3D_" prefix.
- **Verbose level** - to choose verbosity level in the range from 0 to 10.
  - 0, no standard output,
  - 2, prints the data, quality statistics of the skin and final meshes and indicates when the final mesh is being saved. In addition the software gives indication regarding the CPU time.
  - 10, same as 2 plus the main steps in the computation, quality statistics histogram of the skin mesh, quality statistics histogram together with the characteristics of the final mesh.
- **Print log in a file** - if this option is checked on the log is printed in a file placed in the working directory, otherwise it is printed on the standard output.
- **Remove log on success** - if this option is checked on the log file is kept only if an error occurs during the computation. This option is only available if **Print log in a file** is enabled (there must be a log file to delete it) and **Keep all working files** is disabled (in this case the log file is always kept).
- **Keep all working files** - allows checking input and output files of MG-Tetra software, while usually these files are removed after the launch of the mesher. The log file (if any) is also kept if this option is checked.

## Advanced meshing options

- A table allows to input in the command line any text for MG-Tetra, for example, advanced options.
- **Add option** - adds a line to the table where you can type an option and its value as text. A check box in the first column activates/deactivates the option of the current row. A deactivated option will be erased upon pressing *Ok*.

**See Also** a sample TUI Script of the [creation of a MG-Tetra Optimization hypothesis](ghs3dplugin_python_interface_page.md#tui_ghs3d).

[Back to top](optimization_page.md#optimization_top)
