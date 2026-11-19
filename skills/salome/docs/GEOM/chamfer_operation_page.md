<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/chamfer_operation_page.html -->

# Chamfer

To produce a **Chamfer** in the **Main Menu** select **Operations - > Chamfer**

This operation allows you to make chamfer of the edges of a Shape.   
The **Result** will be a **GEOM_Object**.

To create chamfer on all edges of the given shape, you need to define the **Main Object** to create a chamfer on and the **Dimension** (radius) of the chamfer.   
**TUI Command:** *geompy.MakeChamferAll(Shape, D)*   
**Arguments:** Name + 1 SHAPE + 1 value (Chamfer dimension).   
**Advanced options** [Preview](restore_presentation_parameters_page.md#preview_anchor)

![chamfer1.png](https://docs.salome-platform.org/latest/gui/GEOM/chamfer1.png)

![chamfer_all.png](https://docs.salome-platform.org/latest/gui/GEOM/chamfer_all.png)

Chamfer on the whole object

In the algorithms below there exist two ways to define the **Dimension** of the Chamfer   
Firstly the **Dimension** can be defined via **D1** and **D2**, which represent the offset on the first and the second face forming the edge.   
Secondly the **Dimension** can be defined via **D**, which represents the offset on the first face, and the **Angle**, which is the angle between the first face and the chamfer plane.

To create chamfer on the specified edges of the given shape, you need to define the **Main Object** to create a fillet on, select the two faces to which belongs the necessary common edge in the viewer and define the **Dimension** of the Chamfer.   
**TUI Command:** *geompy.MakeChamferEdge(Shape, D1, D2, Face1, Face2),* where *Shape* is a shape to create a chamfer on, *D1* is a chamfer size along *Face1*, *D2* is a chamfer size along *Face2*, *Face1* and *Face2* are indices of faces in Shape.

**Alternative TUI Command:** *geompy.MakeChamferEdge(Shape, D, Angle, Face1, Face2),* where *D1* is a chamfer size along *Face1* and *Angle* is the angle between Face1 and the chamfer plane.

![chamfer2.png](https://docs.salome-platform.org/latest/gui/GEOM/chamfer2.png)

![chamfer_edge.png](https://docs.salome-platform.org/latest/gui/GEOM/chamfer_edge.png)

Chamfer on the specified edges

To create chamfer on the specified faces of the given shape, you need to define the **Main Object** to create a fillet on, select the necessary faces the OCC Viewer and define the **Dimension** of the Chamfer.   
**TUI Command:** *geompy.MakeChamferFaces(Shape, D1, D2, ListOfFaceID),* where *Shape* is a shape to create chamfer on, *D1* and D2 are chamfer sizes along faces from *ListOfFaceID*. For each Edge Face1 and Face2 are defined basing on their indices.

**Alternative TUI Command:** *geompy.MakeChamferFaces(Shape, D, Angle, ListOfFaceID),* where *D1* is a chamfer size along *Face1* and *Angle* is the angle between Face1 and the chamfer plane.

![chamfer3.png](https://docs.salome-platform.org/latest/gui/GEOM/chamfer3.png)

![chamfer_faces.png](https://docs.salome-platform.org/latest/gui/GEOM/chamfer_faces.png)

Chamfer on the specified faces

To create chamfer on an arbitrary set of edges of the given shape to define the **Main Object** to create a fillet on, select the necessary edges the OCC Viewer and define the **Dimension** of the Chamfer.   
**TUI Command:** *geompy.MakeChamferEdges(Shape, D1, D2, ListOfEdgeID),* where *Shape* is a shape to create chamfer on, *D1* and D2 are chamfer sizes along faces defined by the algorithm basing on *ListOfEdgeID*, which is a list of indices of edges in *Shape*. For each Edge the algorithm selects Face1 and Face2 basing on their indices.

**Alternative TUI Command:** *geompy.MakeChamferEdges(Shape, D, Angle, ListOfEdgeID),* where *D1* is a chamfer size along *Face1* and *Angle* is the angle between Face1 and the chamfer plane.

![chamfer4.png](https://docs.salome-platform.org/latest/gui/GEOM/chamfer4.png)

Our **TUI Scripts** provide you with useful examples of the use of [Transformation Operations](tui_transformation_operations_page.md#tui_chamfer).
