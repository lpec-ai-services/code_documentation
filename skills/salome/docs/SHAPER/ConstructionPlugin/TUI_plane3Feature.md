<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ConstructionPlugin/TUI_plane3Feature.html -->

# Create Plane by other plane

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Plane_4 = model.addPlane(Part_1_doc, model.selection("FACE", "Box_1_1/Top"), 10, False)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/d6e324c0dcb30a7e898f8556b78ea0a0/plane3.py)
