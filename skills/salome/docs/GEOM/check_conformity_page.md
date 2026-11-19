<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/check_conformity_page.html -->

# Check Conformity

The Check Conformity tool provides the user with a simple python API to analyze, available shape for Boolean Operations or not.   
Also tool provide advanced output to indicate imperfections in the input shape.

This is just a TUI functionality.

**TUI Commands:**

- *geompy.CheckConformity(shape),*   
  where   
  *shape* is the shape checked for validity.

  The following functionality is available from the tool:
- *geompy.isValid()*
- *geompy.selfIntersected2D()*
- *geompy.interferingSubshapes(shapeType1, shapeType2),* where   
  *shapeType1* is the first type of subshape.   
  *shapeType2* is the second type of subshape.
- *geompy.smallEdges()*
- *geompy.distantShapes(shapeType, subShapeType, tolerance),* where   
  *shapeType* is the type of shape.   
  *subShapeType* is the type of subshape.   
  *tolerance* is available tolerance, by default used tolerance of sub-shape.
- *geompy.updateTolerance()*

See also a [TUI example](tui_check_conformity_page.md).
