<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_scaleXYZFeature.html -->

# Scale by different factors along axes

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Sphere_1 = model.addSphere(Part_1_doc, model.selection("VERTEX", "PartSet/Origin"), 10)
Scale_1 = model.addScale(Part_1_doc, [model.selection("SOLID", "Sphere_1_1")] , model.selection("VERTEX", "PartSet/Origin"), 2 , 3, 4)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/c6dc7c6120329ab2e456cde2dad91798/scaleXYZ.py)
