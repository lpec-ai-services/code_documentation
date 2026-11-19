<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/TUI_edgeFeature.html -->

# Create Edge

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Edge_1 = model.addEdge(Part_1_doc, [model.selection("EDGE", "[Box_1_1/Left][Box_1_1/Top]")])
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/d976e432e42cd25b11eff5bdb5f58845/edge.py)
