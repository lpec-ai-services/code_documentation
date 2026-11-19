<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_circleFeature.html -->

# Create Sketch Circle

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
SketchCircle_1 = Sketch_1.addCircle(38.6, 47.5, 31.5)
SketchCircle_2 = Sketch_1.addCircle(0.0, 14.1, 15.0, 0.1, 17.2, 19.9)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/9989b40b2ea051fe310627548754248e/circle.py)
