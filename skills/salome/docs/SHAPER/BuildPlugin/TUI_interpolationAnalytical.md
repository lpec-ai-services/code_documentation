<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/TUI_interpolationAnalytical.html -->

# Create Interpolation analytical

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()
Interpolation_1 = model.addInterpolation(Part_1_doc, "5*sin(t)","5*cos(t)","t*0.2", 0, 25, 100)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/874644d413cdab535e5b12c4a300d673/interpolationAnalytical.py)
