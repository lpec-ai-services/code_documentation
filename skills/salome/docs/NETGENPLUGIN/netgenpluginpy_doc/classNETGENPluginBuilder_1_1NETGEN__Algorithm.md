<!-- source: https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/netgenpluginpy_doc/classNETGENPluginBuilder_1_1NETGEN__Algorithm.html -->

# NETGEN_Algorithm Class Reference

Base of all NETGEN algorithms.
[More...](classNETGENPluginBuilder_1_1NETGEN__Algorithm.md#details)

## Detailed Description

Base of all NETGEN algorithms.

This class provides common methods for all algorithms implemented by NETGEN plugin.

Note
:   This class must not be instantiated directly.

## Constructor & Destructor Documentation

### __init__()

```python
def __init__(self, mesh, geom = 0)
```

Private constructor.

Parameters
:   |  |  |
    | --- | --- |
    | mesh | parent mesh object algorithm is assigned to |
    | geom | geometry (shape/sub-shape) algorithm is assigned to; if it is `0` (default), the algorithm is assigned to the main shape |

## Member Function Documentation

### SetMaxSize()

```python
def SetMaxSize(self, theSize)
```

Sets `MaxSize` parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theSize | new value of the `MaxSize` parameter |

### SetMinSize()

```python
def SetMinSize(self, theSize)
```

Sets `MinSize` parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theSize | new value of the `MinSize` parameter |

### SetOptimize()

```python
def SetOptimize(self, theVal)
```

Sets `Optimize` flag.

Parameters
:   |  |  |
    | --- | --- |
    | theVal | new value of the `Optimize` parameter |

### SetFineness()

```python
def SetFineness(self, theFineness)
```

Sets `Fineness` parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theFineness | new value of the `Fineness` parameter; it can be: [VeryCoarse](namespaceNETGENPluginBuilder.md#aa647f579f3005518abe895c94784a6d5), [Coarse](namespaceNETGENPluginBuilder.md#a3dfd217c55fb5a2dbee356756ac7d612), [Moderate](namespaceNETGENPluginBuilder.md#a3c80f069011ec4fb0ae85fa37c823eae), [Fine](namespaceNETGENPluginBuilder.md#aab1d1e268628320d6683bb2dd81a4d4c), [VeryFine](namespaceNETGENPluginBuilder.md#a669774e626dd6a9864f04ede3d0533a8) or [Custom](namespaceNETGENPluginBuilder.md#a7749f590e058d92087be1509e66bcb02) |

### SetGrowthRate()

```python
def SetGrowthRate(self, theRate)
```

Sets `GrowthRate` parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theRate | new value of the `GrowthRate` parameter |

### SetNbThreads()

```python
def SetNbThreads(self, theNumber)
```

Sets `NbThreads` parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theRate | new value of the `NbThreads` parameter |

### Parameters()

```python
def Parameters(self, which = SOLE)
```

Creates meshing hypothesis according to the chosen algorithm type and initializes it with default parameters.

Parameters
:   |  |  |
    | --- | --- |
    | which | hypothesis type; can be either [SOLE](namespaceNETGENPluginBuilder.md#ae07ea749e409e2e117bf186d476c6933) (default) or [SIMPLE](namespaceNETGENPluginBuilder.md#a1ad51692cb081aff523260fd45798996) |

Returns
:   hypothesis object

### SetMeshSizeFile()

```python
def SetMeshSizeFile(self, file)
```

Defines a file specifying size of elements at points and lines.

Parameters
:   |  |  |
    | --- | --- |
    | file | name of the file |

### SetLocalSizeOnShape()

```python
def SetLocalSizeOnShape(self, shape, size)
```

Set size of elements on a shape.

Parameters
:   |  |  |
    | --- | --- |
    | shape | - geometry |
    | size | - element size |

## Field Documentation

### meshMethod

```python
meshMethod
```

### params

```python
params
```

### algoType

```python
algoType
```
