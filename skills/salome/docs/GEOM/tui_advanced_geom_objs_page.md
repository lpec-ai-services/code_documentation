<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_advanced_geom_objs_page.html -->

# Advanced Geometrical Objects

## Creation of PipeTShape

```python
# Creation of PipeTShape

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create PipeTShape object
pipetshape = geompy.MakePipeTShape(80.0, 20.0, 200.0, 50.0, 20.0, 200.0)

# add object in the study
id_pipetshape = geompy.addToStudy(pipetshape[0],"PipeTShape")
# add groups in the study
for g in pipetshape[1:]:
    geompy.addToStudyInFather(pipetshape[0], g, g.GetName())
 
# Create junction vertices
P1 = geompy.MakeVertex(0.0, 0.0, 0.0)
P2 = geompy.MakeVertex(400.0, 0.0, 0.0)
P3 = geompy.MakeVertex(200.0, 0.0, 200.0)

# create PipeTShape object with position
pipetshape_position = geompy.MakePipeTShape(80.0, 20.0, 200.0, 50.0, 20.0, 200.0, True, P1, P2, P3)

# add object in the study
id_pipetshape_position = geompy.addToStudy(pipetshape_position[0],"PipeTShape_position")
# add groups in the study
for g in pipetshape_position[1:]:
    geompy.addToStudyInFather(pipetshape_position[0], g, g.GetName())

# create PipeTShape object with left thickness reduction
pipetshape_thr = geompy.MakePipeTShape(80.0, 20.0, 200.0, 50.0, 20.0, 200.0,
                                       theRL=60, theWL=20, theLtransL=40, theLthinL=20)

# add object in the study
id_pipetshape_thr = geompy.addToStudy(pipetshape_thr[0],"PipeTShape_left_thickness_reduction")
# add groups in the study
for g in pipetshape_thr[1:]:
    geompy.addToStudyInFather(pipetshape_thr[0], g, g.GetName())

# create PipeTShape with chamfer object
pipetshapechamfer = geompy.MakePipeTShapeChamfer(80.0, 20.0, 200.0, 50.0, 20.0, 200.0, 20.0, 20.0)

# add object in the study
id_pipetshapechamfer = geompy.addToStudy(pipetshapechamfer[0],"PipeTShapeChamfer")
# add groups in the study
for g in pipetshapechamfer[1:]:
    geompy.addToStudyInFather(pipetshapechamfer[0], g, g.GetName())

# create PipeTShape with chamfer object with position
pipetshapechamfer_position = geompy.MakePipeTShapeChamfer(80.0, 20.0, 200.0, 50.0, 20.0, 200.0, 20.0, 20.0, True, P1, P2, P3)

# add object in the study
id_pipetshapechamfer_position = geompy.addToStudy(pipetshapechamfer_position[0],"PipeTShapeChamfer_position")
# add groups in the study
for g in pipetshapechamfer_position[1:]:
    geompy.addToStudyInFather(pipetshapechamfer_position[0], g, g.GetName())

# create PipeTShape with chamfer object with left and right thickness reductions
pipetshapechamfer_thr = geompy.MakePipeTShapeChamfer(80.0, 20.0, 200.0, 50.0, 20.0, 200.0, 20.0, 20.0,
                                                     theRL=60, theWL=20, theLtransL=40, theLthinL=20,
                                                     theRR=40, theWR=10, theLtransR=60, theLthinR=30)

# add object in the study
id_pipetshapechamfer_thr = geompy.addToStudy(pipetshapechamfer_thr[0],"PipeTShapeChamfer_two_thickness_reductions")
# add groups in the study
for g in pipetshapechamfer_thr[1:]:
    geompy.addToStudyInFather(pipetshapechamfer_thr[0], g, g.GetName())

# create PipeTShape with fillet object
pipetshapefillet = geompy.MakePipeTShapeFillet(80.0, 20.0, 200.0, 50.0, 20.0, 200.0, 5.0)

# add object in the study
id_pipetshapefillet = geompy.addToStudy(pipetshapefillet[0],"PipeTShapeFillet")
# add groups in the study
for g in pipetshapefillet[1:]:
    geompy.addToStudyInFather(pipetshapefillet[0], g, g.GetName())

# create PipeTShape with fillet object with position
pipetshapefillet_position = geompy.MakePipeTShapeFillet(80.0, 20.0, 200.0, 50.0, 20.0, 200.0, 5.0, True, P1, P2, P3)

# add object in the study
id_pipetshapefillet_position = geompy.addToStudy(pipetshapefillet_position[0],"PipeTShapeFillet_position")
# add groups in the study
for g in pipetshapefillet_position[1:]:
    geompy.addToStudyInFather(pipetshapefillet_position[0], g, g.GetName())

# create PipeTShape with fillet object with three thickness reductions
pipetshapefillet_thr = geompy.MakePipeTShapeFillet(80.0, 20.0, 200.0, 50.0, 20.0, 200.0,
                                                   5.0, True, None, None, None,
                                                   60, 20, 40, 20,
                                                   40, 10, 60, 30,
                                                   20, 10, 30, 30)

# add object in the study
id_pipetshapefillet_thr = geompy.addToStudy(pipetshapefillet_thr[0],"PipeTShapeFillet_three_thickness_reductions")
# add groups in the study
for g in pipetshapefillet_thr[1:]:
    geompy.addToStudyInFather(pipetshapefillet_thr[0], g, g.GetName())

# display pipetshapes
gg.createAndDisplayGO(id_pipetshape)
gg.createAndDisplayGO(id_pipetshape_position)
gg.createAndDisplayGO(id_pipetshape_thr)
gg.createAndDisplayGO(id_pipetshapechamfer)
gg.createAndDisplayGO(id_pipetshapechamfer_position)
gg.createAndDisplayGO(id_pipetshapechamfer_thr)
gg.createAndDisplayGO(id_pipetshapefillet)
gg.createAndDisplayGO(id_pipetshapefillet_position)
gg.createAndDisplayGO(id_pipetshapefillet_thr)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/advanced_geom_objs_ex01.py)

## Creation of DividedDisk

```python
# Creation of DividedDisk

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create DividedDisk object
divideddisk = geompy.MakeDividedDisk(100, 1, GEOM.SQUARE)

# add object in the study
id_divideddisk = geompy.addToStudy(divideddisk,"DividedDisk")

# display divideddisk
gg.createAndDisplayGO(id_divideddisk)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/advanced_geom_objs_ex02.py)

## Creation of DividedCylinder

```python
# Creation of DividedCylinder

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create DividedCylinder object
dividedcylinder = geompy.MakeDividedCylinder(100, 300, GEOM.SQUARE)

# add object in the study
id_dividedcylinder = geompy.addToStudy(dividedcylinder,"DividedCylinder")

# display dividedcylinder
gg.createAndDisplayGO(id_dividedcylinder)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/advanced_geom_objs_ex03.py)

## Creation of SmoothingSurface

```python
import salome, GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

# create a could of points
points = [
    geompy.MakeVertex( 0,0,0 ),
    geompy.MakeVertex( 9,0,0 ),
    geompy.MakeVertex( 0,9,0 ),
    geompy.MakeVertex( 9,9,0 ),
    geompy.MakeVertex( 3,3,1 ),
    geompy.MakeVertex( 6,6,2 )]

# create SmoothingSurface object
smoothingsurface = geompy.MakeSmoothingSurface( points )

# add object in the study
id_smoothingsurface = geompy.addToStudy(smoothingsurface,"SmoothingSurface")

# display smoothingsurface
gg = salome.ImportComponentGUI("GEOM")
gg.createAndDisplayGO(id_smoothingsurface)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/advanced_geom_objs_smoothingsurface.py)
