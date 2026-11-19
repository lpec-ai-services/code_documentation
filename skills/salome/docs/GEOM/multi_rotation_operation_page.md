<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/multi_rotation_operation_page.html -->

# Multi Rotation

To produce a **Multi Rotation** in the **Main Menu** select **Operations - > Transformation - > Multi Rotation**

This operation creates a compound of several rotated shapes basing on the initial shape.

In case of **Simple Multi Rotation** the object is multiplied by rotation.

![neo-mrot1.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-mrot1.png)

The following parameters and options can be defined in this dialog:

- **Result Name**;
- **Main Object**  to be rotated;
- **Vector** defines the axis of rotation (DZ by default);
- **Angular step** is the angle by which the object is rotated. By default (if the checkbox is not checked), it is 2 * *PI* / *NbTimes*;
- **Nb. Times** is the number of rotated shape copies in the resulting compound. If *NbTimes* = 1, the result contains only the initial shape;
- [Advanced options](restore_presentation_parameters_page.md).

The **Result** will be a **GEOM_Object** (compound).

**TUI Commands:**   
*geompy.MultiRotate1DNbTimes(Shape, Axis, NbTimes)*   
*geompy.MultiRotate1DByStep(Shape, Axis, AngleStep, NbTimes)*

****NB!**** There is another way to execute a Multi-rotation operation, which is currently accessible only via TUI commands: *geompy.MakeMultiRotation1DNbTimes(Shape, Dir, Point, NbTimes)*, *geompy.MakeMultiRotation1DByStep(Shape, Dir, Point, AngleStep, NbTimes)*, which works in the same way, but the Axis is defined by direction and point.

![multi_rotation1d1.png](https://docs.salome-platform.org/latest/gui/GEOM/multi_rotation1d1.png)

The initial object

![multi_rotation1d2.png](https://docs.salome-platform.org/latest/gui/GEOM/multi_rotation1d2.png)

The result of a simple multi-rotation

In case of **Double Multi Rotation** the object is multiplied by rotation and additionally translated several times in each direction.

![neo-mrot2.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-mrot2.png)

The following parameters and options can be defined in this dialog:

- **Result Name**;
- **Main Object**  to be rotated;
- **Vector** defines the axis of rotation (DZ by default);
- **Angular step** is the angle by which the object is rotated. By default (if the checkbox is not checked), it is 2 * *PI* / *NbTimes*;
- **Nb. Times** (*NbTimes1*) is the number of rotated shape copies in the resulting compound;
- **Reverse** checkbox allows changing the direction of translation;
- **Radial step**  is the distance between the shape copies in the same direction. Translation direction passes through the center of gravity of the initial shape and its projection on the rotation axis;
- **Nb. Times** (*NbTimes2*) is the number of shape copies in the same direction. If *NbTimes2* = 1, the result is the same as for **Simple Multi Rotation**. If both *NbTimes1* and *NbTimes2* are equal to 1, the result will contain only the initial non-transformed shape;
- [Advanced options](restore_presentation_parameters_page.md).

**TUI Commands:**   
*geompy.MultiRotate2DNbTimes(Shape, Axis, NbTimes1, RadialStep, NbTimes2)*   
*geompy.MultiRotate2DByStep(Shape, Axis, AngleStep, NbTimes1, RadialStep, NbTimes2)*

**NB!** There is another way to execute a Double Multi-rotation operation, which is currently accessible only via TUI commands: *geompy.MakeMultiRotation2DNbTimes(Shape, Dir, Point, NbTimes1, RadialStep, NbTimes2)*, *geompy.MakeMultiRotation2DByStep(Shape, Dir, Point, AngleStep, NbTimes1, RadialStep, NbTimes2)*, which works in the same way, but the Axis is defined by direction and point.

![multi_rotation2d1.png](https://docs.salome-platform.org/latest/gui/GEOM/multi_rotation2d1.png)

The initial object

![multi_rotation2d2.png](https://docs.salome-platform.org/latest/gui/GEOM/multi_rotation2d2.png)

The result of a double multi-rotation

Our **TUI Scripts** provide you with useful examples of the use of [Transformation Operations](tui_transformation_operations_page.md#tui_multi_rotation).
