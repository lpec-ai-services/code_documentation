<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/TUI_normalToFaceFeature.html -->

# Create normal to a face

```python
from salome.shaper import model
import os

### Create a Box
model.begin()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
model.do()

### Create a top face of the box normal
Normal_1 = model.getNormal(Part_1_doc, model.selection("FACE", "Box_1_1/Top"))
model.do()

model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/7284dd041b84ea26ba2a2702cc4fd04f/create_normal_to_face.py)

# Create normal to a face at vertex

```python

from salome.shaper import model
import os

model.begin()
Box_1 = model.addBox(Part_1_doc, 10, 10, 10)
model.do()
    
Normal_1 = model.getNormal(Part_1_doc, model.selection("FACE", "Box_1_1/Front"), model.selection("VERTEX", "[Box_1_1/Front][Box_1_1/Right][Box_1_1/Bottom]"))
model.do()

model.end()
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SHAPER/_downloads/3a7362a8eb990cf292bff03d99b48196/create_normal_to_face_at_vertex.py)
