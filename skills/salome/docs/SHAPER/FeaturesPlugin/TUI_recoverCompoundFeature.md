<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_recoverCompoundFeature.html -->

# Recover

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Plane_4 = model.addPlane(Part_1_doc, model.selection("FACE", "Box_1_1/Left"), model.selection("FACE", "Box_1_1/Right"))
Plane_5 = model.addPlane(Part_1_doc, model.selection("FACE", "Box_1_1/Front"), model.selection("FACE", "Box_1_1/Back"))
Split_1 = model.addSplit(Part_1_doc, [model.selection("SOLID", "Box_1_1")], [model.selection("FACE", "Plane_1")])
Split_2 = model.addSplit(Part_1_doc, [model.selection("SOLID", "Split_1_1_1")], [model.selection("FACE", "Plane_2")])
Recover_1 = model.addRecover(Part_1_doc, Split_2, [Split_1.result()], True)
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/02003e9f51f99df27b2252b18b33ee2a/recover_compound.py)
