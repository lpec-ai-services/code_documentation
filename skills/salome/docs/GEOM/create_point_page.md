<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_point_page.html -->

# Point

To create a **Point** in the **Main Menu** select **New Entity - > Basic - > Point**

There are five algorithms to create a **Point** in the 3D space.   
Each time the **Result** of the operation will be a GEOM_Object (vertex).

Firstly, we can define a point by setting its X, Y and Z **Coordinates**.   
**TUI Command:** *geompy.MakeVertex(X, Y, Z)*   
**Arguments:** Name (Vertex_n by default) + X, Y and Z coordinates of the point.

![point1.png](https://docs.salome-platform.org/latest/gui/GEOM/point1.png)

Secondly, we can define a point by a **Reference** to another point and the shift of the coordinates of the new point regarding the coordinates of the old one.   
**TUI Command:** *geompy.MakeVertexWithRef(Reference, X,Y,Z).*   
**Arguments:** Name + 1 reference point + 3 coordinates defining the position of this point regarding the reference one.

![point2.png](https://docs.salome-platform.org/latest/gui/GEOM/point2.png)

Thirdly, we can define a point by an **Edge** and a **Parameter** indicating its position on the Edge, ranging from 0.0 to 1.0. For example, 0.5 means that the point is located in the middle of the edge.   
**TUI Command:** *geompy.MakeVertexOnCurve(Edge,Parameter,takeOrientationIntoAccount).*   
**Arguments:** Name + 1 edge + 1 Parameter defining the position of the point on the given edge + flag that tells if it is necessary to take the edge orientation into account.

![point3.png](https://docs.salome-platform.org/latest/gui/GEOM/point3.png)

Alternatively, it is possible to define a point by an **Edge** and a **Length**. The **Length** defines the position of the point on the given edge. It can exceed the length of the edge or be negative. In this case the edge is extrapolated along its curve (except for bezier and b-spline curves). The **Start Point** defines the direction for the length calculation (if not defined, the first vertex of the Edge is used, else the vertex of the Edge, which is closest to the Start Point).   
**TUI Command:** *geompy.MakeVertexOnCurveByLength(Edge,Length,StartPoint=None).*   
**Arguments:** Name + 1 edge + 1 Length + 1 Point.

![point3_3.png](https://docs.salome-platform.org/latest/gui/GEOM/point3_3.png)

It is also possible to define 3D coordinates of the point projected on the given edge to produce the resulting point.   
**TUI Command:** *geompy.MakeVertexOnCurveByCoord(Edge,X,Y,Z).*   
**Arguments:** Name + 1 edge + 3 coordinate values of the projected point.

![point3_2.png](https://docs.salome-platform.org/latest/gui/GEOM/point3_2.png)

Fourthly, we can define a point by intersection of two **Lines** or **Wires** (or a Wire and a Line). If they intersect only once, a point will be created. If there are several intersections, a compound of points will be created.   
**TUI Command:** *geompy.MakePointOnLinesIntersection(myLine1,myWire1).*   
**Arguments:** Name + 2 1D objects

![point4.png](https://docs.salome-platform.org/latest/gui/GEOM/point4.png)

Finally, we can define a point located on a **Face**. The position of the point on it can be defined in one of two ways:

- by two  **Parameters: U**  and **V**, ranging from 0.0 to 1.0. For example, (0.5; 0.5) means that the point is located in the middle of the face.   
  **TUI Command:** *geompy.MakeVertexOnSurface(myFace,myUParameter,myVParameter).*   
  **Arguments:** Name + 1 face + 2 Parameters defining the position of the point on the given face.

![point5.png](https://docs.salome-platform.org/latest/gui/GEOM/point5.png)

- by three coordinates of the point projected on the given face.   
  **TUI Command:** *geompy.MakeVertexOnSurfaceByCoord(myFace,X,Y,Z).*   
  **Arguments:** Name + 1 face + 3 coordinate values to project point on the given face.

![point5_2.png](https://docs.salome-platform.org/latest/gui/GEOM/point5_2.png)

Note
:   This dialog supports navigation through the selectable objects (in OCC 3D viewer only):

    - Scroll mouse wheel with pressed *Ctrl* key or press *"S"*, *"P"* keys when input focus is in the viewer to navigate between selectable objects.
    - Press left mouse button to select an appropriate object to the dialog box.

    For more details, please refer to the *"Functionality common for OCC and VTK viewers"* chapter of the GUI module's documentation.

**Example:**

![points.png](https://docs.salome-platform.org/latest/gui/GEOM/points.png)

Points by edge and parameter and by coordinates

Our **TUI Scripts** provide you with useful examples of creation of [Basic Geometric Objects](tui_basic_geom_objs_page.md#tui_creation_point).
