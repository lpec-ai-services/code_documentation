<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__IInsertOperations.html -->

# GEOM_IInsertOperations Interface Reference

Interface for shape insert operations (like copy, import).
[More...](interfaceGEOM_1_1GEOM__IInsertOperations.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for shape insert operations (like copy, import).

## Member Typedef Documentation

### ListOfTransferDatum

```python
typedef sequence< TransferDatum > ListOfTransferDatum
```

Sequence of non-topological information transfer data.

## Member Function Documentation

### MakeCopy()

```python
GEOM_Object MakeCopy(in GEOM_Object theOriginal)
```

Create a copy of the given object.

### Export()

```python
void Export(in GEOM_Object theObject, in string theFileName, in string theFormatName)
```

Deprecated method. Use Export<FormatName> (from the corresponding plugin) instead; here <FormatName> is a name of format.

Export the given shape into a file with given name.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be stored in the file. |
    | theFileName | Name of the file to store the given shape in. |
    | theFormatName | Specify format for the shape storage. |

### ImportFile()

```python
ListOfGBO ImportFile(in string theFileName, in string theFormatName)
```

Deprecated method. Use Import<FormatName> (from the corresponding plugin) instead; here <FormatName> is a name of format.

Import a shape from the STL, BREP, IGES or STEP file (depends on given format) with given name.

Parameters
:   |  |  |
    | --- | --- |
    | theFileName | The file, containing the shape. |
    | theFormatName | Specify format for the file reading. If format 'IGES_SCALE' is used instead of 'IGES' or format 'STEP_SCALE' is used instead of 'STEP', file length unit will be ignored (set to 'meter') and result model will be scaled. |

Returns
:   List of [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created shape and groups of materials.

### ReadValue()

```python
string ReadValue(in string theFileName, in string theFormatName, in string theParameterName)
```

Deprecated method. Use ReadValue (from the corresponding plugin) instead.

Read a value of parameter from a file, containing a shape.

Parameters
:   |  |  |
    | --- | --- |
    | theFileName | The file, containing the shape. |
    | theFormatName | Specify format for the file reading. |
    | theParameterName | Specify the parameter. For example, pass "LEN_UNITS" to obtain length units, in which the file is written. |

Returns
:   Value of requested parameter in form of text string.

### RestoreShape()

```python
GEOM_Object RestoreShape(in SALOMEDS::TMPFile theStream)
```

Read a shape from the binary stream, containing its bounding representation (BRep).

Note
:   [GEOM_Object::GetShapeStream()](interfaceGEOM_1_1GEOM__Object.md#ab9d9b65c86d4df378bccacb6dee91362) method can be used to obtain the shape's BRep stream.

Parameters
:   |  |  |
    | --- | --- |
    | theStream | The BRep binary stream. |

Returns
:   New [GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the shape, read from theStream.

### LoadTexture()

```python
long LoadTexture(in string theTextureFile)
```

Load texture from file.

Parameters
:   |  |  |
    | --- | --- |
    | theTextureFile | texture file name |

Returns
:   unique texture identifier

### AddTexture()

```python
long AddTexture(in long theWidth, in long theHeight, in SALOMEDS::TMPFile theTexture)
```

Add texture to the study.

Parameters
:   |  |  |
    | --- | --- |
    | theWidth | texture width in pixels |
    | theHeight | texture height in pixels |
    | theTexture | texture byte array |

Returns
:   unique texture identifier

### GetTexture()

```python
SALOMEDS::TMPFile GetTexture(in long theID, out long theWidth, out long theHeight)
```

Get previously loaded texture data.

Parameters
:   |  |  |
    | --- | --- |
    | theID | texture identifier |
    | theWidth | texture width in pixels |
    | theHeight | texture height in pixels |

Returns
:   texture byte array

### GetAllTextures()

```python
ListOfLong GetAllTextures()
```

Get list of all available texture IDs.

Returns
:   list of all texture IDs available for the current study

### TransferData()

```python
boolean TransferData(in GEOM_Object theObjectFrom, in GEOM_Object theObjectTo, in find_shape_method theFindMethod, out ListOfTransferDatum theResult)
```

Transfer non-topological data from one object to another.

Parameters
:   |  |  |
    | --- | --- |
    | theObjectFrom | the source object of non-topological data |
    | theObjectTo | the destination object of non-topological data |
    | theFindMethod | method to search sub-shapes of theObjectFrom in shape theObjectTo. Possible values are: [GEOM::FSM_GetInPlace](namespaceGEOM.md#a4d764798e5127e57ed43bd2da68a613ea8d5ebcfdf2f81affbc89309f798413dd), [GEOM::FSM_GetInPlaceByHistory](namespaceGEOM.md#a4d764798e5127e57ed43bd2da68a613ea0ff71cf4eaee66c013d024c80f860474) and [GEOM::FSM_GetInPlace_Old](namespaceGEOM.md#a4d764798e5127e57ed43bd2da68a613ea05095964f7d9393ee01e934419c2509e). Other values of [GEOM::find_shape_method](namespaceGEOM.md#a4d764798e5127e57ed43bd2da68a613e) are not supported. |
    | theResult | statistics of the operation. Output parameter. It represents a sequence of Transfer Datum. A datum has the type (string code), the total number of items of this type and the number of transferred items. |

Returns
:   true in case of success; otherwise false.

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
