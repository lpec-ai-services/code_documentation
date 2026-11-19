<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/tui_measurements.html -->

# Measurements

## Minimum Distance

```python
# Minimum Distance

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create and mesh two boxes

p1 = geom_builder.MakeVertex(10.0, 10.0, 10.0)
p2 = geom_builder.MakeVertex(20.0, 20.0, 20.0)
p3 = geom_builder.MakeVertex(30.0, 40.0, 50.0)
p4 = geom_builder.MakeVertex(70.0, 100.0, 200.0)

box1 = geom_builder.MakeBoxTwoPnt(p1, p2)
box2 = geom_builder.MakeBoxTwoPnt(p3, p4)

mesh1 = smesh_builder.Mesh(box1, 'box1')
mesh1.Segment().NumberOfSegments(2)
mesh1.Triangle().MaxElementArea(10)

mesh2 = smesh_builder.Mesh(box2, 'box2')
mesh2.Segment().NumberOfSegments(5)
mesh2.Triangle().MaxElementArea(20)

if not mesh1.Compute(): raise Exception("Error when computing Mesh")
if not mesh2.Compute(): raise Exception("Error when computing Mesh")

# compute min distance from grp1 to the origin (not available yet)
smesh_builder.MinDistance(mesh1)

# compute min distance from node 10 of mesh1 to the origin
smesh_builder.MinDistance(mesh1, id1=10)
# ... or
mesh1.MinDistance(10)

# compute min distance between nodes 10 and 20 of mesh1
smesh_builder.MinDistance(mesh1, id1=10, id2=20)
# ... or
mesh1.MinDistance(10, 20)

# compute min distance from element 100 of mesh1 to the origin (not available yet)
smesh_builder.MinDistance(mesh1, id1=100, isElem1=True)
# ... or
mesh1.MinDistance(100, isElem1=True)

# compute min distance between elements 100 and 200 of mesh1 (not available yet)
smesh_builder.MinDistance(mesh1, id1=100, id2=200, isElem1=True, isElem2=True)
# ... or
mesh1.MinDistance(100, 200, True, True)

# compute min distance from element 100 to node 20 of mesh1 (not available yet)
smesh_builder.MinDistance(mesh1, id1=100, id2=20, isElem1=True)
# ... or
mesh1.MinDistance(100, 20, True)

# compute min distance from mesh1 to mesh2 (not available yet)
smesh_builder.MinDistance(mesh1, mesh2)

# compute min distance from node 10 of mesh1 to node 20 of mesh2
smesh_builder.MinDistance(mesh1, mesh2, 10, 20)

# compute min distance from node 10 of mesh1 to element 200 of mesh2 (not available yet)
smesh_builder.MinDistance(mesh1, mesh2, 10, 200, isElem2=True)

# etc...
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/e1bf1987a7126546efe509bf0843e44d/measurements_ex01.py)

## Bounding Box

```python
# Bounding Box

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create and mesh two boxes

p1 = geom_builder.MakeVertex(10.0, 10.0, 10.0)
p2 = geom_builder.MakeVertex(20.0, 20.0, 20.0)
p3 = geom_builder.MakeVertex(30.0, 40.0, 50.0)
p4 = geom_builder.MakeVertex(70.0, 100.0, 200.0)

box1 = geom_builder.MakeBoxTwoPnt(p1, p2)
box2 = geom_builder.MakeBoxTwoPnt(p3, p4)

mesh1 = smesh_builder.Mesh(box1, 'box1')
mesh1.Segment().NumberOfSegments(2)
mesh1.Triangle().MaxElementArea(10)

mesh2 = smesh_builder.Mesh(box2, 'box2')
mesh2.Segment().NumberOfSegments(5)
mesh2.Triangle().MaxElementArea(20)

if not mesh1.Compute(): raise Exception("Error when computing Mesh")
if not mesh2.Compute(): raise Exception("Error when computing Mesh")

# compute bounding box for mesh1
mesh1.BoundingBox()

# compute bounding box for list of nodes of mesh2
mesh2.BoundingBox([363, 364, 370, 371, 372, 373, 379, 380, 381])

# compute bounding box for list of elements of mesh2
mesh2.BoundingBox([363, 364, 370, 371, 372, 373, 379, 380, 381], isElem=True)

# compute common bounding box of mesh1 and mesh2
smesh_builder.BoundingBox([mesh1, mesh2])

# etc...
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/0989e78c949c182c77e25fa0d1b02cb8/measurements_ex02.py)

## Basic Properties

```python
# Basic Properties

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a box
box = geom_builder.MakeBoxDXDYDZ(100,100,100)
face = geom_builder.SubShapeAllSorted(box, geom_builder.ShapeType['FACE'])[0]

# mesh a box
mesh = smesh_builder.Mesh(box)
submesh_1d = mesh.Segment().NumberOfSegments(5)
submesh_2d = mesh.Quadrangle()
submesh_3d = mesh.Hexahedron()
submesh_2d_face = mesh.Triangle(face)
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# create a group

group_2d = mesh.Group(face)

# compute basic properties

print("Get basic properties: approach 1 (via measurements tool) ----")

measure = smesh_builder.CreateMeasurements()

print("* for mesh:")
print("  length:", measure.Length(mesh.mesh))
print("  area:",   measure.Area(mesh.mesh))
print("  volume:", measure.Volume(mesh.mesh))

print("* for group (2d):")
print("  length:", measure.Length(group_2d))
print("  area:",   measure.Area(group_2d))
print("  volume:", measure.Volume(group_2d))

print("* for submesh (2d):")
print("  length:", measure.Length(submesh_2d_face.GetSubMesh()))
print("  area:",   measure.Area(submesh_2d_face.GetSubMesh()))
print("  volume:", measure.Volume(submesh_2d_face.GetSubMesh()))

measure.UnRegister()

print("Get basic properties: approach 2 (via smeshBuilder) ----")

print("* for mesh:")
print("  length:", smesh_builder.GetLength(mesh))
print("  area:",   smesh_builder.GetArea(mesh))
print("  volume:", smesh_builder.GetVolume(mesh))

print("* for group (2d):")
print("  length:", smesh_builder.GetLength(group_2d))
print("  area:",   smesh_builder.GetArea(group_2d))
print("  volume:", smesh_builder.GetVolume(group_2d))

print("* for submesh (2d):")
print("  length:", smesh_builder.GetLength(submesh_2d_face))
print("  area:",   smesh_builder.GetArea(submesh_2d_face))
print("  volume:", smesh_builder.GetVolume(submesh_2d_face))

print("Get basic properties: approach 3 (via smeshBuilder.Mesh) ----")

print("* for mesh:")
print("  length:", mesh.GetLength())
print("  area:",   mesh.GetArea())
print("  volume:", mesh.GetVolume())

print("* for group (2d): unsupported")

print("* for submesh (2d): unsupported")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/6274b4e935fcc196bf3e9ec137746395/measurements_ex03.py)

## Angle

```python
# Angle measurement

import salome
salome.salome_init_without_session()

from salome.smesh import smeshBuilder

smesh_builder = smeshBuilder.New()

# use smeshBuilder.GetAngle() to compute angle between 3 arbitrary points

p0 = [1,0,0]
p1 = [0,0,0]
p2 = [0,1,0]

a1 = smesh_builder.GetAngle(p0, p1, p2)
print("Right angle measure", a1 )

# use Mesh.GetAngle() to compute angle between 3 nodes of a mesh

mesh = smesh_builder.Mesh()
n0 = mesh.AddNode( *p0 )
n1 = mesh.AddNode( *p1 )
n2 = mesh.AddNode( *p2 )

a2 = mesh.GetAngle( n0,n1,n2 )
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/c4096e6be3b0ac444fc86d23bd8e38cb/measurements_ex04.py)
