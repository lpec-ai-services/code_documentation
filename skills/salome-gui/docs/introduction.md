<!-- source: introduction.rst -->

# Introduction to Salome Platform

Welcome to SALOME Platform! Modern technological products (cars, structures, electrical or electronic equipment) are getting more and more complex every year and must meet increasingly severe requirements in terms of quality and performance. For example, for structures and their environment the demands to reduce risks and optimize costs are extremely high. It requires particularly refined simulations concerning structural behavior and robustness to ensure high reliability.

The numeric modeling of a physical problem, the development of solutions and their integration into the design process are often handled in very specific environments. SALOME represents a generic CAD-based application for digital simulation with "high reactivity to market evolutions and customer expectations".

SALOME is a free software that provides a generic platform for Pre and Post-Processing for numerical simulation. It is based on an open and flexible architecture made of reusable components available as free software.

SALOME is a CAD/CAE integration platform. It provides reusable components for:

1.  3D modeling (bottom-up construction, import, healing);
2.  Visualization;
3.  Computational schemas management;
4.  Post-processing.

SALOME is tailored for integration of custom components:

1.  CAD interfaces;
2.  Mesh generators;
3.  Finite Element solvers with specific pre-processors.

The SALOME platform is available in Open Source.

**Salome Platform:**

1.  Supports interoperability between CAD modeling and computation software (CAD-CAE link)
2.  Makes easier the integration of new components on heterogeneous systems for numerical computation
3.  Sets the priority to multi-physics coupling between computation software
4.  Provides a generic user interface, user-friendly and efficient, which helps to reduce the costs and delays of carrying out the studies
5.  Reduces training time to the specific time for learning the software solution which has been based on this platform
6.  All functionalities are accessible through the programmatic integrated Python console

**What can you do in SALOME? (Some of SALOME main functions)**

1.  Define geometrical models (create/modify geometrical items), import and export them using the BREP, IGES and STEP formats;
2.  Define meshing of these geometrical items, import and export them;
3.  Handle physical properties and quantities attached to geometrical items, import and export them to a reusable format;
4.  Perform computations using a solver (optionally provided): read input data, configure the solver, and write calculation results);
5.  Visualize result fields in 3D, 2D and export images of their visualization to an appropriate format;
6.  Manage study schemes: definition, save/restore;
7.  Manage computation schemes: definition, execution.

This part of documentation on Salome also covers `introduction_to_gui_page`, common for all modules, such as study management, Salome viewers, preferences, etc.

And finally, there is an additional chapter, which provides a short guide about the `tui_page` to access SALOME GUI functionalities from the Python code.

- `introduction_to_gui.rst` (`introduction_to_gui.rst.md`)
- `text_user_interface.rst` (`text_user_interface.rst.md`)
