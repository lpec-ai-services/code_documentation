<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/tui_grouping_elements.html -->

# Grouping Elements

## Create a Standalone Group

```python
# Create a Standalone Group

from mechanic import *

# Get ids of all faces with area > 100 
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Area, SMESH.FT_MoreThan, 100.)

anIds = mesh.GetIdsFromFilter(aFilter) 

# create a group consisting of faces with area > 100
aGroup1 = mesh.MakeGroupByIds("Area > 100", SMESH.FACE, anIds)

# create a group that contains all nodes from the mesh
aGroup2 = mesh.CreateEmptyGroup(SMESH.NODE, "all nodes")
aGroup2.AddFrom(mesh.mesh)

# ====================================
# Various methods of the Group object
# ====================================

aGroup = mesh.CreateEmptyGroup(SMESH.NODE, "aGroup")

# set/get group name
aGroup.SetName( "new name" )
print("name", aGroup.GetName())

# get group type (type of entities in the group, SMESH.NODE in our case)
print("type", aGroup.GetType())

# get number of entities (nodes in our case) in the group
print("size", aGroup.Size())

# check of emptiness
print("is empty", aGroup.IsEmpty())

# check of presence of an entity in the group
aGroup.Add([1,2]) # Add() method is specific to the standalone group
print("contains node 2", aGroup.Contains(2))

# get an entity by index
print("1st node", aGroup.GetID(1))

# get all entities
print("all", aGroup.GetIDs())

# get number of nodes (actual for groups of elements)
print("nb nodes", aGroup.GetNumberOfNodes())

# get underlying nodes (actual for groups of elements)
print("nodes", aGroup.GetNodeIDs())

# set/get color
import SALOMEDS
aGroup.SetColor( SALOMEDS.Color(1.,1.,0.));
print("color", aGroup.GetColor())

# ----------------------------------------------------------------------------
# methods specific to the standalone group and not present in GroupOnGeometry
# and GroupOnFilter
# ----------------------------------------------------------------------------

# clear the group's contents
aGroup.Clear()

# add contents of other object (group, sub-mesh, filter)
aGroup.AddFrom( aGroup2 )

# removes entities
aGroup.Remove( [2,3,4] )
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/c3ec8edb4f4f821b31bef2c70e6c4fa7/grouping_elements_ex01.py)

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/create_group.png)

## Create a Group on Geometry

```python
# Create a Group on Geometry

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a box
box = geom_builder.MakeBox(0., 0., 0., 100., 100., 100.)
geom_builder.addToStudy(box, "box")

# add the first face of the box to the study
subShapeList = geom_builder.SubShapeAll(box, geom_builder.ShapeType["FACE"])
face = subShapeList[0]
geom_builder.addToStudyInFather(box, face, "face 1") 

# create group of edges on the face
aGeomGroupE = geom_builder.CreateGroup(face, geom_builder.ShapeType["EDGE"])
geom_builder.AddObject(aGeomGroupE, 3)
geom_builder.AddObject(aGeomGroupE, 6)
geom_builder.AddObject(aGeomGroupE, 8)
geom_builder.AddObject(aGeomGroupE, 10)
geom_builder.addToStudyInFather(face, aGeomGroupE, "Group of Edges")

# create quadrangle 2D mesh on the box
quadra = smesh_builder.Mesh(box, "Box : quadrangle 2D mesh")
algo1D = quadra.Segment()
quadra.Quadrangle()
algo1D.NumberOfSegments(7) 

# compute the mesh
if not quadra.Compute(): raise Exception("Error when computing Mesh")

# create SMESH group on the face with name "SMESHGroup1"
aSmeshGroup1 = quadra.GroupOnGeom(face, "SMESHGroup1")

# create SMESH group on <aGeomGroupE> with default name
aSmeshGroup2 = quadra.GroupOnGeom(aGeomGroupE)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/1b6004036b8dc05106e4a0f5ec17da46/grouping_elements_ex02.py)

## Create a Group on Filter

```python
# Create a Group on Filter

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

box = geom_builder.MakeBoxDXDYDZ(10,10,10)

# make a mesh with quadrangles of different area in range [1,16]
mesh = smesh_builder.Mesh(box,"Quad mesh")
hyp1D = mesh.Segment().StartEndLength( 1, 4 )
mesh.Quadrangle()
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# create a group on filter selecting faces of medium size
critaria = [ \
    smesh_builder.GetCriterion(SMESH.FACE, SMESH.FT_Area, ">", 1.1, BinaryOp=SMESH.FT_LogicalAND ),
    smesh_builder.GetCriterion(SMESH.FACE, SMESH.FT_Area, "<", 15.0 )
    ]
filt = smesh_builder.GetFilterFromCriteria( critaria )
filtGroup = mesh.GroupOnFilter( SMESH.FACE, "group on filter", filt )
print("Group on filter contains %s elements" % filtGroup.Size())

# group on filter is updated if the mesh is modified
hyp1D.SetStartLength( 2.5 )
hyp1D.SetEndLength( 2.5 )
if not mesh.Compute(): raise Exception("Error when computing Mesh")
print("After mesh change, group on filter contains %s elements" % filtGroup.Size())

# set a new filter defining the group
filt2 = smesh_builder.GetFilter( SMESH.FACE, SMESH.FT_RangeOfIds, "1-50" )
filtGroup.SetFilter( filt2 )
print("With a new filter, group on filter contains %s elements" % filtGroup.Size())

# group is updated at modification of the filter
filt2.SetCriteria( [ smesh_builder.GetCriterion( SMESH.FACE, SMESH.FT_RangeOfIds, "1-70" )])
filtIDs3 = filtGroup.GetIDs()
print("After filter modification, group on filter contains %s elements" % filtGroup.Size())
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/a2654861ec9075e77a0c2a0215ded0ab/grouping_elements_ex03.py)

## Edit a Group

```python
# Edit a Group

from mechanic import *

# Get ids of all faces with area > 35
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Area, SMESH.FT_MoreThan, 35.)

anIds = mesh.GetIdsFromFilter(aFilter) 

print("Criterion: Area > 35, Nb = ", len(anIds))

# create a group by adding elements with area > 35
aGroup = mesh.CreateEmptyGroup(SMESH.FACE, "Area > 35")
aGroup.Add(anIds) 

# Get ids of all faces with area > 40
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Area, SMESH.FT_MoreThan, 40.)

anIds = mesh.GetIdsFromFilter(aFilter)

print("Criterion: Area > 40, Nb = ", len(anIds)) 

# create a group of elements with area [35; 40] by removing elements with area > 40 from group aGroup
aGroup.Remove(anIds) 
aGroup.SetName("35 < Area < 40")

# print the result
aGroupElemIDs = aGroup.GetListOfID()

print("Criterion: 35 < Area < 40, Nb = ", len(aGroupElemIDs))

j = 1
for i in range(len(aGroupElemIDs)):
  if j > 20: j = 1; print("")
  print(aGroupElemIDs[i], end=' ')
  j = j + 1
  pass
print("")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/737f444696d17d3f1da150b5d86cf553/grouping_elements_ex04.py)

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/editing_groups1.png)

## Union of groups

```python
# Union of groups

from mechanic import *
import SALOMEDS

# Criterion : AREA > 20
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Area, SMESH.FT_MoreThan, 20.)

anIds = mesh.GetIdsFromFilter(aFilter)

print("Criterion: Area > 20, Nb = ", len( anIds )) 

# create a group by adding elements with area > 20
aGroup1 = mesh.CreateEmptyGroup(SMESH.FACE, "Area > 20")
aGroup1.Add(anIds)

# Criterion : AREA = 20
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Area, SMESH.FT_EqualTo, 20.)

anIds = mesh.GetIdsFromFilter(aFilter)

print("Criterion: Area = 20, Nb = ", len( anIds )) 

# create a group by adding elements with area = 20
aGroup2 = mesh.CreateEmptyGroup( SMESH.FACE, "Area = 20" )

aGroup2.Add(anIds)

# create union group : area >= 20
aGroup3 = mesh.UnionListOfGroups([aGroup1, aGroup2], "Area >= 20")
aGroup3.SetColor( SALOMEDS.Color(1.,1.,0.));
print("Criterion: Area >= 20, Nb = ", len(aGroup3.GetListOfID()))
# Please note that also there is UnionGroups() method which works with two groups only

# Criterion : AREA < 20
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Area, SMESH.FT_LessThan, 20.)

anIds = mesh.GetIdsFromFilter(aFilter)

print("Criterion: Area < 20, Nb = ", len(anIds))

# create a group by adding elements with area < 20
aGroup4 = mesh.CreateEmptyGroup(SMESH.FACE, "Area < 20")
aGroup4.Add(anIds)
aGroup4.SetColor( SALOMEDS.Color(1.,0.,0.));

# create union group : area >= 20 and area < 20
aGroup5 = mesh.UnionListOfGroups([aGroup3, aGroup4], "Any Area")
print("Criterion: Any Area, Nb = ", len(aGroup5.GetListOfID()))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/28f196e13af7cebfceabc54ea2238064/grouping_elements_ex05.py)

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/union_groups1.png)

## Intersection of groups

```python
# Intersection of groups

from mechanic import *

# Criterion : AREA > 20
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Area, SMESH.FT_MoreThan, 20.)

anIds = mesh.GetIdsFromFilter(aFilter)

print("Criterion: Area > 20, Nb = ", len(anIds)) 

# create a group by adding elements with area > 20
aGroup1 = mesh.CreateEmptyGroup(SMESH.FACE, "Area > 20")
aGroup1.Add(anIds)

# Criterion : AREA < 60
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Area, SMESH.FT_LessThan, 60.)

anIds = mesh.GetIdsFromFilter(aFilter)

print("Criterion: Area < 60, Nb = ", len(anIds)) 

# create a group by adding elements with area < 60
aGroup2 = mesh.CreateEmptyGroup(SMESH.FACE, "Area < 60")
aGroup2.Add(anIds)

# create an intersection of groups : 20 < area < 60
aGroup3 = mesh.IntersectListOfGroups([aGroup1, aGroup2], "20 < Area < 60")
print("Criterion: 20 < Area < 60, Nb = ", len(aGroup3.GetListOfID()))
# Please note that also there is IntersectGroups() method which works with two groups only
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/9d22de9d5d6c1bf51a428f2fde9727e3/grouping_elements_ex06.py)

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/intersect_groups1.png)

## Cut of groups

```python
# Cut of groups

from mechanic import *

# Criterion : AREA > 20
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Area, SMESH.FT_MoreThan, 20.)

anIds = mesh.GetIdsFromFilter(aFilter)

print("Criterion: Area > 20, Nb = ", len(anIds)) 

# create a group by adding elements with area > 20
aGroupMain = mesh.MakeGroupByIds("Area > 20", SMESH.FACE, anIds)

# Criterion : AREA < 60
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Area, SMESH.FT_LessThan, 60.)

anIds = mesh.GetIdsFromFilter(aFilter)

print("Criterion: Area < 60, Nb = ", len(anIds)) 

# create a group by adding elements with area < 60
aGroupTool = mesh.MakeGroupByIds("Area < 60", SMESH.FACE, anIds)
 
# create a cut of groups : area >= 60
aGroupRes = mesh.CutGroups(aGroupMain, aGroupTool, "Area >= 60")
print("Criterion: Area >= 60, Nb = ", len(aGroupRes.GetListOfID()))
# Please note that also there is CutListOfGroups() method which works with lists of groups of any lengths
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/4e5816c20bde8c34c24662e0045d2b53/grouping_elements_ex07.py)

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/cut_groups1.png)

## Creating groups of entities basing on nodes of other groups

```python
# Creating groups of entities basing on nodes of other groups

from mechanic import *
import SALOMEDS

# Criterion : AREA > 100
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Area, SMESH.FT_MoreThan, 100.)

# create a group by adding elements with area > 100
aSrcGroup1 = mesh.GroupOnFilter(SMESH.FACE, "Area > 100", aFilter)
aSrcGroup1.SetColor( SALOMEDS.Color(1.,1.,0.))
print("Criterion: Area > 100, Nb = ", aSrcGroup1.Size())

# Criterion : AREA < 30
aFilter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Area, SMESH.FT_LessThan, 30.)

# create a group by adding elements with area < 30
aSrcGroup2 = mesh.GroupOnFilter(SMESH.FACE, "Area < 30", aFilter)
aSrcGroup2.SetColor( SALOMEDS.Color(1.,0.,0.))
print("Criterion: Area < 30, Nb = ", aSrcGroup2.Size())

# Create group of edges using source groups of faces
aGrp = mesh.CreateDimGroup( [aSrcGroup1, aSrcGroup2], SMESH.EDGE, "Edges" )

# Create group of nodes using source groups of faces
aGrp = mesh.CreateDimGroup( [aSrcGroup1, aSrcGroup2], SMESH.NODE, "Nodes" )
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/4b66381ee851950e8f6fb7e8e9c63976/grouping_elements_ex08.py)

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/dimgroup_tui1.png)

## Creating face groups separated by sharp edges

```python
# Creating groups of faces separated by sharp edges

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a mesh on a box
box = geom_builder.MakeBoxDXDYDZ( 10,10,10, theName="Box" )
mesh = smesh_builder.Mesh(box,"Mesh")
mesh.AutomaticHexahedralization()

# create groups of faces of each side of the box
groups = mesh.FaceGroupsSeparatedByEdges( 89 )
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/a6b506f0a6d9030f333bba649943b7fd/grouping_elements_ex09.py)
