<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/TUI_faceFeatures.html -->

# Create Face

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Face_1 = model.addFace(Part_1_doc, [model.selection("FACE", "Box_1_1/Top"),
                                    model.selection("FACE", "Box_1_1/Front")])
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/b888966c1128d904bda3d1a5739d4522/face.py)
