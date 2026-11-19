<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_modify_elmts.html -->

# Modify elements by transforming elements

Translate and Rotate for any kind of elements:

```python
doc.performTranslation(elements, vec)
doc.performRotation(elements, ver, vec, angle)
doc.performScale (elements, destination_point, k)
```

Operations on *elts*: [Elements](tui_elements.md#tuielements2)

GUI command: [Modify elements by transforming elements](gui_modify_elmts.md#guimodifyelements)
