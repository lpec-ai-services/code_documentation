<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_whatis_page.html -->

# What Is

```python
# What Is

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

# create a box
box = geompy.MakeBoxDXDYDZ(100,30,100)
Descr = geompy.WhatIs(box)
print("\nBox 100x30x100 description:")
print(Descr)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/whatis.py)
