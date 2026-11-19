<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_smoothingsurface_page.html -->

# Smoothing Surface

To create a  **Smoothing Surface** in the **Main Menu** select **New Entity - > Advanced - > SmoothingSurface**

![smoothingsurface_dlg.png](https://docs.salome-platform.org/latest/gui/GEOM/smoothingsurface_dlg.png)

In this dialog you can specify the following parameters:

- **Name** of the surface;
- the list of **Points** or compounds of points, from which it is approximated;
- **Max nbr of Bezier pieces** in the resulting surface;
- **Max BSpline surface degree** of the resulting BSpline surface;
- **3D tolerance of initial approximation**

Note
:   **3D tolerance of the initial approximation** represents the tolerance of initial plate surface approximation. If this parameter is equal to 0 (default), its value is automatically computed as  *max(0.0001, 10*error)*, where *error* is the 3D tolerance of the surface representing the maximal distance between the computed plate surface and given points.

**Advanced options:** [Preview](restore_presentation_parameters_page.md#preview_anchor)

Press "Apply" or "Apply & Close" button to get the resulting *GEOM_Object(Surface)*.

**TUI Command:** *geompy.MakeSmoothingSurface(thelPoints, theNbMax, theDegMax, theDMax)*, where:

- *thelPoints* is a list of points or compounds of points;
- *theNbMax* maximum number of Bezier pieces in the resulting surface;
- *theDegMax* maximum degree;   
  - *theDMax* specifies 3D tolerance of the initial approximation.

Example:

![smoothingsurface.png](https://docs.salome-platform.org/latest/gui/GEOM/smoothingsurface.png)

Our **TUI Scripts** provide you with useful examples of creation of [Advanced objects](tui_advanced_geom_objs_page.md#tui_creation_smoothingsurface).
