<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ConstructionPlugin/TUI_axis5Feature.html -->

# Create Axis by plane and point

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Axis_4 = model.addAxis(Part_1_doc, model.selection("FACE", "PartSet/XOY"), model.selection("VERTEX", "PartSet/Origin"))
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/38c8c9203c389964e9c7bdf2033357be/axis5.py)
