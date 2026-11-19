<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_linearcopyFeature.html -->

# Create Linear copy

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sphere_1 = model.addSphere(Part_1_doc, model.selection("VERTEX", "PartSet/Origin"), 10)
LinearCopy_1 = model.addMultiTranslation(Part_1_doc, [model.selection("SOLID", "Sphere_1_1")], model.selection("EDGE", "PartSet/OX"), 30, 3, model.selection("EDGE", "PartSet/OY"), 30, 2)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/1eb0df7c1abb870bdd9bbcc51f4952a8/linearcopy.py)
