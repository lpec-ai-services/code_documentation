<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/classgeomBuilder_1_1geomBuilder.html -->

# geomBuilder Class Reference

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, args)
```

## Member Function Documentation

### __new__()

```python
def __new__(cls, args)
```

### _autoPublish()

```python
def _autoPublish(self, theObj, theName, theDefaultName = "noname") private
```

Process object publication in the study, as follows:

- if *theName* is specified (not None), the object is published in the study with this name, not taking into account "auto-publishing" option;
- if *theName* is NOT specified, the object is published in the study (using default name, which can be customized using *theDefaultName* parameter) only if auto-publishing is switched on.

Parameters
:   |  |  |
    | --- | --- |
    | theObj | object, a subject for publishing |
    | theName | object name for study |
    | theDefaultName | default name for the auto-publishing |

See also
:   [addToStudyAuto()](group__l1__publish__data.md#ga5e79902a873c815eea08b843026b02ea)

### GetAdvancedOperations()

```python
def GetAdvancedOperations(self)
```

### GetSTLPluginOperations()

```python
def GetSTLPluginOperations(self)
```

### GetBREPPluginOperations()

```python
def GetBREPPluginOperations(self)
```

### GetSTEPPluginOperations()

```python
def GetSTEPPluginOperations(self)
```

### GetIGESPluginOperations()

```python
def GetIGESPluginOperations(self)
```

### GetXAOPluginOperations()

```python
def GetXAOPluginOperations(self)
```

### GetVTKPluginOperations()

```python
def GetVTKPluginOperations(self)
```

## Field Documentation

### myMaxNbSubShapesAllowed

```python
myMaxNbSubShapesAllowed
```

### myBuilder

```python
myBuilder
```

### BasicOp

```python
BasicOp
```

### CurvesOp

```python
CurvesOp
```

### PrimOp

```python
PrimOp
```

### ShapesOp

```python
ShapesOp
```

### HealOp

```python
HealOp
```

### InsertOp

```python
InsertOp
```

### BoolOp

```python
BoolOp
```

### TrsfOp

```python
TrsfOp
```

### LocalOp

```python
LocalOp
```

### MeasuOp

```python
MeasuOp
```

### BlocksOp

```python
BlocksOp
```

### GroupOp

```python
GroupOp
```

### FieldOp

```python
FieldOp
```

### TestOp

```python
TestOp
```

### myStudy

```python
myStudy
```

### def_names

```python
def_names
```
