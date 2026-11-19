<!-- source: https://docs.salome-platform.org/latest/gui/HYBRIDPLUGIN/hybridplugin_python_interface_page.html -->

# Python Interface

Python package [HYBRIDPluginBuilder](../HYBRIDPLUGIN/hybridpluginpy_doc/namespaceHYBRIDPluginBuilder.md) defines several classes, destined for creation of the 3D meshes.

HYBRID meshing plugin dynamically adds several methods to the [smeshBuilder.Mesh](../HYBRIDPLUGIN/hybridpluginpy_doc/classsmeshBuilder_1_1Mesh.md) class to create meshing algorithms.

Below you can see an example of usage of the [HYBRIDPluginBuilder](../HYBRIDPLUGIN/hybridpluginpy_doc/namespaceHYBRIDPluginBuilder.md) Python API for mesh generation:

1. [Construction of Mesh using MG-Hybrid algorithm](hybridplugin_python_interface_page.md#tui_hybrid_basic)

# Construction of Mesh using MG-Hybrid algorithm

## Example of mesh generation with HYBRID algorithm:

```python
import salome
salome.salome_init()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

import SMESH, SALOMEDS
from salome.smesh import smeshBuilder
smesh =  smeshBuilder.New()

# create a box
box = geompy.MakeBoxDXDYDZ(200., 200., 200.)
geompy.addToStudy(box, "box")

# create a mesh on the box
hybridMesh = smesh.Mesh(box,"box: MG-Hybrid and BLSurf mesh")

# create a BLSurf algorithm for faces
BLSURF = hybridMesh.Triangle(algo=smeshBuilder.BLSURF)
HYBRID = hybridMesh.Tetrahedron(algo=smeshBuilder.HYBRID)

# compute the mesh
hybridMesh.Compute()

# End of script
```

[Download this script](https://docs.salome-platform.org/latest/examples/HYBRIDPLUGIN/hybriddemo.py)

[Back to top](hybridplugin_python_interface_page.md#tui_hybrid)
