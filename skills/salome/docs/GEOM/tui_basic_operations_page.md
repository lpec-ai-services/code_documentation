<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_basic_operations_page.html -->

# Basic Operations

## Partition

```python
# Partition

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create a vertex and a vector
p0   = geompy.MakeVertex(  0.,   0.,   0.)
p200 = geompy.MakeVertex(200., 200., 200.)
pz   = geompy.MakeVertex(  0.,   0., 100.)

# create a vector
vxyz = geompy.MakeVectorDXDYDZ(100., 100., 100.)

# create a box from two points
box = geompy.MakeBoxTwoPnt(p0, p200)

# create a plane
trimsize  = 500.
plane = geompy.MakePlane(pz, vxyz, trimsize)

# create partition
partition = geompy.MakePartition([box], [plane])

# add objects in the study
id_box = geompy.addToStudy(box,"Box")
id_plane = geompy.addToStudy(plane,"Plane")
id_partition = geompy.addToStudy(partition,"Partition")

# display the partition objects and the plane
gg.createAndDisplayGO(id_box)
gg.setDisplayMode(id_box,1)
gg.createAndDisplayGO(id_plane)
gg.setDisplayMode(id_plane,1)
gg.createAndDisplayGO(id_partition)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/basic_operations_ex01.py)

## Archimede

```python
# Archimede

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create a vertex and a vector
p0   = geompy.MakeVertex(  0.,   0.,   0.)
p200 = geompy.MakeVertex(200., 200., 200.)

# create a box from two points
box = geompy.MakeBoxTwoPnt(p0, p200)

# perform an Archimede operation on the selected shape with selected parameters
weight  = 1000000.
waterdensity = 1.
meshingdeflection = 0.01
archimede  = geompy.Archimede(box, weight, waterdensity, meshingdeflection)

# add objects in the study
id_box = geompy.addToStudy(box,"Box")
id_archimede = geompy.addToStudy(archimede,"Archimede")

# display the box and the result of Archimede operation
gg.createAndDisplayGO(id_box)
gg.setDisplayMode(id_box,1)
gg.createAndDisplayGO(id_archimede)
gg.setDisplayMode(id_archimede,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/basic_operations_ex02.py)

## Restore presentation parameters and sub-shapes

```python
# Restore presentation parameters and sub-shapes

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
import SALOMEDS

# create a box and a cylinder
box = geompy.MakeBoxDXDYDZ(200, 200, 200)
cyl = geompy.MakeCylinderRH(100, 300)

# create translated box
vec = geompy.MakeVectorDXDYDZ(100, 50, 0)
tra = geompy.MakeTranslationVector(box, vec)

# create partition objects
partition1 = geompy.MakePartition([box, cyl])
partition2 = geompy.MakePartition([box], [cyl])
partition3 = geompy.MakePartition([box], [tra])

# set colours
box.SetColor(SALOMEDS.Color(1,0,0))
cyl.SetColor(SALOMEDS.Color(0,1,0))

# add objects in the study
geompy.addToStudy(box, "Box")
geompy.addToStudy(cyl, "Cylinder")
geompy.addToStudy(vec, "Vector")
geompy.addToStudy(tra, "Translation")
geompy.addToStudy(partition1, "Partition_1")
geompy.addToStudy(partition2, "Partition_2")
geompy.addToStudy(partition3, "Partition_3")

# Restore presentation parameters and sub-shapes
# different methods can be used to find the sub-shapes in the result:
# GetInPlace, GetSame, GetInPlaceByHistory, GetShapesOnShape.
# By default, GetInPlace method is used (GEOM.FSM_GetInPlace)
geompy.RestoreSubShapes(partition1)

geompy.RestoreSubShapes(partition2, [], GEOM.FSM_GetInPlace)

# The list of arguments can be used to avoid restoring all arguments,
# but restore only the passed.
geompy.RestoreSubShapes(partition3, [tra], GEOM.FSM_GetInPlaceByHistory)

# To find sub-shapes in a transformed shape only one method could be
# used: pass GEOM.FSM_Transformed for that.
# True passed for the last argument, means that the transformed shape
# will inherit colour and sub-shapes from its first argument (see above
# MakeTranslation).
geompy.RestoreSubShapes(tra, [], GEOM.FSM_Transformed, True)

# Also we could do this directly with method addToStudy:
partition4 = geompy.MakePartition([box, tra])
geompy.addToStudy(partition4, "Partition_4", True, [],
                  GEOM.FSM_GetInPlaceByHistory, False)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/basic_operations_ex03.py)

## Get shared shapes

```python
# Get shared sub-shapes

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
import SALOMEDS

# create a box and partigion it by two planes
box = geompy.MakeBoxDXDYDZ(200, 200, 200)
p = geompy.MakeVertex(100, 100, 100)
v1 = geompy.MakeVectorDXDYDZ(1, 1, 0)
v2 = geompy.MakeVectorDXDYDZ(1, -1, 0)
pln1 = geompy.MakePlane(p, v1, 2000)
pln2 = geompy.MakePlane(p, v2, 2000)
partition = geompy.MakePartition([box], [pln1, pln2])

# extract solids from result of partition
solids = geompy.SubShapeAllSorted(partition, geompy.ShapeType['SOLID'])

# get shared shapes from the partition (compound of 4 solids)
# a) faces that are shared by all 4 solids (0 found)
pF_T = geompy.GetSharedShapesMulti(partition, geompy.ShapeType['FACE'])
# b) faces that are shared by any couple of solids (4 found)
pF_F = geompy.GetSharedShapesMulti(partition, geompy.ShapeType['FACE'], False)
# c) edges that are shared by all 4 solids (1 found)
pE_T = geompy.GetSharedShapesMulti(partition, geompy.ShapeType['EDGE'])
# d) edges that are shared by any couple of solids (13 found)
pE_F = geompy.GetSharedShapesMulti(partition, geompy.ShapeType['EDGE'], False)

# get shared shapes from the list of solids
# a) faces that are shared by all 4 solids (0 found)
sF_T = geompy.GetSharedShapesMulti(solids, geompy.ShapeType['FACE'])
# b) faces that are shared by 1st/2nd, 1st/3rd and 1st/4th solids (2 found)
sF_F = geompy.GetSharedShapesMulti(solids, geompy.ShapeType['FACE'], False)
# c) edges that are shared by all 4 solids (1 found)
sE_T = geompy.GetSharedShapesMulti(solids, geompy.ShapeType['EDGE'])
# d) edges that are shared by 1st/2nd, 1st/3rd and 1st/4th solids (7 found)
sE_F = geompy.GetSharedShapesMulti(solids, geompy.ShapeType['EDGE'], False)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/basic_operations_ex04.py)
