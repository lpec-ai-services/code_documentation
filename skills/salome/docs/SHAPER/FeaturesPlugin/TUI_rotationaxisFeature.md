<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_rotationaxisFeature.html -->

# Rotation by axis and angle

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Cone_1 = model.addCone(Part_1_doc, model.selection("VERTEX", "PartSet/Origin"), model.selection("EDGE", "PartSet/OZ"), 10, 5, 10)
Rotation_1 = model.addRotation(Part_1_doc, [model.selection("COMPOUND", "all-in-Cone_1")], model.selection("EDGE", "PartSet/OX"), 120)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/9f687db36985627ac46080e1f6057e1b/rotation1.py)
