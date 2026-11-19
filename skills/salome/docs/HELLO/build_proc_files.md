<!-- source: https://docs.salome-platform.org/latest/gui/HELLO/build_proc_files.html -->

# Build procedure input files

In most cases SALOME uses **CMake-based** build system for modules. CMake is a cross-platform build system which works on Linux, Windows and other operating systems.

The `CMakeLists.txt` files are used to describe the build procedure, in particular:

- Test platform;
- Test system configuration;
- Detect pre-requisites;
- Generate build rules (for example, standard UNIX makefiles on Linux, MSVC solutions, etc).

Project's root directory provides main CMake configuration that allows build all targets into one set of binaries and libraries. Each sub-directory also includes CMake configuration file (CMakeLists.txt) that specifies targets being build.

The file `CMakeLists.txt` in root directory of the HELLO module provides basic build rules to be used in other `CMakeLists.txt` files. It sets main properties of project: name, version, pre-requisites, installation paths, programming languages being used by the project, tree of sub-directories, etc.

A lot of files used by the build procedure of HELLO module are located in SALOME KERNEL module (that is referenced by the `KERNEL_ROOT_DIR` environment variable), namely in its `salome_adm` sub-folder. Similarly, the `GUI_ROOT_DIR` environment variable is used for the graphical user interface (GUI) module of SALOME; this module also provides a set of configuration utilities (`*`.cmake files) in its `adm_local` folder.

The files with an .in extension are the skeletons which are processed by CMake to transform it to the resulting files in the build directory during the configuration process.

[<< Previous](tree_structure.md)  
[>> Next](idl_dir.md)
