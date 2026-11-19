<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_surface_from_face_page.html -->

# Surface From Face

To create a **Surface From Face** in the **Main Menu** select **New Entity - > Basic - > Surface From Face**

This function takes a face at input and creates a new **GEOM_Object**, i.e. topological shape by extracting the underlying surface of the source face and limiting it by the **Umin, Umax, Vmin** and **Vmax** parameters of the source face (in the parametric space).   
[Advanced options](restore_presentation_parameters_page.md).

**TUI Command:** *geompy.MakeSurfaceFromFace(theFace)*, where *theFace* the input face.   
**Arguments:** Name + Object (Face).

![surface_from_face1.png](https://docs.salome-platform.org/latest/gui/GEOM/surface_from_face1.png)

Surface From Face

**Example:**

![surface_from_face_example.png](https://docs.salome-platform.org/latest/gui/GEOM/surface_from_face_example.png)

Original Face (white) and Created Surface

Our **TUI Scripts** provide you with useful examples of the use of [Surface From Face](tui_basic_geom_objs_page.md#tui_creation_surface) creation.
