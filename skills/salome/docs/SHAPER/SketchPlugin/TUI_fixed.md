<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_fixed.html -->

# Create Fixed constraint

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
SketchCircle_1 = Sketch_1.addCircle(38.7, 43.3, 29.29)
SketchConstraintRigid_1 = Sketch_1.setFixed(SketchCircle_1.results()[1])
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/856e69ffc07991e0a8cc719ce2e4d6cf/fixed.py)
