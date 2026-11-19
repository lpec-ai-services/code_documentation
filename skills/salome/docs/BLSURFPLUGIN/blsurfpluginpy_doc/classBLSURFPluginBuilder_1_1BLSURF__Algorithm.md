<!-- source: https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurfpluginpy_doc/classBLSURFPluginBuilder_1_1BLSURF__Algorithm.html -->

# BLSURF_Algorithm Class Reference

MG-CADSurf 2D algorithm.
[More...](classBLSURFPluginBuilder_1_1BLSURF__Algorithm.md#details)

## Detailed Description

MG-CADSurf 2D algorithm.

It can be created by calling [smeshBuilder.Mesh.Triangle](classsmeshBuilder_1_1Mesh.md#a58d92bcd67822a8ea2a782177e9a41a4)(smeshBuilder.MG-CADSurf,geom=0)

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

### SetPhysicalMesh()

```python
def SetPhysicalMesh(self, thePhysicalMesh = DefaultSize)
```

Sets a way to define size of mesh elements to generate.

Parameters
:   |  |  |
    | --- | --- |
    | thePhysicalMesh | is: DefaultSize, MG_CADSURF_Custom or SizeMap. |

### SetGeometricMesh()

```python
def SetGeometricMesh(self, theGeometricMesh = DefaultGeom)
```

Sets a way to define maximum angular deflection of mesh from CAD model.

Parameters
:   |  |  |
    | --- | --- |
    | theGeometricMesh | is: DefaultGeom (0)) or MG_CADSURF_GlobalSize (1)) |

### SetPhySize()

```python
def SetPhySize(self, theVal, isRelative = False)
```

Sets size of mesh elements to generate.

Parameters
:   |  |  |
    | --- | --- |
    | theVal | : constant global size when using a global physical size. |
    | isRelative | : if True, the value is relative to the length of the diagonal of the bounding box |

### SetMinSize()

```python
def SetMinSize(self, theVal = -1, isRelative = False)
```

Sets lower boundary of mesh element size.

Parameters
:   |  |  |
    | --- | --- |
    | theVal | : global minimal cell size desired. |
    | isRelative | : if True, the value is relative to the length of the diagonal of the bounding box |

### SetMaxSize()

```python
def SetMaxSize(self, theVal = -1, isRelative = False)
```

Sets upper boundary of mesh element size.

Parameters
:   |  |  |
    | --- | --- |
    | theVal | : global maximal cell size desired. |
    | isRelative | : if True, the value is relative to the length of the diagonal of the bounding box |

### SetAngleMesh()

```python
def SetAngleMesh(self, theVal = _geometric_approximation)
```

Sets angular deflection (in degrees) from CAD surface.

Parameters
:   |  |  |
    | --- | --- |
    | theVal | value of angular deflection |

### SetChordalError()

```python
def SetChordalError(self, distance)
```

Sets the maximum desired distance between a triangle and its supporting CAD surface.

Parameters
:   |  |  |
    | --- | --- |
    | distance | the distance between a triangle and a surface |

### SetGradation()

```python
def SetGradation(self, toUseGradation = True, theVal = _gradation)
```

Sets maximal allowed ratio between the lengths of two adjacent edges.

Parameters
:   |  |  |
    | --- | --- |
    | toUseGradation | to use gradation |
    | theVal | value of maximal length ratio |

### SetVolumeGradation()

```python
def SetVolumeGradation(self, toUseGradation = True, theVal = _gradation)
```

Sets maximal allowed ratio between the lengths of two adjacent edges in 3D mesh.

Parameters
:   |  |  |
    | --- | --- |
    | toUseGradation | to use gradation |
    | theVal | value of maximal length ratio |

### SetTopology()

```python
def SetTopology(self, way)
```

Sets topology usage way.

Parameters
:   |  |  |
    | --- | --- |
    | way | defines how mesh conformity is assured  - FromCAD - mesh conformity is assured by conformity of a shape - PreProcess or PreProcessPlus - by pre-processing a CAD model (OBSOLETE: FromCAD will be used) - PreCAD - by pre-processing with PreCAD a CAD model |

### SetSurfaceProximity()

```python
def SetSurfaceProximity(self, toUse)
```

Activate/deactivate surface proximity computation.

Parameters
:   |  |  |
    | --- | --- |
    | toUse | boolean flag |

### SetNbSurfaceProximityLayers()

```python
def SetNbSurfaceProximityLayers(self, nbLayers)
```

Set number of surface element layers to be generated due to surface proximity.

Parameters
:   |  |  |
    | --- | --- |
    | nbLayers | number of layers |

### SetSurfaceProximityRatio()

```python
def SetSurfaceProximityRatio(self, ratio)
```

Set coefficient by which size of element refined due to surface proximity is increased.

Parameters
:   |  |  |
    | --- | --- |
    | ratio | proximity coefficient |

### SetVolumeProximity()

```python
def SetVolumeProximity(self, toUse)
```

Activate/deactivate volume proximity computation.

Parameters
:   |  |  |
    | --- | --- |
    | toUse | boolean flag |

### SetNbVolumeProximityLayers()

```python
def SetNbVolumeProximityLayers(self, nbLayers)
```

Set number of surface element layers to be generated due to volume proximity.

Parameters
:   |  |  |
    | --- | --- |
    | nbLayers | number of layers |

### SetVolumeProximityRatio()

```python
def SetVolumeProximityRatio(self, ratio)
```

Set coefficient by which size of element refined due to volume proximity is increased.

Parameters
:   |  |  |
    | --- | --- |
    | ratio | proximity coefficient |

### SetVerbosity()

```python
def SetVerbosity(self, level)
```

Sets verbosity level in the range 0 to 10.

Parameters
:   |  |  |
    | --- | --- |
    | level | verbosity level |

### SetEnforceCadEdgesSize()

```python
def SetEnforceCadEdgesSize(self, toEnforce)
```

Set enforce_cad_edge_sizes parameter.

Relaxes the given sizemap constraint around CAD edges to allow a better element quality and a better geometric approximation. It is only useful in combination with the gradation option.

### SetJacobianRectificationRespectGeometry()

```python
def SetJacobianRectificationRespectGeometry(self, allowRectification)
```

Set jacobian_rectification_respect_geometry parameter.

While making the mesh quadratic, allows to lose the CAD-mesh associativity in order to correct elements with nagative Jacobian

### SetJacobianRectification()

```python
def SetJacobianRectification(self, allowRectification)
```

Set rectify_jacobian parameter.

While making the mesh quadratic, allow to fix nagative Jacobian surface elements

### SetUseDeprecatedPatchMesher()

```python
def SetUseDeprecatedPatchMesher(self, useDeprecatedPatchMesher)
```

Set use_deprecated_patch_mesher parameter (compatibility with older versions of Meshgems)

the use_deprecated_patch_mesher parameter allows to keep the same behaviour than in salome < 8.3 (meshgems 2.1.11 instead of meshgems >= 2.4.5)

### SetRespectGeometry() [1/2]

```python
def SetRespectGeometry(self, toRespect)
```

Set respect_geometry parameter.

This patch independent option can be deactivated to allow MeshGems-CADSurf to lower the geometry accuracy in its patch independent process.

### SetMaxNumberOfPointsPerPatch()

```python
def SetMaxNumberOfPointsPerPatch(self, nb)
```

Set max_number_of_points_per_patch parameter.

This parameter controls the maximum amount of points MeshGems-CADSurf is allowed to generate on a single CAD patch. For an automatic gestion of the memory, one can set this parameter to 0

### SetMaxNumberOfThreads()

```python
def SetMaxNumberOfThreads(self, nb)
```

Set max_number_of_threads parameter.

Set the maximum of threads to use for multithreading mesh computation

### SetRespectGeometry() [2/2]

```python
def SetRespectGeometry(self, toRespect)
```

Set respect_geometry parameter.

This patch independent option can be deactivated to allow MeshGems-CADSurf to lower the geometry accuracy in its patch independent process.

### SetTinyEdgesAvoidSurfaceIntersections()

```python
def SetTinyEdgesAvoidSurfaceIntersections(self, toAvoidIntersection)
```

Set tiny_edges_avoid_surface_intersections parameter.

This option defines the priority between the tiny feature suppression and the surface intersection prevention.

### SetClosedGeometry()

```python
def SetClosedGeometry(self, isClosed)
```

Set closed_geometry parameter parameter.

Describes whether the geometry is expected to be closed or not. When activated, this option helps MeshGems-PreCAD to treat the dirtiest geometries.

### SetDebug()

```python
def SetDebug(self, isDebug)
```

Set debug parameter.

Make MeshGems-CADSurf will be very verbose and will output some intermediate files in the working directory. This option is mainly meant for Distene support issues.

### SetPeriodicTolerance()

```python
def SetPeriodicTolerance(self, tol)
```

Set periodic_tolerance parameter.

This parameter defines the maximum size difference between two periodic edges and also the maximum distance error between two periodic entities.

### SetRequiredEntities()

```python
def SetRequiredEntities(self, howToTreat)
```

Set required_entities parameter.

The required entities control the correction operations. Accepted values for this parameter are :

- "respect" : MeshGems-CADSurf is not allowed to alter any required entity, even for correction purposes,
- "ignore" : MeshGems-CADSurf will ignore the required entities in its processing,
- "clear" : MeshGems-CADSurf will clear any required status for the entities. There will not be any entity marked as required in the generated mesh.

### SetSewingTolerance()

```python
def SetSewingTolerance(self, tol)
```

Set sewing_tolerance parameter.

This parameter is the tolerance of the assembly.

### SetTags()

```python
def SetTags(self, howToTreat)
```

Set tags parameter.

The tag (attribute) system controls the optimisation process. Accepted values for this parameter are :

- "respect" : the CAD tags will be preserved and unaltered by the optimisation operations,
- "ignore" : the CAD tags will be ignored by the optimisation operations but they will still be present in the output mesh,
- "clear" : MeshGems-CADSurf will clear any tag on any entity and optimise accordingly. There will not be any tag in the generated mesh.

### SetPatchIndependent()

```python
def SetPatchIndependent(self, isIndependent)
```

Activate/deactivate fully patch independent meshing.

Parameters
:   |  |  |
    | --- | --- |
    | isIndependent | boolean flag |

This feature can only be used if the *tags* parameter is set to "respect". By default this option deactivated.

### SetComputeRidges()

```python
def SetComputeRidges(self, toCompute)
```

Set to preserve lines defined by a sharp angle in the input discrete geometry.

Parameters
:   |  |  |
    | --- | --- |
    | toCompute | boolean flag |

If this option is deactivated, MeshGems-CADSurf will not try to preserve lines defined by a sharp angle in the input discrete geometry. Only input ridges, free edges, non manifold edges and separation betwen zones with different attributes will be respected (if tags is set to respect). By default this option activated.

### SetOptimiseTinyEdges()

```python
def SetOptimiseTinyEdges(self, toOptimise, length = -1)
```

Activate removal of the tiny edges from the generated mesh when it improves the local mesh quality, without taking into account the tags (attributes) specifications.

Parameters
:   |  |  |
    | --- | --- |
    | toOptimise | "to optimize" flag value |
    | length | minimal length under which an edge is considered to be a tiny |

### SetCorrectSurfaceIntersection()

```python
def SetCorrectSurfaceIntersection(self, toCorrect, maxCost)
```

Activate correction of all surface intersections.

Parameters
:   |  |  |
    | --- | --- |
    | toCorrect | "to correct" flag value |
    | maxCost | the time the user is ready to spend in the intersection prevention process For example, maxCost = 3 means that MeshGems-CADSurf will not spend more time in the intersection removal process than 3 times the time required to mesh without processing the intersections. |

### SetPreCADMergeEdges()

```python
def SetPreCADMergeEdges(self, toMergeEdges = False)
```

To optimize merges edges.

Parameters
:   |  |  |
    | --- | --- |
    | toMergeEdges | "merge edges" flag value |

### SetPreCADRemoveDuplicateCADFaces()

```python
def SetPreCADRemoveDuplicateCADFaces(self, toRemoveDuplicateCADFaces = False)
```

To remove duplicate CAD Faces.

Parameters
:   |  |  |
    | --- | --- |
    | toRemoveDuplicateCADFaces | "remove_duplicate_cad_faces" flag value |

### SetPreCADProcess3DTopology()

```python
def SetPreCADProcess3DTopology(self, toProcess = False)
```

To process 3D topology.

Parameters
:   |  |  |
    | --- | --- |
    | toProcess | "PreCAD process 3D" flag value |

### SetPreCADRemoveNanoEdges()

```python
def SetPreCADRemoveNanoEdges(self, toRemoveNanoEdges = False)
```

To remove nano edges.

Parameters
:   |  |  |
    | --- | --- |
    | toRemoveNanoEdges | "remove nano edges" flag value |

### SetPreCADDiscardInput()

```python
def SetPreCADDiscardInput(self, toDiscardInput = False)
```

To compute topology from scratch.

Parameters
:   |  |  |
    | --- | --- |
    | toDiscardInput | "discard input" flag value |

### SetPreCADEpsNano()

```python
def SetPreCADEpsNano(self, epsNano)
```

Sets the length below which an edge is considered as nano for the topology processing.

Parameters
:   |  |  |
    | --- | --- |
    | epsNano | nano edge length threshold value |

### SetOptionValue()

```python
def SetOptionValue(self, optionName, level)
```

Sets advanced option value.

Parameters
:   |  |  |
    | --- | --- |
    | optionName | advanced option name |
    | level | advanced option value |

### SetPreCADOptionValue()

```python
def SetPreCADOptionValue(self, optionName, optionValue)
```

Sets advanced PreCAD option value.

Parameters
:   |  |  |
    | --- | --- |
    | optionName | name of the option |
    | optionValue | value of the option |

### SetAdvancedOption()

```python
def SetAdvancedOption(self, optionsAndValues)
```

Adds custom advanced option values.

Parameters
:   |  |  |
    | --- | --- |
    | optionsAndValues | options and values in a form "option_1 v1 option_2 v2'" |

### AddOption()

```python
def AddOption(self, optionName, level)
```

Adds custom advanced option value.

Parameters
:   |  |  |
    | --- | --- |
    | optionName | custom advanced option name |
    | level | custom advanced option value |

### AddPreCADOption()

```python
def AddPreCADOption(self, optionName, optionValue)
```

Adds custom advanced PreCAD option value.

Parameters
:   |  |  |
    | --- | --- |
    | optionName | custom name of the option |
    | optionValue | value of the option |

### SetGMFFile()

```python
def SetGMFFile(self, fileName)
```

Sets GMF file for export at computation.

Parameters
:   |  |  |
    | --- | --- |
    | fileName | GMF file name |

### GetAllEnforcedVertices()

```python
def GetAllEnforcedVertices(self)
```

To get all the enforced vertices.

### GetAllEnforcedVerticesByFace()

```python
def GetAllEnforcedVerticesByFace(self)
```

To get all the enforced vertices sorted by face (or group, compound)

### GetAllEnforcedVerticesByCoords()

```python
def GetAllEnforcedVerticesByCoords(self)
```

To get all the enforced vertices sorted by coords of input vertices.

### GetAllCoordsByFace()

```python
def GetAllCoordsByFace(self)
```

To get all the coords of input vertices sorted by face (or group, compound)

### GetEnforcedVertices()

```python
def GetEnforcedVertices(self, theFace)
```

To get all the enforced vertices on a face (or group, compound)

Parameters
:   |  |  |
    | --- | --- |
    | theFace | : GEOM face (or group, compound) on which to define an enforced vertex |

### ClearAllEnforcedVertices()

```python
def ClearAllEnforcedVertices(self)
```

To clear all the enforced vertices.

### SetEnforcedVertex()

```python
def SetEnforcedVertex(self, theFace, x, y, z, vertexName = "", groupName = "")
```

To set an enforced vertex on a face (or group, compound) given the coordinates of a point.

If the point is not on the face, it will projected on it. If there is no projection, no enforced vertex is created.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | : GEOM face (or group, compound) on which to define an enforced vertex |
    | x | : x coordinate |
    | y | : y coordinate |
    | z | : z coordinate |
    | vertexName | : name of the enforced vertex |
    | groupName | : name of the group |

### SetEnforcedVertexGeom()

```python
def SetEnforcedVertexGeom(self, theFace, theVertex, groupName = "")
```

To set an enforced vertex on a face (or group, compound) given a GEOM vertex, group or compound.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | : GEOM face (or group, compound) on which to define an enforced vertex |
    | theVertex | : GEOM vertex (or group, compound) to be projected on theFace. |
    | groupName | : name of the group |

### AddEnforcedVertex()

```python
def AddEnforcedVertex(self, x, y, z, vertexName = "", groupName = "")
```

Set an enforced vertex on a face given the coordinates of a point.

The face if found by the application.

Parameters
:   |  |  |
    | --- | --- |
    | x | : x coordinate |
    | y | : y coordinate |
    | z | : z coordinate |
    | vertexName | : name of the enforced vertex |
    | groupName | : name of the group |

### AddEnforcedVertexGeom()

```python
def AddEnforcedVertexGeom(self, theVertex, groupName = "")
```

To set an enforced vertex on a face given a GEOM vertex, group or compound.

The face if found by the application.

Parameters
:   |  |  |
    | --- | --- |
    | theVertex | : GEOM vertex (or group, compound). |
    | groupName | : name of the group |

### UnsetEnforcedVertex()

```python
def UnsetEnforcedVertex(self, theFace, x, y, z)
```

To remove an enforced vertex on a given GEOM face (or group, compound) given the coordinates.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | : GEOM face (or group, compound) on which to remove the enforced vertex |
    | x | : x coordinate |
    | y | : y coordinate |
    | z | : z coordinate |

### UnsetEnforcedVertexGeom()

```python
def UnsetEnforcedVertexGeom(self, theFace, theVertex)
```

To remove an enforced vertex on a given GEOM face (or group, compound) given a GEOM vertex, group or compound.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | : GEOM face (or group, compound) on which to remove the enforced vertex |
    | theVertex | : GEOM vertex (or group, compound) to remove. |

### UnsetEnforcedVertices()

```python
def UnsetEnforcedVertices(self, theFace)
```

To remove all enforced vertices on a given face.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | : face (or group/compound of faces) on which to remove all enforced vertices |

### SetInternalEnforcedVertexAllFaces()

```python
def SetInternalEnforcedVertexAllFaces(self, toEnforceInternalVertices)
```

To tell BLSURF to add a node on internal vertices.

Parameters
:   |  |  |
    | --- | --- |
    | toEnforceInternalVertices | : boolean; if True the internal vertices are added as enforced vertices |

### GetInternalEnforcedVertexAllFaces()

```python
def GetInternalEnforcedVertexAllFaces(self)
```

To know if BLSURF will add a node on internal vertices.

### SetInternalEnforcedVertexAllFacesGroup()

```python
def SetInternalEnforcedVertexAllFacesGroup(self, groupName)
```

To define a group for the nodes of internal vertices.

Parameters
:   |  |  |
    | --- | --- |
    | groupName | : string; name of the group |

### GetInternalEnforcedVertexAllFacesGroup()

```python
def GetInternalEnforcedVertexAllFacesGroup(self)
```

To get the group name of the nodes of internal vertices.

### SetEnforcedMeshes()

```python
def SetEnforcedMeshes(self, enfMeshes)
```

Set enforced 1D meshes.

Parameters
:   |  |  |
    | --- | --- |
    | enfMeshes | : list of smeshBuilder.MG_EnforcedMesh1D structures |

Example: cadsurf.SetEnforcedMeshes([ smeshBuilder.MG_EnforcedMesh1D( mesh1D, "Group 1D")]

### SetAttractorGeom()

```python
def SetAttractorGeom(self, theFace, theAttractor, theStartSize, theEndSize, theInfluenceDistance, theConstantSizeDistance)
```

Sets an attractor on the chosen face.

The mesh size will decrease exponentially with the distance from theAttractor, following the rule h(d) = theEndSize - (theEndSize - theStartSize) * exp [ - ( d / theInfluenceDistance ) ^ 2 ]

Parameters
:   |  |  |
    | --- | --- |
    | theFace | : face on which the attractor will be defined |
    | theAttractor | : geometrical object from which the mesh size "h" decreases exponentially |
    | theStartSize | : mesh size on theAttractor |
    | theEndSize | : maximum size that will be reached on theFace |
    | theInfluenceDistance | : influence of the attractor ( the size grow slower on theFace if it's high) |
    | theConstantSizeDistance | : distance until which the mesh size will be kept constant on theFace |

### UnsetAttractorGeom()

```python
def UnsetAttractorGeom(self, theFace)
```

Unsets an attractor on the chosen face.

Parameters
:   |  |  |
    | --- | --- |
    | theFace | : face on which the attractor has to be removed |

### SetSizeMap()

```python
def SetSizeMap(self, theObject, theSizeMap)
```

To set a size map on a face, edge or vertex (or group, compound) given Python function.

If theObject is a face, the function can be: def f(u,v): return u+v If theObject is an edge, the function can be: def f(t): return t/2 If theObject is a vertex, the function can be: def f(): return 10

Parameters
:   |  |  |
    | --- | --- |
    | theObject | : GEOM face, edge or vertex (or group, compound) on which to define a size map |
    | theSizeMap | : Size map defined as a string |

### SetConstantSizeMap()

```python
def SetConstantSizeMap(self, theObject, theSizeMap)
```

To set a constant size map on a face, edge or vertex (or group, compound).

Parameters
:   |  |  |
    | --- | --- |
    | theObject | : GEOM face, edge or vertex (or group, compound) on which to define a size map |
    | theSizeMap | : Size map defined as a double |

### UnsetSizeMap()

```python
def UnsetSizeMap(self, theObject)
```

To remove a size map defined on a face, edge or vertex (or group, compound)

Parameters
:   |  |  |
    | --- | --- |
    | theObject | : GEOM face, edge or vertex (or group, compound) on which to define a size map |

### ClearSizeMaps()

```python
def ClearSizeMaps(self)
```

To remove all the size maps.

### SetQuadAllowed()

```python
def SetQuadAllowed(self, toAllow = True)
```

Sets QuadAllowed flag (DEPRECATED: use SetElementType)

Parameters
:   |  |  |
    | --- | --- |
    | toAllow | "allow quadrangles" flag value TODO: to remove in Salome 9 |

### SetElementType()

```python
def SetElementType(self, theElementType = Triangles)
```

Sets elements type.

Parameters
:   |  |  |
    | --- | --- |
    | theElementType | 0 (Triangles), 1 (QuadrangleDominant), 2 (Quadrangles) |

### Parameters()

```python
def Parameters(self)
```

Defines hypothesis having several parameters.

Returns
:   hypothesis object

### AddPreCadFacesPeriodicity()

```python
def AddPreCadFacesPeriodicity(self, theFace1, theFace2, theSourceVertices = [], theTargetVertices = [])
```

Defines periodicity between two groups of faces, using PreCAD.

Parameters
:   |  |  |
    | --- | --- |
    | theFace1 | : GEOM face (or group, compound) to associate with theFace2 |
    | theFace2 | : GEOM face (or group, compound) associated with theFace1 |
    | theSourceVertices | (optionnal): list of GEOM vertices on theFace1 defining the transformation from theFace1 to theFace2. If None, PreCAD tries to find a simple translation. Else, need at least 3 not aligned vertices. |
    | theTargetVertices | (optionnal): list of GEOM vertices on theFace2 defining the transformation from theFace1 to theFace2. If None, PreCAD tries to find a simple translation. Else, need at least 3 not aligned vertices. |

### AddPreCadEdgesPeriodicity()

```python
def AddPreCadEdgesPeriodicity(self, theEdge1, theEdge2, theSourceVertices = [], theTargetVertices = [])
```

Defines periodicity between two groups of edges, using PreCAD.

Parameters
:   |  |  |
    | --- | --- |
    | theEdge1 | : GEOM edge (or group, compound) to associate with theEdge2 |
    | theEdge2 | : GEOM edge (or group, compound) associated with theEdge1 |
    | theSourceVertices | (optionnal): list of GEOM vertices on theEdge1 defining the transformation from theEdge1 to theEdge2. If None, PreCAD tries to find a simple translation. Else, need at least 3 not aligned vertices. |
    | theTargetVertices | (optionnal): list of GEOM vertices on theEdge2 defining the transformation from theEdge1 to theEdge2. If None, PreCAD tries to find a simple translation. Else, need at least 3 not aligned vertices. |

### SetHyperPatches()

```python
def SetHyperPatches(self, hyperPatchList)
```

Defines hyper-patches.

A hyper-patch is a set of adjacent faces meshed as a whole, ignoring edges between them

Parameters
:   |  |  |
    | --- | --- |
    | hyperPatchList | : list of hyper-patches. A hyper-patch is defined as a list of faces or groups of faces. A face can be identified either as a GEOM object or a face ID (returned e.g. by geompy.GetSubShapeID( mainShape, subShape )). |

Example: cadsurf.SetHyperPatches([[ Face_1, Group_2 ],[ 13, 23 ]])

## Field Documentation

### meshMethod

```python
string meshMethod = "Triangle" static
```

name of the dynamic method in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### algoType

```python
algoType = MG_CADSurf static
```

type of algorithm used with helper function in [smeshBuilder.Mesh](classsmeshBuilder_1_1Mesh.md) class

### docHelper

```python
string docHelper = "Creates triangle algorithm for faces" static
```

doc string of the method

### _anisotropic_ratio

```python
int _anisotropic_ratio = 0 static private
```

### _bad_surface_element_aspect_ratio

```python
int _bad_surface_element_aspect_ratio = 1000 static private
```

### _geometric_approximation

```python
int _geometric_approximation = 22 static private
```

### _gradation

```python
float _gradation = 1.3 static private
```

### _volume_gradation

```python
int _volume_gradation = 2 static private
```

### _metric

```python
string _metric = "isotropic" static private
```

### _remove_tiny_edges

```python
int _remove_tiny_edges = 0 static private
```

### params

```python
params
```

### geompyD

```python
geompyD
```
