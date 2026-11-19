<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_squareface_page.html -->

# Rectangle

A primitive called **Rectangle** is a rectangular face of certain dimensions and orientation

To create a **Rectangle** in the **Main Menu** select **New Entity - > Primitives - > Rectangle**

There are 2 algorithms to create a **Rectangle** in the 3D space.   
The **Result** of each operation will be a GEOM_Object (Face).

Firstly, you can create a **Rectangle** at the origin of coordinates defining its boundaries by the height and the width and its axis by the orientation radio buttons (OXY, OYZ or OZX).This means that the **Rectangle** will lie in "OXY", "OYZ" or "OZX" plane correspondingly.   
**TUI Command:** *geompy.MakeFaceHW(Height, Width, Orientation)*   
**Arguments:** Name + 3 values (Dimensions at origin: height, width and orientation).

![face1.png](https://docs.salome-platform.org/latest/gui/GEOM/face1.png)

Secondly, you can define a **Rectangle** by the height and the width sizes and an **Edge** defining the normal to the center of the face.   
**TUI Command:** *geompy.MakeFaceObjHW(Vector, Height, Width)*   
**Arguments:** Name + 1 Vector (normal to the center) + 2 doubles (to describe a face sizes).

It is also possible to create a **Rectangle** from another selected face. For this, switch the **Object Type** button to **Face**, then select a face object and set the values of Height and Width for the new face. The created face will lie in the plane of the selected face.   
**TUI Command:** *geompy.MakeFaceObjHW(Face, Height, Width)*   
**Arguments:** Name + 1 Face + 2 parameters (to describe a face sizes).

![face2.png](https://docs.salome-platform.org/latest/gui/GEOM/face2.png)

**Example:**

![faces.png](https://docs.salome-platform.org/latest/gui/GEOM/faces.png)

Rectangle

Our **TUI Scripts** provide you with useful examples of creating [Primitives](tui_primitives_page.md#tui_creation_squareface).
