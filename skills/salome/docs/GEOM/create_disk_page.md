<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_disk_page.html -->

# Disk

A primitive called disk is a round plane with a certain radius and orientation

To create a **Disk** in the **Main Menu** select **New Entity - > Primitives - > Disk**

There are 3 algorithms to create a **Disk** in 3D space.   
The **Result** of each operation will be a GEOM_Object (face).

Firstly, you can create a **Disk** at the origin of coordinates defining its radius and selecting the orientation of its axis with radio buttons (OXY, OYZ or OZX).This means that the Disk will lie in "OXY", "OYZ" or "OZX" plane correspondingly.   
**TUI Command:** *geompy.MakeDiskR(Radius, Orientation)*   
**Arguments:** Name + 2 values (Dimensions at origin: radius and orientation).

![disk1.png](https://docs.salome-platform.org/latest/gui/GEOM/disk1.png)

Secondly, you can define a **Disk** by a **Center Point**, a **Vector** defining the normal of a circle and a **Radius**.   
**TUI Command:** *geompy.MakeDiskPntVecR(Point, Vector, Radius)*   
**Arguments:** Name + 1 vertex (for the center) + 1 edge (for the direction) + Radius.

![disk2.png](https://docs.salome-platform.org/latest/gui/GEOM/disk2.png)

Finally, you can define a **Disk** by three **Points** that lie on its boundary.   
**TUI Command:** *geompy.MakeDiskThreePnt(Point1, Point2, Point3)*   
**Arguments:** Name + 3 points which will form the disk.

![disk3.png](https://docs.salome-platform.org/latest/gui/GEOM/disk3.png)

**Example:**

![disks.png](https://docs.salome-platform.org/latest/gui/GEOM/disks.png)

Disks

Our **TUI Scripts** provide you with useful examples of creating [Primitives](tui_primitives_page.md#tui_creation_disk).
