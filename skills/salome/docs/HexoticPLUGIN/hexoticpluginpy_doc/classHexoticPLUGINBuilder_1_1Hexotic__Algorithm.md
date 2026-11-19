<!-- source: https://docs.salome-platform.org/latest/gui/HexoticPLUGIN/hexoticpluginpy_doc/classHexoticPLUGINBuilder_1_1Hexotic__Algorithm.html -->

# Hexotic_Algorithm Class Reference

Defines a hexahedron 3D algorithm.
[More...](classHexoticPLUGINBuilder_1_1Hexotic__Algorithm.md#details)

## Detailed Description

Defines a hexahedron 3D algorithm.

It is created by calling [smeshBuilder.Mesh.Hexahedron](classsmeshBuilder_1_1Mesh.md#a8c05a76fdef5d692fb53e1cc0e364ae5)( smeshBuilder.MG_Hexa, geom=0 )

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

### SetMinMaxHexes()

```python
def SetMinMaxHexes(self, min = 3, max = 8)
```

Defines "SetMinMaxHexes" hypothesis to give two MG-Hexa parameters.

Parameters
:   |  |  |
    | --- | --- |
    | min | minimal level of recursive partitioning on the initial octree cube |
    | max | maximal level of recursive partitioning on the initial octree cube |

Returns
:   hypothesis object

### SetMinMaxSize()

```python
def SetMinMaxSize(self, min, max)
```

Defines "SetMinMaxSize" hypothesis to give two MG-Hexa parameters.

Parameters
:   |  |  |
    | --- | --- |
    | min | minimal element's size |
    | max | maximal element's size |

Returns
:   hypothesis object

### SetSizeMap()

```python
def SetSizeMap(self, theObject, theSize)
```

Sets a size map.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | geometrical object to assign local size to |
    | theSize | local size on the given object |

Returns
:   hypothesis object

### UnsetSizeMap()

```python
def UnsetSizeMap(self, theObject)
```

Unsets a size map : this is meant to be used only by the dump.

Parameters
:   |  |  |
    | --- | --- |
    | theObject | geometrical object to unassign local size |

Returns
:   hypothesis object

### SetAdvancedOption()

```python
def SetAdvancedOption(self, theOptions)
```

Set values of advanced options.

Parameters
:   |  |  |
    | --- | --- |
    | theOptions | string in a form "option_1 v1 option_2 v2" |

### GetAdvancedOption()

```python
def GetAdvancedOption(self)
```

### MinMaxQuad()

```python
def MinMaxQuad(self, min = 3, max = 8, quad = True)
```

(OBSOLETE) Defines "MinMaxQuad" hypothesis to give three MG-Hexa parameters

Parameters
:   |  |  |
    | --- | --- |
    | min | minimal level of recursive partitioning on the initial octree cube |
    | max | maximal level of recursive partitioning on the initial octree cube |
    | quad | not documented |

Returns
:   hypothesis object

### SetOptionValue()

```python
def SetOptionValue(self, optionName, optionValue)
```

Set advanced option value.

Parameters
:   |  |  |
    | --- | --- |
    | optionName | option name |
    | optionValue | option value |

### SetViscousLayers()

```python
def SetViscousLayers(self, numberOfLayers, firstLayerSize, growth, facesWithLayers, imprintedFaces = [], direction = Inward)
```

Defines "ViscousLayers" hypothesis to give MG-Hexa parameters.

Parameters
:   |  |  |
    | --- | --- |
    | numberOfLayers | number of boundary layers |
    | firstLayerSize | height of the first layer |
    | growth | geometric progression for the boundary layer growth |
    | direction | describes whether the layers grow inwards or outwards. Possible values are:  - `smeshBuilder.Inward` : means the layers grow inwards, - `smeshBuilder.Outward` : means the layers grow outwards |
    | facesWithLayers | list of surfaces from which the boundary layers should be grown |
    | imprintedFaces | list of surfaces that can be imprinted by boundary layers |

Returns
:   hypothesis object

### SetKeepFiles()

```python
def SetKeepFiles(self, toKeep)
```

To keep working files or remove them.

Parameters
:   |  |  |
    | --- | --- |
    | toKeep | "keep working files" flag value |

### SetRemoveLogOnSuccess()

```python
def SetRemoveLogOnSuccess(self, toRemove)
```

Remove or not the log file (if any) in case of successful computation.

The log file remains in case of errors anyway. If the "keep working files" flag is set to true, this option has no effect.

Parameters
:   |  |  |
    | --- | --- |
    | toRemove | "remove log on success" flag value |

### SetPrintLogInFile()

```python
def SetPrintLogInFile(self, toPrintLogInFile)
```

Print the the log in a file.

If set to false, the log is printed on the standard output

Parameters
:   |  |  |
    | --- | --- |
    | toPrintLogInFile | "print log in a file" flag value |

### Parameters()

```python
def Parameters(self)
```

Defines hypothesis having several parameters.

Returns
:   hypothesis object

## Field Documentation

### meshMethod

```python
string meshMethod = "Hexahedron" static
```

name of the dynamic method in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### algoType

```python
algoType = MG_Hexa static
```

type of algorithm used with helper function in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### docHelper

```python
string docHelper = "Creates hexahedron 3D algorithm for volumes" static
```

doc string of the method in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### params

```python
params
```
