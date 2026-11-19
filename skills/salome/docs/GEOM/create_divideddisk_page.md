<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_divideddisk_page.html -->

# DividedDisk

The **Divided disk** object is a disk divided into **blocks** for easy hexahedral meshing. Two division patterns are available :

- A square pattern, which is frequently used;
- A hexagonal pattern, which ensures a better mesh quality and especially less acute or obtuse angles.

Moreover, this shape can be used as a basis in an [Extrusion along a path](create_extrusion_alongpath_page.md) operation in order to obtain any **tube shape** prepared for hexahedral meshing (see example below). (Another alternative is to create a 2D mesh on the divided disk and create a 3D mesh by extrusion in the SMESH module.)

Example:

![divided_disk.png](https://docs.salome-platform.org/latest/gui/GEOM/divided_disk.png)

To create a  **Divided Disk**  in the **Main Menu** select **New Entity - > Advanced - > DividedDisk**

There are 2 ways to create a  **Divided Disk** in 3D space.   
For both operations : Specify the parameters of the DividedDisk object creation in the opened dialog box and press "Apply" or "Apply & Close" button. The result of each operation will be a GEOM_Object.

At first it is possible to define a disk by its radius and orientation (plane "OXY", "OYZ" or "OZX"). The resulting disk is located at the origin of coordinates

**TUI Command:** *geompy.MakeDividedDisk(Radius, Orientation, Pattern)*

**Arguments:**

- **Radius** - Radius of the disk
- **Orientation** - Plane on which the disk will be built
- **Pattern** - Division pattern

![divided_disk_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/divided_disk_dlg.png)

At second the disk can be defined by its center, normal and radius.

**TUI Command:** *geompy.MakeDividedDiskPntVecR(Center, Vector, Radius, Pattern)*

**Arguments:**

- **Center** - Center of the disk
- **Vector** - Normal to the plane of the disk
- **Radius** - Radius of the disk
- **Pattern** - Division pattern

![divided_disk_PntVecR_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/divided_disk_PntVecR_dlg.png)

Our **TUI Scripts** provide you with useful examples of creation of [Advanced objects](tui_advanced_geom_objs_page.md#tui_creation_divideddisk).
