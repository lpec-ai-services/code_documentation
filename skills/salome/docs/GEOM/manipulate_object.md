<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/manipulate_object.html -->

# Manipulate GEOM object in the study (module geomtools)

The Python module [geomtools](geompy_doc/group__geomtools.md) provides utility functions to handle GEOM items in SALOME study:

- add or remove a shape;
- display or erase a shape in the viewer;
- completely delete a shape (undisplay, unpublish, and destroy it);
- manage the selection in the object browser

The usage of *geomtools* module can be tested with the following set of instructions:

```python
from salome.geom.geomtools import TEST_createAndDeleteShape
TEST_createAndDeleteShape()
```

This test executes the following procedure:

- Create, publish, and display a cylinder;
- Create, publish, and display a sphere;
- Create a box, publish it in a folder *boxset*, and display it in *pink* color.
- Erase the sphere from the viewer (the sphere still exists in the study)
- Delete the cylinder. It is no longer displayed and does not exist any more in the study or in the [GEOM](../GEOM/geompy_doc/namespaceGEOM.md) component.

At outcome of the test execution, the following objects appear in the SALOME session:

- The box located in a dedicated study folder and displayed in the viewer;
- The sphere in the standard place of the study, and not displayed.
