<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_scalefactorFeature.html -->

# Scale by one common factor

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Cylinder_1 = model.addCylinder(Part_1_doc, model.selection("VERTEX", "PartSet/Origin"), model.selection("EDGE", "PartSet/OZ"), 5, 10)
Scale_1 = model.addScale(Part_1_doc, [model.selection("SOLID", "Cylinder_1_1")] , model.selection("VERTEX", "PartSet/Origin"), 2)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/a5958ce0bc19e274a9a41d74b4c45d8c/scalefactor.py)
