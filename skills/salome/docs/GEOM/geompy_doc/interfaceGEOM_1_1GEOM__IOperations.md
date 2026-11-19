<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__IOperations.html -->

# GEOM_IOperations Interface Reference

Basic methods of all geometric operations.
[More...](interfaceGEOM_1_1GEOM__IOperations.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Basic methods of all geometric operations.

## Member Function Documentation

### IsDone()

```python
boolean IsDone()
```

To know, if the operation was successfully performed.

### SetErrorCode()

```python
void SetErrorCode(in string theErrorID)
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
string GetErrorCode()
```

Get the operation error code.

### StartOperation()

```python
void StartOperation()
```

Opens a new transaction.

### FinishOperation()

```python
void FinishOperation()
```

Closes the previously opened transaction.

### AbortOperation()

```python
void AbortOperation()
```

Aborts the previously opened transaction.
