<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/namespacegeomBuilder.html -->

# geomBuilder Namespace Reference

## Detailed Description

Note
:   Some methods are dynamically added to the **geomBuilder** class in runtime by the plug-in modules. If you fail to find help on some methods in the documentation of Geometry module, try to look into the documentation for the Geometry module plug-ins.

## Function Documentation

### enumitem_eq()

```python
def geomBuilder.enumitem_eq(self, other)
```

### enumitem_lt()

```python
def geomBuilder.enumitem_lt(self, other)
```

### enumitem_le()

```python
def geomBuilder.enumitem_le(self, other)
```

### enumitem_gt()

```python
def geomBuilder.enumitem_gt(self, other)
```

### enumitem_ge()

```python
def geomBuilder.enumitem_ge(self, other)
```

### _toListOfNames()

```python
def geomBuilder._toListOfNames(_names, _size = -1) private
```

### ManageTransactions()

```python
def geomBuilder.ManageTransactions(theOpeName)
```

### PrintOrRaise()

```python
def geomBuilder.PrintOrRaise(message, raiseException = False)
```

### ToList()

```python
def geomBuilder.ToList(arg)
```

Pack an argument into a list.

### New()

```python
def geomBuilder.New(instance = None)
```

Create a new [geomBuilder](namespacegeomBuilder.md) instance.The [geomBuilder](namespacegeomBuilder.md) class provides the Python interface to [GEOM](namespaceGEOM.md) operations.

Typical use is:

```python
import salome
salome.salome_init()
from salome.geom import geomBuilder
geompy = geomBuilder.New()
```

Parameters
:   |  |  |
    | --- | --- |
    | instance | CORBA proxy of [GEOM](namespaceGEOM.md) Engine. If None, the default Engine is used. |

Returns
:   [geomBuilder](namespacegeomBuilder.md) instance

## Variable Documentation

### __eq__

```python
__eq__ private
```

### __lt__

```python
__lt__ private
```

### __le__

```python
__le__ private
```

### __gt__

```python
__gt__ private
```

### __ge__

```python
__ge__ private
```

### geom

```python
geom = None
```

### engine

```python
engine = None
```

### doLcc

```python
bool doLcc = False
```

### created

```python
bool created = False
```

### plugins_var

```python
plugins_var = os.environ.get("GEOM_PluginsList")
```

### plugins

```python
list plugins = None
```

### pluginBuilderName

```python
string pluginBuilderName = pluginName + "Builder"
```

### plugin

```python
plugin = eval(pluginBuilderName)
```

### method

```python
method = getattr(plugin, k)
```

### _v

```python
_v private
```

### _parent_id

```python
_parent_id private
```
