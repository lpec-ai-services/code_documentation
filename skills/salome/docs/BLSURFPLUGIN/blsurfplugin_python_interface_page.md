<!-- source: https://docs.salome-platform.org/latest/gui/BLSURFPLUGIN/blsurfplugin_python_interface_page.html -->

# Python Interface

Note
:   The former name of MG-CADSurf mesher is *BLSURF* and names of the corresponding classes and modules still include *"BLSURF"*.

Python package [BLSURFPluginBuilder](../BLSURFPLUGIN/blsurfpluginpy_doc/namespaceBLSURFPluginBuilder.md) defines [BLSURFPluginBuilder.BLSURF_Algorithm](../BLSURFPLUGIN/blsurfpluginpy_doc/classBLSURFPluginBuilder_1_1BLSURF__Algorithm.md) class providing access to the MG-CADSurf meshing algorithm and its parameters.

You can get an instance of this class by calling [smeshBuilder.Mesh.Triangle](../BLSURFPLUGIN/blsurfpluginpy_doc/classsmeshBuilder_1_1Mesh.md#a58d92bcd67822a8ea2a782177e9a41a4)(algo=smeshBuilder.MG_CADSurf) or [smeshBuilder.Mesh.Triangle](../BLSURFPLUGIN/blsurfpluginpy_doc/classsmeshBuilder_1_1Mesh.md#a58d92bcd67822a8ea2a782177e9a41a4)(algo=smeshBuilder.BLSURF). This call creates an algorithm (if not yet exist), assigns it to the mesh and returns an instance of [BLSURFPluginBuilder.BLSURF_Algorithm](../BLSURFPLUGIN/blsurfpluginpy_doc/classBLSURFPluginBuilder_1_1BLSURF__Algorithm.md) to the caller.

The class of algorithm has methods to set up meshing parameters.

Below you can see examples of usage of this class for 2D mesh generation.

## Example of mesh generation with MG-CADSurf algorithm

```python
# -------------------------------------------------
# blsurf_construct_mesh_basic_hypo Basic hypothesis
# -------------------------------------------------

import salome
salome.salome_init()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

import SMESH, SALOMEDS
from salome.smesh import smeshBuilder
smesh =  smeshBuilder.New()

# create a box
box = geompy.MakeBoxDXDYDZ(200., 200., 200.)
geompy.addToStudy(box, "box")

# get sub-shapes
Face_1   = geompy.SubShapeAllSorted(box, geompy.ShapeType["FACE"])[0]
Edge_1   = geompy.SubShapeAllSorted(box, geompy.ShapeType["EDGE"])[0]
Vertex_1 = geompy.SubShapeAllSorted(box, geompy.ShapeType["VERTEX"])[0]

Face_2   = geompy.SubShapeAllSorted(box,    geompy.ShapeType["FACE"])[5]
Wire_1   = geompy.SubShapeAllSorted(Face_2, geompy.ShapeType["WIRE"])[0]

# Geom object with sizemaps can be unpublished in study.
# They will then be automatically published.
geompy.addToStudyInFather(box,Face_1, "Face_1")
geompy.addToStudyInFather(box,Edge_1, "Edge_1")
geompy.addToStudyInFather(box,Vertex_1, "Vertex_1")

geompy.addToStudyInFather(box   ,Face_2, "Face_2")
geompy.addToStudyInFather(Face_2,Wire_1, "Wire_1")

# create a mesh on the box
cadsurfMesh = smesh.Mesh(box,"box: MG-CADSurf mesh")

# create a BLSurf algorithm for faces
algo2d = cadsurfMesh.Triangle(algo=smeshBuilder.MG_CADSurf)

# ----------------------------------------------
# blsurf_construct_mesh_sizemaps Adding sizemaps
# ----------------------------------------------

# optional - set physical mesh to 2 = Size Map
algo2d.SetPhysicalMesh( 2 )

# optional - set global mesh size
algo2d.SetPhySize( 34.641 )

# set size on Face_1
algo2d.SetSizeMap(Face_1, 'def f(u,v): return 10' )
# set size on Edge_1
algo2d.SetSizeMap(Edge_1, 'def f(t): return 5' )
# set size on Vertex_1
algo2d.SetSizeMap(Vertex_1, 'def f(): return 2' )

# compute the mesh
cadsurfMesh.Compute()

# ----------------------------------------------------------------
# blsurf_construct_mesh_enforced_vertices Adding enforced vertices
# ----------------------------------------------------------------

# Add enforced vertex for Face_1 on (50, 50, 50)
# The projection coordinates will be (50, 50, 0)
algo2d.SetEnforcedVertex(Face_1, 50, 50, 50)

# Add another enforced vertex on (150, 150, 150)
algo2d.SetEnforcedVertex(Face_1, 150, 150, 150)

# Retrieve and print the list of enforced vertices defines on Face_1
enfList = algo2d.GetEnforcedVertices(Face_1)
print("List of enforced vertices for Face_1: ")
print(enfList)

# compute the mesh
cadsurfMesh.Compute()

# Remove an enforced vertex and print the list
algo2d.UnsetEnforcedVertex(Face_1, 50, 50, 50)
enfList = algo2d.GetEnforcedVertices(Face_1)
print("List of enforced vertices for Face_1: ")
print(enfList)

# compute the mesh
cadsurfMesh.Compute()

# Remove all enforced vertices defined on Face_1
algo2d.UnsetEnforcedVertices(Face_1)

# compute the mesh
cadsurfMesh.Compute()

# ---------------------------------------------------
# blsurf_construct_mesh_attractor Adding an attractor
# ---------------------------------------------------

# Add an attractor on Face_2, which shape is Wire_1

# The size on Wire_1 is 1 and will grow until a maximum of 36.641 (physical size set above) 
# The influence distance of the attractor is 20
# The size is kept constant until a distance of 10
algo2d.SetAttractorGeom(Face_2, Wire_1, 1, 36.641, 20, 10)

# In order to let the attractor control the growing of the mesh let set
# the gradation to its maximum
algo2d.SetGradation( 2.5 )

# -----------------------
# Adding enforced meshes
# -----------------------

# create 1D mesh
OZ       = geompy.MakeVectorDXDYDZ(0, 0, 1)
circle_1 = geompy.MakeCircle( geompy.MakeVertex( 100, 75,  200 ), OZ, 50 )
circle_2 = geompy.MakeCircle( geompy.MakeVertex( 100, 150, 200 ), OZ, 70 )
circles  = geompy.MakeCompound([ circle_1, circle_2 ], theName="circles")
mesh_1D  = smesh.Mesh( circles, "enforced circles" )
mesh_1D.Segment().LocalLength( 7 )
mesh_1D.Compute()

# Add enforced mesh
algo2d.SetEnforcedMeshes([
    smeshBuilder.MG_EnforcedMesh1D( mesh_1D, "Enforced edges")])

# -----------------
# compute the mesh
# -----------------

cadsurfMesh.Compute()

# ================================================================
# blsurf_construct_mesh_internal_vertices Using internal vertices
# ================================================================

# Creating a geometry containing internal vertices
Face_3 = geompy.MakeFaceHW(1, 1, 1)
Vertex_2 = geompy.MakeVertex(0.2, 0.2, 0)
Partition_1 = geompy.MakePartition([Face_3, Vertex_2], [], [], [], geompy.ShapeType["FACE"], 0, [], 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
Multi_Translation_1 = geompy.MakeMultiTranslation2D(Partition_1, OX, 1, 10, OY, 1, 10)
Multi_Translation_glued = geompy.MakeGlueEdges(Multi_Translation_1, 1e-7)
geompy.addToStudy( Face_3, 'Face_3' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( Multi_Translation_1, 'Multi_Translation_1' )
geompy.addToStudy( Multi_Translation_glued, 'Multi_Translation_glued' )

# The mesh on the geometry with internal vertices
cadsurfMesh_internal = smesh.Mesh(Multi_Translation_glued, "cadsurfMesh_internal")
algo2d = cadsurfMesh_internal.Triangle(algo=smeshBuilder.MG_CADSurf)
algo2d.SetPhySize( 0.1 )

# Allow MG-CADSURF to take into account internal vertices
algo2d.SetInternalEnforcedVertexAllFaces( True )

# Add the created nodes into a group
algo2d.SetInternalEnforcedVertexAllFacesGroup( "my group" )

# compute the mesh
cadsurfMesh_internal.Compute()

# End of script
```

[Download this script](https://docs.salome-platform.org/latest/examples/BLSURFPLUGIN/blsurfdemo.py)

## Example of periodicity definition with preCAD

```python
# -*- coding: utf-8 -*-

import salome
import math

import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

simple = False

r = 10
dist = 10

p1 = geompy.MakeVertex(0., 0., 0.)
p2 = geompy.MakeVertex(100., 100., 100.)
box = geompy.MakeBoxTwoPnt(p1, p2)
geompy.addToStudy(box, "box")

p3 = geompy.MakeVertex(25., 5., 25.)
sphere1 = geompy.MakeSpherePntR(p3, 15.)
geompy.addToStudy(sphere1, "sphere1")

sphere1_trans = geompy.MakeTranslation(sphere1, 0, 100, 0)
geompy.addToStudy(sphere1_trans, "sphere1_trans")

sphere1_trans = geompy.MakeTranslation(sphere1, 0, 100, 0)
geompy.addToStudy(sphere1_trans, "sphere1_trans")

p4 = geompy.MakeVertex(5, 50, 90)
sphere2 = geompy.MakeSpherePntR(p4, 20.)

sphere2_trans = geompy.MakeTranslation(sphere2, 100, 0, 0)
geompy.addToStudy(sphere2_trans, "sphere2_trans")

sphere2_trans2 = geompy.MakeTranslation(sphere2, 0, 0, -100)
geompy.addToStudy(sphere2_trans2, "sphere2_trans2")

sphere2_trans3 = geompy.MakeTranslation(sphere2, 100, 0, -100)
geompy.addToStudy(sphere2_trans3, "sphere2_trans3")

if simple:
    part = box
else:
    part = geompy.MakePartition([box], [sphere1, sphere1_trans, sphere2, sphere2_trans, sphere2_trans2, sphere2_trans3])
geompy.addToStudy(part, "part")

Vx = geompy.MakeVectorDXDYDZ(1, 0, 0)
Vy = geompy.MakeVectorDXDYDZ(0, 1, 0)
Vz = geompy.MakeVectorDXDYDZ(0, 0, 1)

left_faces = geompy.GetShapesOnPlane(part, geompy.ShapeType["FACE"], Vy, GEOM.ST_ON)
left = geompy.CreateGroup(part, geompy.ShapeType["FACE"])
geompy.UnionList(left, left_faces)
geompy.addToStudyInFather(part, left, "left")

right_faces = geompy.GetShapesOnPlaneWithLocation(part, geompy.ShapeType["FACE"], Vy, p2, GEOM.ST_ON)
right = geompy.CreateGroup(part, geompy.ShapeType["FACE"])
geompy.UnionList(right, right_faces)
geompy.addToStudyInFather(part, right, "right")

back_faces = geompy.GetShapesOnPlane(part, geompy.ShapeType["FACE"], Vx, GEOM.ST_ON)
back = geompy.CreateGroup(part, geompy.ShapeType["FACE"])
geompy.UnionList(back, back_faces)
geompy.addToStudyInFather(part, back, "back")

front_faces = geompy.GetShapesOnPlaneWithLocation(part, geompy.ShapeType["FACE"], Vx, p2, GEOM.ST_ON)
front = geompy.CreateGroup(part, geompy.ShapeType["FACE"])
geompy.UnionList(front, front_faces)
geompy.addToStudyInFather(part, front, "front")

bottom_faces = geompy.GetShapesOnPlane(part, geompy.ShapeType["FACE"], Vz, GEOM.ST_ON)
bottom = geompy.CreateGroup(part, geompy.ShapeType["FACE"])
geompy.UnionList(bottom, bottom_faces)
geompy.addToStudyInFather(part, bottom, "bottom")

top_faces = geompy.GetShapesOnPlaneWithLocation(part, geompy.ShapeType["FACE"], Vz, p2, GEOM.ST_ON)
top = geompy.CreateGroup(part, geompy.ShapeType["FACE"])
geompy.UnionList(top, top_faces)
geompy.addToStudyInFather(part, top, "top")

sources = geompy.CreateGroup(part, geompy.ShapeType["FACE"])
geompy.UnionList(sources, left_faces)
geompy.UnionList(sources, back_faces)
geompy.UnionList(sources, top_faces)
geompy.addToStudyInFather(part, sources, "sources")

# Mesh
# ====

import SMESH
from salome.smesh import smeshBuilder
smesh = smeshBuilder.New()

Mesh = smesh.Mesh(part, "Mesh")

algo2d = Mesh.Triangle(algo=smeshBuilder.MG_CADSurf)
algo2d.SetGeometricMesh( 1 )
algo2d.SetAngleMesh( 4 )
algo2d.SetPhySize( 8 )
algo2d.SetVerbosity(1)

# Periodicity
#algo2d.SetPreCADOptionValue("periodic_tolerance", "1e-2")
algo2d.AddPreCadFacesPeriodicity(left, right)
algo2d.AddPreCadFacesPeriodicity(front, back)
algo2d.AddPreCadFacesPeriodicity(bottom, top)

gr_left = Mesh.Group(left)
gr_right = Mesh.Group(right)
gr_front = Mesh.Group(front)
gr_back = Mesh.Group(back)
gr_bottom = Mesh.Group(bottom)
gr_top = Mesh.Group(top)

Mesh.Compute()

left_translated = Mesh.TranslateObjectMakeMesh( gr_left, SMESH.DirStruct( SMESH.PointStruct ( 0, 100, 0 )), 0, 'left_translated' )
front_translated = Mesh.TranslateObjectMakeMesh( gr_front, SMESH.DirStruct( SMESH.PointStruct ( -100, 0, 0 )), 0, 'front_translated' )
bottom_translated = Mesh.TranslateObjectMakeMesh( gr_bottom, SMESH.DirStruct( SMESH.PointStruct ( 0, 0, 100 )), 0, 'bottom_translated' )

def checkProjection(gr, mesh_translated, tol=1e-7):
    name = gr.GetName() + "_" + mesh_translated.GetName().split("_")[0]
    mesh_source = smesh.CopyMesh(gr, gr.GetName())
    mesh_check = smesh.Concatenate([mesh_source.GetMesh(), mesh_translated.GetMesh()], 0, name=name)
    ll_coincident_nodes = mesh_check.FindCoincidentNodes(tol)
    coincident_nodes = [item for sublist in ll_coincident_nodes for item in sublist]
    mesh_check.MakeGroupByIds("coincident_nodes", SMESH.NODE, coincident_nodes)
    mesh_nodes = mesh_check.GetNodesId()
 if len(ll_coincident_nodes) != mesh_translated.NbNodes():
        non_coincident_nodes = list(set(mesh_nodes) - set(coincident_nodes))
        mesh_check.MakeGroupByIds("non_coincident_nodes", SMESH.NODE, non_coincident_nodes)
 raise Exception("Projection failed for %s"%name)
 
checkProjection(gr_right, left_translated)
checkProjection(gr_back, front_translated)
checkProjection(gr_top, bottom_translated)

salome.sg.updateObjBrowser()
```

[Download this script](https://docs.salome-platform.org/latest/examples/BLSURFPLUGIN/periodicity_prepro.py)
