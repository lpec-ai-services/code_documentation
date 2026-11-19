<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_translationvectorFeature.html -->

# Translation by axis and distance

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Cone_1 = model.addCone(Part_1_doc, model.selection("VERTEX", "PartSet/Origin"), model.selection("EDGE", "PartSet/OZ"), 10, 5, 10)
Translation_1 = model.addTranslation(Part_1_doc, [model.selection("SOLID", "Cone_1_1")], model.selection("EDGE", "([Cone_1_1/Face_1][Cone_1_1/Face_2])([Cone_1_1/Face_1][Cone_1_1/Face_3])"), 40)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/f5bc34fb74b991ad5830929ad50c91ee/translationvector.py)
