<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__IHealingOperations.html -->

# GEOM_IHealingOperations Interface Reference

Interface for shape healing operations.
[More...](interfaceGEOM_1_1GEOM__IHealingOperations.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for shape healing operations.

Shape Processing, SuppressFaces, etc.

## Member Function Documentation

### ProcessShape()

```python
GEOM_Object ProcessShape(in GEOM_Object theShapes, in string_array theOperators, in string_array theParameters, in string_array theValues)
```

Apply a sequence of Shape Healing operators to the given object.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Shape to be processed. |
    | theOperators | List of names of operators ("FixShape", "SplitClosedFaces", etc.). |
    | theParameters | List of names of parameters ("FixShape.Tolerance3d", "SplitClosedFaces.NbSplitPoints", etc.). |
    | theValues | List of values of parameters, in the same order as parameters are listed in *theParameters* list. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

### GetShapeProcessParameters()

```python
void GetShapeProcessParameters(out string_array theOperators, out string_array theParameters, out string_array theValues)
```

Get default sequence of operators, their parameters and parameters' values of Shape Process operation.

In the current implementation the defaults are read from the file pointed by CSF_ShHealingDefaults environmental variable.

Parameters
:   |  |  |
    | --- | --- |
    | theOperators | Output. Default list of names of operators. |
    | theParameters | Output. Default list of names of parameters. |
    | theValues | Output. List of default values of parameters, in the same order as parameters are listed in *theParameters* list. |

### GetOperatorParameters()

```python
void GetOperatorParameters(in string theOperator, out string_array theParameters, out string_array theValues)
```

Get parameters and parameters' values for the given Shape Process operation.

In the current implementation the defaults are read from the file pointed by CSF_ShHealingDefaults environmental variable.

Parameters
:   |  |  |
    | --- | --- |
    | theOperator | Input. The operator's name. |
    | theParameters | Output. Default list of names of parameters. |
    | theValues | Output. List of default values of parameters, in the same order as parameters are listed in *theParameters* list. |

### SuppressFaces()

```python
GEOM_Object SuppressFaces(in GEOM_Object theObject, in short_array theFaces)
```

Remove faces from the given object (shape).

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | theFaces | Indices of faces to be removed, if EMPTY then the method removes ALL faces of the given object. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

### CloseContour()

```python
GEOM_Object CloseContour(in GEOM_Object theObject, in short_array theWires, in boolean isCommonVertex)
```

Close an open wire.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | theWires | Indexes of edge(s) and wire(s) to be closed within *theObject*'s shape, if -1, then theObject itself is a wire. |
    | isCommonVertex | If TRUE : closure by creation of a common vertex, If FALS : closure by creation of an edge between ends. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

### RemoveIntWires()

```python
GEOM_Object RemoveIntWires(in GEOM_Object theObject, in short_array theWires)
```

Remove internal wires and edges from the given object (face).

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | theWires | Indices of wires to be removed, if EMPTY then the method removes ALL internal wires of the given object. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

### FillHoles()

```python
GEOM_Object FillHoles(in GEOM_Object theObject, in short_array theWires)
```

Remove internal closed contours (holes) from the given object.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | theWires | Indices of wires to be removed, if EMPTY then the method removes ALL internal holes of the given object |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

### Sew()

```python
GEOM_Object Sew(in ListOfGO theObjects, in double theTolerance)
```

Sewing of the given object.

Parameters
:   |  |  |
    | --- | --- |
    | theObjects | Shapes to be processed. |
    | theTolerance | Required tolerance value. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

### SewAllowNonManifold()

```python
GEOM_Object SewAllowNonManifold(in ListOfGO theObjects, in double theTolerance)
```

Sewing of the given object. Allows non-manifold sewing.

Parameters
:   |  |  |
    | --- | --- |
    | theObjects | Shapes to be processed. |
    | theTolerance | Required tolerance value. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

### RemoveInternalFaces()

```python
GEOM_Object RemoveInternalFaces(in ListOfGO theSolids)
```

Rebuild the topology of theSolids by removing the faces that are shared by several solids.

Parameters
:   |  |  |
    | --- | --- |
    | theSolids | A list of shapes containing solids to be processed. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

### DivideEdge()

```python
GEOM_Object DivideEdge(in GEOM_Object theObject, in short theEdgeIndex, in double theValue, in boolean isByParameter)
```

Addition of a point to a given edge of *theObject*.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | theEdgeIndex | Index of edge to be divided within theObject's shape, if -1, then theObject itself is the edge. |
    | theValue | Value of parameter on edge or length parameter, depending on *isByParameter*. |
    | isByParameter | If TRUE : *theValue* is treated as a curve parameter [0..1], if FALSE : *theValue* is treated as a length parameter [0..1] |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the processed shape.

### DivideEdgeByPoint()

```python
GEOM_Object DivideEdgeByPoint(in GEOM_Object theObject, in short theEdgeIndex, in ListOfGO thePoints)
```

Addition of points to a given edge of *theObject* by projecting other points to the given edge.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | theEdgeIndex | Index of edge to be divided within theObject's shape, if -1, then theObject itself is the edge. |
    | thePoints | Points to project to theEdgeIndex-th edge. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the processed shape.

### FuseCollinearEdgesWithinWire()

```python
GEOM_Object FuseCollinearEdgesWithinWire(in GEOM_Object theWire, in ListOfGO theVertices)
```

Suppress the vertices in the wire in case if adjacent edges are C1 continuous.

Parameters
:   |  |  |
    | --- | --- |
    | theWire | Wire to minimize the number of C1 continuous edges in. |
    | theVertices | A list of vertices to suppress. If the list is empty, all vertices in a wire will be assumed. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) with modified wire.

### GetFreeBoundary()

```python
boolean GetFreeBoundary(in ListOfGO theObjects, out ListOfGO theClosedWires, out ListOfGO theOpenWires)
```

Get a list of wires (wrapped in GEOM_Object-s), that constitute a free boundary of the given shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theObjects | Shapes to get free boundary of. |
    | theClosedWires | Output. Closed wires on the free boundary of the given shape. |
    | theOpenWires | Output. Open wires on the free boundary of the given shape. |

Returns
:   FALSE, if an error(s) occurred during the method execution.

### ChangeOrientation()

```python
GEOM_Object ChangeOrientation(in GEOM_Object theObject)
```

Change orientation of the given object.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

### ChangeOrientationCopy()

```python
GEOM_Object ChangeOrientationCopy(in GEOM_Object theObject)
```

### LimitTolerance()

```python
GEOM_Object LimitTolerance(in GEOM_Object theObject, in double theTolerance, in boolean theExactAdjust)
```

Try to limit tolerance of the given object by value *theTolerance*.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | theTolerance | Required tolerance value. |
    | theExactAdjust | If true, take into account exact tolerance of edges. In some cases, this may result in edge tolerances being increased to values greater than both the original and required ones. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing processed shape.

### FuncToPythonDump()

```python
void FuncToPythonDump(in GEOM_Object theObject, in GEOM_Object result, in string imports, in string funcName, in string args)
```

Provides Python dump functionality for algorithms entirely implemented in Python.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be processed. |
    | result | Shape of the algorithm execution. |
    | imports | module import for current functon. |
    | funcName | name of a Python function that we need to put into dump. |
    | args | arguments of the Python function. |

### GetStatistics()

```python
ModifStatistics GetStatistics()
```

Return information on what has been done by the last called healing method.

Returns
:   ModifStatistics, information container.

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
