<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_document.html -->

# Document

Give the name of a document:

```python
name = doc.getName()
```

Set the name of a document:

```python
doc.setName(name)
```

Save a document in a “XML” file:

```python
doc.save(filename)
```

Save the model of blocks of a document in a “VTK” file:

```python
doc.saveVtk(filename)
```

Set the tolerance need to find element:

```python
doc.setTolerance(0.0001)
```

Get the tolerance:

```python
tol = doc.getTolerance()
```

Set Debug level (long):

```python
doc.setLevel(debug_level)
```

Removes elements of type Quad Edge or Vertex not belonging to an Hexa:

```python
doc.purge()
```

Associate a shape to the document:

```python
doc.setShape(shape)
```

Gets the shape associated to the document:

```python
doc.getShape()
```

Gets the Brep associated to the document:

```python
doc.getBrep()
```

GUI command: [Document](gui_document.md#guidocument)
