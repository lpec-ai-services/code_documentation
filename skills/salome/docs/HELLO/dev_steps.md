<!-- source: https://docs.salome-platform.org/latest/gui/HELLO/dev_steps.html -->

# Steps in construction of the example module

The example module chosen to illustrate the process of SALOME module development is very simple. The module contains a single component and this component provides several services called **hello** and **goodbye**. Each of these functions accepts a character string as the arguments and returns the status of the operation. The component also provides a simple GUI.

The steps in the development are as follows:

- create a module tree structure
- create a SALOME component that can be loaded by a C++ SALOME container
- configure the module so that the component is known to SALOME
- add a GUI

[<< Previous](index.md)  
[>> Next](tree_structure.md)
