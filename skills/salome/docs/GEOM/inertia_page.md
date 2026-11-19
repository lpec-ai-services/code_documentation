<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/inertia_page.html -->

# Inertia

This operation returns the axial moments of inertia for the selected geometrical object.

![measures4.png](https://docs.salome-platform.org/latest/gui/GEOM/measures4.png)

The table displays:

- 3*3 matrix of its own moments of inertia (in cells **i:j**) and
- the main (principal) moments of inertia **Ip1**, **Ip2** and **Ip3**

Note
:   The matrix of inertia is returned in the central coordinate system (G, Gx, Gy, Gz) where G is the centre of mass of the system and Gx, Gy, Gz the directions parallel to the X(1,0,0), Y(0,1,0), Z(0,0,1) directions of the absolute cartesian coordinate system.
:   There is always a set of axes for which the products of inertia of a geometric system are equal to 0. These axes are the principal axes of inertia. Their origin is coincident with the center of mass of the system. The associated moments are called the principal moments of inertia. The principal axes are not reported by this functionality.

Note
:   This dialog supports navigation through the selectable objects (in OCC 3D viewer only):

    - Scroll mouse wheel with pressed *Ctrl* key or press *"S"*, *"P"* keys when input focus is in the viewer to navigate between selectable objects.
    - Press left mouse button to select an appropriate object to the dialog box.

    For more details, please refer to the *"Functionality common for OCC and VTK viewers"* chapter of the GUI module's documentation.

**TUI Command:** *geompy.Inertia(Shape),* where *Shape* is a shape for which the own matrix of inertia and the main (principal) moments of inertia are returned.

See also a [TUI example](tui_inertia_page.md).
