<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_vertex.html -->

# Vertices

Manage the vertices of the model of blocks of a document.

Add a new vertex of the model of blocks in the document:

```python
vertex_1 = doc.addVertex(x, y, z)
```

Get the number of all vertices of the document:

```python
sum_a = doc.countVertex()
```

Get the number of vertices used only by the model of blocks:

```python
sum_u = doc.countUsedVertex()
```

Get the vertices used by the model of blocks

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

used_vertices = []

for i in range( doc.countUsedVertex() ):
    vertex_i = doc.getUsedVertex(i)
    used_vertices.append(vertex_i)
```

Get a vertex of the document:

```python
vertex_i = doc.getVertex(i)
```

Get the coordinates of a vertex:

```python
x = vertex_i.getX()
y = vertex_i.getY()
z = vertex_i.getZ()
```

Set the coordinates of a vertex:

```python
vertex_i.setX(x1)
vertex_i.setY(y1)
vertex_i.setZ(z1)
```

Find a vertex in the document (with a tolerance):

```python
vertex_f = doc.findVertex(x, y, z)
```

More operations: *Vertex* inherits [Element](tui_elements.md#tuielement).

GUI command: [Vertex](gui_vertex.md#guivertex)
