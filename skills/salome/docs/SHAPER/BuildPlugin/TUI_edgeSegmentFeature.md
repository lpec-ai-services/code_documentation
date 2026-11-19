<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/TUI_edgeSegmentFeature.html -->

# Create Edge by Points

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Edge_1 = model.addEdge(Part_1_doc, model.selection("VERTEX", "[Box_1_1/Back][Box_1_1/Right][Box_1_1/Top]"),
                                   model.selection("VERTEX", "[Box_1_1/Front][Box_1_1/Right][Box_1_1/Bottom]"))
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/14ef231254fc81b524d0ffc7425a59d9/segment.py)
