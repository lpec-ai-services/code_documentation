<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_revolutionByBoundingPlanes.html -->

# Create Revolution by bounding planes

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.standardPlane("XOY"))
SketchCircle_1 = Sketch_1.addCircle(20, 20, 10)
model.do()
Revolution_1 = model.addRevolution(Part_1_doc,
                                   [model.selection("COMPOUND", "Sketch_1")],
                                   model.selection("EDGE", "PartSet/OY"),
                                   model.selection("FACE", "PartSet/XOY"),
                                   0,
                                   model.selection("FACE", "PartSet/YOZ"),
                                   0)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/bd766ef20b55afa657b0cb6ee9b45dac/revolution_by_bounding_planes.py)
