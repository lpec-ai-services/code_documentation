<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_filletfixedFeature.html -->

# Create Fillet by fixed radius

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Fillet_1_objects = [model.selection("EDGE", "[Box_1_1/Left][Box_1_1/Top]"), model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Top]"), model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Left]")]
Fillet_1 = model.addFillet(Part_1_doc, Fillet_1_objects, 2)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/771c758f5328ccd6ef04cf7ad0fbbbc4/fillet1.py)
