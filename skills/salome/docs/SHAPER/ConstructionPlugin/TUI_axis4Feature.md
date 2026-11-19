<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ConstructionPlugin/TUI_axis4Feature.html -->

# Create Axis by cylinder

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Cylinder_1 = model.addCylinder(Part_1_doc, model.selection("VERTEX", "PartSet/Origin"), model.selection("EDGE", "PartSet/OZ"), 5, 10)
Axis_4 = model.addAxis(Part_1_doc, model.selection("FACE", "Cylinder_1_1/Face_1"))
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/d55d9e1a490c87ca4344ab76e092ced9/axis4.py)
