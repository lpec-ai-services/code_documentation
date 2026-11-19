<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_page.html -->

# Python Interface geomBuilder.py

Please, see [structured documentation for geomBuilder.py](geompy_doc/group__geomBuilder.md), where all package functionality is separated in groups by purpose.

Also you can find any function in the [linear documentation for geomBuilder.py](geompy_doc/namespacegeomBuilder.md)

With SALOME 7.2, the Python interface for Geometry has been slightly modified to offer new functionality,   
You may have to modify your scripts generated with SALOME 6 or older versions.   
Please see [Modifying Geometry Python scripts from SALOME 6 and before](geompy_migration_page.md)

## [GEOM](../GEOM/geompy_doc/namespaceGEOM.md) Python script example

```python
# --- salome initialization
import salome
salome.salome_init_without_session()

# --- geom Python interface
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

# --- Create a box and publish it into the salome study
Box_1 = geompy.MakeBoxDXDYDZ(200, 200, 200)
geompy.addToStudy( Box_1, 'Box_1' )

# --- update the study object browser
if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
```

[Download this script](https://docs.salome-platform.org/latest/examples/GEOM/GEOM_box.py)

By the links below you can find sample scripts for all operations provided by Geometry module.

- [Import/Export](tui_import_export_page.md)
- [Creating Geometric Objects](tui_creating_geom_objs_page.md)
  - [Basic Geometrical Objects](tui_basic_geom_objs_page.md)
  - [Primitives](tui_primitives_page.md)
  - [Complex Objects](tui_complex_objs_page.md)
  - [Working with Groups](tui_working_with_groups_page.md)
  - [Building by Blocks](tui_building_by_blocks_page.md)
  - [2D Sketcher](tui_sketcher_page.md)
  - [3D Sketcher](tui_3dsketcher_page.md)
  - [Advanced Geometrical Objects](tui_advanced_geom_objs_page.md)
- [Viewing Geometrical Objects](tui_viewing_geom_objs_page.md)
- [Transformation](tui_transformation_page.md)
  - [Basic Operations](tui_basic_operations_page.md)
  - [Boolean Operations](tui_boolean_operations_page.md)
  - [Transformation Operations](tui_transformation_operations_page.md)
  - [Blocks Operations](tui_blocks_operations_page.md)
  - [Repairing Operations](tui_repairing_operations_page.md)
- [Geometrical Fields](tui_geom_field_page.md)
- [Measurement Tools](tui_measurement_tools_page.md)
- [Using SALOME NoteBook](tui_notebook_geom_page.md)
- [Arranging objects in study](tui_arranging_study_objects_page.md)
- [Examples, generated from GEOM_SWIG test scripts](tui_swig_examples_page.md)
  - [GEOM_TestOthers.py](tui_test_others_page.md)
  - [GEOM_Spanner.py](tui_test_spanner_page.md)
  - [GEOM_TestAll.py](tui_test_all_page.md)
  - [GEOM_TestMeasures.py](tui_test_measures_page.md)
