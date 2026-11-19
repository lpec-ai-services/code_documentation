<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_line_page.html -->

# Line

To create a **Line** in the **Main Menu** select **New Entity - >Basic - > Line**

There are 2 algorithms to create a **Line** in the 3D space. The Result of each operation will be a GEOM_Object (edge).

Firstly you can define a **Line** by **Point1** and **Point2**, which are the points through which the **Line** passes.   
**TUI Command:** *geompy.MakeLineTwoPnt(Point1, Point2)*   
**Arguments:** Name + 2 vertices.

![line1.png](https://docs.salome-platform.org/latest/gui/GEOM/line1.png)

Secondly you can define a **Line** as intersection of **Plane1** and **Plane2**.   
**TUI Command:** *geompy.MakeLineTwoFaces(myFace1, myFace2)*   
**Arguments:** Name + 2 faces.

![line2.png](https://docs.salome-platform.org/latest/gui/GEOM/line2.png)

**Example:**

![lines.png](https://docs.salome-platform.org/latest/gui/GEOM/lines.png)

Line defined through points

**NB!** There is another way to create a line, which is currently accessible only via **TUI** commands.

You can define a line passing through the given **Point** and parallel to the given **Vector**.   
**TUI Command:** *geompy.MakeLine(Point, Vector)*

Our **TUI Scripts** provide you with useful examples of creation of [Basic Geometric Objects](tui_basic_geom_objs_page.md#tui_creation_line).
