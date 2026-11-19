<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_working_with_groups_page.html -->

# Working with Groups

## Creation of a group

```python
# Creation of a group

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create two vertices
p0 = geompy.MakeVertex(0.  , 0.  , 0.  )
p200 = geompy.MakeVertex(200., 200., 200.)

# create a box from two points
Box = geompy.MakeBoxTwoPnt(p0, p200)

# create a group from the faces of the box
group = geompy.CreateGroup(Box, geompy.ShapeType["FACE"])

# add objects to the group
SubFaceList = geompy.SubShapeAllSortedCentres(Box, geompy.ShapeType["FACE"])
for i in [0, 3, 5] :
    FaceID = geompy.GetSubShapeID(Box, SubFaceList[i])
    geompy.AddObject(group, FaceID)

# add all selected shapes from the list to the group
# (the program doesn't raise error, if some shapes are already included)
geompy.UnionList(group, [SubFaceList[0], SubFaceList[2], SubFaceList[5]])

# remove an object from the group
geompy.RemoveObject(group, FaceID)

# remove all selected shapes from the group
# (the program doesn't raise error, if some shapes are not included)
geompy.DifferenceList(group, [SubFaceList[2], SubFaceList[3], SubFaceList[4]])
id_group1 = geompy.addToStudy(group, "Group1")

# display the contents of the group
gg.createAndDisplayGO(id_group1)
salome.sg.updateObjBrowser()
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/working_with_groups_ex01.py)

## Adding an object to the group

```python
# Adding an object to the group

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create two vertices
p0 = geompy.MakeVertex(0.  , 0.  , 0.  )
p200 = geompy.MakeVertex(200., 200., 200.)

# create a box from two points
Box = geompy.MakeBoxTwoPnt(p0, p200)

# create a group from the faces of the box
group = geompy.CreateGroup(Box, geompy.ShapeType["FACE"])

# add objects to the group
SubFaceList = geompy.SubShapeAllSortedCentres(Box, geompy.ShapeType["FACE"])
for i in [0, 3, 5] :
    FaceID = geompy.GetSubShapeID(Box, SubFaceList[i])
    geompy.AddObject(group, FaceID)
id_group1 = geompy.addToStudy(group, "Group1")

# display the contents of the group
gg.createAndDisplayGO(id_group1)
salome.sg.updateObjBrowser()
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/working_with_groups_ex02.py)

## Removing an object from the group

```python
# Removing an object from the group

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

# create two vertices
p0 = geompy.MakeVertex(0.  , 0.  , 0.  )
p200 = geompy.MakeVertex(200., 200., 200.)

# create a box from two points
Box = geompy.MakeBoxTwoPnt(p0, p200)

# create a group from the faces of the box
group = geompy.CreateGroup(Box, geompy.ShapeType["FACE"])

# add objects to the group
SubFaceList = geompy.SubShapeAllSortedCentres(Box, geompy.ShapeType["FACE"])
for i in [0, 3, 5] :
    FaceID = geompy.GetSubShapeID(Box, SubFaceList[i])
    geompy.AddObject(group, FaceID)

# add all selected shapes from the list to the group
# (the program doesn't raise errors, if some shapes are already included)
geompy.UnionList(group, [SubFaceList[0], SubFaceList[2], SubFaceList[5]])

# remove an object from the group
geompy.RemoveObject(group, FaceID)
id_group1 = geompy.addToStudy(group, "Group1")

# display the contents of the group
gg.createAndDisplayGO(id_group1)
salome.sg.updateObjBrowser()
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/working_with_groups_ex03.py)

## Union Groups

```python
# Union Groups

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

# create a box and some groups of faces on it
Box_1 = geompy.MakeBoxDXDYDZ(200, 200, 200)
Group_1 = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_1, [13, 23])
Group_2 = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_2, [3, 27])
Group_3 = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_3, [33, 23])
Group_4 = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_4, [31, 27])

# union groups
Group_U_1_2 = geompy.UnionGroups(Group_1, Group_2)
Group_UL_3_4 = geompy.UnionListOfGroups([Group_3, Group_4])

# publish shapes
geompy.addToStudy(Box_1, 'Box_1')
geompy.addToStudyInFather(Box_1, Group_1, 'Group_1')
geompy.addToStudyInFather(Box_1, Group_2, 'Group_2')
geompy.addToStudyInFather(Box_1, Group_3, 'Group_3')
geompy.addToStudyInFather(Box_1, Group_4, 'Group_4')
geompy.addToStudyInFather(Box_1, Group_U_1_2, 'Group_U_1_2')
geompy.addToStudyInFather(Box_1, Group_UL_3_4, 'Group_UL_3_4')
salome.sg.updateObjBrowser()
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/working_with_groups_ex04.py)

## Intersect Groups

```python
# Intersect Groups

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

# create a box and some groups of faces on it
Box_1 = geompy.MakeBoxDXDYDZ(200, 200, 200)
Group_1 = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_1, [13, 23])
Group_2 = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_2, [3, 27])
Group_3 = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_3, [33, 23])
Group_4 = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_4, [31, 27])

# intersect groups
Group_I_1_3 = geompy.IntersectGroups(Group_1, Group_3)
Group_IL_1_3 = geompy.IntersectListOfGroups([Group_1, Group_3])

# publish shapes
geompy.addToStudy(Box_1, 'Box_1')
geompy.addToStudyInFather(Box_1, Group_1, 'Group_1')
geompy.addToStudyInFather(Box_1, Group_2, 'Group_2')
geompy.addToStudyInFather(Box_1, Group_3, 'Group_3')
geompy.addToStudyInFather(Box_1, Group_4, 'Group_4')
geompy.addToStudyInFather(Box_1, Group_I_1_3, 'Group_I_1_3')
geompy.addToStudyInFather(Box_1, Group_IL_1_3, 'Group_IL_1_3')
salome.sg.updateObjBrowser()
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/working_with_groups_ex05.py)

## Cut Groups

```python
# Cut Groups

import salome
salome.salome_init_without_session()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

# create a box and some groups of faces on it
Box_1 = geompy.MakeBoxDXDYDZ(200, 200, 200)
Group_1 = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_1, [13, 23])
Group_2 = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_2, [3, 27])
Group_3 = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_3, [33, 23])
Group_4 = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Group_4, [31, 27])

# cut groups
Group_C_2_4 = geompy.CutGroups(Group_2, Group_4)
Group_CL_2_4 = geompy.CutListOfGroups([Group_2], [Group_4])

# publish shapes
geompy.addToStudy(Box_1, 'Box_1')
geompy.addToStudyInFather(Box_1, Group_1, 'Group_1')
geompy.addToStudyInFather(Box_1, Group_2, 'Group_2')
geompy.addToStudyInFather(Box_1, Group_3, 'Group_3')
geompy.addToStudyInFather(Box_1, Group_4, 'Group_4')
geompy.addToStudyInFather(Box_1, Group_C_2_4, 'Group_C_2_4')
geompy.addToStudyInFather(Box_1, Group_CL_2_4, 'Group_CL_2_4')
salome.sg.updateObjBrowser()
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/working_with_groups_ex06.py)
