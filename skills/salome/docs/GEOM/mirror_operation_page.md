<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/mirror_operation_page.html -->

# Mirror Image

To produce a **Mirror Image** in the **Main Menu** select **Operations - > Transformation - > Mirror Image**

This operation creates a symmetrical copy of an **Object**, which can be mirrored in three different ways.   
**Create a copy** checkbox allows to keep the initial object, otherwise it will be removed.   
The **Result** will be a **GEOM_Object**.

Firstly an **Object** can be mirrored through a **Point** of symmetry   
**TUI Command:** *geompy.MakeMirrorByPoint(Object, Point)*   
**Arguments:** Name + one or several objects + 1 vertex.   
[Advanced options](restore_presentation_parameters_page.md).

![transformation7.png](https://docs.salome-platform.org/latest/gui/GEOM/transformation7.png)

![mirror_pointsn1.png](https://docs.salome-platform.org/latest/gui/GEOM/mirror_pointsn1.png)

The initial shape and the mirror point

![mirror_pointsn2.png](https://docs.salome-platform.org/latest/gui/GEOM/mirror_pointsn2.png)

The resulting shape (grey)

Secondly an **Object** can be mirrored through an **Axis** of symmetry   
**TUI Command:** *geompy.MakeMirrorByAxis(Object, Axis)*   
**Arguments:** Name + one or several objects + 1 vector.   
[Advanced options](restore_presentation_parameters_page.md).

![transformation8.png](https://docs.salome-platform.org/latest/gui/GEOM/transformation8.png)

![mirror_axissn1.png](https://docs.salome-platform.org/latest/gui/GEOM/mirror_axissn1.png)

The initial shape and the mirror edge

![mirror_axissn2.png](https://docs.salome-platform.org/latest/gui/GEOM/mirror_axissn2.png)

The resulting shape (grey)

Finally an **Object** can be mirrored through a **Plane** of symmetry   
**TUI Command:** *geompy.MakeMirrorByPlane(Shape, Plane)*   
**Arguments:** Name + one or several objects + 1 plane   
[Advanced options](restore_presentation_parameters_page.md).

![transformation9.png](https://docs.salome-platform.org/latest/gui/GEOM/transformation9.png)

![mirror_planesn1.png](https://docs.salome-platform.org/latest/gui/GEOM/mirror_planesn1.png)

The initial shape and the mirror plane

![mirror_planesn2.png](https://docs.salome-platform.org/latest/gui/GEOM/mirror_planesn2.png)

The resulting shape (grey)

Our **TUI Scripts** provide you with useful examples of the use of [Transformation Operations](tui_transformation_operations_page.md#tui_mirror).
