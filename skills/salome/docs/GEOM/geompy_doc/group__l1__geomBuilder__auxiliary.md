<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l1__geomBuilder__auxiliary.html -->

# Auxiliary data structures and methods geomBuilder Python module

## Detailed Description

## Function Documentation

### RaiseIfFailed()

```python
def geomBuilder.RaiseIfFailed(Method_name, Operation)
```

Raise an Error, containing the Method_name, if Operation is Failed.

### ParseParameters()

```python
def geomBuilder.ParseParameters(parameters)
```

Return list of variables value from salome notebook.

### ParseList()

```python
def geomBuilder.ParseList(list)
```

Return list of variables value from salome notebook.

### ParseSketcherCommand()

```python
def geomBuilder.ParseSketcherCommand(command)
```

Return list of variables value from salome notebook.

### PackData()

```python
def geomBuilder.PackData(data)
```

Helper function which can be used to pack the passed string to the byte data.

Only '1' an '0' symbols are valid for the string. The missing bits are replaced by zeroes. If the string contains invalid symbol (neither '1' nor '0'), the function raises an exception. For example,

```python
val = PackData("10001110") # val = 0xAE
val = PackData("1")        # val = 0x80
```

Parameters
:   |  |  |
    | --- | --- |
    | data | unpacked data - a string containing '1' and '0' symbols |

Returns
:   data packed to the byte stream

### ReadTexture()

```python
def geomBuilder.ReadTexture(fname)
```

Read bitmap texture from the text file.

In that file, any non-zero symbol represents '1' opaque pixel of the bitmap. A zero symbol ('0') represents transparent pixel of the texture bitmap. The function returns width and height of the pixmap in pixels and byte stream representing texture bitmap itself.

This function can be used to read the texture to the byte stream in order to pass it to the AddTexture() function of [geomBuilder](namespacegeomBuilder.md) class. For example,

```python
from salome.geom import geomBuilder
geompy = geomBuilder.New()
texture = geompy.readtexture('mytexture.dat')
texture = geompy.AddTexture(*texture)
obj.SetMarkerTexture(texture)
```

Parameters
:   |  |  |
    | --- | --- |
    | fname | texture file name |

Returns
:   sequence of tree values: texture's width, height in pixels and its byte stream

### EnumToLong()

```python
def geomBuilder.EnumToLong(theItem)
```

Returns a long value from enumeration type Can be used for CORBA enumerator types like [GEOM.shape_type](namespaceGEOM.md#a82a00e336c65dad4cc04b65563b26eb5).

Parameters
:   |  |  |
    | --- | --- |
    | theItem | enumeration type |

### init_geom()

```python
def init_geom(self)
```

### GetPluginOperations()

```python
def GetPluginOperations(self, libraryName)
```

### DumpPython()

```python
def DumpPython(self, theIsPublished = True, theIsMultiFile = True)
```

Dump component to the Python script This method overrides IDL function to allow default values for the parameters.

### SubShapeName()

```python
def SubShapeName(self, aSubObj, aMainObj)
```

Get name for sub-shape aSubObj of shape aMainObj.

[Example](../tui_test_all_page.md#swig_SubShapeName)

### hideInStudy()

```python
def hideInStudy(self, obj)
```

Unpublish object in study.

Parameters
:   |  |  |
    | --- | --- |
    | obj | the object to be unpublished |

### MakeCopy()

```python
def MakeCopy(self, theOriginal, theName = None)
```

Create a copy of the given object.

Parameters
:   |  |  |
    | --- | --- |
    | theOriginal | geometry object for copy |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New GEOM_Object, containing the copied shape.

[Example](../tui_test_all_page.md#swig_MakeCopy)

### addPath()

```python
def addPath(self, Path)
```

Add Path to load python scripts from.

Parameters
:   |  |  |
    | --- | --- |
    | Path | a path to load python scripts from |

### LoadTexture()

```python
def LoadTexture(self, Path)
```

Load marker texture from the file.

Parameters
:   |  |  |
    | --- | --- |
    | Path | a path to the texture file |

Returns
:   unique texture identifier

### getObjectID()

```python
def getObjectID(self, obj)
```

Get internal name of the object based on its study entry.

Note
:   This method does not provide an unique identifier of the geometry object.
:   This is internal function of [GEOM](namespaceGEOM.md) component, though it can be used outside it for appropriate reason (e.g. for identification of geometry object).

Parameters
:   |  |  |
    | --- | --- |
    | obj | geometry object |

Returns
:   unique object identifier

### AddTexture()

```python
def AddTexture(self, Width, Height, Texture, RowData = False)
```

Add marker texture.

*Width* and *Height* parameters specify width and height of the texture in pixels. If *RowData* is `True`, *Texture* parameter should represent texture data packed into the byte array. If *RowData* is `False` (default), *Texture* parameter should be unpacked string, in which '1' symbols represent opaque pixels and '0' represent transparent pixels of the texture bitmap.

Parameters
:   |  |  |
    | --- | --- |
    | Width | texture width in pixels |
    | Height | texture height in pixels |
    | Texture | texture data |
    | RowData | if `True`, *Texture* data are packed in the byte stream |

Returns
:   unique texture identifier

### TransferData()

```python
def TransferData(self, theObjectFrom, theObjectTo, theFindMethod = GEOM.FSM_GetInPlace)
```

Transfer not topological data from one [GEOM](namespaceGEOM.md) object to another.

Parameters
:   |  |  |
    | --- | --- |
    | theObjectFrom | the source object of non-topological data |
    | theObjectTo | the destination object of non-topological data |
    | theFindMethod | method to search sub-shapes of theObjectFrom in shape theObjectTo. Possible values are: [GEOM.FSM_GetInPlace](namespaceGEOM.md#a4d764798e5127e57ed43bd2da68a613ea8d5ebcfdf2f81affbc89309f798413dd), [GEOM.FSM_GetInPlaceByHistory](namespaceGEOM.md#a4d764798e5127e57ed43bd2da68a613ea0ff71cf4eaee66c013d024c80f860474) and [GEOM.FSM_GetInPlace_Old](namespaceGEOM.md#a4d764798e5127e57ed43bd2da68a613ea05095964f7d9393ee01e934419c2509e). Other values of [GEOM.find_shape_method](namespaceGEOM.md#a4d764798e5127e57ed43bd2da68a613e) are not supported. |

Returns
:   True in case of success; False otherwise.

[Example](../tui_test_others_page.md#swig_TransferData)

## Variable Documentation

### ShapeType

```python
dictionary ShapeType = {"AUTO":-1, "COMPOUND":0, "COMPSOLID":1, "SOLID":2, "SHELL":3, "FACE":4, "WIRE":5, "EDGE":6, "VERTEX":7, "SHAPE":8, "FLAT":9} static
```

Enumeration ShapeType as a dictionary.

Topological types of shapes (like Open Cascade types). See [GEOM::shape_type](namespaceGEOM.md#a82a00e336c65dad4cc04b65563b26eb5) for details.

### kind

```python
kind = GEOM.GEOM_IKindOfShape static
```

Kinds of shape in terms of *[GEOM.GEOM_IKindOfShape.shape_kind](interfaceGEOM_1_1GEOM__IKindOfShape.md#a89b3365676a2806c547d5bc9bf4d9d7c)* enumeration and a list of parameters, describing the shape.

List of parameters, describing the shape:

- COMPOUND: [nb_solids nb_faces nb_edges nb_vertices]
- COMPSOLID: [nb_solids nb_faces nb_edges nb_vertices]
- SHELL: [[info.CLOSED](classgeomBuilder_1_1info.md#aa19ecea375a9ef477169a10d3003ec4e) / [info.UNCLOSED](classgeomBuilder_1_1info.md#a8e480b6fefe80a7761a8a7c6799dd7ac) nb_faces nb_edges nb_vertices]
- WIRE: [[info.CLOSED](classgeomBuilder_1_1info.md#aa19ecea375a9ef477169a10d3003ec4e) / [info.UNCLOSED](classgeomBuilder_1_1info.md#a8e480b6fefe80a7761a8a7c6799dd7ac) nb_edges nb_vertices]
- SPHERE: [xc yc zc R]
- CYLINDER: [xb yb zb dx dy dz R H]
- BOX: [xc yc zc ax ay az]
- ROTATED_BOX: [xc yc zc zx zy zz xx xy xz ax ay az]
- TORUS: [xc yc zc dx dy dz R_1 R_2]
- CONE: [xb yb zb dx dy dz R_1 R_2 H]
- POLYHEDRON: [nb_faces nb_edges nb_vertices]
- SOLID: [nb_faces nb_edges nb_vertices]
- SPHERE2D: [xc yc zc R]
- CYLINDER2D: [xb yb zb dx dy dz R H]
- TORUS2D: [xc yc zc dx dy dz R_1 R_2]
- CONE2D: [xc yc zc dx dy dz R_1 R_2 H]
- DISK_CIRCLE: [xc yc zc dx dy dz R]
- DISK_ELLIPSE: [xc yc zc dx dy dz R_1 R_2]
- POLYGON: [xo yo zo dx dy dz nb_edges nb_vertices]
- PLANE: [xo yo zo dx dy dz]
- PLANAR: [xo yo zo dx dy dz nb_edges nb_vertices]
- FACE: [nb_edges nb_vertices]
- CIRCLE: [xc yc zc dx dy dz R]
- ARC_CIRCLE: [xc yc zc dx dy dz R x1 y1 z1 x2 y2 z2]
- ELLIPSE: [xc yc zc dx dy dz R_1 R_2 v1x v1y v1z v2x v2y v2z]
- ARC_ELLIPSE: [xc yc zc dx dy dz R_1 R_2 x1 y1 z1 x2 y2 z2 v1x v1y v1z v2x v2y v2z]
- LINE: [xo yo zo dx dy dz]
- SEGMENT: [x1 y1 z1 x2 y2 z2]
- CRV_BSPLINE: [periodicity degree nb_poles nb_knots nb_weights nb_multiplicities xi yi zi ki wi mi]
- CRV_BEZIER: [nb_poles nb_weights xi yi zi wi]
- HYPERBOLA: [xc yc zc dx dy dz R_1 R_2 v1x v1y v1z v2x v2y v2z]
- PARABOLA: [xc yc zc dx dy dz F v1x v1y v1z v2x v2y v2z]
- EDGE: [nb_vertices]
- VERTEX: [x y z]
- LCS: [x y z xx xy xz yx yy yz zx zy zz]
