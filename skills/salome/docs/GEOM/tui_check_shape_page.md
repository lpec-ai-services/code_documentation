<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_check_shape_page.html -->

# Check Shape

```python
# Check Shape

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

# create a box
box = geompy.MakeBoxDXDYDZ(100,30,100)
(IsValid, err) = geompy.CheckShape(box, False, 2, True)
if IsValid == 0:
    geompy.PrintShapeErrors(box, err)
 raise RuntimeError("Invalid box created")
else:
    print("\nBox is valid")
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/check_shape.py)
