<!-- source: https://docs.salome-platform.org/latest/gui/HOMARD/en/gui_usage.html -->

# User’s guide of the graphical interface

## Activation of the module HOMARD

Two ways can be used to launch the module HOMARD:

1. by activating the tab HOMARD into the list of the modules
2. by clicking the button HOMARD into tool bar

The user can choose either to start a new study or to open an old stored one, as it can be done for every module of SALOME.

![figure](https://docs.salome-platform.org/latest/gui/HOMARD/en/_images/homard_1.png)

## Definition of an adaptation

Once the activation of the module HOMARD is done, a case is created. The initial mesh of the series of adapted meshes is selected (see [The creation of a case](gui_create_case.md)). From this case, the successive iterations are defined (see [The iteration](gui_create_iteration.md)) with hypotheses (see [The hypothesis](gui_create_hypothese.md)). The adaptations are launched as described in [The computation](gui_homard.md).

## User’s guide of the graphical interface

- [The creation of a case](gui_create_case.md)
  - [Name of the case](gui_create_case.md#name-of-the-case)
  - [The directory](gui_create_case.md#the-directory)
  - [The initial mesh](gui_create_case.md#the-initial-mesh)
  - [Type of conformity](gui_create_case.md#type-of-conformity)
  - [The boundaries](gui_create_case.md#the-boundaries)
  - [Advanced options](gui_create_case.md#advanced-options)
  - [The pursuit of a case](gui_create_case.md#the-pursuit-of-a-case)
  - [Object browser](gui_create_case.md#object-browser)
  - [Corresponding python functions](gui_create_case.md#corresponding-python-functions)
- [The iteration](gui_create_iteration.md)
  - [Name of the iteration](gui_create_iteration.md#name-of-the-iteration)
  - [The preceding iteration](gui_create_iteration.md#the-preceding-iteration)
  - [The name of the resulting mesh](gui_create_iteration.md#the-name-of-the-resulting-mesh)
  - [The field](gui_create_iteration.md#the-field)
  - [The hypothesis](gui_create_iteration.md#the-hypothesis)
  - [Object browser](gui_create_iteration.md#object-browser)
  - [Corresponding python functions](gui_create_iteration.md#corresponding-python-functions)
- [The hypothesis](gui_create_hypothese.md)
  - [Name of the hypothesis](gui_create_hypothese.md#name-of-the-hypothesis)
  - [Uniform adaptation](gui_create_hypothese.md#uniform-adaptation)
  - [Adaptation by a field](gui_create_hypothese.md#adaptation-by-a-field)
  - [Adaptation by a zone](gui_create_hypothese.md#adaptation-by-a-zone)
  - [Filtering by the groups](gui_create_hypothese.md#filtering-by-the-groups)
  - [Interpolation of fields](gui_create_hypothese.md#interpolation-of-fields)
  - [Advanced options](gui_create_hypothese.md#advanced-options)
  - [Object browser](gui_create_hypothese.md#object-browser)
  - [Corresponding python functions](gui_create_hypothese.md#corresponding-python-functions)
- [The zone](gui_create_zone.md)
  - [Name of the zone](gui_create_zone.md#name-of-the-zone)
  - [Box](gui_create_zone.md#box)
  - [Cylinder](gui_create_zone.md#cylinder)
  - [Pipe](gui_create_zone.md#pipe)
  - [Sphere](gui_create_zone.md#sphere)
  - [Rectangle](gui_create_zone.md#rectangle)
  - [Disk](gui_create_zone.md#disk)
  - [Disk with a hole](gui_create_zone.md#disk-with-a-hole)
  - [Corresponding python functions](gui_create_zone.md#corresponding-python-functions)
- [The boundary](gui_create_boundary.md)
  - [CAO boundary](gui_create_boundary.md#cao-boundary)
  - [Discrete boundary](gui_create_boundary.md#discrete-boundary)
  - [Analytical boundary](gui_create_boundary.md#analytical-boundary)
  - [Object browser](gui_create_boundary.md#object-browser)
  - [Corresponding python functions](gui_create_boundary.md#corresponding-python-functions)
- [The computation](gui_homard.md)
  - [To compute an iteration](gui_homard.md#to-compute-an-iteration)
  - [Object browser](gui_homard.md#object-browser)
  - [To consult the result of an adaptation](gui_homard.md#to-consult-the-result-of-an-adaptation)
  - [Corresponding python functions](gui_homard.md#corresponding-python-functions)
- [Mesh analysis](gui_mesh_info.md)
  - [Importation of the mesh](gui_mesh_info.md#importation-of-the-mesh)
  - [Name of the case](gui_mesh_info.md#name-of-the-case)
  - [The directory](gui_mesh_info.md#the-directory)
  - [Mesh to be analysed](gui_mesh_info.md#mesh-to-be-analysed)
  - [Options for the analysis](gui_mesh_info.md#options-for-the-analysis)
  - [Object browser](gui_mesh_info.md#object-browser)
  - [Computed iteration](gui_mesh_info.md#computed-iteration)
  - [Corresponding python functions](gui_mesh_info.md#corresponding-python-functions)

## Creation of a schema YACS

An automatic creation of a schema YACS is available in the module HOMARD.

- [The schema YACS](gui_create_yacs.md)
  - [Procedure](gui_create_yacs.md#procedure)
  - [Name of the schema](gui_create_yacs.md#name-of-the-schema)
  - [The script](gui_create_yacs.md#the-script)
  - [The directory](gui_create_yacs.md#the-directory)
  - [The initial mesh](gui_create_yacs.md#the-initial-mesh)
  - [The type of the schema](gui_create_yacs.md#the-type-of-the-schema)
  - [Saving the schema](gui_create_yacs.md#saving-the-schema)
  - [Object browser](gui_create_yacs.md#object-browser)
  - [Corresponding python functions](gui_create_yacs.md#corresponding-python-functions)
- [How to use the schema](gui_create_yacs.md#how-to-use-the-schema)
- [Examples](gui_create_yacs.md#examples)
- [A schema YACS for *Code_Aster*](gui_create_yacs_aster.md)
  - [Preparations](gui_create_yacs_aster.md#preparations)
  - [How to do ?](gui_create_yacs_aster.md#how-to-do)

## Preferences

Some default options for the module HOMARD are defined into the preferences.

- [The preferences](preferences.md)
  - [The language](preferences.md#the-language)
  - [Publication of the meshes](preferences.md#publication-of-the-meshes)
