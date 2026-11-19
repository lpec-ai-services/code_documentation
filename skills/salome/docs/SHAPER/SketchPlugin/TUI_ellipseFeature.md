<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/TUI_ellipseFeature.html -->

# Create Sketch Ellipse

```python
from salome.shaper import model

model.begin()
partSet = model.moduleDocument()
Sketch_1 = model.addSketch(partSet, model.defaultPlane("XOY"))
SketchEllipse_1 = Sketch_1.addEllipse(-70, 5, -25, 10, -50, 40, True)
SketchEllipse_2 = Sketch_1.addEllipse(30, 50, 90, 10, 70, 50, False)
model.do()
model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/706a003eab97b119ca19e9a5e66008d4/ellipse.py)
