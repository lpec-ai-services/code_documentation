<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_commonFeature.html -->

# Create Common

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Cylinder_1 = model.addCylinder(Part_1_doc,
                               model.selection("VERTEX", "PartSet/Origin"),
                               model.selection("EDGE", "PartSet/OZ"), 5, 10)
Common_1 = model.addCommon(Part_1_doc,
                           [model.selection("SOLID", "Cylinder_1_1")],
                           [model.selection("SOLID", "Box_1_1")])
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/b8d1be22c077f58b04761b7abebb0030/common.py)
