<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l3__local.html -->

# Local Operations (Fillet, Chamfer and other Features) geomBuilder Python module » All package methods, grouped by their purpose » Transforming geometrical objects

## Detailed Description

## Function Documentation

### MakeFilletAll()

```python
def MakeFilletAll(self, theShape, theR, theName = None)
```

Perform a fillet on all edges of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform fillet on. |
    | theR | Fillet radius. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example 1](../tui_transformation_operations_page.md#tui_fillet)   
[Example 2](../tui_test_others_page.md#swig_MakeFilletAll)

### MakeFillet()

```python
def MakeFillet(self, theShape, theR, theShapeType, theListShapes, theName = None)
```

Perform a fillet on the specified edges/faces of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform fillet on. |
    | theR | Fillet radius. |
    | theShapeType | Type of shapes in *theListShapes* (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theListShapes | Global indices of edges/faces to perform fillet on. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Note
:   Global index of sub-shape can be obtained, using method [GetSubShapeID()](group__l4__access.md#gab8920ca3c07df6afcff7386821a2eccc).

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example](../tui_transformation_operations_page.md#tui_fillet)

### MakeFilletR1R2()

```python
def MakeFilletR1R2(self, theShape, theR1, theR2, theShapeType, theListShapes, theName = None)
```

The same that [MakeFillet()](group__l3__local.md#ga999b3b12bdaa5aff05803179afdcd595) but with two Fillet Radius R1 and R2.

### MakeFillet1D()

```python
def MakeFillet1D(self, theShape, theR, theListOfVertexes, doIgnoreSecantVertices = True, theName = None)
```

Perform a fillet on the specified edges of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Wire Shape to perform fillet on. |
    | theR | Fillet radius. |
    | theListOfVertexes | Global indices of vertexes to perform fillet on. |

Note
:   Global index of sub-shape can be obtained, using method [GetSubShapeID()](group__l4__access.md#gab8920ca3c07df6afcff7386821a2eccc)
:   The list of vertices could be empty, in this case fillet will done done at all vertices in wire

Parameters
:   |  |  |
    | --- | --- |
    | doIgnoreSecantVertices | If FALSE, fillet radius is always limited by the length of the edges, nearest to the fillet vertex. But sometimes the next edge is C1 continuous with the one, nearest to the fillet point, and such two (or more) edges can be united to allow bigger radius. Set this flag to TRUE to allow collinear edges union, thus ignoring the secant vertex (vertices). |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example](../tui_transformation_operations_page.md#tui_fillet2d)

### MakeFillet2D()

```python
def MakeFillet2D(self, theShape, theR, theListOfVertexes, theName = None)
```

Perform a fillet at the specified vertices of the given face/shell.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Face or Shell shape to perform fillet on. |
    | theR | Fillet radius. |
    | theListOfVertexes | Global indices of vertexes to perform fillet on. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Note
:   Global index of sub-shape can be obtained, using method [GetSubShapeID()](group__l4__access.md#gab8920ca3c07df6afcff7386821a2eccc).

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example](../tui_transformation_operations_page.md#tui_fillet2d)

### MakeChamferAll()

```python
def MakeChamferAll(self, theShape, theD, theName = None)
```

Perform a symmetric chamfer on all edges of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform chamfer on. |
    | theD | Chamfer size along each face. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example 1](../tui_transformation_operations_page.md#tui_chamfer)   
[Example 2](../tui_test_others_page.md#swig_MakeChamferAll)

### MakeChamferEdge()

```python
def MakeChamferEdge(self, theShape, theD1, theD2, theFace1, theFace2, theName = None)
```

Perform a chamfer on edges, common to the specified faces, with distance D1 on the Face1.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform chamfer on. |
    | theD1 | Chamfer size along *theFace1*. |
    | theD2 | Chamfer size along *theFace2*. |
    | theFace1,theFace2 | Global indices of two faces of *theShape*. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Note
:   Global index of sub-shape can be obtained, using method [GetSubShapeID()](group__l4__access.md#gab8920ca3c07df6afcff7386821a2eccc).

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example](../tui_transformation_operations_page.md#tui_chamfer)

### MakeChamferEdgeAD()

```python
def MakeChamferEdgeAD(self, theShape, theD, theAngle, theFace1, theFace2, theName = None)
```

Perform a chamfer on edges.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform chamfer on. |
    | theD | Chamfer length |
    | theAngle | Angle of chamfer (angle in radians or a name of variable which defines angle in degrees) |
    | theFace1,theFace2 | Global indices of two faces of *theShape*. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Note
:   Global index of sub-shape can be obtained, using method [GetSubShapeID()](group__l4__access.md#gab8920ca3c07df6afcff7386821a2eccc).

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeChamferFaces()

```python
def MakeChamferFaces(self, theShape, theD1, theD2, theFaces, theName = None)
```

Perform a chamfer on all edges of the specified faces, with distance D1 on the first specified face (if several for one edge)

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform chamfer on. |
    | theD1 | Chamfer size along face from *theFaces*. If both faces, connected to the edge, are in *theFaces*, *theD1* will be get along face, which is nearer to *theFaces* beginning. |
    | theD2 | Chamfer size along another of two faces, connected to the edge. |
    | theFaces | Sequence of global indices of faces of *theShape*. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Note
:   Global index of sub-shape can be obtained, using method [GetSubShapeID()](group__l4__access.md#gab8920ca3c07df6afcff7386821a2eccc).

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example](../tui_transformation_operations_page.md#tui_chamfer)

### MakeChamferFacesAD()

```python
def MakeChamferFacesAD(self, theShape, theD, theAngle, theFaces, theName = None)
```

The Same that [MakeChamferFaces()](group__l3__local.md#ga677669fcf2eacc8f09992b88ab423741) but with params theD is chamfer length and theAngle is Angle of chamfer (angle in radians or a name of variable which defines angle in degrees)

[Example](../tui_test_all_page.md#swig_FilletChamfer)

### MakeChamferEdges()

```python
def MakeChamferEdges(self, theShape, theD1, theD2, theEdges, theName = None)
```

Perform a chamfer on edges, with distance D1 on the first specified face (if several for one edge)

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform chamfer on. |
    | theD1,theD2 | Chamfer size |
    | theEdges | Sequence of edges of *theShape*. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example](../tui_test_all_page.md#swig_FilletChamfer)

### MakeChamferEdgesAD()

```python
def MakeChamferEdgesAD(self, theShape, theD, theAngle, theEdges, theName = None)
```

The Same that [MakeChamferEdges()](group__l3__local.md#gaaa95396495623bae374ae970f2d04536) but with params theD is chamfer length and theAngle is Angle of chamfer (angle in radians or a name of variable which defines angle in degrees)

### MakeChamfer()

```python
def MakeChamfer(self, aShape, d1, d2, aShapeType, ListShape, theName = None)
```

See also
:   [MakeChamferEdge()](group__l3__local.md#ga604693e7e793578cdceff823e7b1e010), [MakeChamferFaces()](group__l3__local.md#ga677669fcf2eacc8f09992b88ab423741)

[Example](../tui_test_others_page.md#swig_MakeChamfer)

### MakeExtrudedCut()

```python
def MakeExtrudedCut(self, theInit, theBase, theH, theAngle, theInvert = False, theName = None)
```

Remove material from a solid by extrusion of the base shape on the given distance.

Parameters
:   |  |  |
    | --- | --- |
    | theInit | Shape to remove material from. It must be a solid or a compound made of a single solid. |
    | theBase | Closed edge or wire defining the base shape to be extruded. |
    | theH | Prism dimension along the normal to theBase |
    | theAngle | Draft angle in degrees. |
    | theInvert | If true material changes the direction |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the initial shape with removed material

[Example](../tui_complex_objs_page.md#tui_creation_prism)

### MakeExtrudedBoss()

```python
def MakeExtrudedBoss(self, theInit, theBase, theH, theAngle, theInvert = False, theName = None)
```

Add material to a solid by extrusion of the base shape on the given distance.

Parameters
:   |  |  |
    | --- | --- |
    | theInit | Shape to add material to. It must be a solid or a compound made of a single solid. |
    | theBase | Closed edge or wire defining the base shape to be extruded. |
    | theH | Prism dimension along the normal to theBase |
    | theAngle | Draft angle in degrees. |
    | theInvert | If true material changes the direction |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the initial shape with added material

[Example](../tui_complex_objs_page.md#tui_creation_prism)
