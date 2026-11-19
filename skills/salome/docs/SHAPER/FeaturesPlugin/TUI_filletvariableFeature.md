<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_filletvariableFeature.html -->

# Create Fillet by variable radius

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Fillet_1 = model.addFillet(Part_1_doc, [model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Top]")], 1, 3)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/a30802e8883511812824a104ddc8616a/fillet2.py)
