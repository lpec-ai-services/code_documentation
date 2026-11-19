<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/check_shape_page.html -->

# Check Shape

This operation checks the topology of the selected geometrical object and returns True if it is valid.

![measures9.png](https://docs.salome-platform.org/latest/gui/GEOM/measures9.png)

In this dialog:

- **Object** - the checked object. **Selection** button allows picking it in the viewer or in the object browser.
- **Check also geometry** option allows testing the geometry of the object as well.
- If **Exact check of edge tolerances** is checked, exact calculation of gaps between curves of edges and surfaces of faces will be performed. If maximum deviation exceeds tolerance of edge, the shape reported as invalid. It takes more time, but gives better results.
- **Errors** list informs of possible errors.
- **Incriminated Sub-shapes** field outputs the list of sub-shapes that cause problem. It is possible to select them in the list and publish in the study for further analysis by clicking **Apply** or **Apply and Close** button.

**TUI Commands:**

- *geompy.CheckShape(theShape, theIsCheckGeom = False, theReturnStatus = 0, theIsExact = False),*   
  where   
  *theShape* is the shape checked for validity.   
  *theIsCheckGeom* is the flag that tells if geometry should be checked also.  
  *theReturnStatus* is the flag that can have the following values:

  - 0 - if theShape is invalid, a description of problem is printed. *IsValid* status is returned.
  - 1 - *IsValid* status and the description of problem are returned.
  - 2 - *IsValid* status and the list of error data are returned.

  *theIsExact* is the flag to switch on/off exact calculation of edge tolerances.
- *geompy.PrintShapeErrors(self, theShape, theShapeErrors, theReturnStatus = 0),*   
  where   
  *theShape* is the shape checked for validity.   
  *theShapeErrors* are the shape errors obtained by CheckShape.   
  *theReturnStatus* is the flag that can have the following values:
  - 0 - the problem description is printed and nothing is returned.
  - 1 - the problem description is returned.

See also a [TUI example](tui_check_shape_page.md).
