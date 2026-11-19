<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classgeomBuilder_1_1geomField.html -->

# geomField Class Reference geomBuilder Python module » All package methods, grouped by their purpose » Field on Geometry

Field on Geometry.
[More...](classgeomBuilder_1_1geomField.md#details)

## Detailed Description

Field on Geometry.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, args)
```

## Member Function Documentation

### getShape()

```python
def getShape(self)
```

Returns the shape the field lies on.

### getName()

```python
def getName(self)
```

Returns the field name.

### getType()

```python
def getType(self)
```

Returns type of field data as integer [0-3].

### getTypeEnum()

```python
def getTypeEnum(self)
```

Returns type of field data: one of [GEOM.FDT_Bool](namespaceGEOM.md#a5ab69b28329e64ad4279f348d7230cb2a2e2c22b80eb7d364a1b470bb741c6abe), [GEOM.FDT_Int](namespaceGEOM.md#a5ab69b28329e64ad4279f348d7230cb2aa7663ed796f85bef8e46869328bbcb40), [GEOM.FDT_Double](namespaceGEOM.md#a5ab69b28329e64ad4279f348d7230cb2a0edbe6a229f527bb5723efe9f233ee03), [GEOM.FDT_String](namespaceGEOM.md#a5ab69b28329e64ad4279f348d7230cb2a02f990f9d6ce81dbebc5c7c42af63052).

### getDimension()

```python
def getDimension(self)
```

Returns dimension of the shape the field lies on: 0 - VERTEX, 1 - EDGE, 2 - FACE, 3 - SOLID, -1 - whole shape.

### getComponents()

```python
def getComponents(self)
```

Returns names of components.

### addStep()

```python
def addStep(self, step, stamp, values)
```

Adds a time step to the field.

Parameters
:   |  |  |
    | --- | --- |
    | step | the time step number further used as the step identifier |
    | stamp | the time step time |
    | values | the values of the time step |

### removeStep()

```python
def removeStep(self, step)
```

Remove a time step from the field.

### countSteps()

```python
def countSteps(self)
```

Returns number of time steps in the field.

### getSteps()

```python
def getSteps(self)
```

Returns a list of time step IDs in the field.

### getStep()

```python
def getStep(self, step)
```

Returns a time step by its ID.

### getStamp()

```python
def getStamp(self, step)
```

Returns the time of the field step.

### setStamp()

```python
def setStamp(self, step, stamp)
```

Changes the time of the field step.

### getValues()

```python
def getValues(self, step)
```

Returns values of the field step.

### setValues()

```python
def setValues(self, step, values)
```

Changes values of the field step.

## Field Documentation

### field

```python
field
```
