<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_explode_page.html -->

# Explode

To **Explode** an object into sub-shapes, in the **Main Menu** select **New Entity > Explode**. This operation opens the **Sub Shapes Selection** dialog box.

![neo-obj1.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-obj1.png)

To create a list of sub-shapes (vertices, edges, wires etc.) of the given shape using the **Explode** operation, you need to define the **Main Object**, which will be exploded and the **Type of Sub-shapes** you wish to obtain from it.

The **Result** of the operation will be a List of **GEOM_Objects** (vertexes, edges, wires, faces, shells or solids).

The choices available in the **Sub Shapes Type** combo box depend on the type of selected **Main Object**:

- **Compound:** to extract compounds;
- **Compsolid:** to extract compsolids;
- **Solid:** to extract solids;
- **Shell:** to extract shells;
- **Face:** to extract faces;
- **Wire:** to extract wires;
- **Edge:** to extract edges;
- **Vertex:** to extract vertices;
- **Shape:** to extract top-level contents of the compound shape;
- **Flat:** to extract "flat" contents of the compound shape.

Note: "flat" contents means that top-level simple-type sub-shapes are extracted from the compound object recursively (i.e. there are no compounds in the result).

Let us take, for example, compound C1 that contains solid S1 and another compound C2 that contains solids S2 and S3 (see the picture below):

- Explode operation with **Shape** type given as parameter will return S1 and C2;
- Explode operation with **Flat** type given as parameter will return S1, S2 and S3.

![flat_contents.png](https://docs.salome-platform.org/latest/gui/GEOM/flat_contents.png)

Switching on **Select Sub-shapes** check box allows manual selection of sub-shapes to be extracted from the main object. In this mode it is possible to select sub-shapes directly in 3D viewer.

When **Select Sub-shapes** check box is switched on, additional **Filter** controls allow to automatically pick up entities, which satisfy the specified threshold value(s). The numerical functor for each sub-shape that is compared with the threshold value(s) is computed according to the topological properties of the shape:

- length for edges and wires;
- area for faces and shells;
- volume for solids, compounds and compsolids.

Filtering capabilities are not available for vertices.

To filter out some entities it is necessary to do the following:

- Activate one or two filtering controls by switching on the corresponding check boxes;
- Select the required threshold comparator type; the following choices are available:
  - **Less Than** or **Equal or Less Than** for the first comparator;
  - **Greater Than** or **Equal or Greater Than** for the second comparator;
- Enter the required threshold value (values);
- Press **Apply** button in the **Filter** group.

The entities, which correspond to the entered filtering parameters, will be automatically highlighted in the 3D viewer.

Using **TUI Commands** you can perform this operation in a variety of ways:

- *geompy.ExtractShapes(Shape, Type, isSorted)* explodes a Shape into sub-shapes of a given Type and returns a List of sub-shapes. This method does not return the Shape itself if it matches the Type.
- *geompy.SubShapeAll(Shape, Type)* explodes a Shape into sub-shapes of a given Type and returns a List of sub-shapes.
- *geompy.SubShapeAllIDs(Shape, Type)* explodes a Shape into sub-shapes of a given Type and returns a List of IDs of sub-shapes.
- *geompy.SubShapeAllSortedCentres(Shape, Type)* explodes a shape into sub-shapes of a given type and sorts them taking into account their gravity centers, to provide a stable order of sub-shapes. It returns a list of sub-shapes.
- *geompy.SubShapeAllSortedCentresIDs(Shape, Type)* explodes a shape into sub-shapes of a given type and sorts them taking into account their gravity centers, to provide a stable order of sub-shapes. It returns a List of IDs of sub-shapes.
- *geompy.SubShape(Shape, Type, ListOfInd)* allows to obtain a compound of sub-shapes of the Shape, selected by their indexes in a list of all sub-shapes of the given Type. Each index is in the range [1, Nb_Sub-Shapes_Of_Given_Type].
- *geompy.SubShapeSortedCentres(Shape, Type, ListOfInd)* allows to obtain a compound of sub-shapes of the Shape, selected by their indexes in a sorted list of all sub-shapes of the given Type. Each index is in the range [1, Nb_Sub-Shapes_Of_Given_Type]

**Arguments:** 1 SHAPE + 1 type of SubShape.

**Example:**

![explode.png](https://docs.salome-platform.org/latest/gui/GEOM/explode.png)

A box exploded into faces
