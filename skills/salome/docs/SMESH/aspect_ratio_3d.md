<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/aspect_ratio_3d.html -->

# Aspect ratio 3D

The **Aspect Ratio 3D** mesh quality criterion calculates the same parameter as the [Aspect Ratio](aspect_ratio.md#aspect-ratio-page) criterion, but it is applied to 3D mesh elements: tetrahedrons, pentahedrons, hexahedrons, etc.

- The **Aspect Ratio** of a **tetrahedron** 3D element defined by vertices {a,b,c,d } is calculated by the formula:

  > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/formula1.png)
- Other element types like polyhedron, pentahedron and hexahedron use the following formula:

  > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/formula2.png)

*To apply the Aspect Ratio 3D quality criterion to your mesh:*

1. Display your mesh in the viewer.
2. Choose **Controls > Volume Controls > Aspect Ratio 3D** or click *“Aspect Ratio 3D”* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image144.png) of the toolbar.

   Your mesh will be displayed in the viewer with its elements colored according to the applied mesh quality control criterion:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image86.jpg)

**See Also** a sample TUI Script of a [Aspect Ratio 3D](tui_quality_controls.md#tui-aspect-ratio-3d) filter.
