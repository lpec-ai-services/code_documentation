<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_arc_page.html -->

# Arc

To create an **Arc** in the **Main Menu** select **New Entity - > Basic - > Arc**

There are 2 algorithms to create an **Arc** in the 3D space.   
The **Result** of each operation will be a GEOM_Object (edge).

Firstly, you can define an **Arc** by three **Points** that lie on it, where Point1 is the starting point, Point2 is a middle point of the arc and Point3 is the ending point of the arc.   
**TUI Command:** *geompy.MakeArc(Point1, Point2, Point3)*   
**Arguments:** Name + 3 vertices.

![arc.png](https://docs.salome-platform.org/latest/gui/GEOM/arc.png)

Secondly, you can define an **Arc** by **Center**, **Start** and **End** points. The arc is built from the **Start** point to the **End** point. The radius of the arc is defined by the distance between the **Center** point and the **Start** point. The **End** point defines the angle of the arc. If the distance between the **Center** point and the **End** point is not equal to the radius, the arc will be built anyway.   
**Reverse** radio button allows to change the direction of the arc.   
**TUI Command:** *geompy.MakeArcCenter(Center Point, Start Point, End Point, boolean Sense)*   
**Arguments:** Name + 3 vertices + Boolean.

![arc2.png](https://docs.salome-platform.org/latest/gui/GEOM/arc2.png)

Finally, it is possible to create an **Arc of Ellipse**, which is also done by three points: the Arguments **Point 1**, **Point 2** and the **Center Point**. The arc is built on the Ellipse that lies in the plane defined by the three points, with the center in the **Center point**. The major radius of the Ellipse is defined by the distance between the **Center Point** and the most remote Argument point. The minor radius is defined by the shortest distance between the other Argument point and the major radius.   
**TUI Command:** *geompy.MakeArcOfEllipse(Center Point, First Point, Second Point)*   
**Arguments:** Name + 3 vertices.

![arcofellipse2.png](https://docs.salome-platform.org/latest/gui/GEOM/arcofellipse2.png)

**Examples:**

![arcsn.png](https://docs.salome-platform.org/latest/gui/GEOM/arcsn.png)

Arc by three points lying on it.

![arcsn1.png](https://docs.salome-platform.org/latest/gui/GEOM/arcsn1.png)

Arc by Start, End and Center.

![arcsn2.png](https://docs.salome-platform.org/latest/gui/GEOM/arcsn2.png)

Reversed arc.

![arcofellipse1.png](https://docs.salome-platform.org/latest/gui/GEOM/arcofellipse1.png)

Arc Of Ellipse.

Our **TUI Scripts** provide you with useful examples of creation of [Basic Geometric Objects](tui_basic_geom_objs_page.md#tui_creation_arc).
