<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/namespaceGEOM.html -->

# GEOM Module Reference

## Typedef Documentation

### Parameters

```python
typedef sequence< Parameter > Parameters
```

### CreationInformationSeq

```python
typedef sequence< CreationInformation > CreationInformationSeq
```

### ModifStatistics

```python
typedef sequence< ModifInfo > ModifStatistics
```

### string_array

```python
typedef sequence<string> string_array
```

### short_array

```python
typedef sequence<short> short_array
```

### ListOfBool

```python
typedef sequence<boolean> ListOfBool
```

### ListOfLong

```python
typedef sequence<long> ListOfLong
```

### ListOfDouble

```python
typedef sequence<double> ListOfDouble
```

### ListOfListOfDouble

```python
typedef sequence< ListOfDouble > ListOfListOfDouble
```

### ListOfListOfLong

```python
typedef sequence< ListOfLong > ListOfListOfLong
```

### ListOfGO

```python
typedef sequence< GEOM_Object > ListOfGO
```

### ListOfGBO

```python
typedef sequence< GEOM_BaseObject > ListOfGBO
```

### ListOfFields

```python
typedef sequence< GEOM_Field > ListOfFields
```

### object_list

```python
typedef sequence<SALOMEDS::SObject> object_list
```

## Enumeration Type Documentation

### shape_type

```python
enum shape_type
```

Topological types of shapes (like Open Cascade types)

| Enumerator | |
| --- | --- |
| COMPOUND | A collection of arbitrary shapes |
| COMPSOLID | A collection of solids |
| SOLID | A part of 3D space bound by a shell |
| SHELL | A collection of faces connected by some edges of their wire boundaries |
| FACE | Part of a plane (in 2D geometry) or a surface (in 3D geometry) bounded by a closed wire |
| WIRE | A sequence of edges connected by their vertices |
| EDGE | Edge, a shape corresponding to a curve, and bound by a vertex at each extremity |
| VERTEX | A zero-dimensional shape corresponding to a point in geometry |
| SHAPE | Arbitrary shape in a Compound (used for processing of Compounds in some operations) |
| FLAT | Flat (top-level) contents of a Compound (used for processing of Compounds in some operations) |

### marker_type

```python
enum marker_type
```

Marker type.

| Enumerator | |
| --- | --- |
| MT_NONE |  |
| MT_POINT |  |
| MT_PLUS |  |
| MT_STAR |  |
| MT_X |  |
| MT_O |  |
| MT_O_POINT |  |
| MT_O_PLUS |  |
| MT_O_STAR |  |
| MT_O_X |  |
| MT_RING1 |  |
| MT_RING2 |  |
| MT_RING3 |  |
| MT_BALL |  |
| MT_USER |  |

### marker_size

```python
enum marker_size
```

/brief Marker size

| Enumerator | |
| --- | --- |
| MS_NONE |  |
| MS_10 |  |
| MS_15 |  |
| MS_20 |  |
| MS_25 |  |
| MS_30 |  |
| MS_35 |  |
| MS_40 |  |
| MS_45 |  |
| MS_50 |  |
| MS_55 |  |
| MS_60 |  |
| MS_65 |  |
| MS_70 |  |

### shape_state

```python
enum shape_state
```

State of shape relatively geometrical surface like plane, sphere or cylinder.

Is used in functions GEOM_IShapesOperations.GetShapesOn<xxx>()

| Enumerator | |
| --- | --- |
| ST_ON | Shape is on surface |
| ST_OUT | Shape is in the direction defined by the normal and not on surface. For plane it means above the plane, For sphere and cylinder it means outside of volume, bounded by the surface. |
| ST_ONOUT | Shape is in the direction defined by the normal and on surface. ONOUT = ON || OUT |
| ST_IN | Complementary to ONOUT. For plane it means below the plane, For sphere and cylinder it means inside the volume, bounded by the surface (beyond axis and surface for cylinder and beyond cented and surface for sphere). |
| ST_ONIN | Complementary to OUT. ONIN = ON || IN |

### find_shape_method

```python
enum find_shape_method
```

Kind of method to find inside one main shape some sub-shapes, corresponding to other given shape (its argument)

Is used in functions [GEOM_Gen.RestoreSubShapesO()](interfaceGEOM_1_1GEOM__Gen.md#a5865402d9f5f6aab75e1e04801382776), [GEOM_Gen.RestoreSubShapesSO()](interfaceGEOM_1_1GEOM__Gen.md#a9890e5a2571ec19def1e6bff707edd92), TransferNames()

| Enumerator | |
| --- | --- |
| FSM_GetInPlace | Use GetInPlace functionality. Suits all cases, except transformations |
| FSM_Transformed | To be used only for transformation result, to find sub-shapes of argument. Only this method can be used after transformation. |
| FSM_GetSame | To find only shared sub-shapes, not modified by the operation |
| FSM_GetShapesOnShape | Use GetShapesOnShape method (can work only on solids) |
| FSM_GetInPlaceByHistory | Use GetInPlaceByHistory method (can work only after Partition) |
| FSM_MultiTransformed | To be used only for multi-transformation result. Only this method can be used after multi-transformation. |
| FSM_GetInPlace_Old | Use old GetInPlace functionality. |

### filling_oper_method

```python
enum filling_oper_method
```

Kind of method to perform filling operation.

Is used in functions [GEOM_I3DPrimOperations.MakeFilling()](interfaceGEOM_1_1GEOM__I3DPrimOperations.md#a3912e4d744f5f66d2fd0e3674eaadc48)

| Enumerator | |
| --- | --- |
| FOM_Default | Default (standard behaviour) |
| FOM_UseOri | Use edges orientation - orientation of edges is used: if the edge is reversed, the curve from this edge is reversed before using it in the filling algorithm. |
| FOM_AutoCorrect | Auto-correct edges orientation - changes the orientation of the curves using minimization of sum of distances between the end points of the edges. |

### curve_type

```python
enum curve_type
```

Kind of the curves.

Used in the functions [GEOM_ICurvesOperations.MakeCurveParametric()](interfaceGEOM_1_1GEOM__ICurvesOperations.md#ac07f0d7225db4594ad01b0b88c844629), [GEOM_ICurvesOperations.MakeCurveParametricNew()](interfaceGEOM_1_1GEOM__ICurvesOperations.md#ac851a93c8012f56f9a20dfbe0a388a34), [GEOM_ICurvesOperations.MakePolyline2D](interfaceGEOM_1_1GEOM__ICurvesOperations.md#af8c8180d37fdd09dfb29a26ca5ce9871), [GEOM_ICurvesOperations.MakePolyline2DOnPlane](interfaceGEOM_1_1GEOM__ICurvesOperations.md#ad9b82435674ac6c855b355f97d2a9268).

| Enumerator | |
| --- | --- |
| Polyline | Polyline curve |
| Bezier | Bezier curve |
| Interpolation | Interpolation, curve |

### field_data_type

```python
enum field_data_type
```

Type of field data.

| Enumerator | |
| --- | --- |
| FDT_Bool |  |
| FDT_Int |  |
| FDT_Double |  |
| FDT_String |  |

### si_check_level

```python
enum si_check_level
```

This enumeration represents the level of checking shape on self-interference.

It defines which interferferences will be checked.

| Enumerator | |
| --- | --- |
| SI_V_V |  |
| SI_V_E |  |
| SI_E_E |  |
| SI_V_F |  |
| SI_E_F |  |
| SI_ALL |  |

### comparison_condition

```python
enum comparison_condition
```

This enumeration represents comparison conditions.

| Enumerator | |
| --- | --- |
| CC_GT | Greater then. |
| CC_GE | Greater then or equal to. |
| CC_LT | Less then. |
| CC_LE | Less then or equal to. |

### wire_build_mode

```python
enum wire_build_mode
```

Wire construction mode. Regulates the way gaps are closed.

Is used in function [GEOM_IShapesOperations.MakeWire()](interfaceGEOM_1_1GEOM__IShapesOperations.md#a3b98993685ef9ee3f119e5d6f11df633)

| Enumerator | |
| --- | --- |
| WBM_FixTolerance | Do not change curves, just enlarge wire tolerance to cover the gaps |
| WBM_Approximation | Replace curves, neighbour to the gap, with BSplines, connecting in the middle of the gap |
| WBM_KeepCurveType | Replace curves, neighbour to the gap, with new curves of the same type and close parameters, connecting in the middle of the gap |

### length_unit

```python
enum length_unit
```

Units of length.

| Enumerator | |
| --- | --- |
| LU_INCH |  |
| LU_MILLIMETER |  |
| LU_FOOT |  |
| LU_MILE |  |
| LU_METER |  |
| LU_KILOMETER |  |
| LU_MILLIINCH |  |
| LU_MICROMETER |  |
| LU_CENTIMETER |  |
| LU_MICROINCH |  |
