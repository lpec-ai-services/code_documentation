<!-- source: https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/netgenpluginpy_doc/classNETGENPluginBuilder_1_1NETGEN__2D__Only__Algorithm.html -->

# NETGEN_2D_Only_Algorithm Class Reference

Triangle NETGEN 2D algorithm.
[More...](classNETGENPluginBuilder_1_1NETGEN__2D__Only__Algorithm.md#details)

## Detailed Description

Triangle NETGEN 2D algorithm.

It can be created by calling [smeshBuilder.Mesh.Triangle](classsmeshBuilder_1_1Mesh.md#a58d92bcd67822a8ea2a782177e9a41a4)( smeshBuilder.NETGEN_2D, geom=0 )

This algorithm generates only 2D (faces) elements for given geometrical shape and, in contrast to [NETGEN_1D2D_Algorithm](classNETGENPluginBuilder_1_1NETGEN__1D2D__Algorithm.md) class, should be used in conjunction with other 1D meshing algorithm.

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

### MaxElementArea()

```python
def MaxElementArea(self, area, UseExisting = 0)
```

Defines `MaxElementArea` parameter of hypothesis basing on the definition of the maximum area of each triangle.

Parameters
:   |  |  |
    | --- | --- |
    | area | maximum area value of each triangle |
    | UseExisting | if `True` - searches for an existing hypothesis created with the same parameters, else (default) - creates a new one |

Returns
:   hypothesis object

### LengthFromEdges()

```python
def LengthFromEdges(self)
```

Defines `LengthFromEdges` hypothesis to build triangles based on the length of the edges taken from the wire.

Returns
:   hypothesis object

### SetUseSurfaceCurvature()

```python
def SetUseSurfaceCurvature(self, toUse = True)
```

Sets `UseSurfaceCurvature` flag.

Parameters
:   |  |  |
    | --- | --- |
    | toUse | new value of the `UseSurfaceCurvature` parameter (`True` by default) |

### SetQuadAllowed()

```python
def SetQuadAllowed(self, toAllow = True)
```

Sets `QuadAllowed` flag.

Parameters
:   |  |  |
    | --- | --- |
    | toAllow | new value of the `QuadAllowed` parameter (`True` by default) |

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

### meshMethod

```python
string meshMethod = "Triangle" static
```

name of the dynamic method in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### algoType

```python
algoType = NETGEN_2D static
```

type of algorithm used with helper function in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### isDefault

```python
bool isDefault = True static
```

flag pointing whether this algorithm should be used by default in dynamic method of [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### docHelper

```python
string docHelper = "Creates triangle 2D algorithm for faces" static
```

doc string of the method

### params

```python
params inherited
```
