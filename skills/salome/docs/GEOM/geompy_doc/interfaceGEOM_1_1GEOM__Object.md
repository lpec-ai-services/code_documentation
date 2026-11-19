<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__Object.html -->

# GEOM_Object Interface Reference

Interface of geometric object.
[More...](interfaceGEOM_1_1GEOM__Object.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface of geometric object.

## Member Function Documentation

### GetShapeType()

```python
shape_type GetShapeType()
```

Get a *shape_type* of the object value.

### GetTopologyType()

```python
shape_type GetTopologyType()
```

Get the topology type of the object value.

In contrast to the shape type, this function returns type of the most top-level sub-shape of the COMPOUND or COMPSOLID, if there is only one sub-shape there.

See also
:   [GetShapeType()](interfaceGEOM_1_1GEOM__Object.md#ad45f0e158e340fb99aa40bc4fb30c23b), [GetCommonShapeType()](interfaceGEOM_1_1GEOM__Object.md#a963c6ef42a0472d508b34144b7d08601)

### GetCommonShapeType()

```python
shape_type GetCommonShapeType()
```

Get the common shape type of the top-level shapes contained in the object.

In contrast to the topology type, this function returns the common type of the top-level sub-shapes of the COMPOUND or COMPSOLID, if there are multiple sub-shapes there. If there is no common shape type ([GetMinShapeType()](interfaceGEOM_1_1GEOM__Object.md#a9a510f849dd10cef608d648972fc982c) and [GetMaxShapeType()](interfaceGEOM_1_1GEOM__Object.md#a5696d06d9dbb9bbdbd8e2156cd7dcbe8) return different values) for the same COMPOUND/COMPSOLID, the generic SHAPE value is returned.

See also
:   [GetShapeType()](interfaceGEOM_1_1GEOM__Object.md#ad45f0e158e340fb99aa40bc4fb30c23b), [GetTopologyType()](interfaceGEOM_1_1GEOM__Object.md#a6714a18847117830a8cf2687a00382ba), [GetMinShapeType()](interfaceGEOM_1_1GEOM__Object.md#a9a510f849dd10cef608d648972fc982c), [GetMaxShapeType()](interfaceGEOM_1_1GEOM__Object.md#a5696d06d9dbb9bbdbd8e2156cd7dcbe8)

### GetMinShapeType()

```python
shape_type GetMinShapeType()
```

Get a minimal type of the top-level shapes contained in the object.

This function is useful for the compounds only; for simple shapes it exactly the same value as [GetShapeType()](interfaceGEOM_1_1GEOM__Object.md#ad45f0e158e340fb99aa40bc4fb30c23b). Note, that compounds are processed recursively.

See also
:   [GetShapeType()](interfaceGEOM_1_1GEOM__Object.md#ad45f0e158e340fb99aa40bc4fb30c23b), [GetCommonShapeType()](interfaceGEOM_1_1GEOM__Object.md#a963c6ef42a0472d508b34144b7d08601), [GetTopologyType()](interfaceGEOM_1_1GEOM__Object.md#a6714a18847117830a8cf2687a00382ba), [GetMaxShapeType()](interfaceGEOM_1_1GEOM__Object.md#a5696d06d9dbb9bbdbd8e2156cd7dcbe8)

### GetMaxShapeType()

```python
shape_type GetMaxShapeType()
```

Get a maximal type of the top-level shapes contained in the object.

This function is useful for the compounds only; for simple shapes it exactly the same value as [GetShapeType()](interfaceGEOM_1_1GEOM__Object.md#ad45f0e158e340fb99aa40bc4fb30c23b). Note, that compounds are processed recursively.

See also
:   [GetShapeType()](interfaceGEOM_1_1GEOM__Object.md#ad45f0e158e340fb99aa40bc4fb30c23b), [GetCommonShapeType()](interfaceGEOM_1_1GEOM__Object.md#a963c6ef42a0472d508b34144b7d08601), [GetTopologyType()](interfaceGEOM_1_1GEOM__Object.md#a6714a18847117830a8cf2687a00382ba), [GetMinShapeType()](interfaceGEOM_1_1GEOM__Object.md#a9a510f849dd10cef608d648972fc982c)

### GetSubShapeName()

```python
string GetSubShapeName(in long subID)
```

Returns a name of a sub-shape if the sub-shape is published in the study.

Parameters
:   |  |  |
    | --- | --- |
    | subID | - sub-shape ID |

Returns
:   string - the found name or an empty string if the sub-shape does not exits or is not published in the study

Note
:   Only sub-shapes directly retrieved (using e.g. ExtractSubShapes() or via group creation) can be found. Also, as sub-shape can be published in the study many times, only the first found name is returned.

### SetColor()

```python
void SetColor(in SALOMEDS::Color theColor)
```

Set color of the object.

Parameters
:   |  |  |
    | --- | --- |
    | theColor | is a color of the object. |

### GetColor()

```python
SALOMEDS::Color GetColor()
```

Get color of the object.

### SetAutoColor()

```python
void SetAutoColor(in boolean theAutoColor)
```

Toggle auto color mode on the object.

Parameters
:   |  |  |
    | --- | --- |
    | theAutoColor | is a flag which toggles auto color mode. |

### GetAutoColor()

```python
boolean GetAutoColor()
```

Get flag of object's auto color mode.

### SetMarkerStd()

```python
void SetMarkerStd(in marker_type theType, in marker_size theSize)
```

Set standard point marker for the object.

Parameters
:   |  |  |
    | --- | --- |
    | theType | standard marker type |
    | theSize | marker relative size |

### SetMarkerTexture()

```python
void SetMarkerTexture(in long theTextureId)
```

Set custom point marker for the object.

The texture can be added by LoadTexture() or AddTexture() functions.

Parameters
:   |  |  |
    | --- | --- |
    | theTextureId | texture ID |

### GetMarkerType()

```python
marker_type GetMarkerType()
```

Get type of the point marker assigned to the object.

Returns
:   current marker type (MT_NONE if no marker is set)

### GetMarkerSize()

```python
marker_size GetMarkerSize()
```

Get size of the point marker assigned to the object.

Returns
:   current marker relative size (MS_NONE if no marker is set)

### GetMarkerTexture()

```python
long GetMarkerTexture()
```

Get texture idenifier of the point marker assigned to the object.

Returns
:   marker texture ID (0 if no marker set)

### getShape()

```python
long long getShape()
```

Get the TopoDS_Shape, for colocated case only.

### GetShapeStream()

```python
SALOMEDS::TMPFile GetShapeStream()
```

Get geometric shape of the object as a byte stream in BRep format.

Note
:   [GEOM_IInsertOperations::RestoreShape()](interfaceGEOM_1_1GEOM__IInsertOperations.md#adc9e776aa41e00b1a4f275d7c9b61a87) method can be used to restore shape from a BRep stream.

### IsMainShape()

```python
boolean IsMainShape()
```

### GetSubShapeIndices()

```python
ListOfLong GetSubShapeIndices()
```

### GetMainShape()

```python
GEOM_Object GetMainShape()
```

### IsParametrical()

```python
boolean IsParametrical()
```

### SetName()

```python
void SetName(in string theName) inherited
```

Set name of the object.

Parameters
:   |  |  |
    | --- | --- |
    | theName | is a name which will be associated with this object. |

### GetName()

```python
string GetName() inherited
```

Get name of the object associated with this object.

### GetEntry()

```python
string GetEntry() inherited
```

Get internal (unique) entry of the object in the [GEOM](namespaceGEOM.md) component's data tree.

Note
:   This is not an entry of the data object in SALOME study. This is internal function of [GEOM](namespaceGEOM.md) component, though it can be used outside it for appropriate reason (e.g. for unique identification of geometry object).

### GetType()

```python
long GetType() inherited
```

Get internal type of operation created this object (POINT, BOX, CYLINDER, EXTRUSION...).

Note
:   To get topological information on the object, use [WhatIs()](interfaceGEOM_1_1GEOM__IMeasureOperations.md#af1e211e4fa6f02d4ef64fcecbc52b36a) or [KindOfShape()](interfaceGEOM_1_1GEOM__IMeasureOperations.md#a6698d180046e2053020ecd2cdbb1b27a) operation.

### GetTick()

```python
long GetTick() inherited
```

Get value of a modification counter of the object.

### SetStudyEntry()

```python
void SetStudyEntry(in string theEntry) inherited
```

Set a Study entry where this object was published.

### GetStudyEntry()

```python
string GetStudyEntry() inherited
```

Get a Study entry where this object was published.

### GetDependency()

```python
ListOfGBO GetDependency() inherited
```

Get a list of all [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) on which were the arguments when this object was constructed and modified.

Note
:   This method is supposed to be used by GUI only.

### GetLastDependency()

```python
ListOfGBO GetLastDependency() inherited
```

Get a list of [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) on which the last function that created or modified the object depends.

Note
:   This method is supposed to be used by GUI only.

### IsShape()

```python
boolean IsShape() inherited
```

### IsSame()

```python
boolean IsSame(in GEOM_BaseObject other) inherited
```

### SetParameters()

```python
void SetParameters(in string theParameters) inherited
```

Set list of parameters

Parameters
:   |  |  |
    | --- | --- |
    | theParameters | is a string containing the notebook variables separated by ":" symbol, used for object creation |

### GetParameters()

```python
string GetParameters() inherited
```

Return list of notebook variables used for object creation separated by ":" symbol.

### GetCreationInformation()

```python
CreationInformationSeq GetCreationInformation() inherited
```

Return name of operation and values of parameters used for object creation.

### GetGen()

```python
GEOM_Gen GetGen() inherited
```

Return the engine creating this object.
