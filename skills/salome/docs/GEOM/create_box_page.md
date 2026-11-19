<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_box_page.html -->

# Box

To create a **Box** in the **Main Menu** select **New Entity - > Primitives - > Box**

There are 2 algorithms for creation of a **Box**.   
The **Result** of each operation will be a GEOM_Object (SOLID).

Firstly, you can define a **Box** by two specified **Vertices** (its opposite corners). The edges of the box will be parallel to the coordinate axes.   
**TUI Command:** *geompy.MakeBoxTwoPnt(Point1, Point2)*   
**Arguments:** Name + 2 vertices (opposite corners of the box).

![box1.png](https://docs.salome-platform.org/latest/gui/GEOM/box1.png)

Secondly, you can define a **Box** by specified dimensions along the coordinate axes and with edges, parallel to them. The center of the box will be at point (DX/2, DY/2, DZ/2).   
**TUI Command:** *geompy.MakeBoxDXDYDZ(DX, DY, DZ)*   
**Arguments:** Name + 3 values (dimensions at origin).

![box2.png](https://docs.salome-platform.org/latest/gui/GEOM/box2.png)

**NB!** There is a third way to create a **Box**, which is currently accessible only via **TUI** commands.   
You can define a **Box** by the coordinates of two **Vertices** (in this way you don't need to create them in advance).   
**TUI Command:** *geompy.MakeBox(x1,y1,z1,x2,y2,z2)*   
**Arguments:** Name + X, Y and Z coordinates of both points.

**Example:**

![boxes.png](https://docs.salome-platform.org/latest/gui/GEOM/boxes.png)

Boxes

Our **TUI Scripts** provide you with useful examples of creation of [Primitives](tui_primitives_page.md#tui_creation_box).
