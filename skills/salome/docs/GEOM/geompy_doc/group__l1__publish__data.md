<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l1__publish__data.html -->

# Publishing results in SALOME study geomBuilder Python module

## Detailed Description

## Function Documentation

### addToStudyAuto()

```python
def addToStudyAuto(self, maxNbSubShapes = -1)
```

Enable / disable results auto-publishing.

The automatic publishing is managed in the following way:

- if *maxNbSubShapes* = 0, automatic publishing is disabled.
- if *maxNbSubShapes* = -1 (default), automatic publishing is enabled and maximum number of sub-shapes allowed for publishing is unlimited; any negative value passed as parameter has the same effect.
- if *maxNbSubShapes* is any positive value, automatic publishing is enabled and maximum number of sub-shapes allowed for publishing is set to specified value.

Parameters
:   |  |  |
    | --- | --- |
    | maxNbSubShapes | maximum number of sub-shapes allowed for publishing. |

### addToStudy()

```python
def addToStudy(self, aShape, aName, doRestoreSubShapes = False, theArgs = [], theFindMethod = GEOM.FSM_GetInPlace, theInheritFirstArg = False)
```

Publish in study aShape with name aName.

Parameters
:   |  |  |
    | --- | --- |
    | aShape | the shape to be published |
    | aName | the name for the shape |
    | doRestoreSubShapes | if True, finds and publishes also sub-shapes of *aShape*, corresponding to its arguments and published sub-shapes of arguments |
    | theArgs,theFindMethod,theInheritFirstArg | see [RestoreSubShapes()](group__l3__restore__ss.md#gac09e38fdc5d1c4f18d59fba5c7be31b5) for these arguments description |

Returns
:   study entry of the published shape in form of string

[Example](../tui_test_all_page.md#swig_all_addtostudy)

### addToStudyInFather()

```python
def addToStudyInFather(self, aFather, aShape, aName)
```

Publish in study aShape with name aName as sub-object of previously published aFather.

Parameters
:   |  |  |
    | --- | --- |
    | aFather | previously published object |
    | aShape | the shape to be published as sub-object of *aFather* |
    | aName | the name for the shape |

Returns
:   study entry of the published shape in form of string

[Example](../tui_test_all_page.md#swig_all_addtostudyInFather)

### NewFolder()

```python
def NewFolder(self, Name, Father = None)
```

Creates a new folder object.

It is a container for any [GEOM](namespaceGEOM.md) objects.

Parameters
:   |  |  |
    | --- | --- |
    | Name | name of the container |
    | Father | parent object. If None, folder under 'Geometry' root object will be created. |

Returns
:   a new created folder

### PutToFolder()

```python
def PutToFolder(self, Object, Folder)
```

Move object to the specified folder.

Parameters
:   |  |  |
    | --- | --- |
    | Object | object to move |
    | Folder | target folder |

### PutListToFolder()

```python
def PutListToFolder(self, ListOfSO, Folder)
```

Move list of objects to the specified folder.

Parameters
:   |  |  |
    | --- | --- |
    | ListOfSO | list of objects to move |
    | Folder | target folder |
