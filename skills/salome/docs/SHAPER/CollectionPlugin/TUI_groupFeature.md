<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/CollectionPlugin/TUI_groupFeature.html -->

# Create Group

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Cone_1 = model.addCone(Part_1_doc, model.selection("VERTEX", "PartSet/Origin"), model.selection("EDGE", "PartSet/OZ"), 10, 5, 10)
Group_1 = model.addGroup(Part_1_doc, [model.selection("EDGE", "[Cone_1_1/Face_1][Cone_1_1/Face_2]"), model.selection("EDGE", "[Cone_1_1/Face_1][Cone_1_1/Face_3]")])
Group_1.result().setName("edges_cone")
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/53ebad4874ffa044d7d85b48c83fcc96/group.py)
