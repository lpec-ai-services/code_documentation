<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_revolutionCutByAngles.html -->

# Create Revolution Cut by angles

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
RevolutionCut_1 = model.addRevolutionCut(Part_1_doc, [model.selection("COMPOUND", "Sketch_1")], model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Top]"), 0, 90, [model.selection("SOLID", "Box_1_1")])
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/d898fd4ce92a11146a9e5da761f0cf2e/revolution_cut_by_angles.py)
