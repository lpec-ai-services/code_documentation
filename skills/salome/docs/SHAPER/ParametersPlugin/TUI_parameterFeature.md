<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/ParametersPlugin/TUI_parameterFeature.html -->

# Create Parameter

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
model.addParameter(partSet, "angle", "60*3.141/180", "main angle")
model.importParameters(partSet, "File.txt")
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/88ebf562f095e76d579c52dfaa3346a6/parameter.py)
[`Download parameters file sample`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/285074ff44e196e08a200da264ea3f4f/File.txt)
