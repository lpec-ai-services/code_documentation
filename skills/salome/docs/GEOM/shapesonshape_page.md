<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/shapesonshape_page.html -->

# Get Shapes on Shape

This operation is a special case of **Explode** operation. It produces a group of sub-shapes of the exploded shape, which are located in a definite way relatively another reference shape. The reference shape should be a solid.

To use this operation, select in the Main Menu **Operations -> Get Shapes on Shape.** The following dialog box will appear.

![shapesonshape.png](https://docs.salome-platform.org/latest/gui/GEOM/shapesonshape.png)

- **Name** is the name of the resulting group of shapes;
- **Shape for exploding** is the shape that will be exploded;
- **Solid for checking** is the reference shape, which should be a solid;
- **Reconstruction Limit** is the type of created sub-shapes: solid, shell, face, wire, edge, vertex;
- **State** is the position of the created sub-shapes relatively the reference shapes:
  - IN - the created sub-shapes are located inside the reference shape;
  - OUT - the created sub-shapes are located outside the reference shape;
  - ON - the created sub-shapes lie on the reference shape;
  - ONIN - the created sub-shapes lie on the reference shape or are located inside it;
  - ONOUT - the created sub-shapes lie on the reference shape or are located outside it;

**Advanced options** [Preview](restore_presentation_parameters_page.md#preview_anchor)

Example:

In the images below the box is the exploded shape and the cylinder is the reference shape. In the first image the edge IN the reference cylinder is highlighted in red, in the second the edges OUT of the reference cylinder are highlighted.

![shonshex1.png](https://docs.salome-platform.org/latest/gui/GEOM/shonshex1.png)

![shonshex2.png](https://docs.salome-platform.org/latest/gui/GEOM/shonshex2.png)
