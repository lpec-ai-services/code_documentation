<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l4__obtain.html -->

# Access to sub-shapes by a criteria geomBuilder Python module » All package methods, grouped by their purpose » Creating geometrical objects » Creating Advanced Geometrical Objects

## Detailed Description

## Function Documentation

### GetFreeFacesIDs()

```python
def GetFreeFacesIDs(self, theShape)
```

Retrieve all free faces from the given shape.

Free face is a face, which is not shared between two shells of the shape.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find free faces in. |

Returns
:   List of IDs of all free faces, contained in theShape.

[Example](../tui_free_faces_page.md)

### GetSharedShapes()

```python
def GetSharedShapes(self, theShape1, theShape2, theShapeType, theName = None)
```

Get all sub-shapes of theShape1 of the given type, shared with theShape2.

Parameters
:   |  |  |
    | --- | --- |
    | theShape1 | Shape to find sub-shapes in. |
    | theShape2 | Shape to find shared sub-shapes with. |
    | theShapeType | Type of sub-shapes to be retrieved. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of sub-shapes of theShape1, shared with theShape2.

[Example](../tui_test_others_page.md#swig_GetSharedShapes)

### GetSharedShapesMulti()

```python
def GetSharedShapesMulti(self, theShapes, theShapeType, theMultiShare = True, theName = None)
```

Get sub-shapes, shared by input shapes.

Parameters
:   |  |  |
    | --- | --- |
    | theShapes | Either a list or compound of shapes to find common sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)). |
    | theMultiShare | Specifies what type of shares should be checked:  - `True` (default): search sub-shapes from 1st input shape shared with all other input shapes; - `False:` causes to search sub-shapes shared between couples of input shapes. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Note
:   If *theShapes* contains single compound, the shares between all possible couples of its top-level shapes are returned; otherwise, only shares between 1st input shape and all rest input shapes are returned.

Returns
:   List of all found sub-shapes.

Examples:

- [Example 1](../tui_basic_operations_page.md#tui_shared_shapes)
- [Example 2](../tui_test_others_page.md#swig_GetSharedShapes)

### GetShapesOnPlane()

```python
def GetShapesOnPlane(self, theShape, theShapeType, theAx1, theState, theName = None)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified plane by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theAx1 | Vector (or line, or linear edge), specifying normal direction and location of the plane to find shapes on. |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of all found sub-shapes.

[Example](../tui_test_others_page.md#swig_GetShapesOnPlane)

### GetShapesOnPlaneIDs()

```python
def GetShapesOnPlaneIDs(self, theShape, theShapeType, theAx1, theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified plane by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theAx1 | Vector (or line, or linear edge), specifying normal direction and location of the plane to find shapes on. |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |

Returns
:   List of all found sub-shapes indices.

[Example](../tui_test_others_page.md#swig_GetShapesOnPlaneIDs)

### GetShapesOnPlaneWithLocation()

```python
def GetShapesOnPlaneWithLocation(self, theShape, theShapeType, theAx1, thePnt, theState, theName = None)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified plane by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theAx1 | Vector (or line, or linear edge), specifying normal direction of the plane to find shapes on. |
    | thePnt | Point specifying location of the plane to find shapes on. |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of all found sub-shapes.

[Example](../tui_test_others_page.md#swig_GetShapesOnPlaneWithLocation)

### GetShapesOnPlaneWithLocationIDs()

```python
def GetShapesOnPlaneWithLocationIDs(self, theShape, theShapeType, theAx1, thePnt, theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified plane by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theAx1 | Vector (or line, or linear edge), specifying normal direction of the plane to find shapes on. |
    | thePnt | Point specifying location of the plane to find shapes on. |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |

Returns
:   List of all found sub-shapes indices.

[Example](../tui_test_others_page.md#swig_GetShapesOnPlaneWithLocationIDs)

### GetShapesOnCylinder()

```python
def GetShapesOnCylinder(self, theShape, theShapeType, theAxis, theRadius, theState, theName = None)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified cylinder by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theAxis | Vector (or line, or linear edge), specifying axis of the cylinder to find shapes on. |
    | theRadius | Radius of the cylinder to find shapes on. |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of all found sub-shapes.

[Example](../tui_test_others_page.md#swig_GetShapesOnCylinder)

### GetShapesOnCylinderIDs()

```python
def GetShapesOnCylinderIDs(self, theShape, theShapeType, theAxis, theRadius, theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified cylinder by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theAxis | Vector (or line, or linear edge), specifying axis of the cylinder to find shapes on. |
    | theRadius | Radius of the cylinder to find shapes on. |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |

Returns
:   List of all found sub-shapes indices.

[Example](../tui_test_others_page.md#swig_GetShapesOnCylinderIDs)

### GetShapesOnCylinderWithLocation()

```python
def GetShapesOnCylinderWithLocation(self, theShape, theShapeType, theAxis, thePnt, theRadius, theState, theName = None)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified cylinder by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theAxis | Vector (or line, or linear edge), specifying axis of the cylinder to find shapes on. |
    | thePnt | Point specifying location of the bottom of the cylinder. |
    | theRadius | Radius of the cylinder to find shapes on. |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of all found sub-shapes.

[Example](../tui_test_others_page.md#swig_GetShapesOnCylinderWithLocation)

### GetShapesOnCylinderWithLocationIDs()

```python
def GetShapesOnCylinderWithLocationIDs(self, theShape, theShapeType, theAxis, thePnt, theRadius, theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified cylinder by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theAxis | Vector (or line, or linear edge), specifying axis of the cylinder to find shapes on. |
    | thePnt | Point specifying location of the bottom of the cylinder. |
    | theRadius | Radius of the cylinder to find shapes on. |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |

Returns
:   List of all found sub-shapes indices

[Example](../tui_test_others_page.md#swig_GetShapesOnCylinderWithLocationIDs)

### GetShapesOnSphere()

```python
def GetShapesOnSphere(self, theShape, theShapeType, theCenter, theRadius, theState, theName = None)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified sphere by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theCenter | Point, specifying center of the sphere to find shapes on. |
    | theRadius | Radius of the sphere to find shapes on. |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of all found sub-shapes.

[Example](../tui_test_others_page.md#swig_GetShapesOnSphere)

### GetShapesOnSphereIDs()

```python
def GetShapesOnSphereIDs(self, theShape, theShapeType, theCenter, theRadius, theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified sphere by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theCenter | Point, specifying center of the sphere to find shapes on. |
    | theRadius | Radius of the sphere to find shapes on. |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |

Returns
:   List of all found sub-shapes indices.

[Example](../tui_test_others_page.md#swig_GetShapesOnSphereIDs)

### GetShapesOnQuadrangle()

```python
def GetShapesOnQuadrangle(self, theShape, theShapeType, theTopLeftPoint, theTopRightPoint, theBottomLeftPoint, theBottomRightPoint, theState, theName = None)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified quadrangle by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theTopLeftPoint | Point, specifying top left corner of a quadrangle |
    | theTopRightPoint | Point, specifying top right corner of a quadrangle |
    | theBottomLeftPoint | Point, specifying bottom left corner of a quadrangle |
    | theBottomRightPoint | Point, specifying bottom right corner of a quadrangle |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of all found sub-shapes.

[Example](../tui_test_others_page.md#swig_GetShapesOnQuadrangle)

### GetShapesOnQuadrangleIDs()

```python
def GetShapesOnQuadrangleIDs(self, theShape, theShapeType, theTopLeftPoint, theTopRightPoint, theBottomLeftPoint, theBottomRightPoint, theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified quadrangle by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theTopLeftPoint | Point, specifying top left corner of a quadrangle |
    | theTopRightPoint | Point, specifying top right corner of a quadrangle |
    | theBottomLeftPoint | Point, specifying bottom left corner of a quadrangle |
    | theBottomRightPoint | Point, specifying bottom right corner of a quadrangle |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |

Returns
:   List of all found sub-shapes indices.

[Example](../tui_test_others_page.md#swig_GetShapesOnQuadrangleIDs)

### GetShapesOnBox()

```python
def GetShapesOnBox(self, theBox, theShape, theShapeType, theState, theName = None)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified *theBox* by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theBox | Shape for relative comparing. |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of all found sub-shapes.

[Example](../tui_test_others_page.md#swig_GetShapesOnBox)

### GetShapesOnBoxIDs()

```python
def GetShapesOnBoxIDs(self, theBox, theShape, theShapeType, theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified *theBox* by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theBox | Shape for relative comparing. |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |

Returns
:   List of all found sub-shapes indices.

[Example](../tui_test_others_page.md#swig_GetShapesOnBoxIDs)

### GetShapesOnShape()

```python
def GetShapesOnShape(self, theCheckShape, theShape, theShapeType, theState, theName = None)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified *theCheckShape* by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theCheckShape | Shape for relative comparing. It must be a solid. |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   List of all found sub-shapes.

[Example](../tui_test_others_page.md#swig_GetShapesOnShape)

### GetShapesOnShapeAsCompound()

```python
def GetShapesOnShapeAsCompound(self, theCheckShape, theShape, theShapeType, theState, theName = None)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified *theCheckShape* by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theCheckShape | Shape for relative comparing. It must be a solid. |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   All found sub-shapes as compound.

[Example](../tui_test_others_page.md#swig_GetShapesOnShapeAsCompound)

### GetShapesOnShapeIDs()

```python
def GetShapesOnShapeIDs(self, theCheckShape, theShape, theShapeType, theState)
```

Find in *theShape* all sub-shapes of type *theShapeType*, situated relatively the specified *theCheckShape* by the certain way, defined through *theState* parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theCheckShape | Shape for relative comparing. It must be a solid. |
    | theShape | Shape to find sub-shapes of. |
    | theShapeType | Type of sub-shapes to be retrieved (see [ShapeType()](group__l1__geomBuilder__auxiliary.md#ga96e518bf4bc81e1f62dca7fa5e971d82)) |
    | theState | The state of the sub-shapes to find (see [GEOM::shape_state](namespaceGEOM.md#ad9572b1d6261e2610cc6d64e022cc2c7)) |

Returns
:   List of all found sub-shapes indices.

[Example](../tui_test_others_page.md#swig_GetShapesOnShapeIDs)

### GetInPlace()

```python
def GetInPlace(self, theShapeWhere, theShapeWhat, isNewImplementation = False, theName = None)
```

Get sub-shape(s) of theShapeWhere, which are coincident with *theShapeWhat* or could be a part of it.

Parameters
:   |  |  |
    | --- | --- |
    | theShapeWhere | Shape to find sub-shapes of. |
    | theShapeWhat | Shape, specifying what to find. |
    | isNewImplementation | implementation of GetInPlace functionality (default = False, old alghorithm based on shape properties) |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   Compound which includes all found sub-shapes if they have different types; or group of all found shapes of the equal type; or a single found sub-shape.

Note
:   This function has a restriction on argument shapes. If *theShapeWhere* has curved parts with significantly outstanding centres (i.e. the mass centre of a part is closer to *theShapeWhat* than to the part), such parts will not be found.

    ![get_in_place_lost_part.png](https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/get_in_place_lost_part.png)

[Example](../tui_test_others_page.md#swig_GetInPlace)

### GetInPlaceByHistory()

```python
def GetInPlaceByHistory(self, theShapeWhere, theShapeWhat, theName = None)
```

Get sub-shape(s) of *theShapeWhere*, which are coincident with *theShapeWhat* or could be a part of it.

Implementation of this method is based on a saved history of an operation, produced *theShapeWhere*. The *theShapeWhat* must be among this operation's arguments (an argument shape or a sub-shape of an argument shape). The operation could be the Partition or one of boolean operations, performed on simple shapes (not on compounds).

Parameters
:   |  |  |
    | --- | --- |
    | theShapeWhere | Shape to find sub-shapes of. |
    | theShapeWhat | Shape, specifying what to find (must be in the building history of the ShapeWhere). |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   Compound which includes all found sub-shapes if they have different types; or group of all found shapes of the equal type; or a single found sub-shape.

[Example](../tui_test_others_page.md#swig_GetInPlace)

### GetInPlaceMap()

```python
def GetInPlaceMap(self, theShapeWhere, theShapeWhat)
```

A sort of GetInPlace functionality, returning IDs of sub-shapes.

For each sub-shape ID of *theShapeWhat* return a list of corresponding sub-shape IDs of *theShapeWhere*. For example, if theShapeWhat is a box and theShapeWhere is this box cut into two parts by a plane, then the result can be as this: len( result_list ) = 35, result_list[ 1 ] = [ 2, 36 ], which means that the box (ID 1) turned into two solids with IDs 2 and 36 within theShapeWhere

Parameters
:   |  |  |
    | --- | --- |
    | theShapeWhere | Shape to find sub-shapes of. |
    | theShapeWhat | Shape, specifying what to find. |

Returns
:   List of lists of sub-shape IDS of theShapeWhere.

### GetSame()

```python
def GetSame(self, theShapeWhere, theShapeWhat, theName = None)
```

Get sub-shape of theShapeWhere, which is equal to *theShapeWhat*.

Parameters
:   |  |  |
    | --- | --- |
    | theShapeWhere | Shape to find sub-shape of. |
    | theShapeWhat | Shape, specifying what to find. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) for found sub-shape.

[Example](../tui_test_others_page.md#swig_GetSame)

### GetSameIDs()

```python
def GetSameIDs(self, theShapeWhere, theShapeWhat)
```

Get sub-shape indices of theShapeWhere, which is equal to *theShapeWhat*.

Parameters
:   |  |  |
    | --- | --- |
    | theShapeWhere | Shape to find sub-shape of. |
    | theShapeWhat | Shape, specifying what to find. |

Returns
:   List of all found sub-shapes indices.

[Example](../tui_test_others_page.md#swig_GetSame)

### ExtendEdge()

```python
def ExtendEdge(self, theEdge, theMin, theMax, theName = None)
```

Resize the input edge with the new Min and Max parameters.

The input edge parameters range is [0, 1]. If theMin parameter is negative, the input edge is extended, otherwise it is shrinked by theMin parameter. If theMax is greater than 1, the edge is extended, otherwise it is shrinked by theMax parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theEdge | the input edge to be resized. |
    | theMin | the minimal parameter value. |
    | theMax | the maximal parameter value. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created edge.

[Example](../tui_transformation_operations_page.md#tui_extend)

### ExtendFace()

```python
def ExtendFace(self, theFace, theUMin, theUMax, theVMin, theVMax, theName = None)
```

Resize the input face with the new UMin, UMax, VMin and VMax parameters.

The input face U and V parameters range is [0, 1]. If theUMin parameter is negative, the input face is extended, otherwise it is shrinked along U direction by theUMin parameter. If theUMax is greater than 1, the face is extended, otherwise it is shrinked along U direction by theUMax parameter. So as for theVMin, theVMax and V direction of the input face.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | the input face to be resized. |
    | theUMin | the minimal U parameter value. |
    | theUMax | the maximal U parameter value. |
    | theVMin | the minimal V parameter value. |
    | theVMax | the maximal V parameter value. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

[Example](../tui_transformation_operations_page.md#tui_extend)

### MakeSurfaceFromFace()

```python
def MakeSurfaceFromFace(self, theFace, theName = None)
```

This function takes some face as input parameter and creates new GEOM_Object, i.e.

topological shape by extracting underlying surface of the source face and limiting it by the Umin, Umax, Vmin, Vmax parameters of the source face (in the parametrical space).

Parameters
:   |  |  |
    | --- | --- |
    | theFace | the input face. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

[Example](../tui_basic_geom_objs_page.md#tui_creation_surface)
