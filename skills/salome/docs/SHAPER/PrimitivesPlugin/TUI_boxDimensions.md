<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/PrimitivesPlugin/TUI_boxDimensions.html -->

# Create Box by dimensions

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/390b4b2b99452fe932961382cb474bbf/box1.py)
