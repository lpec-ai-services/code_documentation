<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_cyl.html -->

# Cylinder

To add a cylinder, the following data have to be mentioned:

- the coordinates of the cylinder base
- the direction of the cylinder
- height and radius of the cylinder

Add a cylinder in the document:

```python
cyl = doc.addCylinder(base, direction, radius, height)
```

Get the values of a cylinder:

```python
ver = cyl.getBase()
vec = cyl.getDirection()
r = cyl.getRadius()
h = cyl.getHeigth()
```

Access to the cylinders of the document:

```python
nc = doc.countCylinder()
cylk = doc.getCylinder(ind)
```

More operations: *Cylinder* inherits [Element](tui_elements.md#tuielement).

GUI command: [Cylinder](gui_cyl.md#guicylinder)
