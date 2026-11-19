<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_pointFeature.html -->

# Create Sketch Point

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
SketchPoint_1 = Sketch_1.addPoint(42.6, 19.0)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/8dd7e7978a4196d20e6d1f94a016eec3/point.py)
