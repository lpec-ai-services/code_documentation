<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__IKindOfShape.html -->

# GEOM_IKindOfShape Interface Reference

Interface for shape_kind enumeration.
[More...](interfaceGEOM_1_1GEOM__IKindOfShape.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for shape_kind enumeration.

## Member Enumeration Documentation

### shape_kind

```python
enum shape_kind
```

| Enumerator | |
| --- | --- |
| NO_SHAPE |  |
| COMPOUND |  |
| COMPSOLID |  |
| SHELL |  |
| WIRE |  |
| SPHERE | full sphere |
| CYLINDER | cylinder |
| BOX | box with faces, parallel to global coordinate planes |
| ROTATED_BOX | other box |
| TORUS | full torus |
| CONE | cone |
| POLYHEDRON | solid, bounded by polygons |
| SOLID | other solid |
| SPHERE2D | spherical face (closed) |
| CYLINDER2D | cylindrical face with defined height |
| TORUS2D | toroidal face (closed) |
| CONE2D | conical face with defined height |
| DISK_CIRCLE | planar, bounded by circle |
| DISK_ELLIPSE | planar, bounded by ellipse |
| POLYGON | planar, bounded by segments |
| PLANE | infinite planar |
| PLANAR | other planar |
| FACE | other face |
| CIRCLE | full circle |
| ARC_CIRCLE | arc of circle |
| ELLIPSE | full ellipse |
| ARC_ELLIPSE | arc of ellipse |
| LINE | infinite segment |
| SEGMENT | segment |
| CRV_BSPLINE | B-Spline curve |
| CRV_BEZIER | Bezier curve |
| HYPERBOLA | hyperbola |
| PARABOLA | parabola |
| EDGE | other edge |
| VERTEX |  |
| LCS |  |
| ADVANCED | all advanced shapes (temporary implementation) |
