<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_angle.html -->

# Create Angle constraint

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
SketchLine_1 = Sketch_1.addLine(55.1, 13.0, 6.42, 35.5)
SketchLine_2 = Sketch_1.addLine(50.2, 22.4, 36.8, 58.8)
SketchConstraintAngle_1 = Sketch_1.setAngle(SketchLine_2.result(), SketchLine_1.result(), 45)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/a297e9f8d347454e4acad6a387227a40/angle.py)
