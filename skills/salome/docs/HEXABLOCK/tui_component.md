<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_component.html -->

# Component

Acces to HexaBlock component in python language:

```python
import hexablock
```

Add a new empty document in the session:

```python
doc = hexablock.addDocument(name)
```

Add a new document loaded from a *xml* file:

```python
doc2 = hexablock.loadDocument(filename)
```

Get the number of opened document in the session:

```python
nd = hexablock.countDocument()
```

Get the document number *i*:

```python
doc_i = hexablock.getDocument(i)
```

Remove a document in the session:

```python
hexablock.removeDocument(doc_i)
```

Get a document from the current study:

```python
doc = hexablock.getFromStudy(doc_entry)
```

Add a document in the current study:

```python
hexablock.addToStudy(doc)
```

A tool to dump a model of block:

```python
hexablock.dump(doc, [mesh, [full]])
```

- doc: the document to dump
- mesh: an optional mesh of this document
- full:

  - False: to have a short dump (by default)
  - True: to have a full dump

GUI command: [Component](gui_component.md#guicomponent)
