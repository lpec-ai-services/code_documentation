<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__IntFieldStep.html -->

# GEOM_IntFieldStep Interface Reference

Interface of the integer field time step.
[More...](interfaceGEOM_1_1GEOM__IntFieldStep.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface of the integer field time step.

## Member Function Documentation

### SetValues()

```python
boolean SetValues(in ListOfLong intValues)
```

Changes values of the field step. Returns false if number of values is wrong.

### GetValues()

```python
ListOfLong GetValues()
```

Returns values of the field step.

### SetStamp()

```python
void SetStamp(in long stamp) inherited
```

Changes the time of the field step.

### GetStamp()

```python
long GetStamp() inherited
```

Returns the time of the field step.

### GetID()

```python
long GetID() inherited
```

Returns the number of the field step.

### GetField()

```python
GEOM_Field GetField() inherited
```

Returns the field the step belongs to.

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
