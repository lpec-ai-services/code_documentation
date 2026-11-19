<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/python_interface.html -->

# Geometry module Python Interface

The GEOM python package essentially contains:

- Python Interface [geomBuilder.py](geompy_page.md) to import/export, create and transform geometrical objects, manage fields, use measurement tools;
- Utility functions within Python module [geomtools.py](manipulate_object.md) to handle GEOM items in SALOME study:
  - add or remove a shape;
  - display or erase a shape in the viewer;
  - completely delete a shape (undisplay, unpublish, and destroy it);
  - manage the selection in the object browser.
- [Wrapping functions](pythonutils_page.md) for GEOM tools
- Python package [structelem](struct_elem_visualisation.md) that provides functions to create geometrical 3D representations of mechanical models called "structural elements"

The functions are distributed in the python package *salome.geom.* Its documentation is mainly generated from the code of source python files.

Note
:   The main package *salome* contains other sub-packages that are distributed with the other SALOME modules. For example, the KERNEL module provides the python package salome.kernel and SMESH the package salome.smesh.
