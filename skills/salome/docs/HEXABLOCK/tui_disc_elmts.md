<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_disc_elmts.html -->

# Disconnect elements

Disconnect a quadrangle:

```python
elts = doc.disconnectQuad(hexa, quad)
```

Disconnect an edge:

```python
elts = doc.disconnectEdge(hexa, edge)
```

Disconnect edges:

```python
elts =  doc.disconnectEdges(hexas, edges)
```

Disconnect a vertex:

```python
elts = doc.disconnectVertex(hexa, ver)
```

Operations on *elts*… [Elements](tui_elements.md#tuielements2)

GUI command: [Disconnect elements](gui_disc_elmts.md#guidisconnectelements)
