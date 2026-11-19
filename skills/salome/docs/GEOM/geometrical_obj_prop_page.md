<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geometrical_obj_prop_page.html -->

# Geometrical Object Types

**GetType function:**

The **Type** property of the geometrical object specifies the way the object has been created. It is an integer identifier that has a predefined value depending on the function type used for the object creation. The type of the object can be retrieved using the **GetType**() function of the **GEOM_Object** interface.

**For example**: the geometrical object created using [MakeBox()](../GEOM/geompy_doc/group__l3__3d__primitives.md#ga98d8ce37ac733cb9afe6c273c1b304df) functions has type equal to 7. The shape imported from the BREP, IGES, STEP or other CAD file, has type equal to 1.

The possible values of the geometrical objects are listed in the table below:

|  |  |
| --- | --- |
| ID | STRING |
| 0 | COPY |
| 1 | IMPORT |
| 2 | POINT |
| 3 | VECTOR |
| 4 | PLANE |
| 5 | LINE |
| 6 | TORUS |
| 7 | BOX |
| 8 | CYLINDER |
| 9 | CONE |
| 10 | SPHERE |
| 11 | PRISM |
| 12 | REVOLUTION |
| 13 | BOOLEAN |
| 14 | PARTITION |
| 15 | POLYLINE |
| 16 | CIRCLE |
| 17 | SPLINE |
| 18 | ELLIPSE |
| 19 | CIRC_ARC |
| 20 | FILLET |
| 21 | CHAMFER |
| 22 | EDGE |
| 23 | WIRE |
| 24 | FACE |
| 25 | SHELL |
| 26 | SOLID |
| 27 | COMPOUND |
| 28 | SUBSHAPE |
| 29 | PIPE |
| 30 | ARCHIMEDE |
| 31 | FILLING |
| 32 | EXPLODE |
| 33 | GLUED |
| 34 | SKETCHER |
| 35 | CDG |
| 36 | FREE_BOUNDS |
| 37 | GROUP |
| 38 | BLOCK |
| 39 | MARKER |
| 40 | THRUSECTIONS |
| 41 | COMPOUNDFILTER |
| 42 | SHAPES_ON_SHAPE |
| 43 | ELLIPSE_ARC |
| 44 | 3DSKETCHER |
| 45 | FILLET_2D |
| 46 | FILLET_1D |
| 201 | PIPETSHAPE |

Also geompy.py module provides a helper function [ShapeIdToType()](../GEOM/geompy_doc/group__l3__groups.md#gaa9df8679b04d14134ba0a5389e8d6312) that allows converting the geometrical object id value to its string representation.

For example, the output of the following code:

```python
import salome
salome.salome_init()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

box = geompy.MakeBoxDXDYDZ(10,10,10)
type = geompy.ShapeIdToType(box.GetType())
print type
```

will be the "BOX" value.

**GetShapeType function:**

The ShapeType property specifies the geometrical object in terms of its topologic nature.

The possible values are defined in the [GEOM](../GEOM/geompy_doc/namespaceGEOM.md) namespace: { COMPOUND, COMPSOLID, SOLID, SHELL, FACE, WIRE, EDGE, VERTEX, SHAPE }

This type can be retrieved using the **GetShapeType**() function of the **GEOM_Object** interface.

For example:

```python
import salome
salome.salome_init()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

box = geompy.MakeBoxDXDYDZ(10,10,10)
type = box.GetShapeType()
print type == GEOM.SOLID
```

The result is "True".
