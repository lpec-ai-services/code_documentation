<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_revolutionCutThroughAll.html -->

# Create Revolution Cut by 360 degrees

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
RevolutionCut_1 = model.addRevolutionCut(Part_1_doc, [model.selection("COMPOUND", "Sketch_1")], model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Top]"), [model.selection("SOLID", "Box_1_1")])
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/59eebef037cf77aa0a750c60d161b880/revolution_cut_through_all.py)
