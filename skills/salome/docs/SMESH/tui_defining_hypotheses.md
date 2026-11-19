<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/tui_defining_hypotheses.html -->

# Defining Hypotheses and Algorithms

This page provides example codes of [defining algorithms](#tui-defining-meshing-algos)
and hypotheses.

- Wire discretisation 1D algorithm

  > - [Adaptive](#tui-1d-adaptive) hypothesis
  > - [Arithmetic Progression](#tui-1d-arithmetic) hypothesis
  > - [Geometric Progression](#tui-1d-arithmetic) hypothesis
  > - [Deflection and Number of Segments](#tui-deflection-1d) hypotheses
  > - [Start and End Length](#tui-start-and-end-length) hypothesis
  > - [Local Length](#tui-average-length) hypothesis
  > - [Propagation](#tui-propagation) additional hypotheses
  > - [Fixed Points 1D](#tui-fixed-points) hypothesis
- Triangle: NETGEN 2D algorithm

  > - [Maximum Element Area](#tui-max-element-area) hypothesis
  > - [Length from Edges](#tui-length-from-edges) hypothesis
- Quadrangle: Mapping 2D algorithm

  > - [Quadrangle Parameters](#tui-quadrangle-parameters) hypothesis
- [Radial Quadrangle 1D-2D](#tui-radial-quadrangle) algorithm
- NETGEN 3D algorithm

  > - [Maximum Element Volume](#tui-max-element-volume) hypothesis
  > - [Viscous layers](#tui-viscous-layers) hypotheses
- Hexahedron (i,j,k) 3D algorithm

  > - [Renumber 3D hypothesis](#tui-block-renumber)
- [Projection Algorithms](#tui-projection)
- [Extrusion 3D](#tui-prism-3d-algo) algorithm
- [Radial Prism](#tui-radial-prism) algorithm
- [Body Fitting](#tui-cartesian-algo) algorithm
- [Import 1D-2D Elements from Another Mesh](#tui-import) algorithm
- [Use Faces to be Created Manually](#tui-use-existing-faces) algorithm
- [Segments around Vertex](#tui-segments-around-vertex) algorithm

## Defining 1D Hypotheses

### Arithmetic Progression and Geometric Progression

```python
# Arithmetic Progression and Geometric Progression

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a box
box = geom_builder.MakeBoxDXDYDZ(10., 10., 10.)
geom_builder.addToStudy(box, "Box")

# create a hexahedral mesh on the box
hexa = smesh_builder.Mesh(box, "Box : hexahedrical mesh")

# create a Regular 1D algorithm for edges
algo1D = hexa.Segment()

# optionally reverse node distribution on certain edges
allEdges = geom_builder.SubShapeAllSorted( box, geom_builder.ShapeType["EDGE"])
reversedEdges = [ allEdges[0], allEdges[4] ]

# define "Arithmetic1D" hypothesis to cut all edges in several segments with increasing arithmetic length 
algo1D.Arithmetic1D(1, 4, reversedEdges)

# define "Geometric Progression" hypothesis on one edge to cut this edge in segments with length increasing by 20% starting from 1
gpAlgo = hexa.Segment( allEdges[1] )
gpAlgo.GeometricProgression( 1, 1.2 )

# propagate distribution of nodes computed using "Geometric Progression" to parallel edges
gpAlgo.PropagationOfDistribution() 

# create a quadrangle 2D algorithm for faces
hexa.Quadrangle()

# create a hexahedron 3D algorithm for solids
hexa.Hexahedron()

# compute the mesh
if not hexa.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/12204b4656d0eabca15d091d25ea0502/defining_hypotheses_ex01.py)

### Adaptive

```python
# Usage of Adaptive 1D hypothesis

import math

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

box   = geom_builder.MakeBoxDXDYDZ( 100, 100, 100 )
tool  = geom_builder.MakeTranslation( box, 50, 0, 10 )
axis  = geom_builder.MakeVector( geom_builder.MakeVertex( 100, 0, 100 ),geom_builder.MakeVertex( 100, 10, 100 ),)
tool  = geom_builder.Rotate( tool, axis, math.pi * 25 / 180. )
shape = geom_builder.MakeCut( box, tool )
cyl   = geom_builder.MakeCylinder( geom_builder.MakeVertex( -10,5, 95 ), geom_builder.MakeVectorDXDYDZ(1,0,0), 2, 90)
shape = geom_builder.MakeCut( shape, cyl )
tool  = geom_builder.MakeBoxTwoPnt( geom_builder.MakeVertex( -10, 2, 15 ), geom_builder.MakeVertex( 90, 5, 16 ))
shape = geom_builder.MakeCut( shape, tool, theName="shape" )

# Parameters of Adaptive hypothesis. minSize and maxSize are such that they do not limit
# size of segments because size of geometrical features lies within [2.-100.] range, hence
# size of segments is defined by deflection parameter and size of geometrical features only.
minSize = 0.1
maxSize = 200
deflection = 0.05

mesh = smesh_builder.Mesh( shape )
mesh.Segment().Adaptive( minSize, maxSize, deflection )
mesh.Triangle().MaxElementArea( 300 )
if not mesh.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/d2052e49ad4062c3494c38b97c28793b/defining_hypotheses_adaptive1d.py)

### Deflection and Number of Segments

```python
# Deflection and Number of Segments

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a face from arc and straight segment
px = geom_builder.MakeVertex(100., 0.  , 0.  )
py = geom_builder.MakeVertex(0.  , 100., 0.  )
pz = geom_builder.MakeVertex(0.  , 0.  , 100.)

exy = geom_builder.MakeEdge(px, py)
arc = geom_builder.MakeArc(py, pz, px)

wire = geom_builder.MakeWire([exy, arc])

isPlanarFace = 1
face1 = geom_builder.MakeFace(wire, isPlanarFace)
geom_builder.addToStudy(face1,"Face1")

# get edges from the face
e_straight,e_arc = geom_builder.SubShapeAll(face1, geom_builder.ShapeType["EDGE"])
geom_builder.addToStudyInFather(face1, e_arc, "Arc Edge")

# create hexahedral mesh
hexa = smesh_builder.Mesh(face1, "Face : triangle mesh")

# define "NumberOfSegments" hypothesis to cut a straight edge in a fixed number of segments
algo1D = hexa.Segment()
algo1D.NumberOfSegments(6)

# define "MaxElementArea" hypothesis
algo2D = hexa.Triangle()
algo2D.MaxElementArea(70.0)

# define a local "Deflection1D" hypothesis on the arc
algo_local = hexa.Segment(e_arc)
algo_local.Deflection1D(1.0)

# compute the mesh
if not hexa.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/52f9fb53556d737b9fcb190bfe27e768/defining_hypotheses_ex02.py)

### Start and End Length

```python
# Start and End Length

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a box
box = geom_builder.MakeBoxDXDYDZ(10., 10., 10.)
geom_builder.addToStudy(box, "Box")

# get one edge of the box to put local hypothesis on
p5 = geom_builder.MakeVertex(5., 0., 0.)
EdgeX = geom_builder.GetEdgeNearPoint(box, p5)
geom_builder.addToStudyInFather(box, EdgeX, "Edge [0,0,0 - 10,0,0]")

# create a hexahedral mesh on the box
hexa = smesh_builder.Mesh(box, "Box : hexahedrical mesh")

# set algorithms
algo1D = hexa.Segment()
hexa.Quadrangle()
hexa.Hexahedron()

# define "NumberOfSegments" hypothesis to cut an edge in a fixed number of segments
algo1D.NumberOfSegments(4)

# create a local hypothesis
algo_local = hexa.Segment(EdgeX)

# define "StartEndLength" hypothesis to cut an edge in several segments with increasing geometric length
algo_local.StartEndLength(1, 6)

# define "Propagation" hypothesis that propagates all other hypothesis
# on all edges on the opposite side in case of quadrangular faces
algo_local.Propagation()

# compute the mesh
if not hexa.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/286830fa070d5db024b14075e25d3793/defining_hypotheses_ex03.py)

### Local Length

```python
# Local Length

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a box
box = geom_builder.MakeBoxDXDYDZ(10., 10., 10.)
geom_builder.addToStudy(box, "Box")

# get one edge of the box to put local hypothesis on
p5 = geom_builder.MakeVertex(5., 0., 0.)
EdgeX = geom_builder.GetEdgeNearPoint(box, p5)
geom_builder.addToStudyInFather(box, EdgeX, "Edge [0,0,0 - 10,0,0]")

# create a hexahedral mesh on the box
hexa = smesh_builder.Mesh(box, "Box : hexahedrical mesh")

# set algorithms
algo1D = hexa.Segment()
hexa.Quadrangle()
hexa.Hexahedron()

# define "NumberOfSegments" hypothesis to cut all edges in a fixed number of segments
algo1D.NumberOfSegments(4)

# create a sub-mesh
algo_local = hexa.Segment(EdgeX)

# define "LocalLength" hypothesis to cut an edge in several segments with the same length
algo_local.LocalLength(2.)

# define "Propagation" hypothesis that propagates all other hypothesis
# on all edges on the opposite side in case of quadrangular faces
algo_local.Propagation()

# compute the mesh
if not hexa.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/23de5741d8615d278c47f776beeb989b/defining_hypotheses_ex04.py)

## Defining 2D and 3D hypotheses

### Maximum Element Area

```python
# Maximum Element Area

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a face
px   = geom_builder.MakeVertex(100., 0.  , 0.  )
py   = geom_builder.MakeVertex(0.  , 100., 0.  )
pz   = geom_builder.MakeVertex(0.  , 0.  , 100.)

vxy = geom_builder.MakeVector(px, py)
arc = geom_builder.MakeArc(py, pz, px)
wire = geom_builder.MakeWire([vxy, arc])

isPlanarFace = 1
face = geom_builder.MakeFace(wire, isPlanarFace)

# add the face in the study
id_face = geom_builder.addToStudy(face, "Face to be meshed")

# create a mesh
tria_mesh = smesh_builder.Mesh(face, "Face : triangulation")

# define 1D meshing:
algo = tria_mesh.Segment()
algo.NumberOfSegments(20)

# define 2D meshing:

# assign triangulation algorithm
algo = tria_mesh.Triangle()

# assign "Max Element Area" hypothesis
algo.MaxElementArea(100)

# compute the mesh
if not tria_mesh.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/491d99563ef883947fb4189e656f5872/defining_hypotheses_ex05.py)

### Maximum Element Volume

```python
# Maximum Element Volume

import salome
salome.salome_init_without_session()

from salome.smesh import smeshBuilder
from salome.geom import geomBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a cylinder
cyl = geom_builder.MakeCylinderRH(30., 50.)
geom_builder.addToStudy(cyl, "cyl")

# create a mesh on the cylinder
tetra = smesh_builder.Mesh(cyl, "Cylinder : tetrahedrical mesh")

# assign algorithms
algo1D = tetra.Segment()
algo2D = tetra.Triangle()
algo3D = tetra.Tetrahedron()

# assign 1D and 2D hypotheses
algo1D.NumberOfSegments(7)
algo2D.MaxElementArea(150.)

# assign Max Element Volume hypothesis
algo3D.MaxElementVolume(200.)

# compute the mesh
ret = tetra.Compute()
if ret == 0:
    raise Exception("problem when computing the mesh")

print("Computation succeeded")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/be4c2438025dcfe00122df3da9d5a5ca/defining_hypotheses_ex06.py)

### Length from Edges

```python
# Length from Edges

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create sketchers
sketcher1 = geom_builder.MakeSketcher("Sketcher:F 0 0:TT 70 0:TT 70 70:TT 0 70:WW")
sketcher2 = geom_builder.MakeSketcher("Sketcher:F 20 20:TT 50 20:TT 50 50:TT 20 50:WW")

# create a face from two wires
isPlanarFace = 1
face1 = geom_builder.MakeFaces([sketcher1, sketcher2], isPlanarFace)
geom_builder.addToStudy(face1, "Face1")

# create a mesh
tria = smesh_builder.Mesh(face1, "Face : triangle 2D mesh")

# Define 1D meshing
algo1D = tria.Segment()
algo1D.LocalLength(3.)

# create and assign the algorithm for 2D meshing with triangles
algo2D = tria.Triangle()

# create and assign "LengthFromEdges" hypothesis to build triangles with
# linear size close to the length of the segments generated on the face wires (3.)
algo2D.LengthFromEdges()

# compute the mesh
if not tria.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/da3da08926da17d77395b59d38babe3f/defining_hypotheses_ex07.py)

### Renumber 3D hypothesis

```python
# "Elements of a domain" filter and "Renumber" hypothesis

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create two boxes to have two domains in the mesh

box1 = geom_builder.MakeBoxDXDYDZ( 100,100,100 )
box2 = geom_builder.MakeTranslation( box1, 200, 0, 0 )
boxes = geom_builder.MakeCompound( [box1, box2] )
box1, box2 = geom_builder.SubShapeAll( boxes, geom_builder.ShapeType["SHAPE"], "box")

vertex = geom_builder.SubShape( box1, geom_builder.ShapeType["VERTEX"], [1] )

# create a mesh

mesh = smesh_builder.Mesh( boxes )
mesh.Segment(box1).NumberOfSegments( 5 )  # to have different nb of elements on the boxes
mesh.Segment(box2).NumberOfSegments( 10 )
mesh.Quadrangle()
ijkAlgo = mesh.Hexahedron()

# Use Renumber hypothesis to get hexahedra and nodes numbered like in a structured mesh.
# k axis of box1 will be ( 100,100,0 ) - ( 100,100,100 )
# k axis of box2 will be ( 0,0,0 ) - (0,0,100), by default
v000 = geom_builder.MakeVertex( 100,100,0, theName='v000' ) # can use box sub-vertex or standalone one
v001 = geom_builder.GetVertexNearPoint( box1, geom_builder.MakeVertex(100,100,100), theName='v001')
ijkAlgo.Renumber([ smeshBuilder.BlockCS( box1, v000, v001 ) ])

if not mesh.Compute(): raise Exception("Error when computing Mesh")

# Create filters with FT_ConnectedElements criterion by pointing a domain in different ways:

# using point coordinates in box_1
nodeFilter = smesh_builder.GetFilter( SMESH.NODE, SMESH.FT_ConnectedElements, "=", "1.,2,10", mesh=mesh )
print("Nb. nodes in box_1:", len( nodeFilter.GetIDs()))

# using point coordinates in box_2
edgeFilter = smesh_builder.GetFilter( SMESH.EDGE, SMESH.FT_ConnectedElements, "=", [202,1,1 ], mesh=mesh )
print("Nb. segments in box_2:", len( edgeFilter.GetIDs()))

# using a geom vertex of box_1
faceFilter = smesh_builder.GetFilter( SMESH.FACE, SMESH.FT_ConnectedElements, "=", vertex, mesh=mesh )
print("Nb. faces in box_1:", len( edgeFilter.GetIDs()))

# using node ID in box_2
voluFilter = smesh_builder.GetFilter( SMESH.VOLUME, SMESH.FT_ConnectedElements, "=", 10, mesh=mesh )
print("Nb. volumes in box_2:", len( voluFilter.GetIDs()))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/3e7ca2bf482eb8de750328b030a46634/filters_ex39.py)

## Defining Additional Hypotheses

### Propagation

```python
# Propagation

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a box
base = geom_builder.MakeSketcher("Sketcher:F 0 0:TT 10 0:TT 20 10:TT 0 10:WF", theName="F")
box  = geom_builder.MakePrismDXDYDZ( base, 0,0,10 )
geom_builder.addToStudy(box, "Box")

# get one edge of the box to put local hypothesis on
p5 = geom_builder.MakeVertex(5., 0., 0.)
EdgeX = geom_builder.GetEdgeNearPoint(box, p5)
geom_builder.addToStudyInFather(box, EdgeX, "Edge [0,0,0 - 10,0,0]")

# create a hexahedral mesh on the box
hexa = smesh_builder.Mesh(box, "Propagation of hypothesis")

# set global algorithms and hypotheses
algo1D = hexa.Segment()
hexa.Quadrangle()
hexa.Hexahedron()
algo1D.NumberOfSegments(4)

# create a sub-mesh with local 1D hypothesis and "Propagation of 1D Hypothesis"
algo_local = hexa.Segment(EdgeX)

# define "Arithmetic1D" hypothesis to cut an edge in several segments with increasing length
algo_local.Arithmetic1D(1, 4)

# define "Propagation" hypothesis that propagates "Arithmetic1D" hypothesis
# from 'EdgeX' on opposite sides of all quadilateral faces
algo_local.Propagation()

# compute the mesh which contains prisms
if not hexa.Compute(): raise Exception("Error when computing Mesh")

# create another mesh on the box
mesh = smesh_builder.Mesh(box, "Propagation of distribution of nodes")

# set global algorithms and hypotheses
algo1D = mesh.Segment()
mesh.Quadrangle()
mesh.Hexahedron()
algo1D.NumberOfSegments(4)

# create a sub-mesh with local 1D hypothesis and "Propagation of Node Distribution"
algo_local = mesh.Segment(EdgeX)
algo_local.Arithmetic1D(1, 4)

# define "Propagation Of Distribution" hypothesis that propagates
# distribution of nodes generated by "Arithmetic1D" hypothesis
# from 'EdgeX' on opposite sides of all quadilateral faces
algo_local.PropagationOfDistribution()

# compute the mesh which contains hexahedra only
if not mesh.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/73bc5b3a84ec2ad604aab633469fa58c/defining_hypotheses_ex08.py)

## Defining Meshing Algorithms

```python
# Defining Meshing Algorithms

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a box
box = geom_builder.MakeBoxDXDYDZ(10., 10., 10.)
geom_builder.addToStudy(box, "Box")

# Create a hexahedral mesh on the box
hexa = smesh_builder.Mesh(box, "Box : hexahedrical mesh")

# create a Regular 1D algorithm for edges
algo1D = hexa.Segment()

# create a quadrangle 2D algorithm for faces
algo2D = hexa.Quadrangle()

# create a hexahedron 3D algorithm for solids
algo3D = hexa.Hexahedron()

# define hypotheses
algo1D.Arithmetic1D(1, 4)

# compute the mesh
if not hexa.Compute(): raise Exception("Error when computing Mesh")

# 2. Create a tetrahedral mesh on the box
tetra = smesh_builder.Mesh(box, "Box : tetrahedrical mesh")

# create a 1D algorithm for edges
algo1D = tetra.Segment()

# create a 2D algorithm for faces
algo2D = tetra.Triangle()

# create a 3D algorithm for solids
algo3D = tetra.Tetrahedron()

# define hypotheses
algo1D.Arithmetic1D(1, 4)
algo2D.LengthFromEdges()

# compute the mesh
if not tetra.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/ea2e49d2304cee04753f564e698ac0d7/defining_hypotheses_ex09.py)

### Projection Algorithms

```python
# Projection Algorithms

# Project prisms from one meshed box to another mesh on the same box

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# Prepare geometry

# Create a parallelepiped
box = geom_builder.MakeBoxDXDYDZ(200, 100, 70)
geom_builder.addToStudy( box, "box" )

# Get geom faces to mesh with triangles in the 1ts and 2nd meshes
faces = geom_builder.SubShapeAll(box, geom_builder.ShapeType["FACE"])
# 2 adjacent faces of the box
f1 = faces[2]
f2 = faces[0]
# face opposite to f2
f2opp = geom_builder.GetOppositeFace( box, f2 )

# Get vertices used to specify how to associate sides of faces at projection
[v1F1, v2F1] = geom_builder.SubShapeAll(f1, geom_builder.ShapeType["VERTEX"])[:2]
[v1F2, v2F2] = geom_builder.SubShapeAll(f2, geom_builder.ShapeType["VERTEX"])[:2]
geom_builder.addToStudyInFather( box, v1F1, "v1F1" )
geom_builder.addToStudyInFather( box, v2F1, "v2F1" )
geom_builder.addToStudyInFather( box, v1F2, "v1F2" )
geom_builder.addToStudyInFather( box, v2F2, "v2F2" )

# Make group of 3 edges of f1 and f2
edgesF1 = geom_builder.CreateGroup(f1, geom_builder.ShapeType["EDGE"])
geom_builder.UnionList( edgesF1, geom_builder.SubShapeAll(f1, geom_builder.ShapeType["EDGE"])[:3])
edgesF2 = geom_builder.CreateGroup(f2, geom_builder.ShapeType["EDGE"])
geom_builder.UnionList( edgesF2, geom_builder.SubShapeAll(f2, geom_builder.ShapeType["EDGE"])[:3])
geom_builder.addToStudyInFather( box, edgesF1, "edgesF1" )
geom_builder.addToStudyInFather( box, edgesF2, "edgesF2" )

# Make the source mesh with prisms
src_mesh = smesh_builder.Mesh(box, "Source mesh")
src_mesh.Segment().NumberOfSegments(9,10)
src_mesh.Quadrangle()
src_mesh.Hexahedron()
src_mesh.Triangle(f1) # triangular sub-mesh
if not src_mesh.Compute(): raise Exception("Error when computing Mesh")

# Mesh the box using projection algorithms

# Define the same global 1D and 2D hypotheses
tgt_mesh = smesh_builder.Mesh(box, "Target mesh")
tgt_mesh.Segment().NumberOfSegments(9,10,UseExisting=True)
tgt_mesh.Quadrangle()

# Define Projection 1D algorithm to project 1d mesh elements from group edgesF2 to edgesF1
# It is actually not needed, just a demonstration
proj1D = tgt_mesh.Projection1D( edgesF1 )
# each vertex must be at the end of a connected group of edges (or a sole edge)
proj1D.SourceEdge( edgesF2, src_mesh, v2F1, v2F2 )

# Define 2D hypotheses to project triangles from f1 face of the source mesh to
# f2 face in the target mesh. Vertices specify how to associate sides of faces
proj2D = tgt_mesh.Projection2D( f2 )
proj2D.SourceFace( f1, src_mesh, v1F1, v1F2, v2F1, v2F2 )

# 2D hypotheses to project triangles from f2 of target mesh to the face opposite to f2.
# Association of face sides is default
proj2D = tgt_mesh.Projection2D( f2opp )
proj2D.SourceFace( f2 )

# 3D hypotheses to project prisms from the source to the target mesh
proj3D = tgt_mesh.Projection3D()
proj3D.SourceShape3D( box, src_mesh, v1F1, v1F2, v2F1, v2F2 )
if not tgt_mesh.Compute(): raise Exception("Error when computing Mesh")

# Move the source mesh to visually compare the two meshes
src_mesh.TranslateObject( src_mesh, smesh_builder.MakeDirStruct( 210, 0, 0 ), Copy=False)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/2c1db68831f15e3fd43424d9f547961e/defining_hypotheses_ex10.py)

### Projection 1D2D

```python
# Projection 1D2D
# Project triangles from one meshed face to another mesh on the same box

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# Prepare geometry

# Create a box
box = geom_builder.MakeBoxDXDYDZ(100, 100, 100)

# Get geom faces to mesh with triangles in the 1ts and 2nd meshes
faces = geom_builder.SubShapeAll(box, geom_builder.ShapeType["FACE"])
# 2 adjacent faces of the box
Face_1 = faces[2]
Face_2 = faces[0]

geom_builder.addToStudy( box, 'box' )
geom_builder.addToStudyInFather( box, Face_1, 'Face_1' )
geom_builder.addToStudyInFather( box, Face_2, 'Face_2' )

# Make the source mesh triangulated by default algorithm
src_mesh = smesh_builder.Mesh(Face_1, "Source mesh")
src_mesh.Segment().NumberOfSegments(15)
src_mesh.Triangle()
if not src_mesh.Compute(): raise Exception("Error when computing Mesh")

# Mesh the target mesh using the algorithm Projection1D2D
tgt_mesh = smesh_builder.Mesh(Face_2, "Target mesh")
tgt_mesh.Projection1D2D().SourceFace(Face_1,src_mesh)
if not tgt_mesh.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/0470e4bfb1bddee4e9171e5c07f12a5c/defining_hypotheses_ex11.py)

## 1D Mesh with Fixed Points example

```python
# 1D Mesh with Fixed Points example

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# Create face and explode it on edges
face = geom_builder.MakeFaceHW(100, 100, 1)
edges = geom_builder.SubShapeAllSorted(face, geom_builder.ShapeType["EDGE"])
geom_builder.addToStudy( face, "Face" )

# get the first edge from exploded result
edge1 = geom_builder.GetSubShapeID(face, edges[0])

# Define Mesh on previously created face
Mesh_1 = smesh_builder.Mesh(face)

# Create Fixed Point 1D hypothesis and define parameters.
# Note: values greater than 1.0 and less than 0.0 are not taken into account;
# duplicated values are removed. Also, if not specified explicitly, values 0.0 and 1.0
# add added automatically.
# The number of segments should correspond to the number of points (NbSeg = NbPnt-1);
# extra values of segments splitting parameter are not taken into account,
# while missing values are considered to be equal to 1.
Fixed_points_1D_1 = smesh_builder.CreateHypothesis('FixedPoints1D')
Fixed_points_1D_1.SetPoints( [ 1.1, 0.9, 0.5, 0.0, 0.5, -0.3 ] )
Fixed_points_1D_1.SetNbSegments( [ 3, 1, 2 ] )
Fixed_points_1D_1.SetReversedEdges( [edge1] )

# Add hypothesis to mesh and define 2D parameters
Mesh_1.AddHypothesis(Fixed_points_1D_1)
Regular_1D = Mesh_1.Segment()
Quadrangle_2D = Mesh_1.Quadrangle()
# Compute mesh
if not Mesh_1.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/4bd00e57e23729794e5975425f20e7df/defining_hypotheses_ex12.py)

## Radial Quadrangle 1D-2D example

```python
# Radial Quadrangle 1D-2D example

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# Create face from the wire and add to study
Face = geom_builder.MakeSketcher("Sketcher:F 0 0:TT 20 0:R 90:C 20 90:WF", [0, 0, 0, 1, 0, 0, 0, 0, 1])
geom_builder.addToStudy(Face,"Face")
circle, radius1, radius2 = geom_builder.SubShapeAllSorted(Face, geom_builder.ShapeType["EDGE"])
geom_builder.addToStudyInFather(Face, radius1,"radius1")
geom_builder.addToStudyInFather(Face, radius2,"radius2")
geom_builder.addToStudyInFather(Face, circle,"circle")

# Define geometry for mesh, and Radial Quadrange algorithm
mesh = smesh_builder.Mesh(Face)
radial_Quad_algo = mesh.Quadrangle(algo=smeshBuilder.RADIAL_QUAD)

# The Radial Quadrange algorithm can work without any hypothesis
# In this case it uses "Default Nb of Segments" preferences parameter to discretize edges
# So by default there will be 15 segments in both radial and circular directions
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# The Radial Quadrange uses global or local 1d hypotheses if it does
# not have its own hypotheses.
# Define global hypotheses to discretize radial edges and a local one for circular edge
# So that there will be 5 radial layers and 10 circular segments
global_Nb_Segments = mesh.Segment().NumberOfSegments(5)
local_Nb_Segments  = mesh.Segment(circle).NumberOfSegments(10)
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# Define own parameters of Radial Quadrange algorithm
# The number of radial layers will be 4
radial_Quad_algo.NumberOfLayers( 4 )
if not mesh.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/50362ae73574e05e3f29dd064f453de5/defining_hypotheses_ex13.py)

## Quadrangle Parameters example 1 (meshing a face with 3 edges)

```python
# Quadrangle Parameters example 1 (meshing a face with 3 edges)

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# Get 1/4 part from the disk face.
Box_1 = geom_builder.MakeBoxDXDYDZ(100, 100, 100)
Disk_1 = geom_builder.MakeDiskR(100, 1)
Common_1 = geom_builder.MakeCommon(Disk_1, Box_1)
triaVertex = geom_builder.GetVertexNearPoint( Common_1, geom_builder.MakeVertex(0,0,0) )
geom_builder.addToStudy( Common_1, "Common_1" )
geom_builder.addToStudyInFather( Common_1, triaVertex, "triaVertex" )

# Set the Geometry for meshing
Mesh_1 = smesh_builder.Mesh(Common_1)

# Define 1D hypothesis
Regular_1D = Mesh_1.Segment()
Nb_Segments_1 = Regular_1D.NumberOfSegments(10)

# Create Quadrangle parameters and define the Base Vertex.
Quadrangle_2D = Mesh_1.Quadrangle().TriangleVertex( triaVertex )

# Compute the mesh
if not Mesh_1.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/e8d5f373752aecbe62216d2b40638310/defining_hypotheses_ex14.py)

## Quadrangle Parameters example 2 (using different types)

```python
# Quadrangle Parameters example 2 (using different types)

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# Make quadrangle face and explode it on edges.
Vertex_1 = geom_builder.MakeVertex(0, 0, 0)
Vertex_2 = geom_builder.MakeVertex(40, 0, 0)
Vertex_3 = geom_builder.MakeVertex(40, 30, 0)
Vertex_4 = geom_builder.MakeVertex(0, 30, 0)
Quadrangle_Face_1 = geom_builder.MakeQuad4Vertices(Vertex_1, Vertex_4, Vertex_3, Vertex_2)
[Edge_1,Edge_2,Edge_3,Edge_4] = geom_builder.SubShapeAllSorted(Quadrangle_Face_1, geom_builder.ShapeType["EDGE"])
geom_builder.addToStudy( Quadrangle_Face_1, "Quadrangle Face_1" )
geom_builder.addToStudyInFather( Quadrangle_Face_1, Edge_2, "Edge_2" )

# Set the Geometry for meshing
Mesh_1 = smesh_builder.Mesh(Quadrangle_Face_1)

# Create Quadrangle parameters and
# define the Type as Quadrangle Preference
Quad_algo = Mesh_1.Quadrangle()
Quadrangle_Parameters_1 = Quad_algo.QuadrangleParameters( smeshBuilder.QUAD_QUADRANGLE_PREF )

# Define other hypotheses and algorithms
Regular_1D = Mesh_1.Segment()
Nb_Segments_1 = Regular_1D.NumberOfSegments(4)

# Define submesh on one edge to provide different number of segments
Regular_1D_1 = Mesh_1.Segment(geom=Edge_2)
Nb_Segments_2 = Regular_1D_1.NumberOfSegments(10)

# Compute mesh (with Quadrangle Preference type)
if not Mesh_1.Compute(): raise Exception("Error when computing Mesh")

# Change type to Reduced and compute again
Quadrangle_Parameters_1.SetQuadType( smeshBuilder.QUAD_REDUCED )
if not Mesh_1.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/e71b2308058b64f8753811686a57f9a1/defining_hypotheses_ex15.py)

## “Import 1D-2D Elements from Another Mesh” example

```python
# "Import 2D Elements from Another Mesh" example

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# Make a patritioned box

box = geom_builder.MakeBoxDXDYDZ(100,100,100)

N = geom_builder.MakeVectorDXDYDZ( 1,0,0 )
O = geom_builder.MakeVertex( 50,0,0 )
plane = geom_builder.MakePlane( O, N, 200 ) # plane YOZ

shape2boxes = geom_builder.MakeHalfPartition( box, plane )
boxes = geom_builder.SubShapeAllSorted(shape2boxes, geom_builder.ShapeType["SOLID"])

geom_builder.addToStudy( boxes[0], "boxes[0]")
geom_builder.addToStudy( boxes[1], "boxes[1]")
midFace0 = geom_builder.SubShapeAllSorted(boxes[0], geom_builder.ShapeType["FACE"])[5]
geom_builder.addToStudyInFather( boxes[0], midFace0, "middle Face")
midFace1 = geom_builder.SubShapeAllSorted(boxes[1], geom_builder.ShapeType["FACE"])[0]
geom_builder.addToStudyInFather( boxes[1], midFace1, "middle Face")

# Mesh one of boxes with quadrangles. It is a source mesh

srcMesh = smesh_builder.Mesh(boxes[0], "source mesh") # box coloser to CS origin
nSeg1 = srcMesh.Segment().NumberOfSegments(4)
srcMesh.Quadrangle()
if not srcMesh.Compute(): raise Exception("Error when computing Mesh")
srcFaceGroup = srcMesh.GroupOnGeom( midFace0, "src faces", SMESH.FACE )

# Import faces from midFace0 to the target mesh

tgtMesh = smesh_builder.Mesh(boxes[1], "target mesh")
importAlgo = tgtMesh.UseExisting2DElements(midFace1)
import2hyp = importAlgo.SourceFaces( [srcFaceGroup] )
tgtMesh.Segment().NumberOfSegments(3)
tgtMesh.Quadrangle()
if not tgtMesh.Compute(): raise Exception("Error when computing Mesh")

# Import the whole source mesh with groups
import2hyp.SetCopySourceMesh(True,True)
if not tgtMesh.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/43ae3c71193cad31f1f3f13759b922ba/defining_hypotheses_ex16.py)

## Viscous layers construction

```python
# Viscous layers construction

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

X = geom_builder.MakeVectorDXDYDZ( 1,0,0 )
O = geom_builder.MakeVertex( 100,50,50 )
plane = geom_builder.MakePlane( O, X, 200 ) # plane YZ

box = geom_builder.MakeBoxDXDYDZ(200,100,100)

shape = geom_builder.MakeHalfPartition( box, plane )

faces = geom_builder.SubShapeAllSorted(shape, geom_builder.ShapeType["FACE"])
face1 = faces[1]
ignoreFaces = [ faces[0], faces[-1]]

geom_builder.addToStudy( shape, "shape" )
geom_builder.addToStudyInFather( shape, face1, "face1")

# 3D Viscous layers

mesh = smesh_builder.Mesh(shape, "CFD")

mesh.Segment().NumberOfSegments( 4 )

mesh.Triangle()
mesh.Quadrangle(face1)
algo3D = mesh.Tetrahedron()

thickness = 20
numberOfLayers = 10
stretchFactor = 1.5
groupName = "Boundary layers"
layersHyp = algo3D.ViscousLayers(thickness,numberOfLayers,stretchFactor,
                                 ignoreFaces,           # optional
                                 groupName = groupName) # optional

if not mesh.Compute(): raise Exception("Error when computing Mesh")

# retrieve boundary prisms created by mesh.Compute()
boundaryGroup = mesh.GetGroupByName( layersHyp.GetGroupName() )[0]
print( "Nb boundary prisms", boundaryGroup.Size() )

mesh.MakeGroup("Tetras",SMESH.VOLUME,SMESH.FT_ElemGeomType,"=",SMESH.Geom_TETRA)
mesh.MakeGroup("Pyras",SMESH.VOLUME,SMESH.FT_ElemGeomType,"=",SMESH.Geom_PYRAMID)
mesh.MakeGroup("Prims",SMESH.VOLUME,SMESH.FT_ElemGeomType,"=",SMESH.Geom_PENTA)

# 2D Viscous layers

# 3 edges of the 4 edges of face1
edgeIds = geom_builder.SubShapeAllIDs( face1, geom_builder.ShapeType["EDGE"])[:-1]

mesh = smesh_builder.Mesh(face1,"VicsousLayers2D")
mesh.Segment().NumberOfSegments( 5 )

# viscous layers will be created on 1 edge, as we set 3 edges to ignore
vlHyp = mesh.Triangle().ViscousLayers2D( 2, 3, 1.5,
                                         edgeIds, isEdgesToIgnore=True, # optional
                                         groupName=groupName)           # optional
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# retrieve boundary elements created by mesh.Compute()
quadrangles = mesh.GetGroupByName( vlHyp.GetGroupName() )[0]
print( "Nb boundary quadrangles", quadrangles.Size() )

# viscous layers will be created on 3 edges, as we pass isEdgesToIgnore=False
vlHyp.SetEdges( edgeIds, False )

if not mesh.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/bfe0e9e376ef698e778ce2942b4a189d/defining_hypotheses_ex17.py)

## Viscous layers API construction

```python
# Viscous layers construction

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

X = geom_builder.MakeVectorDXDYDZ( 1,0,0 )
O = geom_builder.MakeVertex( 100,50,50 )
plane = geom_builder.MakePlane( O, X, 200 ) # plane YZ

box = geom_builder.MakeBoxDXDYDZ(200,100,100)

shape = geom_builder.MakeHalfPartition( box, plane )

faces = geom_builder.SubShapeAllSorted(shape, geom_builder.ShapeType["FACE"])
face1 = faces[1]
# 4 left, 34 middle, 50 right
# Have to pass the middle face id, otherwise it is going to create two disjoint boxes
# because the common face is not going to be ignored and both boxes are going to shrink
# in this direction too
ignoreFaces = [4,34,50]

geom_builder.addToStudy( shape, "shape" )
geom_builder.addToStudyInFather( shape, face1, "face1")

# 3D Viscous layers
mesh = smesh_builder.Mesh(shape, "CFD")

ViscousBuilder = mesh.ViscousLayerBuilder()
thickness = 20	
numberOfLayers = 10
stretchFactor = 1.5
groupName = "Boundary layers"
ViscousBuilder.setBuilderParameters( thickness, numberOfLayers, stretchFactor, 
                                                ignoreFaces,                # optional
                                                groupName = groupName )     # optional

Shrinkshape = ViscousBuilder.GetShrinkGeometry()

shrinkMesh = smesh_builder.Mesh(Shrinkshape, "Shrink")
shrinkMesh.Segment().NumberOfSegments( 4 )
faces = geom_builder.SubShapeAllSorted(Shrinkshape, geom_builder.ShapeType["FACE"])
shrinkFace1 = faces[1]

shrinkMesh.Triangle()
shrinkMesh.Quadrangle(shrinkFace1)
algo3D = shrinkMesh.Tetrahedron()

if not shrinkMesh.Compute(): raise Exception("Error when computing Mesh")

#Add viscous layer
FinalMesh = ViscousBuilder.AddLayers( shrinkMesh )

mesh.MakeGroup("Tetras",SMESH.VOLUME,SMESH.FT_ElemGeomType,"=",SMESH.Geom_TETRA)
mesh.MakeGroup("Pyras",SMESH.VOLUME,SMESH.FT_ElemGeomType,"=",SMESH.Geom_PYRAMID)
mesh.MakeGroup("Prims",SMESH.VOLUME,SMESH.FT_ElemGeomType,"=",SMESH.Geom_PENTA)

# 2D Viscous layers

# 3 edges of the 4 edges of face1
edgeIds = geom_builder.SubShapeAllIDs( face1, geom_builder.ShapeType["EDGE"])[:-1]

mesh = smesh_builder.Mesh(face1,"Face1")
ViscousBuilder = mesh.ViscousLayerBuilder()
ViscousBuilder.setBuilderParameters( 2, 3, 1.5, 
                                    edgeIds, True, # optional
                                    groupName = groupName )     # optional

#For 2D, edges are not selectable (to be developed in occt) the entire face is shrink
shrinkFace = ViscousBuilder.GetShrinkGeometry()
shrinkMesh = smesh_builder.Mesh(shrinkFace, "VicsousLayers2D")

shrinkMesh.Segment().NumberOfSegments( 5 )
algo2D = shrinkMesh.Triangle()

if not shrinkMesh.Compute(): raise Exception("Error when computing Mesh of shrink face")

FinalMeshFace = ViscousBuilder.AddLayers( shrinkMesh )
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/1e22546e0917b3f1962a9b16c5c99d21/defining_hypotheses_vlapi_ex17.py)

## Radial Prism example

```python
# Usage of Radial Prism 3D meshing algorithm

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# Create geometry: hollow sphere

sphere_1 = geom_builder.MakeSphereR( 100 )
sphere_2 = geom_builder.MakeSphereR( 50 )

hollow_sphere = geom_builder.MakeCut( sphere_1, sphere_2, theName="hollow sphere")

faces = geom_builder.ExtractShapes( hollow_sphere, geom_builder.ShapeType["FACE"] )

# Create mesh 

mesh = smesh_builder.Mesh( hollow_sphere, "Mesh of hollow sphere" )

# assign Global Radial Prism algorithm
prism_algo = mesh.Prism()

# define projection between the inner and outer spheres
mesh.Triangle( smeshBuilder.NETGEN_1D2D, faces[0] )    # NETGEN on faces[0]
mesh.Projection1D2D( faces[1] ).SourceFace( faces[0] ) # projection faces[0] -> faces[1]

# define distribution of layers using Number of Segments hypothesis in logarithmic mode
prism_algo.NumberOfSegments( 4, 5. )

# compute the mesh
if not mesh.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/971f5dbc12205326e5e37ac002a22b18/radial_prism_3d_algo.py)

## Usage of Body Fitting algorithm

```python
# Usage of Body Fitting algorithm

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a sphere
sphere = geom_builder.MakeSphereR( 50 )

# cut the sphere by a box
box = geom_builder.MakeBoxDXDYDZ( 100, 100, 100 )
partition = geom_builder.MakePartition([ sphere ], [ box ], theName="partition")

# create a mesh and assign a "Body Fitting" algo
mesh = smesh_builder.Mesh( partition )
cartAlgo = mesh.BodyFitted()

# define a cartesian grid using Coordinates
coords = list(range(-100,100,10))
cartHyp = cartAlgo.SetGrid( coords,coords,coords, 1000000)

# compute the mesh
if not mesh.Compute(): raise Exception("Error when computing Mesh")
print("nb hexahedra",mesh.NbHexas())
print("nb tetrahedra",mesh.NbTetras())
print("nb polyhedra",mesh.NbPolyhedrons())
print()

# define the grid by setting constant spacing
cartHyp = cartAlgo.SetGrid( "10","10","10", 1000000)

if not mesh.Compute(): raise Exception("Error when computing Mesh")
print("nb hexahedra",mesh.NbHexas())
print("nb tetrahedra",mesh.NbTetras())
print("nb polyhedra",mesh.NbPolyhedrons())
print("nb faces",mesh.NbFaces())
print()

# activate creation of faces
cartHyp.SetToCreateFaces( True )

if not mesh.Compute(): raise Exception("Error when computing Mesh")
print("nb hexahedra",mesh.NbHexas())
print("nb tetrahedra",mesh.NbTetras())
print("nb polyhedra",mesh.NbPolyhedrons())
print("nb faces",mesh.NbFaces())
print()

# enable consideration of shared faces
cartHyp.SetToConsiderInternalFaces( True )
if not mesh.Compute(): raise Exception("Error when computing Mesh")
print("nb hexahedra",mesh.NbHexas())
print("nb tetrahedra",mesh.NbTetras())
print("nb polyhedra",mesh.NbPolyhedrons())
print("nb faces",mesh.NbFaces())
print()

# define the grid by setting different spacing in 2 sub-ranges of geometry
spaceFuns = ["5","10+10*t"]
cartAlgo.SetGrid( [spaceFuns, [0.5]], [spaceFuns, [0.5]], [spaceFuns, [0.25]], 10 )

if not mesh.Compute(): raise Exception("Error when computing Mesh")
print("nb hexahedra",mesh.NbHexas())
print("nb tetrahedra",mesh.NbTetras())
print("nb polyhedra",mesh.NbPolyhedrons())
print()

# Example of customization of dirtections of the grid axes

# make a box with non-orthogonal edges
xDir = geom_builder.MakeVectorDXDYDZ( 1.0, 0.1, 0.0, "xDir" )
yDir = geom_builder.MakeVectorDXDYDZ(-0.1, 1.0, 0.0, "yDir"  )
zDir = geom_builder.MakeVectorDXDYDZ( 0.2, 0.3, 1.0, "zDir"  )
face = geom_builder.MakePrismVecH( xDir, yDir, 1.0 )
box  = geom_builder.MakePrismVecH( face, zDir, 1.0, theName="box" )

spc = "0.1" # spacing

# default axes
mesh = smesh_builder.Mesh( box, "custom axes")
algo = mesh.BodyFitted()
algo.SetGrid( spc, spc, spc, 10000 )
if not mesh.Compute(): raise Exception("Error when computing Mesh")
print("Default axes")
print("   nb hex:",mesh.NbHexas())

# set axes using edges of the box
algo.SetAxesDirs( xDir, [-0.1,1,0], zDir )
if not mesh.Compute(): raise Exception("Error when computing Mesh")
print("Manual axes")
print("   nb hex:",mesh.NbHexas())

# set optimal orthogonal axes
algo.SetOptimalAxesDirs( isOrthogonal=True )
if not mesh.Compute(): raise Exception("Error when computing Mesh")
print("Optimal orthogonal axes")
print("   nb hex:",mesh.NbHexas())

# set optimal non-orthogonal axes
algo.SetOptimalAxesDirs( isOrthogonal=False )
if not mesh.Compute(): raise Exception("Error when computing Mesh")
print("Optimal non-orthogonal axes")
print("   nb hex:",mesh.NbHexas())
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/9483c88cfd907598a06f28e5f7dab5ef/cartesian_algo.py)

## Usage of “Use Faces to be Created Manually” algorithm

This sample demonstrates how to use **Use Faces to be Created Manually** algorithm,
which is actually just a stub allowing to use your own 2D algorithm
implemented in Python.

```python
# Usage of "Use Faces to be Created Manually" algorithm

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# define my 2D algorithm
def my2DMeshing(geomFace, mesh):
    import numpy as np

    # find gravity center of geomFace
    gcXYZ = geom_builder.PointCoordinates( geom_builder.MakeCDG( geomFace ))

    # define order and orientation of edges
    sortedEdges = []
    geomEdges = geom_builder.SubShapeAll( geomFace, geom_builder.ShapeType["EDGE"])
    sortedEdges.append(( geomEdges.pop(0), True ))
    while geomEdges:
        prevEdge_rev = sortedEdges[ -1 ]
        prevVV = geom_builder.SubShapeAll( prevEdge_rev[0], geom_builder.ShapeType["VERTEX"])
        prevV2 = prevVV[ prevEdge_rev[1] ]
        found = False
        for iE in range( len( geomEdges )):
            v1,v2 = geom_builder.SubShapeAll( geomEdges[ iE ], geom_builder.ShapeType["VERTEX"])
            same1,same2 = [( geom_builder.MinDistance( prevV2, v ) < 1e-7 ) for v in [v1,v2] ]
            if not same1 and not same2: continue
            sortedEdges.append(( geomEdges.pop( iE ), same1 ))
            found = True
            break
        assert found
    sortedEdges.reverse()

    # put nodes on edges in a right order
    nodes = []
    for edge, isForward in sortedEdges:
        v1,v2 = geom_builder.SubShapeAll( edge, geom_builder.ShapeType["VERTEX"])
        edgeNodes = mesh.GetSubMeshNodesId( v2,   all=False ) + \
                    mesh.GetSubMeshNodesId( edge, all=False ) + \
                    mesh.GetSubMeshNodesId( v1,   all=False )
        if not isForward: edgeNodes.reverse()
        nodes.extend( edgeNodes[:-1] )

    # create nodes inside the geomFace
    r1 = 0.6
    r2 = 1 - r1
    nodesInside = []
    for n in nodes:
        nXYZ = mesh.GetNodeXYZ( n )
        newXYZ = np.add( np.multiply( r1, gcXYZ ), np.multiply( r2, nXYZ ))
        nodesInside.append( mesh.AddNode( newXYZ[0], newXYZ[1], newXYZ[2] ))
        mesh.SetNodeOnFace( nodesInside[-1], geomFace, 0, 0 )

    # find out orientation of faces to create
    #    geomFace normal
    faceNorm = geom_builder.GetNormal( geomFace )
    v1,v2 = [ geom_builder.PointCoordinates( v ) \
              for v in geom_builder.SubShapeAll( faceNorm, geom_builder.ShapeType["VERTEX"]) ]
    faceNormXYZ = np.subtract( v2, v1 )
    outDirXYZ   = np.subtract( v1, [ 50, 50, 50 ] )
    if np.dot( faceNormXYZ, outDirXYZ ) < 0: # reversed face
        faceNormXYZ = np.multiply( -1., faceNormXYZ )
    #   mesh face normal
    e1 = np.subtract( mesh.GetNodeXYZ( nodes[0] ), mesh.GetNodeXYZ( nodes[1] ))
    e2 = np.subtract( mesh.GetNodeXYZ( nodes[0] ), mesh.GetNodeXYZ( nodesInside[0] ))
    meshNorm = np.cross( e1, e2 )
    #   faces orientation
    reverse = ( np.dot( faceNormXYZ, meshNorm ) < 0 )

    # create mesh faces
    iN = len( nodes )
    while iN:
        n1, n2, n3, n4 = nodes[iN-1], nodes[iN-2], nodesInside[iN-2], nodesInside[iN-1]
        iN -= 1
        if reverse:
            f = mesh.AddFace( [n1, n2, n3, n4] )
        else:
            f = mesh.AddFace( [n4, n3, n2, n1] )
        # new faces must be assigned to geometry to allow 3D algorithm finding them
        mesh.SetMeshElementOnShape( f, geomFace )

    if reverse:
        nodesInside.reverse()
    polygon = mesh.AddPolygonalFace( nodesInside )
    mesh.SetMeshElementOnShape( polygon, geomFace )

    return

# create geometry and get faces to mesh with my2DMeshing()
box = geom_builder.MakeBoxDXDYDZ( 100, 100, 100 )
f1 = geom_builder.SubShapeAll( box, geom_builder.ShapeType["FACE"])[0]
f2 = geom_builder.GetOppositeFace( box, f1 )
geom_builder.addToStudy( box, "box" )
geom_builder.addToStudy( f1, "f1" )
geom_builder.addToStudy( f2, "f2" )

# compute 1D mesh
mesh = smesh_builder.Mesh( box )
mesh.Segment().NumberOfSegments( 5 )
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# compute 2D mesh
mesh.Quadrangle()
mesh.UseExistingFaces(f1) # UseExistingFaces() allows using my2DMeshing();
mesh.UseExistingFaces(f2) # assign UseExistingFaces() BEFORE calling my2DMeshing()!
my2DMeshing(f1, mesh)
my2DMeshing(f2, mesh)
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# compute 3D mesh
mesh.Prism()
if not mesh.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/1f6d3ef027427f511b43ad9856291ec9/use_existing_faces.py)

Resulting mesh:

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/use_existing_face_sample_mesh.png)

## Usage of Extrusion 3D meshing algorithm

```python
# Usage of Extrusion 3D meshing algorithm

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

OX = geom_builder.MakeVectorDXDYDZ(1,0,0)
OY = geom_builder.MakeVectorDXDYDZ(0,1,0)
OZ = geom_builder.MakeVectorDXDYDZ(0,0,1)

#  Y ^       Make geometry of a "pipe" with the following base (cross section).
#    |       Big central quadrangles will be meshed with triangles, walls
#                         of the pipe will be meshed with quadrilaterals
#   +--+--+--+--+--+--+
#   |  |  |  |  |  |  |
#   +--+--+--+--+--+--+
#   |  |     |     |  |
#   +--+     |     +--+
#   |  |     |     |  |
#   +--+-----+-----+--+
#   |  |     |     |  |
#   +--+     |     +--+
#   |  |     |     |  |
#   +--+--+--+--+--+--+
#   |  |  |  |  |  |  |  -->
#   +--+--+--+--+--+--+   X

quadBig   = geom_builder.MakeFaceHW( 20,20, 1 )
quadBig   = geom_builder.MakeTranslation( quadBig, 15,15,0 )
quadSmall = geom_builder.MakeFaceHW( 10,10, 1 )
smallQuads1 = geom_builder.MakeMultiTranslation1D( quadSmall, OX, 10, 3 )
smallQuads2 = geom_builder.MakeMultiTranslation1D( quadSmall, OY, 10, 3 )
smallQuads2 = geom_builder.SubShapeAllSortedCentres( smallQuads2, geom_builder.ShapeType["FACE"])[1:]

base = geom_builder.MakeCompound( smallQuads2 + [smallQuads1, quadBig])
axis = geom_builder.MakeLine( geom_builder.MakeVertex( 25,25,0), OZ )
base = geom_builder.MultiRotate1DNbTimes( base, axis, 4)
base = geom_builder.MakePartition( [base], theName="base")
path = geom_builder.MakeSketcher("Sketcher:F 0 0:TT 0 100:R 0:C -90 180:T 0 -150",[0,0,0, 0,-1,0, 1,0,0])

# Make the pipe, each quadrangle of the base turns into a prism with composite wall faces
pipe   = geom_builder.MakePipe( base, path )
prisms = geom_builder.MakePartition( [pipe], theName="prisms")

# get base faces of the prism to define sub-mesh on them
smallQuad = geom_builder.GetFaceNearPoint( prisms, geom_builder.MakeVertex( 0,0,0 ), "smallQuad")
bigQuad   = geom_builder.GetFaceNearPoint( prisms, geom_builder.MakeVertex( 15,15,0 ), "bigQuad")

mesh = smesh_builder.Mesh( prisms )

# assign Global hypotheses

# 1D algorithm and hypothesis for division along the pipe
mesh.Segment().NumberOfSegments(15)

# Extrusion 3D algo
mesh.Prism()

# assign Local hypotheses

# 1D and 2D algos and hyps to mesh smallQuad with quadrilaterals
mesh.Segment(smallQuad).LocalLength( 3 )
mesh.Quadrangle(smallQuad)

# 1D and 2D algos and hyps to mesh bigQuad with triangles
mesh.Segment(bigQuad).LocalLength( 3 )
mesh.Triangle(bigQuad)

# compute the mesh
if not mesh.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/8a02a84d0fc1e279dde7a6b67ef8cec9/prism_3d_algo.py)

The result geometry and mesh is shown below

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/prism_tui_sample.png)

## Usage of Medial Axis Projection algorithm

```python
# Usage of Medial Axis Projection algorithm

# for meshing a ring face with quadrangles

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a ring face
circleEdge1 = geom_builder.MakeCircleR( 3 )
circleEdge2 = geom_builder.MakeCircleR( 7 )
ring = geom_builder.MakeFaceWires( [ circleEdge1, circleEdge2 ], True, theName='Ring' )
circleLen1  = geom_builder.BasicProperties( circleEdge1 )[0]
circleLen2  = geom_builder.BasicProperties( circleEdge2 )[0]

# make a mesh

mesh = smesh_builder.Mesh( ring )

circNbSeg = 60
algo1d = mesh.Segment()
algo1d.NumberOfSegments( circNbSeg ) # division of circle edges

algo2d = mesh.Quadrangle( smeshBuilder.QUAD_MA_PROJ )
algo2d.StartEndLength( circleLen2 / circNbSeg, circleLen1 / circNbSeg ) # radial division

if not mesh.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/5fd8cb9cb324afa907e370939ee9b3ea/quad_medial_axis_algo.py)

## Usage of Segments around Vertex algorithm

```python
# Usage of Segments around Vertex algorithm

# for meshing a box with quadrangles with refinement near vertices

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a box
box = geom_builder.MakeBoxDXDYDZ( 10, 10, 10 )

# make a mesh
mesh = smesh_builder.Mesh( box )

# define quadrangle meshing
algo1d = mesh.Segment()
algo1d.LocalLength( 1. )
mesh.Quadrangle()

# add Hexahedron algo to assure that there are no triangles
mesh.Hexahedron()

# define refinement near vertices
algo1d.LengthNearVertex( 0.2 )

if not mesh.Compute(): raise Exception("Error when computing Mesh")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/60fb0f987eafa1ef015a417e3a98853f/defining_hypotheses_len_near_vertex.py)
