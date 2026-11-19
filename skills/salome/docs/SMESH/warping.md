<!-- source: https://docs.salome-platform.org/latest/gui/SMESH/warping.html -->

# Warping

![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image24.gif)

**Warping** indicates that a face is not planar and is applied only to
2D elements with 4 nodes. This quality control criterion is based on a
projection plane created by:

1. bisecting the four element edges,
2. creating a point on the plane at the vector average of the corners, where the x-axis extends from the point to the bisector on edge 2.

The plane normal is in the direction of the cross product of the
x-axis and the vector from the origin to the bisector of edge 3. Every
corner of the quad will then be a distance *h* from the plane. The
length of each half edge is measured and the shortest length is
assigned *l*. The warp angle is the arcsine of the ratio of the
projection height *h* to the half edge length *l*.

*To apply the Warping quality criterion to your mesh:*

1. Display your mesh in the viewer.
2. Choose **Controls > Face Controls > Warping Angle** or click *“Warping angle”* button ![img](https://docs.salome-platform.org/latest/gui/SMESH/_images/image39.png) of the toolbar.

   Your mesh will be displayed in the viewer with its elements colored according to the applied mesh quality control criterion:

   > ![figure](https://docs.salome-platform.org/latest/gui/SMESH/_images/image97.jpg)

**See Also** a sample TUI Script of a [Warping](tui_quality_controls.md#tui-warping) filter.
