<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/TUI_shellFeature.html -->

# Create Shell

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
Shell_1 = model.addShell(Part_1_doc, [model.selection("FACE", "Box_1_1/Top"),
                                      model.selection("FACE", "Box_1_1/Front")])
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/ed2b62f14a4161c89daae7d1fab9c7cb/shell.py)
