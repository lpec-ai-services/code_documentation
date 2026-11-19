<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_topological_geom_objs_page.html -->

# Topological Objects

## Creation of an Edge

```python
# Creation of an Edge

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

#
# create edge by two points
#

# create vertices
p0   = geompy.MakeVertex(0.  , 0.  , 0.  )
pxyz = geompy.MakeVertex(100., 100., 100.)

# create an edge
edge = geompy.MakeEdge(p0, pxyz)

# add object in the study
id_edge = geompy.addToStudy(edge,"Edge_1")

# display an edge
gg.createAndDisplayGO(id_edge) 

#
# create edge from wire
#

# create a circle
c = geompy.MakeCircle(None, None, 100)

# create a wire
w = geompy.MakeWire([c], 1e-07)

# create an edge from wire
edge = geompy.MakeEdgeWire(w)

# add object in the study
id_edge = geompy.addToStudy(edge,"Edge_2")

# display an edge
gg.createAndDisplayGO(id_edge) 

#
# create edge from existing curve and a length
#

# create a circle
c = geompy.MakeCircle(None, None, 100)

# create an edge of length 25.0 from the circle
edge = geompy.MakeEdgeOnCurveByLength(c, 25.0)

# add object in the study
id_edge = geompy.addToStudy(edge,"Edge_3")

# display an edge
gg.createAndDisplayGO(id_edge)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/topological_geom_objs_ex01.py)

## Creation of a Wire

```python
# Creation of a Wire

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create vertices
px   = geompy.MakeVertex(100., 0.  , 0.  )
py   = geompy.MakeVertex(0.  , 100., 0.  )
pz   = geompy.MakeVertex(0.  , 0.  , 100.)

# create a vector from two points
vxy = geompy.MakeVector(px, py)

# create an arc from three points
arc = geompy.MakeArc(py, pz, px)

# create a wire
wire = geompy.MakeWire([vxy, arc])

# add an object in the study
id_wire = geompy.addToStudy(wire,"Wire")

# display the wire
gg.createAndDisplayGO(id_wire) 

# Create a wire from edges that are not connected to each other.
# Given tolerance should cover the gaps to build connected wire.
# Three different modes to do that are possible.
gap = 1
tolerance = gap
px_gap  = geompy.MakeVertex(100. + gap, 0.  , 0.  )
py_gap  = geompy.MakeVertex(0.  , 100. + gap, 0.  )
vxy_gap = geompy.MakeVector(px_gap, py_gap)

# 1. Join edges by fixing tolerance
wire_ft = geompy.MakeWire([vxy_gap, arc], tolerance, "wire_fixed_tolerance")
# final wire tolerance will be near the half of the gap (0.5)
print(geompy.Tolerance(wire_ft)[5])
assert(abs(geompy.Tolerance(wire_ft)[5] - 0.5) < 1e-04)

# 2. Join edges by changing their underlying curves (but keeping curve types)
#    This functionality is available in TUI only.
wire_cc = geompy.MakeWireConstCurveType([vxy_gap, arc], tolerance, "wire_const_curve_type")
# final wire tolerance will stay small
print(geompy.Tolerance(wire_cc)[5])
assert(geompy.Tolerance(wire_cc)[5] < 1e-04)

# 3. Join edges by changing their underlying curves (approximating with b-splines)
#    This functionality is available in TUI only.
wire_ap = geompy.MakeWireWithMode([vxy_gap, arc], tolerance, GEOM.WBM_Approximation, "wire_approximated_curves")
# final wire tolerance will stay small
print(geompy.Tolerance(wire_ap)[5])
assert(geompy.Tolerance(wire_ap)[5] < 1e-04)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/topological_geom_objs_ex02.py)

## Creation of a Face

```python
# Creation of a Face

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create vertices
p0   = geompy.MakeVertex(0.  , 0.  , 0.  )
px   = geompy.MakeVertex(100., 0.  , 0.  )
py   = geompy.MakeVertex(0.  , 100., 0.  )
pz   = geompy.MakeVertex(0.  , 0.  , 100.)
pxyz = geompy.MakeVertex(100., 100., 100.)

# create a vector from two points
vxy = geompy.MakeVector(px, py)

# create an arc from three points
arc = geompy.MakeArc(py, pz, px)

# create a wire
wire = geompy.MakeWire([vxy, arc])

# create sketchers
sketcher1 = geompy.MakeSketcher("Sketcher:F -100 -100:TT 250 -100:R 0:C 100 150:R 0:L 300:WW",
                                [100,0,0, 1,1,1, -1,1,0])
sketcher2 = geompy.MakeSketcher("Sketcher:F 0 0:TT 70 0:TT 70 70:TT 0 70:WW")
sketcher3 = geompy.MakeSketcher("Sketcher:F 20 20:TT 50 20:TT 50 50:TT 20 50:WW")
isPlanarFace = 1

sphere = geompy.MakeSphereR(100)
box = geompy.MakeBoxDXDYDZ(200, 200, 200)
cut = geompy.MakeCutList(sphere, [box], True)

# create a face from the wire
face1 = geompy.MakeFace(wire, isPlanarFace)

# create faces from two wires
face2 = geompy.MakeFaceWires([wire, sketcher1],isPlanarFace)
face3 = geompy.MakeFaces([sketcher2, sketcher3],isPlanarFace)
face4 = geompy.MakeFaceFromSurface(face1, sketcher1)

# create face from edges with constraints
face5 = geompy.MakeFaceWithConstraints([geompy.GetSubShape(cut, [5]), geompy.GetSubShape(cut, [3]), 
                                        geompy.GetSubShape(cut, [11]), geompy.GetSubShape(cut, [3]), 
                                        geompy.GetSubShape(cut, [13]), geompy.GetSubShape(cut, [3])])

# create circle from 3 points
pCirc1 = geompy.MakeVertex(17.274575, 63.776413, 50.610737)
pCirc2 = geompy.MakeVertex(37.5, 49.081782, 127.552826)
pCirc3 = geompy.MakeVertex(62.5, 78.471044, 50.610737)
Circle_1 = geompy.MakeCircleThreePnt(pCirc1, pCirc2, pCirc3)
listE = []
listE.append(Circle_1)

# create list of points
listV = []
pV1 = geompy.MakeVertex(64.694631, 85.225425, 64.54915)
listV.append(pV1)
pV2 = geompy.MakeVertex(11.528956, 67.95085, 95.45085)
listV.append(pV2)
pV3 = geompy.MakeVertex(36.233192, 82.369878, 102.699525)
listV.append(pV3)
pV4 = geompy.MakeVertex(35.305369, 85.225425, 64.54915)
listV.append(pV4)
pV5 = geompy.MakeVertex(50, 75.355339, 115.355339)
listV.append(pV5)

# create face from edges and points 
face6 = geompy.MakeWrappedFace(listE, listV, 1e-5)

# add objects in the study
id_face1 = geompy.addToStudy(face1,"Face1")
id_face2 = geompy.addToStudy(face2,"Face2")
id_face3 = geompy.addToStudy(face3,"Face3")
id_face4 = geompy.addToStudy(face4,"Face4")
id_face5 = geompy.addToStudy(face5,"Face5")
id_face6 = geompy.addToStudy(face5,"Face6")

# display the faces
gg.createAndDisplayGO(id_face1)
gg.setDisplayMode(id_face1,1)
gg.setTransparency(id_face1,0.2)
gg.createAndDisplayGO(id_face2)
gg.setDisplayMode(id_face2,1)
gg.setTransparency(id_face2,0.2)
gg.createAndDisplayGO(id_face3)
gg.setDisplayMode(id_face3,1)
gg.setTransparency(id_face3,0.2) 
gg.createAndDisplayGO(id_face4)
gg.setDisplayMode(id_face4,1)
gg.setTransparency(id_face4,0.2)
gg.createAndDisplayGO(id_face5)
gg.setDisplayMode(id_face5,1)
gg.setTransparency(id_face5,0.2)
gg.createAndDisplayGO(id_face6)
gg.setDisplayMode(id_face6,1)
gg.setTransparency(id_face6,0.2)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/topological_geom_objs_ex03.py)

## Creation of a Shell

```python
# Creation of a Shell

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

#create vertices
p0   = geompy.MakeVertex( 0.,  0.,  0.)
pxyz = geompy.MakeVertex( 5.,  5., 40.)

# create sketchers
sketcher1 = geompy.MakeSketcher("Sketcher:F 0 0:TT 70 0:TT 70 70:TT 0 70:WW")
sketcher2 = geompy.MakeSketcher("Sketcher:F 20 20:TT 50 20:TT 50 50:TT 20 50:WW")
isPlanarFace = 1

# create a face from two wires
face = geompy.MakeFaces([sketcher1, sketcher2],isPlanarFace)

# create a prism
prism = geompy.MakePrism(face, p0, pxyz)

# explode the prism into faces
prism_faces = geompy.SubShapeAllSortedCentres(prism, geompy.ShapeType["FACE"])

# create a shell from a set of faces
shell = geompy.MakeShell([prism_faces[0], prism_faces[2], prism_faces[3],
                          prism_faces[7], prism_faces[9]])

# add objects in the study
id_shell = geompy.addToStudy(shell,"Shell")

# display the shell
gg.createAndDisplayGO(id_shell)
gg.setDisplayMode(id_shell,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/topological_geom_objs_ex04.py)

## Creation of a Solid

```python
# Creation of a Solid

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

#create vertices
p0 = geompy.MakeVertex( 0.,  0.,  0.)
pz = geompy.MakeVertex( 0.,  0., 40.)

# create sketchers
sketcher = geompy.MakeSketcher("Sketcher:F -50 -50:TT 100 -50:R 0:C 50 70:R 0:L 100:WW")

# create faces from two wires
face = geompy.MakeFace(sketcher,1)

# create a prism
prism = geompy.MakePrism(face, p0, pz)

# explode the prism into faces
prism_faces = geompy.SubShapeAllSortedCentres(prism, geompy.ShapeType["FACE"])

# create a shell from a set of faces
shell = geompy.MakeShell([prism_faces[0], prism_faces[1],
                          prism_faces[3], prism_faces[4],
                          prism_faces[5], prism_faces[2]])

# create a solid, bounded by the given shells
solid = geompy.MakeSolid([shell])

# add objects in the study
id_solid = geompy.addToStudy(solid,"Solid")

# display the solid
gg.createAndDisplayGO(id_solid)
gg.setDisplayMode(id_solid,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/topological_geom_objs_ex05.py)

## Creation of a Solid from the set of connected faces

```python
# Creation of a Solid(s) from connected faces

import salome
salome.salome_init()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create a box 
box = geompy.MakeBoxDXDYDZ(200, 200, 200)

# make a copy of a box translated by X coordinate
box_translation = geompy.MakeTranslation(box, 200, 0, 0)

# extract shells from boxes
box_shell = geompy.SubShapeAllSorted(box, geompy.ShapeType["SHELL"])[0]
box_translation_shell = geompy.SubShapeAllSorted(box_translation, geompy.ShapeType["SHELL"])[0]

# extract faces from boxes 
box_faces = geompy.SubShapeAllSorted(box, geompy.ShapeType["FACE"])
box_translation_faces = geompy.SubShapeAllSorted(box_translation, geompy.ShapeType["FACE"])

# create solids from shells
msf_shells_noint = geompy.MakeSolidFromConnectedFaces([box_shell, box_translation_shell],0)
msf_shells_int = geompy.MakeSolidFromConnectedFaces([box_shell, box_translation_shell], 1)

# create solids from faces
msf_faces_noint = geompy.MakeSolidFromConnectedFaces(box_faces+box_translation_faces, 0)
msf_faces_int = geompy.MakeSolidFromConnectedFaces(box_faces+box_translation_faces, 1)

# add objects in the study
id_solid_shells_noint = geompy.addToStudy(msf_shells_noint,"Solid_from_shells_no_intersect")
id_solid_shells_int = geompy.addToStudy(msf_shells_int,"Solid_from_shells_intersect")
id_solid_faces_noint = geompy.addToStudy(msf_faces_noint,"Solid_from_faces_no_intersect")
id_solid_faces_int = geompy.addToStudy(msf_faces_int,"Solid_from_faces_intersect")

# display the results
gg.createAndDisplayGO(id_solid_shells_noint)
gg.setDisplayMode(id_solid_shells_noint,1) 
gg.createAndDisplayGO(id_solid_shells_int)
gg.setDisplayMode(id_solid_shells_int,1) 
gg.createAndDisplayGO(id_solid_faces_noint)
gg.setDisplayMode(id_solid_faces_noint,1) 
gg.createAndDisplayGO(id_solid_faces_int)
gg.setDisplayMode(id_solid_faces_int,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/topological_geom_objs_ex07.py)

## Creation of a Compound

```python
# Creation of a Compound

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create a vertex and a vector
p1 = geompy.MakeVertex(  -30.,  -30.,  50.)
p2 = geompy.MakeVertex(  -60.,  -60.,  30.)
p3 = geompy.MakeVertex(  -30.,  -30.,  10.)

# create an arc from three points
arc = geompy.MakeArc(p1, p2, p3)
ShapeListCompound = []
i = 0
while i <= 3 :
    S = geompy.MakeTranslation(arc, i * 50., 0., 0.)
    ShapeListCompound.append(S)
    i = i + 1

# create a compound of the given shapes
compound = geompy.MakeCompound(ShapeListCompound)

# add object in the study
id_compound = geompy.addToStudy(compound,"Compound")

# display the compound
gg.createAndDisplayGO(id_compound)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/topological_geom_objs_ex06.py)
