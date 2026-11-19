<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l3__blocks__op.html -->

# Blocks Operations geomBuilder Python module » All package methods, grouped by their purpose » Transforming geometrical objects

## Detailed Description

## Function Documentation

### GetPoint()

```python
def GetPoint(self, theShape, theX, theY, theZ, theEpsilon, theName = None)
```

Get a vertex, found in the given shape by its coordinates.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Block or a compound of blocks. |
    | theX,theY,theZ | Coordinates of the sought vertex. |
    | theEpsilon | Maximum allowed distance between the resulting vertex and point with the given coordinates. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found vertex.

[Example](../tui_test_others_page.md#swig_GetPoint)

### GetVertexNearPoint()

```python
def GetVertexNearPoint(self, theShape, thePoint, theName = None)
```

Find a vertex of the given shape, which has minimal distance to the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Any shape. |
    | thePoint | Point, close to the desired vertex. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found vertex.

[Example](../tui_test_others_page.md#swig_GetVertexNearPoint)

### GetEdge()

```python
def GetEdge(self, theShape, thePoint1, thePoint2, theName = None)
```

Get an edge, found in the given shape by two given vertices.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Block or a compound of blocks. |
    | thePoint1,thePoint2 | Points, close to the ends of the desired edge. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found edge.

[Example](../tui_test_others_page.md#swig_GetEdge)

### GetEdgeNearPoint()

```python
def GetEdgeNearPoint(self, theShape, thePoint, theName = None)
```

Find an edge of the given shape, which has minimal distance to the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Block or a compound of blocks. |
    | thePoint | Point, close to the desired edge. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found edge.

[Example](../tui_test_others_page.md#swig_GetEdgeNearPoint)

### GetFaceByPoints()

```python
def GetFaceByPoints(self, theShape, thePoint1, thePoint2, thePoint3, thePoint4, theName = None)
```

Returns a face, found in the given shape by four given corner vertices.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Block or a compound of blocks. |
    | thePoint1,thePoint2,thePoint3,thePoint4 | Points, close to the corners of the desired face. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found face.

Example

### GetFaceByEdges()

```python
def GetFaceByEdges(self, theShape, theEdge1, theEdge2, theName = None)
```

Get a face of block, found in the given shape by two given edges.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Block or a compound of blocks. |
    | theEdge1,theEdge2 | Edges, close to the edges of the desired face. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found face.

Example

### GetOppositeFace()

```python
def GetOppositeFace(self, theBlock, theFace, theName = None)
```

Find a face, opposite to the given one in the given block.

Parameters
:   |  |  |
    | --- | --- |
    | theBlock | Must be a hexahedral solid. |
    | theFace | Face of *theBlock*, opposite to the desired face. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found face.

[Example](../tui_test_spanner_page.md#swig_GetOppositeFace)

### GetFaceNearPoint()

```python
def GetFaceNearPoint(self, theShape, thePoint, theName = None)
```

Find a face of the given shape, which has minimal distance to the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Block or a compound of blocks. |
    | thePoint | Point, close to the desired face. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found face.

[Example](../tui_test_spanner_page.md#swig_GetFaceNearPoint)

### GetFaceByNormale()

```python
def GetFaceByNormale(self, theBlock, theVector, theName = None)
```

Find a face of block, whose outside normale has minimal angle with the given vector.

Parameters
:   |  |  |
    | --- | --- |
    | theBlock | Block or a compound of blocks. |
    | theVector | Vector, close to the normale of the desired face. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found face.

Example

### GetShapesNearPoint()

```python
def GetShapesNearPoint(self, theShape, thePoint, theShapeType, theTolerance = 1e-07, theName = None)
```

Find all sub-shapes of type *theShapeType* of the given shape, which have minimal distance to the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Any shape. |
    | thePoint | Point, close to the desired shape. |
    | theShapeType | Defines what kind of sub-shapes is searched [GEOM::shape_type](namespaceGEOM.md#a82a00e336c65dad4cc04b65563b26eb5) |
    | theTolerance | The tolerance for distances comparison. All shapes with distances to the given point in interval [minimal_distance, minimal_distance + theTolerance] will be gathered. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New GEOM_Object, containing a group of all found shapes.

[Example](../tui_test_others_page.md#swig_GetShapesNearPoint)

### MakeBlockExplode()

```python
def MakeBlockExplode(self, theCompound, theMinNbFaces, theMaxNbFaces, theName = None)
```

Get all the blocks, contained in the given compound.

Parameters
:   |  |  |
    | --- | --- |
    | theCompound | The compound to explode. |
    | theMinNbFaces | If solid has lower number of faces, it is not a block. |
    | theMaxNbFaces | If solid has higher number of faces, it is not a block. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Note
:   If theMaxNbFaces = 0, the maximum number of faces is not restricted.

Returns
:   List of [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the retrieved blocks.

[Example 1](../tui_blocks_operations_page.md#tui_explode_on_blocks)   
[Example 2](../tui_test_others_page.md#swig_MakeBlockExplode)

### GetBlockNearPoint()

```python
def GetBlockNearPoint(self, theCompound, thePoint, theName = None)
```

Find block, containing the given point inside its volume or on boundary.

Parameters
:   |  |  |
    | --- | --- |
    | theCompound | Compound, to find block in. |
    | thePoint | Point, close to the desired block. If the point lays on boundary between some blocks, we return block with nearest center. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found block.

Example

### GetBlockByParts()

```python
def GetBlockByParts(self, theCompound, theParts, theName = None)
```

Find block, containing all the elements, passed as the parts, or maximum quantity of them.

Parameters
:   |  |  |
    | --- | --- |
    | theCompound | Compound, to find block in. |
    | theParts | List of faces and/or edges and/or vertices to be parts of the found block. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found block.

[Example](../tui_test_others_page.md#swig_GetBlockByParts)

### GetBlocksByParts()

```python
def GetBlocksByParts(self, theCompound, theParts, theName = None)
```

Return all blocks, containing all the elements, passed as the parts.

Parameters
:   |  |  |
    | --- | --- |
    | theCompound | Compound, to find blocks in. |
    | theParts | List of faces and/or edges and/or vertices to be parts of the found blocks. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found blocks.

Example

### MakeMultiTransformation1D()

```python
def MakeMultiTransformation1D(self, Block, DirFace1, DirFace2, NbTimes, theName = None)
```

Multi-transformate block and glue the result.

Transformation is defined so, as to superpose direction faces.

Parameters
:   |  |  |
    | --- | --- |
    | Block | Hexahedral solid to be multi-transformed. |
    | DirFace1 | ID of First direction face. |
    | DirFace2 | ID of Second direction face. |
    | NbTimes | Quantity of transformations to be done. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Note
:   Unique ID of sub-shape can be obtained, using method [GetSubShapeID()](group__l4__access.md#gab8920ca3c07df6afcff7386821a2eccc).

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example](../tui_blocks_operations_page.md#tui_multi_transformation)

### MakeMultiTransformation2D()

```python
def MakeMultiTransformation2D(self, Block, DirFace1U, DirFace2U, NbTimesU, DirFace1V, DirFace2V, NbTimesV, theName = None)
```

Multi-transformate block and glue the result.

Parameters
:   |  |  |
    | --- | --- |
    | Block | Hexahedral solid to be multi-transformed. |
    | DirFace1U,DirFace2U | IDs of Direction faces for the first transformation. |
    | DirFace1V,DirFace2V | IDs of Direction faces for the second transformation. |
    | NbTimesU,NbTimesV | Quantity of transformations to be done. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

[Example](../tui_blocks_operations_page.md#tui_multi_transformation)

### Propagate()

```python
def Propagate(self, theShape, theName = None)
```

Build all possible propagation groups.

Propagation group is a set of all edges, opposite to one (main) edge of this group directly or through other opposite edges. Notion of Opposite Edge make sense only on quadrangle face.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to build propagation groups on. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), each of them is a propagation group.

[Example](../tui_test_others_page.md#swig_Propagate)
