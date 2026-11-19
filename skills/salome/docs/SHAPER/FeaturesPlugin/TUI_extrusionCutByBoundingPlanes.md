<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_extrusionCutByBoundingPlanes.html -->

# Create Extrusion Cut by bounding planes

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
ExtrusionCut_1 = model.addExtrusionCut(Part_1_doc,
                                       [],
                                       model.selection(),
                                       model.selection("FACE", "Box_1_1/Bottom"),
                                       0,
                                       model.selection("FACE", "Box_1_1/Top"),
                                       0,
                                       [model.selection("SOLID", "Box_1_1")])
Sketch_1 = model.addSketch(Part_1_doc, model.selection("FACE", "Box_1_1/Top"))
SketchCircle_1 = Sketch_1.addCircle(5, 0, 2)
ExtrusionCut_1.setNestedSketch(Sketch_1)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/c564f77950eb7e0f039d92d1b1e48a3e/extrusion_cut_by_bounding_planes.py)
