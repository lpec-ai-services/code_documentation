<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1ISTLOperations.html -->

# ISTLOperations Interface Reference

Interface for STLPlugin modeling functions.
[More...](interfaceGEOM_1_1ISTLOperations.md#details)

`import"STLPlugin.idl";`

## Detailed Description

Interface for STLPlugin modeling functions.

## Member Function Documentation

### ExportSTL()

```python
void ExportSTL(in GEOM::GEOM_Object theObject, in string theFileName, in boolean theIsASCII, in double theDeflection, in boolean theIsRelative)
```

Export the given shape into a file with given name in STL format.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be stored in the file. |
    | theFileName | Name of the file to store the given shape in. |
    | theIsASCII | The format of the exported file (ASCII or Binary). |
    | theDeflection | Deflection of the given shape. |
    | theIsRelative | Mode for writing the file. If True (default value), the deflection is calculated from the relative size of the shape; if False, the user defined deflection is used. |

### ImportSTL()

```python
GEOM::ListOfGO ImportSTL(in string theFileName)
```

Import a shape from the STL file.

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
