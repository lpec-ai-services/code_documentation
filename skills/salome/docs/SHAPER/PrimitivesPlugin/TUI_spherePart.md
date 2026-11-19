<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/PrimitivesPlugin/TUI_spherePart.html -->

# Create Part of sphere

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sphere_1 = model.addSphere(Part_1_doc,5,10,180,245,0,90)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/e07f882324d7dd877edf90a9346f474d/sphere2.py)
