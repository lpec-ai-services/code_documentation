<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tui_execution_distribution_page.html -->

# Distribute Geometry script execution.

Several kinds of studies require distributed geometry and mesh calculations. For instance, in some parametric studies, we need to compute a lot of geometries and associated meshes in parallel on a cluster.

These studies are defined with a YACS Schema in which geometry and meshing are done in distributed Python nodes running on distributed SALOME Containers. We need to instantiate [GEOM](../GEOM/geompy_doc/namespaceGEOM.md) and SMESH Engines on these containers.

The standard way of geometry initialization in a Python script is:

```python
import salome
salome.salome_init()

from salome.geom import geomBuilder
geompy = geomBuilder.New()
```

With this initialization, the geometry engine runs in the default container, embedded in the SALOME Graphical User Interface process (see YACS documentation for concepts).

To select another engine than the default "FactoryServer", the CORBA engine can be given as an optional parameter of the method New. For instance:

```python
from salome.geom import geomBuilder
lcc = salome.lcc
engineGeom = lcc.FindOrLoadComponent("myServer", "GEOM")
geompy = geomBuilder.New(engineGeom)
```

Or, within a Distributed Python Node of a YACS Schema, where the container is already provided in the Python context of the node, with *my_container*:

```python
from salome.geom import geomBuilder
my_container.load_component_Library("GEOM")
engineGeom = my_container.create_component_instance("GEOM")
geompy = geomBuilder.New(engineGeom)
```
