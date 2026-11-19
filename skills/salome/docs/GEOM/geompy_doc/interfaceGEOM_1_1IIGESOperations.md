<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1IIGESOperations.html -->

# IIGESOperations Interface Reference

Interface for IGESPlugin modeling functions.
[More...](interfaceGEOM_1_1IIGESOperations.md#details)

`import"IGESPlugin.idl";`

## Detailed Description

Interface for IGESPlugin modeling functions.

## Member Function Documentation

### ExportIGES()

```python
void ExportIGES(in GEOM::GEOM_Object theObject, in string theFileName, in string theVersion)
```

Export the given shape into a file with given name in IGES format.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | Shape to be stored in the file. |
    | theFileName | Name of the file to store the given shape in. |
    | theVersion | Version of IGES format which defines, whether to write only faces (5.1 IGES format) or shells and solids also (5.3 IGES format). |

### ImportIGES()

```python
GEOM::ListOfGO ImportIGES(in string theFileName, in boolean theIsIgnoreUnits)
```

Import a shape from the IGES file.

Parameters
:   |  |  |
    | --- | --- |
    | theFileName | The file, containing the shape. |
    | theIsIgnoreUnits | If True, file length units will be ignored (set to 'meter') and result model will be scaled, if its units are not meters. If False (default), file length units will be taken into account. |

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
