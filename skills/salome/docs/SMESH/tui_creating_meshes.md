<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/tui_creating_meshes.html -->

# Creating Meshes

First of all see [Example of 3d mesh generation:](smeshpy_interface.md#example-3d-mesh) which is an example of good python script style for Mesh module.

## Construction of a mesh

```python
# Construction of a Mesh

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a box
box = geom_builder.MakeBox(0., 0., 0., 100., 200., 300.)
idbox = geom_builder.addToStudy(box, "box")

# create a mesh
tetra = smesh_builder.Mesh(box, "MeshBox")

algo1D = tetra.Segment()
algo1D.NumberOfSegments(7)

algo2D = tetra.Triangle()
algo2D.MaxElementArea(800.)

algo3D = tetra.Tetrahedron()
algo3D.MaxElementVolume(900.)

# compute the mesh
ret = tetra.Compute()
if not ret:
    raise Exception("problem when computing the mesh")

print("mesh computed")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/2e1bc23c47a71c74d92ae330a559b18a/creating_meshes_ex01.py)

## Construction of a sub-mesh

```python
# Construction of a Sub-mesh

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a box
box = geom_builder.MakeBoxDXDYDZ(10., 10., 10.)
geom_builder.addToStudy(box, "Box")

# select one edge of the box for definition of a local hypothesis
p5 = geom_builder.MakeVertex(5., 0., 0.)
EdgeX = geom_builder.GetEdgeNearPoint(box, p5)
geom_builder.addToStudyInFather(box, EdgeX, "Edge [0,0,0 - 10,0,0]")

# create a hexahedral mesh on the box
mesh = smesh_builder.Mesh(box, "Box : hexahedral 3D mesh")

# create a Regular_1D algorithm for discretization of edges
algo1D = mesh.Segment()

# define "NumberOfSegments" hypothesis to cut
# all the edges in a fixed number of segments
algo1D.NumberOfSegments(4)

# create a quadrangle 2D algorithm for the faces
mesh.Quadrangle()

# construct a sub-mesh on the edge with a local Regular_1D algorithm
algo_local = mesh.Segment(EdgeX)

# define "Arithmetic1D" hypothesis to cut EdgeX in several segments with length arithmetically
# increasing from 1.0 to 4.0
algo_local.Arithmetic1D(1, 4)

# define "Propagation" hypothesis that propagates algo_local and "Arithmetic1D" hypothesis
# from EdgeX to all parallel edges
algo_local.Propagation()

# assign a hexahedral algorithm
mesh.Hexahedron()

# any sub-shape can be meshed individually --
# compute mesh on two surfaces using different methods

# get surfaces
surfaces = geom_builder.SubShapeAll(box, geom_builder.ShapeType["FACE"])

# method 1: no sub-mesh is created
if not mesh.Compute( surfaces[0] ): raise Exception("Error when computing Mesh")

# method 2: a sub-mesh is created
submesh = mesh.GetSubMesh( surfaces[2], "submesh 2" )
if not submesh.Compute(): raise Exception("Error when computing Mesh")

# compute the whole mesh
if not mesh.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/809457231d64ed785d040a528df9517e/creating_meshes_ex02.py)

## Change priority of sub-meshes in mesh

```python
# Change priority of sub-meshes in Mesh

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

box = geom_builder.MakeBoxDXDYDZ(200, 200, 200)
[Face_1, Face_2, Face_3, Face_4, Face_5, Face_6] = geom_builder.SubShapeAllSorted(box, geom_builder.ShapeType["FACE"])

# create Mesh object on Box shape
mesh = smesh_builder.Mesh(box)

# assign mesh algorithms and hypotheses
mesh.Segment().NumberOfSegments(20)
mesh.Triangle().MaxElementArea(1200)
mesh.Tetrahedron().MaxElementVolume(40000)

# create sub-mesh and assign algorithms on Face_1
mesh.Segment(geom=Face_1).NumberOfSegments(4)
mesh.Triangle(geom=Face_1)

# create sub-mesh and assign algorithms on Face_2
mesh.Segment(geom=Face_2).NumberOfSegments(8)
mesh.Triangle(geom=Face_2)

# create sub-mesh and assign algorithms on Face_3
mesh.Segment(geom=Face_3).NumberOfSegments(12)
mesh.Triangle(geom=Face_3)

# get existing sub-mesh priority order: F1 -> F2 -> F3
[[SubMesh_F1, SubMesh_F3, SubMesh_F2]] = mesh.GetMeshOrder()
isDone = mesh.Compute()
if not isDone: raise Exception("Error when computing Mesh")
print("Nb elements at initial order of sub-meshes:", mesh.NbElements())

# set new sub-mesh order: F2 -> F1 -> F3
isDone = mesh.SetMeshOrder([[SubMesh_F2, SubMesh_F1, SubMesh_F3]])
isDone = mesh.Compute()
if not isDone: raise Exception("Error when computing Mesh")
print("Nb elements at new order of sub-meshes:", mesh.NbElements())

# compute with other sub-mesh order: F3 -> F2 -> F1
isDone = mesh.SetMeshOrder([[SubMesh_F3, SubMesh_F2, SubMesh_F1]])
isDone = mesh.Compute()
if not isDone: raise Exception("Error when computing Mesh")
print("Nb elements at another order of sub-meshes:", mesh.NbElements())
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/20dd6dc63a95d45b6dfa560c10a1a560/creating_meshes_ex03.py)

## Intermediate edition while meshing

```python
import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
geompy = geomBuilder.New()

# This script demonstrates generation of 3D mesh basing on a modified 2D mesh
#
# Purpose is to get a tetrahedral mesh in a sphere cut by a cube.
# The requirement is to have a surface mesh on the cube comprised of
# triangles of exactly the same size arranged in a grid pattern.
#
# To fulfill this requirement we mesh the box using Quadrangle: Mapping
# meshing algorithm, split quadrangles into triangles and then generate
# tetrahedrons.

# Make the geometry

Box_1    = geompy.MakeBox(-100,-100,-100, 100, 100, 100)
Sphere_1 = geompy.MakeSphereR( 300 )
Cut_1    = geompy.MakeCut(Sphere_1, Box_1, theName="Cut_1")
# get a spherical face
Sph_Face = geompy.ExtractShapes( Sphere_1, geompy.ShapeType["FACE"] )[0]

# get the shape Sph_Face turned into during MakeCut()
Sph_Face = geompy.GetInPlace(Cut_1, Sph_Face, isNewImplementation=True, theName="Sphere_1")

# 1) Define a mesh with 1D and 2D meshers

import  SMESH
from salome.smesh import smeshBuilder
smesh = smeshBuilder.New()

Mesh_1 = smesh.Mesh(Cut_1)

# "global" meshers (assigned to Cut_1) that will be used for the box
Regular_1D = Mesh_1.Segment()
Local_Length_1 = Regular_1D.LocalLength(20)
Quadrangle_2D = Mesh_1.Quadrangle()

# a "local" mesher (assigned to a sub-mesh on Sphere_1) to mesh the sphere
algo_2D = Mesh_1.Triangle( smeshBuilder.NETGEN_1D2D, Sph_Face )
algo_2D.SetMaxSize( 70. )
algo_2D.SetFineness( smeshBuilder.Moderate )
algo_2D.SetMinSize( 7. )

# 2) Compute 2D mesh
isDone = Mesh_1.Compute()
if not isDone:
  raise Exception("Error when computing Mesh")

# 3) Split quadrangles into triangles
Mesh_1.SplitQuadObject( Mesh_1, Diag13=True )

# 4) Define a 3D mesher
Mesh_1.Tetrahedron()

# 5) Compute 3D mesh
isDone = Mesh_1.Compute()
if not isDone:
  raise Exception("Error when computing Mesh")

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/08f8cef87b834f3cc0c594623c00a4e8/a3DmeshOnModified2Dmesh.py)

## Editing a mesh (i.e. changing hypotheses)

```python
# Editing of a mesh

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

def PrintMeshInfo(theMesh):
    aMesh = theMesh.GetMesh()
    print("Information about mesh:")
    print("Number of nodes       : ", aMesh.NbNodes())
    print("Number of edges       : ", aMesh.NbEdges())
    print("Number of faces       : ", aMesh.NbFaces())
    print("Number of volumes     : ", aMesh.NbVolumes())
    pass

# create a box
box = geom_builder.MakeBox(0., 0., 0., 20., 20., 20.)
geom_builder.addToStudy(box, "box")

# select one edge of the box for definition of a local hypothesis
subShapeList = geom_builder.SubShapeAll(box, geom_builder.ShapeType["EDGE"])
edge = subShapeList[0]
name = geom_builder.SubShapeName(edge, box)
geom_builder.addToStudyInFather(box, edge, name)

# create a mesh
tria = smesh_builder.Mesh(box, "Mesh 2D")
algo1D = tria.Segment()
hyp1 = algo1D.NumberOfSegments(3)
algo2D = tria.Triangle()
hyp2 = algo2D.MaxElementArea(10.)

# create a sub-mesh
algo_local = tria.Segment(edge)
hyp3 = algo_local.Arithmetic1D(1, 6)
hyp4 = algo_local.Propagation()

# compute the mesh
if not tria.Compute(): raise Exception("Error when computing Mesh")
PrintMeshInfo(tria)

# remove a local hypothesis
tria.RemoveHypothesis(hyp4, edge)

# compute the mesh
if not tria.Compute(): raise Exception("Error when computing Mesh")
PrintMeshInfo(tria)

# change the value of the 2D hypothesis
hyp2.SetMaxElementArea(2.)

# compute the mesh
if not tria.Compute(): raise Exception("Error when computing Mesh")
PrintMeshInfo(tria)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/774e54b71ae25baab1b1fdc43954d133/creating_meshes_ex04.py)

## Export of a Mesh

```python
# Export of a Mesh

import os
import tempfile
import MEDLoader

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a box
box = geom_builder.MakeBox(0., 0., 0., 100., 200., 300.)
idbox = geom_builder.addToStudy(box, "box")

# create a mesh
tetra = smesh_builder.Mesh(box, "MeshBox")
tetra.Segment().NumberOfSegments(7)
tetra.Triangle()
tetra.Tetrahedron()

# compute the mesh
if not tetra.Compute(): raise Exception("Error when computing Mesh")

# export the mesh in a MED file
medFile = tempfile.NamedTemporaryFile(suffix=".med").name
tetra.ExportMED( medFile, 0 )

# export a group in a MED file
face = geom_builder.SubShapeAll( box, geom_builder.ShapeType["FACE"])[0] # a box side
group = tetra.GroupOnGeom( face, "face group" ) # group of 2D elements on the <face>
tetra.ExportMED( medFile, meshPart=group )

# ========================
# autoDimension parameter
# ========================

face = geom_builder.MakeFaceHW( 10, 10, 1, "rectangle" )
mesh2D = smesh_builder.Mesh( face, "mesh2D" )
mesh2D.AutomaticHexahedralization(0)

# exported mesh is in 2D space because it is a planar mesh lying
# on XOY plane, and autoDimension=True by default
mesh2D.ExportMED( medFile )
medMesh = MEDLoader.ReadUMeshFromFile(medFile,mesh2D.GetName(),0)
print("autoDimension==True, exported mesh is in %sD"%medMesh.getSpaceDimension())

# exported mesh is in 3D space, same as in Mesh module,
# thanks to autoDimension=False
mesh2D.ExportMED( medFile, autoDimension=False )
medMesh = MEDLoader.ReadUMeshFromFile(medFile,mesh2D.GetName(),0)
print("autoDimension==False, exported mesh is in %sD"%medMesh.getSpaceDimension())

os.remove( medFile )
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/c817a9ea69fd258c9ec9255ac0229c1c/creating_meshes_ex05.py)

## How to mesh a cylinder with hexahedrons?

The next script creates a hexahedral mesh on a cylinder. A picture below the script
demonstrates the resulting mesh.

```python
# Creating a hexahedral mesh on a cylinder.
#
# This example uses Partition to divide the cylinder into blocks, which is
# a general approach. But for the case of cylinder there is a dedicated
# command creating a blocked cylinder: geom_builder.MakeDividedCylinder()

import math

import salome
salome.salome_init_without_session()

import GEOM
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# Parameters
# ----------

radius =  50
height = 200

# Build a cylinder
# ----------------

base      = geom_builder.MakeVertex(0, 0, 0)
direction = geom_builder.MakeVectorDXDYDZ(0, 0, 1)

cylinder = geom_builder.MakeCylinder(base, direction, radius, height)

geom_builder.addToStudy(cylinder, "cylinder")

# Build blocks
# ------------

size = radius/2.0

box_rot  = geom_builder.MakeBox(-size, -size, 0,  +size, +size, height)
box_axis = geom_builder.MakeLine(base, direction)
box      = geom_builder.MakeRotation(box_rot, box_axis, math.pi/4)

hole = geom_builder.MakeCut(cylinder, box)

plane_trim = 2000

plane_a = geom_builder.MakePlane(base, geom_builder.MakeVectorDXDYDZ(1, 0, 0), plane_trim)
plane_b = geom_builder.MakePlane(base, geom_builder.MakeVectorDXDYDZ(0, 1, 0), plane_trim)

blocks_part = geom_builder.MakePartition([hole], [plane_a, plane_b], [], [], geom_builder.ShapeType["SOLID"])
blocks_list = [box] + geom_builder.SubShapeAll(blocks_part, geom_builder.ShapeType["SOLID"])
blocks_all  = geom_builder.MakeCompound(blocks_list)
blocks      = geom_builder.MakeGlueFaces(blocks_all, 0.0001)

geom_builder.addToStudy(blocks, "cylinder:blocks")

# Build geometric groups
# ----------------------

group_a = geom_builder.CreateGroup(blocks, geom_builder.ShapeType["FACE"])
geom_builder.addToStudyInFather(blocks, group_a, "baseA")
items = geom_builder.GetShapesOnPlaneWithLocationIDs(blocks, geom_builder.ShapeType["FACE"], direction, base, GEOM.ST_ON)
geom_builder.UnionIDs(group_a, items)

base_b = geom_builder.MakeVertex(0, 0, height)
group_b = geom_builder.CreateGroup(blocks, geom_builder.ShapeType["FACE"])
geom_builder.addToStudyInFather(blocks, group_b, "baseB")
items = geom_builder.GetShapesOnPlaneWithLocationIDs(blocks, geom_builder.ShapeType["FACE"], direction, base_b, GEOM.ST_ON)
geom_builder.UnionIDs(group_b, items)

group_1 = geom_builder.CreateGroup(blocks, geom_builder.ShapeType["SOLID"])
geom_builder.addToStudyInFather(blocks, group_1, "limit")
group_1_all = geom_builder.SubShapeAllIDs(blocks, geom_builder.ShapeType["SOLID"])
geom_builder.UnionIDs(group_1, group_1_all)
group_1_box = geom_builder.GetBlockNearPoint(blocks, base)
geom_builder.DifferenceList(group_1, [group_1_box])

# Mesh the blocks with hexahedral
# -------------------------------

smesh_builder.UpdateStudy()

hexa = smesh_builder.Mesh(blocks)

hexa_1d = hexa.Segment()
hexa_1d.NumberOfSegments(1)

vertex = geom_builder.MakeVertex(+radius, +radius, 0)
edge = geom_builder.GetEdgeNearPoint(blocks, vertex)
algo = hexa.Segment(edge)
algo.NumberOfSegments(5)
algo.Propagation()

vertex = geom_builder.MakeVertex(-radius, +radius, 0)
edge = geom_builder.GetEdgeNearPoint(blocks, vertex)
algo = hexa.Segment(edge)
algo.NumberOfSegments(8)
algo.Propagation()

vertex = geom_builder.MakeVertex((radius+size)/2, 0, 0)
edge = geom_builder.GetEdgeNearPoint(blocks, vertex)
algo = hexa.Segment(edge)
algo.NumberOfSegments(10)
algo.Propagation()

vertex = geom_builder.MakeVertex(+radius, 0, height/2)
edge = geom_builder.GetEdgeNearPoint(blocks, vertex)
algo = hexa.Segment(edge)
algo.NumberOfSegments(20)
algo.Propagation()

hexa.Quadrangle()
hexa.Hexahedron()

if not hexa.Compute(): raise Exception("Error when computing Mesh")

hexa.Group(group_a)
hexa.Group(group_b)
hexa.Group(group_1)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/6c99165de2ef76bd1a5ae6a6478f04b9/creating_meshes_ex06.py)

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/mesh_cylinder_hexa.png)

## Building a compound of meshes

```python
# Building a compound of meshes

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

## create a bottom box
Box_inf = geom_builder.MakeBox(0., 0., 0., 200., 200., 50.)

# get a top face
Psup1=geom_builder.MakeVertex(100., 100., 50.)
Fsup1=geom_builder.GetFaceNearPoint(Box_inf, Psup1)
# get a bottom face
Pinf1=geom_builder.MakeVertex(100., 100., 0.)
Finf1=geom_builder.GetFaceNearPoint(Box_inf, Pinf1)

## create a top box
Box_sup = geom_builder.MakeBox(100., 100., 50., 200., 200., 100.)

# get a top face
Psup2=geom_builder.MakeVertex(150., 150., 100.)
Fsup2=geom_builder.GetFaceNearPoint(Box_sup, Psup2)
# get a bottom face
Pinf2=geom_builder.MakeVertex(150., 150., 50.)
Finf2=geom_builder.GetFaceNearPoint(Box_sup, Pinf2)

## Publish in the study
geom_builder.addToStudy(Box_inf, "Box_inf")
geom_builder.addToStudyInFather(Box_inf, Fsup1, "Fsup")
geom_builder.addToStudyInFather(Box_inf, Finf1, "Finf")

geom_builder.addToStudy(Box_sup, "Box_sup")
geom_builder.addToStudyInFather(Box_sup, Fsup2, "Fsup")
geom_builder.addToStudyInFather(Box_sup, Finf2, "Finf")

smesh_builder.UpdateStudy()

## create a bottom mesh
Mesh_inf = smesh_builder.Mesh(Box_inf, "Mesh_inf")
algo1D_1=Mesh_inf.Segment()
algo1D_1.NumberOfSegments(10)
algo2D_1=Mesh_inf.Quadrangle()
algo3D_1=Mesh_inf.Hexahedron()
if not Mesh_inf.Compute(): raise Exception("Error when computing Mesh")

# create a group on the top face
Gsup1=Mesh_inf.Group(Fsup1, "Sup")
# create a group on the bottom face
Ginf1=Mesh_inf.Group(Finf1, "Inf")

## create a top mesh
Mesh_sup = smesh_builder.Mesh(Box_sup, "Mesh_sup")
algo1D_2=Mesh_sup.Segment()
algo1D_2.NumberOfSegments(5)
algo2D_2=Mesh_sup.Quadrangle()
algo3D_2=Mesh_sup.Hexahedron()
if not Mesh_sup.Compute(): raise Exception("Error when computing Mesh")

# create a group on the top face
Gsup2=Mesh_sup.Group(Fsup2, "Sup")
# create a group on the bottom face
Ginf2=Mesh_sup.Group(Finf2, "Inf")

## create compounds
# create a compound of two meshes with renaming namesake groups and
# merging elements with the given tolerance
Compound1 = smesh_builder.Concatenate([Mesh_inf, Mesh_sup], 0, 1, 1e-05,
                                      name='Compound with RenamedGrps and MergeElems')
# create a compound of two meshes with uniting namesake groups and
# creating groups of all elements
Compound2 = smesh_builder.Concatenate([Mesh_inf, Mesh_sup], 1, 0, 1e-05, True,
                                      name='Compound with UniteGrps and GrpsOfAllElems')

# copy Gsup1 into a separate mesh and translate it
groupMesh = Mesh_inf.TranslateObjectMakeMesh( Gsup1, [300,0,0] )

# add Ginf2 to groupMesh
smesh_builder.Concatenate([Ginf2], False, meshToAppendTo = groupMesh )

if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/d73350ff5ce13b42b593f9bfc63628cc/creating_meshes_ex07.py)

## Mesh Copying

```python
# Mesh Copying

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# make geometry of a box
box = geom_builder.MakeBoxDXDYDZ(100,100,100)
face = geom_builder.SubShapeAllSorted(box, geom_builder.ShapeType["FACE"])[0]

# generate a prismatic 3D mesh
mesh = smesh_builder.Mesh(box, "box")
localAlgo = mesh.Triangle(face)
mesh.Segment().NumberOfSegments( 3 )
mesh.Quadrangle()
mesh.Prism()
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# objects to copy
fGroup = mesh.GroupOnGeom( face, "2D on face")
nGroup = mesh.GroupOnGeom( face, "nodes on face", SMESH.NODE)
subMesh = localAlgo.GetSubMesh()

# make a new mesh by copying different parts of the mesh

# 1. copy the whole mesh
newMesh = smesh_builder.CopyMesh( mesh, "whole mesh copy")

# 2. copy a group of 2D elements along with groups
newMesh = smesh_builder.CopyMesh( fGroup,  "face group copy with groups",toCopyGroups=True)

# 3. copy a group of nodes
newMesh = smesh_builder.CopyMesh( nGroup, "node group copy")

# 4. copy some faces
faceIds = fGroup.GetIDs()[-10:]
newMesh = smesh_builder.CopyMesh( mesh.GetIDSource( faceIds, SMESH.FACE ), "some faces copy")

# 5. copy some nodes
nodeIds = nGroup.GetIDs()[-10:]
newMesh = smesh_builder.CopyMesh( mesh.GetIDSource( nodeIds, SMESH.NODE), "some nodes copy")

# 6. copy a sub-mesh
newMesh = smesh_builder.CopyMesh( subMesh, "sub-mesh copy" )

# make a new mesh with same hypotheses on a modified geometry

smallBox = geom_builder.MakeScaleAlongAxes( box, None, 1, 0.5, 0.5 )
cutBox = geom_builder.MakeCut( box, smallBox, theName="box - smallBox" )

ok, newMesh, groups, submehses, hyps, invIDs = smesh_builder.CopyMeshWithGeom( mesh, cutBox, "cutBox" )
if not newMesh.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/fda5c13ba0c20ebd5af3fe370502ecc8/creating_meshes_ex08.py)

## Creating Dual Mesh

```python
# Creating dual Mesh

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/B61570/work_in_progress/dual_mesh')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS

# Creating a sphere
geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Sphere_1 = geompy.MakeSphereR(100)
[geomObj_1] = geompy.ExtractShapes(Sphere_1, geompy.ShapeType["FACE"], True)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Sphere_1, 'Sphere_1' )

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()

# Meshing sphere in Tetrahedron
NETGEN_3D_Parameters_1 = smesh.CreateHypothesisByAverageLength( 'NETGEN_Parameters', 'NETGENEngine', 34.641, 0 )
Mesh_1 = smesh.Mesh(Sphere_1,'Mesh_1')
status = Mesh_1.AddHypothesis( Sphere_1, NETGEN_3D_Parameters_1 )
NETGEN_1D_2D_3D = Mesh_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
isDone = Mesh_1.Compute()
if not isDone:
  raise Exception("Error when computing Mesh")

# Creating Dual mesh with projection on shape
dual_Mesh_1 = smesh.CreateDualMesh( Mesh_1, 'dual_Mesh_1', True)

assert(dual_Mesh_1.NbPolyhedrons() > 0)
assert(dual_Mesh_1.NbTetras() == 0)

# Creating Dual mesh without projection on shape
dual_Mesh_2 = smesh.CreateDualMesh( Mesh_1, 'dual_Mesh_2', False)

assert(dual_Mesh_2.NbPolyhedrons() > 0)
assert(dual_Mesh_2.NbTetras() == 0)

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/57f52c639c5d931ff2a3e0acb7584f54/create_dual_mesh.py)

## Creating Parallel Mesh

```python
# contains function to compute a mesh in parallel
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder
import SALOMEDS

import numpy as np

geompy = geomBuilder.New()

nbox = 2
boxsize = 100
offset = 0
# Create 3D faces
boxes = []
# First creating all the boxes
for i in range(nbox):
    for j in range(nbox):
        for k in range(nbox):

            x_orig = i*(boxsize+offset)
            y_orig = j*(boxsize+offset)
            z_orig = k*(boxsize+offset)

            tmp_box = geompy.MakeBoxDXDYDZ(boxsize, boxsize, boxsize)

            if not i == j == k == 0:
                box = geompy.MakeTranslation(tmp_box, x_orig,
                                             y_orig, z_orig)
            else:
                box = tmp_box

            geompy.addToStudy(box, 'box_{}:{}:{}'.format(i, j, k))

            boxes.append(box)

# Create fuse of all boxes
all_boxes = geompy.MakeCompound(boxes)
geompy.addToStudy(all_boxes, 'Compound_1')

# Removing duplicates faces and edges
all_boxes = geompy.MakeGlueFaces(all_boxes, 1e-07)
geompy.addToStudy(all_boxes, 'Glued_Faces_1')

rubik_cube = geompy.MakeGlueEdges(all_boxes, 1e-07)
geompy.addToStudy(rubik_cube, 'rubik_cube')

smesh = smeshBuilder.New()
print("Creating Parallel Mesh")
par_mesh = smesh.ParallelMesh(rubik_cube, name="par_mesh")

print("Creating hypoehtesis for netgen")
NETGEN_3D_Parameters_1 = smesh.CreateHypothesisByAverageLength( 'NETGEN_Parameters',
                                         'NETGENEngine', 34.641, 0 )
print("Adding hypothesis")
par_mesh.AddGlobalHypothesis(NETGEN_3D_Parameters_1)

print("Setting parallelism method")
par_mesh.SetParallelismMethod(smeshBuilder.MULTITHREAD)

print("Setting parallelism options")
param = par_mesh.GetParallelismSettings()
param.SetNbThreads(6)

print("Starting parallel compute")
is_done = par_mesh.Compute()
if not is_done:
    raise Exception("Error when computing Mesh")

print("  Tetrahedron: ",  par_mesh.NbTetras())
print("  Triangle: ", par_mesh.NbTriangles())
print("  edge: ", par_mesh.NbEdges())

assert  par_mesh.NbTetras() > 0
assert  par_mesh.NbTriangles() > 0
assert  par_mesh.NbEdges() > 0
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/94dcd25b9a11b6cde27b028fc158da9a/creating_parallel_mesh.py)
