<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1IBREPOperations.html -->

# IBREPOperations Interface Reference

Interface for BREPPlugin modeling functions.
[More...](interfaceGEOM_1_1IBREPOperations.md#details)

`import"BREPPlugin.idl";`

## Detailed Description

Interface for BREPPlugin modeling functions.

## Member Function Documentation

### ExportBREP()

```python
void ExportBREP(in GEOM::GEOM_Object theObject, in string theFileName)
```

Export the given shape into a file with given name in BREP format.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be stored in the file. |
    | theFileName | Name of the file to store the given shape in. |

### ImportBREP()

```python
GEOM::ListOfGO ImportBREP(in string theFileName)
```

Import a shape from the BREP file.

Parameters
:   |  |  |
    | --- | --- |
    | theFileName | The file, containing the shape. |

Returns
:   List of GEOM_Objects, containing the created shape and propagation groups.

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
