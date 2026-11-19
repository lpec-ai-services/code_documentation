<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_groups.html -->

# Define groups on the model of blocks

Three kinds of group of meshing elements:

- group of hexahedra:

  > HexaBlocks.HexaCell
- group of quadrangles:

  > HexaBlocks.QuadCell
- group of edges:

  > HexaBlocks.EdgeCell

Four kinds of group of nodes:

- group of nodes in hexahedra:

  > HexaBlocks.HexaNode
- group of nodes in quadrangles:

  > HexaBlocks.QuadNode
- group of nodes in edges:

  > HexaBlocks.EdgeNode
- group of nodes on vertices:

  > HexaBlocks.VertexNode

Add a new group in the document:

```python
grp = doc.addHexaGroup(name)
grp = doc.addQuadGroup(name)
grp = doc.addEdgeGroup(name)
grp = doc.addQuadNodeGroup(name)
grp = doc.addHexaNodeGroup(name)
grp = doc.addEdgeNodeGroup(name)
grp = doc.addVertexNodeGroup(name)
```

Remove a group from the document:

```python
doc.removeGroup(grp)
```

Get the number of groups of the document:

```python
ng = doc.countGroup()
```

Get a group of the document:

```python
grp = doc.getGroup(index)
```

Find a group by his name in the document:

```python
g = doc.findGroup(name)
```

Get the name of a group:

```python
name = grp.getName()
```

Set the name of a group:

```python
grp.setName(name)
```

Get the kind of group among the 7 possibilities:

```python
kind = grp.getKind()
```

Add an element in a group:

```python
grp.addElement(element)
```

Get the number of elements of a group:

```python
nb = grp.countElement()
```

Get an element of a group:

```python
el = grp.getElement(index)
```

Remove an element of a group:

```python
grp.removeElement(index)
```

Clear all elements of a group:

```python
grp.clearElement()
```

GUI command: [Manage groups on the model](gui_groups.md#guigroups)
