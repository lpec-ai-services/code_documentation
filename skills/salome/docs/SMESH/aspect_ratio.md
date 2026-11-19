<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/aspect_ratio.html -->

# Aspect Ratio

The **Aspect Ratio** quality criterion for mesh elements reveals the degree of conformity of a mesh element to the regular element of its type (with all edges having the same length).

- The **Aspect Ratio** of a **triangle** 2D element consisting of 3 nodes is calculated by the formula:

  > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/formula4.png)
- The **Aspect Ratio** of a **quadrangle** 2D element consisting of 4 nodes is calculated using The Verdict Geometric Quality Library available within VTK. The calculation formula is:

  > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/formula5.png)

*To apply the Aspect Ratio quality criterion to your mesh:*

1. Display your mesh in the viewer.
2. Choose **Controls > Face Controls > Aspect Ratio** or click *Aspect Ratio* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image37.png) in the toolbar.

   Your mesh will be displayed in the viewer with its elements colored according to the applied mesh quality control criterion:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image94.jpg)

**See Also** a sample TUI Script of an [Aspect Ratio](tui_quality_controls.md#tui-aspect-ratio) filter.
