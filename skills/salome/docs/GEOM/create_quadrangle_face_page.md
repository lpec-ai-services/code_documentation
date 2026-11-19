<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_quadrangle_face_page.html -->

# Quadrangle face

This operation allows to build a face bypassing the intermediate stage of building edges and wires (in case of building by 4 points) or wires (in case of building by 4 or 2 edges).

There are 3 algorithms to create a Quadrangle Face in the 3D space.   
The **Result** of each op

The created blocks can be processed with [Operations on Blocks](blocks_operations_page.md).

Our **TUI Scripts** provide you with useful examples of [Building by Blocks](tui_building_by_blocks_page.md)

The created blocks can be processed with [Operations on Blocks](blocks_operations_page.md).

Our **TUI Scripts** provide you with useful examples of [Building by Blocks](tui_building_by_blocks_page.md). age "Building by Blocks". eration will be a **GEOM_Object** (face).

Firstly you can define a Quadrangle Face by four vertices. Edges are created automatically.

**TUI Command:** *geompy.MakeQuad4Vertices(V1, V2, V3, V4),* **Arguments:** Name + 4 Points.

![block1.png](https://docs.salome-platform.org/latest/gui/GEOM/block1.png)

Secondly, you can define a Quadrangle Face by two edges, while the other two edges are created automatically. **TUI Command:** *geompy.MakeQuad2Edges(E1, E2)* **Arguments:** Name + 2 Edges.

![block2.png](https://docs.salome-platform.org/latest/gui/GEOM/block2.png)

Finally, you can define a Quadrangle Face by four edges.

**TUI Command:** *geompy.MakeQuad(E1, E2, E3, E4),*. **Arguments:** Name + 4 Edges.

![block3.png](https://docs.salome-platform.org/latest/gui/GEOM/block3.png)

**Example:**

![image185.png](https://docs.salome-platform.org/latest/gui/GEOM/image185.png)

Quadrangle face built by blocks
