<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_vector_page.html -->

# Vector

To create a **Vector** in the **Main Menu** select **New Entity - > Basic - > Vector**

There are 2 algorithms to create a **Vector** in the 3D space.   
The **Result** of each operation will be a GEOM_Object (edge).

Firstly, you can define a Vector by its **Start** and **End Points**.   
**TUI Command:** *geompy.MakeVector(Point1, Point2)*   
**Arguments:** Name + 2 vertices.

![vector1.png](https://docs.salome-platform.org/latest/gui/GEOM/vector1.png)

Secondly, you can define a **Vector** starting in the **Origin of coordinates** by its **End Point**.   
**TUI Command:** *geompy.MakeVectorDXDYDZ(DX, DY, DZ)*   
**Arguments:** Name + 3 values

![vector2.png](https://docs.salome-platform.org/latest/gui/GEOM/vector2.png)

**Example:**

![image34.png](https://docs.salome-platform.org/latest/gui/GEOM/image34.png)

A vector by two points and a vector from the origin of coordinates

Our **TUI Scripts** provide you with useful examples of creation of [Basic Geometric Objects](tui_basic_geom_objs_page.md#tui_creation_vector).
