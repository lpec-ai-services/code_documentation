<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_elements.html -->

# Elements

You must be careful with the signification of the word “element”, when it is used with singular or plural form :

> - The class “Element” is a basic class. The classes Vertex, Edge, Quad an Hexa inherit from the Element Class. This class is used to call common function like getName(), setName() …
> - The class “Elements” (plural) represents a set of Elements (vertices, edges, quads an hexaedras). This class is used to implements grids or result of ome complex operations (join, prism, …)

## Element

Set a name of an element:

```python
elt.setName(name)
```

Get a name of an element:

```python
elt.getName()
```

Print the name of an element:

```python
elt.printName()
```

Dump an element:

```python
elt.dump()
```

## Elements

Remove a set of elements from a document:

```python
doc.removeElements(elts)
```

Number of vertices in a set of elements:

```python
nb_vertices = elts.countVertex()
```

Number of edges in a set of elements:

```python
nb_edges = elts.countEdge()
```

Number of quads in a set of elements:

```python
nb_quads = elts.countQuad()
```

Number of hexahedrons in a set of elements:

```python
nb_hexas = elts.countHexa()
```

Get the vertex number *i*:

```python
vertex_i = elts.getVertex(i)
```

Get the edge number *i*:

```python
edge_i = elts.getEdge(i)
```

Get the quad number *i*:

```python
quad_i = elts.getQuad(i)
```

Get the hexahedron number *i*:

```python
hexa_i = elts.getHexa(i)
```

Specialized access to all vertices of a set of elements:

```python
ve_xyz = elts.getVertexIJK(i, j, k)
```

with:
:   0 <= i < ni+1, 0 <= j < nj+1, 0 <= k < nk+1

Specialized access to all edges // Vx axis:

```python
ed_a = elts.getEdgeI(i, j, k)
```

with:
:   0 <= i < ni, 0 <= j < nj+1, 0 <= k < nk+1

Specialized access to all edges // Vy axis:

```python
ed_b = elts.getEdgeJ(i, j, k)
```

with:
:   0 <= i < ni+1, 0 <= j < nj, 0 <= k < nk+1

Specialized access to all edges // Vz axis:

```python
ed_c = elts.getEdgeK(i, j, k)
```

with:
:   0 <= i < ni+1, 0 <= j < nj+1, 0 <= k < nk

Specialized access to all quadrangles // on plane Vx, Vy:

```python
qu_a = elts.getQuadIJ(i, j, k)
```

with:
:   0 <= i < ni, 0 <= j < nj, 0 <= k < nk+1

Specialized access to all quadrangles // on plane Vx, Vz:

```python
qu_b = elts.getQuadIK(i, j, k)
```

with:
:   0 <= i < ni, 0 <= j < nj+1, 0 <= k < nk

Specialized access to all quadrangles // on plane Vy, Vz:

```python
qu_c = elts.getQuadJK(i, j, k)
```

with:
:   0 <= i < ni+1, 0 <= j < nj, 0 <= k < nk

Specialized access to all hexahedra:

```python
he_xyz = elts.getHexaIJK(i, j, k)
```

with:
:   0 <= i < ni, 0 <= j < nj, 0 <= k < nk

## Cross Elements

*CrossElements* inherits *Elements*. So you have all *Elements* functions available to *CrossElements*,
plus the following functions:

*part* argument specifies the block of the *cross elements* where to search the vertex, the edge, the quad or the hexa.

Specialized access to all vertices of a set of elements:

```python
ve_xyz = elts.getVertexIJK(part, i, j, k)
```

with:
:   0 <= i < ni+1, 0 <= j < nj+1, 0 <= k < nk+1

Specialized access to all edges // Vx axis:

```python
ed_a = elts.getEdgeI(part, i, j, k)
```

with:
:   0 <= i < ni, 0 <= j < nj+1, 0 <= k < nk+1

Specialized access to all edges // Vy axis:

```python
ed_b = elts.getEdgeJ(part, i, j, k)
```

with:
:   0 <= i < ni+1, 0 <= j < nj, 0 <= k < nk+1

Specialized access to all edges // Vz axis:

```python
ed_c = elts.getEdgeK(part, i, j, k)
```

with:
:   0 <= i < ni+1, 0 <= j < nj+1, 0 <= k < nk

Specialized access to all quadrangles // on plane Vx, Vy:

```python
qu_a = elts.getQuadIJ(part, i, j, k)
```

with:
:   0 <= i < ni, 0 <= j < nj, 0 <= k < nk+1

Specialized access to all quadrangles // on plane Vx, Vz:

```python
qu_b = elts.getQuadIK(part, i, j, k)
```

with:
:   0 <= i < ni, 0 <= j < nj+1, 0 <= k < nk

Specialized access to all quadrangles // on plane Vy, Vz:

```python
qu_c = elts.getQuadJK(part, i, j, k)
```

with:
:   0 <= i < ni+1, 0 <= j < nj, 0 <= k < nk

Specialized access to all hexahedra:

```python
he_xyz = elts.getHexaIJK(part, i, j, k)
```

with:
:   0 <= i < ni, 0 <= j < nj, 0 <= k < nk
