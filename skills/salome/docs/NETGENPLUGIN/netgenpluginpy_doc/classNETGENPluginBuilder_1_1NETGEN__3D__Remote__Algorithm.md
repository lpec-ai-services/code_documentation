<!-- source: https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/netgenpluginpy_doc/classNETGENPluginBuilder_1_1NETGEN__3D__Remote__Algorithm.html -->

# NETGEN_3D_Remote_Algorithm Class Reference

Tetrahedron 3D algorithm.
[More...](classNETGENPluginBuilder_1_1NETGEN__3D__Remote__Algorithm.md#details)

## Detailed Description

Tetrahedron 3D algorithm.

It can be created by calling [smeshBuilder.Mesh.Tetrahedron()](classsmeshBuilder_1_1Mesh.md#a2622f0d55649077abf581277531e6b2b) or [smeshBuilder.Mesh.Tetrahedron](classsmeshBuilder_1_1Mesh.md#a2622f0d55649077abf581277531e6b2b)( smeshBuilder.NETGEN, geom=0 )

This algorithm generates only 3D (volumes) elements for given geometrical shape and, in contrast to [NETGEN_1D2D3D_Algorithm](classNETGENPluginBuilder_1_1NETGEN__1D2D3D__Algorithm.md) class, should be used in conjunction with other 1D and 2D meshing algorithms.

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

### MaxElementVolume()

```python
def MaxElementVolume(self, vol, UseExisting = 0) inherited
```

Defines `MaxElementVolume` hypothesis to specify the maximum volume value of each tetrahedron.

Parameters
:   |  |  |
    | --- | --- |
    | vol | maximum volume value of each tetrahedron |
    | UseExisting | if `True` - searches for the existing hypothesis created with the same parameters, else (default) - creates a new one |

Returns
:   hypothesis object

### SetMaxSize()

```python
def SetMaxSize(self, theSize) inherited
```

Sets `MaxSize` parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theSize | new value of the `MaxSize` parameter |

### SetMinSize()

```python
def SetMinSize(self, theSize) inherited
```

Sets `MinSize` parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theSize | new value of the `MinSize` parameter |

### SetOptimize()

```python
def SetOptimize(self, theVal) inherited
```

Sets `Optimize` flag.

Parameters
:   |  |  |
    | --- | --- |
    | theVal | new value of the `Optimize` parameter |

### SetFineness()

```python
def SetFineness(self, theFineness) inherited
```

Sets `Fineness` parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theFineness | new value of the `Fineness` parameter; it can be: [VeryCoarse](namespaceNETGENPluginBuilder.md#aa647f579f3005518abe895c94784a6d5), [Coarse](namespaceNETGENPluginBuilder.md#a3dfd217c55fb5a2dbee356756ac7d612), [Moderate](namespaceNETGENPluginBuilder.md#a3c80f069011ec4fb0ae85fa37c823eae), [Fine](namespaceNETGENPluginBuilder.md#aab1d1e268628320d6683bb2dd81a4d4c), [VeryFine](namespaceNETGENPluginBuilder.md#a669774e626dd6a9864f04ede3d0533a8) or [Custom](namespaceNETGENPluginBuilder.md#a7749f590e058d92087be1509e66bcb02) |

### SetGrowthRate()

```python
def SetGrowthRate(self, theRate) inherited
```

Sets `GrowthRate` parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theRate | new value of the `GrowthRate` parameter |

### SetNbThreads()

```python
def SetNbThreads(self, theNumber) inherited
```

Sets `NbThreads` parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theRate | new value of the `NbThreads` parameter |

### Parameters()

```python
def Parameters(self, which = SOLE) inherited
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
def SetMeshSizeFile(self, file) inherited
```

Defines a file specifying size of elements at points and lines.

Parameters
:   |  |  |
    | --- | --- |
    | file | name of the file |

### SetLocalSizeOnShape()

```python
def SetLocalSizeOnShape(self, shape, size) inherited
```

Set size of elements on a shape.

Parameters
:   |  |  |
    | --- | --- |
    | shape | - geometry |
    | size | - element size |

## Field Documentation

### algoType

```python
algoType = NETGEN_3D_Remote static
```

type of algorithm used with helper function in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### isDefault

```python
bool isDefault = False static
```

flag pointing either this algorithm should be used by default in dynamic method of [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### docHelper

```python
string docHelper = "Remotely Creates tetrahedron 3D algorithm for solids" static
```

doc string of the method

### meshMethod

```python
string meshMethod = "Tetrahedron" static inherited
```

name of the dynamic method in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### params

```python
params inherited
```
