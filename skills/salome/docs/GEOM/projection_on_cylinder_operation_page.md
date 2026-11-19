<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/projection_on_cylinder_operation_page.html -->

# Projection on Cylinder

To produce a **Projection on Cylinder** in the **Main Menu** select **Operations - > Transformation - > Projection on Cylinder**

This operation makes a projection of a **Source planar wire or face** on a cylinder defined by its radius. The cylinder's coordinate system is the same as the global coordinate system. The result represents a wire or a face that represents a projection of the source shape onto a cylinder.

To make a projection it is necessary to define:

- **Object** to be projected. It can be either a planar wire or a face;
- **Radius** of the cylinder;
- **Starting angle** from the cylinder's X axis around Z axis. This is the angle of the projection start.
- **Length angle** where the total length of the wire should be projected. If it is unchecked the projection is not scaled and the natural wire length is kept for the projection.
- **Rotation angle** the angle between the tangent vector to the first curve at the first point of the object projection in 2D space and U-direction of the cylinder in 2D space.
- [Advanced options](restore_presentation_parameters_page.md).

![proj_on_cyl_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/proj_on_cyl_dlg.png)

The following figure explains the meaning of each input angle:

![proj_on_cyl_angles.png](https://docs.salome-platform.org/latest/gui/GEOM/proj_on_cyl_angles.png)

Input angles of projection on the cylinder

**Example:**

![proj_on_cyl_preview.png](https://docs.salome-platform.org/latest/gui/GEOM/proj_on_cyl_preview.png)

The curve (in red) and its projection on the cylinder

**TUI Command:** *geompy.MakeProjectionOnCylinder(theObject, theRadius, theStartAngle=0.0, theAngleLength=-1.0, theAngleRotation=0.0),* where *theObject* is a shape to be projected, *theRadius* is a cylinder radius, *theStartAngle* is the starting angle of projection in radians, *theAngleLength* the projection length angle in radians, *theAngleRotation* projection rotation angle in radians. The *Result* will be a *GEOM_Object*.

Our **TUI Scripts** provide you with useful examples of the use of [Transformation Operations](tui_transformation_operations_page.md#tui_projection).
