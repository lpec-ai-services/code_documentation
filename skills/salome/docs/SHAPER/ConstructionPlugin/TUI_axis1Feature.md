<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ConstructionPlugin/TUI_axis1Feature.html -->

# Create Axis by dimensions

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Axis_4 = model.addAxis(Part_1_doc, 10, 10, 10)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/345868a2edee69b4696122439d0ba4d5/axis1.py)
