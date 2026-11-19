<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_migration_page.html -->

# Modifying Geometry Python scripts from SALOME 6 and before

In SALOME 7.2, the Python interface for Geometry has been slightly modified to offer new functionality:

- [Distribute Geometry script execution.](tui_execution_distribution_page.md)
- [Auto completion and interactive documentation in edition.](tui_auto_completion_documentation_page.md)

Scripts generated for SALOME 6 and older versions must be adapted to work in SALOME 7.2 with full functionality.   
The compatibility mode allows old scripts to work in almost all cases, but with a warning.

**Salome initialisation must always be done as shown below**   
(*salome_init()* can be invoked safely several times):

```python
import salome
salome.salome_init()
```

**Geometry initialisation is modified.**   
the old mode:

```python
import geompy
geompy.init_geom()
```

the new mode:

```python
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
```

**Of course, *from geompy import ** is no more possible.**   
You have to explicitly write *geompy.some_method()*.

**Some variables have been transferred from the namespace *geompy.GEOM* to the namespace *[GEOM](../GEOM/geompy_doc/namespaceGEOM.md)*.**   
All occurrences of *geompy.GEOM.* can be replaced by *[GEOM](../GEOM/geompy_doc/namespaceGEOM.md).*.   
For instance:

```python
param_polyline = geompy.MakeCurveParametric("t", "sin(t)", "cos(t)", 0., 100., 100, geompy.GEOM.Polyline, theNewMethod=True)
```

is replaced by:

```python
param_polyline = geompy.MakeCurveParametric("t", "sin(t)", "cos(t)", 0., 100., 100, GEOM.Polyline, theNewMethod=True)
```
