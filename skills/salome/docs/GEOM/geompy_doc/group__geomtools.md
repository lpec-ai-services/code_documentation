<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__geomtools.html -->

# geomtools - Tools to access GEOM engine and objects

## Detailed Description

This module provides tools to facilitate the use of geom engine and geom objects in Salome.

## Function Documentation

### getGeompy()

```python
def geomtools.getGeompy()
```

Return an object behaving exactly like geompy module.

### TEST_createAndDeleteShape()

```python
def geomtools.TEST_createAndDeleteShape()
```

This test is a simple use case that illustrates how to create a [GEOM](namespaceGEOM.md) shape in a SALOME session (create the [GEOM](namespaceGEOM.md) object, put in in the study, and display the shape in a viewer) and delete a shape from a SALOME session (erase the shape from the viewer, delete the entry from the study, and finally destroy the underlying [GEOM](namespaceGEOM.md) object).
