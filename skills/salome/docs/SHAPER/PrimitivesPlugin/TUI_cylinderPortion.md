<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/PrimitivesPlugin/TUI_cylinderPortion.html -->

# Create Portion of cylinder

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Cylinder_2 = model.addCylinder(Part_1_doc, model.selection("VERTEX", "Cylinder_1_1/Face_1&Cylinder_1_1/Face_2"), model.selection("EDGE", "PartSet/OX"), 5, 10, 45)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/6e3514a234d02061a039e8419d3d8ee5/cylinder2.py)
