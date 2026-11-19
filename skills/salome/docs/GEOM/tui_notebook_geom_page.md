<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_notebook_geom_page.html -->

# Using SALOME NoteBook

```python
# Using SALOME NoteBook

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
import salome_notebook
gg = salome.ImportComponentGUI("GEOM")

# set variables
notebook = salome_notebook.notebook
notebook.set("Length", 150)
notebook.set("Width", 100)

# create box
box = geompy.MakeBoxDXDYDZ("Length", "Width", 200)

# add object in the study
id_box = geompy.addToStudy(box,"Box")

# display the boxes
gg.createAndDisplayGO(id_box)
gg.setDisplayMode(id_box,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/notebook_geom.py)
