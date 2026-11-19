<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_viewing_geom_objs_page.html -->

# Viewing Geometrical Objects

## Changing Display Mode

```python
# Changing Display Mode

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
box = geompy.MakeBox(0,0,0, 50,50,50)
box2 = geompy.MakeBox(-50,-50,-50, 0,0,0)

sphere = geompy.MakeSphere(50,50,50, 30)
fuse = geompy.MakeBoolean(box,sphere,3)
fuse_id = geompy.addToStudy(fuse,"Fuse")

gg = salome.ImportComponentGUI("GEOM")
gg.createAndDisplayGO(fuse_id)
gg.setDisplayMode(fuse_id,1)
gg.setVectorsMode(fuse_id, True)
gg.setVerticesMode(fuse_id, True)
gg.setNameMode(fuse_id, 1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/viewing_geom_objs_ex01.py)

## Changing Color

```python
# Changing Color

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
box = geompy.MakeBox(0,0,0, 50,50,50)

sphere = geompy.MakeSphere(50,50,50, 30)
fuse = geompy.MakeBoolean(box,sphere,3)
fuse_id = geompy.addToStudy(fuse,"Fuse")

gg = salome.ImportComponentGUI("GEOM")
gg.createAndDisplayGO(fuse_id)
gg.setDisplayMode(fuse_id,1)
gg.setColor(fuse_id,218,165,31)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/viewing_geom_objs_ex02.py)

## Changing Transparency

```python
# Changing Transparency

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

box = geompy.MakeBox(0,0,0, 50,50,50)
sphere = geompy.MakeSphere(50,50,50, 30)

fuse = geompy.MakeBoolean(box,sphere,3)
fuse_id = geompy.addToStudy(fuse,"Fuse")

gg = salome.ImportComponentGUI("GEOM")
gg.createAndDisplayGO(fuse_id)
gg.setDisplayMode(fuse_id,1)
gg.setColor(fuse_id,218,165,31)
gg.setTransparency(fuse_id,0.5)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/viewing_geom_objs_ex03.py)

## Set Point Marker

```python
# Set Point Marker

import os
import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

texture_file = os.path.join(os.getenv("GEOM_ROOT_DIR"), "share", "salome", "resources", "geom", "textures", "texture1.dat")
texture = geompy.LoadTexture(texture_file)

v1 = geompy.MakeVertex(0, 0, 0)
v2 = geompy.MakeVertex(100, 0, 0)
v3 = geompy.MakeVertex(0, 100, 0)

v1.SetMarkerStd(GEOM.MT_O_PLUS, GEOM.MS_25)
v2.SetMarkerStd(GEOM.MT_BALL,   GEOM.MS_40)
v3.SetMarkerTexture(texture)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/viewing_geom_objs_ex04.py)
