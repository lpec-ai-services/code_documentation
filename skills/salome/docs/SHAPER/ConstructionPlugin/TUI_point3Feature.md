<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ConstructionPlugin/TUI_point3Feature.html -->

# Create Point by projection

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Point_2 = model.addPoint(Part_1_doc, 10, 10, 10)
Point_3 = model.addPoint(Part_1_doc, model.selection("VERTEX", "Point_1"), model.selection("FACE", "PartSet/XOY"))
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/9689adc14fadb3d7b77fd5cc665d6044/point3.py)
