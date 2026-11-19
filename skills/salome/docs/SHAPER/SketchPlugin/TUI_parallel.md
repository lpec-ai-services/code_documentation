<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_parallel.html -->

# Create Parallel constraint

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
SketchLine_1 = Sketch_1.addLine(13, 58, 69, 75)
SketchLine_2 = Sketch_1.addLine(12, 38, 73, 23)
SketchConstraintParallel_1 = Sketch_1.setParallel(SketchLine_1.result(), SketchLine_2.result())
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/ac13ee4ff93fb51e92db2a90bf687dac/parallel.py)
