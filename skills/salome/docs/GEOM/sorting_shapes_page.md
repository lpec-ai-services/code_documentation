<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/sorting_shapes_page.html -->

# Sorting Shapes Algorithm

Some algorithms of [GEOM](../GEOM/geompy_doc/namespaceGEOM.md) module return a list of shapes sorted in accordance with some criterion. The goal of this sorting is a possibility to obtain stable result regardless SALOME version being used.

The algorithm that provides such a possibility consists of the following steps:

1. For each shape a pair of point and number is associated. The point and number depend on the shape type:

   |  |  |  |
   | --- | --- | --- |
   | Shape Type | Point | Number |
   | Vertex | Vertex isself | Orientation value converted to double |
   | Edge, Wire | Center of mass | Total length of edges |
   | Face, Shell | Center of mass | Total area of faces |
   | Other | Center of mass | Total volume of solids |
2. Each point is converted to double using the following expression:
   ```python
   point.X() * 999.0 + point.Y() * 99.0 + point.Z() * 0.9
   ```
3. The shapes are sorted in ascending order. The shape comparison criterion is the following. Shape_1 is considered less then Shape_2 if:
   - Shape_1's double value obtained on the step 2 is less than the corresponding value of Shape_2.  
     **Otherwise** if they are equal with the confusion tolerance (1.e-7):
   - Shape_1's number obtained on the step 1 is less than the corresponding number of Shape_2.  
     **Otherwise** if they are equal with the confusion tolerance (1.e-7) and the shapes have either Face or more complex type:
   - Shape_1's squared diagonal of bounding box is less than the one of Shape_2.  
     **Otherwise** if they are equal with the confusion tolerance (1.e-7):
   - Get the minimal and maximal values of X, Y and Z coordinates of bounding boxes for Shape_1 and Shape_2. Compute the following values for Shape_1 and Shape_2:
     ```python
     (aXmin+aXmax) * 999.0 + (aYmin+aYmax) * 99.0 + (aZmin+aZmax) * 0.9
     ```
      Shape_1 is less than Shape_2 if this value for Shape_1 is less than the value for Shape_2.

This algorithm is used in the following [geomBuilder](../GEOM/geompy_doc/classgeomBuilder_1_1geomBuilder.md) methods:

- [SubShapeAllSortedCentres](../GEOM/geompy_doc/group__l4__decompose.md#gaea264a43aec703d8e75a94c1340fa028)
- [SubShapeAllSortedCentresIDs](../GEOM/geompy_doc/group__l4__decompose.md#ga701a350a3627eba81be044ae18f8b79a)
- [SubShapeSortedCentres](../GEOM/geompy_doc/group__l4__decompose.md#ga7997ff327d631291011eb2cb494ba6eb)
- [ExtractShapes](../GEOM/geompy_doc/group__l4__decompose.md#ga5b9728065321f28d5e0099f609d1af13)

and as a part of some other algorithms where sorting is required.
