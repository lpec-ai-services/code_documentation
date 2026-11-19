<!-- source: https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/ghs3dplugin_python_interface_page.html -->

# Python Interface

Note
:   The former name of MG-Tetra mesher is *GHS3D* and names of the corresponding classes and modules still include *"GHS3D"*.

Python package [GHS3DPluginBuilder](../GHS3DPLUGIN/ghs3dpluginpy_doc/namespaceGHS3DPluginBuilder.md) defines [GHS3DPluginBuilder.GHS3D_Algorithm](../GHS3DPLUGIN/ghs3dpluginpy_doc/classGHS3DPluginBuilder_1_1GHS3D__Algorithm.md) class providing access to the MG-Tetra meshing algorithm and its parameters.

You can get an instance of this class by calling [smeshBuilder.Mesh.Tetrahedron](../GHS3DPLUGIN/ghs3dpluginpy_doc/classsmeshBuilder_1_1Mesh.md#a2622f0d55649077abf581277531e6b2b)(algo=smeshBuilder.MG_Tetra) or [smeshBuilder.Mesh.Tetrahedron](../GHS3DPLUGIN/ghs3dpluginpy_doc/classsmeshBuilder_1_1Mesh.md#a2622f0d55649077abf581277531e6b2b)(algo=smeshBuilder.GHS3D). This call creates an algorithm (if not yet exist), assigns it to the mesh and returns an instance of [GHS3DPluginBuilder.GHS3D_Algorithm](../GHS3DPLUGIN/ghs3dpluginpy_doc/classGHS3DPluginBuilder_1_1GHS3D__Algorithm.md) to the caller.

The class of algorithm has methods to set up meshing parameters.

Below you can see examples of usage of this class for tetrahedral mesh generation.

1. [Construction of Mesh using MG-Tetra algorithm](ghs3dplugin_python_interface_page.md#tui_ghs3d_basic)
2. [Adding enforced vertices](ghs3dplugin_python_interface_page.md#tui_ghs3d_enforced_vertices)
3. [Adding enforced mesh](ghs3dplugin_python_interface_page.md#tui_ghs3d_enforced_meshes)
4. [Mesh optimization](ghs3dplugin_python_interface_page.md#tui_ghs3d_optimization)

# Construction of Mesh using MG-Tetra algorithm

## Example of mesh generation with MG-Tetra algorithm:

```python
import salome
salome.salome_init()

from salome.geom import geomBuilder
geompy = geomBuilder.New()

from salome.smesh import smeshBuilder
smesh =  smeshBuilder.New()

# create a box
box = geompy.MakeBoxDXDYDZ(200., 200., 200.)
geompy.addToStudy(box, "box")

# create a mesh on the box
mgtetraMesh = smesh.Mesh(box,"box: MG-Tetra and MG-CADSurf mesh")

# create a MG_CADSurf algorithm for faces
MG_CADSurf = mgtetraMesh.Triangle(algo=smeshBuilder.MG_CADSurf)
MG_Tetra = mgtetraMesh.Tetrahedron(algo=smeshBuilder.MG_Tetra)

# compute the mesh
ok = mgtetraMesh.Compute()

if not ok:
 raise Exception("Error when computing mgtetraMesh")

volume = smesh.GetVolume(mgtetraMesh)
expected_volume = 200**3

assert (volume-expected_volume)/expected_volume < 1e-12

# End of script
```

[Download this script](https://docs.salome-platform.org/latest/examples/GHS3DPLUGIN/ghs3ddemo.py)

![ghs3d_screenshot.png](https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/ghs3d_screenshot.png)

MG-Tetra mesh without hypothesis

[Back to top](ghs3dplugin_python_interface_page.md#tui_ghs3d)

# Adding enforced vertices

## Example of enforced vertices with MG-Tetra algorithm:

```python
# An enforced vertex can be added via:
# - the coordinates x,y,z
# - a GEOM vertex or compound (No geometry, TUI only)
#
# The created enforced nodes can also be stored in
# a group.
#
# This feature is available only on meshes without geometry.

# Ex1: Add one enforced vertex with coordinates (50,50,100) 
#      and physical size 2.

import math

import salome
salome.salome_init()

from salome.geom import geomBuilder
geompy = geomBuilder.New()

import SMESH
from salome.smesh import smeshBuilder
smesh =  smeshBuilder.New()

def isNodeAtCoord(node_id, x, y, z, tol=1e-12):
  xn, yn, zn = mgtetraMesh.GetNodeXYZ(node_id)
  dist = math.sqrt((x-xn)**2+(y-yn)**2+(z-zn)**2)
  print("dist: ", dist)
 return dist < tol

# create a box
box = geompy.MakeBoxDXDYDZ(200., 200., 200.)
geompy.addToStudy(box, "box")
# create a mesh on the box
mgtetraMesh = smesh.Mesh(box,"box: MG-Tetra and MG-CADSurf mesh")
# create a MG-CADSurf algorithm for faces
mgtetraMesh.Triangle(algo=smeshBuilder.MG_CADSurf)
# compute the mesh
ok  = mgtetraMesh.Compute()
if not ok:
 raise Exception("Error when computing MG-CADSurf mesh")

# Make a copy of the 2D mesh
mgtetraMesh_wo_geometry = smesh.CopyMesh( mgtetraMesh, 'MG-Tetra w/o geometry', 0, 0)

# create a MG_Tetra algorithm and hypothesis and assign them to the mesh
MG_Tetra = mgtetraMesh.Tetrahedron( smeshBuilder.MG_Tetra )
MG_Tetra_Parameters = MG_Tetra.Parameters()
# Create the enforced vertex
x1 = 50
y1 = 50
z1 = 100
MG_Tetra_Parameters.SetEnforcedVertex( x1, y1, z1, 2) # no group
# Compute the mesh
ok = mgtetraMesh.Compute()
if not ok:
 raise Exception("Error when computing MG_Tetra mesh")

# Check that the enforced node is at the enforced coords
node_closest = mgtetraMesh.FindNodeClosestTo(x1, y1, z1)

assert isNodeAtCoord(node_closest, x1, y1, z1)

# Ex2: Add one vertex enforced by a GEOM vertex at (50,50,100) 
#      with physical size 5 and add it to a group called "My special nodes"

# Create another MG_Tetra hypothesis and assign it to the mesh without geometry
MG_Tetra_Parameters_wo_geometry = smesh.CreateHypothesis('MG-Tetra Parameters', 'GHS3DEngine')
mgtetraMesh_wo_geometry.AddHypothesis( MG_Tetra )
mgtetraMesh_wo_geometry.AddHypothesis( MG_Tetra_Parameters_wo_geometry )

# Create the enforced vertex
x2 = 50
y2 = 50
z2 = 100
p2 = geompy.MakeVertex(x2, y2, z2)
geompy.addToStudy(p2, "p2")
gr_enforced_name = "My special nodes"
MG_Tetra_Parameters_wo_geometry.SetEnforcedVertexGeomWithGroup( p2, 5 , gr_enforced_name)
#MG_Tetra_Parameters.SetEnforcedVertexGeom( p1, 5 ) # no group

# compute the mesh
ok = mgtetraMesh_wo_geometry.Compute()
if not ok:
 raise Exception("Error when computing MG_Tetra mesh without geometry")

# Check that the enforced node is at the enforced coords
gr_enforced_nodes = mgtetraMesh_wo_geometry.GetGroupByName(gr_enforced_name)[0]
assert (gr_enforced_nodes.Size() == 1)
node_enforced = gr_enforced_nodes.GetIDs()[0]

assert isNodeAtCoord(node_enforced, x2, y2, z2)

# Erase all enforced vertices
MG_Tetra_Parameters.ClearEnforcedVertices()

# End of script
```

[Download this script](https://docs.salome-platform.org/latest/examples/GHS3DPLUGIN/ghs3d_enfvert.py)

![ghs3d_screenshot_enf1.png](https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/ghs3d_screenshot_enf1.png)

MG-Tetra mesh with enforced vertex

![ghs3d_screenshot_enf2.png](https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/ghs3d_screenshot_enf2.png)

MG-Tetra mesh with enforced vertex from GEOM vertex

[Back to top](ghs3dplugin_python_interface_page.md#tui_ghs3d)

# Adding enforced mesh

## Example of enforced meshes with MG-Tetra algorithm:

```python
# It is possible to constrain MG-Tetra with another mesh or group.
# The constraint can refer to the nodes, edges or faces.
# This feature is available only on 2D meshes without geometry.
# The constraining elements are called enforced elements for the mesh.
# They can be recovered using groups if necessary.

# In the following examples, a box and a cylinder are meshed in 2D.
# The mesh of the cylinder will be used as a constraint for the 
# 3D mesh of the box.

import salome
salome.salome_init()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

import SMESH, SALOMEDS
from salome.smesh import smeshBuilder
smesh =  smeshBuilder.New()

box = geompy.MakeBoxDXDYDZ(200, 200, 200)
geompy.addToStudy( box, "box" )
cylindre = geompy.MakeCylinderRH(50, 50)
geompy.TranslateDXDYDZ(cylindre, 100, 100, 30)
face_cyl = geompy.ExtractShapes(cylindre, geompy.ShapeType["FACE"], True)[1]
geompy.addToStudy( cylindre, 'cylindre' )
geompy.addToStudyInFather( cylindre, face_cyl, 'face_cyl' )
p1 = geompy.MakeVertex(20, 20, 20)
p2 = geompy.MakeVertex(180, 180, 20)
c = geompy.MakeCompound([p1,p2])
geompy.addToStudy( p1, "p1" )
geompy.addToStudy( p2, "p2" )
geompy.addToStudy( c, "c" )

# Create the 2D algorithm and hypothesis
MG_CADSurf = smesh.CreateHypothesis('MG-CADSurf', 'BLSURFEngine')
# For the box
MG_CADSurf_Parameters = smesh.CreateHypothesis('MG-CADSurf Parameters', 'BLSURFEngine')
MG_CADSurf_Parameters.SetPhysicalMesh( 1 )
MG_CADSurf_Parameters.SetPhySize( 200 )
# For the cylinder
MG_CADSurf_Parameters2 = smesh.CreateHypothesis('MG-CADSurf Parameters', 'BLSURFEngine')
MG_CADSurf_Parameters2.SetGeometricMesh( 1 )

# Create the 3D algorithm and hypothesis
MG_Tetra = smesh.CreateHypothesis('MG-Tetra', 'GHS3DEngine')
MG_Tetra_Parameters_node = smesh.CreateHypothesis('MG-Tetra Parameters', 'GHS3DEngine')
#MG_Tetra_Parameters_node.SetToMeshHoles( 1 )
MG_Tetra_Parameters_edge = smesh.CreateHypothesis('MG-Tetra Parameters', 'GHS3DEngine')
#MG_Tetra_Parameters_edge.SetToMeshHoles( 1 )
MG_Tetra_Parameters_face = smesh.CreateHypothesis('MG-Tetra Parameters', 'GHS3DEngine')
MG_Tetra_Parameters_face.SetToMeshHoles( 1 ) # to mesh inside the cylinder
MG_Tetra_Parameters_mesh = smesh.CreateHypothesis('MG-Tetra Parameters', 'GHS3DEngine')
MG_Tetra_Parameters_mesh.SetToMeshHoles( 1 ) # to mesh inside the cylinder

# Create the mesh on the cylinder
Mesh_cylindre = smesh.Mesh(cylindre)
smesh.SetName(Mesh_cylindre,"Mesh_cylindre")
Mesh_cylindre.AddHypothesis( MG_CADSurf )
Mesh_cylindre.AddHypothesis( MG_CADSurf_Parameters2 )
# Create some groups
face_cyl_faces = Mesh_cylindre.GroupOnGeom(face_cyl,'group_face_cyl', SMESH.FACE)
face_cyl_edges = Mesh_cylindre.GroupOnGeom(face_cyl,'group_edge_cyl', SMESH.EDGE)
face_cyl_nodes = Mesh_cylindre.GroupOnGeom(face_cyl,'group_node_cyl', SMESH.NODE)
ok = Mesh_cylindre.Compute()
if not ok:
 raise Exception("Error when computing Mesh_cylindre with MG_CADSurf")

# Create the mesh on the cylinder
Mesh_box_tri = smesh.Mesh(box,"Mesh_box_tri")
Mesh_box_tri.AddHypothesis( MG_CADSurf )
Mesh_box_tri.AddHypothesis( MG_CADSurf_Parameters )
ok = Mesh_box_tri.Compute()
if not ok:
 raise Exception("Error when computing Mesh_box_tri with MG_CADSurf")

# Create 4 copies of the 2D mesh to test the 3 types of contraints (NODE, EDGE, FACE)
# from the whole mesh and from groups of elements.
# Then the 3D algo and hypothesis are assigned to them.

mesh_mesh = smesh.CopyMesh( Mesh_box_tri, 'Enforced by faces of mesh', 0, 0)
mesh_mesh.AddHypothesis( MG_Tetra )
mesh_mesh.AddHypothesis( MG_Tetra_Parameters_mesh)

mesh_node = smesh.CopyMesh( Mesh_box_tri, 'Enforced by group of nodes', 0, 0)
mesh_node.AddHypothesis( MG_Tetra )
mesh_node.AddHypothesis( MG_Tetra_Parameters_node)

mesh_edge = smesh.CopyMesh( Mesh_box_tri, 'Enforced by group of edges', 0, 0)
mesh_edge.AddHypothesis( MG_Tetra )
mesh_edge.AddHypothesis( MG_Tetra_Parameters_edge)

mesh_face = smesh.CopyMesh( Mesh_box_tri, 'Enforced by group of faces', 0, 0)
mesh_face.AddHypothesis( MG_Tetra )
mesh_face.AddHypothesis( MG_Tetra_Parameters_face)

# Add the enforced elements
MG_Tetra_Parameters_mesh.SetEnforcedMeshWithGroup(Mesh_cylindre.GetMesh(),SMESH.FACE,"faces from cylinder")
MG_Tetra_Parameters_node.SetEnforcedMeshWithGroup(face_cyl_nodes,SMESH.NODE,"nodes from face_cyl_nodes")
MG_Tetra_Parameters_edge.SetEnforcedMeshWithGroup(face_cyl_edges,SMESH.EDGE,"edges from face_cyl_edges")
MG_Tetra_Parameters_face.SetEnforcedMeshWithGroup(face_cyl_faces,SMESH.FACE,"faces from face_cyl_faces")

#Compute the meshes
ok = mesh_node.Compute()
if not ok:
 raise Exception("Error when computing mesh_node")
ok = mesh_edge.Compute()
if not ok:
 raise Exception("Error when computing mesh_edge")
ok = mesh_face.Compute()
if not ok:
 raise Exception("Error when computing mesh_face")
ok = mesh_mesh.Compute()
if not ok:
 raise Exception("Error when computing mesh_mesh")

def getNbNodes(mesh):
 try:
 #mesh
    nb_nodes = mesh.NbNodes()
 except:
 # group
    nb_nodes = mesh.GetNumberOfNodes()
 return nb_nodes

def checkEnforcedMesh(mesh, enforced_group, result_group, tol=1e-7):
  name = "Check " + mesh.GetName()
 # test nb nodes are the same between enforced group and the result group
 if getNbNodes(enforced_group) != getNbNodes(enforced_group):
 raise Exception("Enforce mesh failed for %s, wrong nummber of nodes"%name)
 # test that all nodes are imposed at the same place by finding coincident nodes in a compound mesh
  mesh_check = smesh.Concatenate([enforced_group, result_group], 0, name=name)
  ll_coincident_nodes = mesh_check.FindCoincidentNodes(tol)
  coincident_nodes = [item for sublist in ll_coincident_nodes for item in sublist]
  mesh_check.MakeGroupByIds("coincident_nodes", SMESH.NODE, coincident_nodes)
  mesh_nodes = mesh_check.GetNodesId()
 if len(ll_coincident_nodes) != getNbNodes(enforced_group):
    non_coincident_nodes = list(set(mesh_nodes) - set(coincident_nodes))
    mesh_check.MakeGroupByIds("non_coincident_nodes", SMESH.NODE, non_coincident_nodes)
 raise Exception("Enforce mesh failed for %s"%name)

checkEnforcedMesh(mesh_node, face_cyl_nodes, mesh_node.GetGroupByName("nodes from face_cyl_nodes")[0])
checkEnforcedMesh(mesh_edge, face_cyl_edges, mesh_edge.GetGroupByName("edges from face_cyl_edges")[0])
checkEnforcedMesh(mesh_face, face_cyl_faces, mesh_face.GetGroupByName("faces from face_cyl_faces")[0])
checkEnforcedMesh(mesh_mesh, Mesh_cylindre.GetMesh(), mesh_mesh.GetGroupByName("faces from cylinder")[0])

# End of script
```

[Download this script](https://docs.salome-platform.org/latest/examples/GHS3DPLUGIN/ghs3d_enfmesh.py)

![ghs3d_screenshot_enf3.png](https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/ghs3d_screenshot_enf3.png)

![ghs3d_screenshot_enf4.png](https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/ghs3d_screenshot_enf4.png)

![ghs3d_screenshot_enf5.png](https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/ghs3d_screenshot_enf5.png)

![ghs3d_screenshot_enf6.png](https://docs.salome-platform.org/latest/gui/GHS3DPLUGIN/ghs3d_screenshot_enf6.png)

# Mesh optimization

## Example of mesh optimization with MG-Tetra Optimization:

```python
import salome
salome.salome_init()

from salome.geom import geomBuilder
geompy = geomBuilder.New()

import SMESH
from salome.smesh import smeshBuilder
smesh =  smeshBuilder.New()

# create a disk
disk = geompy.MakeDiskR(100., 1, theName="disk")

# triangulate the disk
mesh = smesh.Mesh( disk )
cadsurf = mesh.Triangle( smeshBuilder.MG_CADSurf )
cadsurf.SetQuadAllowed( True )
ok = mesh.Compute()
if not ok:
 raise Exception("Error when computing mesh")

# extrude the 2D mesh into a prismatic mesh
mesh.ExtrusionSweepObject( mesh, [0,0,10], 7 )

# split prisms into tetrahedra
mesh.SplitVolumesIntoTetra( mesh )

# copy the mesh into a new mesh, since only a mesh not based of geometry
# can be optimized using MG-Tetra Optimization
optMesh = smesh.CopyMesh( mesh, "optimization" )

# add MG-Tetra Optimization
mg_opt = optMesh.Tetrahedron( smeshBuilder.MG_Tetra_Optimization )
mg_opt.SetSmoothOffSlivers( True )
mg_opt.SetOptimizationLevel( smeshBuilder.Strong_Optimization )

# run optimization
ok = optMesh.Compute()
if not ok:
 raise Exception("Error when computing optimization mesh")

print("Nb tetra before optimization", mesh.NbTetras())
print("Nb tetra after  optimization", optMesh.NbTetras())

# Check that aspect ratio 3D of optimized mesh is better than original mesh
min_aspectratio_orig, max_aspectratio_orig = mesh.GetMinMax(SMESH.FT_AspectRatio3D)
min_aspectratio_optim, max_aspectratio_optim = optMesh.GetMinMax(SMESH.FT_AspectRatio3D)

assert (min_aspectratio_orig - min_aspectratio_optim)/min_aspectratio_orig < 0.5
assert (max_aspectratio_orig - max_aspectratio_optim)/max_aspectratio_orig < 0.5

# End of script
```

[Download this script](https://docs.salome-platform.org/latest/examples/GHS3DPLUGIN/ghs3d_optimization.py)

[Back to top](ghs3dplugin_python_interface_page.md#tui_ghs3d)
