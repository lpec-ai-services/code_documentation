<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_discret_law.html -->

# Define a law of discretization

Add a new law of discretization in the document:

```python
law_1 = doc.addLaw(name, nb_nodes)
```

Add laws on propagations based on min or max segment length:

```python
hexablock.addLaws(doc, lg, lgmax)
```

Get the number of the law in the document:

```python
nl = doc.countLaw()
```

Get a law of the document:

```python
law_i = doc.getLaw(i)
```

Remove a law from the document:

```python
doc.removeLaw(law_1)
```

Find a law of discretization in the document:

```python
law_1 = doc.findLaw(name)
```

Get the name of the law:

```python
name = law_1.getName()
```

Change the name of the law:

```python
law_1.setName(name)
```

Get the number of nodes for the law of discretization:

```python
nb = law_1.getNodes()
```

Set the number of nodes for the law of discretization:

```python
law_1.setNodes(nb)
```

Get the kind of the law (uniform, arithmetic, geometric):

```python
kd = law_1.getKind()
```

Set the kind of law of discretization:

```python
law_1.setKind(kind)
```

Get the coefficient of the law:

```python
coef = law_1.getCoefficient()
```

Set the coefficient of the law:

```python
law_1.setCoefficent(coef)
```

Get the default law. This law is applied when there is no law on a propagation:

```python
default_law = doc.getLaw(0)
```

It is possible to change the default law:

```python
default_law.setNodes(10)
```

And the default law is not removable

GUI command: [Manage discretization laws](gui_discret_law.md#guidiscretelaw)
