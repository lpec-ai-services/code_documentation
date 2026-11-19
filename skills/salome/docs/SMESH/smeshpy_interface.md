<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/smeshpy_interface.html -->

# Python interface

Python API of SALOME Mesh module defines several classes that can
be used for easy mesh creation and edition.

Documentation of SALOME Mesh module Python API is available in two forms:

- [Structured documentation](modules.md), where all methods and classes are grouped by their functionality.
- [Linear documentation](py-modindex.md) grouped only by classes, declared in the [`smeshBuilder`](smeshBuilder.md#module-smeshBuilder) Python module.

With SALOME 7.2, the Python interface for Mesh has been slightly modified to offer new functionality.
You may have to modify your scripts generated with SALOME 6 or older versions.
Please see [Modifying Mesh Python scripts from SALOME 6 and before](smesh_migration.md#smesh-migration-page).

Class [`smeshBuilder.smeshBuilder`](smeshBuilder.md#smeshBuilder.smeshBuilder) provides an interface to create and handle
meshes. It can be used to create an empty mesh or to import mesh from the data file.

As soon as a mesh is created, it is possible to manage it via its own
methods, described in class [`smeshBuilder.Mesh`](smeshBuilder.md#smeshBuilder.Mesh) documentation.

Class [`smeshstudytools.SMeshStudyTools`](smeshstudytools.md#smeshstudytools.SMeshStudyTools) provides several methods to manipulate mesh objects in Salome study.

A usual workflow to generate a mesh on geometry is following:

1. Create an instance of `smeshBuilder.smeshBuilder`:
   :   ```python
       from salome.smesh import smeshBuilder
       smesh = smeshBuilder.New()
       ```
2. Create a [`smeshBuilder.Mesh`](smeshBuilder.md#smeshBuilder.Mesh) object:

   > ```python
   > mesh = smesh.Mesh( geometry )
   > ```
3. Create and assign algorithms by calling corresponding methods of the mesh. If a sub-shape is provided as an argument, a sub-mesh is implicitly created on this sub-shape:
   :   ```python
       regular1D  = mesh.Segment()
       quadrangle = mesh.Quadrangle()
       # use other 2D algorithm on a face -- a sub-mesh appears in the mesh
       triangle   = mesh.Triangle( face )
       ```
4. Create and assign hypotheses by calling corresponding methods of algorithms:
   :   ```python
       regular1D.LocalLength( 10. )
       quadrangle.Reduced()
       triangle.SetMaxSize( 20. )
       triangle.SetFineness( smeshBuilder.VeryCoarse )
       ```
5. Compute the mesh (generate mesh nodes and elements):
   :   ```python
       mesh.Compute()
       ```

An easiest way to start with Python scripting is to do something in
GUI and then to get a corresponding Python script via
**File > Dump Study** menu item. Don’t forget that you can get
all methods of any object in hand (e.g. a mesh group or a hypothesis)
by calling *dir()* Python built-in function.

All methods of the [`Mesh Group`](smesh_module.md#SMESH.SMESH_GroupBase) can be found in [Create a Standalone Group](tui_grouping_elements.md#tui-create-standalone-group) sample script.

An example below demonstrates usage of the Python API for 3D mesh
generation and for retrieving basic information on mesh nodes, elements and groups.

## Example of 3d mesh generation:

```python
# 3d mesh generation and mesh exploration

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

###
# Geometry: an assembly of a box, a cylinder and a truncated cone
# to be meshed with tetrahedra
###

# Define values
name = "ex21_lamp" 
cote = 60 
section = 20 
size = 200 
radius_1 = 80 
radius_2 = 40 
height = 100 

# Build a box
box = geom_builder.MakeBox(-cote, -cote, -cote, +cote, +cote, +cote) 

# Build a cylinder
pt1 = geom_builder.MakeVertex(0, 0, cote/3) 
di1 = geom_builder.MakeVectorDXDYDZ(0, 0, 1) 
cyl = geom_builder.MakeCylinder(pt1, di1, section, size) 

# Build a truncated cone
pt2 = geom_builder.MakeVertex(0, 0, size) 
cone = geom_builder.MakeCone(pt2, di1, radius_1, radius_2, height) 

# Fuse
box_cyl = geom_builder.MakeFuse(box, cyl) 
piece = geom_builder.MakeFuse(box_cyl, cone) 

# Add to the study
geom_builder.addToStudy(piece, name) 

# Create a group of faces
faces_group = geom_builder.CreateGroup(piece, geom_builder.ShapeType["FACE"]) 
group_name = name + "_grp" 
geom_builder.addToStudy(faces_group, group_name) 
faces_group.SetName(group_name) 

# Add faces to the group
faces = geom_builder.SubShapeAllIDs(piece, geom_builder.ShapeType["FACE"]) 
geom_builder.UnionIDs(faces_group, faces) 

###
# Create a mesh
###

# Define a mesh on a geometry
tetra = smesh_builder.Mesh(piece, name) 

# Define 1D algorithm and hypothesis
algo1d = tetra.Segment() 
algo1d.LocalLength(10) 

# Define 2D algorithm and hypothesis
algo2d = tetra.Triangle() 
algo2d.LengthFromEdges() 

# Define 3D algorithm and hypothesis
algo3d = tetra.Tetrahedron()
algo3d.MaxElementVolume(100) 

# Compute the mesh
if not tetra.Compute(): raise Exception("Error when computing Mesh")

# Create a mesh group of all triangles generated on geom faces present in faces_group
group = tetra.Group(faces_group)

###
# Explore the mesh
###

# Retrieve coordinates of nodes
coordStr = ""
for node in tetra.GetNodesId():
    x,y,z = tetra.GetNodeXYZ( node )
    coordStr += "%s (%s, %s, %s) " % ( node, x,y,z )
    pass

# Retrieve nodal connectivity of triangles
triaStr = ""
for tria in tetra.GetElementsByType( SMESH.FACE ):
    nodes = tetra.GetElemNodes( tria )
    triaStr += "%s (%s, %s, %s) " % ( tria, nodes[0], nodes[1], nodes[2] )

# Retrieve group contents
groupStr = ""
for group in tetra.GetGroups():
    ids   = group.GetIDs()
    name  = group.GetName()
    eType = group.GetType()
    groupStr += "'%s' %s: %s \n" % ( name, eType, ids )
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/ebd3862228c833f838012ee500d5b6be/mesh_3d.py)

Examples of Python scripts for Mesh operations are available by
the following links:

- [Creating Meshes](tui_creating_meshes.md)
- [Defining Hypotheses and Algorithms](tui_defining_hypotheses.md)
- [Grouping Elements](tui_grouping_elements.md)
- [Filters usage](tui_filters.md)
- [Modifying Meshes](tui_modifying_meshes.md)
- [Transforming Meshes](tui_transforming_meshes.md)
- [Viewing Meshes](tui_viewing_meshes.md)
- [Quality Controls](tui_quality_controls.md)
- [Adaptation](tui_adaptation.md)
- [Measurements](tui_measurements.md)
- [How to work with objects from the GUI ?](tui_work_on_objects_from_gui.md)
- [Using SALOME NoteBook](tui_notebook_smesh.md)
