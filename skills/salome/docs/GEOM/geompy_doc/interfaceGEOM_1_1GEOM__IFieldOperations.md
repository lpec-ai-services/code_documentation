<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__IFieldOperations.html -->

# GEOM_IFieldOperations Interface Reference

Interface for field operation.
[More...](interfaceGEOM_1_1GEOM__IFieldOperations.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for field operation.

## Member Function Documentation

### CreateField()

```python
GEOM_Field CreateField(in GEOM_Object shape, in string name, in field_data_type type, in short dimension, in string_array componentNames)
```

Creates a field.

### CountFields()

```python
long CountFields(in GEOM_Object shape)
```

Returns number of fields on a shape.

### GetFields()

```python
ListOfFields GetFields(in GEOM_Object shape)
```

Returns all fields on a shape.

### GetField()

```python
GEOM_Field GetField(in GEOM_Object shape, in string name)
```

Returns a field on a shape by its name.

### GetNbSubShapes()

```python
long GetNbSubShapes(in GEOM_Object shape, in short fieldDim)
```

Returns number of sub-shapes of given dimension.

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
