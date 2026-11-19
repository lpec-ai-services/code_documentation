<!-- source: https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/ghs3dpluginpy_doc/classGHS3DPluginBuilder_1_1GHS3D__Optimizer.html -->

# GHS3D_Optimizer Class Reference

MG-Tetra Optimization algorithm - optimizer of tetrahedral meshes.
[More...](classGHS3DPluginBuilder_1_1GHS3D__Optimizer.md#details)

## Detailed Description

MG-Tetra Optimization algorithm - optimizer of tetrahedral meshes.

It can be created by calling [smeshBuilder.Mesh.Tetrahedron](classsmeshBuilder_1_1Mesh.md#a2622f0d55649077abf581277531e6b2b)( smeshBuilder.MG_Tetra_Optimization )

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
    | geom | - not used |

## Member Function Documentation

### Parameters()

```python
def Parameters(self)
```

Defines hypothesis having several parameters.

Returns
:   hypothesis object

### SetOptimizationOnly()

```python
def SetOptimizationOnly(self, optMode)
```

Set Optimization mode.

Parameters
:   |  |  |
    | --- | --- |
    | optMode | optimization mode, one of the following values: smeshBuilder.Mode_NO, smeshBuilder.Mode_YES (default), smeshBuilder.MODE_ONLY |

### SetSplitOverConstrained()

```python
def SetSplitOverConstrained(self, ovcMode)
```

Set mode of splitting over-constrained elements.

Parameters
:   |  |  |
    | --- | --- |
    | ovcMode,one | of the following values smeshBuilder.Mode_NO (default), smeshBuilder.Mode_YES, smeshBuilder.Mode_ONLY |

### SetSmoothOffSlivers()

```python
def SetSmoothOffSlivers(self, toSmooth)
```

Activate smoothing sliver elements:

Parameters
:   |  |  |
    | --- | --- |
    | toSmooth | - Boolean flag |

### SetPThreadsMode()

```python
def SetPThreadsMode(self, mode)
```

Set multithread mode.

Parameters
:   |  |  |
    | --- | --- |
    | mode | - the mode, one of the following values: smeshBuilder.Mode_SAFE, smeshBuilder.Mode_AGGRESSIVE, smeshBuilder.Mode_NONE (default) |

### SetMaximalNumberOfThreads()

```python
def SetMaximalNumberOfThreads(self, nb)
```

Set maximal number of threads.

Parameters
:   |  |  |
    | --- | --- |
    | nb | - number of threads |

### SetOptimizationLevel()

```python
def SetOptimizationLevel(self, level)
```

Set Optimization level:

Parameters
:   |  |  |
    | --- | --- |
    | level | optimization level, one of the following values  - None_Optimization - Light_Optimization - Standard_Optimization - StandardPlus_Optimization - Strong_Optimization.  Default is Standard_Optimization |

### SetMaximumMemory()

```python
def SetMaximumMemory(self, MB)
```

Set maximal size of memory to be used by the algorithm (in Megabytes).

Parameters
:   |  |  |
    | --- | --- |
    | MB | maximal size of memory |

### SetInitialMemory()

```python
def SetInitialMemory(self, MB)
```

Set initial size of memory to be used by the algorithm (in Megabytes) in automatic memory adjustment mode.

Parameters
:   |  |  |
    | --- | --- |
    | MB | initial size of memory |

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

### SetAdvancedOption()

```python
def SetAdvancedOption(self, option)
```

Sets command line option as text.

Parameters
:   |  |  |
    | --- | --- |
    | option | command line option |

### SetMinSize()

```python
def SetMinSize(self, theMinSize) inherited
```

Set lower boundary of mesh element size Set it to zero to deactivate this option.

### SetMaxSize()

```python
def SetMaxSize(self, theMaxSize) inherited
```

Set upper boundary of mesh element size Set it to zero to deactivate this option.

### SetVolumeProximity()

```python
def SetVolumeProximity(self, toUse) inherited
```

Activate/deactivate volume proximity computation.

### SetNbVolumeProximityLayers()

```python
def SetNbVolumeProximityLayers(self, nbLayers) inherited
```

Set number of surface element layers to be generated due to volume proximity.

### SetToMeshHoles()

```python
def SetToMeshHoles(self, toMesh) inherited
```

To mesh "holes" in a solid or not.

Default is to mesh.

Parameters
:   |  |  |
    | --- | --- |
    | toMesh | "mesh holes" flag value |

### SetToMakeGroupsOfDomains()

```python
def SetToMakeGroupsOfDomains(self, toMakeGroups) inherited
```

To make groups of volumes of different domains when mesh is generated from skin.

Default is to make groups. This option works only (1) for the mesh w/o shape and (2) if GetToMeshHoles() == true

Parameters
:   |  |  |
    | --- | --- |
    | toMakeGroups | "Make groups of domains" flag value |

### SetToUseBoundaryRecoveryVersion()

```python
def SetToUseBoundaryRecoveryVersion(self, toUse) inherited
```

To use boundary recovery version which tries to create mesh on a very poor quality surface mesh.

Parameters
:   |  |  |
    | --- | --- |
    | toUse | "use boundary recovery version" flag value |

### SetFEMCorrection()

```python
def SetFEMCorrection(self, toUseFem) inherited
```

Applies finite-element correction by replacing overconstrained elements where it is possible.

The process is cutting first the overconstrained edges and second the overconstrained facets. This insure that no edges have two boundary vertices and that no facets have three boundary vertices.

Parameters
:   |  |  |
    | --- | --- |
    | toUseFem | "apply finite-element correction" flag value |

### SetToRemoveCentralPoint()

```python
def SetToRemoveCentralPoint(self, toRemove) inherited
```

To remove initial central point.

Parameters
:   |  |  |
    | --- | --- |
    | toRemove | "remove initial central point" flag value |

### SetAlgorithm()

```python
def SetAlgorithm(self, algoId) inherited
```

To set the algorithm id.

Parameters
:   |  |  |
    | --- | --- |
    | algorithm | ID 0 MGTetra HPC - 1 MGTetra |

### SetUseNumOfThreads()

```python
def SetUseNumOfThreads(self, useThreads) inherited
```

To use parallel mode.

Parameters
:   |  |  |
    | --- | --- |
    | toUseNumOfThreads | "use max number of threads" flag value |

### SetNumOfThreads()

```python
def SetNumOfThreads(self, numThreads) inherited
```

To set the number of threads to be used.

Parameters
:   |  |  |
    | --- | --- |
    | numberOfThreads | define max_num_threads for MGTetra and MGTetra HPC |

### SetPthreadMode() [1/2]

```python
def SetPthreadMode(self, pthreadMode) inherited
```

Set SetPthreadMode.

Parameters
:   |  |  |
    | --- | --- |
    | pthreadMode | for parallel algorithm in MGTetra  - 0 - none - 1 - aggresive - 2 - safe |

### SetPthreadMode() [2/2]

```python
def SetPthreadMode(self, parallelMode) inherited
```

Set SetParallelMode.

Parameters
:   |  |  |
    | --- | --- |
    | parallelMode | for parallel algorithm in MGTetra HPC  - 0 - none - 1 - reproducible_given_max_number_of_threads - 2 - reproducible - 3 - aggressive |

### SetEnforcedVertex()

```python
def SetEnforcedVertex(self, x, y, z, size, vertexName = "", groupName = "") inherited
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
def SetEnforcedVertexGeom(self, theVertex, size, groupName = "") inherited
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
def RemoveEnforcedVertex(self, x, y, z) inherited
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
def RemoveEnforcedVertexGeom(self, theVertex) inherited
```

To remove an enforced vertex given a GEOM vertex, group or compound.

Parameters
:   |  |  |
    | --- | --- |
    | theVertex | : GEOM vertex (or group, compound) to be projected on theFace. |

### SetEnforcedMesh()

```python
def SetEnforcedMesh(self, theSource, elementType, size = -1, groupName = "") inherited
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
def SetOptionValue(self, optionName, optionValue) inherited
```

Set advanced option value.

Parameters
:   |  |  |
    | --- | --- |
    | optionName | option name |
    | optionValue | option value |

### SetTextOption()

```python
def SetTextOption(self, option) inherited
```

OBSOLETE Sets command line option as text.

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
algoType = MG_Tetra_Optimization static
```

type of algorithm used with helper function in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### docHelper

```python
string docHelper = "Creates MG-Tetra optimizer of tetrahedral meshes" static
```

doc string of the method in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### params

```python
params
```
