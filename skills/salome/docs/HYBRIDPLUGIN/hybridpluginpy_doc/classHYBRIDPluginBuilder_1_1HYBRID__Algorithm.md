<!-- source: https://docs.salome-platform.org/latest/gui/HYBRIDPLUGIN/hybridpluginpy_doc/classHYBRIDPluginBuilder_1_1HYBRID__Algorithm.html -->

# HYBRID_Algorithm Class Reference

MG-Hybrid 3D algorithm.
[More...](classHYBRIDPluginBuilder_1_1HYBRID__Algorithm.md#details)

## Detailed Description

MG-Hybrid 3D algorithm.

It can be created by calling [smeshBuilder.Mesh.Tetrahedron](classsmeshBuilder_1_1Mesh.md#a2622f0d55649077abf581277531e6b2b)( smeshBuilder.HYBRID, geom=0 )

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

### Parameters()

```python
def Parameters(self)
```

Defines hypothesis having several parameters.

Returns
:   hypothesis object

### SetToUseLibrary()

```python
def SetToUseLibrary(self, toUseLib)
```

To call MG-Hybrid by library.

Default is no (i.e. by executable)

Parameters
:   |  |  |
    | --- | --- |
    | toUseLib | "mesh layers on all wrap" flag value |

### SetLayersOnAllWrap()

```python
def SetLayersOnAllWrap(self, toMesh)
```

To mesh layers on all wrap.

Default is to mesh.

Parameters
:   |  |  |
    | --- | --- |
    | toMesh | "mesh layers on all wrap" flag value |

### SetFacesWithLayers()

```python
def SetFacesWithLayers(self, faceIDs)
```

To mesh layers on given faces.

Parameters
:   |  |  |
    | --- | --- |
    | faceIDs | faces or face IDs to construct boundary layers on |

### SetFacesWithImprinting()

```python
def SetFacesWithImprinting(self, faceIDs)
```

To imprint the layers on given faces.

Parameters
:   |  |  |
    | --- | --- |
    | faceIDs | faces or face IDs to imprint the boundary layers on |

### SetFacesWithSnapping()

```python
def SetFacesWithSnapping(self, faceIDs)
```

To snap the layers on given surface (use existing surface layers as base for volume layers).

Parameters
:   |  |  |
    | --- | --- |
    | faceIDs | faces or face IDs that already have surface layers |

### SetCollisionMode()

```python
def SetCollisionMode(self, mode)
```

Set Collision Mode:

Parameters
:   |  |  |
    | --- | --- |
    | mode | Collision Mode, one of the following values  - Decrease_Collision_Mode - Stop_Collision_Mode  Default is Decrease_Collision_Mode |

### SetBoundaryLayersGrowth()

```python
def SetBoundaryLayersGrowth(self, mode)
```

To mesh Boundary Layers growing inward or outward.

Parameters
:   |  |  |
    | --- | --- |
    | mode,one | of the following values  - Layer_Growth_Inward - Layer_Growth_Outward  Default is Layer_Growth_Inward |

### SetElementGeneration()

```python
def SetElementGeneration(self, mode)
```

To mesh with element type Tetra Dominant or hexa Dominant in the remaining volume (outside layers).

Parameters
:   |  |  |
    | --- | --- |
    | mode,one | of the following values  - Generation_Tetra_Dominant - Generation_Hexa_Dominant - Generation_Cartesian_Core  Default is Generation_Tetra_Dominant |

### SetAddMultinormals()

```python
def SetAddMultinormals(self, addMultinormals)
```

To mesh adding extra normals at opening ridges and corners.

Default is no.

Parameters
:   |  |  |
    | --- | --- |
    | addMultinormals | boolean value |

### SetSmoothNormals()

```python
def SetSmoothNormals(self, smoothNormals)
```

To mesh smoothing normals at closed ridges and corners.

Default is no.

Parameters
:   |  |  |
    | --- | --- |
    | smoothNormals | boolean value |

### SetHeightFirstLayer()

```python
def SetHeightFirstLayer(self, heightFirstLayer)
```

To set height of the first layer.

Default is 0.0

Parameters
:   |  |  |
    | --- | --- |
    | heightFirstLayer | double value |

### SetHeightIsRelative()

```python
def SetHeightIsRelative(self, isRelative)
```

Sizes of boundary layers are relative to the surface size.

Default no

Parameters
:   |  |  |
    | --- | --- |
    | isRelative | boolean flag |

### SetBoundaryLayersProgression()

```python
def SetBoundaryLayersProgression(self, boundaryLayersProgression)
```

To set boundary layers coefficient of geometric progression.

Default is 1.0

Parameters
:   |  |  |
    | --- | --- |
    | boundaryLayersProgression | double value |

### SetCoreSize()

```python
def SetCoreSize(self, CoreSize)
```

Set core elements size.

Default is 0.0

Parameters
:   |  |  |
    | --- | --- |
    | CoreSize | double value |

### SetMultinormalsAngle()

```python
def SetMultinormalsAngle(self, multinormalsAngle)
```

To set multinormals angle threshold at opening ridges.

Default is 30.0

Parameters
:   |  |  |
    | --- | --- |
    | multinormalsAngle | double value |

### SetNbOfBoundaryLayers()

```python
def SetNbOfBoundaryLayers(self, nbOfBoundaryLayers)
```

To set number of boundary layers.

Default is 1

Parameters
:   |  |  |
    | --- | --- |
    | nbOfBoundaryLayers | int value |

### SetBoundaryLayersMaxElemAngle()

```python
def SetBoundaryLayersMaxElemAngle(self, angle)
```

Set maximum internal angles of boundary elements (in degree)

Parameters
:   |  |  |
    | --- | --- |
    | angle | angle in degree |

### SetWorkingDirectory()

```python
def SetWorkingDirectory(self, path)
```

Set path to working directory.

Parameters
:   |  |  |
    | --- | --- |
    | path | working directory |

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

### SetVerboseLevel()

```python
def SetVerboseLevel(self, level)
```

Set verbosity level [0-10].

Parameters
:   |  |  |
    | --- | --- |
    | level | verbosity level  - 0 - no standard output, - 2 - prints the data, quality statistics of the skin and final meshes and indicates when the final mesh is being saved. In addition the software gives indication regarding the CPU time. - 10 - same as 2 plus the main steps in the computation, quality statistics histogram of the skin mesh, quality statistics histogram together with the characteristics of the final mesh. |

### SetToCreateNewNodes()

```python
def SetToCreateNewNodes(self, toCreate)
```

To create new nodes.

Parameters
:   |  |  |
    | --- | --- |
    | toCreate | "create new nodes" flag value |

### SetToUseBoundaryRecoveryVersion()

```python
def SetToUseBoundaryRecoveryVersion(self, toUse)
```

To use boundary recovery version which tries to create mesh on a very poor quality surface mesh.

Parameters
:   |  |  |
    | --- | --- |
    | toUse | "use boundary recovery version" flag value |

### SetFEMCorrection()

```python
def SetFEMCorrection(self, toUseFem)
```

Applies finite-element correction by replacing overconstrained elements where it is possible.

The process is cutting first the overconstrained edges and second the overconstrained facets. This insure that no edges have two boundary vertices and that no facets have three boundary vertices.

Parameters
:   |  |  |
    | --- | --- |
    | toUseFem | "apply finite-element correction" flag value |

### SetToRemoveCentralPoint()

```python
def SetToRemoveCentralPoint(self, toRemove)
```

To remove initial central point.

Parameters
:   |  |  |
    | --- | --- |
    | toRemove | "remove initial central point" flag value |

### SetEnforcedVertex()

```python
def SetEnforcedVertex(self, x, y, z, size, vertexName = "", groupName = "")
```

To set an enforced vertex.

Parameters
:   |  |  |
    | --- | --- |
    | x | : x coordinate |
    | y | : y coordinate |
    | z | : z coordinate |
    | size | : size of 1D element around enforced vertex |
    | vertexName | : name of the enforced vertex |
    | groupName | : name of the group |

### SetEnforcedVertexGeom()

```python
def SetEnforcedVertexGeom(self, theVertex, size, groupName = "")
```

To set an enforced vertex given a GEOM vertex, group or compound.

Parameters
:   |  |  |
    | --- | --- |
    | theVertex | : GEOM vertex (or group, compound) to be projected on theFace. |
    | size | : size of 1D element around enforced vertex |
    | groupName | : name of the group |

### RemoveEnforcedVertex()

```python
def RemoveEnforcedVertex(self, x, y, z)
```

To remove an enforced vertex.

Parameters
:   |  |  |
    | --- | --- |
    | x | : x coordinate |
    | y | : y coordinate |
    | z | : z coordinate |

### RemoveEnforcedVertexGeom()

```python
def RemoveEnforcedVertexGeom(self, theVertex)
```

To remove an enforced vertex given a GEOM vertex, group or compound.

Parameters
:   |  |  |
    | --- | --- |
    | theVertex | : GEOM vertex (or group, compound) to be projected on theFace. |

### SetEnforcedMesh()

```python
def SetEnforcedMesh(self, theSource, elementType, size = -1, groupName = "")
```

To set an enforced mesh with given size and add the enforced elements in the group "groupName".

Parameters
:   |  |  |
    | --- | --- |
    | theSource | : source mesh which provides constraint elements/nodes |
    | elementType | : SMESH.ElementType (NODE, EDGE or FACE) |
    | size | : size of elements around enforced elements. Unused if -1. |
    | groupName | : group in which enforced elements will be added. Unused if "". |

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

### SetAdvancedOption()

```python
def SetAdvancedOption(self, optionAndValue)
```

Sets command line option as text.

Parameters
:   |  |  |
    | --- | --- |
    | optionAndValue | command line option in a form "option value" |

### SetTextOption()

```python
def SetTextOption(self, option)
```

Sets command line option as text.

OBSOLETE. Use [SetAdvancedOption()](classHYBRIDPluginBuilder_1_1HYBRID__Algorithm.md#a131fe9c599a0924dd13ab776921cf6d2)

Parameters
:   |  |  |
    | --- | --- |
    | option | command line option |

## Field Documentation

### meshMethod

```python
string meshMethod = "Tetrahedron" static
```

name of the dynamic method in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### algoType

```python
algoType = MG_Hybrid static
```

type of algorithm used with helper function in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### docHelper

```python
string docHelper = "Creates tetrahedron 3D algorithm for volumes" static
```

doc string of the method in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### params

```python
params
```
