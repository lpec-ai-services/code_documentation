<!-- source: https://docs.salome-platform.org/latest/gui/PYHELLO/tree_structure.html -->

# Create the module tree structure

The first step in the development process is the creation of the module tree file structure. The typical SALOME module usually includes some set of the configuration files (used in the build procedure of a module), Makefiles, IDL file that provides a definition of a CORBA services implemented in a module and a set of source Python files which implement the module CORBA engine and (optionally) its GUI.

The following file structure is typical for the SALOME module:

```python

+ PYHELLO1_SRC
   + CMakeLists.txt
   + SalomePYHELLOConfig.cmake.in
   + adm_local
     + CMakeLists.txt
     + cmake_files
       + CMakeLists.txt
       + FindSalomePYHELLO.cmake
   + bin
     + CMakeLists.txt
     + VERSION.in
     + runPYHELLO.in
     + runPYHELLO.py
   + idl
     + CMakeLists.txt
     + PYHELLO_Gen.idl
   + src
     + CMakeLists.txt
     + PYHELLO
       + CMakeLists.txt
       + PYHELLO.py
       + PYHELLO_utils.py
     + PYHELLOGUI
       + CMakeLists.txt
       + PYHELLOGUI.py
       + PYHELLO_msg_en.ts
       + PYHELLO_msg_fr.ts
       + PYHELLO_icons.ts
   + resources
     + CMakeLists.txt
     + PYHELLO.png
     + PYHELLO_small.png
     + ExecPYHELLO.png
     + handshake.png
     + stop.png
     + PYHELLOCatalog.xml.in
     + SalomeApp.xml.in
     + schema.xml
   + doc
     + CMakeLists.txt
     + doxyfile.in
     + index.doc
```

Note that other files can be optionally present. For example, in some SALOME modules sources tree you can find such files as AUTHORS, INSTALL, ChangeLog, COPYING, NEWS, README, etc. Some files are specific only for this PYHELLO sample module, for example PNG images in the resources directory which are used in the GUI dialog boxes etc.

The usual way of the sources directory tree structure initial creation is to copy it from the existing SALOME module.

Warning
:   The files of the platform base module (KERNEL) must not be copied to initialise a module tree structure. It is usually preferable to copy files from another module such as GEOM or MED.

The module name is PYHELLO, the component name is PYHELLO and all the files are put in a directory named PYHELLO1_SRC. Below is a short description of these files. Note, that files with .in suffix are the cmake templates from which the actual files are generated during the build procedure.

- `CMakeLists.txt`

These files are input text files that contain the project parameters and describe the flow control of the build process in simple CMake language as a part of the build system based on CMake. These files define the build procedure, namely, compilation and installation rules such as compiler and linker options, installation destination folder, package version etc.

- `adm_local`

This directory contains additional administrative files used by the build procedure.

- `adm_local/cmake_files/FindSalomePYHELLO.cmake`

Some modules can need some external packages in order to compile and run properly. The usual approach is to write a special *.cmake file for the purpose of finding a certain piece of software and to set it's libraries, include files and definitions into appropriate variables so that they can be used in the build process of another project. It is possible to include the standard CMake detection modules (FindXyz.cmake files, located in the standard CMake installation directory) or, if CMake does not provide a search procedure for some required software, it is necessary to create *.cmake module for each pre-requisite.

Also, it is good idea to create and distribute *.cmake file for the project being developed; it can be used then in the dependent projects. For example, PYHELLO module installs a file FindSalomePYHELLO.cmake that can be used for its detection.

To search SALOME PYHELLO module in some other project it will be only needed to write the following code in CMakeLists.txt:

```python
FIND_PACKAGE(SalomePYHELLO)
```

- `bin`

This directory usually contains different scripts.

- bin/VERSION.in

This file is used to document the module, it must give its version (at least) and (optionally) compatibilities or incompatibilities with other modules. This file is strongly recommended but is not essential for operation of the module.

- bin/runPYHELLO.in
- bin/runPYHELLO.py

These files are not essential but make the example easier to use. These are scripts that can be used to run SALOME session with PYHELLO module.

- `idl`

This directory contains IDL files that specify the CORBA services supplied by SALOME module.

- idl/PYHELLO_Gen.idl

This is the CORBA IDL definition of the services implemented by SALOME PYHELLO module.

- `src`

This is a root directory of the module source codes. Usually it contains one or more sub-directories that provide an implementation of module libraries, executables, Python API modules, etc. The hierarchy of the sources tree is arbitrary; it follows the specific module needs.

- src/PYHELLO/PYHELLO.py
- src/PYHELLO/PYHELLO_utils.py

These files provide the implementation of a CORBA engine of the PYHELLO module. In particular, this is an implementation of the services defined in the PYHELLO_Gen.idl file.

- src/PYHELLOGUI/PYHELLOGUI.py

The src/PYHELLOGUI is an optional directory that provides an implementation of PYHELLO module's GUI. Strictly speaking, the GUI is optional for each SALOME module. In some cases it's enough to implement CORBA engine only. Then, the services of the module will be avaiable in a CORBA environment. The module can be loaded to the SALOME container and its services can be used in the Supervisor computation schemas, in Python scripts or/and refer to it in other modules. A GUI is necessary in the cases if it is planned to access to the module functionality from the SALOME GUI session via menu actions, dialog boxes and so on.

- src/PYHELLOGUI/PYHELLO_msg_en.ts
- src/PYHELLOGUI/PYHELLO_msg_fr.ts
- src/PYHELLOGUI/PYHELLO_icons.ts

These files provide a description (internationalization) of GUI resources of the PYHELLO module. `PYHELLO_msg_en.ts` provides an English translation of the string resources used in a module. `PYHELLO_icons.ts` defines images and icons resources used within the GUI of the PYHELLO module. Please refer to Qt linguist documentation for more details.

- `resources`

This optional directory usually contains different resources files required for the correct operation of SALOME module.

- resources/PYHELLO.png
- resources/PYHELLO_small.png
- resources/ExecPYHELLO.png
- resources/handshake.png
- resources/stop.png

The resources folder usually includes different resource files used within the SALOME module. For example, PYHELLO.png file provides an icon of PYHELLO module to be shown in the SALOME GUI desktop. ExecPYHELLO.png is an icon for the makeBanner() function used in the menu and toolbar. The icons handshake.png and stop.png are used in the dialog boxes and PYHELLO_small.png icon is used to display in the Object browser for root PYHELLO entity.

- resources/PYHELLOCatalog.xml.in

The XML description of the CORBA services provided by the PYHELLO module. This file is parsed by Supervisor and YACS module to generate the list of service nodes to be used in the calculation schemas. The simplest way to create this file is to use Catalog Generator utility provided by the SALOME KERNEL module, that can automatically generate XML description file from the IDL file.

- resources/SalomeApp.xml.in

This file is essential for the module. It provides some parameters of the module which define module behavior in SALOME. In particular it should provide a section with the name corresponding to the name of a module ("PYHELLO" in this case) with the following parameters:

```python
<section name="PYHELLO">
  <parameter name="name"            value="PyHello"/>
  <parameter name="icon"            value="PYHELLO.png"/>
  <parameter name="library"         value="SalomePyQtGUI"/>
  <parameter name="documentation"   value="pyhello_help"/>
  <parameter name="version"         value="@SALOMEPYHELLO_VERSION@"/>
</section>
```

The *"name"* parameter defines GUI name of a module. The *"icon"* parameter defines a GUI icon of a module. The parameter *"library"* specifies the name of the C++ library representing the front-end of the module in the SALOME GUI desktop. The Python modules which do not implement its own C++ front-end GUI library should specify "SalomePyQtGUI" value in this parameter. The *"documentation"* parameter provides a name for the help-related resource section (see below). The *"version"* parameter defines the version of the module.

The section *"resources"* also specifies the directory that contains resources of a module (icons, translation files, etc).

```python
<section name="resources">
  <parameter name="PYHELLO" value="${PYHELLO_ROOT_DIR}/share/salome/resources/pyhello"/>
</section>
```

The section *"pyhello_help"* provides information on the location of the help page and the eventual sub-menu in the Help menu.

```python
<section name="pyhello_help" >
  <parameter name="sub_menu"        value="Samples"/>
  <parameter name="%1 User's Guide" value="%PYHELLO_ROOT_DIR%/share/doc/salome/gui/PYHELLO/index.html"/>
</section>
```

- doc/doxyfile.in

The Doxygen configuration file. The Doxygen is used to build this documentation. The file doxyfile.in provides a rules for the generation of module documentation.

- doc/index.doc

An input file for the Doxygen, which provides a source of this documentation.

- `doc/images`

This sub-folder contains images used in the documentation.

- `doc/static`

This sub-folder contains auxiliary files used when generating documentation by Doxygen, like header (`header.html.in`) and footer (`footer.html`) of the HTML pages, style sheet (`doxygen.css`) etc.

[<< Previous](dev_steps.md)  
[>> Next](build_proc_files.md)
