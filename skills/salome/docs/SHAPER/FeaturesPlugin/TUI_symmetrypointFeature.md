<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_symmetrypointFeature.html -->

# Symmetry through a Point of symmetry

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Cylinder_1 = model.addCylinder(Part_1_doc, model.selection("VERTEX", "PartSet/Origin"), model.selection("EDGE", "PartSet/OZ"), 5, 10)
Symmetry_1 = model.addSymmetry(Part_1_doc, [model.selection("SOLID", "Cylinder_1_1")], model.selection("VERTEX", "PartSet/Origin"), True)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/37e5f6ef0e5c16e0a2c61a73108f0eb7/symmetrypoint.py)
