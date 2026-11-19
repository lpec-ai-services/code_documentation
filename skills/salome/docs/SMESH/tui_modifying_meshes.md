<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/tui_modifying_meshes.html -->

# Modifying Meshes

## Adding Nodes and Elements

### Add Node

```python
# Add Node

import salome
salome.salome_init_without_session()

from salome.smesh import smeshBuilder
smesh_builder = smeshBuilder.New()

mesh = smesh_builder.Mesh()

# add node
new_id = mesh.AddNode(50, 10, 0)
print("")
if new_id == 0: print("KO node addition.")
else:           print("New Node has been added with ID ", new_id)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/6e1cd90cfadc6bbe15da8a8a1311e768/modifying_meshes_ex01.py)

### Add 0D Element

```python
# Add 0D Element

import salome
salome.salome_init_without_session()

from salome.smesh import smeshBuilder
smesh_builder = smeshBuilder.New()

mesh = smesh_builder.Mesh()

# add node
node_id = mesh.AddNode(50, 10, 0)

# add 0D Element
new_id = mesh.Add0DElement(node_id)

print("")
if new_id == 0: print("KO node addition.")
else:           print("New 0D Element has been added with ID ", new_id)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/1b629b2311c6994191751923e81fb876/modifying_meshes_ex02.py)

### Add 0D Element on Element Nodes

```python
# Add 0D Element on Element Nodes

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create a geometry
box = geom_builder.MakeBoxDXDYDZ( 10, 10, 10 )
face = geom_builder.SubShapeAll( box, geom_builder.ShapeType["FACE"])[0]

# make 3D mesh
mesh = smesh_builder.Mesh( box )
mesh.AutomaticHexahedralization(0)

# create 0D elements on all nodes of the mesh
res = mesh.Add0DElementsToAllNodes( mesh )

# find 0D elements on all nodes of the mesh, all found nodes are added to a new group
groupName = "0Dmesh"
res = mesh.Add0DElementsToAllNodes( mesh, groupName )
mesh.RemoveGroupWithContents( res ) # remove all found 0D elements

# create 0D elements on all nodes of a sub-mesh, with group creation
groupName = "0Dsubmesh"
submesh = mesh.GetSubMesh( face, "faceSM")
res = mesh.Add0DElementsToAllNodes( submesh, groupName )

# create 0D elements on all nodes of a group
group = mesh.Group( face, "faceGroup" )
res = mesh.Add0DElementsToAllNodes( group )

# remove all 0D elements
mesh.RemoveElements( mesh.GetIdsFromFilter( smesh_builder.GetFilter( SMESH.ELEM0D,
                                                                     SMESH.FT_ElemGeomType,
                                                                     "=",SMESH.Geom_POINT )))

# create 0D elements on all nodes of some elements
res = mesh.Add0DElementsToAllNodes( mesh.GetElementsId() )

mesh.RemoveElements( mesh.GetElementsByType( SMESH.ELEM0D ))

# create 0D elements on some nodes
nodes = list(range(1,10))
res = mesh.Add0DElementsToAllNodes( mesh.GetIDSource( nodes, SMESH.NODE ))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/a93f4d175b426d647a7e653ad8781ce9/modifying_meshes_ex03.py)

### Add Edge

```python
# Add Edge

from mechanic import *

# add node
n1 = mesh.AddNode(50, 10, 0)
if n1 == 0: print("KO node addition.") 

# add edge
e1 = mesh.AddEdge([n1, 38])
if e1 == 0: print("KO edge addition.")
else:       print("New Edge has been added with ID ", e1)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/4756c7a2c504c2836f39b89085e55127/modifying_meshes_ex04.py)

### Add Triangle

```python
# Add Triangle

from mechanic import *

# add node
n1 = mesh.AddNode(50, 10, 0)
if n1 == 0: print("KO node addition.")

# add triangle
t1 = mesh.AddFace([n1, 38, 39])
if t1 == 0: print("KO triangle addition.")
else:       print("New Triangle has been added with ID ", t1)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/87b1b9fe4e75824cd79bc5abd1599bd4/modifying_meshes_ex05.py)

### Add Quadrangle

```python
# Add Quadrangle

from mechanic import *

# add node
n1 = mesh.AddNode(50, 10, 0)
if n1 == 0: print("KO node addition.")

n2 = mesh.AddNode(40, 20, 0)
if n2 == 0: print("KO node addition.")

# add quadrangle
q1 = mesh.AddFace([n2, n1, 38, 39])
if q1 == 0: print("KO quadrangle addition.")
else:       print("New Quadrangle has been added with ID ", q1)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/bd936f10a0cfd3b5fcc46d76ae1b06b3/modifying_meshes_ex06.py)

### Add Tetrahedron

```python
# Add Tetrahedron

from mechanic import *

# add node
n1 = mesh.AddNode(50, 10, 0)
if n1 == 0: print("KO node addition.")

# add tetrahedron
t1 = mesh.AddVolume([n1, 38, 39, 246])
if t1 == 0: print("KO tetrahedron addition.")
else:       print("New Tetrahedron has been added with ID ", t1)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/ccfb461e145c58042ea146ef689468ce/modifying_meshes_ex07.py)

### Add Hexahedron

```python
# Add Hexahedron

from mechanic import *

# add nodes
nId1 = mesh.AddNode(50, 10, 0)
nId2 = mesh.AddNode(47, 12, 0)
nId3 = mesh.AddNode(50, 10, 10)
nId4 = mesh.AddNode(47, 12, 10)

if nId1 == 0 or nId2 == 0 or nId3 == 0 or nId4 == 0: print("KO node addition.")

# add hexahedron
vId = mesh.AddVolume([nId2, nId1, 38, 39, nId4, nId3, 245, 246])
if vId == 0: print("KO Hexahedron addition.")
else:        print("New Hexahedron has been added with ID ", vId)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/4ee14a7b9e6c164c76de5c351e660df3/modifying_meshes_ex08.py)

### Add Polygon

```python
# Add Polygon

import salome
salome.salome_init_without_session()

from salome.smesh import smeshBuilder

smesh_builder = smeshBuilder.New()

# create an empty mesh structure
mesh = smesh_builder.Mesh() 

# a method to build a polygonal mesh element with <nb_vert> angles:
def MakePolygon (a_mesh, x0, y0, z0, radius, nb_vert, smesh_builder):
    import math

    al = 2.0 * math.pi / nb_vert
    node_ids = []

    # Create nodes for a polygon
    for ii in range(nb_vert):
        nid = smesh_builder.AddNode(x0 + radius * math.cos(ii*al),
                                    y0 + radius * math.sin(ii*al),
                                    z0)
        node_ids.append(nid)
        pass

    # Create a polygon
    return smesh_builder.AddPolygonalFace(node_ids)

# Create three polygons
f1 = MakePolygon(mesh, 0, 0,  0, 30, 13, smesh_builder=mesh)
f2 = MakePolygon(mesh, 0, 0, 10, 21,  9, smesh_builder=mesh)
f3 = MakePolygon(mesh, 0, 0, 20, 13,  6, smesh_builder=mesh)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/f9de69c23e86a95a363ffa95b0476007/modifying_meshes_ex09.py)

### Add Polyhedron

```python
# Add Polyhedron

import math

import salome
salome.salome_init_without_session()

from salome.smesh import smeshBuilder

smesh_builder = smeshBuilder.New()

# create an empty mesh structure
mesh = smesh_builder.Mesh()  

# Create nodes for 12-hedron with pentagonal faces
al = 2 * math.pi / 5.0
cosal = math.cos(al)
aa = 13
rr = aa / (2.0 * math.sin(al/2.0))
dr = 2.0 * rr * cosal
r1 = rr + dr
dh = rr * math.sqrt(2.0 * (1.0 - cosal * (1.0 + 2.0 * cosal)))
hh = 2.0 * dh - dr * (rr*(cosal - 1) + (rr + dr)*(math.cos(al/2) - 1)) / dh

dd = [] # top
cc = [] # below top
bb = [] # above bottom
aa = [] # bottom

for i in range(5):
    cos_bot = math.cos(i*al)
    sin_bot = math.sin(i*al)

    cos_top = math.cos(i*al + al/2.0)
    sin_top = math.sin(i*al + al/2.0)

    nd = mesh.AddNode(rr * cos_top, rr * sin_top, hh     ) # top
    nc = mesh.AddNode(r1 * cos_top, r1 * sin_top, hh - dh) # below top
    nb = mesh.AddNode(r1 * cos_bot, r1 * sin_bot,      dh) # above bottom
    na = mesh.AddNode(rr * cos_bot, rr * sin_bot,       0) # bottom
    dd.append(nd) # top
    cc.append(nc) # below top
    bb.append(nb) # above bottom
    aa.append(na) # bottom
    pass

# Create a polyhedral volume (12-hedron with pentagonal faces)
mesh.AddPolyhedralVolume([dd[0], dd[1], dd[2], dd[3], dd[4],  # top
                          dd[0], cc[0], bb[1], cc[1], dd[1],  # -
                          dd[1], cc[1], bb[2], cc[2], dd[2],  # -
                          dd[2], cc[2], bb[3], cc[3], dd[3],  # - below top
                          dd[3], cc[3], bb[4], cc[4], dd[4],  # -
                          dd[4], cc[4], bb[0], cc[0], dd[0],  # -
                          aa[4], bb[4], cc[4], bb[0], aa[0],  # .
                          aa[3], bb[3], cc[3], bb[4], aa[4],  # .
                          aa[2], bb[2], cc[2], bb[3], aa[3],  # . above bottom
                          aa[1], bb[1], cc[1], bb[2], aa[2],  # .
                          aa[0], bb[0], cc[0], bb[1], aa[1],  # .
                          aa[0], aa[1], aa[2], aa[3], aa[4]], # bottom
                         [5,5,5,5,5,5,5,5,5,5,5,5])
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/78adb83278e7fdfa08204a06a2234c43/modifying_meshes_ex10.py)

## Removing Nodes and Elements

### Removing Nodes

```python
# Removing Nodes

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create and mesh two boxes

box = geom_builder.MakeBoxDXDYDZ(10.0, 10.0, 10.0)
mesh = smesh_builder.Mesh(box, 'box')
mesh.Segment().NumberOfSegments(10)
mesh.Triangle().MaxElementArea(5)

if not mesh.Compute(): raise Exception("Error when computing Mesh")
print("After Compute(): %s nodes, %s faces" % ( mesh.NbNodes(), mesh.NbFaces()))

# remove nodes #246 and #255

res = mesh.RemoveNodes([246, 255])
print("After RemoveNodes(): %s nodes, %s faces" % ( mesh.NbNodes(), mesh.NbFaces()))

# removing node #100 with reconnection 

mesh.RemoveNodeWithReconnection( 100 )
print("After RemoveNodeWithReconnection(): %s nodes, %s faces" % ( mesh.NbNodes(), mesh.NbFaces()))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/aff931340777d781b6673724912c9419/modifying_meshes_ex11.py)

### Removing Elements

```python
# Removing Elements

from mechanic import *

# remove three elements: #850, #859 and #814
res = mesh.RemoveElements([850, 859, 814])
if res == 1: print("Elements removing is OK!")
else:        print("KO Elements removing.")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/9d43cdf3770c8e4e4ff2c338ad07dd53/modifying_meshes_ex12.py)

### Removing Orphan Nodes

```python
# Removing Orphan Nodes

from mechanic import *

# add orphan nodes
mesh.AddNode(0,0,0)
mesh.AddNode(1,1,1)
# remove just created orphan nodes
res = mesh.RemoveOrphanNodes()
if res == 1: print("Removed %d nodes!" % res)
else:        print("KO nodes removing.")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/d500144992b3b86f24fed124f049eea0/modifying_meshes_ex13.py)

## Moving Nodes

```python
# Moving Nodes

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

box = geom_builder.MakeBoxDXDYDZ(200, 200, 200)

mesh = smesh_builder.Mesh( box )
mesh.Segment().AutomaticLength(0.1)
mesh.Quadrangle()
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# find node at (0,0,0) which is located on a geom vertex
node000 = None
for vId in geom_builder.SubShapeAllIDs( box, geom_builder.ShapeType["VERTEX"]):
    if node000: break
    nodeIds = mesh.GetSubMeshNodesId( vId, True )
    for node in nodeIds:
        xyz = mesh.GetNodeXYZ( node )
        if xyz[0] == 0 and xyz[1] == 0 and xyz[2] == 0 :
            node000 = node
            pass
        pass
    pass

if not node000:
    raise Exception("node000 not found")

# find node000 using a dedicated function 
n = mesh.FindNodeClosestTo( -1,-1,-1 )
if not n == node000:
    raise Exception("FindNodeClosestTo() returns " + str( n ) + " != " + str( node000 ))

# move node000 to a new location
x,y,z = -10, -10, -10
n = mesh.MoveNode( n,x,y,z )
if not n:
    raise Exception("MoveNode() returns " + n)

# check the coordinates of the node000
xyz = mesh.GetNodeXYZ( node000 )
if not ( xyz[0] == x and xyz[1] == y and xyz[2] == z) :
    raise Exception("Wrong coordinates: " + str( xyz ) + " != " + str( [x,y,z] ))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/89037ab3bcf5808dc46168ff99a3686e/modifying_meshes_ex15.py)

## Diagonal Inversion

```python
# Diagonal Inversion

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

smesh_builder = smeshBuilder.New()

# create an empty mesh structure
mesh = smesh_builder.Mesh() 

# create the following mesh:
# .----.----.----.
# |   /|   /|   /|
# |  / |  / |  / |
# | /  | /  | /  |
# |/   |/   |/   |
# .----.----.----.

bb = [0, 0, 0, 0]
tt = [0, 0, 0, 0]
ff = [0, 0, 0, 0, 0, 0]

bb[0] = mesh.AddNode( 0., 0., 0.)
bb[1] = mesh.AddNode(10., 0., 0.)
bb[2] = mesh.AddNode(20., 0., 0.)
bb[3] = mesh.AddNode(30., 0., 0.)

tt[0] = mesh.AddNode( 0., 15., 0.)
tt[1] = mesh.AddNode(10., 15., 0.)
tt[2] = mesh.AddNode(20., 15., 0.)
tt[3] = mesh.AddNode(30., 15., 0.)

ff[0] = mesh.AddFace([bb[0], bb[1], tt[1]])
ff[1] = mesh.AddFace([bb[0], tt[1], tt[0]])
ff[2] = mesh.AddFace([bb[1], bb[2], tt[2]])
ff[3] = mesh.AddFace([bb[1], tt[2], tt[1]])
ff[4] = mesh.AddFace([bb[2], bb[3], tt[3]])
ff[5] = mesh.AddFace([bb[2], tt[3], tt[2]])

# inverse the diagonal bb[1] - tt[2]
print("\nDiagonal inversion ... ", end=' ')
res = mesh.InverseDiag(bb[1], tt[2])
if not res: print("failed!")
else:       print("done.")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/7cb9fcf718e9cadee43e2e2495b90c48/modifying_meshes_ex16.py)

## Uniting two Triangles

```python
# Uniting two Triangles

import salome
salome.salome_init_without_session()

from salome.smesh import smeshBuilder

smesh_builder = smeshBuilder.New()

# create an empty mesh structure
mesh = smesh_builder.Mesh() 

# create the following mesh:
# .----.----.----.
# |   /|   /|   /|
# |  / |  / |  / |
# | /  | /  | /  |
# |/   |/   |/   |
# .----.----.----.

bb = [0, 0, 0, 0]
tt = [0, 0, 0, 0]
ff = [0, 0, 0, 0, 0, 0]

bb[0] = mesh.AddNode( 0., 0., 0.)
bb[1] = mesh.AddNode(10., 0., 0.)
bb[2] = mesh.AddNode(20., 0., 0.)
bb[3] = mesh.AddNode(30., 0., 0.)

tt[0] = mesh.AddNode( 0., 15., 0.)
tt[1] = mesh.AddNode(10., 15., 0.)
tt[2] = mesh.AddNode(20., 15., 0.)
tt[3] = mesh.AddNode(30., 15., 0.)

ff[0] = mesh.AddFace([bb[0], bb[1], tt[1]])
ff[1] = mesh.AddFace([bb[0], tt[1], tt[0]])
ff[2] = mesh.AddFace([bb[1], bb[2], tt[2]])
ff[3] = mesh.AddFace([bb[1], tt[2], tt[1]])
ff[4] = mesh.AddFace([bb[2], bb[3], tt[3]])
ff[5] = mesh.AddFace([bb[2], tt[3], tt[2]]) 

# delete the diagonal bb[1] - tt[2]
print("\nUnite two triangles ... ", end=' ')
res = mesh.DeleteDiag(bb[1], tt[2])
if not res: print("failed!")
else:       print("done.")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/097d554a8e78b909a0f144e0d2256762/modifying_meshes_ex17.py)

## Uniting a Set of Triangles

```python
# Uniting a Set of Triangles

import salome
salome.salome_init_without_session()

import SMESH
from salome.smesh import smeshBuilder

smesh_builder = smeshBuilder.New()

# create an empty mesh structure
mesh = smesh_builder.Mesh() 

# create the following mesh:
# .----.----.----.
# |   /|   /|   /|
# |  / |  / |  / |
# | /  | /  | /  |
# |/   |/   |/   |
# .----.----.----.

bb = [0, 0, 0, 0]
tt = [0, 0, 0, 0]
ff = [0, 0, 0, 0, 0, 0]

bb[0] = mesh.AddNode( 0., 0., 0.)
bb[1] = mesh.AddNode(10., 0., 0.)
bb[2] = mesh.AddNode(20., 0., 0.)
bb[3] = mesh.AddNode(30., 0., 0.)

tt[0] = mesh.AddNode( 0., 15., 0.)
tt[1] = mesh.AddNode(10., 15., 0.)
tt[2] = mesh.AddNode(20., 15., 0.)
tt[3] = mesh.AddNode(30., 15., 0.)

ff[0] = mesh.AddFace([bb[0], bb[1], tt[1]])
ff[1] = mesh.AddFace([bb[0], tt[1], tt[0]])
ff[2] = mesh.AddFace([bb[1], bb[2], tt[2]])
ff[3] = mesh.AddFace([bb[1], tt[2], tt[1]])
ff[4] = mesh.AddFace([bb[2], bb[3], tt[3]])
ff[5] = mesh.AddFace([bb[2], tt[3], tt[2]])

# unite a set of triangles
print("\nUnite a set of triangles ... ", end=' ')
res = mesh.TriToQuad([ff[2], ff[3], ff[4], ff[5]], SMESH.FT_MinimumAngle, 60.)
if not res: print("failed!")
else:       print("done.")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/036c43b1feb406e842eb80202d08cde5/modifying_meshes_ex18.py)

## Orientation

```python
# Orientation

import salome
salome.salome_init_without_session()

from salome.smesh import smeshBuilder

smesh_builder = smeshBuilder.New()

# create an empty mesh structure
mesh = smesh_builder.Mesh() 

# build five quadrangles:
dx = 10
dy = 20

n1  = mesh.AddNode(0.0 * dx, 0, 0)
n2  = mesh.AddNode(1.0 * dx, 0, 0)
n3  = mesh.AddNode(2.0 * dx, 0, 0)
n4  = mesh.AddNode(3.0 * dx, 0, 0)
n5  = mesh.AddNode(4.0 * dx, 0, 0)
n6  = mesh.AddNode(5.0 * dx, 0, 0)
n7  = mesh.AddNode(0.0 * dx, dy, 0)
n8  = mesh.AddNode(1.0 * dx, dy, 0)
n9  = mesh.AddNode(2.0 * dx, dy, 0)
n10 = mesh.AddNode(3.0 * dx, dy, 0)
n11 = mesh.AddNode(4.0 * dx, dy, 0)
n12 = mesh.AddNode(5.0 * dx, dy, 0)

f1 = mesh.AddFace([n1, n2, n8 , n7 ])
f2 = mesh.AddFace([n2, n3, n9 , n8 ])
f3 = mesh.AddFace([n3, n4, n10, n9 ])
f4 = mesh.AddFace([n4, n5, n11, n10])
f5 = mesh.AddFace([n5, n6, n12, n11]) 

# Change the orientation of the second and the fourth faces.
mesh.Reorient([2, 4])
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/06098821763a11e08b2bf47d01309535/modifying_meshes_ex19.py)

## Cutting Quadrangles

```python
# Cutting Quadrangles

from mechanic import *

# cut two quadrangles: 405 and 406
mesh.QuadToTri([405, 406], SMESH.FT_MinimumAngle)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/846ac600d041173e728e368b5cc890c1/modifying_meshes_ex20.py)

## Cutting Triangles

```python
# Cutting Triangles

import salome
salome.salome_init_without_session()

from salome.smesh import smeshBuilder

smesh_builder = smeshBuilder.New()

# create 3 triangles and 1 segment all sharing edge 1-2
mesh = smesh_builder.Mesh()
n1 = mesh.AddNode( 0, 0, 0)
n2 = mesh.AddNode( 0, 0, -10)
n3 = mesh.AddNode( 10, 0, 0)
n4 = mesh.AddNode( 0, 10, 0)
n5 = mesh.AddNode( 0, -10, 0)
mesh.AddFace([ n1, n2, n3])
mesh.AddFace([ n1, n2, n4])
mesh.AddFace([ n1, n2, n5])
mesh.AddEdge([ n1, n2] )

# ===========================================================================
# cut all the triangles and the segment by setting a new node on the segment
# ===========================================================================

mesh.AddNodeOnSegment( n1, n2, 0.6 )
assert mesh.NbNodes() == 6     # one new node created
assert mesh.NbTriangles() == 6 # each of the 3 triangles is split into two
assert mesh.NbEdges() == 2     # a segment is split into two

# ===============================================================
# cut a triangle into three by adding a new node on the triangle
# ===============================================================

triangleID = 1
mesh.AddNodeOnFace( triangleID, 2, 0, -6 )
assert mesh.NbNodes() == 7     # one new node created
assert mesh.NbTriangles() == 8 # the triangles is split into three
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/9f25d8d2004fbeb2bf97fea48036cbb0/modifying_meshes_cut_triangles.py)

## Split Volumes into Tetrahedra

```python
# Split volumic elements into tetrahedrons

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# mesh a hexahedral mesh
box = geom_builder.MakeBoxDXDYDZ (1, 1, 1 )
mesh = smesh_builder.Mesh( box )
mesh.AutomaticHexahedralization(0)
print("Nb volumes mesh: %s" % mesh.NbHexas())

# split each hexahedron into 6 tetrahedra
mesh.SplitVolumesIntoTetra( mesh, smesh_builder.Hex_6Tet )
print("Nb volumes mesh: %s" % mesh.NbTetras())
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/90a394299f9553ec24bb2b1358be6407/modifying_meshes_split_vol.py)

## Smoothing

```python
# Smoothing

from mechanic import *

# select the top face
faces = geom_builder.SubShapeAllSorted(mechanic, geom_builder.ShapeType["FACE"])

# create a group of faces to be smoothed
group_smooth = mesh.GroupOnGeom(faces[3], "Group of faces (smooth)", SMESH.FACE)

# perform smoothing

# boolean SmoothObject(Object, IDsOfFixedNodes, MaxNbOfIterations, MaxAspectRatio, Method)
res0 = mesh.SmoothObject(group_smooth, [], 20, 2., smesh_builder.CENTROIDAL_SMOOTH)
res1 = mesh.SmoothObject(group_smooth, [], 20, 2., smesh_builder.LAPLACIAN_SMOOTH)
print("\nSmoothing ... ", end=' ')
if not (res0 and res1): print("failed!")
else:       print("done.")
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/fb06efae4bc24119913bf107a764b58f/modifying_meshes_ex21.py)

## Extrusion

```python
# Extrusion

# There is a series of Extrusion Along Line methods added at different times;
# a fully functional method is ExtrusionSweepObjects()

import math

import salome
salome.salome_init_without_session()

import SMESH
from salome.smesh import smeshBuilder

smesh_builder = smeshBuilder.New()

# create an empty mesh
mesh = smesh_builder.Mesh() 

# add a node
mesh.AddNode( 0.,0.,0. )

# extrude a node into a line of 10 segments along the X axis
ids = mesh.GetNodesId()
stepVector = [1.,0.,0.]
nbSteps = 10
mesh.ExtrusionSweep( ids, stepVector, nbSteps, IsNodes=True )

# create some groups
lastNode      = mesh.GetNodesId()[-1]
lastNodeGroup = mesh.MakeGroupByIds( "node %s"% lastNode, SMESH.NODE, [lastNode])
lineGroup     = mesh.MakeGroupByIds( "line", SMESH.EDGE, mesh.GetElementsId() )

# rotate the segments around the first node to get a mesh of a disk quarter
axisZ  = [0.,0.,0., 0.,0.,1.]
groups = mesh.RotationSweepObject( lineGroup, axisZ, math.pi/2., 10, 1e-3, MakeGroups=True, TotalAngle=True )

# extrude all faces into volumes
obj        = mesh
stepVector = [0.,0.,-1.]
nbSteps    = 5
groups = mesh.ExtrusionSweepObject2D( obj, stepVector, nbSteps, MakeGroups=True )

# remove all segments created by the last command
for g in groups:
    if g.GetType() == SMESH.EDGE:
        mesh.RemoveGroupWithContents( g )

# extrude all segments into faces along Z
obj = mesh
stepVector = [0.,0.,1.]
mesh.ExtrusionSweepObject1D( obj, stepVector, nbSteps )

# extrude a group
obj        = mesh.GetGroupByName( "line_extruded", SMESH.FACE )[0]
stepVector = [0,-5.,0.]
nbSteps    = 1
mesh.ExtrusionSweepObject( obj, stepVector, nbSteps )

# extrude all nodes and triangle faces of the disk quarter, applying a scale factor
diskGroup = mesh.GetGroupByName( "line_rotated", SMESH.FACE )[0]
crit = [ smesh_builder.GetCriterion( SMESH.FACE, SMESH.FT_ElemGeomType,'=',SMESH.Geom_TRIANGLE ),
         smesh_builder.GetCriterion( SMESH.FACE, SMESH.FT_BelongToMeshGroup,'=', diskGroup )]
trianglesFilter = smesh_builder.GetFilterFromCriteria( crit )

nodes      = [ diskGroup ]
edges      = []
faces      = [ trianglesFilter ]
stepVector = [0,0,1]
nbSteps    = 10
mesh.ExtrusionSweepObjects( nodes, edges, faces, stepVector, nbSteps, scaleFactors=[0.5], linearVariation=True )

# extrude a cylindrical group of faces by normal
cylGroup = None
for g in mesh.GetGroups( SMESH.FACE ):
    if g.GetName().startswith("node "):
        cylGroup = g
        break

elements = cylGroup
stepSize = 5.
nbSteps  = 2
mesh.ExtrusionByNormal( elements, stepSize, nbSteps )
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/4c1f20697b11135c46bbad72121a0579/modifying_meshes_ex22.py)

## Extrusion along a Path

```python
# Extrusion along a Path

import math

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# 1. Create points
points = [[0, 0], [50, 30], [50, 110], [0, 150], [-80, 150], [-130, 70], [-130, -20]]

iv = 1
vertices = []
for point in points:
    vert = geom_builder.MakeVertex(point[0], point[1], 0)
    vertices.append(vert)
    iv += 1

# 2. Create edges and wires
Edge_straight = geom_builder.MakeEdge(vertices[0], vertices[4])
Edge_bezierrr = geom_builder.MakeBezier(vertices)
Wire_polyline = geom_builder.MakePolyline(vertices)
Edge_Circle   = geom_builder.MakeCircleThreePnt(vertices[0], vertices[1], vertices[2])

geom_builder.addToStudy(Edge_straight, "Edge_straight")
geom_builder.addToStudy(Edge_bezierrr, "Edge_bezierrr")
geom_builder.addToStudy(Wire_polyline, "Wire_polyline")
geom_builder.addToStudy(Edge_Circle  , "Edge_Circle")

# 3. Explode wire on edges, as they will be used for mesh extrusion
Wire_polyline_edges = geom_builder.SubShapeAll(Wire_polyline, geom_builder.ShapeType["EDGE"])
for ii in range(len(Wire_polyline_edges)):
    geom_builder.addToStudyInFather(Wire_polyline, Wire_polyline_edges[ii], "Edge_" + repr(ii + 1))

# Mesh

# Mesh the given shape with the given 1d hypothesis
def Mesh1D(shape1d, nbSeg, name):
  mesh1d_tool = smesh_builder.Mesh(shape1d, name)
  algo = mesh1d_tool.Segment()
  hyp  = algo.NumberOfSegments(nbSeg)
  isDone = mesh1d_tool.Compute()
  if not isDone: raise Exception('Mesh %s: computation failed' % name)
  return mesh1d_tool

# Create a mesh with six nodes, seven edges and two quadrangle faces
def MakeQuadMesh2(mesh_name):
  quad_1 = smesh_builder.Mesh(name = mesh_name)
  
  # six nodes
  n1 = quad_1.AddNode(0, 20, 10)
  n2 = quad_1.AddNode(0, 40, 10)
  n3 = quad_1.AddNode(0, 40, 30)
  n4 = quad_1.AddNode(0, 20, 30)
  n5 = quad_1.AddNode(0,  0, 30)
  n6 = quad_1.AddNode(0,  0, 10)

  # seven edges
  quad_1.AddEdge([n1, n2]) # 1
  quad_1.AddEdge([n2, n3]) # 2
  quad_1.AddEdge([n3, n4]) # 3
  quad_1.AddEdge([n4, n1]) # 4
  quad_1.AddEdge([n4, n5]) # 5
  quad_1.AddEdge([n5, n6]) # 6
  quad_1.AddEdge([n6, n1]) # 7

  # two quadrangle faces
  quad_1.AddFace([n1, n2, n3, n4]) # 8
  quad_1.AddFace([n1, n4, n5, n6]) # 9
  return [quad_1, [1,2,3,4,5,6,7], [8,9]]

# Path meshes
Edge_straight_mesh = Mesh1D(Edge_straight, 7, "Edge_straight")
Edge_bezierrr_mesh = Mesh1D(Edge_bezierrr, 7, "Edge_bezierrr")
Wire_polyline_mesh = Mesh1D(Wire_polyline, 3, "Wire_polyline")
Edge_Circle_mesh   = Mesh1D(Edge_Circle  , 8, "Edge_Circle")

# Initial meshes (to be extruded)
[quad_1, ee_1, ff_1] = MakeQuadMesh2("quad_1")
[quad_2, ee_2, ff_2] = MakeQuadMesh2("quad_2")
[quad_3, ee_3, ff_3] = MakeQuadMesh2("quad_3")
[quad_4, ee_4, ff_4] = MakeQuadMesh2("quad_4")
[quad_5, ee_5, ff_5] = MakeQuadMesh2("quad_5")
[quad_6, ee_6, ff_6] = MakeQuadMesh2("quad_6")
[quad_7, ee_7, ff_7] = MakeQuadMesh2("quad_7")

# ExtrusionAlongPath
# IDsOfElements, PathMesh, PathShape, NodeStart,
# HasAngles, Angles, HasRefPoint, RefPoint
refPoint = SMESH.PointStruct(0, 0, 0)
a10 = math.radians( 10.0 )
a45 = math.radians( 45.0 )

# 1. Extrusion of two mesh edges along a straight path
error = quad_1.ExtrusionAlongPath([1,2], Edge_straight_mesh, Edge_straight, 1,
                                  0, [], 0, refPoint)

# 2. Extrusion of one mesh edge along a curved path
error = quad_2.ExtrusionAlongPath([2], Edge_bezierrr_mesh, Edge_bezierrr, 1,
                                  0, [], 0, refPoint)

# 3. Extrusion of one mesh edge along a curved path with usage of angles
error = quad_3.ExtrusionAlongPath([2], Edge_bezierrr_mesh, Edge_bezierrr, 1,
                                  1, [a45, a45, a45, 0, -a45, -a45, -a45], 0, refPoint)

# 4. Extrusion of one mesh edge along the path, which is a part of a meshed wire
error = quad_4.ExtrusionAlongPath([4], Wire_polyline_mesh, Wire_polyline_edges[0], 1,
                                  1, [a10, a10, a10], 0, refPoint)

# 5. Extrusion of two mesh faces along the path, which is a part of a meshed wire
error = quad_5.ExtrusionAlongPath(ff_5 , Wire_polyline_mesh, Wire_polyline_edges[2], 4,
                                  0, [], 0, refPoint)

# 6. Extrusion of two mesh faces along a closed path
error = quad_6.ExtrusionAlongPath(ff_6 , Edge_Circle_mesh, Edge_Circle, 1,
                                  0, [], 0, refPoint)

# 7. Extrusion of two mesh faces along a closed path with usage of angles
error = quad_7.ExtrusionAlongPath(ff_7, Edge_Circle_mesh, Edge_Circle, 1,
                                  1, [a45, -a45, a45, -a45, a45, -a45, a45, -a45], 0, refPoint)

# Make the same meshes using a fully functional method ExtrusionAlongPathObjects() having
# the following arguments:
#   Nodes, Edges, Faces, PathObject, PathShape=None,
#   NodeStart=1, HasAngles=False, Angles=[], LinearVariation=False,
#   HasRefPoint=False, RefPoint=[0,0,0], MakeGroups=False,
#   ScaleFactors=[], ScalesVariation=False

quad_1 = MakeQuadMesh2("quad_1")[0]
quad_2 = MakeQuadMesh2("quad_2")[0]
quad_3 = MakeQuadMesh2("quad_3")[0]
quad_4 = MakeQuadMesh2("quad_4")[0]
quad_5 = MakeQuadMesh2("quad_5")[0]
quad_6 = MakeQuadMesh2("quad_6")[0]
quad_7 = MakeQuadMesh2("quad_7")[0]

# 1. Extrusion of two mesh edges along a straight path
nn, ee, ff = [], [1,2], []
error = quad_1.ExtrusionAlongPathObjects( nn, ee, ff, Edge_straight_mesh )

# 2. Extrusion of one mesh edge along a curved path
nn, ee, ff = [], [2], []
error = quad_2.ExtrusionAlongPathObjects( nn, ee, ff, Edge_bezierrr_mesh )

# 3. Extrusion of one mesh edge along a curved path with usage of angles
error = quad_3.ExtrusionAlongPathObjects( nn, ee, ff, Edge_bezierrr_mesh,
                                          Angles=[a45, a45, a45, 0, -a45, -a45, -a45])

# 4. Extrusion of one mesh edge along the path, which is a part of a meshed wire
nn, ee, ff = [], [4], []
error = quad_4.ExtrusionAlongPathObjects( nn, ee, ff, Wire_polyline_mesh, Wire_polyline_edges[0],
                                          Angles=[a10, a10, a10])

# 5. Extrusion of two mesh faces along the path, which is a part of a meshed wire
nn, ee, ff = [], [], quad_5
error = quad_5.ExtrusionAlongPathObjects( nn, ee, ff, Wire_polyline_mesh, Wire_polyline_edges[2],
                                          NodeStart=4 )

# 6. Extrusion of two mesh faces along a closed path
nn, ee, ff = [], [], quad_6
error = quad_6.ExtrusionAlongPathObjects( nn, ee, ff, Edge_Circle_mesh )

# 7. Extrusion of two mesh faces along a closed path with usage of angles
nn, ee, ff = [], [], quad_7
error = quad_7.ExtrusionAlongPathObjects( nn, ee, ff, Edge_Circle_mesh, Edge_Circle,
                                          Angles=[a45, -a45, a45, -a45, a45, -a45, a45, -a45])
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/b416c1b5f10b7bbf7e06f92d01f8962e/modifying_meshes_ex23.py)

## Revolution

```python
# Revolution

import math

from mechanic import *

# create a group of faces to be revolved
FacesRotate = [492, 493, 502, 503]
GroupRotate = mesh.CreateEmptyGroup(SMESH.FACE,"Group of faces (rotate)")
GroupRotate.Add(FacesRotate)

# define revolution angle and axis
angle45 = 45 * math.pi / 180
axisXYZ = SMESH.AxisStruct(-38.3128, -73.3658, -23.321, -13.3402, -13.3265, 6.66632)

# perform revolution of an object
mesh.RotationSweepObject(GroupRotate, axisXYZ, angle45, 4, 1e-5)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/7b77ef172b604d101da6c197508c3495/modifying_meshes_ex24.py)

## Pattern Mapping

```python
# Pattern Mapping

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# define the geometry
Box_1 = geom_builder.MakeBoxDXDYDZ(200., 200., 200.)
geom_builder.addToStudy(Box_1, "Box_1")

faces = geom_builder.SubShapeAll(Box_1, geom_builder.ShapeType["FACE"])
Face_1 = faces[0]
Face_2 = faces[1]

geom_builder.addToStudyInFather(Box_1, Face_1, "Face_1")
geom_builder.addToStudyInFather(Box_1, Face_2, "Face_2")

# build a quadrangle mesh 3x3 on Face_1
Mesh_1 = smesh_builder.Mesh(Face_1)
algo1D = Mesh_1.Segment()
algo1D.NumberOfSegments(3)
Mesh_1.Quadrangle()

isDone = Mesh_1.Compute()
if not isDone: raise Exception('Mesh Mesh_1 : computation failed')

# build a triangle mesh on Face_2
Mesh_2 = smesh_builder.Mesh(Face_2)

algo1D = Mesh_2.Segment()
algo1D.NumberOfSegments(1)
algo2D = Mesh_2.Triangle()
algo2D.MaxElementArea(240)

isDone = Mesh_2.Compute()
if not isDone: raise Exception('Mesh Mesh_2 : computation failed')

# create a 2d pattern
pattern = smesh_builder.GetPattern()

isDone = pattern.LoadFromFace(Mesh_2.GetMesh(), Face_2, 0)
if (isDone != 1): print('LoadFromFace :', pattern.GetErrorCode())

# apply the pattern to a face of the first mesh
facesToSplit = Mesh_1.GetElementsByType(SMESH.FACE)
print("Splitting %d rectangular face(s) to %d triangles..."%(len(facesToSplit), 2*len(facesToSplit)))
pattern.ApplyToMeshFaces(Mesh_1.GetMesh(), facesToSplit, 0, 0)
isDone = pattern.MakeMesh(Mesh_1.GetMesh(), 0, 0)
if (isDone != 1): print('MakeMesh :', pattern.GetErrorCode())  

# create quadrangle mesh
Mesh_3 = smesh_builder.Mesh(Box_1)
Mesh_3.Segment().NumberOfSegments(1)
Mesh_3.Quadrangle()
Mesh_3.Hexahedron()
isDone = Mesh_3.Compute()
if not isDone: raise Exception('Mesh Mesh_3 : computation failed')

# create a 3d pattern (hexahedrons)
pattern_hexa = smesh_builder.GetPattern()

smp_hexa = """!!! Nb of points:
15
      0        0        0   !- 0
      1        0        0   !- 1
      0        1        0   !- 2
      1        1        0   !- 3
      0        0        1   !- 4
      1        0        1   !- 5
      0        1        1   !- 6
      1        1        1   !- 7
    0.5        0      0.5   !- 8
    0.5        0        1   !- 9
    0.5      0.5      0.5   !- 10
    0.5      0.5        1   !- 11
      1        0      0.5   !- 12
      1      0.5      0.5   !- 13
      1      0.5        1   !- 14
  !!! Indices of points of 4 elements:
  8 12 5 9 10 13 14 11
  0 8 9 4 2 10 11 6
  2 10 11 6 3 13 14 7
  0 1 12 8 2 3 13 10"""

pattern_hexa.LoadFromFile(smp_hexa)

# apply the pattern to a mesh
volsToSplit = Mesh_3.GetElementsByType(SMESH.VOLUME)
print("Splitting %d hexa volume(s) to %d hexas..."%(len(volsToSplit), 4*len(volsToSplit)))
pattern_hexa.ApplyToHexahedrons(Mesh_3.GetMesh(), volsToSplit,0,3)
isDone = pattern_hexa.MakeMesh(Mesh_3.GetMesh(), True, True)
if (isDone != 1): print('MakeMesh :', pattern_hexa.GetErrorCode())  

# create one more quadrangle mesh
Mesh_4 = smesh_builder.Mesh(Box_1)
Mesh_4.Segment().NumberOfSegments(1)
Mesh_4.Quadrangle()
Mesh_4.Hexahedron()
isDone = Mesh_4.Compute()
if not isDone: raise Exception('Mesh Mesh_4 : computation failed')

# create another 3d pattern (pyramids)
pattern_pyra = smesh_builder.GetPattern()

smp_pyra = """!!! Nb of points:
9
        0        0        0   !- 0
        1        0        0   !- 1
        0        1        0   !- 2
        1        1        0   !- 3
        0        0        1   !- 4
        1        0        1   !- 5
        0        1        1   !- 6
        1        1        1   !- 7
      0.5      0.5      0.5   !- 8
  !!! Indices of points of 6 elements:
  0 1 5 4 8
  7 5 1 3 8
  3 2 6 7 8
  2 0 4 6 8
  0 2 3 1 8
  4 5 7 6 8"""

pattern_pyra.LoadFromFile(smp_pyra)

# apply the pattern to a face mesh
volsToSplit = Mesh_4.GetElementsByType(SMESH.VOLUME)
print("Splitting %d hexa volume(s) to %d hexas..."%(len(volsToSplit), 6*len(volsToSplit)))
pattern_pyra.ApplyToHexahedrons(Mesh_4.GetMesh(), volsToSplit,1,0)
isDone = pattern_pyra.MakeMesh(Mesh_4.GetMesh(), True, True)
if (isDone != 1): print('MakeMesh :', pattern_pyra.GetErrorCode())
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/70e4565612e03074060c7dc19a452f94/modifying_meshes_ex25.py)

## Convert mesh to/from quadratic

```python
# Convert mesh to/from quadratic

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create sphere of radius 100

Sphere = geom_builder.MakeSphereR( 100 )
geom_builder.addToStudy( Sphere, "Sphere" )

# create simple tetrahedral mesh

Mesh = smesh_builder.Mesh(Sphere)
Mesh.Segment().NumberOfSegments(5)
Mesh.Triangle()
Mesh.Tetrahedron()

# compute mesh

if not Mesh.Compute(): raise Exception("Error when computing Mesh")

# convert to quadratic
# theForce3d = 1; this results in the medium node lying at the
# middle of the line segments connecting start and end node of a mesh
# element

Mesh.ConvertToQuadratic( theForce3d=1 )

# revert back to the non-quadratic mesh

Mesh.ConvertFromQuadratic()

# convert to quadratic
# theForce3d = 0; this results in the medium node lying at the
# geometrical edge from which the mesh element is built

Mesh.ConvertToQuadratic( theForce3d=0 )

# to convert not the whole mesh but a sub-mesh, provide it as 
# an additional argument to the functions:
# Mesh.ConvertToQuadratic( 0, subMesh )
# Mesh.ConvertFromQuadratic( subMesh )
#
# Note that the mesh becomes non-conformal at conversion of sub-mesh.
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/f9840972e6d731df57c2f1e83f3cc152/modifying_meshes_ex26.py)

## Split bi-quadratic into linear

```python
# Split bi-quadratic to linear

import salome
salome.salome_init_without_session()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# make a shape consisting of two quadranges
OY  = geom_builder.MakeVectorDXDYDZ(0, 1, 0)
OY1 = geom_builder.MakeTranslation( OY, 1, 0, 0 )
OY2 = geom_builder.MakeTranslation( OY, 2, 0, 0 )
q1  = geom_builder.MakeQuad2Edges( OY, OY1 )
q2  = geom_builder.MakeQuad2Edges( OY1, OY2 )

shape = geom_builder.Partition( [q1,q2], theName='shape' )
ff    = geom_builder.SubShapeAll( shape, geom_builder.ShapeType["FACE"], theName="quad" )

# mesh one quadrange with quadrangless and the other with triangles
mesh = smesh_builder.Mesh( shape )
mesh.Segment().NumberOfSegments(1)
mesh.Quadrangle()
mesh.Triangle( ff[1] )
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# make group of quadrangles and extrude them into a hexahedron
quadGroup = mesh.Group( ff[0], "quads")
mesh.ExtrusionSweepObject2D( quadGroup, [0,0,1], 1 )

# make the mesh bi-quadratic
mesh.ConvertToQuadratic( theToBiQuad=True )

# split all elements into linear ones
mesh.SplitBiQuadraticIntoLinear()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/062c400846600ff4b34273cb78d10874/split_biquad.py)

## Double nodes on groups boundaries

Double nodes on shared faces between groups of volumes and create flat elements on demand.

The list of groups must contain at least two groups. The groups have to be disjoint: no common element into two different groups.

The nodes of the internal faces at the boundaries of the groups are doubled. Optionally, the internal faces are replaced by flat elements.

Triangles are transformed into prisms, and quadrangles into hexahedrons.

The flat elements are stored in groups of volumes.

These groups are named according to the position of the group in the list:
the group j_n_p is the group of the flat elements that are built between the group #n and the group #p in the list.
If there is no shared faces between the group #n and the group #p in the list, the group j_n_p is not created.
All the flat elements are gathered into the group named “joints3D” (or “joints2D” in 2D situation).
The flat element of the multiple junctions between the simple junction are stored in a group named “jointsMultiples”.

This example represents an iron cable (a thin cylinder) in a concrete block (a big cylinder).
The big cylinder is defined by two geometric volumes.

```python
# Double nodes on groups boundaries

# This example represents an iron cable (a thin cylinder) in a concrete block (a big cylinder).
# The big cylinder is defined by two geometric volumes.

import salome
salome.salome_init_without_session()

import GEOM
import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# geometry 

O = geom_builder.MakeVertex(0, 0, 0)
OX = geom_builder.MakeVectorDXDYDZ(1, 0, 0)
OY = geom_builder.MakeVectorDXDYDZ(0, 1, 0)
OZ = geom_builder.MakeVectorDXDYDZ(0, 0, 1)
Vertex_1 = geom_builder.MakeVertex(50, 0, 0)
Cylinder_1 = geom_builder.MakeCylinder(O, OX, 10, 500)
Cylinder_2 = geom_builder.MakeCylinder(Vertex_1, OX, 100, 400)
Vertex_2 = geom_builder.MakeVertex(-200, -200, -200)
Vertex_3 = geom_builder.MakeVertex(250, 200, 200)
Box_1 = geom_builder.MakeBoxTwoPnt(Vertex_2, Vertex_3)
Fuse_1 = geom_builder.MakeFuse(Cylinder_1, Cylinder_2)
Partition_1 = geom_builder.MakePartition([Fuse_1], [Cylinder_1, Box_1], [], [], geom_builder.ShapeType["SOLID"], 0, [], 0)
[Solid_1,Solid_2] = geom_builder.GetShapesOnShape(Cylinder_1, Partition_1, geom_builder.ShapeType["SOLID"], GEOM.ST_IN)
[Solid_3,Solid_4] = geom_builder.GetShapesOnShape(Cylinder_2, Partition_1, geom_builder.ShapeType["SOLID"], GEOM.ST_IN)
Vertex_4 = geom_builder.MakeVertex(450, 0, 0)
Vertex_5 = geom_builder.MakeVertex(500, 0, 0)
Vertex_6 = geom_builder.MakeVertex(550, 0, 0)
vec1 = geom_builder.MakeVector(Vertex_4, Vertex_5)
vec2 = geom_builder.MakeVector(Vertex_5, Vertex_6)
[Face_1] = geom_builder.GetShapesOnPlane(Partition_1, geom_builder.ShapeType["FACE"], vec1, GEOM.ST_ON)
[Face_2] = geom_builder.GetShapesOnPlane(Partition_1, geom_builder.ShapeType["FACE"], vec2, GEOM.ST_ON)

# meshing (we have linear tetrahedrons here, but other elements are OK)

Mesh_1 = smesh_builder.Mesh(Partition_1)
Mesh_1.Segment().NumberOfSegments(15)
Mesh_1.Triangle().LengthFromEdges()
Mesh_1.Tetrahedron()
if not Mesh_1.Compute(): raise Exception("Error when computing Mesh")

# relevant groups of volumes and faces

Solid_1_1 = Mesh_1.GroupOnGeom(Solid_1,'Solid_1',SMESH.VOLUME)
Solid_2_1 = Mesh_1.GroupOnGeom(Solid_2,'Solid_2',SMESH.VOLUME)
Solid_3_1 = Mesh_1.GroupOnGeom(Solid_3,'Solid_3',SMESH.VOLUME)
Solid_4_1 = Mesh_1.GroupOnGeom(Solid_4,'Solid_4',SMESH.VOLUME)
Face_1_1 = Mesh_1.GroupOnGeom(Face_1,'Face_1',SMESH.FACE)
Face_2_1 = Mesh_1.GroupOnGeom(Face_2,'Face_2',SMESH.FACE)

# Building of flat elements

Mesh_1.DoubleNodesOnGroupBoundaries([Solid_1_1, Solid_2_1, Solid_3_1, Solid_4_1], 1)

Mesh_1.CreateFlatElementsOnFacesGroups([Face_1_1, Face_2_1])
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/32ff97eacf4877188ec0168dc716a805/generate_flat_elements.py)

Here, the 4 groups of volumes [Solid_1_1, Solid_2_1, Solid_3_1, Solid_4_1] constitute a partition of the mesh.
The flat elements on group boundaries and on faces are built with the
2 last lines of the code above.

If the last argument (Boolean) in DoubleNodesOnGroupBoundaries is set to 1,
the flat elements are built, otherwise, there is only a duplication of the nodes.

To observe flat element groups, save the resulting mesh on a MED file and reload it.
