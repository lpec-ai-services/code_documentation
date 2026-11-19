<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/TUI_vertexFeature.html -->

# Create Vertex

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Vertex_1_objects = [model.selection("VERTEX", "[Box_1_1/Back][Box_1_1/Left][Box_1_1/Top]"), model.selection("VERTEX", "[Box_1_1/Front][Box_1_1/Left][Box_1_1/Top]"), model.selection("VERTEX", "[Box_1_1/Front][Box_1_1/Right][Box_1_1/Top]")]
Vertex_1 = model.addVertex(Part_1_doc, Vertex_1_objects)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/7e29e004478a3bc6c43e3eb961f3ee44/vertex.py)
