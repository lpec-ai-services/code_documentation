<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_collinear.html -->

# Create Collinear constraint

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
SketchLine_1 = Sketch_1.addLine(6, 25, 20, 40)
SketchLine_2 = Sketch_1.addLine(44, 26, 80, 61)
SketchConstraintCollinear_1 = Sketch_1.setCollinear(SketchLine_1.result(), SketchLine_2.result())
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/50eac26ddead677b97e7d434e9be694f/collinear.py)
