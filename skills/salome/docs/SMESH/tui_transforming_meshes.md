<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/tui_transforming_meshes.html -->

# Transforming Meshes

## Translation

```python
# Translation

from mechanic import *

# define translation vector
vector = [-150., -150., 0.]

# make a translated copy of all elements of the mesh
mesh.TranslateObject(mesh, vector, Copy=True)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/0127d475c380645c27adf86fc783877b/transforming_meshes_ex01.py)

## Rotation

```python
# Rotation

import math

from mechanic import *

# define rotation axis and angle
axisXYZ = SMESH.AxisStruct(0., 0., 0., 5., 5., 20.)
angle270 = 1.5 * math.pi

# rotate a mesh
mesh.Rotate([], axisXYZ, angle270, 1)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/86c1498cfa982469209504840ae44be7/transforming_meshes_ex02.py)

## Scale

```python
# Scale

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

Box = geom_builder.MakeBoxDXDYDZ(200, 200, 200)
f = geom_builder.SubShapeAllSorted(Box, geom_builder.ShapeType["FACE"])

Mesh1 = smesh_builder.Mesh(f[0])
Regular_1D = Mesh1.Segment()
Nb_Segments_1 = Regular_1D.NumberOfSegments(3)
Nb_Segments_1.SetDistrType( 0 )
Quadrangle_2D = Mesh1.Quadrangle()
if not Mesh1.Compute(): raise Exception("Error when computing Mesh")

#Perform scale operation for the whole mesh and creation of a new mesh
newMesh = Mesh1.ScaleMakeMesh(Mesh1,SMESH.PointStruct(100,100,200),[0.5,0.3,0.7],True,"ScaledMesh")

#Perform scale operation for the whole mesh and copy elements
Mesh1.Scale(Mesh1,SMESH.PointStruct(200,100,100),[0.5,0.5,0.5],True,True)

#Perform scale operation for two edges and move elements
Mesh1.Scale([1,2],SMESH.PointStruct(-100,100,100),[0.8,1.0,0.7],False)

#Perform scale operation for one face and move elements
Mesh1.Scale([21],SMESH.PointStruct(0,200,200),[0.7,0.7,0.7],False)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/c31c3948b7aa939f572e20cc2582bba0/transforming_meshes_ex03.py)

## Symmetry

```python
# Symmetry

from mechanic import *

# create a symmetrical copy of the mesh mirrored through a point
axis = SMESH.AxisStruct(0, 0, 0, 0, 0, 0)

mesh.Mirror([], axis, smesh_builder.POINT, 1)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/1043e1cc097860a72303121ac2fefbf9/transforming_meshes_ex04.py)

## Merging Nodes

```python
# Merging Nodes

from mechanic import *

# criterion of coincidence
Tolerance = 4.0

# find close nodes of triangle elements only
triangleFilter = smesh_builder.GetFilter( SMESH.FACE, SMESH.FT_ElemGeomType,'=', SMESH.Geom_TRIANGLE )
GroupsOfNodesOfTriangles = mesh.FindCoincidentNodesOnPart([triangleFilter],Tolerance)

# prevent nodes located on geom edges from removal during merge:
# create a group including all nodes on edges
allSegs = mesh.MakeGroup( "all segments", SMESH.EDGE, SMESH.FT_ElemGeomType,'=', SMESH.Geom_EDGE )

mesh.MergeNodes(GroupsOfNodesOfTriangles, NodesToKeep=allSegs)

# find close nodes in the whole mesh
GroupsOfNodes = mesh.FindCoincidentNodes(Tolerance)

mesh.MergeNodes(GroupsOfNodes, NodesToKeep=allSegs)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/cc916c40e5f8035078967fc6dea46f8f/transforming_meshes_ex05.py)

## Merging Elements

```python
# Merging Elements

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a face to be meshed
px = geom_builder.MakeVertex(100., 0.  , 0.  )
py = geom_builder.MakeVertex(0.  , 100., 0.  )
pz = geom_builder.MakeVertex(0.  , 0.  , 100.)

vxy = geom_builder.MakeVector(px, py)
arc = geom_builder.MakeArc(py, pz, px)

wire = geom_builder.MakeWire([vxy, arc])
isPlanarFace = 1

face1 = geom_builder.MakeFace(wire, isPlanarFace)
id_face1 = geom_builder.addToStudy(face1, "Face1")

# create a circle to be an extrusion path
px1 = geom_builder.MakeVertex( 100.,  100.,  0.)
py1 = geom_builder.MakeVertex(-100., -100.,  0.)
pz1 = geom_builder.MakeVertex(   0.,    0., 50.)

circle = geom_builder.MakeCircleThreePnt(py1, pz1, px1)
id_circle = geom_builder.addToStudy(circle, "Path")
 
# create a 2D mesh on the face
trias = smesh_builder.Mesh(face1, "Face : 2D mesh")

algo1D = trias.Segment()
algo1D.NumberOfSegments(6)
algo2D = trias.Triangle()
algo2D.LengthFromEdges()

if not trias.Compute(): raise Exception("Error when computing Mesh")

# create a group of all triangles currently present in the mesh
faceTriGroup = trias.Group( face1, "face triangles" )

# create a path mesh
circlemesh = smesh_builder.Mesh(circle, "Path mesh")
algo = circlemesh.Segment()
algo.NumberOfSegments(10)
if not circlemesh.Compute(): raise Exception("Error when computing Mesh")

# extrusion of the mesh
trias.ExtrusionAlongPath([], circlemesh, circle, 1, MakeGroups=True )

# get a group "opposite" to faceTriGroup within the generated prismatic mesh
oppositeGroup = trias.GetGroupByName( faceTriGroup.GetName() + "_top" )[0]

# get edges of the groups
edgeGroup = trias.CreateDimGroup([ faceTriGroup, oppositeGroup ], SMESH.EDGE, "face edges")

# merge nodes of the groups only
print("Number of nodes before MergeNodes:", end=' ') 
trias.NbNodes()
tolerance = 0.001
array_of_nodes_groups = trias.FindCoincidentNodesOnPart([faceTriGroup, oppositeGroup], tolerance)

trias.MergeNodes(array_of_nodes_groups)

print("Number of nodes after MergeNodes:", trias.NbNodes())
print("")
print("Number of elements before MergeEqualElements:")
print("Edges      : ", trias.NbEdges())
print("Faces      : ", trias.NbFaces())
print("Volumes    : ", trias.NbVolumes())

# merge elements of the groups
equalFaces = trias.FindEqualElements( [faceTriGroup, oppositeGroup, edgeGroup] )
trias.MergeElements( equalFaces )
print("Number of elements after MergeEqualElements:")
print("Edges      : ", trias.NbEdges())
print("Faces      : ", trias.NbFaces())
print("Volumes    : ", trias.NbVolumes())
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/b8d7a7f7ebbd199e59cb0acb7bbcfdcb/transforming_meshes_ex06.py)

## Sew Meshes Border to Side

```python
# Sew Meshes Border to Side

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create two faces of a box
box1 = geom_builder.MakeBox(0., 0., -10., 30., 20., 25.)
facesList1 = geom_builder.SubShapeAll(box1, geom_builder.ShapeType["FACE"])
face1 = facesList1[2]

box2 = geom_builder.MakeBox(0., 5., 0., 20., 20., 15.)
facesList2 = geom_builder.SubShapeAll(box2, geom_builder.ShapeType["FACE"])
face2 = facesList2[1]

edgesList = geom_builder.SubShapeAll(face2, geom_builder.ShapeType["EDGE"])
edge1 = edgesList[2]

aComp = geom_builder.MakeCompound([face1, face2])
geom_builder.addToStudy(aComp, "Two faces")

# create a mesh on two faces
mesh = smesh_builder.Mesh(aComp, "Two faces : quadrangle mesh")

algo1D = mesh.Segment()
algo1D.NumberOfSegments(9)
algo2D = mesh.Quadrangle()

algo_local = mesh.Segment(edge1)
algo_local.Arithmetic1D(1, 4)
algo_local.Propagation()

if not mesh.Compute(): raise Exception("Error when computing Mesh")

# sew border to side
# FirstNodeIDOnFreeBorder, SecondNodeIDOnFreeBorder, LastNodeIDOnFreeBorder,
# FirstNodeIDOnSide, LastNodeIDOnSide,
# CreatePolygons, CreatePolyedrs
mesh.SewBorderToSide(5, 45, 6, 113, 109, 0, 0)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/42b9d3686da1b2fc4596a38eec09de6f/transforming_meshes_ex07.py)

## Sew Conform Free Borders

```python
# Sew Conform Free Borders

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create two faces of the box
box1 = geom_builder.MakeBox(0., 0., -10., 20., 20., 15.)
facesList1 = geom_builder.SubShapeAll(box1, geom_builder.ShapeType["FACE"])
face1 = facesList1[2]

box2 = geom_builder.MakeBox(0., 5., 0., 20., 20., 15.)
facesList2 = geom_builder.SubShapeAll(box2, geom_builder.ShapeType["FACE"])
face2 = facesList2[1]

edgesList = geom_builder.SubShapeAll(face2, geom_builder.ShapeType["EDGE"])
edge1 = edgesList[2]

aComp = geom_builder.MakeCompound([face1, face2])
geom_builder.addToStudy(aComp, "Two faces")

# create a mesh on two faces
mesh = smesh_builder.Mesh(aComp, "Two faces : quadrangle mesh")

algo1D = mesh.Segment()
algo1D.NumberOfSegments(9)
algo2D = mesh.Quadrangle()

algo_local = mesh.Segment(edge1)
algo_local.Arithmetic1D(1, 4)
algo_local.Propagation()

if not mesh.Compute(): raise Exception("Error when computing Mesh")

# sew conform free borders
# FirstNodeID1, SecondNodeID1, LastNodeID1, FirstNodeID2, SecondNodeID2
mesh.SewConformFreeBorders(5, 45, 6, 3, 24)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/b6cd61854865b3386c8d40aa97c7a4c3/transforming_meshes_ex08.py)

## Sew Free Borders

```python
# Sew Free Borders

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# make two not sewed quadranges
OY0 = geom_builder.MakeVectorDXDYDZ(0, 1, 0)
OY1 = geom_builder.MakeTranslation( OY0, 1, 0, 0, theName="OY1" )
OY2 = geom_builder.MakeTranslation( OY0, 1.01, 0, 0, theName="OY2" )
OY3 = geom_builder.MakeTranslation( OY0, 2, 0, 0 )
q1  = geom_builder.MakeQuad2Edges( OY0, OY1 )
q2  = geom_builder.MakeQuad2Edges( OY2, OY3 )

shape = geom_builder.MakeCompound( [q1,q2], theName='shape' )

# make a non-uniform quadrangle mesh on two faces
mesh = smesh_builder.Mesh(shape, "Two faces : quadrangle mesh")
mesh.Segment().Arithmetic1D( 0.1, 0.4 )
mesh.Segment(q1).NumberOfSegments( 5 )
mesh.Quadrangle()
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# sew free borders

segs1 = mesh.GetSubMeshElementsId( OY1 ) # mesh segments generated on borders
segs2 = mesh.GetSubMeshElementsId( OY2 )

FirstNodeID1  = mesh.GetElemNode( segs1[0], 0 )
SecondNodeID1 = mesh.GetElemNode( segs1[0], 1 )
LastNodeID1   = mesh.GetElemNode( segs1[-1], 1 )
FirstNodeID2  = mesh.GetElemNode( segs2[0], 0 )
SecondNodeID2 = mesh.GetElemNode( segs2[0], 1 )
LastNodeID2   = mesh.GetElemNode( segs2[-1], 1 )
CreatePolygons = True
CreatePolyedrs = False

res = mesh.SewFreeBorders(FirstNodeID1, SecondNodeID1, LastNodeID1,
                          FirstNodeID2, SecondNodeID2, LastNodeID2,
                          CreatePolygons, CreatePolyedrs )
print(res)
print("nb polygons:", mesh.NbPolygons())
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/f6c811c7c3d3128eea67c8fbca64173e/transforming_meshes_ex09.py)

## Sew Side Elements

```python
# Sew Side Elements

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create two boxes
box1 = geom_builder.MakeBox(0.,  0., 0., 10., 10., 10.)
box2 = geom_builder.MakeBox(0., 15., 0., 20., 25., 10.)

EdgesList = geom_builder.SubShapeAll(box2, geom_builder.ShapeType["EDGE"])

aComp = geom_builder.MakeCompound([box1, box2])
geom_builder.addToStudy(aComp, "Two boxes")

# create a mesh on two boxes
mesh = smesh_builder.Mesh(aComp, "Sew Side Elements")

algo1D = mesh.Segment()
algo1D.NumberOfSegments(2)
algo2D = mesh.Quadrangle()

algo_local = mesh.Segment(EdgesList[8])
algo_local.NumberOfSegments(4)
algo_local.Propagation()

if not mesh.Compute(): raise Exception("Error when computing Mesh")

# sew side elements

# find elements to sew
face1 = geom_builder.GetFaceNearPoint( aComp, geom_builder.MakeVertex( 5, 10, 5 ))
IDsOfSide1Elements = mesh.GetSubMeshElementsId( face1 )
print("side faces 1:",IDsOfSide1Elements)

face1Translated = geom_builder.MakeTranslation( face1, 0,5,0 )
faceFilter = smesh_builder.GetFilter( SMESH.FACE, SMESH.FT_BelongToGeom,'=', face1Translated )
IDsOfSide2Elements = mesh.GetIdsFromFilter( faceFilter )
print("side faces 2:",IDsOfSide2Elements)

# find corresponding nodes on sides
edge1 = geom_builder.GetEdgeNearPoint( aComp, geom_builder.MakeVertex( 0, 10, 5 ))
segs1 = mesh.GetSubMeshElementsId( edge1 ) # mesh segments generated on edge1
NodeID1OfSide1ToMerge = mesh.GetElemNode( segs1[0], 0 )
NodeID2OfSide1ToMerge = mesh.GetElemNode( segs1[0], 1 )
print("nodes of side1:", [NodeID1OfSide1ToMerge,NodeID2OfSide1ToMerge])

edge2 = geom_builder.GetEdgeNearPoint( aComp, geom_builder.MakeVertex( 0, 15, 5 ))
segs2 = mesh.GetSubMeshElementsId( edge2 ) # mesh segments generated on edge2
NodeID1OfSide2ToMerge = mesh.GetElemNode( segs2[0], 0 )
NodeID2OfSide2ToMerge = mesh.GetElemNode( segs2[0], 1 )
print("nodes of side2:", [NodeID1OfSide2ToMerge,NodeID2OfSide2ToMerge])

res = mesh.SewSideElements(IDsOfSide1Elements, IDsOfSide2Elements,
                           NodeID1OfSide1ToMerge, NodeID1OfSide2ToMerge,
                           NodeID2OfSide1ToMerge, NodeID2OfSide2ToMerge)
print(res)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/652abc6a52325b9bbbb4b59604e12734/transforming_meshes_ex10.py)

## Duplicate nodes or/and elements

```python
# Duplicate nodes or/and elements

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# Create a box

box = geom_builder.MakeBox(0., 0., 0., 100., 200., 300.)

# Define hexa mesh on a box
mesh = smesh_builder.Mesh(box, "Mesh")
mesh.Segment().NumberOfSegments(7)
mesh.Quadrangle()
mesh.Hexahedron()

# Compute mesh
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# Duplicate nodes only

# Nodes to duplicate
nodes1 = mesh.CreateEmptyGroup( SMESH.NODE, 'nodes1' )
nodes1.Add( [ 119, 125, 131, 137 ] )

# Group of faces to replace nodes with new ones 
faces1 = mesh.CreateEmptyGroup( SMESH.FACE, 'faces1' )
faces1.Add( [ 144, 151, 158 ] )

# Duplicate nodes
print("\nMesh before the first nodes duplication:")
print("Nodes       : ", mesh.NbNodes())
print("Edges       : ", mesh.NbEdges())
print("Quadrangles : ", mesh.NbQuadrangles())

groupOfCreatedNodes = mesh.DoubleNodeGroup(nodes1, faces1, theMakeGroup=True)
print("New nodes:", groupOfCreatedNodes.GetIDs())

print("\nMesh after the first nodes duplication:")
print("Nodes       : ", mesh.NbNodes())
print("Edges       : ", mesh.NbEdges())
print("Quadrangles : ", mesh.NbQuadrangles())

# Duplicate nodes and border elements

# Edges to duplicate
edges = mesh.CreateEmptyGroup( SMESH.EDGE, 'edges' )
edges.Add( [ 32, 33, 34 ] )

# Nodes not to duplicate
nodes2 = mesh.CreateEmptyGroup( SMESH.NODE, 'nodes2' )
nodes2.Add( [ 35, 38 ] )

# Group of faces to replace nodes with new ones 
faces2 = mesh.CreateEmptyGroup( SMESH.FACE, 'faces2' )
faces2.Add( [ 141, 148, 155 ] )

# Duplicate nodes
print("\nMesh before the second nodes duplication:")
print("Nodes       : ", mesh.NbNodes())
print("Edges       : ", mesh.NbEdges())
print("Quadrangles : ", mesh.NbQuadrangles())

groupOfNewEdges = mesh.DoubleNodeElemGroup( edges, nodes2, faces2, theMakeGroup=True )
print("New edges:", groupOfNewEdges.GetIDs())

print("\nMesh after the second nodes duplication:")
print("Nodes       : ", mesh.NbNodes())
print("Edges       : ", mesh.NbEdges())
print("Quadrangles : ", mesh.NbQuadrangles())

# Duplicate elements only

# Duplicate all faces and make a group of new faces.
# If a mesh is given to DoubleElements(), all elements of the greatest dimension are duplicated
newFacesGroup = mesh.DoubleElements( mesh, "newFacesGroup" )

# Duplicate edges contained in the group "edges" and add new edges to this group
mesh.DoubleElements( edges, edges.GetName() )

# Duplicate two first edges of the mesh
mesh.DoubleElements([ 1, 2 ])
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/b63cab2b25ffd1727f7387c2428cdc3d/transforming_meshes_ex11.py)

## Create boundary elements

```python
# Create boundary elements

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

box = geom_builder.MakeBoxDXDYDZ(100, 100, 100)
gFaces = geom_builder.SubShapeAllSorted(box, geom_builder.ShapeType["FACE"])
f1,f2 = gFaces[0],gFaces[1]
geom_builder.addToStudy(box,"box")
geom_builder.addToStudyInFather(box,f1,"face1")
geom_builder.addToStudyInFather(box,f2,"face2")

twoFaces = geom_builder.MakeCompound([f1,f2])

## -----------
##
## 2D from 3D
##
## -----------
dim = SMESH.BND_2DFROM3D

init_mesh = smesh_builder.Mesh(box, "box")
init_mesh.AutomaticHexahedralization() # it makes 3 x 3 x 3 hexahedrons

# remove some faces
faces = init_mesh.GetElementsByType( SMESH.FACE )
nb_faces = len( faces )
rm_face = faces[ : nb_faces // 2]
init_mesh.RemoveElements( rm_face )

# restore boundary in this mesh
mesh = smesh_builder.CopyMesh( init_mesh, "2D from 3D")
groupName = "bnd 2D"
nb, new_mesh, new_group = mesh.MakeBoundaryElements(dim, groupName)

# restore boundary (only) in other mesh
meshName = "2D boundary of " + init_mesh.GetName()
nb, new_mesh, new_group = init_mesh.MakeBoundaryElements(dim, groupName, meshName)

# restore boundary in mesh copy
meshName = init_mesh.GetName() + " + boundary"
nb, new_mesh, new_group = init_mesh.MakeBoundaryElements(dim, groupName, meshName, toCopyAll=True)

## -----------
##
## 1D from 2D
##
## -----------
dim = SMESH.BND_1DFROM2D

init_mesh = smesh_builder.Mesh(f1, "2D mesh")
init_mesh.AutomaticHexahedralization()

# remove some edges
edges = init_mesh.GetElementsByType( SMESH.EDGE )
nb_edges = len( edges )
rm_edge = edges[ : nb_edges // 2]
init_mesh.RemoveElements( rm_edge )

# restore boundary edges in this mesh
mesh = smesh_builder.CopyMesh( init_mesh, "1D from 2D")
groupName = "bnd 1D"
nb, new_mesh, new_group = mesh.MakeBoundaryElements(dim, groupName)

# restore boundary edges (only) in other mesh
meshName = "1D boundary of " + init_mesh.GetName()
nb, new_mesh, new_group = init_mesh.MakeBoundaryElements(dim, groupName, meshName)

# restore boundary edges in mesh copy
meshName = init_mesh.GetName() + " + boundary"
nb, new_mesh, new_group = init_mesh.MakeBoundaryElements(dim, groupName, meshName, toCopyAll=True)

## ------------------
##
## 1D from 2D GROUPS
##
## ------------------
dim = SMESH.BND_1DFROM3D

init_mesh = smesh_builder.Mesh(box, "box")
init_mesh.AutomaticHexahedralization() # it makes 3 x 3 x 3 hexahedrons
# remove all edges
rm_edges = init_mesh.GetElementsByType( SMESH.EDGE )
init_mesh.RemoveElements( rm_edges )

# make groups of faces
fGroup1 = init_mesh.Group( f1, "f1" )
fGroup2 = init_mesh.Group( f2, "f2" )

# make 1D boundary around groups in this mesh
mesh = smesh_builder.CopyMesh( init_mesh, "1D from 2D groups", toCopyGroups=True)
groups = mesh.GetGroups()
nb, new_mesh, new_group = mesh.MakeBoundaryElements(dim, groupName,groups=groups)

# make 1D boundary (only) in other mesh
meshName =  "boundary from groups of " + init_mesh.GetName()
groups = init_mesh.GetGroups()
nb, new_mesh, new_group = init_mesh.MakeBoundaryElements(dim, groupName, meshName,groups=groups)

# make 1D boundary in mesh copy
meshName = init_mesh.GetName() + " + boundary from groups"
nb, new_mesh, new_group = init_mesh.MakeBoundaryElements(dim, groupName, meshName,
                                                         groups=groups, toCopyAll=True)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/7b4b1375d1ac397865bec143f48f1eb7/transforming_meshes_ex12.py)

## Reorient faces

```python
# Reorient faces

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a geometry consisting of two faces
box = geom_builder.MakeBoxDXDYDZ( 10, 10, 10 )
faces = geom_builder.SubShapeAllSorted( box, geom_builder.ShapeType["FACE"])

shape = geom_builder.MakeCompound( faces[:2] )
faces = geom_builder.SubShapeAll( shape, geom_builder.ShapeType["FACE"] )
geom_builder.addToStudy( shape, "shape")
geom_builder.addToStudyInFather( shape, faces[0], "faces[0]")
geom_builder.addToStudyInFather( shape, faces[1], "faces[1]")

# create a 2D mesh
mesh = smesh_builder.Mesh( shape, "test_Reorient2D")
mesh.AutomaticHexahedralization(0.5)
localAlgo = mesh.Segment(faces[0])
localAlgo.NumberOfSegments( 11 )
if not mesh.Compute(): raise Exception("Error when computing Mesh")
group = mesh.Group( faces[1] )

vec = geom_builder.MakeVectorDXDYDZ( 1, 1, 1 )

# ============
# Reorient2D()
# ============

# Each of arguments of Reorient2D() function can be of different types:
#
# 2DObject    - the whole mesh
# Direction   - a GEOM object (vector)
# FaceOrPoint - an ID of face
mesh.Reorient2D( mesh, vec, mesh.NbElements() )
#
# 2DObject    - a sub-mesh
# Direction   - components of a vector
# FaceOrPoint - a GEOM object (vertex)
mesh.Reorient2D( localAlgo.GetSubMesh(), [ 1, -1, 1 ], geom_builder.GetFirstVertex( vec ))
#
# 2DObject    - a group of faces
# Direction   - a SMESH.DirStruct structure
# FaceOrPoint - coordinates of a point
mesh.Reorient2D( group, smesh_builder.MakeDirStruct( -10, 1, 10 ), [0,0,0])
#
# FaceOrPoint - a SMESH.PointStruct structure
mesh.Reorient2D( localAlgo.GetSubMesh().GetIDs(), [10,1,0], SMESH.PointStruct(0,0,0))

# ========================
# Reorient2DByNeighbours()
# ========================

# Use faces of 'group' as a reference to reorient equally all faces
mesh.Reorient2DByNeighbours([mesh], [group])

# Orient equally face on 'group', but not define which orientation is correct
mesh.Reorient2DByNeighbours([group])

# =================
# Reorient2DBy3D()
# =================

# Use Reorient2DBy3D() to orient faces of 2 geom faces to have their normal pointing inside volumes

mesh3D = smesh_builder.Mesh( box, '3D mesh')
mesh3D.AutomaticHexahedralization(0.5)
group0 = mesh3D.Group( faces[0] )
group1 = mesh3D.Group( faces[1] )

# pass group0 and ids of faces of group1 to inverse
nbRev = mesh3D.Reorient2DBy3D([ group0, group1.GetIDs() ], mesh3D, theOutsideNormal=False)
print("Nb reoriented faces:", nbRev)

# orient the reversed faces back
nbRev = mesh3D.Reorient2DBy3D( mesh3D, mesh3D, theOutsideNormal=True)
print("Nb re-reoriented faces:", nbRev)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/03805e61be3f6d00295292bab5b479ea/transforming_meshes_ex13.py)

## Create 2D mesh from 3D elements

```python
# Create 2D mesh from 3D elements

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

box = geom_builder.MakeBoxDXDYDZ(100, 100, 100)

gFaces = geom_builder.SubShapeAllSorted(box, geom_builder.ShapeType["FACE"])
f1,f2 = gFaces[0],gFaces[1]
geom_builder.addToStudy(box,"box")
geom_builder.addToStudyInFather(box,f1,"face1")
geom_builder.addToStudyInFather(box,f2,"face2")

twoFaces = geom_builder.MakeCompound([f1,f2])

## -----------
##
## Create 2D from 3D elements
##
## -----------

init_mesh = smesh_builder.Mesh(box, "box")
init_mesh.AutomaticHexahedralization() # it makes 3 x 3 x 3 hexahedrons
init_mesh.Compute()

mesh_1 = smesh_builder.CopyMesh(init_mesh, "Mesh_1")
#Return the number of created faces in the original mesh.
nb, new_mesh, new_group = mesh_1.MakeBoundaryOfEachElement()

if nb != 54: raise Exception("Error on MakeBoundaryOfEachElement call. The number of created elements does not match.")
if new_mesh.GetId() != mesh_1.GetId(): raise Exception("The mesh created from MakeBoundaryElements should be the same of the call")
if new_group: raise Exception("The group created from MakeBoundaryElements should be undefined")

mesh_2 = smesh_builder.CopyMesh(init_mesh, "Mesh_2")

#Return the number of created faces and a new_mesh and new_group 
nb, new_mesh, new_group = mesh_2.MakeBoundaryOfEachElement("MyFacesElements", "Face_Mesh")
if nb != 54: raise Exception("Error on MakeBoundaryOfEachElement call. The number of created elements does not match.")
if new_mesh.GetId() == mesh_2.GetId(): raise Exception("The mesh created from MakeBoundaryElements should be the different of the call")
if not new_group: raise Exception("The group created from MakeBoundaryElements should be defined")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/757f73b634dfd344dd56accbcb88cd7e/transforming_meshes_ex14.py)

## Offset 2D mesh

```python
# Offset 2D mesh, sub-mesh, group or elements from filter.

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

box = geom_builder.MakeBoxDXDYDZ(100, 100, 100)

## -----------
##
## Offset mesh
##
## -----------

init_mesh = smesh_builder.Mesh(box, "box")
init_mesh.AutomaticTetrahedralization()
init_mesh.Compute()

#Offset triangular elements in mesh (expand the entire mesh)
offset = 20
mesh, mesh_group = init_mesh.Offset( init_mesh, offset, MakeGroups=False, CopyElements=False )
assert isinstance( mesh, smeshBuilder.Mesh )
assert len( mesh_group ) == 0
offsetMeshArea = smesh_builder.GetArea(mesh)

#Offset triangular elements in mesh (shrink the entire mesh)
offset = -20
mesh, mesh_group = init_mesh.Offset( init_mesh, offset, MakeGroups=False, CopyElements=False, NewMeshName="MeshShrink" )
assert isinstance( mesh, smeshBuilder.Mesh )
assert len( mesh_group ) == 0
assert mesh.GetName() == "MeshShrink"
shrinkMeshArea = smesh_builder.GetArea(mesh)

assert offsetMeshArea > shrinkMeshArea
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/8aea68673848b155be9527bd84541959/transforming_meshes_ex15.py)
