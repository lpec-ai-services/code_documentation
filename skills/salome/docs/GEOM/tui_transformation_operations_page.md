<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_transformation_operations_page.html -->

# Transformation Operations

## Translation

```python
# Translation

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create a vertex and a vector
p1 = geompy.MakeVertex(10, 40, 0)
p2 = geompy.MakeVertex( 0,  0, 50)
p3 = geompy.MakeVertex(50, 80, 0)
v = geompy.MakeVector(p1, p2)
vt = geompy.MakeVector(p1, p3)

# create a cylinder
height = 35
radius1 = 20
cylinder = geompy.MakeCylinder(p1, v, radius1, height)

# translate the given object along the vector, specified by its end points
# (all three functions produce the same result)
translation1 = geompy.MakeTranslationTwoPoints(cylinder, p1, p3)
translation2 = geompy.MakeTranslation(cylinder, 40, 40, 0)
translation3 = geompy.MakeTranslationVector(cylinder, vt)
translation4 = geompy.MakeTranslationVectorDistance(cylinder, vt, 200)

# add objects in the study
id_cylinder = geompy.addToStudy(cylinder, "Cylinder")
id_translation1 = geompy.addToStudy(translation1, "Translation1")
id_translation2 = geompy.addToStudy(translation2, "Translation2")
id_translation3 = geompy.addToStudy(translation3, "Translation3")
id_translation4 = geompy.addToStudy(translation4, "Translation4")

# display the results
gg.createAndDisplayGO(id_cylinder)
gg.setDisplayMode(id_cylinder,1)
gg.createAndDisplayGO(id_translation1)
gg.setDisplayMode(id_translation1,1)
gg.createAndDisplayGO(id_translation2)
gg.setDisplayMode(id_translation2,1)
gg.createAndDisplayGO(id_translation3)
gg.setDisplayMode(id_translation3,1) 
gg.createAndDisplayGO(id_translation4)
gg.setDisplayMode(id_translation4,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/transformation_operations_ex01.py)

## Rotation

```python
# Rotation

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
import math
gg = salome.ImportComponentGUI("GEOM")

# create a vertex and a vector
p1 = geompy.MakeVertex(10, 40,  0)
p2 = geompy.MakeVertex( 0,  0, 50)
p3 = geompy.MakeVertex(10, 50,-20)
p4 = geompy.MakeVertex(10, 50, 60)
v = geompy.MakeVector(p1, p2)
vr = geompy.MakeVector(p3, p4)

# create a cylinder
height = 35
radius1 = 20
cylinder = geompy.MakeCylinder(p1, v, radius1, height)

# rotate the given object around the given axis by the given angle
rotation1 = geompy.MakeRotation(cylinder, vr, math.pi)
rotation2 = geompy.MakeRotationThreePoints(cylinder, p4, p1, p2)

# add objects in the study
id_vr = geompy.addToStudy(vr, "Rotation 1 axis")
id_p4 = geompy.addToStudy(p4, "Rotation 2 center")
id_p1 = geompy.addToStudy(p1, "Rotation 2 point 1")
id_p2 = geompy.addToStudy(p2, "Rotation 2 point 2")
id_cylinder = geompy.addToStudy(cylinder, "Cylinder")
id_rotation1 = geompy.addToStudy(rotation1, "Rotation 1")
id_rotation2 = geompy.addToStudy(rotation2, "Rotation 2")

# display the results
gg.createAndDisplayGO(id_vr)
gg.createAndDisplayGO(id_p4)
gg.createAndDisplayGO(id_p1)
gg.createAndDisplayGO(id_p2)
gg.createAndDisplayGO(id_cylinder)
gg.setDisplayMode(id_cylinder,1)
gg.createAndDisplayGO(id_rotation1)
gg.createAndDisplayGO(id_rotation2)
gg.setDisplayMode(id_rotation1,1)
gg.setDisplayMode(id_rotation2,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/transformation_operations_ex02.py)

## Modify Location

```python
# Modify Location

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
import math
gg = salome.ImportComponentGUI("GEOM")

# create a vertex and a vector
p1 = geompy.MakeVertex(10, 40, 0)
p2 = geompy.MakeVertex( 0,  0, 50)
v = geompy.MakeVector(p1, p2)

# create a cylinder
height = 35
radius1 = 20
cylinder = geompy.MakeCylinder(p1, v, radius1, height)
circle   = geompy.MakeCircle(p2, v, radius1)

# create local coordinate systems
cs1 = geompy.MakeMarker( 0, 0, 0, 1,0,0, 0,1,0)
cs2 = geompy.MakeMarker(30,40,40, 1,0,0, 0,1,0)

# modify the location of the given object
position = geompy.MakePosition(cylinder, cs1, cs2)
position2 = geompy.PositionAlongPath(position, circle, 0.75, 1, 1)

# add objects in the study
id_cs1 = geompy.addToStudy(cs1, "Coordinate system 1")
id_cs2 = geompy.addToStudy(cs2, "Coordinate system 2")
id_cylinder = geompy.addToStudy(cylinder, "Cylinder")
id_circle = geompy.addToStudy(circle, "Circle")
id_position = geompy.addToStudy(position, "Position")
id_position2 = geompy.addToStudy(position2, "PositionAlongPath")

# display the results
gg.createAndDisplayGO(id_cylinder)
gg.setDisplayMode(id_cylinder,1)
gg.createAndDisplayGO(id_position)
gg.setDisplayMode(id_position,1)
gg.createAndDisplayGO(id_circle)
gg.setDisplayMode(id_circle,1)
gg.createAndDisplayGO(id_position2)
gg.setDisplayMode(id_position2,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/transformation_operations_ex03.py)

## Mirror Image

```python
# Mirror Image

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create a box
box = geompy.MakeBoxDXDYDZ(200, 200, 200)

# create an object, symmetrical to another object through the given plane
p1 = geompy.MakeVertex( 0, 25,  0)
p2 = geompy.MakeVertex( 5, 25,  0)
p3 = geompy.MakeVertex( 0,-30, 40)
plane = geompy.MakePlaneThreePnt(p1, p2, p3, 1000.)
mirror1 = geompy.MakeMirrorByPlane(box, plane)

# create an object, symmetrical to another object through the given axis
p4 = geompy.MakeVertex( 210, 210, -20)
p5 = geompy.MakeVertex( 210, 210, 220)
axis = geompy.MakeVector(p4, p5)
mirror2 = geompy.MakeMirrorByAxis(box, axis)

# create an object, symmetrical to another object through the given point
mirror3 = geompy.MakeMirrorByPoint(box, p4)

# add objects in the study
id_box = geompy.addToStudy(box, "Box")
id_plane = geompy.addToStudy(plane, "Plane")
id_mirror1 = geompy.addToStudy(mirror1, "Mirror plane")
id_axis = geompy.addToStudy(axis, "Axis")
id_mirror2 = geompy.addToStudy(mirror2, "Mirror axis")
id_p4 = geompy.addToStudy(p4, "Point")
id_mirror3 = geompy.addToStudy(mirror3, "Mirror point")

# display the results
gg.createAndDisplayGO(id_box)
gg.setDisplayMode(id_box,1)
gg.createAndDisplayGO(id_plane)
gg.createAndDisplayGO(id_mirror1)
gg.setDisplayMode(id_mirror1,1)
gg.createAndDisplayGO(id_axis)
gg.createAndDisplayGO(id_mirror2)
gg.setDisplayMode(id_mirror2,1)
gg.createAndDisplayGO(id_p4)
gg.createAndDisplayGO(id_mirror3)
gg.setDisplayMode(id_mirror3,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/transformation_operations_ex04.py)

## Scale Transform

```python
# Scale Transform

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create a box and a sphere
box = geompy.MakeBoxDXDYDZ(200, 200, 200)

# scale the given object by the factor
p0 = geompy.MakeVertex(100, 100, 100)
factor = 0.5
scale = geompy.MakeScaleTransform(box, p0, factor)

# add objects in the study
id_box = geompy.addToStudy(box, "Box")
id_scale = geompy.addToStudy(scale, "Scale")

# display the results
gg.createAndDisplayGO(id_box)
gg.setDisplayMode(id_box,1)
gg.setTransparency(id_box,0.5)
gg.createAndDisplayGO(id_scale)
gg.setDisplayMode(id_scale,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/transformation_operations_ex05.py)

## Offset Surface

```python
# Offset Surface

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create a box and a sphere
box = geompy.MakeBox(20, 20, 20, 200, 200, 200)

# create a new object as offset of the given object
offset  = geompy.MakeOffset(box, 70.)
offset2 = geompy.MakeOffsetIntersectionJoin(box, 70.)
offset3 = geompy.MakeOffsetPartial(box, 70., [13, 33])

# add objects in the study
id_box = geompy.addToStudy(box, "Box")
id_offset = geompy.addToStudy(offset, "Offset")
id_offset2 = geompy.addToStudy(offset2, "Offset_intersection_join")
id_offset3 = geompy.addToStudy(offset3, "Offset_Partial")

# display the results
gg.createAndDisplayGO(id_box)
gg.setDisplayMode(id_box,1)
gg.createAndDisplayGO(id_offset)
gg.createAndDisplayGO(id_offset2)
gg.createAndDisplayGO(id_offset3)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/transformation_operations_ex06.py)

## Projection

```python
# Projection

import salome
salome.salome_init_without_session()
from salome.geom import geomBuilder
geompy = geomBuilder.New()

# create a cylindric face and a curve(edge)
cylinder = geompy.MakeCylinderRH(100, 300)
[face_cyl] = geompy.SubShapes(cylinder, [3])

p1 = geompy.MakeVertex(200, 0, 100)
p2 = geompy.MakeVertex(200, 80, 100)
p3 = geompy.MakeVertex(200, 80, 180)
p4 = geompy.MakeVertex(130, 80, 180)
p5 = geompy.MakeVertex(90, 80, 240)

curve = geompy.MakeInterpol([p1, p2, p3, p4, p5], False, False)

# create a new object as projection of the
# given curve on the given cylindric face
projection = geompy.MakeProjection(curve, face_cyl)

# add objects in the study
geompy.addToStudy(cylinder, "cylinder")
geompy.addToStudyInFather(cylinder, face_cyl, "face_cyl")
geompy.addToStudy(curve, "curve")
geompy.addToStudy(projection, "projection")

#projection of point on wire
e1 = geompy.MakeLineTwoPnt(p1, p2)
e2 = geompy.MakeLineTwoPnt(p2, p3)

w1 = geompy.MakeWire([e1, e2], 1.e-7)
v1 = geompy.MakeVertex(300, 40, 100)

prj = geompy.MakeProjection(v1, w1)
geompy.addToStudy(w1, "w1")
geompy.addToStudy(v1, "v1")
geompy.addToStudy(prj, "projOnWire")

#projection of a wire on cylinder
pp1 = geompy.MakeVertex(100, 200, 0)
pp2 = geompy.MakeVertex(100, 200, 80)
pp3 = geompy.MakeVertex(100, 220, 90)
pp4 = geompy.MakeVertex(100, 130, 80)
pp5 = geompy.MakeVertex(100, 90, 80)
cc1 = geompy.MakeInterpol([pp1, pp2, pp3, pp4, pp5], True, False)
ww1 = geompy.MakeWire([cc1], 1.e-7)
vx = geompy.MakeVectorDXDYDZ(100, 0, 0)
pln1 = geompy.MakePlane(pp1, vx, 200)
face1 = geompy.MakeFaceFromSurface(pln1, ww1)
prj_cyl = geompy.MakeProjectionOnCylinder(face1, 100)

geompy.addToStudy(face1, "pln_face")
geompy.addToStudy(prj_cyl, "projOnCylinder")
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/transformation_operations_ex07.py)

## Multi Translation

```python
# Multi Translation

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create vertices and vectors
p0  = geompy.MakeVertex( 0.,  0.,  0.)
px  = geompy.MakeVertex(20.,  0.,  0.)
py  = geompy.MakeVertex( 0., 20.,  0.)
pz  = geompy.MakeVertex( 0.,  0., 20.)
pxy = geompy.MakeVertex( 50., 0., 0.)
pxyz = geompy.MakeVertex( 50., 50., 50.)
vz  = geompy.MakeVector(p0, pz)
vxy = geompy.MakeVector(px, py)
vtr1d = geompy.MakeVector(p0, pxyz)
vtr2d = geompy.MakeVector(p0, pxy)

# create an arc
arc = geompy.MakeArc(py, pz, px)

# create a wire
wire = geompy.MakeWire([vxy, arc])

# create a planar face
face = geompy.MakeFace(wire, 1)

# create a prism
prism = geompy.MakePrismVecH(face, vz, 20.0)

# translate the given object along the given vector a given number of times
tr1d = geompy.MakeMultiTranslation1D(prism, vtr1d, 20, 4)

# consequently apply two specified translations to the object a given number of times
tr2d = geompy.MakeMultiTranslation2D(prism, vtr1d, 20, 4, vtr2d, 80, 3)

# add objects in the study
id_prism = geompy.addToStudy(prism,"Prism")
id_tr1d = geompy.addToStudy(tr1d,"Translation 1D")
id_tr2d = geompy.addToStudy(tr2d,"Translation 2D")

# display the prism and the results of fillet operation
gg.createAndDisplayGO(id_prism)
gg.setDisplayMode(id_prism,1)
gg.createAndDisplayGO(id_tr1d)
gg.setDisplayMode(id_tr1d,1)
gg.createAndDisplayGO(id_tr2d)
gg.setDisplayMode(id_tr2d,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/transformation_operations_ex08.py)

## Multi Rotation

```python
# Multi Rotation

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")
import math

# create vertices and vectors
p0  = geompy.MakeVertex( 0.,  0.,  0.)
px  = geompy.MakeVertex(20.,  0.,  0.)
py  = geompy.MakeVertex( 0., 20.,  0.)
pz  = geompy.MakeVertex( 0.,  0., 20.)
pxyz = geompy.MakeVertex( 50., 50., 10.)
vz  = geompy.MakeVector(p0, pz)
vxy = geompy.MakeVector(px, py)
vrot = geompy.MakeVector(p0, pxyz)

# create an arc
arc = geompy.MakeArc(py, pz, px)

# create a wire
wire = geompy.MakeWire([vxy, arc])

# create a planar face
face = geompy.MakeFace(wire, 1)

# create a prism
prism = geompy.MakePrismVecH(face, vz, 20.0)

# 1. Rotate the prism around the axis vrot 4 times

# rotation angle = 2 * PI / 4
rot1da = geompy.MultiRotate1DNbTimes(prism, vrot, 4)

# by the given angle of 30 degrees
rot1db = geompy.MultiRotate1DByStep(prism, vrot, math.pi/6., 4)

# 2. Rotate the prism around the axis vrot 4 times
#    and translate the result of each rotation 5 times on distance 50

# rotation angle = 2 * PI / 4
rot2da = geompy.MultiRotate2DNbTimes(prism, vrot, 4, 50, 5)

# by the given angle of 60 degrees
rot2db = geompy.MultiRotate2DByStep(prism, vrot, math.pi/3., 4, 50, 5)

# add objects in the study
id_prism = geompy.addToStudy(prism,"Prism")
id_rot1da = geompy.addToStudy(rot1da,"Rotation 1D Nb.Times")
id_rot1db = geompy.addToStudy(rot1db,"Rotation 1D By Step")
id_rot2da = geompy.addToStudy(rot2da,"Rotation 2D Nb.Times")
id_rot2db = geompy.addToStudy(rot2db,"Rotation 2D By Step")

# display the prism and the results of fillet operation
gg.createAndDisplayGO(id_prism)
gg.setDisplayMode(id_prism,1)
gg.createAndDisplayGO(id_rot1da)
gg.setDisplayMode(id_rot1da,1)
gg.createAndDisplayGO(id_rot1db)
gg.setDisplayMode(id_rot1db,1)
gg.createAndDisplayGO(id_rot2da)
gg.setDisplayMode(id_rot2da,1) 
gg.createAndDisplayGO(id_rot2db)
gg.setDisplayMode(id_rot2db,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/transformation_operations_ex09.py)

## Fillet 2D

```python
# Fillet 2D

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create a face in OXY plane
face = geompy.MakeFaceHW(100, 100, 1)
fillet2d = geompy.MakeFillet2D(face, 30, [7, 9])

# add objects in the study
id_face  = geompy.addToStudy(face,"Face_1")
id_fillet2d  = geompy.addToStudy(fillet2d,"Fillet 2D_1")

# display disks
gg.createAndDisplayGO(id_face)
gg.createAndDisplayGO(id_fillet2d)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/transformation_operations_ex10.py)

## Fillet 1D

```python
# Fillet 1D

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create box
Box_1 = geompy.MakeBoxDXDYDZ(200, 200, 200)
# take box edges to create custom complex wire
[Edge_1,Edge_2,Edge_3,Edge_4,Edge_5,Edge_6,Edge_7,Edge_8,Edge_9,Edge_10,Edge_11,Edge_12] = geompy.SubShapeAllSortedCentres(Box_1, geompy.ShapeType["EDGE"])
# create wire
Wire_1 = geompy.MakeWire([Edge_12, Edge_7, Edge_11, Edge_6, Edge_1,Edge_4])
# make fillet at given wire vertices with giver radius
Fillet_1D_1 = geompy.MakeFillet1D(Wire_1, 55, [3, 4, 6, 8, 10])

id_Wire_1 = geompy.addToStudy(Wire_1, "Wire_1")
id_Fillet_1D_1= geompy.addToStudy(Fillet_1D_1, "Fillet_1D_1")

# display disks
gg.createAndDisplayGO(id_Wire_1)
gg.createAndDisplayGO(id_Fillet_1D_1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/transformation_operations_ex11.py)

## Fillet

```python
# Fillet

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")
radius  = 10.
ShapeTypeEdge = geompy.ShapeType["EDGE"]

# create vertices and vectors
p0  = geompy.MakeVertex(  0.,   0.,   0.)
px  = geompy.MakeVertex(100.,   0.,   0.)
py  = geompy.MakeVertex(  0., 100.,   0.)
pz  = geompy.MakeVertex(  0.,   0., 100.)
vz  = geompy.MakeVector(p0, pz)
vxy = geompy.MakeVector(px, py)

# create an arc
arc = geompy.MakeArc(py, pz, px)

# create a wire
wire = geompy.MakeWire([vxy, arc])

# create a planar face
face = geompy.MakeFace(wire, 1)

# create a prism
prism = geompy.MakePrismVecH(face, vz, 100.0)

# get the list of IDs (IDList) for the fillet
prism_edges = geompy.SubShapeAllSortedCentres(prism, ShapeTypeEdge)
IDlist_e = []
IDlist_e.append(geompy.GetSubShapeID(prism, prism_edges[0]))
IDlist_e.append(geompy.GetSubShapeID(prism, prism_edges[1]))
IDlist_e.append(geompy.GetSubShapeID(prism, prism_edges[2]))

# make a fillet on the specified edges of the given shape
fillet = geompy.MakeFillet(prism, radius, ShapeTypeEdge, IDlist_e)

# make a fillet on all edges of the given shape
filletall = geompy.MakeFilletAll(prism, radius)

# add objects in the study
id_prism = geompy.addToStudy(prism,"Prism")
id_fillet = geompy.addToStudy(fillet,"Fillet")
id_filletall = geompy.addToStudy(filletall,"Fillet all")

# display the prism and the results of fillet operation
gg.createAndDisplayGO(id_prism)
gg.setDisplayMode(id_prism,1)
gg.createAndDisplayGO(id_fillet)
gg.setDisplayMode(id_fillet,1)
gg.createAndDisplayGO(id_filletall)
gg.setDisplayMode(id_filletall,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/transformation_operations_ex12.py)

## Chamfer

```python
# Chamfer

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")
d1 = 10.
d2 = 10.
ShapeTypeFace = geompy.ShapeType["FACE"]

# create vertices and vectors
p0  = geompy.MakeVertex(  0.,   0.,   0.)
px  = geompy.MakeVertex(100.,   0.,   0.)
py  = geompy.MakeVertex(  0., 100.,   0.)
pz  = geompy.MakeVertex(  0.,   0., 100.)
vz  = geompy.MakeVector(p0, pz)
vxy = geompy.MakeVector(px, py)

# create an arc
arc = geompy.MakeArc(py, pz, px)

# create a wire
wire = geompy.MakeWire([vxy, arc])

# create a planar face
face = geompy.MakeFace(wire, 1)

# create a prism
prism = geompy.MakePrismVecH(face, vz, 100.0)

# get the list of IDs (IDList) for the chamfer
prism_faces = geompy.SubShapeAllSortedCentres(prism, ShapeTypeFace)
f_ind_1 = geompy.GetSubShapeID(prism, prism_faces[0])
f_ind_2 = geompy.GetSubShapeID(prism, prism_faces[1])
IDlist_f = [f_ind_1, f_ind_2]

# perform a chamfer on the edges common to the specified faces
chamfer_e = geompy.MakeChamferEdge(prism, d1, d2, f_ind_1, f_ind_2)

# perform a chamfer on all edges of the specified faces
chamfer_f = geompy.MakeChamferFaces(prism, d1, d2, IDlist_f)
chamfer_f1 = geompy.MakeChamfer(prism, d1, d2, ShapeTypeFace, IDlist_f)

# perform a symmetric chamfer on all edges of the given shape
chamfer_all = geompy.MakeChamferAll(prism, d1)

# add objects in the study
id_prism = geompy.addToStudy(prism,"Prism")
id_chamfer_e = geompy.addToStudy(chamfer_e,"Chamfer edge")
id_chamfer_f = geompy.addToStudy(chamfer_f,"Chamfer faces")
id_chamfer_f1 = geompy.addToStudy(chamfer_f1,"Chamfer faces 1")
id_chamfer_all = geompy.addToStudy(chamfer_all,"Chamfer all")

# display the prism and the results of chamfer operation
gg.createAndDisplayGO(id_prism)
gg.setDisplayMode(id_prism,1)
gg.createAndDisplayGO(id_chamfer_e)
gg.setDisplayMode(id_chamfer_e,1)
gg.createAndDisplayGO(id_chamfer_f)
gg.setDisplayMode(id_chamfer_f,1)
gg.createAndDisplayGO(id_chamfer_f1)
gg.setDisplayMode(id_chamfer_f1,1)
gg.createAndDisplayGO(id_chamfer_all)
gg.setDisplayMode(id_chamfer_all,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/transformation_operations_ex13.py)

## Extend Edge and Face

```python
# Extend Edge and Face

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create vertices
p1 = geompy.MakeVertex(  0.,     0.,   0.)
p2 = geompy.MakeVertex(100.,   100.,   0.)
p3 = geompy.MakeVertex(  0.,   100.,   0.)

# create edges
edge1 = geompy.MakeEdge(p1, p2)
edge2 = geompy.MakeCircleR(100)

# create faces
face1   = geompy.MakePlaneThreePnt(p1, p2, p3, 200)
sphere1 = geompy.MakeSpherePntR(p1, 100)
faces2  = geompy.SubShapeAllSorted(sphere1, GEOM.FACE)
face2   = faces2[0]

# perform edge extension
resEdge1 = geompy.ExtendEdge(edge1,  0.2,  0.8)
resEdge2 = geompy.ExtendEdge(edge1, -0.3,  1.3)
resEdge3 = geompy.ExtendEdge(edge2,  0.5,  1)
resEdge4 = geompy.ExtendEdge(edge2,  0.2,  0.5)

# perform face extension
resFace1 = geompy.ExtendFace(face1, 0.2, 0.8, -0.3, 1.3)
resFace2 = geompy.ExtendFace(face1, 0,   0.5,  1,   2)
resFace3 = geompy.ExtendFace(face2, 0.2, 0.8,  0.3, 0.7)
resFace4 = geompy.ExtendFace(face2, 0.5, 1,    0.5, 1)

# add objects in the study
id_edge1    = geompy.addToStudy(edge1,    "Edge 1")
id_edge2    = geompy.addToStudy(edge2,    "Edge 2")
id_face1    = geompy.addToStudy(face1,    "Face 1")
id_face2    = geompy.addToStudy(face2,    "Face 2")
id_resEdge1 = geompy.addToStudy(resEdge1, "Extended Edge 1")
id_resEdge2 = geompy.addToStudy(resEdge2, "Extended Edge 1")
id_resEdge3 = geompy.addToStudy(resEdge3, "Extended Edge 2")
id_resEdge4 = geompy.addToStudy(resEdge4, "Extended Edge 3")
id_resFace1 = geompy.addToStudy(resFace1, "Extended Face 1")
id_resFace2 = geompy.addToStudy(resFace2, "Extended Face 2")
id_resFace3 = geompy.addToStudy(resFace3, "Extended Face 3")
id_resFace4 = geompy.addToStudy(resFace4, "Extended Face 4")

# display the prism and the results of chamfer operation
gg.createAndDisplayGO(id_edge1)
gg.setDisplayMode(id_edge1, 1)
gg.createAndDisplayGO(id_edge2)
gg.setDisplayMode(id_edge2, 1)
gg.createAndDisplayGO(id_face1)
gg.setDisplayMode(id_face1, 1)
gg.createAndDisplayGO(id_face2)
gg.setDisplayMode(id_face2, 1)
gg.createAndDisplayGO(id_resEdge1)
gg.setDisplayMode(id_resEdge1, 1) 
gg.createAndDisplayGO(id_resEdge2)
gg.setDisplayMode(id_resEdge2, 1)
gg.createAndDisplayGO(id_resEdge3)
gg.setDisplayMode(id_resEdge3, 1)
gg.createAndDisplayGO(id_resEdge4)
gg.setDisplayMode(id_resEdge4, 1)
gg.createAndDisplayGO(id_resFace1)
gg.setDisplayMode(id_resFace1, 1)
gg.createAndDisplayGO(id_resFace2)
gg.setDisplayMode(id_resFace2, 1) 
gg.createAndDisplayGO(id_resFace3)
gg.setDisplayMode(id_resFace3, 1)
gg.createAndDisplayGO(id_resFace4)
gg.setDisplayMode(id_resFace4, 1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/transformation_operations_ex14.py)
