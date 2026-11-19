<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/CollectionPlugin/TUI_groupShapeFeature.html -->

# Create Group Shape

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
GroupShape_1 = model.addGroupShape(Part_1_doc, [model.selection("COMPOUND", "Group_1"),
                                                      model.selection("COMPOUND", "Group_2")])
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/390719164d5f54f1c4589497e1f2c352/group_shape.py)
