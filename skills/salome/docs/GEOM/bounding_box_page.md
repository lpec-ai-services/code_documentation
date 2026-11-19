<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/bounding_box_page.html -->

# Bounding Box

This operation performs precise computation of bounding box for the selected geometrical object and displays its dimensions.

![measures5.png](https://docs.salome-platform.org/latest/gui/GEOM/measures5.png)

The coordinates of two corners of its bounding box are shown in the table.

Press **Apply** or **Apply and Close** button to publish the bounding **Box** in the study.

Note
:   This dialog supports navigation through the selectable objects (in OCC 3D viewer only):

    - Scroll mouse wheel with pressed *Ctrl* key or press *"S"*, *"P"* keys when input focus is in the viewer to navigate between selectable objects.
    - Press left mouse button to select an appropriate object to the dialog box.

    For more details, please refer to the *"Functionality common for OCC and VTK viewers"* chapter of the GUI module's documentation.

**TUI Commands:** *[Xmin,Xmax, Ymin,Ymax, Zmin,Zmax] = geompy.BoundingBox(Shape, precise)*, *BBox = geompy.MakeBoundingBox(Shape, precise)*, where *Shape* is the shape for which the bounding box is computed. *precise* TRUE for precise computation; FALSE for fast one. Default value is False.

See also a [TUI example](tui_bounding_box_page.md).
