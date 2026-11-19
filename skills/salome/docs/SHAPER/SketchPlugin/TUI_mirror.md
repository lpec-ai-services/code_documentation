<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_mirror.html -->

# Create Mirror copy

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()

Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
SketchCircle_1 = Sketch_1.addCircle(25, 25, 11)
SketchLine_1 = Sketch_1.addLine(9, 78, 78, 9)

SketchConstraintMirror_1 = Sketch_1.addMirror(SketchLine_1.result(), [SketchCircle_1.results()[1]])

model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/f4b975398e643241018fce19551cddce/mirror.py)
