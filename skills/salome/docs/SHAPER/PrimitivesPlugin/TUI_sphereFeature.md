<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/PrimitivesPlugin/TUI_sphereFeature.html -->

# Create Sphere

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sphere_1 = model.addSphere(Part_1_doc, model.selection("VERTEX", "PartSet/Origin"), 10)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/af9856fd07f25f05bb9a77ed68709236/sphere1.py)
