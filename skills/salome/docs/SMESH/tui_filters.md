<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/tui_filters.html -->

# Filters usage

Filters allow picking only the mesh elements satisfying to a
specific condition or a set of conditions. Filters can be used to create
or edit mesh groups, remove elements from the mesh, control
mesh quality by different parameters, etc.

Several filtering criteria can be combined together by using logical
operators *AND* and *OR*. In addition, a filtering criterion can
be reverted using logical operator *NOT*.

Mesh filters can use the functionality of mesh quality controls to filter
mesh nodes / elements by a specific characteristic (Area, Length, etc).

This page provides a short description of the existing mesh filters,
describes required parameters and gives simple examples of usage in
Python scripts.

**See also:** [Quality Controls](tui_quality_controls.md#tui-quality-controls-page)

## Aspect ratio

filters 2D mesh elements (faces) according to the aspect ratio value:

- element type should be *SMESH.FACE*
- functor type should be *SMESH.FT_AspectRatio*
- threshold is floating point value (aspect ratio)

```python
# Aspect ratio
# This script demonstrates various usages of filters

# create mesh
from mechanic import *

# get faces with aspect ratio > 2.5
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_AspectRatio, SMESH.FT_MoreThan, 2.5)
ids = mesh.GetIdsFromFilter(filter)
print("Number of faces with aspect ratio > 2.5:", len(ids))

# get faces with aspect ratio > 1.5
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_AspectRatio, '>', 1.5, mesh=mesh)
ids = filter.GetIDs()
print("Number of faces with aspect ratio > 1.5:", len(ids))

# copy the faces with aspect ratio > 1.5 to another mesh;
# this demonstrates that a filter can be used where usually a group or sub-mesh is acceptable
filter.SetMesh( mesh.GetMesh() ) # - actually non necessary as mesh is set at filter creation
mesh2 = smesh_builder.CopyMesh( filter, "AR > 1.5" )
print("Number of copied faces with aspect ratio > 1.5:", mesh2.NbFaces())

# create a group (Group on Filter) of faces with Aspect Ratio < 1.5
group = mesh.MakeGroup("AR < 1.5", SMESH.FACE, SMESH.FT_AspectRatio, '<', 1.5)
print("Number of faces with aspect ratio < 1.5:", group.Size())

# combine several criteria to Create a Group of only Triangular faces with Aspect Ratio < 1.5;
# note that contents of a GroupOnFilter is dynamically updated as the mesh changes
crit = [ smesh_builder.GetCriterion( SMESH.FACE, SMESH.FT_AspectRatio, '<', 1.5, BinaryOp=SMESH.FT_LogicalAND ),
         smesh_builder.GetCriterion( SMESH.FACE, SMESH.FT_ElemGeomType,'=', SMESH.Geom_TRIANGLE ) ]
triaGroup = mesh.MakeGroupByCriteria( "Tria AR < 1.5", crit )
print("Number of triangles with aspect ratio < 1.5:", triaGroup.Size())

# get range of values of Aspect Ratio of all faces in the mesh
aspects = mesh.GetMinMax( SMESH.FT_AspectRatio )
print("MESH: Min aspect = %s, Max aspect = %s" % ( aspects[0], aspects[1] ))

# get max value of Aspect Ratio of faces in triaGroup
grAspects = mesh.GetMinMax( SMESH.FT_AspectRatio, triaGroup )
print("GROUP: Max aspect = %s" % grAspects[1])

# get Aspect Ratio of an element
aspect = mesh.FunctorValue( SMESH.FT_AspectRatio, ids[0] )
print("Aspect ratio of the face %s = %s" % ( ids[0], aspect ))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/e6e1fd4d42fbbff32d1c89ac93bbff85/filters_ex01.py)

**See also:** [Aspect Ratio](tui_quality_controls.md#tui-aspect-ratio)

## Aspect ratio 3D

filters 3D mesh elements (volumes) according to the aspect ratio value:

- element type is *SMESH.VOLUME*
- functor type is *SMESH.FT_AspectRatio3D*
- threshold is floating point value (aspect ratio)

```python
# Aspect ratio 3D

# create mesh with volumes
from mechanic import *

# get volumes with aspect ratio < 2.0
filter = smesh_builder.GetFilter(SMESH.VOLUME, SMESH.FT_AspectRatio3D, SMESH.FT_LessThan, 2.0)
ids = mesh.GetIdsFromFilter(filter)
print("Number of volumes with aspect ratio < 2.0:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/d0fb578937382319f5ef39d5acc8f7b4/filters_ex02.py)

**See also:** [Aspect Ratio 3D](tui_quality_controls.md#tui-aspect-ratio-3d)

## Scaled Jacobian

filters 3D mesh elements (volumes) according to the scaled jacobian value:

- element type is *SMESH.VOLUME*
- functor type is *SMESH.FT_ScaledJacobian*
- threshold is floating point value

```python
# Scaled Jacobian

# create mesh with volumes
from mechanic import *

# get volumes with scaled jacobian > 0.75
filter = smesh_builder.GetFilter(SMESH.VOLUME, SMESH.FT_ScaledJacobian, SMESH.FT_MoreThan, 0.75 )
ids = mesh.GetIdsFromFilter(filter)
print("Number of volumes with scaled jacobian > 0.75:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/3c063ba12fe814f9289abdc6da7de52d/filters_ex40.py)

**See also:** [Scaled Jacobian](tui_quality_controls.md#tui-scaled-jacobian)

## Warping angle

filters 2D mesh elements (faces) according to the warping angle value:

- element type is *SMESH.FACE*
- functor type is *SMESH.FT_Warping*
- threshold is floating point value (warping angle)

```python
# Warping angle

# create mesh
from mechanic import *

# get faces with warping angle = 2.0e-13 with tolerance 5.0e-14
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Warping, "=", 2.0e-13, Tolerance=5.0e-14)
ids = mesh.GetIdsFromFilter(filter)
print("Number of faces with warping angle = 2.0e-13 (tolerance 5.0e-14):", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/3e601dfac5266e48aacd3b6b9650a0cc/filters_ex03.py)

**See also:** [Warping](tui_quality_controls.md#tui-warping)

## Warping 3D

filters 3D mesh elements (volumes) according to the maximum warping angle value of the faces of volumes:

- element type is *SMESH.VOLUME*
- functor type is *SMESH.FT_Warping3D*
- threshold is floating point value (warping angle)

```python
# Warping 3D

# create mesh
from mechanic import *

# get faces with warping angle = 2.0e-13 with tolerance 5.0e-14
filter = smesh_builder.GetFilter(SMESH.VOLUME, SMESH.FT_Warping3D, "=", 2.0e-13, Tolerance=5.0e-14)
ids = mesh.GetIdsFromFilter(filter)
print("Number of volumes with warping = 2.0e-13 (tolerance 5.0e-14):", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/068de6194d1e9b17c274eb19a9470257/filters_ex41.py)

**See also:** [Warping 3D](tui_quality_controls.md#tui-warping-3d)

## Minimum angle

filters 2D mesh elements (faces) according to the minimum angle value:

- element type is *SMESH.FACE*
- functor type is *SMESH.FT_MinimumAngle*
- threshold is floating point value (minimum angle)

```python
# Minimum angle

# create mesh
from mechanic import *

# get faces with minimum angle > 75
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_MinimumAngle,">", 75)
ids = mesh.GetIdsFromFilter(filter)
print("Number of faces with minimum angle > 75:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/f5257997dc2a6322acf7fc162f426cf5/filters_ex04.py)

**See also:** [Minimum Angle](tui_quality_controls.md#tui-minimum-angle)

## Taper

filters 2D mesh elements (faces) according to the taper value:

- element type is *SMESH.FACE*
- functor type is *SMESH.FT_Taper*
- threshold is floating point value (taper)

```python
# Taper

# create mesh
from mechanic import *

# get faces with taper < 1.e-15
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Taper, SMESH.FT_LessThan, 1.e-15)
ids = mesh.GetIdsFromFilter(filter)
print("Number of faces with taper < 1.e-15:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/26377a8a7d9d7a7c82c6cfadbf9f990a/filters_ex05.py)

**See also:** [Taper](tui_quality_controls.md#tui-taper)

## Skew

filters 2D mesh elements (faces) according to the skew value:

- element type is *SMESH.FACE*
- functor type is *SMESH.FT_Skew*
- threshold is floating point value (skew)

```python
# Skew

# create mesh
from mechanic import *

# get faces with skew > 50
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_Skew, SMESH.FT_MoreThan, 50)
ids = mesh.GetIdsFromFilter(filter)
print("Number of faces with skew > 50:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/b9a6ded169d876c04f809e49ef3e4f60/filters_ex06.py)

**See also:** [Skew](tui_quality_controls.md#tui-skew)

## Area

filters 2D mesh elements (faces) according to the area value:

- element type is *SMESH.FACE*
- functor type is *SMESH.FT_Area*
- threshold is floating point value (area)

```python
# Area

# create mesh
from mechanic import *

# get faces with area > 60 and < 90
criterion1 = smesh_builder.GetCriterion(SMESH.FACE, SMESH.FT_Area, SMESH.FT_MoreThan, 60)
criterion2 = smesh_builder.GetCriterion(SMESH.FACE, SMESH.FT_Area, SMESH.FT_LessThan, 90)
filter = smesh_builder.GetFilterFromCriteria([criterion1,criterion2], SMESH.FT_LogicalAND)
ids = mesh.GetIdsFromFilter(filter)
print("Number of faces with area in range (60,90):", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/2792513a62eada69c468e8997426b208/filters_ex07.py)

**See also:** [Area](tui_quality_controls.md#tui-area)

## Volume

filters 3D mesh elements (volumes) according to the volume value:

- element type is *SMESH.VOLUME*
- functor type is *SMESH.FT_Volume3D*
- threshold is floating point value (volume)

```python
# Volume

# create mesh with volumes
from mechanic import *

# get volumes faces with volume > 100
filter = smesh_builder.GetFilter(SMESH.VOLUME, SMESH.FT_Volume3D, SMESH.FT_MoreThan, 100)
ids = mesh.GetIdsFromFilter(filter)
print("Number of volumes with volume > 100:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/c8aaa3f7a5548b265b0292059a5503a0/filters_ex08.py)

**See also:** [Volume](tui_quality_controls.md#tui-volume)

## Free borders

filters 1D mesh elements (edges) which represent free borders of a mesh:

- element type is *SMESH.EDGE*
- functor type is *SMESH.FT_FreeBorders*
- threshold value is not required

```python
# Free borders

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create mesh
face = geom_builder.MakeFaceHW(100, 100, 1, theName="quadrangle")
mesh = smesh_builder.Mesh(face)
mesh.Segment().NumberOfSegments(10)
mesh.Triangle().MaxElementArea(25)
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# get all free borders
filter = smesh_builder.GetFilter(SMESH.EDGE, SMESH.FT_FreeBorders)
ids = mesh.GetIdsFromFilter(filter)
print("Number of edges on free borders:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/f075c61d522a66fb3b4e9fe45a2992af/filters_ex09.py)

**See also:** [Free Borders](tui_quality_controls.md#tui-free-borders)

## Free edges

filters 2D mesh elements (faces) having edges (i.e. links between
nodes, not mesh segments) belonging to one face of mesh only:

- element type is *SMESH.FACE*
- functor type is *SMESH.FT_FreeEdges*
- threshold value is not required

```python
# Free edges

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create mesh
face = geom_builder.MakeFaceHW(100, 100, 1)
geom_builder.addToStudy( face, "quadrangle" )
mesh = smesh_builder.Mesh(face)
mesh.Segment().NumberOfSegments(10)
mesh.Triangle().MaxElementArea(25)
if not mesh.Compute(): raise Exception("Error when computing Mesh")

# get all faces with free edges
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_FreeEdges)
ids = mesh.GetIdsFromFilter(filter)
print("Number of faces with free edges:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/5731b1e9731e896b997a936a0ceadadb/filters_ex10.py)

**See also:** [Free Edges](tui_quality_controls.md#tui-free-edges)

## Free nodes

filters free nodes:

- element type is *SMESH.NODE*
- functor type is *SMESH.FT_FreeNodes*
- threshold value is not required

```python
# Free nodes

# create mesh
from mechanic import *

# add node
mesh.AddNode(0,0,0)

# get all free nodes
filter = smesh_builder.GetFilter(SMESH.NODE, SMESH.FT_FreeNodes)
ids = mesh.GetIdsFromFilter(filter)
print("Number of free nodes:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/98f8be45aeed46307c6bfa79b5e49d10/filters_ex11.py)

**See also:** [Free Nodes](tui_quality_controls.md#tui-free-nodes)

## Free faces

filters free faces:

- element type is *SMESH.FACE*
- functor type is *SMESH.FT_FreeFaces*
- threshold value is not required

```python
# Free faces

# create mesh
from mechanic import *

# get all free faces
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_FreeFaces)
ids = mesh.GetIdsFromFilter(filter)
print("Number of free faces:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/0622f72ac208534552eac641f931972f/filters_ex12.py)

**See also:** [Free Faces](tui_quality_controls.md#tui-free-faces)

## Bare border faces

filters faces with bare borders:

- element type is *SMESH.FACE*
- functor type is *SMESH.FT_BareBorderFace*
- threshold value is not required

```python
# Bare border faces

# create mesh
from mechanic import *

# remove some faces to have faces with bare borders
mesh.RemoveElements( mesh.GetElementsByType(SMESH.FACE)[0:5] )

# get all faces with bare borders
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_BareBorderFace)
ids = mesh.GetIdsFromFilter(filter)
print("Faces with bare borders:", ids)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/3097e10678622e835b683855b2deba18/filters_ex13.py)

**See also:** [Bare border faces](tui_quality_controls.md#tui-bare-border-faces)

## Coplanar faces

filters coplanar faces:

- element type is *SMESH.FACE*
- functor type is *SMESH.FT_CoplanarFaces*
- threshold value is the face ID
- tolerance is in degrees

```python
# Coplanar faces

# create mesh
from mechanic import *

faceID = mesh.GetElementsByType(SMESH.FACE)[0]
# get all faces co-planar to the first face with tolerance 5 degrees
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_CoplanarFaces,faceID,Tolerance=5.0)
ids = mesh.GetIdsFromFilter(filter)
print("Number of faces coplanar with the first one:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/6563f4b61ad4e1ef647daab5adc6885b/filters_ex14.py)

## Over-constrained faces

filters over-constrained faces:

- element type is *SMESH.FACE*
- functor type is *SMESH.FT_OverConstrainedFace*
- threshold value is not required

```python
# Over-constrained faces

# create mesh
from mechanic import *

# get all over-constrained faces
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_OverConstrainedFace)
ids = mesh.GetIdsFromFilter(filter)
print("Over-constrained faces:", ids)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/c0d7d73c8da20e773a6c37beeb323cae/filters_ex15.py)

**See also:** [Over-constrained faces](tui_quality_controls.md#tui-over-constrained-faces)

### Double edges, Double faces, Double volumes

filters mesh elements basing on the same set of nodes:

- element type is either *SMESH.EDGE*, *SMESH.FACE* or *SMESH.VOLUME*
- functor type is either *SMESH.FT_EqualEdges*, *SMESH.FT_EqualFaces* or *SMESH.FT_EqualVolumes*,
- threshold value is not required

```python
# Double edges, Double faces, Double volumes

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# make a mesh on a box
box = geom_builder.MakeBoxDXDYDZ(100,100,100)
mesh = smesh_builder.Mesh( box, "Box" )
mesh.Segment().NumberOfSegments(10)
mesh.Quadrangle()
mesh.Hexahedron()
if not mesh.Compute(): raise Exception("Error when computing Mesh")
# copy all elements with translation and Merge nodes
mesh.TranslateObject( mesh, smesh_builder.MakeDirStruct( 10,0,0), Copy=True )
mesh.MergeNodes( mesh.FindCoincidentNodes(1e-7) )
# create filters to find equal elements
equalEdgesFilter   = smesh_builder.GetFilter(SMESH.EDGE, SMESH.FT_EqualEdges)
equalFacesFilter   = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_EqualFaces)
equalVolumesFilter = smesh_builder.GetFilter(SMESH.VOLUME, SMESH.FT_EqualVolumes)
# get equal elements
print("Number of equal edges:",   len( mesh.GetIdsFromFilter( equalEdgesFilter )))
print("Number of equal faces:",   len( mesh.GetIdsFromFilter( equalFacesFilter )))
print("Number of equal volumes:", len( mesh.GetIdsFromFilter( equalVolumesFilter )))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/c2e0cb1877a9042658f25454e17a2fa8/filters_ex16.py)

## Double nodes

filters mesh nodes which are coincident with other nodes (within a given tolerance):

- element type is *SMESH.NODE*
- functor type is *SMESH.FT_EqualNodes*
- threshold value is not required
- default tolerance is 1.0e-7

```python
# Double nodes

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# make a mesh on a box
box = geom_builder.MakeBoxDXDYDZ(100,100,100)
mesh = smesh_builder.Mesh( box, "Box" )
mesh.Segment().NumberOfSegments(10)
mesh.Quadrangle()
mesh.Hexahedron()
if not mesh.Compute(): raise Exception("Error when computing Mesh")
# copy all elements with translation
mesh.TranslateObject( mesh, [10,0,0], Copy=True )
# create  a filter to find nodes equal within tolerance of 1e-5
filter = smesh_builder.GetFilter(SMESH.NODE, SMESH.FT_EqualNodes, Tolerance=1e-5)
# get equal nodes
print("Number of equal nodes:", len( mesh.GetIdsFromFilter( filter )))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/0a60eb81476f4904ec0dc343c5cfaebc/filters_ex17.py)

## Node connectivity number

filters nodes according to a number of elements of highest dimension connected to a node:

- element type should be *SMESH.NODE*
- functor type should be *SMESH.FT_NodeConnectivityNumber*
- threshold is an integer value (number of elements)

```python
# Number of connectivities of a node

# create a mesh
from mechanic import *

# get nodes connected to more than 6 tetrahedra
conn_nb_filter = smesh_builder.GetFilter(SMESH.NODE, SMESH.FT_NodeConnectivityNumber,'>', 6 )
ids = mesh.GetIdsFromFilter( conn_nb_filter )
print("Number of nodes connected to more than 6 tetrahedra:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/9f6a49b0c3d44600ea0d61e3717ba804/filters_node_nb_conn.py)

## Borders at multi-connection

filters 1D mesh elements (segments) according to the specified number of
connections (faces and volumes on whose border the segment lies):

- element type is *SMESH.EDGE*
- functor type is *SMESH.FT_MultiConnection*
- threshold is integer value (number of connections)

```python
# Borders at multi-connection

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# make a mesh on a box
box = geom_builder.MakeBoxDXDYDZ(100,100,100)
mesh = smesh_builder.Mesh( box, "Box" )
mesh.Segment().NumberOfSegments(10)
mesh.Quadrangle()
mesh.Hexahedron()
if not mesh.Compute(): raise Exception("Error when computing Mesh")
# copy all elements with translation and merge nodes
mesh.TranslateObject( mesh, [10,0,0], Copy=True )
mesh.MergeNodes( mesh.FindCoincidentNodes( 1e-5 ))

# get mesh edges with number of connected elements (faces and volumes) == 3
filter = smesh_builder.GetFilter(SMESH.EDGE, SMESH.FT_MultiConnection, 3)
ids = mesh.GetIdsFromFilter(filter)
print("Number of border edges with 3 faces connected:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/af6317fd7862ef9a2df7b161a6fac3f9/filters_ex18.py)

**See also:** [Borders at Multiconnection](tui_quality_controls.md#tui-borders-at-multiconnection)

## Borders at multi-connection 2D

filters 2D mesh elements (faces) with the specified maximal number of
faces connected to a border (link between nodes, not mesh segment):

- element type is *SMESH.FACE*
- functor type is *SMESH.FT_MultiConnection2D*
- threshold is integer value (number of connections)

```python
# Borders at multi-connection 2D

# create mesh
from mechanic import *

# get faces which consist of edges belonging to 2 mesh elements
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_MultiConnection2D, 2)
ids = mesh.GetIdsFromFilter(filter)
print("Number of faces consisting of edges belonging to 2 faces:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/bea19044c874da42538ffd8b7c6bbd3a/filters_ex19.py)

**See also:** [Borders at Multiconnection 2D](tui_quality_controls.md#tui-borders-at-multiconnection-2d)

## Length

filters 1D mesh elements (edges) according to the edge length value:

- element type should be *SMESH.EDGE*
- functor type should be *SMESH.FT_Length*
- threshold is floating point value (length)

```python
# Length

# create mesh
from mechanic import *

# get edges with length > 14
filter = smesh_builder.GetFilter(SMESH.EDGE, SMESH.FT_Length, SMESH.FT_MoreThan, 14)
ids = mesh.GetIdsFromFilter(filter)
print("Number of edges with length > 14:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/6cb693cb710ef618e28ae1f74a243aff/filters_ex20.py)

**See also:** [Length 1D](tui_quality_controls.md#tui-length-1d)

## Length 2D

filters 2D mesh elements (faces) according to the maximum length of its
edges (links between nodes):

- element type should be *SMESH.FACE*
- functor type should be *SMESH.FT_Length2D*
- threshold is floating point value (edge length)

```python
# Length 2D

# create mesh
from mechanic import *

# get all faces that have edges with length > 14
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_MaxElementLength2D, SMESH.FT_MoreThan, 14)
ids = mesh.GetIdsFromFilter(filter)
print("Number of faces with maximum edge length > 14:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/4a12d46a310d549de5f80ec06dceedad/filters_ex21.py)

**See also:** [Length 2D](tui_quality_controls.md#tui-length-2d)

## Element Diameter 2D

filters 2D mesh elements (faces) according to the maximum length
of its edges and diagonals:

- element type should be *SMESH.FACE*
- functor type should be *SMESH.FT_MaxElementLength2D*
- threshold is floating point value (length)

```python
# Element Diameter 2D

# create mesh
from mechanic import *

# get all faces that have elements with length > 10
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_MaxElementLength2D, SMESH.FT_MoreThan, 10)
ids = mesh.GetIdsFromFilter(filter)
print("Number of faces with maximum element length > 10:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/a9f1f0f1e7234c993804cacc130f239d/filters_ex22.py)

**See also:** [Element Diameter 2D](tui_quality_controls.md#tui-max-element-length-2d)

## Element Diameter 3D

filters 3D mesh elements (volumes) according to the maximum length
of its edges and diagonals:

- element type should be *SMESH.VOLUME*
- functor type should be *SMESH.FT_MaxElementLength3D*
- threshold is floating point value (edge/diagonal length)

```python
# Element Diameter 3D

# create mesh with volumes
from mechanic import *

# get all volumes that have elements with length > 10
filter = smesh_builder.GetFilter(SMESH.VOLUME, SMESH.FT_MaxElementLength3D, SMESH.FT_MoreThan, 10)
ids = mesh.GetIdsFromFilter(filter)
print("Number of volumes with maximum element length > 10:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/6d47af40a9c59e63e162640454c69246/filters_ex23.py)

**See also:** [Element Diameter 3D](tui_quality_controls.md#tui-max-element-length-3d)

## Bare border volumes

filters 3D mesh elements with bare borders, i.e. having a facet not
shared with other volumes and without a face on it:

- element type is *SMESH.VOLUME*
- functor type is *SMESH.FT_BareBorderVolume*
- threshold value is not required

```python
# Bare border volumes

# create mesh
from mechanic import *

# remove some volumes to have volumes with bare borders
mesh.RemoveElements(mesh.GetElementsByType(SMESH.VOLUME)[0:5])
# get all volumes with bare borders
filter = smesh_builder.GetFilter(SMESH.VOLUME, SMESH.FT_BareBorderVolume)
ids = mesh.GetIdsFromFilter(filter)
print("Volumes with bare borders:", ids)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/fe855bf6b567889807aa9c0afbbf89ff/filters_ex24.py)

**See also:** [Bare border volumes](tui_quality_controls.md#tui-bare-border-volumes)

## Over-constrained volumes

filters over-constrained volumes, whose all nodes are on the mesh boundary:

- element type is *SMESH.VOLUME*
- functor type is *SMESH.FT_OverConstrainedVolume*
- threshold value is not required

```python
# Over-constrained volumes

# create mesh
from mechanic import *

# get all over-constrained volumes
filter = smesh_builder.GetFilter(SMESH.VOLUME, SMESH.FT_OverConstrainedVolume)
ids = mesh.GetIdsFromFilter(filter)
print("Over-constrained volumes:", ids)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/b3485cf03e49ba6a4e002d7e5719cd6e/filters_ex25.py)

**See also:** [Over-constrained faces](tui_quality_controls.md#tui-over-constrained-faces)

## Belong to Mesh Group

filters mesh entities (nodes or elements) included in a mesh group
defined by threshold value:

- element type can be any, from *SMESH.NODE* to *SMESH.BALL*
- functor type should be *SMESH.FT_BelongToMeshGroup*
- threshold is mesh group object

```python
# Belong to Mesh Group criterion

# create mesh
from mechanic import *

# create a group of all faces (quadrangles) generated on sub_face3
quads_on_face3 = mesh.MakeGroup("quads_on_face3", SMESH.FACE, SMESH.FT_BelongToGeom,'=',sub_face3)
print("There are %s quadrangles generated on '%s' and included in the group '%s'" % ( quads_on_face3.Size(), sub_face3.GetName(), quads_on_face3.GetName() ))

# create a group of all the rest quadrangles, generated on other faces by combining 2 criteria:
# - negated FT_BelongToMeshGroup to select elements not included in quads_on_face3
# - FT_ElemGeomType to select quadrangles
not_on_face3 = smesh_builder.GetCriterion( SMESH.FACE, SMESH.FT_BelongToMeshGroup,'=',quads_on_face3, SMESH.FT_LogicalNOT )
quadrangles  = smesh_builder.GetCriterion( SMESH.FACE, SMESH.FT_ElemGeomType,'=',SMESH.Geom_QUADRANGLE )

rest_quads = mesh.MakeGroupByCriteria("rest_quads", [ not_on_face3, quadrangles ])
print("'%s' group includes all the rest %s quadrangles" % ( rest_quads.GetName(), rest_quads.Size() ))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/fbe2862eaf41b3bf0bf5056583677d8a/filters_belong2group.py)

## Belong to Geom

filters mesh entities (nodes or elements) which all nodes lie on the
shape defined by threshold value:

- element type can be any, from *SMESH.NODE* to *SMESH.BALL*
- functor type should be *SMESH.FT_BelongToGeom*
- threshold is geometrical object
- tolerance is a distance between a node and the geometrical object; it is used if an node is not associated to any geometry.

```python
# Belong to Geom

# create mesh
from mechanic import *

# get all faces which nodes lie on the face sub_face3
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_BelongToGeom, sub_face3)
ids = mesh.GetIdsFromFilter(filter)
print("Number of faces which nodes lie on sub_face3:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/137b1dde080185ec7b3d007595299a8a/filters_ex26.py)

## Lying on Geom

filters mesh entities (nodes or elements) at least one node of which lies on the
shape defined by threshold value:

- element type can be any, from *SMESH.NODE* to *SMESH.BALL*
- functor type should be *SMESH.FT_LyingOnGeom*
- threshold is geometrical object
- tolerance is a distance between a node and the geometrical object;

it is used if an node is not associated to any geometry.

```python
# Lying on Geom

# create mesh
from mechanic import *

# get all faces at least one node of each lies on the face sub_face3
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_LyingOnGeom, sub_face3)
ids = mesh.GetIdsFromFilter(filter)
print("Number of faces at least one node of each lies on sub_face3:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/41211628178a80fc4b232817c209e34e/filters_ex27.py)

## Belong to Plane

filters mesh entities (nodes or elements) which all nodes belong to the
plane defined by threshold value with the given tolerance:

- element type can be any except *SMESH.VOLUME*
- functor type should be *SMESH.FT_BelongToPlane*
- threshold is geometrical object (plane)
- default tolerance is 1.0e-7

```python
# Belong to Plane

# create mesh
from mechanic import *

# create plane
plane_1 = geom_builder.MakePlane(p3,seg1,2000)
geom_builder.addToStudy(plane_1, "plane_1")

# get all nodes which lie on the plane \a plane_1
filter = smesh_builder.GetFilter(SMESH.NODE, SMESH.FT_BelongToPlane, plane_1)
ids = mesh.GetIdsFromFilter(filter)
print("Number of nodes which lie on the plane plane_1:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/535550cf62c3da0181f527f840a1676a/filters_ex28.py)

## Belong to Cylinder

filters mesh entities (nodes or elements) which all nodes belong to the
cylindrical face defined by threshold value with the given tolerance:

- element type can be any except *SMESH.VOLUME*
- functor type should be *SMESH.FT_BelongToCylinder*
- threshold is geometrical object (cylindrical face)
- default tolerance is 1.0e-7

```python
# Belong to Cylinder

# create mesh
from mechanic import *

# get all faces which lie on the cylindrical face \a sub_face1
filter = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_BelongToCylinder, sub_face1)
ids = mesh.GetIdsFromFilter(filter)
print("Number of faces which lie on the cylindrical surface sub_face1:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/e9b045bfa356760779f3c2b99c2a4270/filters_ex29.py)

## Belong to Surface

filters mesh entities (nodes or elements) which all nodes belong to the
arbitrary surface defined by threshold value with the given tolerance:

- element type can be any except *SMESH.VOLUME*
- functor type should be *SMESH.FT_BelongToGenSurface*
- threshold is geometrical object (arbitrary surface)
- default tolerance is 1.0e-7

```python
# Belong to Surface

# create mesh
from mechanic import *

# create b-spline
spline_1 = geom_builder.MakeInterpol([p4,p6,p3,p1])
surface_1 = geom_builder.MakePrismVecH( spline_1, vz, 70.0 )
geom_builder.addToStudy(surface_1, "surface_1")

# get all nodes which lie on the surface \a surface_1
filter = smesh_builder.GetFilter(SMESH.NODE, SMESH.FT_BelongToGenSurface, surface_1)
ids = mesh.GetIdsFromFilter(filter)
print("Number of nodes which lie on the surface surface_1:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/b67b5ecaae90e05a88963d1d9a55f32b/filters_ex30.py)

## Range of IDs

filters mesh entities elements (nodes or elements) according to the
specified identifiers range:

- element type can be any, from *SMESH.NODE* to *SMESH.BALL*
- functor type is *SMESH.FT_RangeOfIds*
- threshold is string listing required IDs and/or ranges of IDs, e.g.”1,2,3,50-60,63,67,70-78”

```python
# Range of IDs

# create mesh
from mechanic import *

# get nodes with identifiers [5-10] and [15-30]
criterion1 = smesh_builder.GetCriterion(SMESH.NODE, SMESH.FT_RangeOfIds, Threshold="5-10",\
                                        BinaryOp=SMESH.FT_LogicalOR)
criterion2 = smesh_builder.GetCriterion(SMESH.NODE, SMESH.FT_RangeOfIds, Threshold="15-30")
filter = smesh_builder.CreateFilterManager().CreateFilter()
filter.SetCriteria([criterion1,criterion2])
ids = mesh.GetIdsFromFilter(filter)
print("Number of nodes in ranges [5-10] and [15-30]:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/1a3656628608f77a926e18e1e847e1dd/filters_ex31.py)

## Badly oriented volume

filters 3D mesh elements (volumes), which are incorrectly oriented from
the point of view of MED convention.

- element type should be *SMESH.VOLUME*
- functor type is *SMESH.FT_BadOrientedVolume*
- threshold is not required

```python
# Badly oriented volume

# create mesh with volumes
from mechanic import *

# get all badly oriented volumes
filter = smesh_builder.GetFilter(SMESH.VOLUME, SMESH.FT_BadOrientedVolume)
ids = mesh.GetIdsFromFilter(filter)
print("Number of badly oriented volumes:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/dba77082dc4f90829733ace5bb9ef912/filters_ex32.py)

## Linear / quadratic

filters linear / quadratic mesh elements:

- element type should be either *SMESH.EDGE*, *SMESH.FACE* or *SMESH.VOLUME*
- functor type is *SMESH.FT_LinearOrQuadratic*
- threshold is not required
- if unary operator is set to SMESH.FT_LogicalNOT, the quadratic elements are selected, otherwise (by default) linear elements are selected

```python
# Linear / quadratic

# create mesh
from mechanic import *

# get linear and quadratic edges
filter_linear    = smesh_builder.GetFilter(SMESH.EDGE, SMESH.FT_LinearOrQuadratic)
filter_quadratic = smesh_builder.GetFilter(SMESH.EDGE, SMESH.FT_LinearOrQuadratic, SMESH.FT_LogicalNOT)
ids_linear    = mesh.GetIdsFromFilter(filter_linear)
ids_quadratic = mesh.GetIdsFromFilter(filter_quadratic)
print("Number of linear edges:", len(ids_linear), "; number of quadratic edges:", len(ids_quadratic))

# convert mesh to quadratic
print("Convert to quadratic...")
mesh.ConvertToQuadratic()

# get linear and quadratic edges
ids_linear    = mesh.GetIdsFromFilter(filter_linear)
ids_quadratic = mesh.GetIdsFromFilter(filter_quadratic)
print("Number of linear edges:", len(ids_linear), "; number of quadratic edges:", len(ids_quadratic))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/cc8f576c7f23af337d33b08cd6bb216a/filters_ex33.py)

## Group color

filters mesh entities, belonging to the group with the color defined by the threshold value.

- element type can be any, from *SMESH.NODE* to *SMESH.BALL*
- functor type is *SMESH.FT_GroupColor*
- threshold should be of SALOMEDS.Color type

```python
# Group color

# create mesh
from mechanic import *

# create group of edges
all_edges = mesh.GetElementsByType(SMESH.EDGE)
grp = mesh.MakeGroupByIds("edges group", SMESH.EDGE, all_edges[:len(all_edges) // 4])
import SALOMEDS
c = SALOMEDS.Color(0.1, 0.5, 1.0)
grp.SetColor(c)
# get number of the edges not belonging to the group with the given color
filter = smesh_builder.GetFilter(SMESH.EDGE, SMESH.FT_GroupColor, c, SMESH.FT_LogicalNOT)
ids = mesh.GetIdsFromFilter(filter)
print ("Number of edges not belonging to the group with color (0.1, 0.5, 1.0):", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/7c81841da07896244bb6c2791ef55a3f/filters_ex34.py)

## Geometry type

filters mesh elements by the geometric type defined with the threshold
value. The list of available geometric types depends on the element
entity type.

- element type can be any, e.g.: *SMESH.EDGE*, *SMESH.FACE*, *SMESH.VOLUME*, etc.
- functor type should be *SMESH.FT_ElemGeomType*
- threshold is either of smesh.GeometryType values. Type *SMESH.GeometryType._items* in the Python Console to see all geometric types.

```python
# Geometry type

# create mesh with volumes
from mechanic import *

# get all triangles, quadrangles, tetrahedrons, pyramids
filter_tri = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_ElemGeomType, SMESH.Geom_TRIANGLE)
filter_qua = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_ElemGeomType, SMESH.Geom_QUADRANGLE)
filter_tet = smesh_builder.GetFilter(SMESH.VOLUME, SMESH.FT_ElemGeomType, SMESH.Geom_TETRA)
filter_pyr = smesh_builder.GetFilter(SMESH.VOLUME, SMESH.FT_ElemGeomType, SMESH.Geom_PYRAMID)
ids_tri = mesh.GetIdsFromFilter(filter_tri)
ids_qua = mesh.GetIdsFromFilter(filter_qua)
ids_tet = mesh.GetIdsFromFilter(filter_tet)
ids_pyr = mesh.GetIdsFromFilter(filter_pyr)
print("Number of triangles:", len(ids_tri))
print("Number of quadrangles:", len(ids_qua))
print("Number of tetrahedrons:", len(ids_tet))
print("Number of pyramids:", len(ids_pyr))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/bebb1b732bae9a5f7f821b4e2806e721/filters_ex35.py)

## Entity type

filters mesh elements by the geometric type and number of nodes.

- element type can be any, e.g.: *SMESH.EDGE*, *SMESH.FACE*, *SMESH.VOLUME*, etc.
- functor type should be *SMESH.FT_EntityType*
- threshold is either of SMESH.EntityType values. Type *SMESH.EntityType._items* in the Python Console to see all entity types.

```python
# Entity type

# create a mesh
from mechanic import *

# make the mesh quadratic
mesh.ConvertToQuadratic()
# make some elements bi-quadratic
for face in shape_faces[: len(shape_faces) // 2]:
    mesh.ConvertToQuadratic( theSubMesh=mesh.Group( face ), theToBiQuad=True )

# get triangles with 7 nodes
filter_tri = smesh_builder.GetFilter(SMESH.FACE, SMESH.FT_EntityType,'=', SMESH.Entity_BiQuad_Triangle )
ids_tri = mesh.GetIdsFromFilter(filter_tri)
print("Number of bi-quadratic triangles:", len(ids_tri))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/682dd6c35330c2d1cad99928cff196ab/filters_ex37.py)

## Ball diameter

filters ball elements by diameter.

- element type should be *SMESH.BALL*
- functor type should be *SMESH.FT_BallDiameter*
- threshold is floating point value (ball diameter)

```python
# Ball diameter

# create a mesh
from mechanic import *

# create several balls with increasing diameter
for i in range(1,10):
    diameter = float( i )
    mesh.AddBall( i, diameter )
    pass

# get balls with diameter > 5.
diam_filter = smesh_builder.GetFilter(SMESH.BALL, SMESH.FT_BallDiameter,'>', 5. )
ids = mesh.GetIdsFromFilter( diam_filter )
print("Number of balls with diameter > 5:", len(ids))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/5c2e2e3cc912757180ff56d1003f4cf5/filters_ex38.py)

## Elements of a domain

filters elements of a specified domain.

- element type can be any, e.g.: *SMESH.EDGE*, *SMESH.FACE*, *SMESH.VOLUME*, etc.
- functor type should be *SMESH.FT_ConnectedElements*
- threshold is either (1) node ID or (2) geometrical vertex or (3) 3 coordinates of a point.

```python
# "Elements of a domain" filter and "Renumber" hypothesis

import salome
salome.salome_init_without_session()

import SMESH
from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

geom_builder = geomBuilder.New()
smesh_builder = smeshBuilder.New()

# create two boxes to have two domains in the mesh

box1 = geom_builder.MakeBoxDXDYDZ( 100,100,100 )
box2 = geom_builder.MakeTranslation( box1, 200, 0, 0 )
boxes = geom_builder.MakeCompound( [box1, box2] )
box1, box2 = geom_builder.SubShapeAll( boxes, geom_builder.ShapeType["SHAPE"], "box")

vertex = geom_builder.SubShape( box1, geom_builder.ShapeType["VERTEX"], [1] )

# create a mesh

mesh = smesh_builder.Mesh( boxes )
mesh.Segment(box1).NumberOfSegments( 5 )  # to have different nb of elements on the boxes
mesh.Segment(box2).NumberOfSegments( 10 )
mesh.Quadrangle()
ijkAlgo = mesh.Hexahedron()

# Use Renumber hypothesis to get hexahedra and nodes numbered like in a structured mesh.
# k axis of box1 will be ( 100,100,0 ) - ( 100,100,100 )
# k axis of box2 will be ( 0,0,0 ) - (0,0,100), by default
v000 = geom_builder.MakeVertex( 100,100,0, theName='v000' ) # can use box sub-vertex or standalone one
v001 = geom_builder.GetVertexNearPoint( box1, geom_builder.MakeVertex(100,100,100), theName='v001')
ijkAlgo.Renumber([ smeshBuilder.BlockCS( box1, v000, v001 ) ])

if not mesh.Compute(): raise Exception("Error when computing Mesh")

# Create filters with FT_ConnectedElements criterion by pointing a domain in different ways:

# using point coordinates in box_1
nodeFilter = smesh_builder.GetFilter( SMESH.NODE, SMESH.FT_ConnectedElements, "=", "1.,2,10", mesh=mesh )
print("Nb. nodes in box_1:", len( nodeFilter.GetIDs()))

# using point coordinates in box_2
edgeFilter = smesh_builder.GetFilter( SMESH.EDGE, SMESH.FT_ConnectedElements, "=", [202,1,1 ], mesh=mesh )
print("Nb. segments in box_2:", len( edgeFilter.GetIDs()))

# using a geom vertex of box_1
faceFilter = smesh_builder.GetFilter( SMESH.FACE, SMESH.FT_ConnectedElements, "=", vertex, mesh=mesh )
print("Nb. faces in box_1:", len( edgeFilter.GetIDs()))

# using node ID in box_2
voluFilter = smesh_builder.GetFilter( SMESH.VOLUME, SMESH.FT_ConnectedElements, "=", 10, mesh=mesh )
print("Nb. volumes in box_2:", len( voluFilter.GetIDs()))
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/3e7ca2bf482eb8de750328b030a46634/filters_ex39.py)

## How to combine several criteria into a filter?

Several criteria can be combined into a filter.

```python
# Combine several criteria into a filter

# create mesh
from mechanic import *

# get all the quadrangle faces ...
criterion1 = smesh_builder.GetCriterion(SMESH.FACE, SMESH.FT_ElemGeomType, SMESH.Geom_QUADRANGLE, SMESH.FT_LogicalAND)
# ... but those from sub_face3
criterion2 = smesh_builder.GetCriterion(SMESH.FACE, SMESH.FT_BelongToGeom, sub_face3, SMESH.FT_LogicalNOT)

quadFilter = smesh_builder.GetFilterFromCriteria([criterion1,criterion2])

# get faces satisfying the criteria
ids = mesh.GetIdsFromFilter(quadFilter)

# create a group of faces satisfying the criteria
myGroup = mesh.GroupOnFilter(SMESH.FACE,"Quads_on_cylindrical_faces",quadFilter)
```

[`Download this script`](https://docs.salome-platform.org/latest/gui/SMESH/_downloads/30b361627f374d2e326033d031d02531/filters_ex36.py)
