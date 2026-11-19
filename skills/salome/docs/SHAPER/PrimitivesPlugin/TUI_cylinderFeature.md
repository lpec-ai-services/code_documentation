<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/PrimitivesPlugin/TUI_cylinderFeature.html -->

# Create Cylinder

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Cylinder_1 = model.addCylinder(Part_1_doc, model.selection("VERTEX", "PartSet/Origin"), model.selection("EDGE", "PartSet/OZ"), 5, 10)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/e48989906652b501c2af1989f8b6ca55/cylinder1.py)
