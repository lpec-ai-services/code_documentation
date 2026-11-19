<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/skew.html -->

# Skew

**Skew** mesh quality criterion reflects the angle between the lines
that join opposite sides of a quadrangle element or the greatest angle
between a median and a midline in a triangle element. This mesh quality
criterion can be applied to elements composed of 4 and 3 nodes
(quadrangles and triangles).

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image27.jpg)

*To apply the Skew quality criterion to your mesh:*

1. Display your mesh in the viewer.
2. Choose **Controls > Face Controls > Skew** or click *“Skew”* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image40.png) of the toolbar.

   Your mesh will be displayed in the viewer with its elements colored according to the applied mesh quality control criterion:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image93.jpg)

**See Also** a sample TUI Script of a [Skew](tui_quality_controls.md#tui-skew) filter.
