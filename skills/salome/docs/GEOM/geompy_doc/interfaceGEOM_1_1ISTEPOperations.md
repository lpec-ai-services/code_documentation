<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1ISTEPOperations.html -->

# ISTEPOperations Interface Reference

Interface for STEPPlugin modeling functions.
[More...](interfaceGEOM_1_1ISTEPOperations.md#details)

`import"STEPPlugin.idl";`

## Detailed Description

Interface for STEPPlugin modeling functions.

## Member Function Documentation

### ExportSTEP()

```python
void ExportSTEP(in GEOM::GEOM_Object theObject, in string theFileName, in GEOM::length_unit theUnit)
```

Export the given shape into a file with given name in STEP format.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be stored in the file. |
    | theFileName | Name of the file to store the given shape in. |
    | theUnit | the length unit. |

### ImportSTEP()

```python
GEOM::ListOfGO ImportSTEP(in string theFileName, in boolean theIsIgnoreUnits, in boolean IsCreateAssemblies)
```

Import a shape from the STEP file.

Parameters
:   |  |  |
    | --- | --- |
    | theFileName | The file, containing the shape. |
    | theIsIgnoreUnits | If True, file length units will be ignored (set to 'meter') and result model will be scaled, if its units are not meters. If False (default), file length units will be taken into account. |
    | IsCreateAssemblies | If True, for each assembly compound is created in the result. If False Compounds that contain a single shape are eliminated from the result. |

Returns
:   List of GEOM_Objects, containing the created shape and propagation groups.

### ReadValue()

```python
string ReadValue(in string theFileName, in string theParameterName)
```

Read a value of parameter from a file, containing a shape.

Parameters
:   |  |  |
    | --- | --- |
    | theFileName | The file, containing the shape. |
    | theParameterName | Specify the parameter. For example, pass "LEN_UNITS" to obtain length units, in which the file is written. |

Returns
:   Value of requested parameter in form of text string.

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
