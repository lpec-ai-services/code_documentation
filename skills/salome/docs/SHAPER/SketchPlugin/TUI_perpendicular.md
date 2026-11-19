<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_perpendicular.html -->

# Create Perpendicular constraint

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
SketchLine_1 = Sketch_1.addLine(13, 58, 69, 75)
SketchLine_2 = Sketch_1.addLine(12, 38, 73, 23)
SketchConstraintParallel_1 = Sketch_1.setPerpendicular(SketchLine_1.result(), SketchLine_2.result())
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/31aaa23fab2b5f7578a1e8dcbe5c4ad6/perpendicular.py)
