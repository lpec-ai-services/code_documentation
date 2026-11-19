<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_removeSubShapesFeature.html -->

# Remove Sub-Shapes

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sketch_1 = model.addSketch(Part_1_doc, model.standardPlane("XOY"))
SketchCircle_1 = Sketch_1.addCircle(0, -25, 50)
SketchCircle_2 = Sketch_1.addCircle(0, 25, 50)
model.do()
Extrusion_1 = model.addExtrusion(Part_1_doc,
                                [model.selection("COMPOUND", "Sketch_1")],
                                model.selection(),
                                10,
                                0)
Remove_SubShapes_1 = model.addRemoveSubShapes(Part_1_doc,
                                              model.selection("COMPSOLID", "Extrusion_1_1"))
Remove_SubShapes_1.setSubShapesToRemove([model.selection("SOLID", "Extrusion_1_1_2")])
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/59568c1cf8dc021aa48627df561452de/remove_subshapes.py)
