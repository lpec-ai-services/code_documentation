<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_propag.html -->

# Discretization defined on the model of blocks

Get the number of propagation existing on the model of blocks:

```python
np = doc.countPropagation()
```

Get a propagation of the model of blocks:

```python
propa = doc.getPropagation(index)
```

Find a propagation by an edge of the model of blocks:

```python
propa = doc.findPropagation(edge)
```

Get all edges of the propagation and the way in the propagation:

```python
edges = propa.getEdges()
bo = propa.getWay()
```

Set a law of discretization for a propagation:

```python
propa.setLaw(law)
```

Get the law of the propagation for a propagation:

```python
law = propa.getLaw()
```

Set the way where the law is applied on the propagation:

```python
propa.setWay(bo)
```

GUI command: [Discretize on the propagation edges](gui_propag.md#guipropag)
