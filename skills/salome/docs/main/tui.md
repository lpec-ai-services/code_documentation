<!-- source: https://docs.salome-platform.org/latest/main/tui.html -->

![figure](https://docs.salome-platform.org/latest/main/_images/head.png)

# Developer’s Documentation

This chapter contains different reference manuals and other documents which can be
helpful for the developers who wants to customize the **SALOME platform** or develop
new features, modules, plugins, etc.

## Modules documentation

- [KERNEL module](../tui/KERNEL/index.md)

*This is the developer reference manual for the SALOME KERNEL module. It provides a general
description of the main services implemented within the KERNEL module.*

- [GUI module](../tui/GUI/index.md)

*This is the developer reference manual for the SALOME GUI module. It provides a description
of the basic functionalities available in the GUI module.*

- [Shaper module](../tui/SHAPER/index.md)

*This section contains developer reference manual for the SALOME Shaper module. Shaper is a
CAD modeler which came as a replacement for the former Geometry module.*

- [Geometry module](../tui/GEOM/index.md)

This section contains developer reference manual for the SALOME Geometry module, the legacy
CAD modeler of the SALOME platform.*

- [Mesh module](../tui/SMESH/index.md)

*This is the developer reference manual for the SALOME Mesh module. This module can be used
for generating of the meshes from the CAD model prepared in Geometry or Shaper.*

- [YACS module](../tui/YACS/index.md)

*This section contains developer reference manual for the SALOME YACS module.*

- [Fields module](../dev/FIELDS/index.md)

*This section contains developer reference manual for the SALOME Fields module formely known
as Med module.*

- [ParaVis module](../dev/PARAVIS/index.md)

*This section contains developer reference manual for the SALOME ParaVis module.*

## Guides

| Legend | |
| --- | --- |
| [warn](https://docs.salome-platform.org/latest/main/_images/warn.png) | Document is not up to date |
| [fr](https://docs.salome-platform.org/latest/main/_images/fr.png) | Document in French |
| [pdf](https://docs.salome-platform.org/latest/main/_images/pdf.png) | Document in PDF format |

### Architecture

- [![pdf](https://docs.salome-platform.org/latest/main/_images/pdf.png)](https://docs.salome-platform.org/latest/main/_images/pdf.png) [SALOME GUI Architecture](https://docs.salome-platform.org/latest/extra/SALOME_GUI_Architecture.pdf) (PDF, 1 MB) [![warn](https://docs.salome-platform.org/latest/main/_images/warn.png)](https://docs.salome-platform.org/latest/main/_images/warn.png)

### Module Development

- The **SALOME Tutorial** provides an introduction to the development of new modules
  and integrating them to the SALOME platform, as well as new applications based on SALOME.
  The tutorial can be downloaded from [SALOME site](https://www.salome-platform.org/downloads).
- [![pdf](https://docs.salome-platform.org/latest/main/_images/pdf.png)](https://docs.salome-platform.org/latest/main/_images/pdf.png) [Implement Dump Python](https://docs.salome-platform.org/latest/extra/DumpPython_Extension.pdf) (PDF, 67 KB)

### Mesh

- [![pdf](https://docs.salome-platform.org/latest/main/_images/pdf.png)](https://docs.salome-platform.org/latest/main/_images/pdf.png) [Use of SMDS API](https://docs.salome-platform.org/latest/extra/SALOME_4.1.2_SMDS_reference_guide.pdf) (PDF, 416 KB) [![warn](https://docs.salome-platform.org/latest/main/_images/warn.png)](https://docs.salome-platform.org/latest/main/_images/warn.png)
- [![pdf](https://docs.salome-platform.org/latest/main/_images/pdf.png)](https://docs.salome-platform.org/latest/main/_images/pdf.png) [Integration of new meshing algorithm as plug-in to SALOME Mesh module](https://docs.salome-platform.org/latest/extra/SALOME_Mesh_Plugins.pdf) (PDF, 91 KB)

### Code Coupling

- [![pdf](https://docs.salome-platform.org/latest/main/_images/pdf.png)](https://docs.salome-platform.org/latest/main/_images/pdf.png) [Normalisation des maillages et des champs pour le couplage](https://docs.salome-platform.org/latest/extra/Normalisation_pour_le_couplage_de_codes.pdf) (PDF, 1 MB) [![fr](https://docs.salome-platform.org/latest/main/_images/fr.png)](https://docs.salome-platform.org/latest/main/_images/fr.png)
- [![pdf](https://docs.salome-platform.org/latest/main/_images/pdf.png)](https://docs.salome-platform.org/latest/main/_images/pdf.png) [Documentation of the Interface for Code Coupling / ICoCo](https://docs.salome-platform.org/latest/extra/Interface_for_Code_Coupling.pdf) (PDF, 1.6 MB) [![fr](https://docs.salome-platform.org/latest/main/_images/fr.png)](https://docs.salome-platform.org/latest/main/_images/fr.png)
- [![pdf](https://docs.salome-platform.org/latest/main/_images/pdf.png)](https://docs.salome-platform.org/latest/main/_images/pdf.png) [Le couplage de codes paralleles dans la plateforme SALOME](https://docs.salome-platform.org/latest/extra/Couplage_de_codes_paralleles.pdf) (PDF, 589 KB) [![fr](https://docs.salome-platform.org/latest/main/_images/fr.png)](https://docs.salome-platform.org/latest/main/_images/fr.png)
- [![pdf](https://docs.salome-platform.org/latest/main/_images/pdf.png)](https://docs.salome-platform.org/latest/main/_images/pdf.png) [Démonstrateur couplage fluide structure EDF](https://docs.salome-platform.org/latest/extra/Demonstrateur_couplage_fluide_structure_EDF.pdf) (PDF, 1.2 MB) [![fr](https://docs.salome-platform.org/latest/main/_images/fr.png)](https://docs.salome-platform.org/latest/main/_images/fr.png)

### Installation procedure

- [Build procedure](../dev/cmake/html/index.md) (CMake)

### Development

- [Contributing to the SALOME project with Git](../dev/git/html/Git_Simple_Write_Procedure.md)
