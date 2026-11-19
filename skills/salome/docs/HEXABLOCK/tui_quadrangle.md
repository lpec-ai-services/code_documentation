<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_quadrangle.html -->

# Quadrangles

Manage the quadrangles of the document.

Add a quadrangle in the document:

```python
quad_1 = doc.addQuad(edge_1, edge_2, edge_3, edge_4)
quad_2 = doc.addQuadVertices(vertex_1, vertex_2, vertex_3, vertex_4)
```

Notice: the vertices and edges follow the outline of the quadrangle.

Get the number of all quadrangles of the document:

```python
sum_a = doc.countQuad()
```

Get the number of used quadrangles in the model of blocks:

```python
sum_u = doc.countUsedQuad()
```

Get the quads used by the model of blocks

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

used_quads = []

for i in range( doc.countUsedQuad() ):
    quad_i = doc.getUsedQuad(i)
    used_quads.append(quad_i)
```

Get a quadrangle of the document:

```python
quad_i = doc.getQuad(i)
```

Get an edge of a quadrangle:

```python
edge_e = quad_i.getEdge(0 or 1 or 2 or 3)
```

Get a vertex of a quadrangle:

```python
vertex_v = quad_i.getVertex(0 or 1 or 2 or 3)
```

Find a quadrangle in the document:

```python
quad_f = doc.findQuad(vertex_1, vertex_2)
```

More operations: *Quad* inherits [Element](tui_elements.md#tuielement).

GUI command: [Quadrangle](gui_quadrangle.md#guiquadrangles)
