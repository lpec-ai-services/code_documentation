<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/modules.html -->

# Structured documentation

## Creating meshes

|  |  |
| --- | --- |
| [`smeshBuilder.Concatenate`](smeshBuilder.md#smeshBuilder.smeshBuilder.Concatenate)(meshes, ...[, ...]) | Concatenate the given meshes into one mesh, optionally to meshToAppendTo. |
| [`smeshBuilder.CopyMesh`](smeshBuilder.md#smeshBuilder.smeshBuilder.CopyMesh)(meshPart, meshName[, ...]) | Create a mesh by copying a part of another mesh. |

### Importing and exporting meshes

|  |  |
| --- | --- |
| [`smeshBuilder.CreateMeshesFromUNV`](smeshBuilder.md#smeshBuilder.smeshBuilder.CreateMeshesFromUNV)(theFileName) | Create a Mesh object importing data from the given UNV file |
| [`smeshBuilder.CreateMeshesFromMED`](smeshBuilder.md#smeshBuilder.smeshBuilder.CreateMeshesFromMED)(theFileName) | Create a Mesh object(s) importing data from the given MED file |
| [`smeshBuilder.CreateMeshesFromSTL`](smeshBuilder.md#smeshBuilder.smeshBuilder.CreateMeshesFromSTL)(theFileName) | Create a Mesh object importing data from the given STL file |
| [`smeshBuilder.CreateMeshesFromCGNS`](smeshBuilder.md#smeshBuilder.smeshBuilder.CreateMeshesFromCGNS)(theFileName) | Create Mesh objects importing data from the given CGNS file |
| [`smeshBuilder.CreateMeshesFromGMF`](smeshBuilder.md#smeshBuilder.smeshBuilder.CreateMeshesFromGMF)(theFileName) | Create a Mesh object importing data from the given GMF file. |
| [`Mesh.ExportMED`](smeshBuilder.md#smeshBuilder.Mesh.ExportMED)(*args, **kwargs) | Export the mesh in a file in MED format allowing to overwrite the file if it exists or add the exported data to its contents |
| [`Mesh.ExportUNV`](smeshBuilder.md#smeshBuilder.Mesh.ExportUNV)(f[, meshPart, renumber]) | Export the mesh in a file in UNV format |
| [`Mesh.ExportSTL`](smeshBuilder.md#smeshBuilder.Mesh.ExportSTL)(f[, ascii, meshPart]) | Export the mesh in a file in STL format |
| [`Mesh.ExportCGNS`](smeshBuilder.md#smeshBuilder.Mesh.ExportCGNS)(f[, overwrite, meshPart, ...]) | Export the mesh in a file in CGNS format |
| [`Mesh.ExportDAT`](smeshBuilder.md#smeshBuilder.Mesh.ExportDAT)(f[, meshPart, renumber]) | Export the mesh in a file in DAT format |
| [`Mesh.ExportGMF`](smeshBuilder.md#smeshBuilder.Mesh.ExportGMF)(f[, meshPart]) | Export the mesh in a file in GMF format. |

### Constructing meshes

|  |  |
| --- | --- |
| [`smeshBuilder.Mesh`](smeshBuilder.md#smeshBuilder.smeshBuilder.Mesh)([obj, name]) | Create a mesh. |
| [`Mesh.SetName`](smeshBuilder.md#smeshBuilder.Mesh.SetName)(name) | Set a name to the mesh |
| [`Mesh.SetMeshOrder`](smeshBuilder.md#smeshBuilder.Mesh.SetMeshOrder)(submeshes) | Set priority of sub-meshes. |
| [`Mesh.Compute`](smeshBuilder.md#smeshBuilder.Mesh.Compute)([geom, discardModifs, refresh]) | Compute the mesh and return the status of the computation |
| [`Mesh.Evaluate`](smeshBuilder.md#smeshBuilder.Mesh.Evaluate)([geom]) | Evaluate size of prospective mesh on a shape |
| [`Mesh.Clear`](smeshBuilder.md#smeshBuilder.Mesh.Clear)([refresh]) | Remove all nodes and elements generated on geometry. |
| [`Mesh.GetMesh`](smeshBuilder.md#smeshBuilder.Mesh.GetMesh)() | Return the mesh, that is an encapsulated instance of [`SMESH.SMESH_Mesh`](smesh_module.md#SMESH.SMESH_Mesh) interface |
| [`Mesh.GetShape`](smeshBuilder.md#smeshBuilder.Mesh.GetShape)() | Return the shape associated to the mesh |
| [`Mesh.HasShapeToMesh`](smeshBuilder.md#smeshBuilder.Mesh.HasShapeToMesh)() | Return `True` if this mesh is based on geometry |
| [`Mesh.GetComputeErrors`](smeshBuilder.md#smeshBuilder.Mesh.GetComputeErrors)([shape]) | Return a list of error messages ([`SMESH.ComputeError`](smesh_module.md#SMESH.ComputeError)) of the last `Compute()` |
| [`Mesh.GetAlgoState`](smeshBuilder.md#smeshBuilder.Mesh.GetAlgoState)(theSubObject) | Return errors of hypotheses definition. |
| [`Mesh.GetFailedShapes`](smeshBuilder.md#smeshBuilder.Mesh.GetFailedShapes)([publish]) | Return a list of sub-shapes meshing of which failed, grouped into GEOM groups by error of an algorithm |
| [`Mesh.GetMeshOrder`](smeshBuilder.md#smeshBuilder.Mesh.GetMeshOrder)() | Return sub-mesh objects list in meshing order |

### Defining Algorithms

|  |  |
| --- | --- |
| [`Mesh.Segment`](smeshBuilder.md#smeshBuilder.Mesh.Segment)([geom_shape]) | Create segment 1D algorithm for edges |
| [`Mesh.Quadrangle`](smeshBuilder.md#smeshBuilder.Mesh.Quadrangle)([geom_shape]) | Create quadrangle 1D-2D algorithm for faces |
| [`Mesh.Hexahedron`](smeshBuilder.md#smeshBuilder.Mesh.Hexahedron)([geom_shape]) | Create hexahedron 3D algorithm for volumes |
| [`Mesh.Prism`](smeshBuilder.md#smeshBuilder.Mesh.Prism)([geom_shape]) | Create prism 3D algorithm for volumes |
| [`Mesh.BodyFitted`](smeshBuilder.md#smeshBuilder.Mesh.BodyFitted)([geom_shape]) | Create Body Fitting 3D algorithm for volumes |
| [`Mesh.Projection1D`](smeshBuilder.md#smeshBuilder.Mesh.Projection1D)([geom_shape]) | Create projection 1D algorithm for edges |
| [`Mesh.Projection2D`](smeshBuilder.md#smeshBuilder.Mesh.Projection2D)([geom_shape]) | Create projection 2D algorithm for faces |
| [`Mesh.Projection1D2D`](smeshBuilder.md#smeshBuilder.Mesh.Projection1D2D)([geom_shape]) | Create projection 1D-2D algorithm for faces |
| [`Mesh.Projection3D`](smeshBuilder.md#smeshBuilder.Mesh.Projection3D)([geom_shape]) | Create projection 3D algorithm for volumes |
| [`Mesh.UseExisting1DElements`](smeshBuilder.md#smeshBuilder.Mesh.UseExisting1DElements)([geom_shape]) | Create 1D algorithm for edges with reusing of existing mesh elements |
| [`Mesh.UseExisting2DElements`](smeshBuilder.md#smeshBuilder.Mesh.UseExisting2DElements)([geom_shape]) | Create 1D-2D algorithm for faces with reusing of existing mesh elements |
| [`Mesh.UseExistingSegments`](smeshBuilder.md#smeshBuilder.Mesh.UseExistingSegments)([geom_shape]) | Create 1D algorithm allowing batch meshing of edges |
| [`Mesh.UseExistingFaces`](smeshBuilder.md#smeshBuilder.Mesh.UseExistingFaces)([geom_shape]) | Create 2D algorithm allowing batch meshing of faces |
| [`Mesh.AutomaticTetrahedralization`](smeshBuilder.md#smeshBuilder.Mesh.AutomaticTetrahedralization)([fineness]) | Compute a tetrahedral mesh using AutomaticLength + Triangle + Tetrahedron |
| [`Mesh.AutomaticHexahedralization`](smeshBuilder.md#smeshBuilder.Mesh.AutomaticHexahedralization)([fineness]) | Compute an hexahedral mesh using AutomaticLength + Quadrangle + Hexahedron |
| [`smesh_algorithm.Mesh_Algorithm`](StdMeshersBuilder.md#smesh_algorithm.Mesh_Algorithm)() | The base class to define meshing algorithms |

### Defining hypotheses

#### 1D Meshing Hypotheses

|  |  |
| --- | --- |
| [`StdMeshersBuilder_Segment.NumberOfSegments`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment.NumberOfSegments)(n) | Defines "NumberOfSegments" hypothesis to cut an edge in a fixed number of segments |
| [`StdMeshersBuilder_Segment.LocalLength`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment.LocalLength)(l[, ...]) | Defines "LocalLength" hypothesis to cut an edge in several segments with the same length |
| [`StdMeshersBuilder_Segment.MaxSize`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment.MaxSize)([length, ...]) | Defines "MaxSize" hypothesis to cut an edge into segments not longer than given value |
| [`StdMeshersBuilder_Segment.Arithmetic1D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment.Arithmetic1D)(...) | Defines "Arithmetic1D" hypothesis to cut an edge in several segments with a length |
| [`StdMeshersBuilder_Segment.GeometricProgression`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment.GeometricProgression)(...) | Defines "GeometricProgression" hypothesis to cut an edge in several |
| [`StdMeshersBuilder_Segment.FixedPoints1D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment.FixedPoints1D)(points) | Defines "FixedPoints1D" hypothesis to cut an edge using parameter |
| [`StdMeshersBuilder_Segment.StartEndLength`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment.StartEndLength)(...) | Defines "StartEndLength" hypothesis to cut an edge in several segments with increasing geometric length |
| [`StdMeshersBuilder_Segment.Adaptive`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment.Adaptive)(minSize, ...) | Defines "Adaptive" hypothesis to cut an edge into segments keeping segment size within the given range and considering (1) deflection of segments from the edge and (2) distance from segments to closest edges and faces to have segment length not longer than two times shortest distances to edges and faces. |
| [`StdMeshersBuilder_Segment.Deflection1D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment.Deflection1D)(d[, ...]) | Defines "Deflection1D" hypothesis |
| [`StdMeshersBuilder_Segment.AutomaticLength`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment.AutomaticLength)([...]) | Defines "AutomaticLength" hypothesis |
| [`StdMeshersBuilder_Segment_Python.PythonSplit1D`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment_Python.PythonSplit1D)(n, func) | Defines "PythonSplit1D" hypothesis |

#### 2D Meshing Hypotheses

|  |  |
| --- | --- |
| [`StdMeshersBuilder_Quadrangle.QuadrangleParameters`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Quadrangle.QuadrangleParameters)([...]) | Defines "QuadrangleParameters" hypothesis |
| [`StdMeshersBuilder_Quadrangle.QuadranglePreference`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Quadrangle.QuadranglePreference)([...]) | Defines "QuadrangleParams" hypothesis with a type of quadrangulation that only |
| [`StdMeshersBuilder_Quadrangle.TrianglePreference`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Quadrangle.TrianglePreference)([...]) | Defines "QuadrangleParams" hypothesis with a type of quadrangulation that only |
| [`StdMeshersBuilder_Quadrangle.Reduced`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Quadrangle.Reduced)([...]) | Defines "QuadrangleParams" hypothesis with a type of quadrangulation that only |
| [`StdMeshersBuilder_Quadrangle.TriangleVertex`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Quadrangle.TriangleVertex)(vertex) | Defines "QuadrangleParams" hypothesis with QUAD_STANDARD type of quadrangulation |

#### Additional Hypotheses

|  |  |
| --- | --- |
| [`smesh_algorithm.Mesh_Algorithm.ViscousLayers`](StdMeshersBuilder.md#smesh_algorithm.Mesh_Algorithm.ViscousLayers)(...) | Defines "ViscousLayers" hypothesis to give parameters of layers of prisms to build near mesh boundary. |
| [`smesh_algorithm.Mesh_Algorithm.ViscousLayers2D`](StdMeshersBuilder.md#smesh_algorithm.Mesh_Algorithm.ViscousLayers2D)(...) | Defines "ViscousLayers2D" hypothesis to give parameters of layers of quadrilateral elements to build near mesh boundary. |
| [`StdMeshersBuilder.StdMeshersBuilder_Segment.Propagation`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment.Propagation)() | Defines "Propagation" hypothesis that propagates 1D hypotheses |
| [`StdMeshersBuilder.StdMeshersBuilder_Segment.PropagationOfDistribution`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment.PropagationOfDistribution)() | Defines "Propagation of Node Distribution" hypothesis that propagates |
| [`StdMeshersBuilder.StdMeshersBuilder_Segment.QuadraticMesh`](StdMeshersBuilder.md#StdMeshersBuilder.StdMeshersBuilder_Segment.QuadraticMesh)() | Defines "QuadraticMesh" hypothesis, forcing construction of quadratic edges. |

### Constructing sub-meshes

|  |  |
| --- | --- |
| [`Mesh.GetSubMesh`](smeshBuilder.md#smeshBuilder.Mesh.GetSubMesh)(geom, name) | Get a sub-mesh object associated to a *geom* geometrical object. |
| [`Mesh.ClearSubMesh`](smeshBuilder.md#smeshBuilder.Mesh.ClearSubMesh)(geomId[, refresh]) | Remove all nodes and elements of indicated shape |

### Editing Meshes

|  |  |
| --- | --- |
| [`Mesh.AddHypothesis`](smeshBuilder.md#smeshBuilder.Mesh.AddHypothesis)(hyp[, geom]) | Assign a hypothesis |
| [`Mesh.RemoveHypothesis`](smeshBuilder.md#smeshBuilder.Mesh.RemoveHypothesis)(hyp[, geom]) | Unassign a hypothesis |
| [`Mesh.RemoveGlobalHypotheses`](smeshBuilder.md#smeshBuilder.Mesh.RemoveGlobalHypotheses)() | Remove all global hypotheses |
| [`Mesh.GetHypothesisList`](smeshBuilder.md#smeshBuilder.Mesh.GetHypothesisList)(geom) | Get the list of hypotheses added on a geometry |
| [`Mesh.IsUsedHypothesis`](smeshBuilder.md#smeshBuilder.Mesh.IsUsedHypothesis)(hyp, geom) | Return True if an algorithm or hypothesis is assigned to a given shape |

## Grouping elements

|  |  |
| --- | --- |
| [`Mesh.SetAutoColor`](smeshBuilder.md#smeshBuilder.Mesh.SetAutoColor)(theAutoColor) | Toggle auto color mode on the object. |
| [`Mesh.GetAutoColor`](smeshBuilder.md#smeshBuilder.Mesh.GetAutoColor)() | Get flag of object auto color mode. |
| [`Mesh.HasDuplicatedGroupNamesMED`](smeshBuilder.md#smeshBuilder.Mesh.HasDuplicatedGroupNamesMED)() | Check the group names for duplications. |

### Creating groups

|  |  |
| --- | --- |
| [`Mesh.CreateEmptyGroup`](smeshBuilder.md#smeshBuilder.Mesh.CreateEmptyGroup)(elementType, name) | Create an empty standalone mesh group |
| [`Mesh.Group`](smeshBuilder.md#smeshBuilder.Mesh.Group)(grp[, name]) | Create a mesh group based on the geometric object *grp* and give it a *name*. |
| [`Mesh.GroupOnGeom`](smeshBuilder.md#smeshBuilder.Mesh.GroupOnGeom)(grp[, name, typ]) | Create a mesh group based on the geometrical object *grp* and give it a *name*. |
| [`Mesh.GroupOnFilter`](smeshBuilder.md#smeshBuilder.Mesh.GroupOnFilter)(typ, name, filter) | Create a mesh group with given *name* based on the *filter*. |
| [`Mesh.MakeGroupByIds`](smeshBuilder.md#smeshBuilder.Mesh.MakeGroupByIds)(groupName, elementType, ...) | Create a mesh group by the given ids of elements |
| [`Mesh.MakeGroup`](smeshBuilder.md#smeshBuilder.Mesh.MakeGroup)(groupName, elementType[, ...]) | Create a mesh group by the given conditions |
| [`Mesh.MakeGroupByCriterion`](smeshBuilder.md#smeshBuilder.Mesh.MakeGroupByCriterion)(groupName, Criterion) | Create a mesh group by the given criterion |
| [`Mesh.MakeGroupByCriteria`](smeshBuilder.md#smeshBuilder.Mesh.MakeGroupByCriteria)(groupName, theCriteria) | Create a mesh group by the given criteria (list of [`SMESH.Filter.Criterion`](smesh_module.md#SMESH.Filter.Criterion)) |
| [`Mesh.MakeGroupByFilter`](smeshBuilder.md#smeshBuilder.Mesh.MakeGroupByFilter)(groupName, theFilter) | Create a mesh group by the given filter |
| [`Mesh.FaceGroupsSeparatedByEdges`](smeshBuilder.md#smeshBuilder.Mesh.FaceGroupsSeparatedByEdges)(sharpAngle) | Distribute all faces of the mesh among groups using sharp edges and optionally existing 1D elements as group boundaries. |
| [`Mesh.CreateDimGroup`](smeshBuilder.md#smeshBuilder.Mesh.CreateDimGroup)(groups, elemType, name) | Create a standalone group of entities basing on nodes of other groups. |
| [`Mesh.ConvertToStandalone`](smeshBuilder.md#smeshBuilder.Mesh.ConvertToStandalone)(group) | Convert group on geom into standalone group |
| [`Mesh.GetGroups`](smeshBuilder.md#smeshBuilder.Mesh.GetGroups)([elemType]) | Get the list of groups existing in the mesh in the order of creation (starting from the oldest one) |
| [`Mesh.NbGroups`](smeshBuilder.md#smeshBuilder.Mesh.NbGroups)() | Get the number of groups existing in the mesh |
| [`Mesh.GetGroupNames`](smeshBuilder.md#smeshBuilder.Mesh.GetGroupNames)() | Get the list of names of groups existing in the mesh |
| [`Mesh.GetGroupByName`](smeshBuilder.md#smeshBuilder.Mesh.GetGroupByName)(name[, elemType]) | Find groups by name and type |

### Operations on groups

|  |  |
| --- | --- |
| [`Mesh.UnionGroups`](smeshBuilder.md#smeshBuilder.Mesh.UnionGroups)(group1, group2, name) | Produce a union of two groups. |
| [`Mesh.UnionListOfGroups`](smeshBuilder.md#smeshBuilder.Mesh.UnionListOfGroups)(groups, name) | Produce a union list of groups. |
| [`Mesh.IntersectGroups`](smeshBuilder.md#smeshBuilder.Mesh.IntersectGroups)(group1, group2, name) | Prodice an intersection of two groups. |
| [`Mesh.IntersectListOfGroups`](smeshBuilder.md#smeshBuilder.Mesh.IntersectListOfGroups)(groups, name) | Produce an intersection of groups. |
| [`Mesh.CutGroups`](smeshBuilder.md#smeshBuilder.Mesh.CutGroups)(main_group, tool_group, name) | Produce a cut of two groups. |
| [`Mesh.CutListOfGroups`](smeshBuilder.md#smeshBuilder.Mesh.CutListOfGroups)(main_groups, ...) | Produce a cut of groups. |

### Deleting Groups

|  |  |
| --- | --- |
| [`Mesh.RemoveGroup`](smeshBuilder.md#smeshBuilder.Mesh.RemoveGroup)(group) | Remove a group |
| [`Mesh.RemoveGroupWithContents`](smeshBuilder.md#smeshBuilder.Mesh.RemoveGroupWithContents)(group) | Remove a group with its contents |

## Mesh Information

|  |  |
| --- | --- |
| [`smeshBuilder.GetMeshInfo`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetMeshInfo)(obj) | Get the mesh statistic. |
| [`Mesh.GetEngine`](smeshBuilder.md#smeshBuilder.Mesh.GetEngine)() | Return a smeshBuilder instance created this mesh |
| [`Mesh.GetGeomEngine`](smeshBuilder.md#smeshBuilder.Mesh.GetGeomEngine)() | Return a geomBuilder instance |
| [`Mesh.GetGeometryByMeshElement`](smeshBuilder.md#smeshBuilder.Mesh.GetGeometryByMeshElement)(theElementID, ...) | Return a geometrical object on which the given element was built. |
| [`Mesh.MeshDimension`](smeshBuilder.md#smeshBuilder.Mesh.MeshDimension)() | Return the mesh dimension depending on the dimension of the underlying shape or, if the mesh is not based on any shape, basing on deimension of elements |
| [`Mesh.GetMeshInfo`](smeshBuilder.md#smeshBuilder.Mesh.GetMeshInfo)([obj]) | Get the mesh statistic. |
| [`Mesh.NbNodes`](smeshBuilder.md#smeshBuilder.Mesh.NbNodes)() | Return the number of nodes in the mesh |
| [`Mesh.NbElements`](smeshBuilder.md#smeshBuilder.Mesh.NbElements)() | Return the number of elements in the mesh |
| [`Mesh.Nb0DElements`](smeshBuilder.md#smeshBuilder.Mesh.Nb0DElements)() | Return the number of 0d elements in the mesh |
| [`Mesh.NbBalls`](smeshBuilder.md#smeshBuilder.Mesh.NbBalls)() | Return the number of ball discrete elements in the mesh |
| [`Mesh.NbEdges`](smeshBuilder.md#smeshBuilder.Mesh.NbEdges)() | Return the number of edges in the mesh |
| [`Mesh.NbEdgesOfOrder`](smeshBuilder.md#smeshBuilder.Mesh.NbEdgesOfOrder)(elementOrder) | Return the number of edges with the given order in the mesh |
| [`Mesh.NbFaces`](smeshBuilder.md#smeshBuilder.Mesh.NbFaces)() | Return the number of faces in the mesh |
| [`Mesh.NbFacesOfOrder`](smeshBuilder.md#smeshBuilder.Mesh.NbFacesOfOrder)(elementOrder) | Return the number of faces with the given order in the mesh |
| [`Mesh.NbTriangles`](smeshBuilder.md#smeshBuilder.Mesh.NbTriangles)() | Return the number of triangles in the mesh |
| [`Mesh.NbTrianglesOfOrder`](smeshBuilder.md#smeshBuilder.Mesh.NbTrianglesOfOrder)(elementOrder) | Return the number of triangles with the given order in the mesh |
| [`Mesh.NbBiQuadTriangles`](smeshBuilder.md#smeshBuilder.Mesh.NbBiQuadTriangles)() | Return the number of biquadratic triangles in the mesh |
| [`Mesh.NbQuadrangles`](smeshBuilder.md#smeshBuilder.Mesh.NbQuadrangles)() | Return the number of quadrangles in the mesh |
| [`Mesh.NbQuadranglesOfOrder`](smeshBuilder.md#smeshBuilder.Mesh.NbQuadranglesOfOrder)(elementOrder) | Return the number of quadrangles with the given order in the mesh |
| [`Mesh.NbBiQuadQuadrangles`](smeshBuilder.md#smeshBuilder.Mesh.NbBiQuadQuadrangles)() | Return the number of biquadratic quadrangles in the mesh |
| [`Mesh.NbPolygons`](smeshBuilder.md#smeshBuilder.Mesh.NbPolygons)([elementOrder]) | Return the number of polygons of given order in the mesh |
| [`Mesh.NbVolumes`](smeshBuilder.md#smeshBuilder.Mesh.NbVolumes)() | Return the number of volumes in the mesh |
| [`Mesh.NbVolumesOfOrder`](smeshBuilder.md#smeshBuilder.Mesh.NbVolumesOfOrder)(elementOrder) | Return the number of volumes with the given order in the mesh |
| [`Mesh.NbTetras`](smeshBuilder.md#smeshBuilder.Mesh.NbTetras)() | Return the number of tetrahedrons in the mesh |
| [`Mesh.NbTetrasOfOrder`](smeshBuilder.md#smeshBuilder.Mesh.NbTetrasOfOrder)(elementOrder) | Return the number of tetrahedrons with the given order in the mesh |
| [`Mesh.NbHexas`](smeshBuilder.md#smeshBuilder.Mesh.NbHexas)() | Return the number of hexahedrons in the mesh |
| [`Mesh.NbHexasOfOrder`](smeshBuilder.md#smeshBuilder.Mesh.NbHexasOfOrder)(elementOrder) | Return the number of hexahedrons with the given order in the mesh |
| [`Mesh.NbTriQuadraticHexas`](smeshBuilder.md#smeshBuilder.Mesh.NbTriQuadraticHexas)() | Return the number of triquadratic hexahedrons in the mesh |
| [`Mesh.NbPyramids`](smeshBuilder.md#smeshBuilder.Mesh.NbPyramids)() | Return the number of pyramids in the mesh |
| [`Mesh.NbPyramidsOfOrder`](smeshBuilder.md#smeshBuilder.Mesh.NbPyramidsOfOrder)(elementOrder) | Return the number of pyramids with the given order in the mesh |
| [`Mesh.NbPrisms`](smeshBuilder.md#smeshBuilder.Mesh.NbPrisms)() | Return the number of prisms in the mesh |
| [`Mesh.NbPrismsOfOrder`](smeshBuilder.md#smeshBuilder.Mesh.NbPrismsOfOrder)(elementOrder) | Return the number of prisms with the given order in the mesh |
| [`Mesh.NbHexagonalPrisms`](smeshBuilder.md#smeshBuilder.Mesh.NbHexagonalPrisms)() | Return the number of hexagonal prisms in the mesh |
| [`Mesh.NbPolyhedrons`](smeshBuilder.md#smeshBuilder.Mesh.NbPolyhedrons)() | Return the number of polyhedrons in the mesh |
| [`Mesh.NbSubMesh`](smeshBuilder.md#smeshBuilder.Mesh.NbSubMesh)() | Return the number of submeshes in the mesh |
| [`Mesh.GetNodesId`](smeshBuilder.md#smeshBuilder.Mesh.GetNodesId)() | Return the list of mesh nodes IDs |
| [`Mesh.GetElementsId`](smeshBuilder.md#smeshBuilder.Mesh.GetElementsId)() | Return the list of all mesh elements IDs |
| [`Mesh.GetElementsByType`](smeshBuilder.md#smeshBuilder.Mesh.GetElementsByType)(elementType) | Return the list of IDs of mesh elements with the given type |
| [`Mesh.GetElementType`](smeshBuilder.md#smeshBuilder.Mesh.GetElementType)(id[, iselem]) | Return the type of mesh element or node |
| [`Mesh.GetElementGeomType`](smeshBuilder.md#smeshBuilder.Mesh.GetElementGeomType)(id) | Return the geometric type of mesh element |
| [`Mesh.GetElementShape`](smeshBuilder.md#smeshBuilder.Mesh.GetElementShape)(id) | Return the shape type of mesh element |
| [`Mesh.GetSubMeshElementsId`](smeshBuilder.md#smeshBuilder.Mesh.GetSubMeshElementsId)(Shape) | Return the list of sub-mesh elements IDs |
| [`Mesh.GetSubMeshNodesId`](smeshBuilder.md#smeshBuilder.Mesh.GetSubMeshNodesId)(Shape, all) | Return the list of sub-mesh nodes IDs |
| [`Mesh.GetSubMeshElementType`](smeshBuilder.md#smeshBuilder.Mesh.GetSubMeshElementType)(Shape) | Return type of elements on given shape |
| [`Mesh.GetNodeXYZ`](smeshBuilder.md#smeshBuilder.Mesh.GetNodeXYZ)(id) | Get XYZ coordinates of a node. |
| [`Mesh.GetNodeInverseElements`](smeshBuilder.md#smeshBuilder.Mesh.GetNodeInverseElements)(id[, elemType]) | Return list of IDs of inverse elements for the given node. |
| [`Mesh.GetNodePosition`](smeshBuilder.md#smeshBuilder.Mesh.GetNodePosition)(NodeID) | Return the position of a node on the shape |
| [`Mesh.GetElementPosition`](smeshBuilder.md#smeshBuilder.Mesh.GetElementPosition)(ElemID) | Return the position of an element on the shape |
| [`Mesh.GetShapeID`](smeshBuilder.md#smeshBuilder.Mesh.GetShapeID)(id) | Return the ID of the shape, on which the given node was generated. |
| [`Mesh.GetShapeIDForElem`](smeshBuilder.md#smeshBuilder.Mesh.GetShapeIDForElem)(id) | Return the ID of the shape, on which the given element was generated. |
| [`Mesh.GetElemNbNodes`](smeshBuilder.md#smeshBuilder.Mesh.GetElemNbNodes)(id) | Return the number of nodes of the given element |
| [`Mesh.GetElemNode`](smeshBuilder.md#smeshBuilder.Mesh.GetElemNode)(id, index) | Return the node ID the given (zero based) index for the given element. |
| [`Mesh.GetElemNodes`](smeshBuilder.md#smeshBuilder.Mesh.GetElemNodes)(id) | Return the IDs of nodes of the given element |
| [`Mesh.IsMediumNode`](smeshBuilder.md#smeshBuilder.Mesh.IsMediumNode)(elementID, nodeID) | Return true if the given node is the medium node in the given quadratic element |
| [`Mesh.IsMediumNodeOfAnyElem`](smeshBuilder.md#smeshBuilder.Mesh.IsMediumNodeOfAnyElem)(nodeID[, elementType]) | Return true if the given node is the medium node in one of quadratic elements |
| [`Mesh.ElemNbEdges`](smeshBuilder.md#smeshBuilder.Mesh.ElemNbEdges)(id) | Return the number of edges for the given element |
| [`Mesh.ElemNbFaces`](smeshBuilder.md#smeshBuilder.Mesh.ElemNbFaces)(id) | Return the number of faces for the given element |
| [`Mesh.GetElemFaceNodes`](smeshBuilder.md#smeshBuilder.Mesh.GetElemFaceNodes)(elemId, faceIndex) | Return nodes of given face (counted from zero) for given volumic element. |
| [`Mesh.GetFaceNormal`](smeshBuilder.md#smeshBuilder.Mesh.GetFaceNormal)(faceId[, normalized]) | Return three components of normal of given mesh face (or an empty array in KO case) |
| [`Mesh.FindElementByNodes`](smeshBuilder.md#smeshBuilder.Mesh.FindElementByNodes)(nodes) | Return an element based on all given nodes. |
| [`Mesh.GetElementsByNodes`](smeshBuilder.md#smeshBuilder.Mesh.GetElementsByNodes)(nodes[, elemType]) | Return elements including all given nodes. |
| [`Mesh.IsPoly`](smeshBuilder.md#smeshBuilder.Mesh.IsPoly)(id) | Return true if the given element is a polygon |
| [`Mesh.IsQuadratic`](smeshBuilder.md#smeshBuilder.Mesh.IsQuadratic)(id) | Return true if the given element is quadratic |
| [`Mesh.GetBallDiameter`](smeshBuilder.md#smeshBuilder.Mesh.GetBallDiameter)(id) | Return diameter of a ball discrete element or zero in case of an invalid *id* |
| [`Mesh.BaryCenter`](smeshBuilder.md#smeshBuilder.Mesh.BaryCenter)(id) | Return XYZ coordinates of the barycenter of the given element. |
| [`Mesh.FindNodeClosestTo`](smeshBuilder.md#smeshBuilder.Mesh.FindNodeClosestTo)(x, y, z) | Find the node closest to a point |
| [`Mesh.FindElementsByPoint`](smeshBuilder.md#smeshBuilder.Mesh.FindElementsByPoint)(x, y, z[, ...]) | Find the elements where a point lays IN or ON |
| [`Mesh.GetPointState`](smeshBuilder.md#smeshBuilder.Mesh.GetPointState)(x, y, z) | Return point state in a closed 2D mesh in terms of TopAbs_State enumeration: smesh.TopAbs_IN, smesh.TopAbs_OUT, smesh.TopAbs_ON and smesh.TopAbs_UNKNOWN. |
| [`Mesh.Get1DBranches`](smeshBuilder.md#smeshBuilder.Mesh.Get1DBranches)(edges[, startNode]) | Partition given 1D elements into groups of contiguous edges. |
| [`Mesh.Dump`](smeshBuilder.md#smeshBuilder.Mesh.Dump)() | Get the mesh description |

## Quality controls and Filtering

|  |  |
| --- | --- |
| [`smeshBuilder.GetEmptyCriterion`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetEmptyCriterion)() | Create an empty criterion |
| [`smeshBuilder.GetCriterion`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetCriterion)(elementType, CritType) | Create a criterion by the given parameters Criterion structures allow to define complex filters by combining them with logical operations (AND / OR) (see example below) |
| [`smeshBuilder.GetFilter`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetFilter)(elementType[, ...]) | Create a filter with the given parameters |
| [`smeshBuilder.GetFilterFromCriteria`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetFilterFromCriteria)(criteria) | Create a filter from criteria |
| [`smeshBuilder.GetFunctor`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetFunctor)(theCriterion) | Create a numerical functor by its type |
| [`Mesh.GetIdsFromFilter`](smeshBuilder.md#smeshBuilder.Mesh.GetIdsFromFilter)(filter[, meshParts]) | Pass mesh elements through the given filter and return IDs of fitting elements |
| [`Mesh.GetMaxElementLength`](smeshBuilder.md#smeshBuilder.Mesh.GetMaxElementLength)(elemId) | Get maximum element length. |
| [`Mesh.GetAspectRatio`](smeshBuilder.md#smeshBuilder.Mesh.GetAspectRatio)(elemId) | Get aspect ratio of 2D or 3D element. |
| [`Mesh.GetWarping`](smeshBuilder.md#smeshBuilder.Mesh.GetWarping)(elemId) | Get warping angle of 2D element. |
| [`Mesh.GetMinimumAngle`](smeshBuilder.md#smeshBuilder.Mesh.GetMinimumAngle)(elemId) | Get minimum angle of 2D element. |
| [`Mesh.GetTaper`](smeshBuilder.md#smeshBuilder.Mesh.GetTaper)(elemId) | Get taper of 2D element. |
| [`Mesh.GetSkew`](smeshBuilder.md#smeshBuilder.Mesh.GetSkew)(elemId) | Get skew of 2D element. |
| [`Mesh.GetMinMax`](smeshBuilder.md#smeshBuilder.Mesh.GetMinMax)(funType[, meshPart]) | Return minimal and maximal value of a given functor. |
| [`Mesh.IsManifold`](smeshBuilder.md#smeshBuilder.Mesh.IsManifold)() | Check if a 2D mesh is manifold |
| [`Mesh.IsCoherentOrientation2D`](smeshBuilder.md#smeshBuilder.Mesh.IsCoherentOrientation2D)() | Check if orientation of 2D elements is coherent |

## Measurements

|  |  |
| --- | --- |
| [`smeshBuilder.MinDistance`](smeshBuilder.md#smeshBuilder.smeshBuilder.MinDistance)(src1[, src2, id1, ...]) | Get minimum distance between two objects |
| [`smeshBuilder.GetMinDistance`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetMinDistance)(src1[, src2, ...]) | Get [`SMESH.Measure`](smesh_module.md#SMESH.Measure) structure specifying minimum distance data between two objects |
| [`smeshBuilder.BoundingBox`](smeshBuilder.md#smeshBuilder.smeshBuilder.BoundingBox)(objects) | Get bounding box of the specified object(s) |
| [`smeshBuilder.GetBoundingBox`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetBoundingBox)(objects) | Get [`SMESH.Measure`](smesh_module.md#SMESH.Measure) structure specifying bounding box data of the specified object(s) |
| [`smeshBuilder.GetLength`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetLength)(obj) | Get sum of lengths of all 1D elements in the mesh object. |
| [`smeshBuilder.GetArea`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetArea)(obj) | Get sum of areas of all 2D elements in the mesh object. |
| [`smeshBuilder.GetVolume`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetVolume)(obj) | Get sum of volumes of all 3D elements in the mesh object. |
| [`smeshBuilder.GetAngle`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetAngle)(p1, p2, p3) | Computes a radian measure of an angle defined by 3 points: <(p1,p2,p3) |
| [`Mesh.GetFreeBorders`](smeshBuilder.md#smeshBuilder.Mesh.GetFreeBorders)() | Verify whether a 2D mesh element has free edges (edges connected to one face only). |
| [`Mesh.MinDistance`](smeshBuilder.md#smeshBuilder.Mesh.MinDistance)(id1[, id2, isElem1, isElem2]) | Get minimum distance between two nodes, elements or distance to the origin |
| [`Mesh.GetMinDistance`](smeshBuilder.md#smeshBuilder.Mesh.GetMinDistance)(id1[, id2, isElem1, isElem2]) | Get [`SMESH.Measure`](smesh_module.md#SMESH.Measure) structure specifying minimum distance data between two objects |
| [`Mesh.BoundingBox`](smeshBuilder.md#smeshBuilder.Mesh.BoundingBox)([objects, isElem]) | Get bounding box of the specified object(s) |
| [`Mesh.GetBoundingBox`](smeshBuilder.md#smeshBuilder.Mesh.GetBoundingBox)([objects, isElem]) | Get [`SMESH.Measure`](smesh_module.md#SMESH.Measure) structure specifying bounding box data of the specified object(s) |
| [`Mesh.GetFunctor`](smeshBuilder.md#smeshBuilder.Mesh.GetFunctor)(funcType) | Return a cached numerical functor by its type. |
| [`Mesh.FunctorValue`](smeshBuilder.md#smeshBuilder.Mesh.FunctorValue)(funcType, elemId[, isElem]) | Return value of a functor for a given element |
| [`Mesh.GetLength`](smeshBuilder.md#smeshBuilder.Mesh.GetLength)([elemId]) | Get length of given 1D elements or of all 1D mesh elements |
| [`Mesh.GetArea`](smeshBuilder.md#smeshBuilder.Mesh.GetArea)([elemId]) | Get area of given 2D elements or of all 2D mesh elements |
| [`Mesh.GetVolume`](smeshBuilder.md#smeshBuilder.Mesh.GetVolume)([elemId]) | Get volume of given 3D elements or of all 3D mesh elements |
| [`Mesh.GetAngle`](smeshBuilder.md#smeshBuilder.Mesh.GetAngle)(node1, node2, node3) | Computes a radian measure of an angle defined by 3 nodes: <(node1,node2,node3) |

## Modifying meshes

|  |  |
| --- | --- |
| [`smeshBuilder.GetPattern`](smeshBuilder.md#smeshBuilder.smeshBuilder.GetPattern)() | Create a pattern mapper. |
| [`Mesh.GetMeshEditor`](smeshBuilder.md#smeshBuilder.Mesh.GetMeshEditor)() | Obtain the mesh editor tool |

### Adding nodes and elements

|  |  |
| --- | --- |
| [`Mesh.AddNode`](smeshBuilder.md#smeshBuilder.Mesh.AddNode)(x, y, z) | Add a node to the mesh by coordinates |
| [`Mesh.Add0DElement`](smeshBuilder.md#smeshBuilder.Mesh.Add0DElement)(IDOfNode[, DuplicateElements]) | Create a 0D element on a node with given number. |
| [`Mesh.Add0DElementsToAllNodes`](smeshBuilder.md#smeshBuilder.Mesh.Add0DElementsToAllNodes)(theObject[, ...]) | Create 0D elements on all nodes of the given elements except those nodes on which a 0D element already exists. |
| [`Mesh.AddBall`](smeshBuilder.md#smeshBuilder.Mesh.AddBall)(IDOfNode, diameter) | Create a ball element on a node with given ID. |
| [`Mesh.AddEdge`](smeshBuilder.md#smeshBuilder.Mesh.AddEdge)(IDsOfNodes) | Create a linear or quadratic edge (this is determined by the number of given nodes). |
| [`Mesh.AddFace`](smeshBuilder.md#smeshBuilder.Mesh.AddFace)(IDsOfNodes) | Create a linear or quadratic face (this is determined by the number of given nodes). |
| [`Mesh.AddPolygonalFace`](smeshBuilder.md#smeshBuilder.Mesh.AddPolygonalFace)(IdsOfNodes) | Add a polygonal face defined by a list of node IDs |
| [`Mesh.AddQuadPolygonalFace`](smeshBuilder.md#smeshBuilder.Mesh.AddQuadPolygonalFace)(IdsOfNodes) | Add a quadratic polygonal face defined by a list of node IDs |
| [`Mesh.AddVolume`](smeshBuilder.md#smeshBuilder.Mesh.AddVolume)(IDsOfNodes) | Create both simple and quadratic volume (this is determined by the number of given nodes). |
| [`Mesh.AddPolyhedralVolume`](smeshBuilder.md#smeshBuilder.Mesh.AddPolyhedralVolume)(IdsOfNodes, Quantities) | Create a volume of many faces, giving nodes for each face. |
| [`Mesh.AddPolyhedralVolumeByFaces`](smeshBuilder.md#smeshBuilder.Mesh.AddPolyhedralVolumeByFaces)(IdsOfFaces) | Create a volume of many faces, giving the IDs of the existing faces. |
| [`Mesh.SetNodeOnVertex`](smeshBuilder.md#smeshBuilder.Mesh.SetNodeOnVertex)(NodeID, Vertex) | Bind a node to a vertex |
| [`Mesh.SetNodeOnEdge`](smeshBuilder.md#smeshBuilder.Mesh.SetNodeOnEdge)(NodeID, Edge, paramOnEdge) | Store the node position on an edge |
| [`Mesh.SetNodeOnFace`](smeshBuilder.md#smeshBuilder.Mesh.SetNodeOnFace)(NodeID, Face, u, v) | Store node position on a face |
| [`Mesh.SetNodeInVolume`](smeshBuilder.md#smeshBuilder.Mesh.SetNodeInVolume)(NodeID, Solid) | Bind a node to a solid |
| [`Mesh.SetMeshElementOnShape`](smeshBuilder.md#smeshBuilder.Mesh.SetMeshElementOnShape)(ElementID, Shape) | Bind an element to a shape |
| [`Mesh.Make2DMeshFrom3D`](smeshBuilder.md#smeshBuilder.Mesh.Make2DMeshFrom3D)() | Create 2D mesh as skin on boundary faces of a 3D mesh |
| [`Mesh.MakeBoundaryMesh`](smeshBuilder.md#smeshBuilder.Mesh.MakeBoundaryMesh)(elements[, dimension, ...]) | Create missing boundary elements |
| [`Mesh.MakeBoundaryElements`](smeshBuilder.md#smeshBuilder.Mesh.MakeBoundaryElements)([dimension, ...]) | Create missing boundary elements around either the whole mesh or groups of elements |
| [`Mesh.Append`](smeshBuilder.md#smeshBuilder.Mesh.Append)(meshes[, uniteIdenticalGroups, ...]) | Append given meshes into this mesh. |
| [`Mesh.GetLastCreatedNodes`](smeshBuilder.md#smeshBuilder.Mesh.GetLastCreatedNodes)() | If during the last operation of [`SMESH.SMESH_MeshEditor`](smesh_module.md#SMESH.SMESH_MeshEditor) some nodes were created, this method return the list of their IDs. |
| [`Mesh.GetLastCreatedElems`](smeshBuilder.md#smeshBuilder.Mesh.GetLastCreatedElems)() | If during the last operation of [`SMESH.SMESH_MeshEditor`](smesh_module.md#SMESH.SMESH_MeshEditor) some elements were created this method return the list of their IDs. |
| [`Mesh.ClearLastCreated`](smeshBuilder.md#smeshBuilder.Mesh.ClearLastCreated)() | Forget what nodes and elements were created by the last mesh edition operation |

### Removing nodes and elements

|  |  |
| --- | --- |
| [`Mesh.RemoveElements`](smeshBuilder.md#smeshBuilder.Mesh.RemoveElements)(IDsOfElements) | Remove the elements from the mesh by ids |
| [`Mesh.RemoveNodes`](smeshBuilder.md#smeshBuilder.Mesh.RemoveNodes)(IDsOfNodes) | Remove nodes from mesh by ids |
| [`Mesh.RemoveNodeWithReconnection`](smeshBuilder.md#smeshBuilder.Mesh.RemoveNodeWithReconnection)(nodeID) | Remove a node along with changing surrounding faces to cover a hole. |
| [`Mesh.RemoveOrphanNodes`](smeshBuilder.md#smeshBuilder.Mesh.RemoveOrphanNodes)() | Remove all orphan (free) nodes from mesh |

### Modifying nodes and elements

|  |  |
| --- | --- |
| [`Mesh.MoveNode`](smeshBuilder.md#smeshBuilder.Mesh.MoveNode)(NodeID, x, y, z) | Move the node with the given id |
| [`Mesh.MoveClosestNodeToPoint`](smeshBuilder.md#smeshBuilder.Mesh.MoveClosestNodeToPoint)(x, y, z, NodeID) | Find the node closest to a point and moves it to a point location |
| [`Mesh.MeshToPassThroughAPoint`](smeshBuilder.md#smeshBuilder.Mesh.MeshToPassThroughAPoint)(x, y, z) | Find the node closest to a point and moves it to a point location |
| [`Mesh.ChangeElemNodes`](smeshBuilder.md#smeshBuilder.Mesh.ChangeElemNodes)(ide, newIDs) | Set new nodes for the given element. |

### Convert to/from Quadratic Mesh

|  |  |
| --- | --- |
| [`Mesh.ConvertToQuadratic`](smeshBuilder.md#smeshBuilder.Mesh.ConvertToQuadratic)([theForce3d, ...]) | Convert the mesh to quadratic or bi-quadratic, deletes old elements, replacing them with quadratic with the same id. |
| [`Mesh.ConvertFromQuadratic`](smeshBuilder.md#smeshBuilder.Mesh.ConvertFromQuadratic)([theSubMesh]) | Convert the mesh from quadratic to ordinary, deletes old quadratic elements, replacing them with ordinary mesh elements with the same id. |

### Extrusion and Revolution

|  |  |
| --- | --- |
| [`Mesh.RotationSweepObjects`](smeshBuilder.md#smeshBuilder.Mesh.RotationSweepObjects)(nodes, edges, ...) | Generate new elements by rotation of the given elements and nodes around the axis |
| [`Mesh.RotationSweep`](smeshBuilder.md#smeshBuilder.Mesh.RotationSweep)(IDsOfElements, Axis, ...) | Generate new elements by rotation of the elements around the axis |
| [`Mesh.RotationSweepObject`](smeshBuilder.md#smeshBuilder.Mesh.RotationSweepObject)(theObject, Axis, ...) | Generate new elements by rotation of the elements of object around the axis theObject object which elements should be sweeped. |
| [`Mesh.RotationSweepObject1D`](smeshBuilder.md#smeshBuilder.Mesh.RotationSweepObject1D)(theObject, Axis, ...) | Generate new elements by rotation of the elements of object around the axis theObject object which elements should be sweeped. |
| [`Mesh.RotationSweepObject2D`](smeshBuilder.md#smeshBuilder.Mesh.RotationSweepObject2D)(theObject, Axis, ...) | Generate new elements by rotation of the elements of object around the axis theObject object which elements should be sweeped. |
| [`Mesh.ExtrusionSweepObjects`](smeshBuilder.md#smeshBuilder.Mesh.ExtrusionSweepObjects)(nodes, edges, ...) | Generate new elements by extrusion of the given elements and nodes |
| [`Mesh.ExtrusionSweep`](smeshBuilder.md#smeshBuilder.Mesh.ExtrusionSweep)(IDsOfElements, ...[, ...]) | Generate new elements by extrusion of the elements with given ids |
| [`Mesh.ExtrusionByNormal`](smeshBuilder.md#smeshBuilder.Mesh.ExtrusionByNormal)(Elements, StepSize, ...) | Generate new elements by extrusion along the normal to a discretized surface or wire |
| [`Mesh.ExtrusionSweepObject`](smeshBuilder.md#smeshBuilder.Mesh.ExtrusionSweepObject)(theObject, ...[, ...]) | Generate new elements by extrusion of the elements or nodes which belong to the object |
| [`Mesh.ExtrusionSweepObject1D`](smeshBuilder.md#smeshBuilder.Mesh.ExtrusionSweepObject1D)(theObject, ...) | Generate new elements by extrusion of edges which belong to the object |
| [`Mesh.ExtrusionSweepObject2D`](smeshBuilder.md#smeshBuilder.Mesh.ExtrusionSweepObject2D)(theObject, ...) | Generate new elements by extrusion of faces which belong to the object |
| [`Mesh.AdvancedExtrusion`](smeshBuilder.md#smeshBuilder.Mesh.AdvancedExtrusion)(IDsOfElements, ...[, ...]) | Generate new elements by extrusion of the elements with given ids |
| [`Mesh.ExtrusionAlongPathObjects`](smeshBuilder.md#smeshBuilder.Mesh.ExtrusionAlongPathObjects)(Nodes, Edges, ...) | Generate new elements by extrusion of the given elements and nodes along the path. |
| [`Mesh.ExtrusionAlongPathX`](smeshBuilder.md#smeshBuilder.Mesh.ExtrusionAlongPathX)(Base, Path, NodeStart) | Generate new elements by extrusion of the given elements. |
| [`Mesh.ExtrusionAlongPath`](smeshBuilder.md#smeshBuilder.Mesh.ExtrusionAlongPath)(IDsOfElements, ...) | Generate new elements by extrusion of the given elements. |
| [`Mesh.ExtrusionAlongPathObject`](smeshBuilder.md#smeshBuilder.Mesh.ExtrusionAlongPathObject)(theObject, ...) | Generate new elements by extrusion of the elements which belong to the object. |
| [`Mesh.ExtrusionAlongPathObject1D`](smeshBuilder.md#smeshBuilder.Mesh.ExtrusionAlongPathObject1D)(theObject, ...) | Generate new elements by extrusion of mesh segments which belong to the object. |
| [`Mesh.ExtrusionAlongPathObject2D`](smeshBuilder.md#smeshBuilder.Mesh.ExtrusionAlongPathObject2D)(theObject, ...) | Generate new elements by extrusion of faces which belong to the object. |

### Transforming meshes (Translation, Rotation, Symmetry, Sewing, Merging)

|  |  |
| --- | --- |
| [`Mesh.Mirror`](smeshBuilder.md#smeshBuilder.Mesh.Mirror)(IDsOfElements, Mirror[, ...]) | Create a symmetrical copy of mesh elements |
| [`Mesh.MirrorMakeMesh`](smeshBuilder.md#smeshBuilder.Mesh.MirrorMakeMesh)(IDsOfElements, Mirror[, ...]) | Create a new mesh by a symmetrical copy of mesh elements |
| [`Mesh.MirrorObject`](smeshBuilder.md#smeshBuilder.Mesh.MirrorObject)(theObject, Mirror[, ...]) | Create a symmetrical copy of the object |
| [`Mesh.MirrorObjectMakeMesh`](smeshBuilder.md#smeshBuilder.Mesh.MirrorObjectMakeMesh)(theObject, Mirror) | Create a new mesh by a symmetrical copy of the object |
| [`Mesh.Translate`](smeshBuilder.md#smeshBuilder.Mesh.Translate)(IDsOfElements, Vector, Copy) | Translate the elements |
| [`Mesh.TranslateMakeMesh`](smeshBuilder.md#smeshBuilder.Mesh.TranslateMakeMesh)(IDsOfElements, Vector) | Create a new mesh of translated elements |
| [`Mesh.TranslateObject`](smeshBuilder.md#smeshBuilder.Mesh.TranslateObject)(theObject, Vector, Copy) | Translate the object |
| [`Mesh.TranslateObjectMakeMesh`](smeshBuilder.md#smeshBuilder.Mesh.TranslateObjectMakeMesh)(theObject, Vector) | Create a new mesh from the translated object |
| [`Mesh.Rotate`](smeshBuilder.md#smeshBuilder.Mesh.Rotate)(IDsOfElements, Axis, ...[, ...]) | Rotate the elements |
| [`Mesh.RotateMakeMesh`](smeshBuilder.md#smeshBuilder.Mesh.RotateMakeMesh)(IDsOfElements, Axis, ...) | Create a new mesh of rotated elements |
| [`Mesh.RotateObject`](smeshBuilder.md#smeshBuilder.Mesh.RotateObject)(theObject, Axis, ...[, ...]) | Rotate the object |
| [`Mesh.RotateObjectMakeMesh`](smeshBuilder.md#smeshBuilder.Mesh.RotateObjectMakeMesh)(theObject, Axis, ...) | Create a new mesh from the rotated object |
| [`Mesh.FindCoincidentNodes`](smeshBuilder.md#smeshBuilder.Mesh.FindCoincidentNodes)(Tolerance[, ...]) | Find groups of adjacent nodes within Tolerance. |
| [`Mesh.FindCoincidentNodesOnPart`](smeshBuilder.md#smeshBuilder.Mesh.FindCoincidentNodesOnPart)(...[, ...]) | Find groups of adjacent nodes within Tolerance. |
| [`Mesh.MergeNodes`](smeshBuilder.md#smeshBuilder.Mesh.MergeNodes)(GroupsOfNodes[, ...]) | Merge nodes |
| [`Mesh.FindEqualElements`](smeshBuilder.md#smeshBuilder.Mesh.FindEqualElements)([...]) | Find the elements built on the same nodes. |
| [`Mesh.MergeElements`](smeshBuilder.md#smeshBuilder.Mesh.MergeElements)(GroupsOfElementsID[, ...]) | Merge elements in each given group. |
| [`Mesh.MergeEqualElements`](smeshBuilder.md#smeshBuilder.Mesh.MergeEqualElements)() | Leave one element and remove all other elements built on the same nodes. |
| [`Mesh.FindFreeBorders`](smeshBuilder.md#smeshBuilder.Mesh.FindFreeBorders)([ClosedOnly]) | Returns all or only closed free borders |
| [`Mesh.FillHole`](smeshBuilder.md#smeshBuilder.Mesh.FillHole)(holeNodes[, groupName]) | Fill with 2D elements a hole defined by a SMESH.FreeBorder. |
| [`Mesh.FindCoincidentFreeBorders`](smeshBuilder.md#smeshBuilder.Mesh.FindCoincidentFreeBorders)([tolerance]) | Return groups of FreeBorder's coincident within the given tolerance. |
| [`Mesh.SewCoincidentFreeBorders`](smeshBuilder.md#smeshBuilder.Mesh.SewCoincidentFreeBorders)(freeBorders[, ...]) | Sew FreeBorder's of each group |
| [`Mesh.SewFreeBorders`](smeshBuilder.md#smeshBuilder.Mesh.SewFreeBorders)(FirstNodeID1, ...) | Sew free borders |
| [`Mesh.SewConformFreeBorders`](smeshBuilder.md#smeshBuilder.Mesh.SewConformFreeBorders)(FirstNodeID1, ...) | Sew conform free borders |
| [`Mesh.SewBorderToSide`](smeshBuilder.md#smeshBuilder.Mesh.SewBorderToSide)(...) | Sew border to side |
| [`Mesh.SewSideElements`](smeshBuilder.md#smeshBuilder.Mesh.SewSideElements)(IDsOfSide1Elements, ...) | Sew two sides of a mesh. |

### Changing orientation of elements

|  |  |
| --- | --- |
| [`Mesh.Reorient`](smeshBuilder.md#smeshBuilder.Mesh.Reorient)([IDsOfElements]) | Reorient elements by ids |
| [`Mesh.ReorientObject`](smeshBuilder.md#smeshBuilder.Mesh.ReorientObject)(theObject) | Reorient all elements of the object |
| [`Mesh.Reorient2D`](smeshBuilder.md#smeshBuilder.Mesh.Reorient2D)(the2DObject, theDirection, ...) | Reorient faces contained in *the2DObject*. |
| [`Mesh.Reorient2DByNeighbours`](smeshBuilder.md#smeshBuilder.Mesh.Reorient2DByNeighbours)(objectFaces[, ...]) | Reorient faces contained in a list of *objectFaces* equally to faces contained in a list of *referenceFaces*. |
| [`Mesh.Reorient2DBy3D`](smeshBuilder.md#smeshBuilder.Mesh.Reorient2DBy3D)(the2DObject, the3DObject) | Reorient faces according to adjacent volumes. |

### Uniting triangles

|  |  |
| --- | --- |
| [`Mesh.DeleteDiag`](smeshBuilder.md#smeshBuilder.Mesh.DeleteDiag)(NodeID1, NodeID2) | Replace two neighbour triangles sharing *Node1-Node2* link with a quadrangle built on the same 4 nodes. |
| [`Mesh.TriToQuad`](smeshBuilder.md#smeshBuilder.Mesh.TriToQuad)(IDsOfElements, theCriterion, ...) | Fuse the neighbouring triangles into quadrangles. |
| [`Mesh.TriToQuadObject`](smeshBuilder.md#smeshBuilder.Mesh.TriToQuadObject)(theObject, ...) | Fuse the neighbouring triangles of the object into quadrangles |

### Cutting elements

|  |  |
| --- | --- |
| [`Mesh.InverseDiag`](smeshBuilder.md#smeshBuilder.Mesh.InverseDiag)(NodeID1, NodeID2) | Replace two neighbour triangles sharing Node1-Node2 link with the triangles built on the same 4 nodes but having other common link. |
| [`Mesh.QuadToTri`](smeshBuilder.md#smeshBuilder.Mesh.QuadToTri)(IDsOfElements[, theCriterion]) | Split quadrangles into triangles. |
| [`Mesh.QuadToTriObject`](smeshBuilder.md#smeshBuilder.Mesh.QuadToTriObject)(theObject[, theCriterion]) | Split quadrangles into triangles. |
| [`Mesh.QuadTo4Tri`](smeshBuilder.md#smeshBuilder.Mesh.QuadTo4Tri)([theElements]) | Split each of given quadrangles into 4 triangles. |
| [`Mesh.SplitQuad`](smeshBuilder.md#smeshBuilder.Mesh.SplitQuad)(IDsOfElements, Diag13) | Split quadrangles into triangles. |
| [`Mesh.SplitQuadObject`](smeshBuilder.md#smeshBuilder.Mesh.SplitQuadObject)(theObject, Diag13) | Split quadrangles into triangles. |
| [`Mesh.BestSplit`](smeshBuilder.md#smeshBuilder.Mesh.BestSplit)(IDOfQuad, theCriterion) | Find a better splitting of the given quadrangle. |
| [`Mesh.SplitVolumesIntoTetra`](smeshBuilder.md#smeshBuilder.Mesh.SplitVolumesIntoTetra)(elems[, method, ...]) | Split volumic elements into tetrahedrons |
| [`Mesh.SplitBiQuadraticIntoLinear`](smeshBuilder.md#smeshBuilder.Mesh.SplitBiQuadraticIntoLinear)([elems]) | Split bi-quadratic elements into linear ones without creation of additional nodes: |
| [`Mesh.SplitHexahedraIntoPrisms`](smeshBuilder.md#smeshBuilder.Mesh.SplitHexahedraIntoPrisms)(elems, ...[, ...]) | Split hexahedra into prisms |
| [`Mesh.SplitQuadsNearTriangularFacets`](smeshBuilder.md#smeshBuilder.Mesh.SplitQuadsNearTriangularFacets)() | Split quadrangle faces near triangular facets of volumes |
| [`Mesh.SplitHexaToTetras`](smeshBuilder.md#smeshBuilder.Mesh.SplitHexaToTetras)(theObject, ...) | Split hexahedrons into tetrahedrons. |
| [`Mesh.SplitHexaToPrisms`](smeshBuilder.md#smeshBuilder.Mesh.SplitHexaToPrisms)(theObject, ...) | Split hexahedrons into prisms. |
| [`Mesh.AddNodeOnSegment`](smeshBuilder.md#smeshBuilder.Mesh.AddNodeOnSegment)(Node1, Node2[, position]) | Replace each triangle bound by Node1-Node2 segment with two triangles by connecting a node made on the link with a node opposite to the link. |
| [`Mesh.AddNodeOnFace`](smeshBuilder.md#smeshBuilder.Mesh.AddNodeOnFace)(face, x, y, z) | Split a face into triangles by adding a new node onto the face and connecting the new node with face nodes |

### Smoothing

|  |  |
| --- | --- |
| [`Mesh.Smooth`](smeshBuilder.md#smeshBuilder.Mesh.Smooth)(IDsOfElements, IDsOfFixedNodes, ...) | Smooth elements |
| [`Mesh.SmoothObject`](smeshBuilder.md#smeshBuilder.Mesh.SmoothObject)(theObject, ...) | Smooth elements which belong to the given object |
| [`Mesh.SmoothParametric`](smeshBuilder.md#smeshBuilder.Mesh.SmoothParametric)(IDsOfElements, ...) | Parametrically smooth the given elements |
| [`Mesh.SmoothParametricObject`](smeshBuilder.md#smeshBuilder.Mesh.SmoothParametricObject)(theObject, ...) | Parametrically smooth the elements which belong to the given object |

### Duplication of nodes and elements (to emulate cracks)

|  |  |
| --- | --- |
| [`Mesh.DoubleElements`](smeshBuilder.md#smeshBuilder.Mesh.DoubleElements)(theElements[, theGroupName]) | Create duplicates of given elements, i.e. create new elements based on the same nodes as the given ones. |
| [`Mesh.DoubleNodes`](smeshBuilder.md#smeshBuilder.Mesh.DoubleNodes)(theNodes, theModifiedElems) | Create a hole in a mesh by doubling the nodes of some particular elements |
| [`Mesh.DoubleNode`](smeshBuilder.md#smeshBuilder.Mesh.DoubleNode)(theNodeId, theModifiedElems) | Create a hole in a mesh by doubling the nodes of some particular elements. |
| [`Mesh.DoubleNodeGroup`](smeshBuilder.md#smeshBuilder.Mesh.DoubleNodeGroup)(theNodes, theModifiedElems) | Create a hole in a mesh by doubling the nodes of some particular elements. |
| [`Mesh.DoubleNodeGroups`](smeshBuilder.md#smeshBuilder.Mesh.DoubleNodeGroups)(theNodes, theModifiedElems) | Create a hole in a mesh by doubling the nodes of some particular elements. |
| [`Mesh.DoubleNodeElem`](smeshBuilder.md#smeshBuilder.Mesh.DoubleNodeElem)(theElems, theNodesNot, ...) | Create a hole in a mesh by doubling the nodes of some particular elements |
| [`Mesh.DoubleNodeElemInRegion`](smeshBuilder.md#smeshBuilder.Mesh.DoubleNodeElemInRegion)(theElems, ...) | Create a hole in a mesh by doubling the nodes of some particular elements |
| [`Mesh.DoubleNodeElemGroup`](smeshBuilder.md#smeshBuilder.Mesh.DoubleNodeElemGroup)(theElems, ...[, ...]) | Create a hole in a mesh by doubling the nodes of some particular elements. |
| [`Mesh.DoubleNodeElemGroupInRegion`](smeshBuilder.md#smeshBuilder.Mesh.DoubleNodeElemGroupInRegion)(theElems, ...) | Create a hole in a mesh by doubling the nodes of some particular elements. |
| [`Mesh.DoubleNodeElemGroups`](smeshBuilder.md#smeshBuilder.Mesh.DoubleNodeElemGroups)(theElems, ...[, ...]) | Create a hole in a mesh by doubling the nodes of some particular elements. |
| [`Mesh.DoubleNodeElemGroupsInRegion`](smeshBuilder.md#smeshBuilder.Mesh.DoubleNodeElemGroupsInRegion)(theElems, ...) | Create a hole in a mesh by doubling the nodes of some particular elements. |
| [`Mesh.AffectedElemGroupsInRegion`](smeshBuilder.md#smeshBuilder.Mesh.AffectedElemGroupsInRegion)(theElems, ...) | Identify the elements that will be affected by node duplication (actual duplication is not performed). |
| [`Mesh.DoubleNodesOnGroupBoundaries`](smeshBuilder.md#smeshBuilder.Mesh.DoubleNodesOnGroupBoundaries)(...[, ...]) | Double nodes on shared faces between groups of volumes and create flat elements on demand. |
| [`Mesh.CreateFlatElementsOnFacesGroups`](smeshBuilder.md#smeshBuilder.Mesh.CreateFlatElementsOnFacesGroups)(...) | Double nodes on some external faces and create flat elements. |

### Renumbering nodes and elements

|  |  |
| --- | --- |
| [`Mesh.RenumberNodes`](smeshBuilder.md#smeshBuilder.Mesh.RenumberNodes)() | Renumber mesh nodes to remove unused node IDs |
| [`Mesh.RenumberElements`](smeshBuilder.md#smeshBuilder.Mesh.RenumberElements)() | Renumber mesh elements to remove unused element IDs |

## Auxiliary methods

|  |  |
| --- | --- |
| [`GetName`](smeshBuilder.md#smeshBuilder.GetName)(obj) | Return a name of an object |
| [`DegreesToRadians`](smeshBuilder.md#smeshBuilder.DegreesToRadians)(AngleInDegrees) | Convert an angle from degrees to radians |
| [`New`](smeshBuilder.md#smeshBuilder.New)([instance, instanceGeom]) | Create a new smeshBuilder instance. |
