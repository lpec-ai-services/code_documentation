<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1IVTKOperations.html -->

# IVTKOperations Interface Reference

Interface for VTKPlugin modeling functions.
[More...](interfaceGEOM_1_1IVTKOperations.md#details)

`import"VTKPlugin.idl";`

## Detailed Description

Interface for VTKPlugin modeling functions.

## Member Function Documentation

### ExportVTK()

```python
void ExportVTK(in GEOM::GEOM_Object theObject, in string theFileName, in double theDeflection)
```

Export the given shape into a file with given name in VTK format.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be stored in the file. |
    | theFileName | Name of the file to store the given shape in. |
    | theDeflection | Deflection of the given shape. |

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
