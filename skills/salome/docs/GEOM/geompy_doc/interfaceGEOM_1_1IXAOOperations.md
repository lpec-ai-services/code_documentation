<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1IXAOOperations.html -->

# IXAOOperations Interface Reference

Interface for XAOPlugin modeling functions.
[More...](interfaceGEOM_1_1IXAOOperations.md#details)

`import"XAOPlugin.idl";`

## Detailed Description

Interface for XAOPlugin modeling functions.

## Member Function Documentation

### ExportXAO()

```python
boolean ExportXAO(in GEOM::GEOM_Object shape, in GEOM::ListOfGO groups, in GEOM::ListOfFields fields, in string author, in string fileName, in string shapeFileName)
```

Export a shape to XAO format

Parameters
:   |  |  |
    | --- | --- |
    | shape | The shape to export |
    | groups | The list of groups to export |
    | fields | The list of fields to export |
    | author | The author of the export |
    | fileName | The name of the file to export |
    | shapeFileName | The name of the file to export the shape in an external file |

Returns
:   boolean indicating if export was successful.

### ExportXAOMem()

```python
SALOMEDS::TMPFile ExportXAOMem(in GEOM::GEOM_Object shape, in GEOM::ListOfGO groups, in GEOM::ListOfFields fields, in string author)
```

Export a shape to XAO format in a byte array

Parameters
:   |  |  |
    | --- | --- |
    | shape | The shape to export |
    | groups | The list of groups to export |
    | fields | The list of fields to export |
    | author | The author of the export |

Returns
:   Byte array with exported data.

### ImportXAO()

```python
boolean ImportXAO(in string fileName, out GEOM::GEOM_Object shape, out GEOM::ListOfGO subShapes, out GEOM::ListOfGO groups, out GEOM::ListOfFields fields)
```

Import a shape from XAO format

Parameters
:   |  |  |
    | --- | --- |
    | fileName | The name of the file to import |
    | shape | The imported shape |
    | subShapes | The list of imported subShapes |
    | groups | The list of imported groups |
    | fields | The list of imported fields |

Returns
:   boolean indicating if import was successful.

### ImportXAOMem()

```python
boolean ImportXAOMem(in SALOMEDS::TMPFile theBuff, out GEOM::GEOM_Object shape, out GEOM::ListOfGO subShapes, out GEOM::ListOfGO groups, out GEOM::ListOfFields fields)
```

Import a shape from XAO format byte array

Parameters
:   |  |  |
    | --- | --- |
    | theBuff | The byte array with data in XAO format |
    | shape | The imported shape |
    | subShapes | The list of imported subShapes |
    | groups | The list of imported groups |
    | fields | The list of imported fields |

Returns
:   boolean indicating if import was successful.

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
