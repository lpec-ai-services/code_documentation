<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_lineFeature.html -->

# Create Sketch Line

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
SketchLine_1 = Sketch_1.addLine(64.5, 87.9, -33.4, -42.6)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/b3bc57ed09b9337ab8b6841cecda8de3/line.py)
