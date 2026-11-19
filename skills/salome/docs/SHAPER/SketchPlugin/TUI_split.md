<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_split.html -->

# Create Split

```python
from salome.shaper import model
from salome.shaper import geom

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))

SketchCircle_1 = Sketch_1.addCircle(44, 44, 29)

SketchPoint_1 = Sketch_1.addPoint(15, 44)
SketchConstraintCoincidence_1 = Sketch_1.setCoincident(SketchPoint_1.coordinates(), SketchCircle_1.results()[1])
SketchPoint_2 = Sketch_1.addPoint(44, 73)
SketchConstraintCoincidence_2 = Sketch_1.setCoincident(SketchPoint_2.coordinates(), SketchCircle_1.results()[1])
SketchPoint_3 = Sketch_1.addPoint(64, 23)
SketchConstraintCoincidence_3 = Sketch_1.setCoincident(SketchPoint_3.coordinates(), SketchCircle_1.results()[1])

GeomPoint = geom.Pnt2d(22, 65)
Sketch_1.addSplit(SketchCircle_1, GeomPoint)

model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/77f70025411b000ac2b60977a9584f08/split.py)
