<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_prism_join_quad.html -->

# Extrude and Join Quadrangles

There are two different methods to build hexahedra from quadrangles:

- Extrusion of quadrangles
- Join two sets of quadrangles

## Extrude a quadrangle or quadrangles

### Simple Extrude

To extrude one quad or a set of quads the following data are required:

- *quad* : the quad to be extruded (for one quad extrusion).
- *quads* : the list of quadrangles to be extruded (for multiple quads extrusion).
- *nbLayers*: the number of layers of hexahedra resulting from the extrusion.

One quad extrusion:

```python
elts = doc.extrudeQuadTop(quad, nbLayers)
```

Extrusion of a set of quads:

```python
elts = doc.extrudeQuadsTop(quads, nbLayers)
```

GUI command: [Simple Extrude](gui_prism_join_quad.md#guiextrudequadssimple)

### Uniform Extrude

The following data are required:

- *quad* : the quad to be extruded (for one quad extrusion).
- *quads* : the list of quadrangles to be extruded (for multiple quads extrusion).
- *dir* : the direction of the extrusion.
- *length* : the length of hexahedra resulting from the extrusion.
- *nbLayers*: the number of layers of hexahedra resulting from the extrusion.

One quad extrusion:

```python
elts = doc.extrudeQuadUni(quad, dir, length, nbLayers)
```

Extrusion of a set of quads:

```python
elts = doc.extrudeQuadsUni(quads, dir, length, nbLayers)
```

GUI command: [Uniform Extrude](gui_prism_join_quad.md#guiextrudequadsuniform)

### Custom Extrude

The following data are required:

- *quad* : the quad to be extruded (for one quad extrusion).
- *quads*: the list of quadrangles to be extruded (for multiple quads extrusion).
- *dir* : the direction of the extrusion.
- *th* : a list of heights (in ascendant order because the size is computed from the origin) to specify the size of each layer of extrusion.

One quad extrusion:

```python
elts = doc.extrudeQuad(quad, dir, th)
```

Extrusion of a set of quads:

```python
elts = doc.extrudeQuads(quads, dir, th)
```

GUI command: [Custom Extrude](gui_prism_join_quad.md#guiextrudequadscustom)

Operations on *elts*: [Elements](tui_elements.md#tuielements2)

### Example

```python
# -*- coding: utf-8 -*-
# Copyright (C) 2009-2026  CEA, EDF
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#

####### Test for Extrude Quad ###############

import hexablock

doc = hexablock.addDocument("Extrude Quad Test")

dimx = 11
dimy = 11
dimz = 2

orig1 = doc.addVertex ( 0,0,0)
vx    = doc.addVector ( 1,0,0)
vy    = doc.addVector ( 0,1,0)
vz    = doc.addVector ( 0,0,1)
dir1  = doc.addVector ( 1,1,1)
dir2  = doc.addVector ( 1,1,-1)

dx =1
dy=1
dz=1

grid1 = doc.makeCartesianUni (orig1, vx,vy,vz, dx,dy,dz, dimx,dimy,dimz)

mx = dimx/2
my = dimy/2
liste1 = []
liste2 = []

liste1.append(grid1.getQuadIJ (mx, my, dimz))
liste2.append(grid1.getQuadIJ (mx, my, 0))
for nx in range(dimx):
    if nx!=mx:     
        liste1.append(grid1.getQuadIJ (nx, my, dimz))
        liste2.append(grid1.getQuadIJ (nx, my, 0))

for ny in range(dimy):
    if ny!=my:
        liste1.append(grid1.getQuadIJ (mx, ny, dimz))
        liste2.append(grid1.getQuadIJ (mx, ny, 0))

tlen = []
dh0  = 1
dh   = 0.02
lh = 0
for nro in range(5):
    dh = 1.5*dh + 1
    lh += dh
    tlen.append(lh)

nbiter = 5
doc.saveVtk ("prisme1.vtk")
prisme2 = doc.extrudeQuadsUni (liste2, dir2, dh0, nbiter)
doc.saveVtk ("prisme2.vtk")

prisme1 = doc.extrudeQuads (liste1, dir1, tlen)

doc.saveVtk ("prisme3.vtk")
```

## Join quadrangle or quadrangles

### Uniform Join

The following data are required:

- *quad* : the quad to be joined and from which hexahedra will be created (one quad case).
- *quads* : the set of quadrangles to be joined and from which hexahedra will be created (multiple quad case).
- *quadDest* : a quadrangle from the set of targeted quadrangles.
- *fromPointA*: a vertex belonging to the first quadrangle of the set of quadrangles.
- *toPointA* : the target vertex (in the target quadrangle) for *fromPointA*.
- *fromPointB*: a vertex, consecutive to previous Point a, belonging to the first quadrangle.
- *toPointB* : the target vertex (in the target quadrangle) for *fromPointB*.
- *nbLayers* : number of layers of hexahedra issued from the operation.

To join one quad to an other use the function **joinQuadUni**:

```python
elts = doc.joinQuadUni(quad, quadDest, fromPointA, toPointA, fromPointB, toPointB, nbLayers)
```

To join a set of quads to another quad use the function **joinQuadsUni**:

```python
elts = doc.joinQuadsUni(quads, quadDest, fromPointA, toPointA, fromPointB, toPointB, nbLayers)
```

GUI command: [Uniform Join Quadrangles](gui_prism_join_quad.md#guijoinquadsuniform)

### Custom Join

The following data are required:

- *quad* : the quad to be joined and from which hexahedra will be created (one quad case).
- *quads* : the set of quadrangles to be joined and from which hexahedra will be created (multiple quads case).
- *quadDest* : a quadrangle from the set of targeted quadrangles.
- *fromPointA*: a vertex belonging to the first quadrangle of the set of quadrangles.
- *toPointA* : the target vertex (in the target quadrangle) for *fromPointA*.
- *fromPointB*: a vertex, consecutive to previous Point a, belonging to the first quadrangle.
- *toPointB* : the target vertex (in the target quadrangle) for *fromPointB*.
- *th* : a list of heights to specify the size of each layer of hexahedra issued from the operation.

To make a custom join of one quad to another use the function **joinQuad**:

```python
elts = doc.joinQuad(quad, quadDest, fromPointA, toPointA, fromPointB, toPointB, th)
```

To make a custom join of a set of quads to another quad use the function **joinQuads**:

```python
elts = doc.joinQuads(quads, quadDest, fromPointA, toPointA, fromPointB, toPointB, th)
```

GUI command: [Custom Join Quadrangles](gui_prism_join_quad.md#guijoinquadscustom)

Operations on *elts*: [Elements](tui_elements.md#tuielements2)

### Example

```python
# -*- coding: utf-8 -*-
# Copyright (C) 2009-2026  CEA, EDF
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#

####### Test for Join Quad ###############

import hexablock

doc = hexablock.addDocument("Join Quad Test")

dimx = 11
dimy = 11
dimz = 2

grid1 = doc.makeCartesianTop (dimx,dimy,dimz)

orig2 = doc.addVertex(dimx/2.0,0,8)
vectj = doc.addVector (0,1,0);
vecti = doc.addVector (1,0,0);
grid2 = doc.makeCylinderUni (orig2, vecti, vectj, 1.0, 2.0, 180.0, 11.0, dimz,dimy,dimx)

mx = dimx/2
my = dimy/2
prems = grid1.getQuadIJ (mx, my, dimz)
cible = grid2.getQuadJK (dimz, mx, my)

va1 = prems.getVertex (0)
va2 = prems.getVertex (1)

vb1 = cible.getVertex (1)
vb2 = cible.getVertex (2)

hauteur = 5

liste = []

liste.append(prems)
for nx in range(mx):
    if nx!=mx:
        liste.append(grid1.getQuadIJ(nx, my, dimz))

for ny in range(dimy):
    if (ny!=my):
        liste.append(grid1.getQuadIJ (mx, ny, dimz))

doc.saveVtk ("jointQuad1.vtk")
joint = doc.joinQuadsUni (liste, cible, va1,vb1,va2,vb2, hauteur)
doc.saveVtk ("jointQuad2.vtk")
```
