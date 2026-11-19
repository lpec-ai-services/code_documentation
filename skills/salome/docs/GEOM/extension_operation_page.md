<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/extension_operation_page.html -->

# Extension

To produce an **Extension** of an Edge or a Face select in the **Main Menu** **Operations - > Transformation - > Extension**. The type of extension is defined using the radio buttons.

Firstly it is possible to resize an **Edge** by modifying its first and last parameters

![extension1.png](https://docs.salome-platform.org/latest/gui/GEOM/extension1.png)

Edge Extension

**TUI Command:** *geompy.ExtendEdge(theEdge, theMin, theMax)*, where *theEdge* the input edge to be resized, *theMin* the minimal parameter value, *theMax* the maximal parameter value.   
**Arguments:** Name + Object (Edge) + 2 values (Min and Max Parameters).

**Example:**

![extend_edge_example.png](https://docs.salome-platform.org/latest/gui/GEOM/extend_edge_example.png)

Original edge (white) and extended edge

Note
:   The input Edge parameters range is [0, 1]. If **theMin** parameter is negative, the input Edge is extended, otherwise it is shrinked by **theMin** parameter. If **theMax** is greater than 1, the Edge is extended, otherwise it is shrinked by **theMax** parameter.

Secondly it is possible to resize a **Face** by modifying its minimal and maximal U- and V-Parameters.

![extension2.png](https://docs.salome-platform.org/latest/gui/GEOM/extension2.png)

Face Extension

**TUI Command:** *geompy.ExtendFace(theFace, theUMin, theUMax, theVMin, theVMax)*, where *theFace* the input face to be resized, *theUMin* the minimal U-Parameter value, *theUMax* the maximal U-Parameter value, *theVMin* the minimal V-Parameter value, *theVMax* the maximal V-Parameter value.   
**Arguments:** Name + Object (Face) + 4 values (Min and Max U- and V-Parameters).

**Example:**

![extend_face_example.png](https://docs.salome-platform.org/latest/gui/GEOM/extend_face_example.png)

The original face (gray) and a result face shrinked along U-Direction and extended along V-Direction

Note
:   The input Face U- and V-Parameters range is [0, 1]. If **theUMin** parameter is negative, the input Face is extended, otherwise it is shrinked along U-Direction by **theUMin** parameter. If **theUMax** is greater than 1, the Face is extended, otherwise it is shrinked along U-Direction by **theUMax** parameter. The same applies to **theVMin**, **theVMax** and V-Direction of the input Face.

Our **TUI Scripts** provide you with useful examples of the use of [Extension Operations](tui_transformation_operations_page.md#tui_extend).
