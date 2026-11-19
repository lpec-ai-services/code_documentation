<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/PartSetPlugin/TUI_new_partFeature.html -->

# Create Part

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/e10f825909fc94b2b6128bf3dca3cbd7/new_part.py)
