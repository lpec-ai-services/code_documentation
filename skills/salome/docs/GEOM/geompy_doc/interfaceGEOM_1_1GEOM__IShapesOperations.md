<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__IShapesOperations.html -->

# GEOM_IShapesOperations Interface Reference

Interface for Shapes creation:
[More...](interfaceGEOM_1_1GEOM__IShapesOperations.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for Shapes creation:

Edge from two points, Wire from edges, Face from wire, Shell from faces, Solid from shells, Compound from shapes

## Member Typedef Documentation

### ExtractionStats

```python
typedef sequence< ExtractionStat > ExtractionStats
```

## Member Enumeration Documentation

### ExtractionStatType

```python
enum ExtractionStatType
```

This enumeration represents an extraction statistics type.

It is used in the interface [GEOM_IShapesOperations::MakeExtraction](interfaceGEOM_1_1GEOM__IShapesOperations.md#adc26655972eb5aaedfc742e56fc470ff).

| Enumerator | |
| --- | --- |
| EST_Removed | Removed sub-shapes. |
| EST_Modified | Modified sub-shapes. |
| EST_Added | Newly created sub-shapes. |

## Member Function Documentation

### MakeEdge()

```python
GEOM_Object MakeEdge(in GEOM_Object thePnt1, in GEOM_Object thePnt2)
```

Create a linear edge with specified ends.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1 | Point for the first end of edge. |
    | thePnt2 | Point for the second end of edge. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created edge.

### MakeEdgeOnCurveByLength()

```python
GEOM_Object MakeEdgeOnCurveByLength(in GEOM_Object theRefCurve, in double theLength, in GEOM_Object theStartPoint)
```

Create an edge on another edge, corresponding to the given length on the given edge.

Parameters
:   |  |  |
    | --- | --- |
    | theRefCurve | The referenced edge. |
    | theLength | Length on the referenced edge. It can be negative for extrapolation on base curve. |
    | theStartPoint | Any vertex close to one of edge's ends to select start point among them. If NULL, fist vertex is used. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created edge.

### MakeEdgeWire()

```python
GEOM_Object MakeEdgeWire(in GEOM_Object theWire, in double theLinearTolerance, in double theAngularTolerance)
```

Create an edge from specified wire.

Parameters
:   |  |  |
    | --- | --- |
    | theWire | source Wire. |
    | theLinearTolerance | linear tolerance value |
    | theAngularTolerance | angular tolerance value |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created edge.

### MakeWire()

```python
GEOM_Object MakeWire(in ListOfGO theEdgesAndWires, in double theTolerance, in wire_build_mode theMode)
```

Create a wire from the set of edges and wires.

Parameters
:   |  |  |
    | --- | --- |
    | theEdgesAndWires | List of edge and/or wires. |
    | theTolerance | Maximum distance between vertices, that will be merged. Values less than 1e-07 are equivalent to 1e-07 (Precision::Confusion()). |
    | theMode | Mode of gaps filling. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created wire.

### MakeFace()

```python
GEOM_Object MakeFace(in GEOM_Object theWire, in boolean isPlanarWanted)
```

Create a face on the given wire.

Parameters
:   |  |  |
    | --- | --- |
    | theWire | closed Wire or Edge to build the face on. |
    | isPlanarWanted | If TRUE, only planar face will be built. If impossible, NULL object will be returned. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

### MakeFaceWires()

```python
GEOM_Object MakeFaceWires(in ListOfGO theWires, in boolean isPlanarWanted)
```

Create a face on the given wires set.

Parameters
:   |  |  |
    | --- | --- |
    | theWires | List of closed wires or edges to build the face on. |
    | isPlanarWanted | If TRUE, only planar face will be built. If impossible, NULL object will be returned. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

### MakeFaceFromSurface()

```python
GEOM_Object MakeFaceFromSurface(in GEOM_Object theFace, in GEOM_Object theWire)
```

Create a face based on surface of theFace limited by theWire.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | the face whose surface is used to create a new face. |
    | theWire | closed Wire build the face. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

### MakeWrappedFace()

```python
GEOM_Object MakeWrappedFace(in ListOfGO theEdges, in ListOfGO theVertices, in double theTolerance)
```

Create a bounded face with list of edges and list of vertices.

The list of edges defines the boundary of the desired face and all vertices should lie on it. The result can be a COMPOUND shape with multiple faces, if the underlying surface is somehow split within the given boundary, e.g. by the seam edge of a sphere.

Parameters
:   |  |  |
    | --- | --- |
    | theEdges | list of Edges defining the boundary of the result face (must be closed but not nesessarily belong to the same plane) . |
    | theVertices | list of vertices through which the result face must pass (within the given tolerance). |
    | theTolerance | tolerance. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created shape (FACE or COMPOUND).

### MakeFaceWithConstraints()

```python
GEOM_Object MakeFaceWithConstraints(in ListOfGO theConstraints)
```

Create a face from a set of edges with the given constraints.

Parameters
:   |  |  |
    | --- | --- |
    | theConstraints | List of edges and constraint faces (as a sequence of a Edge + Face couples):  - edges should form a closed wire; - for each edge, constraint face is optional: if a constraint face is missing for some edge, this means that there no constraint associated with this edge. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

### MakeShell()

```python
GEOM_Object MakeShell(in ListOfGO theFacesAndShells)
```

Create a shell from the set of faces and shells.

Parameters
:   |  |  |
    | --- | --- |
    | theFacesAndShells | List of faces and/or shells. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created shell.

### MakeSolidShell()

```python
GEOM_Object MakeSolidShell(in GEOM_Object theShell)
```

Create a solid, bounded by the given shell.

Parameters
:   |  |  |
    | --- | --- |
    | theShell | Bounding shell. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created solid.

### MakeSolidShells()

```python
GEOM_Object MakeSolidShells(in ListOfGO theShells)
```

Create a solid, bounded by the given shells.

Parameters
:   |  |  |
    | --- | --- |
    | theShells | Bounding shells. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created solid.

### MakeCompound()

```python
GEOM_Object MakeCompound(in ListOfGO theShapes)
```

Create a compound of the given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | List of shapes to put in compound. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created compound.

### MakeSolidFromConnectedFaces()

```python
GEOM_Object MakeSolidFromConnectedFaces(in ListOfGO theFacesOrShells, in boolean isIntersect)
```

Make a solid (or solids) from connected set of faces and/or shells.

Parameters
:   |  |  |
    | --- | --- |
    | theFacesOrShells | List of faces and/or shells. |
    | isIntersect | If TRUE, forces performing intersections between arguments. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created solid (or compound of solids).

### MakeGlueFaces()

```python
GEOM_Object MakeGlueFaces(in ListOfGO theShapes, in double theTolerance, in boolean doKeepNonSolids)
```

Replace coincident faces in *theShapes* by one face.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Initial shapes. |
    | theTolerance | Maximum distance between faces, which can be considered as coincident. |
    | doKeepNonSolids | If FALSE, only solids will present in the result, otherwise all initial shapes. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) containing copies of theShapes without coincident faces.

### GetGlueFaces()

```python
ListOfGO GetGlueFaces(in ListOfGO theShapes, in double theTolerance)
```

Find coincident faces in theShapes for possible gluing.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Initial shapes. |
    | theTolerance | Maximum distance between faces, which can be considered as coincident. |

Returns
:   ListOfGO

### MakeGlueFacesByList()

```python
GEOM_Object MakeGlueFacesByList(in ListOfGO theShapes, in double theTolerance, in ListOfGO theFaces, in boolean doKeepNonSolids, in boolean doGlueAllEdges)
```

Replace coincident faces in *theShapes* by one face in compliance with given list of faces.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Initial shapes. |
    | theTolerance | Maximum distance between faces, which can be considered as coincident. |
    | theFaces | List of faces for gluing. |
    | doKeepNonSolids | If FALSE, only solids will present in the result, otherwise all initial shapes. |
    | doGlueAllEdges | If TRUE, all coincident edges of *theShape* will be glued, otherwise only the edges, belonging to *theFaces*. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) containing copies of theShapes without coincident faces.

### MakeGlueEdges()

```python
GEOM_Object MakeGlueEdges(in ListOfGO theShapes, in double theTolerance)
```

Replace coincident edges in *theShapes* by one edge.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Initial shapes. |
    | theTolerance | Maximum distance between edges, which can be considered as coincident. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) containing copies of theShapes without coincident edges.

### GetGlueEdges()

```python
ListOfGO GetGlueEdges(in ListOfGO theShapes, in double theTolerance)
```

Find coincident edges in *theShapes* for possible gluing.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Initial shapes. |
    | theTolerance | Maximum distance between edges, which can be considered as coincident. |

Returns
:   ListOfGO

### MakeGlueEdgesByList()

```python
GEOM_Object MakeGlueEdgesByList(in ListOfGO theShapes, in double theTolerance, in ListOfGO theEdges)
```

Replace coincident edges in *theShapes* by one edge in compliance with given list of edges.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Initial shapes. |
    | theTolerance | Maximum distance between edges, which can be considered as coincident. |
    | theEdges | List of edges for gluing. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) containing copies of theShapes without some edges.

### GetExistingSubObjects()

```python
ListOfGO GetExistingSubObjects(in GEOM_Object theShape, in boolean theGroupsOnly)
```

Get all sub-shapes and groups of *theShape*, that were created already by any other methods.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Any shape. |
    | theGroupsOnly | If this parameter is TRUE, only groups will be returned, else all found sub-shapes and groups. |

Returns
:   List of existing sub-objects of *theShape*.

### MakeExplode()

```python
ListOfGO MakeExplode(in GEOM_Object theShape, in long theShapeType, in boolean isSorted)
```

Deprecated method.

Use [MakeAllSubShapes()](interfaceGEOM_1_1GEOM__IShapesOperations.md#a04096f4ffd7e0f96fb8124cd76453fdb) instead.

### MakeAllSubShapes()

```python
ListOfGO MakeAllSubShapes(in GEOM_Object theShape, in long theShapeType, in boolean isSorted)
```

Explode a shape on sub-shapes of a given type.

If the shape itself has the given type, it is also returned.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be exploded. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | isSorted | If this parameter is TRUE, sub-shapes will be sorted by coordinates of their gravity centers. |

Returns
:   List of sub-shapes of type theShapeType, contained in theShape.

### ExtractSubShapes()

```python
ListOfGO ExtractSubShapes(in GEOM_Object theShape, in long theShapeType, in boolean isSorted)
```

Extract all sub-shapes of the given type from the given shape, excluding the shape itself.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be exploded. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | isSorted | If this parameter is TRUE, sub-shapes will be sorted by coordinates of their gravity centers. |

Returns
:   List of sub-shapes of type theShapeType, contained in theShape.

### SubShapeAllIDs()

```python
ListOfLong SubShapeAllIDs(in GEOM_Object theShape, in long theShapeType, in boolean isSorted)
```

Deprecated method. Use [GetAllSubShapesIDs()](interfaceGEOM_1_1GEOM__IShapesOperations.md#ad2af324aa02b812089c76532aeb7f886) instead.

### GetAllSubShapesIDs()

```python
ListOfLong GetAllSubShapesIDs(in GEOM_Object theShape, in long theShapeType, in boolean isSorted)
```

Explode a shape on sub-shapes of a given type.

Does the same, as MakeAllSubShapes, but returns IDs of sub-shapes, not [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md). It works faster.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be exploded. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | isSorted | If this parameter is TRUE, sub-shapes will be sorted by coordinates of their gravity centers. |

Returns
:   List of IDs of sub-shapes of type theShapeType, contained in theShape.

### GetSubShape()

```python
GEOM_Object GetSubShape(in GEOM_Object theMainShape, in long theID)
```

Get a sub-shape defined by its unique ID inside *theMainShape*.

Parameters
:   |  |  |
    | --- | --- |
    | theMainShape | Main shape. |
    | theID | Unique ID of sub-shape inside *theMainShape*. |

Returns
:   [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), corresponding to found sub-shape.

Note
:   The sub-shape [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) can has ONLY ONE function. Don't try to apply modification operations (without copy) on them.

### MakeSubShapes()

```python
ListOfGO MakeSubShapes(in GEOM_Object theMainShape, in ListOfLong theIndices)
```

Get a set of sub-shapes defined by their unique IDs inside *theMainShape*.

Parameters
:   |  |  |
    | --- | --- |
    | theMainShape | Main shape. |
    | theIndices | List of unique IDs of sub-shapes inside *theMainShape*. |

Returns
:   List of [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), corresponding to found sub-shapes.

Note
:   The sub-shape [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) can has ONLY ONE function. Don't try to apply modification operations (without copy) on them.

### GetSubShapeIndex()

```python
long GetSubShapeIndex(in GEOM_Object theMainShape, in GEOM_Object theSubShape)
```

Get global index of *theSubShape* in *theMainShape*.

Parameters
:   |  |  |
    | --- | --- |
    | theMainShape | Main shape. |
    | theSubShape | Sub-shape of the main shape. |

Returns
:   global index of *theSubShape* in *theMainShape*.

### GetSubShapesIndices()

```python
ListOfLong GetSubShapesIndices(in GEOM_Object theMainShape, in ListOfGO theSubShapes)
```

Get global indices of *theSubShapes* in *theMainShape*.

Parameters
:   |  |  |
    | --- | --- |
    | theMainShape | Main shape. |
    | theSubShapes | List of sub-shapes of the main shape. |

Returns
:   list of global indices of *theSubShapes* in *theMainShape*.

### GetTopologyIndex()

```python
long GetTopologyIndex(in GEOM_Object theMainShape, in GEOM_Object theSubShape)
```

Get index of *theSubShape* in *theMainShape*, unique among sub-shapes of the same type.

Together with method *[GetShapeTypeString()](interfaceGEOM_1_1GEOM__IShapesOperations.md#a50411095a529e15b2dfc33e067b577ec)* it can be used to generate automatic names for sub-shapes, when publishing them in a study.

Parameters
:   |  |  |
    | --- | --- |
    | theMainShape | Main shape. |
    | theSubShape | Sub-shape of the main shape. |

Returns
:   index of *theSubShape* in a list of all sub-shapes of *theMainShape* of the same type.

### GetShapeTypeString()

```python
string GetShapeTypeString(in GEOM_Object theShape)
```

Get name of type of *theShape*.

Use wide type notation, taking into consideration both topology and geometry of the shape. Together with method *[GetTopologyIndex()](interfaceGEOM_1_1GEOM__IShapesOperations.md#a7f78ff81a723d08438e891b2eee3eb2a)* it can be used to generate automatic names for sub-shapes, when publishing them in a study.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | The shape to get a type of. |

Returns
:   String, containing a type name of *theShape*.

### IsSubShapeBelongsTo()

```python
boolean IsSubShapeBelongsTo(in GEOM_Object theSubObject, in long theSubObjectIndex, in GEOM_Object theObject, in long theObjectIndex)
```

Check if the object is a sub-object of another [GEOM](namespaceGEOM.md) object.

Parameters
:   |  |  |
    | --- | --- |
    | theSubObject | Checked sub-object (or its parent object, in case if *theSubObjectIndex* is non-zero). |
    | theSubObjectIndex | When non-zero, specifies a sub-shape index that identifies a sub-object within its parent specified via *theSubObject*. |
    | theObject | An object that is checked for ownership (or its parent object, in case if *theObjectIndex* is non-zero). |
    | theObjectIndex | When non-zero, specifies a sub-shape index that identifies an object within its parent specified via *theObject*. |

Returns
:   TRUE, if the given object contains sub-object.

### NumberOfFaces()

```python
long NumberOfFaces(in GEOM_Object theShape)
```

Count number of faces in the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to count faces in. |

Returns
:   Number of faces in the given shape.

### NumberOfEdges()

```python
long NumberOfEdges(in GEOM_Object theShape)
```

Count number of edges in the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to count edges in. |

Returns
:   Number of edges in theShape.

### NumberOfSubShapes()

```python
long NumberOfSubShapes(in GEOM_Object theShape, in long theShapeType)
```

Count number of sub-shapes of type *theShapeType* in the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to count sub-shapes in. |
    | theShapeType | The type of sub-shapes to count. |

Returns
:   Number of sub-shapes of type *theShapeType* in *theShape*.

### ChangeOrientation()

```python
GEOM_Object ChangeOrientation(in GEOM_Object theShape)
```

Reverses an orientation the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to be reversed. |

Returns
:   The reversed copy of theShape.

### GetFreeFacesIDs()

```python
ListOfLong GetFreeFacesIDs(in GEOM_Object theShape)
```

Retrieve all free faces from the given shape.

Free face is a face, which is not shared between two shells of the shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find free faces in. |

Returns
:   List of IDs of all free faces, contained in theShape.

### GetSharedShapes()

```python
ListOfGO GetSharedShapes(in GEOM_Object theShape1, in GEOM_Object theShape2, in long theShapeType)
```

Get all sub-shapes of theShape1 of the given type, shared with theShape2.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1 | Shape to find sub-shapes in. |
    | theShape2 | Shape to find shared sub-shapes with. |
    | theShapeType | Type of sub-shapes to be retrieved. |

Returns
:   List of sub-shapes of theShape1, shared with theShape2.

### GetSharedShapesMulti()

```python
ListOfGO GetSharedShapesMulti(in ListOfGO theShapes, in long theShapeType, in boolean theMultiShare)
```

Get sub-shapes, shared by input shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Shapes to find common sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | theMultiShare | Specifies what type of shares should be checked:  - `TRUE:` search sub-shapes from 1st input shape shared with all other input shapes; - `FALSE:` causes to search sub-shapes shared between couples of input shapes. |

Note
:   If *theShapes* contains single compound, the shares between all possible couples of its top-level shapes are returned; otherwise, only shares between 1st input shape and all rest input shapes are returned.

Returns
:   List of all found sub-shapes.

### GetShapesOnPlane()

```python
ListOfGO GetShapesOnPlane(in GEOM_Object theShape, in long theShapeType, in GEOM_Object theAx1, in shape_state theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified plane by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | theAx1 | Vector (or line, or linear edge), specifying normal direction and location of the plane to find shapes on. |
    | theState | The state of the sub-shapes to find. |

Returns
:   List of all found sub-shapes.

### GetShapesOnPlaneWithLocation()

```python
ListOfGO GetShapesOnPlaneWithLocation(in GEOM_Object theShape, in long theShapeType, in GEOM_Object theAx1, in GEOM_Object thePnt, in shape_state theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified plane by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | theAx1 | Vector (or line, or linear edge), specifying normal direction of the plane to find shapes on. |
    | thePnt | Point specifying location of the plane to find shapes on. |
    | theState | The state of the sub-shapes to find. |

Returns
:   List of all found sub-shapes.

### GetShapesOnCylinder()

```python
ListOfGO GetShapesOnCylinder(in GEOM_Object theShape, in long theShapeType, in GEOM_Object theAxis, in double theRadius, in shape_state theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified cylinder by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | theAxis | Vector (or line, or linear edge), specifying axis of the cylinder to find shapes on. |
    | theRadius | Radius of the cylinder to find shapes on. |
    | theState | The state of the sub-shapes to find. |

Returns
:   List of all found sub-shapes.

### GetShapesOnCylinderWithLocation()

```python
ListOfGO GetShapesOnCylinderWithLocation(in GEOM_Object theShape, in long theShapeType, in GEOM_Object theAxis, in GEOM_Object thePnt, in double theRadius, in shape_state theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified cylinder by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | theAxis | Vector (or line, or linear edge), specifying axis of the cylinder to find shapes on. |
    | thePnt | Point specifying location of the bottom of the cylinder. |
    | theRadius | Radius of the cylinder to find shapes on. |
    | theState | The state of the sub-shapes to find. |

Returns
:   List of all found sub-shapes.

### GetShapesOnSphere()

```python
ListOfGO GetShapesOnSphere(in GEOM_Object theShape, in long theShapeType, in GEOM_Object theCenter, in double theRadius, in shape_state theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified sphere by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | theCenter | Point, specifying center of the sphere to find shapes on. |
    | theRadius | Radius of the sphere to find shapes on. |
    | theState | The state of the sub-shapes to find. |

Returns
:   List of all found sub-shapes.

### GetShapesOnQuadrangle()

```python
ListOfGO GetShapesOnQuadrangle(in GEOM_Object theShape, in long theShapeType, in GEOM_Object theTopLeftPoint, in GEOM_Object theTopRightPoint, in GEOM_Object theBottomLeftPoint, in GEOM_Object theBottomRightPoint, in shape_state theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified quadrangle by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | theTopLeftPoint | Top left quadrangle corner |
    | theTopRightPoint | Top right quadrangle corner |
    | theBottomLeftPoint | Bottom left quadrangle corner |
    | theBottomRightPoint | Bottom right quadrangle corner |
    | theState | The state of the sub-shapes to find. |

Returns
:   List of all found sub-shapes.

### GetShapesOnPlaneIDs()

```python
ListOfLong GetShapesOnPlaneIDs(in GEOM_Object theShape, in long theShapeType, in GEOM_Object theAx1, in shape_state theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified plane by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | theAx1 | Vector (or line, or linear edge), specifying normal direction and location of the plane to find shapes on. |
    | theState | The state of the sub-shapes to find. |

Returns
:   List of IDs of all found sub-shapes.

### GetShapesOnPlaneWithLocationIDs()

```python
ListOfLong GetShapesOnPlaneWithLocationIDs(in GEOM_Object theShape, in long theShapeType, in GEOM_Object theAx1, in GEOM_Object thePnt, in shape_state theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified plane by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | theAx1 | Vector (or line, or linear edge), specifying normal direction of the plane to find shapes on. |
    | thePnt | Point specifying location of the plane to find shapes on. |
    | theState | The state of the sub-shapes to find. |

Returns
:   List of IDs of all found sub-shapes.

### GetShapesOnCylinderIDs()

```python
ListOfLong GetShapesOnCylinderIDs(in GEOM_Object theShape, in long theShapeType, in GEOM_Object theAxis, in double theRadius, in shape_state theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified cylinder by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | theAxis | Vector (or line, or linear edge), specifying axis of the cylinder to find shapes on. |
    | theRadius | Radius of the cylinder to find shapes on. |
    | theState | The state of the sub-shapes to find. |

Returns
:   List of IDs of all found sub-shapes.

### GetShapesOnCylinderWithLocationIDs()

```python
ListOfLong GetShapesOnCylinderWithLocationIDs(in GEOM_Object theShape, in long theShapeType, in GEOM_Object theAxis, in GEOM_Object thePnt, in double theRadius, in shape_state theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified cylinder by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | theAxis | Vector (or line, or linear edge), specifying axis of the cylinder to find shapes on. |
    | thePnt | Point specifying location of the bottom of the cylinder. |
    | theRadius | Radius of the cylinder to find shapes on. |
    | theState | The state of the sub-shapes to find. |

Returns
:   List of IDs all found sub-shapes.

### GetShapesOnSphereIDs()

```python
ListOfLong GetShapesOnSphereIDs(in GEOM_Object theShape, in long theShapeType, in GEOM_Object theCenter, in double theRadius, in shape_state theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified sphere by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | theCenter | Point, specifying center of the sphere to find shapes on. |
    | theRadius | Radius of the sphere to find shapes on. |
    | theState | The state of the sub-shapes to find. |

Returns
:   List of IDs of all found sub-shapes.

### GetShapesOnQuadrangleIDs()

```python
ListOfLong GetShapesOnQuadrangleIDs(in GEOM_Object theShape, in long theShapeType, in GEOM_Object theTopLeftPoint, in GEOM_Object theTopRightPoint, in GEOM_Object theBottomLeftPoint, in GEOM_Object theBottomRightPoint, in shape_state theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified quadrangle by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | theTopLeftPoint | Top left quadrangle corner |
    | theTopRightPoint | Top right quadrangle corner |
    | theBottomLeftPoint | Bottom left quadrangle corner |
    | theBottomRightPoint | Bottom right quadrangle corner |
    | theState | The state of the sub-shapes to find. |

Returns
:   List of IDs of all found sub-shapes.

### GetShapesOnBoxIDs()

```python
ListOfLong GetShapesOnBoxIDs(in GEOM_Object theBox, in GEOM_Object theShape, in long theShapeType, in shape_state theState)
```

Find sub-shapes complying with given status.

Parameters
:   |  |  |
    | --- | --- |
    | theBox | - the box to check state of sub-shapes against |
    | theShape | - the shape to explore |
    | theShapeType | - type of sub-shape of theShape |
    | theState | - required state |

Returns
:   List of IDs of all found sub-shapes.

### GetShapesOnBox()

```python
ListOfGO GetShapesOnBox(in GEOM_Object theBox, in GEOM_Object theShape, in long theShapeType, in shape_state theState)
```

Find sub-shapes complying with given status.

Parameters
:   |  |  |
    | --- | --- |
    | theBox | - the box to check state of sub-shapes against |
    | theShape | - the shape to explore |
    | theShapeType | - type of sub-shape of theShape |
    | theState | - required state |

Returns
:   List of all found sub-shapes.

### GetShapesOnShapeIDs()

```python
ListOfLong GetShapesOnShapeIDs(in GEOM_Object theCheckShape, in GEOM_Object theShape, in short theShapeType, in shape_state theState)
```

Find sub-shapes complying with given status.

Parameters
:   |  |  |
    | --- | --- |
    | theCheckShape | - the shape to check state of sub-shapes against. It must be a solid. |
    | theShape | - the shape to explore |
    | theShapeType | - type of sub-shape of theShape |
    | theState | - required state |

Returns
:   List of IDs of all found sub-shapes.

### GetShapesOnShape()

```python
ListOfGO GetShapesOnShape(in GEOM_Object theCheckShape, in GEOM_Object theShape, in short theShapeType, in shape_state theState)
```

Find sub-shapes complying with given status.

Parameters
:   |  |  |
    | --- | --- |
    | theCheckShape | - the shape to check state of sub-shapes against. It must be a solid. |
    | theShape | - the shape to explore |
    | theShapeType | - type of sub-shape of theShape |
    | theState | - required state |

Returns
:   List of all found sub-shapes.

### GetShapesOnShapeAsCompound()

```python
GEOM_Object GetShapesOnShapeAsCompound(in GEOM_Object theCheckShape, in GEOM_Object theShape, in short theShapeType, in shape_state theState)
```

Find sub-shapes complying with given status.

Parameters
:   |  |  |
    | --- | --- |
    | theCheckShape | - the shape to check state of sub-shapes against. It must be a solid. |
    | theShape | - the shape to explore |
    | theShapeType | - type of sub-shape of theShape |
    | theState | - required state |

Returns
:   compound includes all found sub-shapes.

### GetInPlace()

```python
GEOM_Object GetInPlace(in GEOM_Object theShapeWhere, in GEOM_Object theShapeWhat)
```

Get sub-shape(s) of *theShapeWhere*, which are coincident with *theShapeWhat* or could be a part of it.

Parameters
:   |  |  |
    | --- | --- |
    | theShapeWhere | Shape to find sub-shapes of. |
    | theShapeWhat | Shape, specifying what to find. |

Returns
:   Compound which includes all found sub-shapes if they have different types; or group of all found shapes of the equal type; or a single found sub-shape.

### GetInPlaceOld()

```python
GEOM_Object GetInPlaceOld(in GEOM_Object theShapeWhere, in GEOM_Object theShapeWhat)
```

Old implementation of GetInPlace functionality, based on shape properties.

### GetInPlaceByHistory()

```python
GEOM_Object GetInPlaceByHistory(in GEOM_Object theShapeWhere, in GEOM_Object theShapeWhat)
```

Get sub-shape(s) of *theShapeWhere*, which are coincident with *theShapeWhat* or could be a part of it.

Implementation of this method is based on a saved history of an operation, produced *theShapeWhere*. The *theShapeWhat* must be among this operation's arguments (an argument shape or a sub-shape of an argument shape). The operation could be the Partition or one of boolean operations, performed on simple shapes (not on compounds).

Parameters
:   |  |  |
    | --- | --- |
    | theShapeWhere | Shape to find sub-shapes of. |
    | theShapeWhat | Shape, specifying what to find. |

Returns
:   Compound which includes all found sub-shapes if they have different types; or group of all found shapes of the equal type; or a single found sub-shape.

### GetInPlaceMap()

```python
ListOfListOfLong GetInPlaceMap(in GEOM_Object theShapeWhere, in GEOM_Object theShapeWhat)
```

A sort of GetInPlace functionality, returning for each sub-shape ID of *theShapeWhat* a list of corresponding sub-shape IDs of *theShapeWhere*. For example, if theShapeWhat is a box and theShapeWhere is this box cut into two parts by a plane, then the result can be as this: len( result_list ) = 35, result_list[ 1 ] = [ 2, 36 ], which means that the box turned into two solids with IDs 2 and 36 within theShapeWhere.

### GetSame()

```python
GEOM_Object GetSame(in GEOM_Object theShapeWhere, in GEOM_Object theShapeWhat)
```

Get sub-shape of theShapeWhere, which are coincident with *theShapeWhat* that can either SOLID, FACE, EDGE or VERTEX.

Parameters
:   |  |  |
    | --- | --- |
    | theShapeWhere | Shape to find sub-shapes of. |
    | theShapeWhat | Shape, specifying what to find. |

Returns
:   found sub-shape.

### GetSameIDs()

```python
ListOfLong GetSameIDs(in GEOM_Object theShapeWhere, in GEOM_Object theShapeWhat)
```

Get sub-shape Ids of theShapeWhere, which are coincident with *theShapeWhat* that can either SOLID, FACE, EDGE or VERTEX.

Parameters
:   |  |  |
    | --- | --- |
    | theShapeWhere | Shape to find sub-shapes of. |
    | theShapeWhat | Shape, specifying what to find. |

Returns
:   found sub-shape Ids.

### ExtendEdge()

```python
GEOM_Object ExtendEdge(in GEOM_Object theEdge, in double theMin, in double theMax)
```

Resize the input edge with the new Min and Max parameters. The input edge parameters range is [0, 1]. If theMin parameter is negative, the input edge is extended, otherwise it is shrinked by theMin parameter. If theMax is greater than 1, the edge is extended, otherwise it is shrinked by theMax parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theEdge | the input edge to be resized. |
    | theMin | the minimal parameter value. |
    | theMax | the maximal parameter value. |

Returns
:   a newly created edge.

### ExtendFace()

```python
GEOM_Object ExtendFace(in GEOM_Object theFace, in double theUMin, in double theUMax, in double theVMin, in double theVMax)
```

Resize the input face with the new UMin, UMax, VMin and VMax parameters. The input face U and V parameters range is [0, 1]. If theUMin parameter is negative, the input face is extended, otherwise it is shrinked along U direction by theUMin parameter. If theUMax is greater than 1, the face is extended, otherwise it is shrinked along U direction by theUMax parameter. So as for theVMin, theVMax and V direction of the input face.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | the input face to be resized. |
    | theUMin | the minimal U parameter value. |
    | theUMax | the maximal U parameter value. |
    | theVMin | the minimal V parameter value. |
    | theVMax | the maximal V parameter value. |

Returns
:   a newly created face.

### MakeSurfaceFromFace()

```python
GEOM_Object MakeSurfaceFromFace(in GEOM_Object theFace)
```

Make a surface from a face. This function takes some face as input parameter and creates new [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), i.e. topological shape by extracting underlying surface of the source face and limiting it by the Umin, Umax, Vmin, Vmax parameters of the source face (in the parametrical space).

Parameters
:   |  |  |
    | --- | --- |
    | theFace | the input face. |

Returns
:   a newly created face.

### GetSubShapeEdgeSorted()

```python
ListOfGO GetSubShapeEdgeSorted(in GEOM_Object theShape, in GEOM_Object theStartPoint)
```

Explode a shape into edges sorted in a row from a starting point.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | - the shape to be exploded on edges. |
    | theStartPoint | - the starting point. |

Returns
:   Ordered list of edges sorted in a row from a starting point.

### GetSubShapesWithTolerance()

```python
ListOfGO GetSubShapesWithTolerance(in GEOM_Object theShape, in short theShapeType, in comparison_condition theCondition, in double theTolerance)
```

Return the list of subshapes that satisfies a certain tolerance criterion. The user defines the type of shapes to be returned, the condition and the tolerance value. The operation is defined for faces, edges and vertices only. E.g. for theShapeType FACE, theCondition CC_GT and theTolerance 1.e-7 this method returns all faces of theShape that have tolerances greater then 1.e7.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | the shape to be exploded |
    | theShapeType | the type of shapes to be returned. Can have the values FACE, EDGE and VERTEX only. |
    | theCondition | the condition type. |
    | theTolerance | the tolerance filter. |

Returns
:   the list of shapes that satisfy the conditions.

### MakeExtraction()

```python
GEOM_Object MakeExtraction(in GEOM_Object theShape, in ListOfLong theSubShapeIDs, out ExtractionStats theStats)
```

Return the shape that is constructed from theShape without extracted sub-shapes from the input list.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | the original shape. |
    | theSubShapeIDs | the list of sub-shape IDs to be extracted from the original shape. |
    | theStats | the operation statistics. Output parameter. |

Returns
:   the shape without extracted sub-shapes.

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
