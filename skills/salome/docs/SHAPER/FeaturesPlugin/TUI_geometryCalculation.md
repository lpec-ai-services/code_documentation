<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_geometryCalculation.html -->

# Get Geometry Calculation

```python
import os
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
properties = model.getGeometryCalculation(Part_1_doc,model.selection("SOLID", "Box_1_1"))
print(" length: ", properties[0])
print(" area: ", properties[1])
print(" volume: ", properties[2])
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/4aba8924bccf73eff13180df21d9b0ee/geometry_calculation.py)
