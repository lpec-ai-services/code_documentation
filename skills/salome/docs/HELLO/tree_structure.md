<!-- source: https://docs.salome-platform.org/latest/gui/HELLO/tree_structure.html -->

# Create the module tree structure

The first step in the development process is the creation of the module tree file hierarchy. The typical SALOME module usually includes configuration files (used in the build procedure of a module), CMakeLists.txt files, IDL file that provides a definition of a CORBA services implemented in a module and a set of source files which are compiled by the build procedure to the module CORBA engine library and (optionally) GUI library.

The following file structure is typical for the SALOME module:

```python

+ HELLO1_SRC
   + CMakeLists.txt
   + SalomeHELLOConfig.cmake.in
   + HELLO_version.h.in
   + AUTHORS
   + COPYING
   + ChangeLog
   + INSTALL
   + NEWS
   + README
   + adm_local
     + CMakeLists.txt
     + cmake_files
       + CMakeLists.txt
       + FindSalomeHELLO.cmake
   + bin
     + CMakeLists.txt
     + VERSION.in
     + runHELLO.in
     + runHELLO.py
   + idl
     + CMakeLists.txt
     + HELLO_Gen.idl
   + src
     + CMakeLists.txt
     + HELLO
       + CMakeLists.txt
       + HELLO.hxx
       + HELLO.cxx
     + HELLOGUI
       + CMakeLists.txt
       + HELLOGUI.h
       + HELLOGUI.cxx
       + HELLO_msg_en.ts
       + HELLO_msg_fr.ts
       + HELLO_icons.ts
   + resources
     + CMakeLists.txt
     + HELLO.png
     + goodbye.png
     + handshake.png
     + testme.png
     + HELLOCatalog.xml.in
     + SalomeApp.xml.in
   + doc
     + CMakeLists.txt
     + doxyfile.in
     + index.doc
     + images
       + head.png
     + static
       + doxygen.css
       + footer.html
       + header.html.in
```

Note that other files can be optionally present.

The usual way of the sources directory tree structure initial creation is to copy it from the existing SALOME module.

Warning
:   The files of the platform base module (KERNEL) must not be copied to initialise a module tree structure. It is usually preferable to copy files from another module such as GEOM or MED.

The module name is HELLO, the component name is HELLO and all the files are put in a directory named HELLO1_SRC. Below is a short description of these files. Note, that files with .in suffix are the cmake templates from which the actual files are generated during the build procedure.

- `CMakeLists.txt`

These files are input text files that contain the project parameters and describe the flow control of the build process in simple CMake language as a part of the build system based on CMake. These files define the build procedure, namely, compilation and installation rules such as compiler and linker options, installation destination folder, package version etc.

- `AUTHORS`
- `COPYING`
- `ChangeLog`
- `INSTALL`
- `NEWS`
- `README`

These files are a usual part of open source projects. These files are used by developers to provide an additional information on a product, like license, authors and distribution information, change log between versions of a product, installation hints, etc.

- `HELLO_version.h.in`

This is an optional C++ header file, that specifies the version macro-definitions which can be used, for example, in other modules to check the version of the SALOME module (HELLO module in this case).

- `adm_local`

This directory contains additional administrative files used by the build procedure.

- `adm_local/cmake_files/FindSalomeHELLO.cmake`

Some modules can need some external packages in order to compile and run properly. The usual approach is to write a special *.cmake file for the purpose of finding a certain piece of software and to set it's libraries, include files and definitions into appropriate variables so that they can be used in the build process of another project. It is possible to include the standard CMake detection modules (FindXyz.cmake files, located in the standard CMake installation directory) or, if CMake does not provide a search procedure for some required software, it is necessary to create *.cmake module for each pre-requisite.

Also, it is good idea to create and distribute *.cmake file for the project being developed; it can be used then in the dependent projects. For example, HELLO module installs a file FindSalomeHELLO.cmake that can be used for its detection.

To search SALOME HELLO module in some other project it will be only needed to write the following code in CMakeLists.txt:

```python
FIND_PACKAGE(SalomeHELLO)
```

- `bin`

This directory usually contains different scripts.

- `bin/VERSION.in`

This file is used to document the module, it must give its version (at least) and (optionally) compatibilities or incompatibilities with other modules. This file is strongly recommended but is not essential for operation of the module.

- `bin/runHELLO.in`
- `bin/runHELLO.py`

These files are not essential but make the example easier to use. These are scripts that can be used to run SALOME session with HELLO module.

- `idl`

This directory contains IDL files that specify the CORBA services supplied by SALOME module.

- `idl/HELLO_Gen.idl`

This is the CORBA IDL definition of the services implemented by SALOME HELLO module.

- `src`

This is a root directory of the module source codes. Usually it contains one or more sub-directories that provide an implementation of module libraries, executables, Python API modules, etc. The hierarchy of the sources tree is arbitrary; it follows the specific module needs.

- `src/HELLO`

This directory provides implementation of engine library.

- `src/HELLO/HELLO.hxx`
- `src/HELLO/HELLO.cxx`

These files provide the implementation of a CORBA engine library of the HELLO module. In particular, this is an implementation of the services defined in the `HELLO_Gen.idl` file.

- `HELLOGUI`

It is an optional directory that provides an implementation of HELLO module's GUI library.

Strictly speaking, the GUI library is optional for each SALOME module. In some cases it's enough to implement CORBA engine only. Then, the services of the module will be available in a CORBA environment. The module can be loaded to the SALOME container and its services can be used in the SALOME supervision computation schemas, in Python scripts or/and in C++ implementation of other modules.

A GUI library is necessary only if it is planned to access the module functionality from the SALOME GUI session via menu actions, dialog boxes and so on.

- `src/HELLOGUI/HELLOGUI.h`
- `src/HELLOGUI/HELLOGUI.cxx`

These files provide the implementation of a GUI library of the HELLO module. In particular, these files specify menus, toolbars, dialog boxes and other such staff.

- `src/HELLOGUI/HELLO_msg_en.ts`
- `src/HELLOGUI/HELLO_msg_fr.ts`
- `src/HELLOGUI/HELLO_icons.ts`

These files provide a description (internationalization) of GUI resources of the HELLO module. `HELLO_msg_en.ts` provides an English translation of the string resources used in a module (there can be also translation files for other languages, for instance French; these files are distinguished by the language suffix). `HELLO_icons.ts` defines images and icons resources used within the GUI library of HELLO module. Please refer to Qt linguist documentation for more details.

- `resources`

This optional directory usually contains different resources files required for the correct operation of SALOME module.

- `resources/HELLO.png`
- `resources/handshake.png`
- `resources/goodbye.png`
- `resources/testme.png`

These are different module icon files. `HELLO.png` file provides main icon of HELLO module to be shown in the SALOME GUI desktop. Other files are the icons for the functions implemented by the module; they are used in the menus and toolbars.

- `resources/HELLOCatalog.xml.in`

The XML description of the CORBA services provided by the HELLO module. This file is parsed by SALOME supervision module (YACS) to generate the list of service nodes to be used in the calculation schemas. The simplest way to create this file is to use Catalog Generator utility provided by the SALOME KERNEL module, that can automatically generate XML description file from the IDL file. In GUI, this utility is available via the Tools main menu.

- `resources/SalomeApp.xml.in`

This file is essential for each SALOME module. It provides some parameters of the module which define its behavior in SALOME. In particular it should provide a section with the name corresponding to the name of a module ("HELLO" in our case) with the following parameters:

```python
<section name="HELLO">
  <parameter name="name"          value="Hello"/>
  <parameter name="icon"          value="HELLO.png"/>
  <parameter name="version"       value="@SALOMEHELLO_VERSION@"/>
  <parameter name="documentation" value="hello_help"/>
</section>
```

The *"name"* parameter defines GUI name of a module. The *"icon"* parameter defines a GUI icon of a module. Optional *"version"* parameter defines the version of the module. The *"documentation"* parameter provides a name for the help-related resource section (see below).

The section *"resources"* of a file specifies the directory that contains resources of a module (icons, translation files, etc).

```python
<section name="resources">
  <parameter name="HELLO" value="%HELLO_ROOT_DIR%/share/salome/resources/hello"/>
</section>
```

The section *"hello_help"* provides information on the location of the help page(s) and the eventual sub-menu in the Help menu. The name of this section can be arbitrary, in such a case it should be specified in the main module's resources section (see above). Alternatively, this section's name can have syntax *"<module_name>_documentation"*, where *module_name* is a name of the module. If such section is present in the resource file, it is not necessary to specify it in the module's main section.

Parameter *"sub_menu"* of the documentation section allows sepecifying the name of the sub-menu in the Help main menu where the documentation materials of a module should be put.

```python
<section name="hello_help" >
  <parameter name="sub_menu"        value="Samples"/>
  <parameter name="%1 User's Guide" value="%HELLO_ROOT_DIR%/share/doc/salome/gui/HELLO/index.html"/>
</section>
```

- `doc`

This directory containes the files related to the module's documentation.

- `doc/doxyfile.in`

The **Doxygen** configuration file. The Doxygen is used to build this documentation. The file `doxyfile.in` provides a rules for the generation of module documentation.

- `doc/index.doc`

An input file for the Doxygen, which provides a source of this documentation.

- `doc/images`

This sub-folder contains images used in the documentation.

- `doc/static`

This sub-folder contains auxiliary files used when generating documentation by Doxygen, like header (`header.html.in`) and footer (`footer.html`) of the HTML pages, style sheet (`doxygen.css`) etc.

[<< Previous](dev_steps.md)  
[>> Next](build_proc_files.md)
