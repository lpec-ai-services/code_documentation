<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_intersectionFeature.html -->

# Create Intersection

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Cylinder_1 = model.addCylinder(Part_1_doc,
                               model.selection("VERTEX", "PartSet/Origin"),
                               model.selection("EDGE", "PartSet/OZ"), 5, 10)
Intersection_1 = model.addIntersection(Part_1_doc,
                                       [model.selection("SOLID", "Cylinder_1_1"),
                                        model.selection("SOLID", "Box_1_1")])
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/fbec1a1e485684472a80c8af0eecdbde/intersection.py)
