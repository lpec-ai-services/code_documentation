<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/interfaceGEOM_1_1GEOM__ICanonicalRecognition.html -->

# GEOM_ICanonicalRecognition Interface Reference

Interface for canonical recognition operations.
[More...](interfaceGEOM_1_1GEOM__ICanonicalRecognition.md#details)

`import"GEOM_Gen.idl";`

## Detailed Description

Interface for canonical recognition operations.

## Member Function Documentation

### isPlane()

```python
boolean isPlane(in GEOM_Object shape, in double tolerance, inout ListOfDouble normal, inout ListOfDouble origin)
```

check if the shape is planar

### isSphere()

```python
boolean isSphere(in GEOM_Object shape, in double tolerance, inout ListOfDouble origin, inout double radius)
```

check if shape is spherical

### isCone()

```python
boolean isCone(in GEOM_Object shape, in double tolerance, inout ListOfDouble axis, inout ListOfDouble apex, inout double halfAngle)
```

check if shape is conical

### isCylinder()

```python
boolean isCylinder(in GEOM_Object shape, in double tolerance, inout ListOfDouble axis, inout ListOfDouble origin, inout double radius)
```

check if shape is cylinder

### isLine()

```python
boolean isLine(in GEOM_Object edge, in double tolerance, inout ListOfDouble direction, inout ListOfDouble origin)
```

check if edge / wire is line

### isCircle()

```python
boolean isCircle(in GEOM_Object edge, in double tolerance, inout ListOfDouble normal, inout ListOfDouble origin, inout double radius)
```

check if edge / wire is circle

### isEllipse()

```python
boolean isEllipse(in GEOM_Object edge, in double tolerance, inout ListOfDouble normal, inout ListOfDouble dirX, inout ListOfDouble origin, inout double majorRadius, inout double minorRadius)
```

check if edge / wire is ellipse

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
