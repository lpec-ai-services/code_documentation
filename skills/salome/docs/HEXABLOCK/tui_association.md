<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_association.html -->

# Associations

To remove an element’s association(s):

```python
em.clearAssociation()
```

**em** can be a document:

> *clearAssociation()* remove all associations of the elements in the document.

**em** can be a vertex, an edge, a quad or a set of elements:

> in this case, *clearAssociation()* remove all associations of the given type.

GUI command: [Associations](gui_association.md#guiassocs)
