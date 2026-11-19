<!-- source: https://docs.salome-platform.org/latest/gui/PYHELLO/dev_steps.html -->

# Steps in construction of the example module

The example module chosen to illustrate the process of SALOME module development is extremely simple. The module contains a single component and this component provides a single service called **makeBanner** that accepts a character string as the sole argument and that returns a character string obtained by the concatenation of a 'Hello' and the input string. The component also provides a simple GUI.

The steps in the development are as follows:

- create a module tree structure
- create a SALOME component that can be loaded by a Python SALOME container
- configure the module so that the component is known to SALOME
- add a graphic GUI

[<< Previous](index.md)  
[>> Next](tree_structure.md)
