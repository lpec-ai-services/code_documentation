<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_coincident.html -->

# Create Coincident constraint

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
SketchCircle_1 = Sketch_1.addCircle(34, 28, 12)
SketchLine_1 = Sketch_1.addLine(41, 45, 61, 72)
SketchConstraintCoincidence_1 = Sketch_1.setCoincident(SketchCircle_1.results()[1], SketchLine_1.startPoint())
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/e1b53b51c53dfa97f74820a668ab33a0/coincident.py)
