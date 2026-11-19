<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_check_self_intersections_page.html -->

# Detect Self-intersections

```python
# Detect Self-intersections

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

# create a box
box = geompy.MakeBoxDXDYDZ(100,100,100)
# create a cylinder
cylinder = geompy.MakeCylinderRH(100, 300)
# make a compound
compound = geompy.MakeCompound([box, cylinder])

# check self-intersection
IsValid = geompy.CheckSelfIntersections(compound)
if not IsValid:
    print("Shape is self-intersected!")
else:
    print("No self-intersection detected in a shape")
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/check_self_intersections.py)
