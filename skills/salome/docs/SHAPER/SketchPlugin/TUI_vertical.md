<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_vertical.html -->

# Create Vertical constraint

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
SketchLine_1 = Sketch_1.addLine(15.5, 14.5, 71.0, 62.8)
SketchConstraintVertical_1 = Sketch_1.setVertical(SketchLine_1.result())
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/b29c8a2bccf0b0ea88dc18cbd90d9df5/vertical.py)
