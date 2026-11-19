<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/rotation_operation_page.html -->

# Rotation

To produce a **Rotation** in the **Main Menu** select **Operations - > Transformation - > Rotation**

This operation **rotates** the initial shape.

The first **Rotation** algorithm needs you to define an **Object** to be rotated, an **Axis** of rotation and an **Angle** of rotation.   
**Reverse** checkbox allows to specify the direction of rotation.   
**Create a copy** checkbox allows to keep the initial object, otherwise it will be removed.   
[Advanced options](restore_presentation_parameters_page.md).

![transformation4.png](https://docs.salome-platform.org/latest/gui/GEOM/transformation4.png)

**TUI Command:** *geompy.MakeRotation(Shape, Axis, Angle)*   
**Arguments:** Name + one or several objects + 1 vector for direction of rotation + 1 angle.

The second algorithm allows to define the rotated **Object** by three points. Rotation axis will pass through the **Central Point** and will be will be orthogonal to a plane defned by three points. In this case rotation **Angle** is the angle between two vectors directed from the **Central Point** to **Point1** and **Point2**.   
**Reverse** checkbox allows to specify the direction of rotation.   
**Create a copy** checkbox allows to keep the initial object, otherwise it will be removed.   
[Advanced options](restore_presentation_parameters_page.md).

![transformation4a.png](https://docs.salome-platform.org/latest/gui/GEOM/transformation4a.png)

**TUI Command:** *geompy.MakeRotationThreePoints(Shape, CentralPoint, Point1, Point2)*   
**Arguments:** 1 shape + 3 points.

**Example:**

![rotationsn1.png](https://docs.salome-platform.org/latest/gui/GEOM/rotationsn1.png)

The initial shape (yellow)

![rotationsn2.png](https://docs.salome-platform.org/latest/gui/GEOM/rotationsn2.png)

The rotated shape (grey)

Our **TUI Scripts** provide you with useful examples of the use of [Transformation Operations](tui_transformation_operations_page.md#tui_rotation).
