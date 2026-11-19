<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/basic_prop_page.html -->

# Basic Properties

This operation returns Length, Surface and Volume properties for the selected geometrical object.

![neo-basicprop.png](https://docs.salome-platform.org/latest/gui/GEOM/neo-basicprop.png)

Note
:   This dialog supports navigation through the selectable objects (in OCC 3D viewer only):

    - Scroll mouse wheel with pressed *Ctrl* key or press *"S"*, *"P"* keys when input focus is in the viewer to navigate between selectable objects.
    - Press left mouse button to select an appropriate object to the dialog box.

    For more details, please refer to the *"Functionality common for OCC and VTK viewers"* chapter of the GUI module's documentation.

**TUI Command:** *geompy.BasicProperties(Shape, theTolerance=1.e-6),* where *Shape* is a shape whose properties are inquired, *theTolerance* is maximal relative error of area and volume computation.

See also a [TUI example](tui_basic_properties_page.md).
