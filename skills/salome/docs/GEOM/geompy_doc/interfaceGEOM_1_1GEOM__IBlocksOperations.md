<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__IBlocksOperations.html -->

# GEOM_IBlocksOperations Interface Reference

Interface for Blocks construction Face from points or edges, Block from faces, Blocks multi-translation and multi-rotation.
[More...](interfaceGEOM_1_1GEOM__IBlocksOperations.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for Blocks construction Face from points or edges, Block from faces, Blocks multi-translation and multi-rotation.

## Member Typedef Documentation

### BCErrors

```python
typedef sequence< BCError > BCErrors
```

Sequence of all Blocks Compound defects.

## Member Enumeration Documentation

### BCErrorType

```python
enum BCErrorType
```

Enumeration of Blocks Compound defects.

| Enumerator | |
| --- | --- |
| NOT_BLOCK |  |
| EXTRA_EDGE |  |
| INVALID_CONNECTION |  |
| NOT_CONNECTED |  |
| NOT_GLUED |  |

## Member Function Documentation

### MakeQuad()

```python
GEOM_Object MakeQuad(in GEOM_Object theEdge1, in GEOM_Object theEdge2, in GEOM_Object theEdge3, in GEOM_Object theEdge4)
```

Create a quadrangle face from four edges. Order of Edges is not important. It is not necessary that edges share the same vertex.

Parameters
:   |  |  |
    | --- | --- |
    | theEdge1,theEdge2,theEdge3,theEdge4 | Edges for the face bound. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

### MakeQuad2Edges()

```python
GEOM_Object MakeQuad2Edges(in GEOM_Object theEdge1, in GEOM_Object theEdge2)
```

Create a quadrangle face on two edges.

The missing edges will be built by creating the shortest ones.

Parameters
:   |  |  |
    | --- | --- |
    | theEdge1,theEdge2 | Two opposite edges for the face. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

### MakeQuad4Vertices()

```python
GEOM_Object MakeQuad4Vertices(in GEOM_Object thePnt1, in GEOM_Object thePnt2, in GEOM_Object thePnt3, in GEOM_Object thePnt4)
```

Create a quadrangle face with specified corners.

The missing edges will be built by creating the shortest ones.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1,thePnt2,thePnt3,thePnt4 | Corner vertices for the face. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

### MakeHexa()

```python
GEOM_Object MakeHexa(in GEOM_Object theFace1, in GEOM_Object theFace2, in GEOM_Object theFace3, in GEOM_Object theFace4, in GEOM_Object theFace5, in GEOM_Object theFace6)
```

Create a hexahedral solid, bounded by the six given faces. Order of faces is not important.

It is not necessary that Faces share the same edge.

Parameters
:   |  |  |
    | --- | --- |
    | theFace1,theFace2,theFace3,theFace4,theFace5,theFace6 | Faces for the hexahedral solid. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created solid.

### MakeHexa2Faces()

```python
GEOM_Object MakeHexa2Faces(in GEOM_Object theFace1, in GEOM_Object theFace2)
```

Create a hexahedral solid between two given faces.

The missing faces will be built by creating the smallest ones.

Parameters
:   |  |  |
    | --- | --- |
    | theFace1,theFace2 | Two opposite faces for the hexahedral solid. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created solid.

### GetPoint()

```python
GEOM_Object GetPoint(in GEOM_Object theShape, in double theX, in double theY, in double theZ, in double theEpsilon)
```

Get a vertex, found in the given shape by its coordinates.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Block or a compound of blocks. |
    | theX,theY,theZ | Coordinates of the sought vertex. |
    | theEpsilon | Maximum allowed distance between the resulting vertex and point with the given coordinates. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found vertex.

### GetVertexNearPoint()

```python
GEOM_Object GetVertexNearPoint(in GEOM_Object theShape, in GEOM_Object thePoint)
```

Find a vertex of the given shape, which has minimal distance to the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Any shape. |
    | thePoint | Point, close to the desired vertex. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found vertex.

### GetEdge()

```python
GEOM_Object GetEdge(in GEOM_Object theShape, in GEOM_Object thePoint1, in GEOM_Object thePoint2)
```

Get an edge, found in the given shape by two given vertices.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Block or a compound of blocks. |
    | thePoint1,thePoint2 | Points, close to the ends of the desired edge. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found edge.

### GetEdgeNearPoint()

```python
GEOM_Object GetEdgeNearPoint(in GEOM_Object theShape, in GEOM_Object thePoint)
```

Find an edge of the given shape, which has minimal distance to the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Block or a compound of blocks. |
    | thePoint | Point, close to the desired edge. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found edge.

### GetFaceByPoints()

```python
GEOM_Object GetFaceByPoints(in GEOM_Object theShape, in GEOM_Object thePoint1, in GEOM_Object thePoint2, in GEOM_Object thePoint3, in GEOM_Object thePoint4)
```

Returns a face, found in the given shape by four given corner vertices.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Block or a compound of blocks. |
    | thePoint1,thePoint2,thePoint3,thePoint4 | Points, close to the corners of the desired face. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found face.

### GetFaceByEdges()

```python
GEOM_Object GetFaceByEdges(in GEOM_Object theShape, in GEOM_Object theEdge1, in GEOM_Object theEdge2)
```

Get a face of block, found in the given shape by two given edges.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Block or a compound of blocks. |
    | theEdge1,theEdge2 | Edges, close to the edges of the desired face. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found face.

### GetOppositeFace()

```python
GEOM_Object GetOppositeFace(in GEOM_Object theBlock, in GEOM_Object theFace)
```

Find a face, opposite to the given one in the given block.

Parameters
:   |  |  |
    | --- | --- |
    | theBlock | Must be a hexahedral solid. |
    | theFace | Face of *theBlock*, opposite to the desired face. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found face.

### GetFaceNearPoint()

```python
GEOM_Object GetFaceNearPoint(in GEOM_Object theShape, in GEOM_Object thePoint)
```

Find a face of the given shape, which has minimal distance to the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Block or a compound of blocks. |
    | thePoint | Point, close to the desired face. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found face.

### GetFaceByNormale()

```python
GEOM_Object GetFaceByNormale(in GEOM_Object theBlock, in GEOM_Object theVector)
```

Find a face of block, whose outside normale has minimal angle with the given vector.

Parameters
:   |  |  |
    | --- | --- |
    | theBlock | Block or a compound of blocks. |
    | theVector | Vector, close to the normale of the desired face. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found face.

### GetShapesNearPoint()

```python
GEOM_Object GetShapesNearPoint(in GEOM_Object theShape, in GEOM_Object thePoint, in long theShapeType, in double theTolerance)
```

Find all sub-shapes of type *theShapeType* of the given shape, which have minimal distance to the given point.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Any shape. |
    | thePoint | Point, close to the desired shape. |
    | theShapeType | Defines what kind of sub-shapes is searched. |
    | theTolerance | The tolerance for distances comparison. All shapes with distances to the given point in interval [minimal_distance, minimal_distance + theTolerance] will be gathered. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing a group of all found shapes.

### IsCompoundOfBlocks()

```python
boolean IsCompoundOfBlocks(in GEOM_Object theCompound, in long theMinNbFaces, in long theMaxNbFaces, out long theNbBlocks)
```

Check, if the compound contains only specified blocks.

Parameters
:   |  |  |
    | --- | --- |
    | theCompound | The compound to check. |
    | theMinNbFaces | If solid has lower number of faces, it is not a block. |
    | theMaxNbFaces | If solid has higher number of faces, it is not a block. |

Note
:   If theMaxNbFaces = 0, the maximum number of faces is not restricted.

Parameters
:   |  |  |
    | --- | --- |
    | theNbBlocks | Number of specified blocks in theCompound. |

Returns
:   TRUE, if the given compound contains only blocks.

### CheckCompoundOfBlocks()

```python
boolean CheckCompoundOfBlocks(in GEOM_Object theCompound, in double theToleranceC1, out BCErrors theErrors)
```

Check, if the compound of blocks is given.

To be considered as a compound of blocks, the given shape must satisfy the following conditions:

- Each element of the compound should be a Block (6 faces and 12 edges).
- A connection between two Blocks should be an entire quadrangle face or an entire edge.
- The compound should be connexe.
- The glue between two quadrangle faces should be applied.

  Note
  :   Single block is also accepted as a valid compound of blocks.

  Parameters
  :   |  |  |
      | --- | --- |
      | theCompound | The compound to check. |
      | theToleranceC1 | the tolerance to check if two neighbor edges are collinear in the common vertex with this tolerance. Negative value means that C1 criterion is not used (old implementation). |
      | theErrors | Structure, containing discovered errors and incriminated sub-shapes. |

  Returns
  :   TRUE, if the given shape is a compound of blocks.

### PrintBCErrors()

```python
string PrintBCErrors(in GEOM_Object theCompound, in BCErrors theErrors)
```

Convert sequence of Blocks Compound errors, returned by *[CheckCompoundOfBlocks()](interfaceGEOM_1_1GEOM__IBlocksOperations.md#af8764b1f463ea4a7155fb5d784072d30)*, into string.

Parameters
:   |  |  |
    | --- | --- |
    | theCompound | The bad compound. |
    | theErrors | The sequence of *theCompound* errors. |

Returns
:   String, describing all the errors in form, suitable for printing.

### GetNonBlocks()

```python
GEOM_Object GetNonBlocks(in GEOM_Object theShape, in double theToleranceC1, out GEOM_Object theNonQuads)
```

Retrieve all non blocks solids and faces from a shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | The shape to explore. |
    | theToleranceC1 | the tolerance to check if two neighbor edges are collinear in the common vertex with this tolerance. Negative value means that C1 criterion is not used (old implementation). |
    | theNonQuads | Output parameter. Group of all non quadrangular faces. |

Returns
:   Group of all non block solids (= not 6 faces, or with 6 faces, but with the presence of non-quadrangular faces).

### RemoveExtraEdges()

```python
GEOM_Object RemoveExtraEdges(in GEOM_Object theShape, in long theOptimumNbFaces)
```

Remove all seam and degenerated edges from *theShape*.

Unite faces and edges, sharing one surface.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | The compound or single solid to remove irregular edges from. |
    | theOptimumNbFaces | If more than zero, unite faces only for those solids, that have more than theOptimumNbFaces faces. If zero, unite faces always, regardsless their quantity in the solid. If negative, do not unite faces at all. For blocks repairing recommended value is 6. |

Returns
:   Improved shape.

### UnionFaces()

```python
GEOM_Object UnionFaces(in GEOM_Object theShape)
```

Performs union faces of *theShape*.

Unite faces sharing one surface.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | The compound or single solid that contains faces to perform union. |

Returns
:   Improved shape.

### CheckAndImprove()

```python
GEOM_Object CheckAndImprove(in GEOM_Object theCompound)
```

Check, if the given shape is a blocks compound.

Fix all detected errors.

Note
:   Single block can be also fixed by this method.

Parameters
:   |  |  |
    | --- | --- |
    | theCompound | The compound to check and improve. |

Returns
:   Improved compound.

### ExplodeCompoundOfBlocks()

```python
ListOfGO ExplodeCompoundOfBlocks(in GEOM_Object theCompound, in long theMinNbFaces, in long theMaxNbFaces)
```

Get all the blocks, contained in the given compound.

Parameters
:   |  |  |
    | --- | --- |
    | theCompound | The compound to explode. |
    | theMinNbFaces | If solid has lower number of faces, it is not a block. |
    | theMaxNbFaces | If solid has higher number of faces, it is not a block. |

Note
:   If theMaxNbFaces = 0, the maximum number of faces is not restricted.

Returns
:   List of [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the retrieved blocks.

### GetBlockNearPoint()

```python
GEOM_Object GetBlockNearPoint(in GEOM_Object theCompound, in GEOM_Object thePoint)
```

Find block, containing the given point inside its volume or on boundary.

Parameters
:   |  |  |
    | --- | --- |
    | theCompound | Compound, to find block in. |
    | thePoint | Point, close to the desired block. If the point lays on boundary between some blocks, we return block with nearest center. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found block.

### GetBlockByParts()

```python
GEOM_Object GetBlockByParts(in GEOM_Object theCompound, in ListOfGO theParts)
```

Find block, containing all the elements, passed as the parts, or maximum quantity of them.

Parameters
:   |  |  |
    | --- | --- |
    | theCompound | Compound, to find block in. |
    | theParts | List of faces and/or edges and/or vertices to be parts of the found block. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found block.

### GetBlocksByParts()

```python
ListOfGO GetBlocksByParts(in GEOM_Object theCompound, in ListOfGO theParts)
```

Return all blocks, containing all the elements, passed as the parts.

Parameters
:   |  |  |
    | --- | --- |
    | theCompound | Compound, to find blocks in. |
    | theParts | List of faces and/or edges and/or vertices to be parts of the found blocks. |

Returns
:   List of [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the found blocks.

### MakeMultiTransformation1D()

```python
GEOM_Object MakeMultiTransformation1D(in GEOM_Object theBlock, in long theDirFace1, in long theDirFace2, in long theNbTimes)
```

Multi-transformate block and glue the result.

Transformation is defined so, as to superpose theDirFace1 with theDirFace2.

Parameters
:   |  |  |
    | --- | --- |
    | theBlock | Hexahedral solid to be multi-transformed. |
    | theDirFace1 | First direction face global index. |
    | theDirFace2 | Second direction face global index. |
    | theNbTimes | Quantity of transformations to be done. |

Note
:   Global index of sub-shape can be obtained, using method *[GEOM_IShapesOperations.GetSubShapeIndex()](interfaceGEOM_1_1GEOM__IShapesOperations.md#a2f6aa8ddf89ba64785607a7eb137ec2b)*.

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeMultiTransformation2D()

```python
GEOM_Object MakeMultiTransformation2D(in GEOM_Object theBlock, in long theDirFace1U, in long theDirFace2U, in long theNbTimesU, in long theDirFace1V, in long theDirFace2V, in long theNbTimesV)
```

Multi-transformate block and glue the result.

Parameters
:   |  |  |
    | --- | --- |
    | theBlock | Hexahedral solid to be multi-transformed. |
    | theDirFace1U,theDirFace2U | Direction faces for the first transformation. |
    | theDirFace1V,theDirFace2V | Direction faces for the second transformation. |
    | theNbTimesU,theNbTimesV | Quantity of transformations to be done. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### Propagate()

```python
ListOfGO Propagate(in GEOM_Object theShape)
```

Build all possible propagation groups.

Propagation group is a set of all edges, opposite to one (main) edge of this group directly or through other opposite edges. Notion of Opposite Edge make sense only on quadrangle face.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to build propagation groups on. |

Returns
:   List of [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), each of them is a propagation group.

### IsDone()

```python
boolean IsDone() inherited
```

To know, if the operation was successfully performed.

### SetErrorCode()

```python
void SetErrorCode(in string theErrorID) inherited
```

Set the operation error code.

Parameters
:   |  |  |
    | --- | --- |
    | theErrorID | is a string describing the error occurred |

Note
:   This method is supposed to be used only by interfaces inheriting from IOperations.

### GetErrorCode()

```python
string GetErrorCode() inherited
```

Get the operation error code.

### StartOperation()

```python
void StartOperation() inherited
```

Opens a new transaction.

### FinishOperation()

```python
void FinishOperation() inherited
```

Closes the previously opened transaction.

### AbortOperation()

```python
void AbortOperation() inherited
```

Aborts the previously opened transaction.
