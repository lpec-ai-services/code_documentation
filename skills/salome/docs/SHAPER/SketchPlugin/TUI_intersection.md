<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_intersection.html -->

# Create Intersection

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()

Point_2 = model.addPoint(Part_1_doc, 10, 10, -10)
Point_3 = model.addPoint(Part_1_doc, 70, 70, 50)
Polyline_1 = model.addPolyline3D(Part_1_doc, [model.selection("VERTEX", "Point_1"), model.selection("VERTEX", "Point_2")], False)

Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))
SketchIntersectionPoint_1 = Sketch_1.addIntersectionPoint(model.selection("EDGE", "Polyline_1_1/Edge_1"), True)

model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/0a80ed9b47c2b53662bad859b74886fd/intersection.py)
