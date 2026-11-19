<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_3dsketcher_page.html -->

# 3D Sketcher

3D Sketcher allows creating a closed or unclosed 3D wire, made of consequent straight segments.

**Example:**

![3dsketch4.png](https://docs.salome-platform.org/latest/gui/GEOM/3dsketch4.png)

To create a 3D Sketch, select in the main menu *New Entity -> Basic -> 3D Sketch*.

![3dsketch_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/3dsketch_dlg.png)

The first point of a sketch can be defined by **Absolute** coordinates X, Y and Z. After this, it is possible to add straight segments.

Each segment starts at the end point of the previous segment or at the first point of the sketch, if there are no validated segments.

The second point of a segment can be defined in two different ways depending on the selected **Coordinates Type** radio buttons:

By **Cartesian coordinates** , which can be either:

- **Absolute** coordinates **X**, **Y** and **Z**, or
- **Relative** coordinates **DX**, **DY** and **DZ** with respect to the previous applied point,

By **Angular coordinates**, which include:

- the **Length** of the segment and an **Angle** in the chosen plane (OXY for example) in **Relative** mode. The angle is then relative to a local coordinate system with the last point of the sketch as origin.

![3dsketch_angle_rel.png](https://docs.salome-platform.org/latest/gui/GEOM/3dsketch_angle_rel.png)

- the **Radius** (i.e. the distance from the origin) and an **Angle** in the chosen plane in **Absolute** mode

![3dsketch_angle_abs.png](https://docs.salome-platform.org/latest/gui/GEOM/3dsketch_angle_abs.png)

In both angular modes you can additionally specify the following:

- the second **Angle** (latitude)

![3dsketch_2angles_rel.png](https://docs.salome-platform.org/latest/gui/GEOM/3dsketch_2angles_rel.png)

- the **Height**

![3dsketch_angle_height_rel.png](https://docs.salome-platform.org/latest/gui/GEOM/3dsketch_angle_height_rel.png)

To validate a segment and to proceed with the definition of the next one, click **Apply** button. **Undo** and **Redo** buttons, respectively, remove or restore the last segment in the wire.

**Sketch Validation** button applies the wire, built by the user, "as is".   
**Sketch Closure** closes the Sketch by a straight line from the start to the end point and applies it.

## TUI Commands

*geompy.Make3DSketcher( [ PointsList ] )* This algorithm creates a wire from the list of real values, which define absolute XYZ coordinates of points. The Result of the operation will be a **GEOM_Object**.

Note
:   To make a closed wire using this TUI command, the first and the last point should have the same coordinates.

Another way to create the 3D Sketcher in TUI is using Sketcher3D interface.

*sk = geompy.Sketcher3D()*

Returns an instance of Sketcher3D interface *sk*.

Use the below examples and see the [Sketcher3D](../GEOM/geompy_doc/classgsketcher_1_1Sketcher3D.md) interface documentation for more information.

**TUI Scripts** provide you with useful examples of the use of [3D Sketcher](tui_3dsketcher_page.md).
