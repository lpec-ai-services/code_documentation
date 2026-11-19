<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_revolution_page.html -->

# Revolution

To create an extruded shape by **Revolution** in the **Main Menu** select **New Entity - > Generation - > Revolution**

To create an extruded shape by **Revolution** you need to define the source **Object** to rotate, the **Axis** of revolution and the **Angle** by which the **Shape** has to be rotated around the **Axis** (in degrees).  
It is possible to select in GUI several objects to make several revolutions (using Shift button).   
 **Both Directions**  checkbox allows extruding the source object both forward and backward.   
The **Result** of the operation will be a GEOM_Object (edge, face, shell, solid or compsolid).

**TUI Command:** *geompy.MakeRevolution(Shape, Axis, Angle).*   
**Arguments:** Name + 1 shape (vertex, edge, planar wire, face or shell) serving as base object + 1 vector (for direction) + 1 value (angle).   
**Advanced options** [Preview](restore_presentation_parameters_page.md#preview_anchor)

![revolution.png](https://docs.salome-platform.org/latest/gui/GEOM/revolution.png)

**Example:**

![revolutionsn.png](https://docs.salome-platform.org/latest/gui/GEOM/revolutionsn.png)

Body of revolution

Our **TUI Scripts** provide you with useful examples of creation of [Complex Geometric Objects](tui_complex_objs_page.md#tui_creation_revolution).
