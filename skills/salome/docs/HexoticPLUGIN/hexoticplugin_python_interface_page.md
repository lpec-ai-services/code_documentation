<!-- source: https://docs.salome-platform.org/latest/gui/HexoticPLUGIN/hexoticplugin_python_interface_page.html -->

# Python Interface

Note
:   The former name of MG-Hexa mesher is *Hexotic* and names of the corresponding classes and modules still include *"Hexotic"*.

Python package [HexoticPLUGINBuilder](../HexoticPLUGIN/hexoticpluginpy_doc/namespaceHexoticPLUGINBuilder.md) defines [HexoticPLUGINBuilder.Hexotic_Algorithm](../HexoticPLUGIN/hexoticpluginpy_doc/classHexoticPLUGINBuilder_1_1Hexotic__Algorithm.md) class providing access to the MG-Hexa meshing algorithm and its parameters.

You can get an instance of this class by calling [smeshBuilder.Mesh.Hexahedron](../HexoticPLUGIN/hexoticpluginpy_doc/classsmeshBuilder_1_1Mesh.md#a8c05a76fdef5d692fb53e1cc0e364ae5)(algo=smeshBuilder.MG_Hexa) or [smeshBuilder.Mesh.Hexahedron](../HexoticPLUGIN/hexoticpluginpy_doc/classsmeshBuilder_1_1Mesh.md#a8c05a76fdef5d692fb53e1cc0e364ae5)(algo=smeshBuilder.Hexotic). This call creates an algorithm (if not yet exist), assigns it to the mesh and returns an instance of [HexoticPLUGINBuilder.Hexotic_Algorithm](../HexoticPLUGIN/hexoticpluginpy_doc/classHexoticPLUGINBuilder_1_1Hexotic__Algorithm.md) to the caller.

The class of algorithm has methods to set up meshing parameters.

Below you can see examples of usage of this class for hexahedral mesh generation.

1. [Construction of Mesh using MG-Hexa algorithm](hexoticplugin_python_interface_page.md#tui_hexotic_basic)
2. [Effect of the sub-domain mode](hexoticplugin_python_interface_page.md#tui_hexotic_sd_mode)
   1. [Sub-domain mode = 1](hexoticplugin_python_interface_page.md#tui_hexotic_sd_mode1)
   2. [Sub-domain mode = 2](hexoticplugin_python_interface_page.md#tui_hexotic_sd_mode2)
   3. [Sub-domain mode = 3](hexoticplugin_python_interface_page.md#tui_hexotic_sd_mode3)
   4. [Sub-domain mode = 4](hexoticplugin_python_interface_page.md#tui_hexotic_sd_mode4)

# Construction of Mesh using MG-Hexa algorithm

## Example of mesh generation with MG-Hexa algorithm:

```python
import salome
salome.salome_init()

from salome.geom import geomBuilder
geompy = geomBuilder.New()

from salome.smesh import smeshBuilder
smesh =  smeshBuilder.New()

# create a sphere
sphere = geompy.MakeSphereR(100.)
geompy.addToStudy(sphere, "sphere")

# create a mesh on the sphere
mghexaMesh = smesh.Mesh(sphere,"sphere: MG-CADSurf and MG-Hexa mesh")

# create a MG-CADSurf algorithm for faces
MG_CADSurf = mghexaMesh.Triangle(algo=smeshBuilder.MG_CADSurf)
MG_CADSurf.SetGeometricMesh( 1 )

# create a MG-Hexa algorithm for volumes
MG_Hexa = mghexaMesh.Hexahedron(algo=smeshBuilder.MG_Hexa)

# Change the level of subdivision
MG_Hexa.SetMinMaxHexes(4, 8)

# Local size

# Get the sphere skin
faces = geompy.SubShapeAll(sphere, geompy.ShapeType["FACE"])

# Set a local size on the face
MG_Hexa.SetMinMaxSize(10, 20)
MG_Hexa.SetSizeMap(faces[0], 10)

# compute the mesh
assert mghexaMesh.Compute(), "Meshing fails"

# End of script
```

[Download this script](https://docs.salome-platform.org/latest/examples/HexoticPLUGIN/hexoticdemo.py)

![hexotic_basic_subdivisions_4_8.png](https://docs.salome-platform.org/latest/gui/HexoticPLUGIN/hexotic_basic_subdivisions_4_8.png)

Left: MG-Hexa mesh without hypothesis, right: MG-Hexa mesh with an hypothesis defined by minl=4 and maxl=8

## Example of mesh generation with MG-Hexa algorithm and viscous layers parameters:

```python
import salome
salome.salome_init()

from salome.geom import geomBuilder
geompy = geomBuilder.New()

from salome.smesh import smeshBuilder
smesh =  smeshBuilder.New()

# Create geometry
Box_1 = geompy.MakeBoxDXDYDZ(50, 50, 50)
geompy.addToStudy( Box_1, 'Box_1' )

# Create mesh
Mesh_mghexa_vl = smesh.Mesh(Box_1, "Mesh_mghexa_vl")

Regular_1D = Mesh_mghexa_vl.Segment()
Local_Length_1 = Regular_1D.LocalLength(8.66025)

MEFISTO_2D = Mesh_mghexa_vl.Triangle(algo=smeshBuilder.MEFISTO)

MG_Hexa = Mesh_mghexa_vl.Hexahedron(algo=smeshBuilder.MG_Hexa)
MG_Hexa_Parameters = MG_Hexa.Parameters()
MG_Hexa.SetViscousLayers(5,5,3,[13,23])
MG_Hexa_Parameters.SetMinSize( 2 )
MG_Hexa_Parameters.SetMaxSize( 4 )
MG_Hexa_Parameters.SetHexesMinLevel( 2 )
MG_Hexa_Parameters.SetHexesMaxLevel( 4 )

# Compute
assert Mesh_mghexa_vl.Compute(), "Meshing fails"

# End of script
```

[Download this script](https://docs.salome-platform.org/latest/examples/HexoticPLUGIN/hexoticdemo_vl.py)

![hexotic_vl_example.png](https://docs.salome-platform.org/latest/gui/HexoticPLUGIN/hexotic_vl_example.png)

Left: MG-Hexa mesh without viscous layers parameters, right: MG-Hexa mesh with viscous layers parameters

## Local size

![hexotic_local_size_example.png](https://docs.salome-platform.org/latest/gui/HexoticPLUGIN/hexotic_local_size_example.png)

Example of use of a local size on the skin of a sphere

[Back to top](hexoticplugin_python_interface_page.md#tui_hexotic)

# Effect of the sub-domain mode

This example illustrates the sub-domain mode of MG-Hexa.

## Sub-domain mode = 1

## Example of sub-domain mode 1 with MG-Hexa algorithm:

```python
import salome
salome.salome_init()

from salome.geom import geomBuilder
geompy = geomBuilder.New()

import SMESH, SALOMEDS
from salome.smesh import smeshBuilder
smesh =  smeshBuilder.New()

# Create geometry: a box cut by a holed sphere
Box_1 = geompy.MakeBoxDXDYDZ(200, 200, 200)
Sphere_1 = geompy.MakeSphereR(75)
Sphere_2 = geompy.MakeSphereR(25)
geompy.TranslateDXDYDZ(Box_1, -100, -100, -100)
Cut_1 = geompy.MakeCut(Sphere_1, Sphere_2)
Cut_2 = geompy.MakeCut(Box_1, Cut_1)
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Sphere_1, 'Sphere_1' )
geompy.addToStudy( Sphere_2, 'Sphere_2' )
geompy.addToStudy( Cut_1, 'Cut_1' )
geompy.addToStudy( Cut_2, 'Cut_2' )

# Create filters
# aFilter1: elements inside small sphere
aFilter1 = smesh.GetFilter(SMESH.VOLUME,SMESH.FT_BelongToGeom,'=',Sphere_2)
# aFilter2: elements inside big sphere and not inside small sphere
aFilter2 = smesh.GetFilterFromCriteria([smesh.GetCriterion(SMESH.VOLUME,SMESH.FT_BelongToGeom,'=',Sphere_1, SMESH.FT_LogicalAND),
                                        smesh.GetCriterion(SMESH.VOLUME,SMESH.FT_BelongToGeom,'=',Sphere_2, SMESH.FT_LogicalNOT)])
# aFilter3: elements not inside big sphere
aFilter3 = smesh.GetFilter(SMESH.VOLUME,SMESH.FT_BelongToGeom,'=',Sphere_1, SMESH.FT_LogicalNOT)

# Create mesh of Cut_2 with sd mode 1
print("Create mesh of Cut_2 with sd mode 1")
Mesh_mghexa_sd1 = smesh.Mesh(Cut_2, "Mesh_mghexa_sd1")

# Create the 2D algo: MG-CADSurf with geometrical mesh
Mesh_mghexa_sd1.Triangle(algo=smeshBuilder.MG_CADSurf).SetGeometricMesh( 1 )

# Create the 3D algo: MG-Hexa with:
# - minl = 4
# - maxl = 8
# - sd = 1
Mesh_mghexa_sd1.Hexahedron(algo=smeshBuilder.MG_Hexa).SetMinMaxHexes(4, 8).SetHexoticSdMode( 1 )

# Create the groups on filters
g1 = Mesh_mghexa_sd1.GroupOnFilter(SMESH.VOLUME, 'small sphere', aFilter1 )
g1.SetColor( SALOMEDS.Color( 1, 0, 0 ))
g2 = Mesh_mghexa_sd1.GroupOnFilter(SMESH.VOLUME, 'big sphere - small sphere', aFilter2 )
g2.SetColor( SALOMEDS.Color( 0, 1, 0 ))
g3 = Mesh_mghexa_sd1.GroupOnFilter(SMESH.VOLUME, 'box - big sphere', aFilter3 )
g3.SetColor( SALOMEDS.Color( 0, 0, 1 ))

# Compute
assert Mesh_mghexa_sd1.Compute(), "Meshing fails"

# End of script
```

[Download this script](https://docs.salome-platform.org/latest/examples/HexoticPLUGIN/hexoticsubdom1.py)

![hexotic_sd_mode_1.png](https://docs.salome-platform.org/latest/gui/HexoticPLUGIN/hexotic_sd_mode_1.png)

MG-Hexa mesh of a box cut by a holed sphere ( sd = 1 )

[Back to top](hexoticplugin_python_interface_page.md#tui_hexotic)

## Sub-domain mode = 2

## Example of sub-domain mode 2 with MG-Hexa algorithm:

```python
import salome
salome.salome_init()

from salome.geom import geomBuilder
geompy = geomBuilder.New()

import SMESH, SALOMEDS
from salome.smesh import smeshBuilder
smesh =  smeshBuilder.New()

# Create geometry: a box cut by a holed sphere
Box_1 = geompy.MakeBoxDXDYDZ(200, 200, 200)
Sphere_1 = geompy.MakeSphereR(75)
Sphere_2 = geompy.MakeSphereR(25)
geompy.TranslateDXDYDZ(Box_1, -100, -100, -100)
Cut_1 = geompy.MakeCut(Sphere_1, Sphere_2)
Cut_2 = geompy.MakeCut(Box_1, Cut_1)
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Sphere_1, 'Sphere_1' )
geompy.addToStudy( Sphere_2, 'Sphere_2' )
geompy.addToStudy( Cut_1, 'Cut_1' )
geompy.addToStudy( Cut_2, 'Cut_2' )

# Create filters
# aFilter1: elements inside small sphere
aFilter1 = smesh.GetFilter(SMESH.VOLUME,SMESH.FT_BelongToGeom,'=',Sphere_2)
# aFilter2: elements inside big sphere and not inside small sphere
aFilter2 = smesh.GetFilterFromCriteria([smesh.GetCriterion(SMESH.VOLUME,SMESH.FT_BelongToGeom,'=',Sphere_1, SMESH.FT_LogicalAND),
                                        smesh.GetCriterion(SMESH.VOLUME,SMESH.FT_BelongToGeom,'=',Sphere_2, SMESH.FT_LogicalNOT)])
# aFilter3: elements not inside big sphere
aFilter3 = smesh.GetFilter(SMESH.VOLUME,SMESH.FT_BelongToGeom,'=',Sphere_1, SMESH.FT_LogicalNOT)

# Create mesh of Cut_2 with sd mode 2
print("Create mesh of Cut_2 with sd mode 2")
Mesh_mghexa_sd2 = smesh.Mesh(Cut_2, "Mesh_mghexa_sd2")

# Create the 2D algo: MG-CADSurf with geometrical mesh
Mesh_mghexa_sd2.Triangle(algo=smeshBuilder.MG_CADSurf).SetGeometricMesh( 1 )

# Create the 3D algo: MG-Hexa with:
# - minl = 4
# - maxl = 8
# - sd = 2
Mesh_mghexa_sd2.Hexahedron(smeshBuilder.MG_Hexa).SetMinMaxHexes(4, 8).SetHexoticSdMode( 2 )

# Create the groups on filters
g1 = Mesh_mghexa_sd2.GroupOnFilter(SMESH.VOLUME, 'small sphere', aFilter1 )
g1.SetColor( SALOMEDS.Color( 1, 0, 0 ))
g2 = Mesh_mghexa_sd2.GroupOnFilter(SMESH.VOLUME, 'big sphere - small sphere', aFilter2 )
g2.SetColor( SALOMEDS.Color( 0, 1, 0 ))
g3 = Mesh_mghexa_sd2.GroupOnFilter(SMESH.VOLUME, 'box - big sphere', aFilter3 )
g3.SetColor( SALOMEDS.Color( 0, 0, 1 ))

# Compute
assert Mesh_mghexa_sd2.Compute(), "Meshing fails"

# End of script
```

[Download this script](https://docs.salome-platform.org/latest/examples/HexoticPLUGIN/hexoticsubdom2.py)

![hexotic_sd_mode_2.png](https://docs.salome-platform.org/latest/gui/HexoticPLUGIN/hexotic_sd_mode_2.png)

MG-Hexa mesh of a box cut by a holed sphere ( sd = 2 )

[Back to top](hexoticplugin_python_interface_page.md#tui_hexotic)

## Sub-domain mode = 3

## Example of sub-domain mode 3 with MG-Hexa algorithm:

```python
import salome
salome.salome_init()

from salome.geom import geomBuilder
geompy = geomBuilder.New()

import SMESH, SALOMEDS
from salome.smesh import smeshBuilder
smesh =  smeshBuilder.New()

# Create geometry: a box cut by a holed sphere
Box_1 = geompy.MakeBoxDXDYDZ(200, 200, 200)
Sphere_1 = geompy.MakeSphereR(75)
Sphere_2 = geompy.MakeSphereR(25)
geompy.TranslateDXDYDZ(Box_1, -100, -100, -100)
Cut_1 = geompy.MakeCut(Sphere_1, Sphere_2)
Cut_2 = geompy.MakeCut(Box_1, Cut_1)
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Sphere_1, 'Sphere_1' )
geompy.addToStudy( Sphere_2, 'Sphere_2' )
geompy.addToStudy( Cut_1, 'Cut_1' )
geompy.addToStudy( Cut_2, 'Cut_2' )

# Create filters
# aFilter1: elements inside small sphere
aFilter1 = smesh.GetFilter(SMESH.VOLUME,SMESH.FT_BelongToGeom,'=',Sphere_2)
# aFilter2: elements inside big sphere and not inside small sphere
aFilter2 = smesh.GetFilterFromCriteria([smesh.GetCriterion(SMESH.VOLUME,SMESH.FT_BelongToGeom,'=',Sphere_1, SMESH.FT_LogicalAND),
                                        smesh.GetCriterion(SMESH.VOLUME,SMESH.FT_BelongToGeom,'=',Sphere_2, SMESH.FT_LogicalNOT)])
# aFilter3: elements not inside big sphere
aFilter3 = smesh.GetFilter(SMESH.VOLUME,SMESH.FT_BelongToGeom,'=',Sphere_1, SMESH.FT_LogicalNOT)

# Create mesh of Cut_2 with sd mode 3
print("Create mesh of Cut_2 with sd mode 3")
Mesh_mghexa_sd3 = smesh.Mesh(Cut_2, "Mesh_mghexa_sd3")

# Create the 2D algo: MG-CADSurf with geometrical mesh
Mesh_mghexa_sd3.Triangle(algo=smeshBuilder.MG_CADSurf).SetGeometricMesh( 1 )

# Create the 3D algo: MG-Hexa with:
# - minl = 4
# - maxl = 8
# - sd = 3
Mesh_mghexa_sd3.Hexahedron(algo=smeshBuilder.MG_Hexa).SetMinMaxHexes(4, 8).SetHexoticSdMode( 3 )

# Create the groups on filters
g1 = Mesh_mghexa_sd3.GroupOnFilter(SMESH.VOLUME, 'small sphere', aFilter1 )
g1.SetColor( SALOMEDS.Color( 1, 0, 0 ))
g2 = Mesh_mghexa_sd3.GroupOnFilter(SMESH.VOLUME, 'big sphere - small sphere', aFilter2 )
g2.SetColor( SALOMEDS.Color( 0, 1, 0 ))
g3 = Mesh_mghexa_sd3.GroupOnFilter(SMESH.VOLUME, 'box - big sphere', aFilter3 )
g3.SetColor( SALOMEDS.Color( 0, 0, 1 ))

# Compute
assert Mesh_mghexa_sd3.Compute(), "Meshing fails"

# End of script
```

[Download this script](https://docs.salome-platform.org/latest/examples/HexoticPLUGIN/hexoticsubdom3.py)

![hexotic_sd_mode_3.png](https://docs.salome-platform.org/latest/gui/HexoticPLUGIN/hexotic_sd_mode_3.png)

MG-Hexa mesh of a box cut by a holed sphere ( sd = 3 )

[Back to top](hexoticplugin_python_interface_page.md#tui_hexotic)

## Sub-domain mode = 4

## Example of sub-domain mode 4 with MG-Hexa algorithm:

```python
import salome
salome.salome_init()

from salome.geom import geomBuilder
geompy = geomBuilder.New()

from salome.smesh import smeshBuilder
smesh =  smeshBuilder.New()

# Create geometry: a box cut by a plane
Box_1 = geompy.MakeBoxDXDYDZ(200, 200, 200)
Translation_1 = geompy.MakeTranslation(Box_1, 0, 200, 0)
Partition_1 = geompy.MakePartition([Box_1, Translation_1])
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Translation_1, 'Translation_1' )
geompy.addToStudy( Partition_1, 'Partition_1' )

# Create mesh of Partition_1 with sd mode 4 (default sd mode in SALOME)
Mesh_mghexa_sd4 = smesh.Mesh(Partition_1, "Mesh_mghexa_sd4")
Mesh_mghexa_sd4.Triangle(smeshBuilder.MG_CADSurf)
Mesh_mghexa_sd4.Hexahedron(smeshBuilder.MG_Hexa).SetMinMaxHexes(4, 8).SetHexoticSdMode( 4 )

# Compute
assert Mesh_mghexa_sd4.Compute(), "Meshing fails"

# End of script
```

[Download this script](https://docs.salome-platform.org/latest/examples/HexoticPLUGIN/hexoticsubdom4.py)

![hexotic_sd_mode_4.png](https://docs.salome-platform.org/latest/gui/HexoticPLUGIN/hexotic_sd_mode_4.png)

MG-Hexa mesh of a box cut by a plane ( On the left, sd = 3: the internal surface is ignored ; on the right sd = 4: all sub-domains are meshed )

[Back to top](hexoticplugin_python_interface_page.md#tui_hexotic)
