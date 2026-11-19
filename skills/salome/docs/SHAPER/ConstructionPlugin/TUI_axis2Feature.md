<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ConstructionPlugin/TUI_axis2Feature.html -->

# Create Axis by points

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Point_2 = model.addPoint(Part_1_doc, 10, 0, 0)
Point_3 = model.addPoint(Part_1_doc, 0, 10, 10)
Axis_4 = model.addAxis(Part_1_doc, model.selection("VERTEX", "Point_1"), model.selection("VERTEX", "Point_2"))
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/5c40a2d6d027a97032efeaf50d8cd446/axis2.py)
