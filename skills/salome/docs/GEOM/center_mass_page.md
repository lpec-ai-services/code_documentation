<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/center_mass_page.html -->

# Center of Mass

This operation calculates and returns the coordinates of the gravity center for the selected geometrical object.

![measures3.png](https://docs.salome-platform.org/latest/gui/GEOM/measures3.png)

Press **Apply** or **Apply and Close** button to publish the **Point** in the study.

Note
:   This dialog supports navigation through the selectable objects (in OCC 3D viewer only):

    - Scroll mouse wheel with pressed *Ctrl* key or press *"S"*, *"P"* keys when input focus is in the viewer to navigate between selectable objects.
    - Press left mouse button to select an appropriate object to the dialog box.

    For more details, please refer to the *"Functionality common for OCC and VTK viewers"* chapter of the GUI module's documentation.

**TUI Command:**  *geompy.MakeCDG(Shape),* where *Shape* is the shape for which a center of gravity is computed.

See also a [TUI example](tui_center_of_mass_page.md).
