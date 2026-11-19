<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/TUI_compsolidFeature.html -->

# Create CompSolid

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
CompSolid_1 = model.addCompSolid(Part_1_doc, [model.selection("SOLID", "Box_1_1")])
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/b2af11988b5af3877863fc512d60f72f/compsolid.py)
