<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_boundingBoxFeature.html -->

# Create bounding box

```python
from salome.shaper import model
import os

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
### Create Cone
Cone_1 = model.addCone(Part_1_doc, model.selection("VERTEX", "PartSet/Origin"), model.selection("EDGE", "PartSet/OZ"), 10, 5, 10)

model.do()
### Create BoundingBox
BoundingBox_1 = model.getBoundingBox(Part_1_doc, model.selection("SOLID", "Cone_1_1"))
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/223b900c9ba7e668f76875c40a5467dc/create_bounding_box.py)
