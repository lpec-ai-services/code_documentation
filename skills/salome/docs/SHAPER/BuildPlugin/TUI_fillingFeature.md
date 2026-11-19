<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/TUI_fillingFeature.html -->

# Create Filling

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Filling_1 = model.addFilling(Part_1_doc, [model.selection("EDGE", "[Box_1_1/Left][Box_1_1/Top]"), model.selection("EDGE", "[Box_1_1/Right][Box_1_1/Top]")])
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/0c12f4958a7e26c5dd05dc1de56079f6/filling.py)
