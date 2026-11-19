<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_filling_page.html -->

# Filling Surface with Edges

To generate a **Filling** in the **Main Menu** select **New Entity - > Generation - > Filling**

To create a curvilinear face from several edges you need to define the following parameters:   
**Input Contours** - the list of edges/wires to use for creation of the surface. You can select either several edges/wires or a compound of them. To prepare for the filling, each input wire is converted into a single BSpline curve by concatenating its edges. List of edges/wires must contain more than one edge.   
**Minimum** and **Maximum Degree** of equation of the resulting BSpline or Besier curves describing the surface.   
**Tolerance** for **2D** and for **3D** - minimum distance between the created surface and the input contours.   
**Number of Iterations** - defines the maximum number of iterations. The iterations are repeated until the required tolerance is reached. So, a greater number of iterations allows producing a better surface.   
**Method** - Kind of method to perform filling operation

1. Default - the standard behaviour.
2. Use edges orientation - the edges orientation is used: if an edge is reversed, the curve from this edge is reversed before being used by the filling algorithm.
3. Auto-correct edges orientation - curves orientation is changed to minimize the sum of distances between ends points of edges.

**Approximation** - if checked, BSpline curves are generated in the process of surface construction (using GeomAPI_PointsToBSplineSurface functionality). By default the surface is created using Besier curves. The usage of **Approximation** slows the algorithm, but allows building the surface for complex cases.

The **Result** of the operation will be a GEOM_Object (face).

**TUI Command:** *geompy.MakeFilling(Contours, MinDegree, MaxDegree, Tol2D, Tol3D, NbIter)*  
**Arguments:** List/compound of edges/wires + 7 Parameters (Min. degree, Max. degree, 2D tolerance, 3D tolerance, Number of iterations, Method, Approximation).   
**Advanced options:** [Preview](restore_presentation_parameters_page.md#preview_anchor)

![filling.png](https://docs.salome-platform.org/latest/gui/GEOM/filling.png)

Note
:   This dialog supports navigation through the selectable objects (in OCC 3D viewer only):

    - Scroll mouse wheel with pressed *Ctrl* key or press *"S"*, *"P"* keys when input focus is in the viewer to navigate between selectable objects.
    - Press left mouse button to select an appropriate object to the dialog box.

    For more details, please refer to the *"Functionality common for OCC and VTK viewers"* chapter of the GUI module's documentation.

**Example:**

![filling_compoundsn.png](https://docs.salome-platform.org/latest/gui/GEOM/filling_compoundsn.png)

Initial edges

![fillingsn.png](https://docs.salome-platform.org/latest/gui/GEOM/fillingsn.png)

Resulting surface

Sample **TUI Scripts** provide you with useful examples of creation of [Complex Geometric Objects](tui_complex_objs_page.md#tui_creation_filling).
