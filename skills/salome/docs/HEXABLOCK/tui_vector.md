<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_vector.html -->

# Vector

Add a vector in the document:

```python
vector_1 = doc.addVector(dx, dy, dz)
vector_2 = doc.addVectorVertices(vertex_1, vertex_2)
```

Get the values of a vector:

```python
dx = vector_1.getDX()
dy = vector_1.getDY()
dz = vector_1.getDZ()
```

Get the number of vector in the document:

```python
sum = doc.countVector()
```

Get a vector of the document:

```python
vector_i = doc.getVector(i)
```

Get the norm of a vector:

```python
norm = vector_i.getNorm()
```

Get the angle on X:

```python
angle = vector_i.getAngleX()
```

More operations: *Vector* inherits [Element](tui_elements.md#tuielement).

GUI command: [Vector](gui_vector.md#guivector)
