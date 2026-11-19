<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_plane_page.html -->

# Plane

To create a **Plane** in the **Main Menu** select **New Entity - > Basic - > Plane**

There are three algorithms to create a plane in the 3D space.   
The **Result** of each operation will be a GEOM_Object (face).

Firstly, you can define a **Plane** by a **Point** through which the plane passes, a **Vector** giving a normal of the plane and a **Size of the Plane** (size of a side of quadrangle face, representing the plane).   
**TUI Command:** *geompy.MakePlane(Point, Vector, TrimSize)*   
**Arguments:** Name + 1 vertex + 1 vector + 1 value (to define the size of the plane).

![plane1.png](https://docs.salome-platform.org/latest/gui/GEOM/plane1.png)

Secondly, you can define a **Plane** by three **Points** through which the plane passes and a **Size of the Plane**.   
**TUI Command:** *geompy.MakePlaneThreePnt(Point1, Point2, Point3, TrimSize)*   
**Arguments:** Name + 3 vertices + 1 value (to define the size of the plane).

![plane2.png](https://docs.salome-platform.org/latest/gui/GEOM/plane2.png)

Thirdly, you can define a **Plane** by another **Plane** or **Face** and a **Size of the Plane**.   
**TUI Command:** *geompy.MakePlaneFace(Face, TrimSize)*   
**Arguments:** Name + 1 face + 1 value (to define the size of the plane).

![plane3.png](https://docs.salome-platform.org/latest/gui/GEOM/plane3.png)

Fourthly, you can define a **Plane** by two Vectors. The first vector defines the center point and the direction, the second vector defines the normal to the Plane.   
**TUI Command:** *geompy.MakePlane2Vec(Vec1, Vec2, TrimSize)*   
**Arguments:** Name + 2 vectors + 1 value (to define the size of the plane).

![plane4.png](https://docs.salome-platform.org/latest/gui/GEOM/plane4.png)

Finally, you can define a **Plane** by the Local Coordinate System and the orientation (OXY, OYZ, OZX).   
**TUI Command:** *geompy.MakePlaneLCS(LCS, TrimSize, [1, 2, or 3])*   
**Arguments:** Name + LCS + 1 value (to define the size of the plane) + 1 value (to define the orientation)

![plane5.png](https://docs.salome-platform.org/latest/gui/GEOM/plane5.png)

**Examples:**

![planes1.png](https://docs.salome-platform.org/latest/gui/GEOM/planes1.png)

Planes created on the basis of the Global Coordinate System

![plane_on_face.png](https://docs.salome-platform.org/latest/gui/GEOM/plane_on_face.png)

A Plane created on a Face of another Shape

Our **TUI Scripts** provide you with useful examples of creation of [Basic Geometric Objects](tui_basic_geom_objs_page.md#tui_creation_plane).
