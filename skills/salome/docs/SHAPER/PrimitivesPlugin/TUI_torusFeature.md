<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/PrimitivesPlugin/TUI_torusFeature.html -->

# Create Torus

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Torus_1 = model.addTorus(Part_1_doc, model.selection("VERTEX", "PartSet/Origin"), model.selection("EDGE", "PartSet/OZ"), 15, 3)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/2787737f450ec421ec91a70303366f46/torus.py)
