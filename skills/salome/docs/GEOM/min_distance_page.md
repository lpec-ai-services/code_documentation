<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/min_distance_page.html -->

# Minimum Distance

This operation returns the minimum distance between two geometrical objects.

![distance.png](https://docs.salome-platform.org/latest/gui/GEOM/distance.png)

The query for minimum distance can find one or more solutions, or even an infinite set of solutions. However, the currently used OCCT algorithm finds a finite number of solutions even if an infinite set of solutions exists.

Select one of the found solutions in the **Solution** list to display it in the Viewer show values corresponding to this solution in the following fields:

- **Length** - the distance value;
- **DX**, **DY** and **DZ** the vector coordinates.

Press **Apply** or **Apply and Close** button to create a set of closest points, corresponding to all found solutions.

Note
:   This dialog supports navigation through the selectable objects (in OCC 3D viewer only):

    - Scroll mouse wheel with pressed *Ctrl* key or press *"S"*, *"P"* keys when input focus is in the viewer to navigate between selectable objects.
    - Press left mouse button to select an appropriate object to the dialog box.

    For more details, please refer to the *"Functionality common for OCC and VTK viewers"* chapter of the GUI module's documentation.

**TUI Commands:**

- *aDist = geompy.MinDistance(Shape1, Shape2),*
- *[aDist, DX, DY, DZ] = geompy.MinDistanceComponents(Shape1, Shape2),*
- *[nbSols, (x11, y11, z11, x21, y21, z21, ...)] = geompy.ClosestPoints(Shape1, Shape2),*

where *Shape1* and *Shape2* are the shapes, between which the minimal distance is computed.

See also a [TUI example](tui_min_distance_page.md).
