<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_asso_quad_to_geom.html -->

# Associate the model of blocks to the geometry

## Elements association

Associate to a vertex of the geometry:

```python
vx.setAssociation(geom_object_vertex)
```

Get the association:

```python
gov = vx.getAssociation()
```

Associate to an edge or a wire of the geometry:

```python
l = edg.addAssociation(geom_object_1D, debut, val)
```

Get the associations:

```python
edge_associations = edg.getAssociations()
```

Associate to a face or a shell of the geometry:

```python
l = quad.addAssociation(geom_object_2D)
```

Give the association:

```python
go2d = quad.getAssociations()
```

## Associate by lines

To associate an opened line to the geometry, the following data have
to be mentioned:

- the starting edge of the model of blocks: *mstart*
- the list of edges of the model of blocks: *mline*
- the starting edge of the geometry: *gstart*
- the curvilinear abscissa on the starting edge of the geometry: *pstart* (double)
- the list of edges of the geometry: *gline*
- the curvilinear abscissa on the last edge of the geometry: *pend*

The number of edges of the model of blocks to associate may be
different from the number of edges of the geometry.

Associate an opened line:

```python
l = doc.associateOpenedLine(mstart, mline, gstart, pstart, gline, pend)
```

To associate a closed line to the geometry, the following data have
to be mentioned:

- the starting vertex of the model of blocks: *mfirst*
- the starting edge of the model of blocks: *mstart*
- the list of edges of the model of blocks: *mline*
- the starting edge of the geometry: *gstart*
- the curvilinear abscissa on the starting edge of the geometry: *pstart* (double)
- the list of edges of the geometry: *gline*

The number of edges of the model of blocks to associate may be
different from the number of edges of the geometry.

Associate a closed line:

```python
l = doc.associateClosedLine(mfirst, mstart, mline, gstart, pstart, gline)
```

## Note for face association

Face association (implicite or explicite) is not necessary for:

- planar faces,
- cylindrical faces,
- conical faces.

Only edges association (implicite) on segments or arcs of cirle is necessary.

The following example show a model of block on which there isn’t faces association but only
implicite edges association on arcs of circle.

### Example

```python
# -*- coding: latin-1 -*-
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

import hexablock

doc  = hexablock.addDocument ("test_cone")

orig = doc.addVertex (0, 0, 0)
ori2 = doc.addVertex (0, 0, 10)
vz   = doc.addVector (0, 0, 1)
vx   = doc.addVector (1 ,0, 0)

rad1   = 2.0
rad2   = 1.0
height = 5.0
angle  = 270.0
hollow = False

nr = 2
na = 8
nl = 1

c1 = doc.makeCylindrical (orig, vx,vz, rad1, angle, height, nr,na,nl, hollow)
c2 = doc.makeCylindrical (ori2, vx,vz, rad2, angle, height, nr,na,nl, hollow)

vh0 = c2.getVertexIJK (0, 0, 0)
vh1 = c2.getVertexIJK (1, 0, 0)

vb0 = c1.getVertexIJK (0, 0, nl)
vb1 = c1.getVertexIJK (1, 0, nl)

qcible = c2.getQuadIJ (0, 0, 0)
qliste = []
for ni in range (nr) :
    for nj in range (na) :
        quad = c1.getQuadIJ (ni, nj, nl)
        qliste.append (quad)

## Join quads to make a cone between the 2 cylinders
doc.joinQuads  (qliste, qcible, vb0, vh0, vb1, vh1, 1)

### -------------------- Mesh 
law = doc.addLaw ("Uniform", 4)

for np in range(doc.countPropagation()):
    propa = doc.getPropagation (np)
    propa.setLaw (law) 

mesh_hexas = hexablock.mesh(doc)
```

### Result

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/cone_mesh.png)

**Cone mesh**

GUI command: [Associate the model of blocks to the geometry](gui_asso_quad_to_geom.md#guiassoquadtogeom)
