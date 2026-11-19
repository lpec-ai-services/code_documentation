<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_extrusionBySizes.html -->

# Create Extrusion by sizes

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.standardPlane("XOY"))
SketchCircle_1 = Sketch_1.addCircle(0, 0, 25)
model.do()
Extrusion_1 = model.addExtrusion(Part_1_doc,
                                 [model.selection("COMPOUND", "Sketch_1")],
                                 model.selection(),
                                 50,
                                 0)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/fdb3747cfb4fe3ecab6beae5581bd72b/extrusion_by_sizes.py)
