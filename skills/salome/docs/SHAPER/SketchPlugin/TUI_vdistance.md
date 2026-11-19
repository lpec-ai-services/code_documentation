<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_vdistance.html -->

# Create Vertical Distance constraint

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
SketchCircle_1 = Sketch_1.addCircle(24.1, 24.5, 18.2)
SketchLine_1 = Sketch_1.addLine(62.3, 85.1, 91.2, 56.4)
SketchConstraintDistanceVertical_1 = Sketch_1.setVerticalDistance(SketchCircle_1.center(), SketchLine_1.startPoint(), 75.5)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/88c178c9f39eff1a20255c3410c68ff7/vdistance.py)
