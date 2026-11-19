<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_chamferDistances.html -->

# Create Chamfer by distances

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 20, 20, 20)
Chamfer_1 = model.addChamfer(Part_1_doc, [model.selection("FACE", "Box_1_1/Top")], True, 2, 2)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/b08f575f6044884e99a83626c5816b3c/chamfer1.py)
