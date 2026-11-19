<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/boundaries_page.html -->

# Check Free Boundaries

This operation detects and highlights the free boundaries of the selected object.

Free boundaries are wires and edges that are not shared between two faces.

![repair9.png](https://docs.salome-platform.org/latest/gui/GEOM/repair9.png)

The information about the number of closed and open free boundaries is also provided.

Press **Apply** or **Apply and Close** button to publish the corresponding wires or edges in the study.

![repair9a.png](https://docs.salome-platform.org/latest/gui/GEOM/repair9a.png)

Free boundary of a compound

**TUI Command:** *(NoError, ClosedWires, OpenWires) = geompy.GetFreeBoundary(Shape),* where *Shape* is a shape to be checked, *NoError* is false if an error occurred while checking free boundaries, *ClosedWires* is a list of closed free boundary wires, *OpenWires* is a list of open free boundary wires.

See also a [TUI example](tui_free_boundaries_page.md).
