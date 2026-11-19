<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/projection_operation_page.html -->

# Projection

To produce a **Projection** in the **Main Menu** select **Operations - > Transformation - > Projection**

This operation makes normal projection of one shape to another.

There are 3 types of projection different by types of operands.

Firstly, you can project **Source vertex, edge or wire** on a given **Target face**.

![projection_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/projection_dlg.png)

Secondly, you can project **Source vertex** on a given **Target wire**.

![projection_dlg1.png](https://docs.salome-platform.org/latest/gui/GEOM/projection_dlg1.png)

Thirdly, you can project **Source vertex** on a given **Target edge**.

![projection_dlg2.png](https://docs.salome-platform.org/latest/gui/GEOM/projection_dlg2.png)

[Advanced options](restore_presentation_parameters_page.md).

Note
:   This dialog supports navigation through the selectable objects (in OCC 3D viewer only):

    - Scroll mouse wheel with pressed *Ctrl* key or press *"S"*, *"P"* keys when input focus is in the viewer to navigate between selectable objects.
    - Press left mouse button to select an appropriate object to the dialog box.

    For more details, please refer to the *"Functionality common for OCC and VTK viewers"* chapter of the GUI module's documentation.

**Example:**

![projection_preview.png](https://docs.salome-platform.org/latest/gui/GEOM/projection_preview.png)

The curve (in red) and its projection on the cylindric surface

**TUI Command:** *geompy.MakeProjection(Source, Target),*   
where *Source* is a shape which has to be projected, *Target* is a shape, on which the *Source* shape will be projected. The *Result* will be a *GEOM_Object*.

Our **TUI Scripts** provide you with useful examples of the use of [Transformation Operations](tui_transformation_operations_page.md#tui_projection).
