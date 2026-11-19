<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__ITestOperations.html -->

# GEOM_ITestOperations Interface Reference

Interface for testing operations.
[More...](interfaceGEOM_1_1GEOM__ITestOperations.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for testing operations.

## Member Function Documentation

### Tesselate()

```python
boolean Tesselate(in GEOM_Object shape, in double linearDeflection, in boolean isRelative, in double angularDeflection)
```

Build a mesh on the given shape.

Parameters
:   |  |  |
    | --- | --- |
    | shape | is a source object |
    | linearDeflection | is a linear deflection |
    | isRelative | says if given value of deflection is relative to shape's bounding box |
    | angularDeflection | is an angular deflection for edges in radians |

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
