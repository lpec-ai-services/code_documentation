<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_symmetryaxisFeature.html -->

# Symmetry through an Axis of symmetry

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Cylinder_1 = model.addCylinder(Part_1_doc, model.selection("VERTEX", "PartSet/Origin"), model.selection("EDGE", "PartSet/OZ"), 5, 10)
Symmetry_1 = model.addSymmetry(Part_1_doc, [model.selection("SOLID", "Cylinder_1_1")], model.selection("EDGE", "([Cylinder_1_1/Face_1][Cylinder_1_1/Face_2])([Cylinder_1_1/Face_1][Cylinder_1_1/Face_3])"), False)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/5950fa092f482972564f080730ad495f/symmetryaxis.py)
