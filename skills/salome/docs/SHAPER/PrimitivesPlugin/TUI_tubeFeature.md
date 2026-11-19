<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/PrimitivesPlugin/TUI_tubeFeature.html -->

# Create Tube

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Torus_1 = model.addTube(Part_1_doc, 3, 5, 12)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/3be0f138d51bacc4adc97de3c4212a10/tube.py)
