<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_fillet1DWire.html -->

# Create 1D-fillet on a wire

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()

### Create Box
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)

### Create Wire
Wire_1_objects = [model.selection("EDGE", "[Box_1_1/Left][Box_1_1/Bottom]"),
                  model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Left]"),
                  model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Top]"),
                  model.selection("EDGE", "[Box_1_1/Front][Box_1_1/Right]")]
Wire_1 = model.addWire(Part_1_doc, Wire_1_objects, False)

### Create Fillet1D
Fillet1D_1 = model.addFillet(Part_1_doc, [model.selection("WIRE", "Wire_1_1")], 3)

model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/b5591928e3aa9a7e40afded78bca7a15/fillet1d_wire.py)
