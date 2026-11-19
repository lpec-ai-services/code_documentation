<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ConstructionPlugin/TUI_plane1Feature.html -->

# Create Plane by points

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Plane_4 = model.addPlane(Part_1_doc, model.selection("VERTEX", "[Box_1_1/Back][Box_1_1/Left][Box_1_1/Top]"), model.selection("VERTEX", "[Box_1_1/Front][Box_1_1/Left][Box_1_1/Top]"), model.selection("VERTEX", "[Box_1_1/Front][Box_1_1/Right][Box_1_1/Bottom]"))
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/f61717064287ef06b29956b98c41e519/plane1.py)
