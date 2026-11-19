<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/tolerance_page.html -->

# Tolerance

This operation returns the maximum and the minimum tolerance for the selected geometrical object.

![new-tolerance.png](https://docs.salome-platform.org/latest/gui/GEOM/new-tolerance.png)

The table displays **Min** and **Max** tolerance values for **Face**, **Edge** and **Vertex** tolerance.

Note
:   This dialog supports navigation through the selectable objects (in OCC 3D viewer only):

    - Scroll mouse wheel with pressed *Ctrl* key or press *"S"*, *"P"* keys when input focus is in the viewer to navigate between selectable objects.
    - Press left mouse button to select an appropriate object to the dialog box.

    For more details, please refer to the *"Functionality common for OCC and VTK viewers"* chapter of the GUI module's documentation.

**TUI Command:** *geompy.Tolerance(Shape),* where *Shape* is a shape for which minimal and maximal tolerances are returned.

See also a [TUI example](tui_tolerance_page.md).
