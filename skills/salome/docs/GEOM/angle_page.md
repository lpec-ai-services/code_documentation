<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/angle_page.html -->

# Angle

This operation returns the angle in degrees between two lines or linear edges.

![angle.png](https://docs.salome-platform.org/latest/gui/GEOM/angle.png)

If both objects are **vectors**, the angle is computed in accordance with their orientations, otherwise the minimum angle is computed.

Note
:   This dialog supports navigation through the selectable objects (in OCC 3D viewer only):

    - Scroll mouse wheel with pressed *Ctrl* key or press *"S"*, *"P"* keys when input focus is in the viewer to navigate between selectable objects.
    - Press left mouse button to select an appropriate object to the dialog box.

    For more details, please refer to the *"Functionality common for OCC and VTK viewers"* chapter of the GUI module's documentation.

**TUI Command:** *geompy.GetAngle(shape1, shape2),* where Shape1 and Shape2 are shapes between which the angle is computed. Another TUI command is *geompy.GetAngleRadians(shape1,shape2),* which returns the value of angle in radians.

See also a [TUI example](tui_angle_page.md).
