<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_circle_page.html -->

# Circle

To create a **Circle** in the **Main Menu** select **New Entity - > Basic - > Circle**

There are 3 algorithms to create a **Circle** in the 3D space.   
The **Result** of each operation will be a GEOM_Object (edge).

Firstly, you can define a **Circle** by a **Center Point**, a **Vector** giving the circle's normal and a **Radius**.   
**TUI Command:** *geompy.MakeCircle(Point, Vector, Radius)*   
**Arguments:** Name + 1 vertex (for the center) + 1 edge (for the direction) + Radius.

Note
:   By default it is presumed that the **Center Point** is located at the Origin of the global coordinate system, and the **Vector** corresponds to OZ axis of the global coordinate system.

![circle1.png](https://docs.salome-platform.org/latest/gui/GEOM/circle1.png)

Secondly, you can define a **Circle** by three **Points** that lie on it.   
**TUI Command:** *geompy.MakeCircleThreePnt(Point1, Point2, Point3)*   
**Arguments:** Name + 3 points which will form the circle.

![circle2.png](https://docs.salome-platform.org/latest/gui/GEOM/circle2.png)

Finally, you can define a circle by a **Center Point** and two **Points**.   
  
**TUI Command:** *geompy.MakeCircleCenter2Pnt(Point1, Point2, Point3)*, where Point1 is the center of the circle, the distance between point1 and Point2 is the radius of the circle and Point3 helps to define the plane where the circle lies.   
**Arguments:** Name + 3 points.

![circle3.png](https://docs.salome-platform.org/latest/gui/GEOM/circle3.png)

**Example:**

![circles.png](https://docs.salome-platform.org/latest/gui/GEOM/circles.png)

A circle by vector and radius and a circle by three points

Our **TUI Scripts** provide you with useful examples of creation of [Basic Geometric Objects](tui_basic_geom_objs_page.md#tui_creation_circle).
