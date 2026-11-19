<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/limitToleranceFeature.html -->

# Limit Tolerance

Limit Tolerance feature tries to set a new value of tolerance for the given shape. However, the final tolerance value also
depends on the initial shape topology (takes into consideration the existing gaps) to obtain a valid resulting shape.

To limit the tolerance in the active part:

1. select in the Main Menu *Features - > Limit Tolerance* item or
2. click ![limit_tol_btn.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/limit_tol_btn.png) **Limit Tolerance** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/LimitTolerance.png)

**Limit Tolerance operation**

Here it is necessary to select a shape and give a value for the desired tolerance value.

- **Shape** sets the shape to be modified.
- **Tolerance** sets the desired tolerance value for the selected shape.
- **Exact check of edge tolerances** if checked, exact calculation of gaps
  :   between curves of edges and surfaces of faces will be performed.
      It takes more time, but gives better results.
      Please note, that this gap value will limit the tolerance below, but not above.

Example of usage:

1. Partition objects obj1 and obj2.
2. Partition fails.
3. Perform Limit Tolerance on objects obj1 and obj2.
4. Try to partition them again.

**TUI Command**:

model.addLimitTolerance(*Part_doc*, *shape*, *tolerance*, *isExact*)
:   Parameters:
    :   - **part** – The current part object.
        - **shape** – A shape.
        - **tolerance** – A tolerance value.
        - **isExact** – An exact check flag.

    Returns:
    :   Result shape with the modified tolerance.

## Result

The Result of the operation will be the selected shape with an updated tolerance, where possible.

**See Also** a sample TUI Script of [Limit Tolerance](TUI_limitToleranceFeature.md#tui-limit-tolerance) operation.
