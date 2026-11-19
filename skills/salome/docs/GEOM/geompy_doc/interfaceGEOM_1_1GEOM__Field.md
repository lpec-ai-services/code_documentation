<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__Field.html -->

# GEOM_Field Interface Reference

Interface of the field.
[More...](interfaceGEOM_1_1GEOM__Field.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface of the field.

## Member Function Documentation

### GetShape()

```python
GEOM_Object GetShape()
```

Returns the shape the field lies on.

### GetDataType()

```python
field_data_type GetDataType()
```

Returns type of field data.

### GetDimension()

```python
short GetDimension()
```

Returns dimension of the shape the field lies on 0 - VERTEX, 1 - EDGE, 2 - FACE, 3 - SOLID, -1 - whole shape.

### GetComponents()

```python
string_array GetComponents()
```

Returns names of components.

### AddStep()

```python
GEOM_FieldStep AddStep(in long stepID, in long stamp)
```

Removes a component. Component number counts from one.

Adds a time step to the field

### RemoveStep()

```python
void RemoveStep(in long stepID)
```

Remove a time step from the field.

### CountSteps()

```python
long CountSteps()
```

Returns number of time steps in the field.

### GetSteps()

```python
ListOfLong GetSteps()
```

Returns a list of time step IDs in the field.

### GetStep()

```python
GEOM_FieldStep GetStep(in long stepID)
```

Returns a time step by its ID.

### GetArraySize()

```python
long GetArraySize()
```

Returns a size of data array that is to be passed to GEOM_FieldStep.SetValues( dataArray ). This size depends on the number of sub-shapes of field dimension and the number of components.

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
