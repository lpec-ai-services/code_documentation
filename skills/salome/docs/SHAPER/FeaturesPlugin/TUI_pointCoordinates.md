<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_pointCoordinates.html -->

# Get point coordinates

```python
import os
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
coordinates = model.getPointCoordinates(Part_1_doc,model.selection("VERTEX", "[Box_1_1/Front][Box_1_1/Left][Box_1_1/Top]"))
print(" x: ", coordinates[0])
print(" y: ", coordinates[1])
print(" z: ", coordinates[2])
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/156308d57e96c4c3b40b4d9c40ccca19/point_coordinates.py)
