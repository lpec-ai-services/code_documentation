<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_check_compound_of_blocks_page.html -->

# Check Compound of Blocks

```python
# Check Compound of Blocks

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create boxes
box1 = geompy.MakeBox(0,0,0,100,50,100)
box2 = geompy.MakeBox(100,0,0,250,50,100)

# make a compound
compound = geompy.MakeCompound([box1, box2])

# glue the faces of the compound
tolerance = 1e-5
glue = geompy.MakeGlueFaces(compound, tolerance)
IsValid = geompy.CheckCompoundOfBlocks(glue)
if IsValid == 0:
 raise RuntimeError("Invalid compound created")
else:
    print("\nCompound is valid")
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/check_compound_of_blocks.py)
