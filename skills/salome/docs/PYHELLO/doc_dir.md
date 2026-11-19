<!-- source: https://docs.salome-platform.org/latest/gui/PYHELLO/doc_dir.html -->

# The doc directory

This directory provides documentation files of the module. The documentation of the module can be implemented in the arbitrary way. But if you want your documentation to appear in the SALOME GUI desktop's Help menu, some specific actions should be done as follows.

The documentation should be generated in the HTML format. For example, the documentation of the PYHELLO module is generated using Doxygen tool. It allows to generate structured set of HTML pages from the set of input plain text files. Input source files should include Doxygen tags and optionally direct HTML tags. For more details please refer to the Doxygen documentation.

The resulting documentation of a module should include at least one file index.html. All the HTML and image files should be exported by the build procedure to the following directory: <module_installation_dir>/share/doc/salome/gui/<MODULE> where <module_installation_dir> is a module installation folder and MODULE is its name. For example, for PYHELLO module, at least one file should exist: <PYHELLO_module_installation_dir>/share/doc/salome/gui/PYHELLO/index.html.

The SALOME GUI automatically searches for the index.html file in the mentioned module directory. If the file is found, the corresponding menu command is automatically added to the Help menu of the SALOME GUI desktop.

[<< Previous](bin_dir.md)  
[>> Next](build_procedure.md)
