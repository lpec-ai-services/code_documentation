<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/TUI_compoundFeature.html -->

# Create Compound

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Compound_1_objects = [model.selection("FACE", "Box_1_1/Front"), model.selection("FACE", "Box_1_1/Top"), model.selection("FACE", "Box_1_1/Left")]
Compound_1 = model.addCompound(Part_1_doc, Compound_1_objects)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/f963c87f46cb73a3507de9d0e5595fa9/compound.py)
