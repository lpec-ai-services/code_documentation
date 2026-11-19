<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_angularcopyFeature.html -->

# Create Angular copy

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Cylinder_1 = model.addCylinder(Part_1_doc, model.selection("VERTEX", "PartSet/Origin"), model.selection("EDGE", "PartSet/OZ"), 5, 10)
AngularCopy_1 = model.addMultiRotation(Part_1_doc, [model.selection("SOLID", "Cylinder_1_1")], model.selection("EDGE", "PartSet/OY"), 90, 3)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/58549882dc2616cd5f752d4692f089ad/angularcopy.py)
