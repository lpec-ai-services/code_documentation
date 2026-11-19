<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_horizontal.html -->

# Create Horizontal constraint

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
SketchLine_1 = Sketch_1.addLine(14.5, 16.0, 71.0, 62.0)
SketchConstraintHorizontal_1 = Sketch_1.setHorizontal(SketchLine_1.result())
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/96d58e9707bd587fbd1c06129a1ac496/horizontal.py)
