<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_edge.html -->

# Edges

Manage the edges of the document.

Add an edge, defined by two vertices, in the document:

```python
edge_12 = doc.addEdge(vertex_1, vertex_2)
```

Add an edge, defined by one vertex and one vector, in the document:

```python
edge_12 = doc.addEdgeVector(vertex, vector)
```

Get the number of all edges in the document:

```python
sum_a = doc.countEdge()
```

Get the number of edges used only in the model of blocks:

```python
sum_u = doc.countUsedEdge()
```

Get the edges used by the model of blocks

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

used_edges = []

for i in range( doc.countUsedEdge() ):
    edge_i = doc.getUsedEdge(i)
    used_edges.append(edge_i)
```

Get an edge of the document:

```python
edge_i = doc.getEdge(i)
```

Get the vertices of an edge:

```python
vertex_a = edge_i.getVertex(0)
vertex_b = edge_i.getVertex(1)
```

Find an edge in the document:

```python
edge_f = doc.findEdge(vertex_1, vertex_2)
```

More operations: *Edge* inherits [Element](tui_elements.md#tuielement).

GUI command: [Edge](gui_edge.md#guiedge)
