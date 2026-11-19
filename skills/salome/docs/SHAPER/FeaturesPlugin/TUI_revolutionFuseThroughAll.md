<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_revolutionFuseThroughAll.html -->

# Create Revolution Fuse by 360 degrees

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Sketch_1 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Top"))
SketchCircle_1 = Sketch_1.addCircle(5, 5, 2.5)
model.do()
RevolutionFuse_1 = model.addRevolutionFuse(Part_1_doc, [model.selection("COMPOUND", "Sketch_1")], model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Top]"), [model.selection("SOLID", "Box_1_1")])
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/c53444b00aed944f2a2c12061c36035e/revolution_fuse_through_all.py)
