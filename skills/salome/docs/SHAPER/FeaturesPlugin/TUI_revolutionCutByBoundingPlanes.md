<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_revolutionCutByBoundingPlanes.html -->

# Create Revolution Cut by bounding planes

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
RevolutionCut_1 = model.addRevolutionCut(Part_1_doc, [model.selection("COMPOUND", "Sketch_1")], model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Top]"), model.selection(), 0, model.selection("FACE", "Box_1_1/Front"), 0, [model.selection("SOLID", "Box_1_1")])
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/b1b284fc7f6182ba48525fc4b31606e7/revolution_cut_by_bounding_planes.py)
