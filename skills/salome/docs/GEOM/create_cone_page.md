<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_cone_page.html -->

# Cone

To create a **Cone** in the **Main Menu** select **New Entity - > Primitives - > Cone**

There are two algorithms for creation of a **Cone**.   
The **Result** of each operation will be a GEOM_Object (SOLID).

Firstly, you can define a **Cone** by the **Base Point** (the central point of the cone base), the **Axis**, the **Height** and the first and the second **Radiuses**.   
**TUI Command:** *geompy.MakeCone(Point, Axis, Radius1, Radius2, height)*   
**Arguments:** Name + 1 vertex + 1 vector (for direction) + 3 values (Radius of the base part, radius of the upper part, height).

![cone1.png](https://docs.salome-platform.org/latest/gui/GEOM/cone1.png)

Secondly, you can define a **Cone** with the center at the origin of coordinates by its **Height** and **Radiuses**. The **Axis** of the **Cone** will be collinear to the OZ axis of the coordinate system.   
**TUI Command:** *geompy.MakeConeR1R2H(Radius1, Radius2, Height)*   
**Arguments:** Name + 3 values (Radius of the base part, radius of the upper part, height).

![cone2.png](https://docs.salome-platform.org/latest/gui/GEOM/cone2.png)

Note
:   If both radiuses are non-zero, the **Cone** will be truncated. If the radiuses are equal, a **Cylinder** will be created instead.

**Example:**

![cones.png](https://docs.salome-platform.org/latest/gui/GEOM/cones.png)

Normal and truncated cones

Our **TUI Scripts** provide you with useful examples of creation of [Primitives](tui_primitives_page.md#tui_creation_cone).
