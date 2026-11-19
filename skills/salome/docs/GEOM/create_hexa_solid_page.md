<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_hexa_solid_page.html -->

# Hexaedral solid

This operation allows to build a hexahedral solid bypassing the intermediate stage of building a shell and 4 faces (in case of building by 2 faces) or just a shell (in case of building by 6 faces).

There are 2 algorithms to create a hexahedral solid in the 3D space.   
The **Result** of the operation will be a **GEOM_Object** (solid).

Firstly, you can define a Hexahedral Solid by two faces, other four faces are created automatically.

**TUI Command:** *geompy.MakeHexa2Faces(F1, F2),* **Arguments:** Name + 2 Faces.

![block4.png](https://docs.salome-platform.org/latest/gui/GEOM/block4.png)

**Example:**

![image181.png](https://docs.salome-platform.org/latest/gui/GEOM/image181.png)

Hexahedral Solid built on the base of two Faces

Secondly, you can define a Hexahedral Solid by all six faces.

**TUI Command:** *geompy.MakeHexa(F1, F2, F3, F4, F5, F6),* **Arguments:** Name + 6 Faces.

![block5.png](https://docs.salome-platform.org/latest/gui/GEOM/block5.png)

**Example:**

![image180.png](https://docs.salome-platform.org/latest/gui/GEOM/image180.png)

Hexahedral Solid built on the base of six Faces

The created blocks can be processed with [Operations on Blocks](blocks_operations_page.md).

Our **TUI Scripts** provide you with useful examples of [Building by Blocks](tui_building_by_blocks_page.md).
