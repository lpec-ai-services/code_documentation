<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__Gen.html -->

# GEOM_Gen Interface Reference

Interface to access other [GEOM](namespaceGEOM.md) interfaces.
[More...](interfaceGEOM_1_1GEOM__Gen.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface to access other [GEOM](namespaceGEOM.md) interfaces.

Also contains some methods to access and manage [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md).

## Member Function Documentation

### Undo()

```python
void Undo()
```

Undo/Redo Management.

### Redo()

```python
void Redo()
```

### AddInStudy()

```python
SALOMEDS::SObject AddInStudy(in GEOM_BaseObject theObject, in string theName, in GEOM_BaseObject theFather)
```

Publishing management.

Adds in theStudy a object theObject under with a name theName, if theFather is not NULL the object is placed under thFather's SObject. Returns a SObject where theObject is placed

### RestoreSubShapesO()

```python
ListOfGO RestoreSubShapesO(in GEOM_Object theObject, in ListOfGO theArgs, in find_shape_method theFindMethod, in boolean theInheritFirstArg, in boolean theAddPrefix)
```

Publish sub-shapes, standing for arguments and sub-shapes of arguments.

To be used from python scripts out of geompy.addToStudy (non-default usage)

Parameters
:   |  |  |
    | --- | --- |
    | theObject | published [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), arguments of which will be published |
    | theArgs | list of [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), operation arguments to be published. If this list is empty, all operation arguments will be published |
    | theFindMethod | method to search sub-shapes, corresponding to arguments and their sub-shapes. Value from enumeration [GEOM::find_shape_method](namespaceGEOM.md#a4d764798e5127e57ed43bd2da68a613e). |
    | theInheritFirstArg | set properties of the first argument for *theObject*. Do not publish sub-shapes in place of arguments, but only in place of sub-shapes of the first argument, because the whole shape corresponds to the first argument. Mainly to be used after transformations, but it also can be useful after partition with one object shape, and some other operations, where only the first argument has to be considered. If theObject has only one argument shape, this flag is automatically considered as True, not regarding really passed value. |
    | theAddPrefix | add prefix "from_" to names of restored sub-shapes, and prefix "from_subshapes_of_" to names of partially restored sub-shapes. |

Returns
:   list of published sub-shapes

### RestoreGivenSubShapesO()

```python
ListOfGO RestoreGivenSubShapesO(in GEOM_Object theObject, in ListOfGO theArgs, in find_shape_method theFindMethod, in boolean theInheritFirstArg, in boolean theAddPrefix)
```

Publish sub-shapes, standing for arguments and sub-shapes of arguments.

To be used from python scripts out of geompy.addToStudy (non-default usage)

Parameters
:   |  |  |
    | --- | --- |
    | theObject | published [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), arguments of which will be published |
    | theArgs | list of [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), operation arguments to be published. If this list is empty, all operation arguments will be published |
    | theFindMethod | method to search sub-shapes, corresponding to arguments and their sub-shapes. Value from enumeration [GEOM::find_shape_method](namespaceGEOM.md#a4d764798e5127e57ed43bd2da68a613e). |
    | theInheritFirstArg | set properties of the first argument for *theObject*. Do not publish sub-shapes in place of arguments, but only in place of sub-shapes of the first argument, because the whole shape corresponds to the first argument. Mainly to be used after transformations, but it also can be useful after partition with one object shape, and some other operations, where only the first argument has to be considered. If theObject has only one argument shape, this flag is automatically considered as True, not regarding really passed value. |
    | theAddPrefix | add prefix "from_" to names of restored sub-shapes, and prefix "from_subshapes_of_" to names of partially restored sub-shapes. |

Returns
:   list of published sub-shapes

### RestoreSubShapesSO()

```python
ListOfGO RestoreSubShapesSO(in SALOMEDS::SObject theSObject, in ListOfGO theArgs, in find_shape_method theFindMethod, in boolean theInheritFirstArg, in boolean theAddPrefix)
```

Publish sub-shapes, standing for arguments and sub-shapes of arguments.

To be used from GUI and from geompy.addToStudy. Work like the above method, but accepts study object theSObject instead of [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md).

Parameters
:   |  |  |
    | --- | --- |
    | theSObject | study object, referencing [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), arguments of which will be published |
    | theArgs | list of [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), operation arguments to be published. If this list is empty, all operation arguments will be published |
    | theFindMethod | method to search sub-shapes, corresponding to arguments and their sub-shapes. Value from enumeration [GEOM::find_shape_method](namespaceGEOM.md#a4d764798e5127e57ed43bd2da68a613e). |
    | theInheritFirstArg | set properties of the first argument for *theObject*. Do not publish sub-shapes in place of arguments, but only in place of sub-shapes of the first argument, because the whole shape corresponds to the first argument. Mainly to be used after transformations, but it also can be useful after partition with one object shape, and some other operations, where only the first argument has to be considered. If theObject has only one argument shape, this flag is automatically considered as True, not regarding really passed value. |
    | theAddPrefix | add prefix "from_" to names of restored sub-shapes, and prefix "from_subshapes_of_" to names of partially restored sub-shapes. |

### GetIBasicOperations()

```python
GEOM_IBasicOperations GetIBasicOperations() raises(SALOME::SALOME_Exception)
```

### GetITransformOperations()

```python
GEOM_ITransformOperations GetITransformOperations() raises(SALOME::SALOME_Exception)
```

### GetI3DPrimOperations()

```python
GEOM_I3DPrimOperations GetI3DPrimOperations() raises(SALOME::SALOME_Exception)
```

### GetIShapesOperations()

```python
GEOM_IShapesOperations GetIShapesOperations() raises(SALOME::SALOME_Exception)
```

### GetIBooleanOperations()

```python
GEOM_IBooleanOperations GetIBooleanOperations() raises(SALOME::SALOME_Exception)
```

### GetICurvesOperations()

```python
GEOM_ICurvesOperations GetICurvesOperations() raises(SALOME::SALOME_Exception)
```

### GetILocalOperations()

```python
GEOM_ILocalOperations GetILocalOperations() raises(SALOME::SALOME_Exception)
```

### GetIHealingOperations()

```python
GEOM_IHealingOperations GetIHealingOperations() raises(SALOME::SALOME_Exception)
```

### GetIInsertOperations()

```python
GEOM_IInsertOperations GetIInsertOperations() raises(SALOME::SALOME_Exception)
```

### GetIMeasureOperations()

```python
GEOM_IMeasureOperations GetIMeasureOperations() raises(SALOME::SALOME_Exception)
```

### GetIBlocksOperations()

```python
GEOM_IBlocksOperations GetIBlocksOperations() raises(SALOME::SALOME_Exception)
```

### GetIGroupOperations()

```python
GEOM_IGroupOperations GetIGroupOperations() raises(SALOME::SALOME_Exception)
```

### GetIFieldOperations()

```python
GEOM_IFieldOperations GetIFieldOperations() raises(SALOME::SALOME_Exception)
```

### GetITestOperations()

```python
GEOM_ITestOperations GetITestOperations() raises(SALOME::SALOME_Exception)
```

### GetICanonicalRecognition()

```python
GEOM_ICanonicalRecognition GetICanonicalRecognition() raises(SALOME::SALOME_Exception)
```

### GetPluginOperations()

```python
GEOM_IOperations GetPluginOperations(in string theLibName) raises(SALOME::SALOME_Exception)
```

### RemoveObject()

```python
void RemoveObject(in GEOM_BaseObject theObject)
```

Removes the object from the [GEOM](namespaceGEOM.md) component.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | is a [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) to be removed |

### GetObject()

```python
GEOM_BaseObject GetObject(in string theEntry)
```

Returns an object defined by the study and its entry in the [GEOM](namespaceGEOM.md) component.

Parameters
:   |  |  |
    | --- | --- |
    | theEntry | is an entry of the requested [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) in the [GEOM](namespaceGEOM.md) component |

Note
:   if the object has not previously been created a NULL [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) is returned

### AddSubShape()

```python
GEOM_Object AddSubShape(in GEOM_Object theMainShape, in ListOfLong theIndices)
```

Add a sub-shape defined by indices in *theIndices* (contains unique IDs of sub-shapes inside *theMainShape*)

Note
:   The sub-shape [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) can has ONLY ONE function. Don't try to apply modification operations on them.
:   Internal method

### GetIORFromString()

```python
GEOM_Object GetIORFromString(in string theIOR)
```

Returns a [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) defined by its IOR.

Parameters
:   |  |  |
    | --- | --- |
    | theIOR | a string containing an IOR of the requested [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) |

### GetStringFromIOR()

```python
string GetStringFromIOR(in GEOM_Object theObject)
```

Returns a string which contains an IOR of the [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md).

Parameters
:   |  |  |
    | --- | --- |
    | theObject | is a [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) which IOR is requested |

### GetDumpName()

```python
string GetDumpName(in string theStudyEntry)
```

Returns a name with which a [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) was dumped into python script.

Parameters
:   |  |  |
    | --- | --- |
    | theStudyEntry | is an entry of the [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) in the study |

### GetAllDumpNames()

```python
string_array GetAllDumpNames()
```

Returns all names with which a [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md) was dumped into python script to avoid the same names in SMESH script.

### PublishNamedShapesInStudy()

```python
ListOfGO PublishNamedShapesInStudy(in Object theObject)
```

Publishes the named sub-shapes of given object in the study.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | The object which named sub-shapes are published |

### CreateFolder()

```python
SALOMEDS::SObject CreateFolder(in string theName, in SALOMEDS::SObject theFather)
```

Creates a new folder.

Creates a new container (folder) for any [GEOM](namespaceGEOM.md) objects. Folder will have name theName. If theFather is not NULL, the folder is placed under theFather object. Otherwise, the folder takes place under root 'Geometry' object.

Parameters
:   |  |  |
    | --- | --- |
    | theName | name of the folder |
    | theFather | parent object |

Returns
:   SObject represented the created folder.

### MoveToFolder()

```python
void MoveToFolder(in GEOM_Object theObject, in SALOMEDS::SObject theFolder)
```

Moves object to the specified folder.

The moved object should be first published in the study.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | [GEOM](namespaceGEOM.md) object to move |
    | theFolder | target folder |

### MoveListToFolder()

```python
void MoveListToFolder(in ListOfGO theListOfGO, in SALOMEDS::SObject theFolder)
```

Moves list of objects to the specified folder.

The moved objects should be first published in the study.

Parameters
:   |  |  |
    | --- | --- |
    | theListOfGO | list of [GEOM](namespaceGEOM.md) objects to move |
    | theFolder | target folder |

### Move()

```python
void Move(in object_list what, in SALOMEDS::SObject where, in long row)
```

Moves objects to the specified position.

This function is used in the drag-n-drop functionality.

Parameters
:   |  |  |
    | --- | --- |
    | what | objects being moved |
    | where | parent object where objects are moved to |
    | row | position in the parent object's children list at which objects are moved |

### GetDependencyTree()

```python
SALOMEDS::TMPFile GetDependencyTree(in string_array theListOfEntries)
```

Collects dependencies of the given objects from other ones.

Parameters
:   |  |  |
    | --- | --- |
    | theListOfEntries | List of [GEOM](namespaceGEOM.md) object entries in OCAF tree (not in study) |

Returns
:   Struct of dependent entries and its links as a byte array

Note
:   This method is supposed to be used by GUI only.

### GetEntriesToReduceStudy()

```python
void GetEntriesToReduceStudy(inout string_array theSelectedEntries, inout string_array theParentEntries, inout string_array theSubEntries, inout string_array theOtherEntries)
```

Fills 3 lists that is used to reduce study of redundant objects:

- dependencies of the given objects from other ones;
- children of the given objects;
- all other objects in study.

  Parameters
  :   |  |  |
      | --- | --- |
      | theSelectedEntries | List of [GEOM](namespaceGEOM.md) object entries in OCAF tree |
      | theParentEntries | List of [GEOM](namespaceGEOM.md) object entries on which the given objects depend |
      | theSubEntries | Children entries list of the given objects |
      | theOtherEntries | List of [GEOM](namespaceGEOM.md) object entries which are in the study, but not in parents and children lists |

  Note
  :   This method is supposed to be used by GUI only.

### BreakLink()

```python
void BreakLink(in string theEntry)
```
