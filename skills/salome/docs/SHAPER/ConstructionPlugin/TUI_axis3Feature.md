<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ConstructionPlugin/TUI_axis3Feature.html -->

# Create Axis by line

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Axis_4 = model.addAxis(Part_1_doc, model.selection("EDGE", "PartSet/OY"))
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/7113c65a2002311ca3e0c1cc8af60325/axis3.py)
