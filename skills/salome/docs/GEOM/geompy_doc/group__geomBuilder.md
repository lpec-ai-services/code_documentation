<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__geomBuilder.html -->

# geomBuilder Python module

## Detailed Description

By default, all functions of [geomBuilder](namespacegeomBuilder.md) Python module do not publish resulting geometrical objects. This can be done in the Python script by means of [addToStudy()](group__l1__publish__data.md#ga2df168cac27bab65dfb96e04b84a120d) or [addToStudyInFather()](group__l1__publish__data.md#ga014081af8bc7512b333cf71b995224a5) functions.

However, it is possible to publish result data in the study automatically. For this, almost each function of [geomBuilder](classgeomBuilder_1_1geomBuilder.md) class has an additional *theName* parameter (`None` by default). As soon as non-empty string value is passed to this parameter, the result object is published in the study automatically.

For example, consider the following Python script:

```python
import salome
from salome.geom import geomBuilder
geompy = geomBuilder.New()
box = geompy.MakeBoxDXDYDZ(100, 100, 100) # box is not published in the study yet
geompy.addToStudy(box, "box")             # explicit publishing
```

Last two lines can be replaced by one-line instruction:

```python
box = geompy.MakeBoxDXDYDZ(100, 100, 100, theName="box") # box is published in the study with "box" name
```

... or simply

```python
box = geompy.MakeBoxDXDYDZ(100, 100, 100, "box") # box is published in the study with "box" name
```

Note, that some functions produce more than one geometrical objects. For example, [GetNonBlocks()](group__l4__blocks__measure.md#gab6b25c60fdc58194140691671aa6d7ac) function returns two objects: group of all non-hexa solids and group of all non-quad faces. For such functions it is possible to specify separate names for results.

For example

```python
# create and publish cylinder
cyl = geompy.MakeCylinderRH(100, 100, "cylinder")
# get non blocks from cylinder
g1, g2 = geompy.GetNonBlocks(cyl, theName="nonblock")
```

Above example will publish both result compounds (first with non-hexa solids and second with non-quad faces) as two items, both named "nonblock". However, if second command is invoked as

```python
g1, g2 = geompy.GetNonBlocks(cyl, theName=("nonhexa", "nonquad"))
```

... the first compound will be published with "nonhexa" name, and second will be named "nonquad".

Automatic publication of all results can be also enabled/disabled by means of the function [addToStudyAuto()](group__l1__publish__data.md#ga5e79902a873c815eea08b843026b02ea). The automatic publishing is managed by the numeric parameter passed to this function:

- if *maxNbSubShapes* = 0, automatic publishing is disabled.
- if *maxNbSubShapes* = -1 (default), automatic publishing is enabled and maximum number of sub-shapes allowed for publishing is unlimited; any negative value passed as parameter has the same effect.
- if *maxNbSubShapes* is any positive value, automatic publishing is enabled and maximum number of sub-shapes allowed for publishing is set to specified value.

When automatic publishing is enabled, you even do not need to pass *theName* parameter to the functions creating objects, instead default names will be used. However, you can always change the behavior, by passing explicit name to the *theName* parameter and it will be used instead default one. The publishing of the collections of objects will be done according to the above mentioned rules (maximum allowed number of sub-shapes).

For example:

```python
import salome
from salome.geom import geomBuilder
geompy = geomBuilder.New()
geompy.addToStudyAuto() # enable automatic publication
box = geompy.MakeBoxDXDYDZ(100, 100, 100)
# the box is created and published in the study with default name
geompy.addToStudyAuto(5) # set max allowed number of sub-shapes to 5
vertices = geompy.SubShapeAll(box, geomBuilder.ShapeType['VERTEX'])
# only 5 first vertices will be published, with default names
print len(vertices)
# note, that result value still contains all 8 vertices
geompy.addToStudyAuto(-1) # disable automatic publication
```

This feature can be used, for example, for debugging purposes.

Note
:   - Use automatic publication feature with caution. When it is enabled, any function of [geomBuilder](classgeomBuilder_1_1geomBuilder.md) class publishes the results in the study, that can lead to the huge size of the study data tree. For example, repeating call of [SubShapeAll()](group__l4__decompose.md#ga1ad1978aabbdb5275f6724b5de17cc98) command on the same main shape each time will publish all child objects, that will lead to a lot of duplicated items in the study.
    - Sub-shapes are automatically published as child items of the parent main shape in the study if main shape was also published before. Otherwise, sub-shapes are published as top-level objects.
    - Some functions of [geomBuilder](classgeomBuilder_1_1geomBuilder.md) class do not have *theName* parameter (and, thus, do not support automatic publication). For example, some transformation operations like [TranslateDXDYDZ()](group__l3__transform.md#gaf7ce99add61b4facb1b427aefd1f9633). Refer to the documentation to check if some function has such possibility.

It is possible to customize the representation of the geometrical data in the data tree; this can be done by using folders. A folder can be created in the study tree using function [NewFolder()](group__l1__publish__data.md#ga160e797b630ed8a52d8745411e310bcd) (by default it is created under the "Geometry" root object). As soon as folder is created, any published geometry object can be moved into it.

For example:

```python
import salome
from salome.geom import geomBuilder
geompy = geomBuilder.New()
box = geompy.MakeBoxDXDYDZ(100, 100, 100, "Box")
# the box was created and published in the study
folder = geompy.NewFolder("Primitives")
# an empty "Primitives" folder was created under default "Geometry" root object
geompy.PutToFolder(box, folder)
# the box was moved into "Primitives" folder
```

Subfolders are also can be created by specifying another folder as a parent:

```python
subfolder = geompy.NewFolder("3D", folder)
# "3D" folder was created under "Primitives" folder
```

Note
:   - Folder container is just a representation layer object that deals with already published objects only. So, any geometry object should be published in the study (for example, with [addToStudy()](group__l1__publish__data.md#ga220ea9ea7cee165565b068dc80623b12) function) BEFORE moving it into any existing folder.
    - [PutToFolder()](group__l1__publish__data.md#ga220ea9ea7cee165565b068dc80623b12) function does not change physical position of geometry object in the study tree, it only affects on the representation of the data tree.
    - It is impossible to publish geometry object using any folder as father.
