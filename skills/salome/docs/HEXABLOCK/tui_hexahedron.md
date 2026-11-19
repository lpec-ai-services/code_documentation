<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_hexahedron.html -->

# Hexahedron

Manage the hexahedral of the document.

Add an hexahedron in the document:

```python
hexa_1 = doc.addHexa(q_A, q_B, q_C, q_D, q_E, q_F)

hexa_2 = doc.addHexaVertices(ACE, ACF, ADE, ADF, BCE, BCF, BDE, DBF)
```

Notice: the arguments follow the convention explain in [Appendix: naming rule to find elements in an hexahedron](annexe.md#annexe)

Get the number of all hexahedra of the document:

```python
sum_a = doc.countHexa()
```

Get an hexahedron of the document:

```python
hexa_i = doc.getHexa(i)
```

Get a vertex of an hexahedron:

```python
vertex_i = hexa_i.getVertex(i)
```

Get an edge of an hexahedron:

```python
edge_i = hexa_i.getEdge(i)
```

Get a quad of an hexahedron:

```python
quad_i = hexa_i.getQuad(i)
```

Get the number of used hexahedrons in the model of blocks:

```python
nb_used_hexa = doc.countUsedHexa()
```

Get the hexahedrons used by the model of blocks

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

used_hexas = []

for i in range( doc.countUsedHexa() ):
    hexa_i = doc.getUsedHexa(i)
    used_hexas.append(hexa_i)
```

Find an hexahedron in the document:

```python
hexa = doc.findHexa(vertex_1, vertex_2)
```

Add an hexahedron with 5 quads:

```python
doc.addHexa5Quads (qa, qc, qd, qe, qf)
```

Add an hexahedron with 4 quads:

```python
doc.addHexa4Quads (qa, qd, qe, qf)
```

Add an hexahedron with 3 quads:

```python
doc.addHexa3Quads (qa, qd, qe)
```

Add an hexahedron with 2 quads:

```python
doc.addHexa2Quads (qa, qb)
```

More operations: *Hexa* inherits [Element](tui_elements.md#tuielement).

GUI command: [Hexahedron](gui_hexahedron.md#guihexahedron)
