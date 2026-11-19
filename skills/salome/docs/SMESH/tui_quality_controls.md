<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/tui_quality_controls.html -->

# Quality Controls

## Free Borders

```python
# Free Borders

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create open shell: a box without one plane
box = geom_builder.MakeBox(0., 0., 0., 20., 20., 15.)
FaceList = geom_builder.SubShapeAll(box, geom_builder.ShapeType["FACE"])
FaceList.remove(FaceList[5])
box = geom_builder.MakeShell(FaceList)
idbox = geom_builder.addToStudy(box, "box")

# create a mesh
mesh = smesh_builder.Mesh(box, "Mesh_free_borders")
algo = mesh.Segment()
algo.NumberOfSegments(5)
algo = mesh.Triangle()
algo.MaxElementArea(20.)
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# criterion : free borders
aFilter = smesh_builder.GetFilter(SMESH.EDGE, SMESH.FT_FreeBorders)
anIds = mesh.GetIdsFromFilter(aFilter)

# print the result
print("Criterion: Free borders Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.GetMesh().CreateGroup(SMESH.EDGE, "Free borders")
aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/8a50d27857a54a59f6ecf23c5e6be8bc/quality_controls_ex01.py)

## Borders at Multiconnection

```python
# Borders at Multiconnection

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create open shell: a box without one plane
box = geom_builder.MakeBox(0., 0., 0., 20., 20., 15.)
FaceList = geom_builder.SubShapeAll(box, geom_builder.ShapeType["FACE"])
FaceList.remove(FaceList[5])
box = geom_builder.MakeShell(FaceList)
idbox = geom_builder.addToStudy(box, "box")

# create a mesh
mesh = smesh_builder.Mesh(box, "Mesh_borders_at_multi-connections")
algo = mesh.Segment()
algo.NumberOfSegments(5)
algo = mesh.Triangle()
algo.MaxElementArea(20.)
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# Criterion : Borders at multi-connection
nb_conn = 2

aFilter = smesh_builder.GetFilter(SMESH.EDGE, SMESH.FT_MultiConnection, SMESH.FT_EqualTo, nb_conn)
anIds = mesh.GetIdsFromFilter(aFilter)

# print the result
print("Criterion: Borders at multi-connections Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.GetMesh().CreateGroup(SMESH.EDGE, "Borders at multi-connections")
aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/c3555427bff6b757a9641d4a2f02b2dd/quality_controls_ex02.py)

## Length 1D

```python
# Length 1D

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create open shell: a box without one plane
box = geom_builder.MakeBox(0., 0., 0., 20., 20., 15.)
FaceList = geom_builder.SubShapeAll(box, geom_builder.ShapeType["FACE"])
FaceList.remove(FaceList[5])
box = geom_builder.MakeShell(FaceList)
idbox = geom_builder.addToStudy(box, "box")

# create a mesh
mesh = smesh_builder.Mesh(box, "Mesh_Length_1D")
algo = mesh.Segment()
algo.NumberOfSegments(5)
algo = mesh.Triangle()
algo.MaxElementArea(20.)
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# Criterion : Length > 3.
length_margin = 3.

aFilter = smesh_builder.GetFilter(SMESH.EDGE, SMESH.FT_Length, SMESH.FT_MoreThan, length_margin)
anIds = mesh.GetIdsFromFilter(aFilter) 

# print the result
print("Criterion: Edges length > ", length_margin, " Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.GetMesh().CreateGroup(SMESH.EDGE, "Edges with length > " + repr(length_margin))
aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/7ca04fdb816bf99ae8944060cd5b78ef/quality_controls_ex03.py)

## Free Edges

```python
# Free Edges

from mechanic import *

aFilterMgr = smesh_builder.CreateFilterManager()

# Remove some elements to obtain free edges
# Criterion : AREA > 95.
area_margin = 95.

aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Area, SMESH.FT_MoreThan, area_margin)

anIds = mesh.GetIdsFromFilter(aFilter)

mesh.RemoveElements(anIds)

# Criterion : Free Edges
aBorders = mesh.GetFreeBorders() 

# create groups
aGroupF = mesh.CreateEmptyGroup(SMESH.FACE, "Faces with free edges")
aGroupN = mesh.CreateEmptyGroup(SMESH.NODE, "Nodes on free edges")

# fill groups with elements, corresponding to the criterion
print("")
print("Criterion: Free edges Nb = ", len(aBorders))
for i in range(len(aBorders)):
  aBorder = aBorders[i]
  print("Face # ", aBorder.myElemId, " : Edge between nodes (", end=' ')
  print(aBorder.myPnt1, ", ", aBorder.myPnt2, ")")

  aGroupF.Add([aBorder.myElemId])
  aGroupN.Add([aBorder.myPnt1, aBorder.myPnt2])
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/098370e4947f5b9e7ed5d85c61a709ef/quality_controls_ex04.py)

## Free Nodes

```python
# Free Nodes

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create box
box = geom_builder.MakeBox(0., 0., 0., 100., 200., 300.)
idbox = geom_builder.addToStudy(box, "box")

# create a mesh
mesh = smesh_builder.Mesh(box, "Mesh_free_nodes")
mesh.Segment().NumberOfSegments(10)
mesh.Triangle().MaxElementArea(150.)
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# Remove some elements to obtain free nodes
# Criterion : AREA < 80.
area_margin = 80.

aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Area, SMESH.FT_LessThan, area_margin)

anIds = mesh.GetIdsFromFilter(aFilter)

mesh.RemoveElements(anIds)

# criterion : free nodes
aFilter = smesh_builder.GetFilter(SMESH.NODE, SMESH.FT_FreeNodes)
anNodeIds = mesh.GetIdsFromFilter(aFilter)

# create a group
aGroup = mesh.CreateEmptyGroup(SMESH.NODE, "Free_nodes")
aGroup.Add(anNodeIds)

# print the result
print("Criterion: Free nodes Nb = ", len(anNodeIds))
j = 1
for i in range(len(anNodeIds)):
  if j > 20: j = 1; print("")
  print(anNodeIds[i], end=' ')
  j = j + 1
  pass
print("")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/ce01ec48183a7782c91a48ea06a3b7da/quality_controls_ex05.py)

## Free Faces

```python
# Free Faces

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

####### GEOM part ########

Box_1 = geom_builder.MakeBoxDXDYDZ(200, 200, 200)
Box_1_vertex_6 = geom_builder.GetSubShape(Box_1, [6])
Box_1 = geom_builder.GetMainShape(Box_1_vertex_6)
Box_1_vertex_16 = geom_builder.GetSubShape(Box_1, [16])
Box_1 = geom_builder.GetMainShape(Box_1_vertex_16)
Box_1_vertex_11 = geom_builder.GetSubShape(Box_1, [11])
Box_1 = geom_builder.GetMainShape(Box_1_vertex_11)
Plane_1 = geom_builder.MakePlaneThreePnt(Box_1_vertex_6, Box_1_vertex_16, Box_1_vertex_11, 2000)
Partition_1 = geom_builder.MakePartition([Box_1], [Plane_1], [], [], geom_builder.ShapeType["SOLID"], 0, [], 0)

Box_1_vertex_19 = geom_builder.GetSubShape(Box_1, [19])
Box_1_vertex_21 = geom_builder.GetSubShape(Box_1, [21])
Plane_2 = geom_builder.MakePlaneThreePnt(Box_1_vertex_16, Box_1_vertex_19, Box_1_vertex_21, 2000)

geom_builder.addToStudy( Box_1, "Box_1" )
geom_builder.addToStudyInFather( Box_1, Box_1_vertex_6, "Box_1:vertex_6" )
geom_builder.addToStudyInFather( Box_1, Box_1_vertex_16, "Box_1:vertex_16" )
geom_builder.addToStudyInFather( Box_1, Box_1_vertex_11, "Box_1:vertex_11" )
geom_builder.addToStudy( Plane_1, "Plane_1" )
geom_builder.addToStudy( Partition_1, "Partition_1" )
geom_builder.addToStudyInFather( Box_1, Box_1_vertex_19, "Box_1:vertex_19" )
geom_builder.addToStudyInFather( Box_1, Box_1_vertex_21, "Box_1:vertex_21" )
geom_builder.addToStudy( Plane_2, "Plane_2" )

###### SMESH part ######

Mesh_1 = smesh_builder.Mesh(Partition_1)
Mesh_1.Segment().MaxSize(34.641)
Mesh_1.Triangle()
Mesh_1.Tetrahedron()
if not Mesh_1.Compute(): raise Exception("Error when computing Mesh")

# create a group of free faces
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_FreeFaces )
aFaceIds = Mesh_1.GetIdsFromFilter(aFilter)

aGroup = Mesh_1.CreateEmptyGroup(SMESH.FACE, "Free_faces")
aGroup.Add(aFaceIds)

# print the result
print("Criterion: Free faces Nb = ", len(aFaceIds))
j = 1
for i in range(len(aFaceIds)):
  if j > 20: j = 1; print("")
  print(aFaceIds[i], end=' ')
  j = j + 1
  pass
print("")

#filter faces from plane 2
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_BelongToPlane, Plane_2)
aFaceIds = Mesh_1.GetIdsFromFilter(aFilter)
aGroup.Remove(aFaceIds)

# create a group of shared faces (located on partition boundary inside box)
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_BelongToPlane, Plane_1)
aFaceIds = Mesh_1.GetIdsFromFilter(aFilter)

aGroup = Mesh_1.CreateEmptyGroup(SMESH.FACE, "Shared_faces")
aGroup.Add(aFaceIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/f36989a47f419e5124112b8f19733b45/quality_controls_ex06.py)

## Bare border faces

```python
# Bare border faces

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

box = geom_builder.MakeBoxDXDYDZ(100, 100, 100)
geom_builder.addToStudy( box, "box" )

mesh = smesh_builder.Mesh(box)
mesh.Segment().NumberOfSegments(3)
mesh.Quadrangle()
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# remove 2 faces
allFaces = mesh.GetElementsByType(SMESH.FACE)
mesh.RemoveElements( allFaces[0:2])

bareGroup = mesh.MakeGroup("bare faces", SMESH.FACE, SMESH.FT_BareBorderFace)
assert(bareGroup.Size() == 3)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/dcf4d3cce910090f9a4373b4ab01a025/quality_controls_ex07.py)

## Bare border volumes

```python
# Bare border volumes

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

box = geom_builder.MakeBoxDXDYDZ(100, 30, 10)
# the smallest face of the box
face = geom_builder.SubShapeAllSorted( box, geom_builder.ShapeType["FACE"])[0]

geom_builder.addToStudy( box, "box" )
geom_builder.addToStudyInFather( box, face, "face" )

mesh = smesh_builder.Mesh(box)
mesh.AutomaticHexahedralization();

# remove half of mesh faces from the smallest face
faceFaces = mesh.GetSubMeshElementsId(face)
faceToRemove = faceFaces[: len(faceFaces) // 2]
mesh.RemoveElements( faceToRemove )

# make a group of volumes missing the removed faces
bareGroup = mesh.MakeGroup("bare volumes", SMESH.VOLUME, SMESH.FT_BareBorderVolume)
assert(bareGroup.Size() == len( faceToRemove))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/5c146d948a478fc8d37fe11c013b3a8a/quality_controls_ex08.py)

## Over-constrained faces

```python
# Over-constrained faces

import salome
salome.salome_init_without_session()

import SMESH
from salome.smesh import smeshBuilder

smesh_builder = smeshBuilder.New()

mesh = smesh_builder.Mesh()
faceFilter = smesh_builder.GetFilter(SMESH.FACE,SMESH.FT_OverConstrainedFace)

#make an edge
n1 = mesh.AddNode(0,0,0)
n2 = mesh.AddNode(10,0,0)
edge = mesh.AddEdge([n1,n2])
assert( not mesh.GetIdsFromFilter( faceFilter ))

# make faces
mesh.ExtrusionSweep([edge], smesh_builder.MakeDirStruct(0,7,0), 5)
assert( 5 == len( mesh.GetIdsFromFilter( faceFilter )))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/013253f4d64fec8d55b7f629a522ee19/quality_controls_ex09.py)

## Over-constrained volumes

```python
# Over-constrained volumes

import salome
salome.salome_init_without_session()

import SMESH
from salome.smesh import smeshBuilder

smesh_builder = smeshBuilder.New()

mesh = smesh_builder.Mesh()
volumeFilter = smesh_builder.GetFilter(SMESH.VOLUME,SMESH.FT_OverConstrainedVolume)

# make volumes by extrusion of one face
n1 = mesh.AddNode(0,0,0)
n2 = mesh.AddNode(10,0,0)
edge = mesh.AddEdge([n1,n2])
mesh.ExtrusionSweep([edge], smesh_builder.MakeDirStruct(0,7,0), 1)
mesh.ExtrusionSweep( mesh.GetElementsByType(SMESH.FACE), smesh_builder.MakeDirStruct(0,0,5), 7)
assert( 7 == len( mesh.GetIdsFromFilter( volumeFilter )))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/34dabee7265e934874012d22953e4b80/quality_controls_ex10.py)

## Length 2D

```python
# Length 2D

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create open shell: a box without one plane
box = geom_builder.MakeBox(0., 0., 0., 20., 20., 15.)
FaceList = geom_builder.SubShapeAll(box, geom_builder.ShapeType["FACE"])
FaceList.remove(FaceList[5])
box = geom_builder.MakeShell(FaceList)
idbox = geom_builder.addToStudy(box, "box")

# create a mesh
mesh = smesh_builder.Mesh(box, "Mesh_Length_2D")
algo = mesh.Segment()
algo.NumberOfSegments(5)
algo = mesh.Triangle()
algo.MaxElementArea(20.)
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# Criterion : Length 2D > 5.7
length_margin = 5.7

aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Length2D, SMESH.FT_MoreThan, length_margin)

anIds = mesh.GetIdsFromFilter(aFilter)

# print the result
print("Criterion: Edges length 2D > ", length_margin, " Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.CreateEmptyGroup(SMESH.FACE, "Faces with length 2D > " + repr(length_margin))
aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/312ffc60869759ebab2bb80f5f34095b/quality_controls_ex11.py)

## Deflection 2D

```python
# Deflection 2D

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# fuse a box and a sphere
Sphere_1 = geom_builder.MakeSphereR(100)
Box_1 = geom_builder.MakeBoxDXDYDZ(200, 200, 200)
Fuse = geom_builder.MakeFuse( Sphere_1, Box_1, theName="box + sphere" )

# create a mesh
mesh = smesh_builder.Mesh( Fuse, "Deflection_2D")
algo = mesh.Segment()
algo.LocalLength(35)
algo = mesh.Triangle()
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# get min and max deflection
minMax = mesh.GetMinMax( SMESH.FT_Deflection2D )
print("min and max deflection: ", minMax)

# get deflection of a certain face
faceID = mesh.NbEdges() + mesh.NbFaces()
defl = mesh.FunctorValue( SMESH.FT_Deflection2D, faceID )
print("deflection of face %s = %s" % ( faceID, defl ))

margin = minMax[1] / 2

# get all faces with deflection LESS than the margin
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Deflection2D, '<', margin, mesh=mesh)
anIds = aFilter.GetIDs()
print("%s faces have deflection less than %s" %( len(anIds), margin ))

# create a group of faces with deflection MORE than the margin
aGroup = mesh.MakeGroup("Deflection > " + repr(margin), SMESH.FACE, SMESH.FT_Deflection2D,'>',margin)
print("%s faces have deflection more than %s: %s ..." %( aGroup.Size(), margin, aGroup.GetIDs()[:10] ))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/37673254f9b63fada7fbb4615e45f8ec/quality_controls_defl.py)

## Borders at Multiconnection 2D

```python
# Borders at Multiconnection 2D

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a compound of two glued boxes
box1 = geom_builder.MakeBox(0., 0., 0., 20., 20., 15.)
box2 = geom_builder.MakeTranslation(box1, 0., 20., 0)
comp = geom_builder.MakeCompound([box1, box2])
box = geom_builder.MakeGlueFaces(comp, 0.000001)
idbox = geom_builder.addToStudy(box, "box")

# create a mesh
mesh = smesh_builder.Mesh(box, "Box compound : 2D triangle mesh")
algo = mesh.Segment()
algo.NumberOfSegments(5)
algo = mesh.Triangle()
algo.MaxElementArea(20.)
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# Criterion : MULTI-CONNECTION 2D = 3
nb_conn = 3

aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_MultiConnection2D, SMESH.FT_EqualTo, nb_conn)

anIds = mesh.GetIdsFromFilter(aFilter) 

# print the result
print("Criterion: Borders at multi-connection 2D = ", nb_conn, " Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.CreateEmptyGroup(SMESH.FACE, "Borders at multi-connection 2D = " + repr(nb_conn))
aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/e272720547597dc8ddaaa1c80feb26b1/quality_controls_ex12.py)

## Area

```python
# Area

from mechanic import *

# Criterion : AREA > 100.
area_margin = 100.

aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Area, SMESH.FT_MoreThan, area_margin)

anIds = mesh.GetIdsFromFilter(aFilter) 

# print the result
print("Criterion: Area > ", area_margin, " Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.CreateEmptyGroup(SMESH.FACE, "Area > " + repr(area_margin))
aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/569e9a7423d5681a763be08e64eaa5fb/quality_controls_ex13.py)

## Taper

```python
# Taper

from mechanic import *

# Criterion : Taper > 3e-20
taper_margin = 3e-20

aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Taper, SMESH.FT_MoreThan, taper_margin)

anIds = mesh.GetIdsFromFilter(aFilter) 

# print the result
print("Criterion: Taper > ", taper_margin, " Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.CreateEmptyGroup(SMESH.FACE, "Taper > " + repr(taper_margin))
aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/933b59151be42932a34c8cd3d7d461f2/quality_controls_ex14.py)

## Aspect Ratio

```python
# Aspect Ratio

from mechanic import *

# Criterion : ASPECT RATIO > 1.8
ar_margin = 1.8

aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_AspectRatio, SMESH.FT_MoreThan, ar_margin)

anIds = mesh.GetIdsFromFilter(aFilter) 

# print the result
print("Criterion: Aspect Ratio > ", ar_margin, " Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.CreateEmptyGroup(SMESH.FACE, "Aspect Ratio > " + repr(ar_margin))
aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/d79373fdee6d509b097b7a45633808ac/quality_controls_ex15.py)

## Minimum Angle

```python
# Minimum Angle

from mechanic import *

# Criterion : MINIMUM ANGLE < 35.
min_angle = 35.

aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_MinimumAngle, SMESH.FT_LessThan, min_angle)

anIds = mesh.GetIdsFromFilter(aFilter) 

# print the result
print("Criterion: Minimum Angle < ", min_angle, " Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.CreateEmptyGroup(SMESH.FACE, "Minimum Angle < " + repr(min_angle))

aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/b039ec90e4811bb4e3b1194df6047679/quality_controls_ex16.py)

## Warping

```python
# Warping

from mechanic import *

# Criterion : WARP ANGLE > 1e-15
wa_margin = 1e-15

aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Warping, SMESH.FT_MoreThan, wa_margin)

anIds = mesh.GetIdsFromFilter(aFilter) 

# print the result
print("Criterion: Warp > ", wa_margin, " Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.CreateEmptyGroup(SMESH.FACE, "Warp > " + repr(wa_margin))

aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/962ded08703f3616b97041011a75fdf0/quality_controls_ex17.py)

## Skew

```python
# Skew

from mechanic import *

# Criterion : Skew > 38.
skew_margin = 38.

aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Skew, SMESH.FT_MoreThan, skew_margin)

anIds = mesh.GetIdsFromFilter(aFilter)

# print the result
print("Criterion: Skew > ", skew_margin, " Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.CreateEmptyGroup(SMESH.FACE, "Skew > " + repr(skew_margin))
aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/397427995f163df4212c01b98090e9e0/quality_controls_ex18.py)

## Element Diameter 2D

```python
# Element Diameter 2D

from mechanic import *

# Criterion : ELEMENT DIAMETER 2D > 10
mel_2d_margin = 10

aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_MaxElementLength2D, SMESH.FT_MoreThan, mel_2d_margin)

anIds = mesh.GetIdsFromFilter(aFilter) 

# print the result
print("Criterion: Element Diameter 2D Ratio > ", mel_2d_margin, " Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.CreateEmptyGroup(SMESH.FACE, "Element Diameter 2D > " + repr(mel_2d_margin))
aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/38819853c64bbd0a628bc3cd8a5c55a9/quality_controls_ex19.py)

## Aspect Ratio 3D

```python
# Aspect Ratio 3D

from mechanic import *

# Criterion : ASPECT RATIO 3D > 4.5
ar_margin = 4.5

aFilter = smesh_builder.GetFilter(SMESH.VOLUME, SMESH.FT_AspectRatio3D, SMESH.FT_MoreThan, ar_margin)

anIds = mesh.GetIdsFromFilter(aFilter) 

# print the result
print("Criterion: Aspect Ratio 3D > ", ar_margin, " Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.CreateEmptyGroup(SMESH.VOLUME, "Aspect Ratio 3D > " + repr(ar_margin))

aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/7a3ca250670bde1e6a834f10c3527827/quality_controls_ex20.py)

## Volume

```python
# Volume

from mechanic import *

# Criterion : VOLUME < 7.
volume_margin = 7.

aFilter = smesh_builder.GetFilter(SMESH.VOLUME, SMESH.FT_Volume3D, SMESH.FT_LessThan, volume_margin)

anIds = mesh.GetIdsFromFilter(aFilter) 

# print the result
print("")
print("Criterion: Volume < ", volume_margin, " Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.CreateEmptyGroup(SMESH.VOLUME, "Volume < " + repr(volume_margin))

aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/42ac2db1647105f08a6d17889bb58576/quality_controls_ex21.py)

## Element Diameter 3D

```python
# Element Diameter 3D

from mechanic import *

# Criterion : ELEMENT DIAMETER 3D > 10
mel_3d_margin = 10

aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_MaxElementLength3D, SMESH.FT_MoreThan, mel_3d_margin)

anIds = mesh.GetIdsFromFilter(aFilter) 

# print the result
print("Criterion: Element Diameter 3D Ratio > ", mel_3d_margin, " Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.CreateEmptyGroup(SMESH.FACE, "Element Diameter 3D > " + repr(mel_3d_margin))
aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/4ae0786509784cbab09088e01d0de171/quality_controls_ex22.py)

## Scaled Jacobian

```python
# Scaled Jacobian

from mechanic import *

# Criterion : Scaled Jacobian > 0.75
scaledJacobian = 0.75

aFilter = smesh_builder.GetFilter(SMESH.VOLUME, SMESH.FT_ScaledJacobian, SMESH.FT_MoreThan, scaledJacobian)

anIds = mesh.GetIdsFromFilter(aFilter) 

# print the result
print("Criterion: Scaled Jacobian > ", scaledJacobian, " Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.CreateEmptyGroup(SMESH.FACE, "Scaled Jacobian > " + repr(scaledJacobian))
aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/44a31e6442d603175f4f8f21ae63ea29/quality_controls_ex24.py)

## Warping 3D

```python
# Warping

from mechanic import *

# Criterion : WARP ANGLE > 1e-15
wa_margin = 1e-15

aFilter = smesh_builder.GetFilter(SMESH.VOLUME, SMESH.FT_Warping3D, SMESH.FT_MoreThan, wa_margin)

anIds = mesh.GetIdsFromFilter(aFilter) 

# print the result
print("Criterion: Warp > ", wa_margin, " Nb = ", len(anIds))
j = 1
for i in range(len(anIds)):
  if j > 20: j = 1; print("")
  print(anIds[i], end=' ')
  j = j + 1
  pass
print("")

# create a group
aGroup = mesh.CreateEmptyGroup(SMESH.VOLUME, "Warp > " + repr(wa_margin))

aGroup.Add(anIds)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/5185329efb276b3e61c7bbea9714b75b/quality_controls_ex23.py)
