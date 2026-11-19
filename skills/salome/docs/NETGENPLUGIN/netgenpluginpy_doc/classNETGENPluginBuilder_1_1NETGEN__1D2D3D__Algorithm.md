<!-- source: https://docs.salome-platform.org/latest/gui/NETGENPLUGIN/netgenpluginpy_doc/classNETGENPluginBuilder_1_1NETGEN__1D2D3D__Algorithm.html -->

# NETGEN_1D2D3D_Algorithm Class Reference

Tetrahedron 1D-2D-3D algorithm.
[More...](classNETGENPluginBuilder_1_1NETGEN__1D2D3D__Algorithm.md#details)

## Detailed Description

Tetrahedron 1D-2D-3D algorithm.

It can be created by calling [smeshBuilder.Mesh.Tetrahedron](classsmeshBuilder_1_1Mesh.md#a2622f0d55649077abf581277531e6b2b)( smeshBuilder.NETGEN_1D2D3D, geom=0 ). This algorithm generates all 1D (edges), 2D (faces) and 3D (volumes) elements for given geometrical shape.

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

### SetSecondOrder()

```python
def SetSecondOrder(self, theVal)
```

Sets `SecondOrder` flag.

Parameters
:   |  |  |
    | --- | --- |
    | theVal | new value of the `SecondOrder` parameter |

### SetNbSegPerEdge()

```python
def SetNbSegPerEdge(self, theVal)
```

Sets `NbSegPerEdge` parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theVal | new value of the `NbSegPerEdge` parameter |

### SetNbSegPerRadius()

```python
def SetNbSegPerRadius(self, theVal)
```

Sets `NbSegPerRadius` parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theVal | new value of the `NbSegPerRadius` parameter |

### SetChordalError()

```python
def SetChordalError(self, theVal)
```

Sets `ChordalError` parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theVal | new value of the `ChordalError` parameter |

### SetRidgeAngle()

```python
def SetRidgeAngle(self, theVal)
```

Sets `RidgeAngle` parameter.

Parameters
:   |  |  |
    | --- | --- |
    | theVal | new value of the `RidgeAngle` parameter |

### SetQuadAllowed()

```python
def SetQuadAllowed(self, toAllow = True)
```

Sets `QuadAllowed` flag.

Parameters
:   |  |  |
    | --- | --- |
    | toAllow | new value of the `QuadAllowed` parameter (`True` by default) |

### SetUseSurfaceCurvature()

```python
def SetUseSurfaceCurvature(self, toUse = True)
```

Sets `UseSurfaceCurvature` flag.

Parameters
:   |  |  |
    | --- | --- |
    | toUse | new value of the `UseSurfaceCurvature` parameter (`True` by default) |

### SetFuseEdges()

```python
def SetFuseEdges(self, toFuse = False)
```

Sets `FuseEdges` flag.

Parameters
:   |  |  |
    | --- | --- |
    | toFuse | new value of the `FuseEdges` parameter (`False` by default) |

### SetNumberOfSegments()

```python
def SetNumberOfSegments(self, theVal)
```

Sets number of segments overriding the value set by [SetLocalLength()](classNETGENPluginBuilder_1_1NETGEN__1D2D3D__Algorithm.md#a9e7df98de4ac6af941fef464d5b250e0)

Parameters
:   |  |  |
    | --- | --- |
    | theVal | new value of number of segments parameter |

### SetLocalLength()

```python
def SetLocalLength(self, theVal)
```

Sets number of segments overriding the value set by [SetNumberOfSegments()](classNETGENPluginBuilder_1_1NETGEN__1D2D3D__Algorithm.md#a86a4d2e9cbd0a2b09a891976036dabab)

Parameters
:   |  |  |
    | --- | --- |
    | theVal | new value of local length parameter |

### MaxElementArea()

```python
def MaxElementArea(self, area)
```

Defines `MaxElementArea` parameter of `NETGEN_SimpleParameters_3D` hypothesis.

Overrides value set by [LengthFromEdges()](classNETGENPluginBuilder_1_1NETGEN__1D2D3D__Algorithm.md#a7bd8693a204f948d1401194f648269ac)

Parameters
:   |  |  |
    | --- | --- |
    | area | new value of `MaxElementArea` parameter |

### LengthFromEdges()

```python
def LengthFromEdges(self)
```

Defines `LengthFromEdges` parameter of `NETGEN_SimpleParameters_3D` hypothesis.

Overrides value set by [MaxElementArea()](classNETGENPluginBuilder_1_1NETGEN__1D2D3D__Algorithm.md#a463f3288f5101b60b572cce7a284b88c)

### LengthFromFaces()

```python
def LengthFromFaces(self)
```

Defines `LengthFromFaces` parameter of `NETGEN_SimpleParameters_3D` hypothesis.

Overrides value set by [MaxElementVolume()](classNETGENPluginBuilder_1_1NETGEN__1D2D3D__Algorithm.md#a44871ddd32b2cc66dafade076487116c)

### MaxElementVolume()

```python
def MaxElementVolume(self, vol)
```

Defines `MaxElementVolume` parameter of `NETGEN_SimpleParameters_3D` hypothesis.

Overrides value set by [LengthFromFaces()](classNETGENPluginBuilder_1_1NETGEN__1D2D3D__Algorithm.md#a84d1f37d9956139a86913efc5a66a746)

Parameters
:   |  |  |
    | --- | --- |
    | vol | new value of `MaxElementVolume` parameter |

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
string meshMethod = "Tetrahedron" static
```

name of the dynamic method in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### algoType

```python
algoType = NETGEN_1D2D3D static
```

type of algorithm used with helper function in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### docHelper

```python
string docHelper = "Creates tetrahedron 3D algorithm for solids" static
```

doc string of the method

### params

```python
params inherited
```
