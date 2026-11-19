<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/check_bop_page.html -->

# Extract BOP Failure

The Extract BOP Failure tool makes it possible to analyse a BOP or Partition failure, in case the result is invalid.   
It performs the general fuse BOP and returns the resulting shape and the list of errors from Check Shape point of view.

This is a TUI-only functionality.

**TUI Command:**

- *(IsValid, ShapeRes, ShapeErrors) = geompy.ExtractBOPFailure(theShapes, theTimer=False, theTopo=False, theParallel=False, theExact=False, theVerbose=True),*   
  where   
  *theShapes* is the list of argument shapes for BOP.   
  *theTimer* - if True, the time of the operation is measured.   
  *theTopo* - if True, only the topological entities will be checked, otherwise geometry and topology are checked.   
  *theParallel* - if True, the operation will be executed in parallel.   
  *theExact* - if True, an exact check will be performed.   
  *theVerbose* - if True, prints execution errors and check results.   
  *Returns:*   
  *IsValid* - a boolean value (whether result shape is valid or not)   
  *ShapeRes* - the result shape itself   
  *ShapeErrors* - the list of [GEOM.GEOM_IMeasureOperations.ShapeError](../GEOM/geompy_doc/structGEOM_1_1GEOM__IMeasureOperations_1_1ShapeError.md)

See also a [TUI example](tui_check_bop_page.md).
