<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/whatis_page.html -->

# What Is ?

This operation provides the list of types and quantities of all topological entities, composing the selected geometrical object.

The information about *COMPOUND* or *COMPSOLID* shapes additionally shows "flat" content - the number of "simple" top-level shapes enclosed into the compound.

![measures8.png](https://docs.salome-platform.org/latest/gui/GEOM/measures8.png)

Note
:   This dialog supports navigation through the selectable objects (in OCC 3D viewer only):

    - Scroll mouse wheel with pressed *Ctrl* key or press *"S"*, *"P"* keys when the input focus is in the viewer to navigate between selectable objects.
    - Press left mouse button to select an appropriate object to the dialog box.

    For more details, please refer to the *"Functionality common for OCC and VTK viewers"* chapter of the GUI module's documentation.

**TUI Command:** *geompy.WhatIs(Shape),* where *Shape* is a shape from which a description is returned.

**Kind of Shape** field characterizes the whole shape. If there is no additional information about the shape, **Basic Properties** button is disabled, otherwise it provides information about center and dimensions of the shape.

![measures8a.png](https://docs.salome-platform.org/latest/gui/GEOM/measures8a.png)

**TUI Command:** *geompy.KindOfShape(Shape),* where *Shape* is a shape from which a description is returned.

See also a [TUI example](tui_whatis_page.md).
