<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_boolean_operations_page.html -->

# Boolean Operations

## Fuse

```python
# Fuse

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create a vertex and a vector
p1 = geompy.MakeVertex(25, 55, 0)
p2 = geompy.MakeVertex( 0,  0, 0)
v = geompy.MakeVector(p1, p2)

# create a cylinder
height = 35
radius1 = 20
cylinder = geompy.MakeCylinder(p1, v, radius1, height)

# create a sphere
sphere = geompy.MakeSphereR(40)

# create a box
box = geompy.MakeBoxDXDYDZ(80, 80, 80)

# fuse
fuse1 = geompy.MakeFuse(cylinder, sphere)
fuse2 = geompy.MakeBoolean(cylinder, sphere, 3)
fuse3 = geompy.MakeFuseList([cylinder, sphere, box])

# add objects in the study
id_cylinder = geompy.addToStudy(cylinder, "Cylinder")
id_sphere = geompy.addToStudy(sphere, "Sphere")
id_box = geompy.addToStudy(box, "Box")
id_fuse1 = geompy.addToStudy(fuse1, "Fuse_1")
id_fuse2 = geompy.addToStudy(fuse2, "Fuse_2")
id_fuse3 = geompy.addToStudy(fuse3, "Fuse_3")

# display results
gg.createAndDisplayGO(id_cylinder)
gg.setDisplayMode(id_cylinder,1)
gg.createAndDisplayGO(id_sphere)
gg.setDisplayMode(id_sphere,1)
gg.createAndDisplayGO(id_box)
gg.setDisplayMode(id_box,1)
gg.createAndDisplayGO(id_fuse1)
gg.setDisplayMode(id_fuse1,1)
gg.createAndDisplayGO(id_fuse2)
gg.setDisplayMode(id_fuse2,1)
gg.createAndDisplayGO(id_fuse3)
gg.setDisplayMode(id_fuse3,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/boolean_operations_ex01.py)

## Common

```python
# Common

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create a vertex and a vector
p1 = geompy.MakeVertex(25, 55, 0)
p2 = geompy.MakeVertex( 0,  0, 0)
v = geompy.MakeVector(p1, p2)

# create a cylinder
height = 35
radius1 = 20
cylinder = geompy.MakeCylinder(p1, v, radius1, height)

# create a sphere
sphere = geompy.MakeSphereR(40)

# create a box
box = geompy.MakeBoxDXDYDZ(80, 80, 80)

# make common
common1 = geompy.MakeCommon(cylinder, sphere)
common2 = geompy.MakeCommonList([cylinder, sphere, box])

# add objects in the study
id_cylinder = geompy.addToStudy(cylinder, "Cylinder")
id_sphere = geompy.addToStudy(sphere, "Sphere")
id_box = geompy.addToStudy(box, "Box")
id_common1 = geompy.addToStudy(common1, "Common_1")
id_common2 = geompy.addToStudy(common2, "Common_2")

# display the results
gg.createAndDisplayGO(id_cylinder)
gg.setDisplayMode(id_cylinder,1)
gg.createAndDisplayGO(id_sphere)
gg.setDisplayMode(id_sphere,1)
gg.createAndDisplayGO(id_box)
gg.setDisplayMode(id_box,1)
gg.createAndDisplayGO(id_common1)
gg.setDisplayMode(id_common1,1)
gg.createAndDisplayGO(id_common2)
gg.setDisplayMode(id_common2,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/boolean_operations_ex02.py)

## Cut

```python
# Cut

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create a vertex and a vector
p1 = geompy.MakeVertex(25, 55, 0)
p2 = geompy.MakeVertex( 0,  0, 0)
v = geompy.MakeVector(p1, p2)

# create a cylinder
height = 35
radius1 = 20
cylinder = geompy.MakeCylinder(p1, v, radius1, height)

# create a sphere
sphere = geompy.MakeSphereR(40)

# create a box
box = geompy.MakeBoxDXDYDZ(80, 80, 80)

#cut
cut1 = geompy.MakeCut(cylinder, sphere)
cut2 = geompy.MakeCutList(cylinder, [sphere, box])

# add objects in the study
id_cylinder = geompy.addToStudy(cylinder, "Cylinder")
id_sphere = geompy.addToStudy(sphere, "Sphere")
id_box = geompy.addToStudy(box, "Box")
id_cut1 = geompy.addToStudy(cut1, "Cut_1")
id_cut2 = geompy.addToStudy(cut2, "Cut_2")

# display the results
gg.createAndDisplayGO(id_cylinder)
gg.setDisplayMode(id_cylinder,1)
gg.createAndDisplayGO(id_sphere)
gg.setDisplayMode(id_sphere,1)
gg.createAndDisplayGO(id_box)
gg.setDisplayMode(id_box,1)
gg.createAndDisplayGO(id_cut1)
gg.setDisplayMode(id_cut1,1) 
gg.createAndDisplayGO(id_cut2)
gg.setDisplayMode(id_cut2,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/boolean_operations_ex03.py)

## Intersection

```python
# Section

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create a vertex and a vector
p1 = geompy.MakeVertex(25, 55, 0)
p2 = geompy.MakeVertex( 0,  0, 0)
v = geompy.MakeVector(p1, p2)

# create a cylinder
height = 35
radius1 = 20
cylinder = geompy.MakeCylinder(p1, v, radius1, height)

# create a sphere
sphere = geompy.MakeSphereR(40)

# make a section
section = geompy.MakeSection(cylinder, sphere)

# add objects in the study
id_section = geompy.addToStudy(section, "Section")

# display the results
gg.createAndDisplayGO(id_section)
gg.setDisplayMode(id_section,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/boolean_operations_ex04.py)
