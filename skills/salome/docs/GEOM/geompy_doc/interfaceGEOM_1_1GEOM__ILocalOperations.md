<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__ILocalOperations.html -->

# GEOM_ILocalOperations Interface Reference

Interface for fillet and chamfer creation.
[More...](interfaceGEOM_1_1GEOM__ILocalOperations.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for fillet and chamfer creation.

## Member Function Documentation

### MakeFilletAll()

```python
GEOM_Object MakeFilletAll(in GEOM_Object theShape, in double theR)
```

Perform a fillet on all edges of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform fillet on. |
    | theR | Fillet radius. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeFilletEdges()

```python
GEOM_Object MakeFilletEdges(in GEOM_Object theShape, in double theR, in ListOfLong theEdges)
```

Perform a fillet on the specified edges of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform fillet on. |
    | theR | Fillet radius. |
    | theEdges | Global indices of edges to perform fillet on. |

Note
:   Global index of sub-shape can be obtained, using method *[GEOM_IShapesOperations.GetSubShapeIndex()](interfaceGEOM_1_1GEOM__IShapesOperations.md#a2f6aa8ddf89ba64785607a7eb137ec2b)*.

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeFilletEdgesR1R2()

```python
GEOM_Object MakeFilletEdgesR1R2(in GEOM_Object theShape, in double theR1, in double theR2, in ListOfLong theEdges)
```

### MakeFilletFaces()

```python
GEOM_Object MakeFilletFaces(in GEOM_Object theShape, in double theR, in ListOfLong theFaces)
```

Perform a fillet on all edges of the specified faces of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform fillet on. |
    | theR | Fillet radius. |
    | theFaces | Global indices of faces to perform fillet on. |

Note
:   Global index of sub-shape can be obtained, using method *[GEOM_IShapesOperations.GetSubShapeIndex()](interfaceGEOM_1_1GEOM__IShapesOperations.md#a2f6aa8ddf89ba64785607a7eb137ec2b)*.

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeFilletFacesR1R2()

```python
GEOM_Object MakeFilletFacesR1R2(in GEOM_Object theShape, in double theR1, in double theR2, in ListOfLong theFaces)
```

### MakeFillet2D()

```python
GEOM_Object MakeFillet2D(in GEOM_Object theShape, in double theR, in ListOfLong theVertexes)
```

Perform a fillet on a face or a shell at the specified vertexes.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform fillet on. |
    | theR | Fillet radius. |
    | theVertexes | Global indices of vertexes to perform fillet on. |

Note
:   Global index of sub-shape can be obtained, using method *[GEOM_IShapesOperations.GetSubShapeIndex()](interfaceGEOM_1_1GEOM__IShapesOperations.md#a2f6aa8ddf89ba64785607a7eb137ec2b)*.

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeFillet1D()

```python
GEOM_Object MakeFillet1D(in GEOM_Object theShape, in double theR, in ListOfLong theVertexes, in boolean doIgnoreSecantVertices)
```

Perform a fillet on edges of the specified vertexes of the given wire.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform fillet on. |
    | theR | Fillet radius. |
    | theVertexes | Global indices of vertexes to perform fillet on. |

Note
:   Global index of sub-shape can be obtained, using method *[GEOM_IShapesOperations.GetSubShapeIndex()](interfaceGEOM_1_1GEOM__IShapesOperations.md#a2f6aa8ddf89ba64785607a7eb137ec2b)*.
:   The list of vertices could be empty, in this case fillet fill be done at all vertices in given wire

Parameters
:   |  |  |
    | --- | --- |
    | doIgnoreSecantVertices | If FALSE, fillet radius is always limited by the length of the edges, nearest to the fillet vertex. But sometimes the next edge is C1 continuous with the one, nearest to the fillet point, and such two (or more) edges can be united to allow bigger radius. Set this flag to TRUE to allow collinear edges union, thus ignoring the secant vertex (vertices). |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeChamferAll()

```python
GEOM_Object MakeChamferAll(in GEOM_Object theShape, in double theD)
```

Perform a symmetric chamfer on all edges of the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform chamfer on. |
    | theD | Chamfer size along each face. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeChamferEdge()

```python
GEOM_Object MakeChamferEdge(in GEOM_Object theShape, in double theD1, in double theD2, in long theFace1, in long theFace2)
```

Perform a chamfer on edges, common to the specified faces. with distance D1 on the Face1.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform chamfer on. |
    | theD1 | Chamfer size along *theFace1*. |
    | theD2 | Chamfer size along *theFace2*. |
    | theFace1,theFace2 | Global indices of two faces of *theShape*. |

Note
:   Global index of sub-shape can be obtained, using method *[GEOM_IShapesOperations.GetSubShapeIndex()](interfaceGEOM_1_1GEOM__IShapesOperations.md#a2f6aa8ddf89ba64785607a7eb137ec2b)*.

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeChamferEdgeAD()

```python
GEOM_Object MakeChamferEdgeAD(in GEOM_Object theShape, in double theD, in double theAngle, in long theFace1, in long theFace2)
```

The Same but with params theD = Chamfer Length and theAngle = Chamfer Angle (Angle in radians)

### MakeChamferFaces()

```python
GEOM_Object MakeChamferFaces(in GEOM_Object theShape, in double theD1, in double theD2, in ListOfLong theFaces)
```

Perform a chamfer on all edges of the specified faces. with distance D1 on the first specified face (if several for one edge)

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform chamfer on. |
    | theD1 | Chamfer size along face from *theFaces*. If both faces, connected to the edge, are in *theFaces*, *theD1* will be get along face, which is nearer to *theFaces* beginning. |
    | theD2 | Chamfer size along another of two faces, connected to the edge. |
    | theFaces | Sequence of global indices of faces of *theShape*. |

Note
:   Global index of sub-shape can be obtained, using method *[GEOM_IShapesOperations.GetSubShapeIndex()](interfaceGEOM_1_1GEOM__IShapesOperations.md#a2f6aa8ddf89ba64785607a7eb137ec2b)*.

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeChamferFacesAD()

```python
GEOM_Object MakeChamferFacesAD(in GEOM_Object theShape, in double theD, in double theAngle, in ListOfLong theFaces)
```

The Same but with params theD = Chamfer Length and theAngle = Chamfer Angle (Angle in radians)

### MakeChamferEdges()

```python
GEOM_Object MakeChamferEdges(in GEOM_Object theShape, in double theD1, in double theD2, in ListOfLong theEdges)
```

Perform a chamfer on edges, with distance D1 on the first specified face (if several for one edge)

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape, to perform chamfer on. |
    | theD1,theD2 | Chamfer size |
    | theEdges | Sequence of edges of *theShape*. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the result shape.

### MakeChamferEdgesAD()

```python
GEOM_Object MakeChamferEdgesAD(in GEOM_Object theShape, in double theD, in double theAngle, in ListOfLong theEdges)
```

The Same but with params theD = Chamfer Length and theAngle = Chamfer Angle (Angle in radians)

### MakeArchimede()

```python
GEOM_Object MakeArchimede(in GEOM_Object theShape, in double theWeight, in double theWaterDensity, in double theMeshDeflection)
```

Perform an Archimde operation on the given shape with given parameters. The object presenting the resulting face is returned.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be put in water. |
    | theWeight | Weight og the shape. |
    | theWaterDensity | Density of the water. |
    | theMeshDeflection | Deflection od the mesh, using to compute the section. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing a section of *theShape* by a plane, corresponding to water level.

### GetSubShapeIndex()

```python
long GetSubShapeIndex(in GEOM_Object theShape, in GEOM_Object theSubShape)
```

Duplicates *[GEOM_IShapesOperations.GetSubShapeIndex()](interfaceGEOM_1_1GEOM__IShapesOperations.md#a2f6aa8ddf89ba64785607a7eb137ec2b)*.

Present here only for compatibility.

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
