<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ConstructionPlugin/TUI_axis6Feature.html -->

# Create Axis by two planes

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Axis_4 = model.addAxis(Part_1_doc, model.selection("FACE", "Box_1_1/Top"), model.selection("FACE", "Box_1_1/Left"))
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/c8ccecc50f7a6bfdb3415086ab78e035/axis6.py)
