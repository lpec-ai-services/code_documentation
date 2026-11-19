<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_blocks_operations_page.html -->

# Blocks Operations

## Multi Transformation

```python
# Multi Transformation

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create vertices
p_25_25_50 = geompy.MakeVertex(25., 25., 50.)
p_50_25_25 = geompy.MakeVertex(50., 25., 25.)
p_25_50_25 = geompy.MakeVertex(25., 50., 25.)

box = geompy.MakeBoxDXDYDZ(50, 50, 50)

top_face = geompy.GetFaceNearPoint(box, p_25_25_50)
yz_face = geompy.GetFaceNearPoint(box, p_50_25_25)
xz_face = geompy.GetFaceNearPoint(box, p_25_50_25)

top_face_ind = geompy.GetSubShapeID(box, top_face)
yz_face_ind = geompy.GetSubShapeID(box, yz_face)
xz_face_ind = geompy.GetSubShapeID(box, xz_face)

# Multi-transformate block and glue the result
box_tr1 = geompy.MakeMultiTransformation1D(box, yz_face_ind, top_face_ind, 3)
box_tr2 = geompy.MakeMultiTransformation2D(box, xz_face_ind, yz_face_ind, 3, top_face_ind, 0, 2)

# add objects in the study
id_box = geompy.addToStudy(box, "Box")
id_box_tr1 = geompy.addToStudy(box_tr1, "Multi-transformed Block 1D")
id_box_tr2 = geompy.addToStudy(box_tr2, "Multi-transformed Block 2D")

# display the results
gg.createAndDisplayGO(id_box)
gg.setDisplayMode(id_box,1)
gg.createAndDisplayGO(id_box_tr1)
gg.createAndDisplayGO(id_box_tr2)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/blocks_operations_ex01.py)

## Explode on Blocks

```python
# Explode on Blocks

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create a box and a sphere
box = geompy.MakeBoxDXDYDZ(200, 200, 200)
sphere = geompy.MakeSphereR(100)

# make a compound
compound = geompy.MakeCompound([box, sphere])

# get all the blocks of the given compound, by criteria: min_nb_faces <= nb. of faces <= max_nb_faces
min_nb_faces = 6
max_nb_faces = 6
make_block_explode = geompy.MakeBlockExplode(compound, min_nb_faces, max_nb_faces)

# add objects in the study
id_compound = geompy.addToStudy(compound, "Compound")
id_make_block_explode = geompy.addToStudyInFather(compound, make_block_explode[0], "MakeBlockExplode")

# display the results
gg.createAndDisplayGO(id_compound)
gg.createAndDisplayGO(id_make_block_explode)
gg.setDisplayMode(id_make_block_explode,1)
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/blocks_operations_ex02.py)

## Propagate

```python
# Propagate

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

# create a box
check_box = geompy.MakeBoxDXDYDZ(200, 200, 200)

# build all possible propagation groups
listChains = geompy.Propagate(check_box)

# add objects in the study
geompy.addToStudy(check_box, "Box")
ii = 1
for chain in listChains:
    geompy.addToStudyInFather(check_box, chain, "propagation chain " + repr(ii))
    ii = ii + 1
 pass

salome.sg.updateObjBrowser()
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/blocks_operations_ex03.py)
