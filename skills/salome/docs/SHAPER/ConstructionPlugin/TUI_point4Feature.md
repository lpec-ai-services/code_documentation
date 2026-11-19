<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ConstructionPlugin/TUI_point4Feature.html -->

# Create Point by intersection

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Axis_4 = model.addAxis(Part_1_doc, model.selection("VERTEX", "[Box_1_1/Back][Box_1_1/Left][Box_1_1/Bottom]"), model.selection("VERTEX", "[Box_1_1/Front][Box_1_1/Right][Box_1_1/Top]"))
Axis_5 = model.addAxis(Part_1_doc, model.selection("VERTEX", "[Box_1_1/Back][Box_1_1/Right][Box_1_1/Bottom]"), model.selection("VERTEX", "[Box_1_1/Front][Box_1_1/Left][Box_1_1/Top]"))
Point_2 = model.addPoint(Part_1_doc, model.selection("EDGE", "Axis_1"), model.selection("EDGE", "Axis_2"))
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/219e992e7aeb5db572d0a888cf1e6b37/point4.py)
