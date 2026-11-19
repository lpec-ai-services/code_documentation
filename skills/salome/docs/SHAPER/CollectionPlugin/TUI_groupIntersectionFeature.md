<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/CollectionPlugin/TUI_groupIntersectionFeature.html -->

# Create Group Intersection

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Group_1 = model.addGroup(Part_1_doc, [model.selection("FACE", "Box_1_1/Top"),
                                      model.selection("FACE", "Box_1_1/Left")])
Group_2 = model.addGroup(Part_1_doc, [model.selection("FACE", "Box_1_1/Front"),
                                      model.selection("FACE", "Box_1_1/Top")])
Group_3 = model.addGroup(Part_1_doc, [model.selection("FACE", "Box_1_1/Front"),
                                      model.selection("FACE", "Box_1_1/Right"),
                                      model.selection("FACE", "Box_1_1/Top")])
GroupIntersection_1_objects = [model.selection("COMPOUND", "Group_1"),
                               model.selection("COMPOUND", "Group_2"),
                               model.selection("COMPOUND", "Group_3")]
GroupIntersection_1 = model.addGroupIntersection(Part_1_doc, GroupIntersection_1_objects)
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/02e5508e4e23b8ec7088dfba8da6c243/group_intersection.py)
