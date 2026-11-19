<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__BaseObject.html -->

# GEOM_BaseObject Interface Reference

A common root of objects in [GEOM](namespaceGEOM.md) module.
[More...](interfaceGEOM_1_1GEOM__BaseObject.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

A common root of objects in [GEOM](namespaceGEOM.md) module.

## Member Function Documentation

### SetName()

```python
void SetName(in string theName)
```

Set name of the object.

Parameters
:   |  |  |
    | --- | --- |
    | theName | is a name which will be associated with this object. |

### GetName()

```python
string GetName()
```

Get name of the object associated with this object.

### GetEntry()

```python
string GetEntry()
```

Get internal (unique) entry of the object in the [GEOM](namespaceGEOM.md) component's data tree.

Note
:   This is not an entry of the data object in SALOME study. This is internal function of [GEOM](namespaceGEOM.md) component, though it can be used outside it for appropriate reason (e.g. for unique identification of geometry object).

### GetType()

```python
long GetType()
```

Get internal type of operation created this object (POINT, BOX, CYLINDER, EXTRUSION...).

Note
:   To get topological information on the object, use [WhatIs()](interfaceGEOM_1_1GEOM__IMeasureOperations.md#af1e211e4fa6f02d4ef64fcecbc52b36a) or [KindOfShape()](interfaceGEOM_1_1GEOM__IMeasureOperations.md#a6698d180046e2053020ecd2cdbb1b27a) operation.

### GetTick()

```python
long GetTick()
```

Get value of a modification counter of the object.

### SetStudyEntry()

```python
void SetStudyEntry(in string theEntry)
```

Set a Study entry where this object was published.

### GetStudyEntry()

```python
string GetStudyEntry()
```

Get a Study entry where this object was published.

### GetDependency()

```python
ListOfGBO GetDependency()
```

Get a list of all [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) on which were the arguments when this object was constructed and modified.

Note
:   This method is supposed to be used by GUI only.

### GetLastDependency()

```python
ListOfGBO GetLastDependency()
```

Get a list of [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) on which the last function that created or modified the object depends.

Note
:   This method is supposed to be used by GUI only.

### IsShape()

```python
boolean IsShape()
```

### IsSame()

```python
boolean IsSame(in GEOM_BaseObject other)
```

### SetParameters()

```python
void SetParameters(in string theParameters)
```

Set list of parameters

Parameters
:   |  |  |
    | --- | --- |
    | theParameters | is a string containing the notebook variables separated by ":" symbol, used for object creation |

### GetParameters()

```python
string GetParameters()
```

Return list of notebook variables used for object creation separated by ":" symbol.

### GetCreationInformation()

```python
CreationInformationSeq GetCreationInformation()
```

Return name of operation and values of parameters used for object creation.

### GetGen()

```python
GEOM_Gen GetGen()
```

Return the engine creating this object.
