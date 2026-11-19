<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_chamferDistAngle.html -->

# Create Chamfer by a distance and an angle

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 20, 20, 20)
Chamfer_1_objects = [model.selection("EDGE", "[Box_1_1/Right][Box_1_1/Top]"), model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Top]"), model.selection("EDGE", "[Box_1_1/Left][Box_1_1/Top]"), model.selection("EDGE", "[Box_1_1/Back][Box_1_1/Top]")]
Chamfer_1 = model.addChamfer(Part_1_doc, Chamfer_1_objects, False, 2, 25)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/10f81808647b19a3d82690e20826649d/chamfer2.py)
