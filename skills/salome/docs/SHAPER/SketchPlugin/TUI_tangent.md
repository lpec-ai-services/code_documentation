<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_tangent.html -->

# Create Tangent constraint

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
SketchCircle_1 = Sketch_1.addCircle(30, 30, 15)
SketchLine_1 = Sketch_1.addLine(10, 80, 80, 27)
SketchConstraintTangent_1 = Sketch_1.setTangent(SketchCircle_1.results()[1], SketchLine_1.result())
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/57a6f503c78281dc944e68ba10c03f04/tangent.py)
