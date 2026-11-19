<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/TUI_wireFeature.html -->

# Create Wire

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Wire_1_objects = [model.selection("EDGE", "[Box_1_1/Left][Box_1_1/Top]"), model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Top]"), model.selection("EDGE", "[Box_1_1/Right][Box_1_1/Top]"), model.selection("EDGE", "[Box_1_1/Back][Box_1_1/Top]")]
Wire_1 = model.addWire(Part_1_doc, Wire_1_objects)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/37961333e9c0ef6698606a6e72ed9cfd/wire.py)
