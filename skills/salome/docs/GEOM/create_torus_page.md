<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_torus_page.html -->

# Torus

To create a **Torus** in the **Main Menu** select **New Entity - > Primitives - > Torus**

There are two algorithms for creation of a **Torus**.   
The **Result** of each operation will be a GEOM_Object (SOLID).

Firstly, you can define a **Torus** by the given **Base Point**, the normal **Vector** and the Major and Minor **Radiuses**.   
**TUI Command:** *geompy.MakeTorus(Point, Vector, RadiusMajor, RadiusMinor)*   
**Arguments:** Name + 1 vertex + 1 vector (for direction) + 2 values (1 & 2 Radius).

![torus1.png](https://docs.salome-platform.org/latest/gui/GEOM/torus1.png)

Secondly, you can define a **Torus** with the center at the origin of coordinates by its Major and Minor **Radiuses**.   
**TUI Command:** *geompy.MakeTorusRR(RadiusMajor, RadiusMinor)*   
**Arguments:** Name + 2 values (1 & 2 Radius from the origin).

![torus2.png](https://docs.salome-platform.org/latest/gui/GEOM/torus2.png)

**Example:**

![toruses.png](https://docs.salome-platform.org/latest/gui/GEOM/toruses.png)

Toruses

Our **TUI Scripts** provide you with useful examples of creation of [Primitives](tui_primitives_page.md#tui_creation_torus).
