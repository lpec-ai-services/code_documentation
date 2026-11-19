<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_cylinder_page.html -->

# Cylinder

To create a **Cylinder** in the **Main Menu** select **New Entity - > Primitives - > Cylinder**

There are 2 algorithms for creation of a **Cylinder**.   
The **Result** of each operation will be a GEOM_Object (SOLID).

Firstly, you can define a **Cylinder** by the **Base Point** (the central point of the cylinder base), the **Vector** (the axis of the cylinder), and its dimensions: the **Radius** and the **Height**. You can optionally specify the **Angle** to create a portion of cylinder.

**TUI Command:** *geompy.MakeCylinder(Point, Axis, Radius, Height)*   
**Arguments:** Name + 1 vertex + 1 vector + 2 values (Dimensions: radius and height).

**TUI Command:** *geompy.MakeCylinderA(Point, Axis, Radius, Height, Angle)*   
**Arguments:** Name + 1 vertex + 1 vector + 3 values (Dimensions: radius, height and angle).

![cylinder1.png](https://docs.salome-platform.org/latest/gui/GEOM/cylinder1.png)

Secondly, you can define a **Cylinder** by the given **Radius** and **Height** at the origin of coordinate system. The axis of the cylinder will be collinear to the OZ axis of the coordinate system. Similarly to the first constructor, you can optionally specify the **Angle** to create a portion of cylinder.

**TUI Command:** *geompy.MakeCylinderRH(Radius, Height)*   
**Arguments:** Name + 2 values (Dimensions at origin: radius and height).

**TUI Command:** *geompy.MakeCylinderRHA(Radius, Height, Angle)*   
**Arguments:** Name + 3 values (Dimensions at origin: radius, height and angle).

![cylinder2.png](https://docs.salome-platform.org/latest/gui/GEOM/cylinder2.png)

**Example:**

![cylinders.png](https://docs.salome-platform.org/latest/gui/GEOM/cylinders.png)

Cylinders

Our **TUI Scripts** provide you with useful examples of creation of [Primitives](tui_primitives_page.md#tui_creation_cylinder).
