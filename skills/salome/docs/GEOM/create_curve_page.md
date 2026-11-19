<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/create_curve_page.html -->

# Curve

To create a **Curve** in the **Main Menu** select **New Entity - > Basic - > Curve**

There are three **Curve Construction** menu choices corresponding to three possible types of curves: Polyline, Besier or B-spline (Interpolated). The curve is defined by a list of **Points** through which it passes.

There are two ways to define these **Points**:

- **By Selection** manual picking of the points in the Object Browser or 3D Viewer.
- **Analytical** parametric definition of the points through python expressions.

The **Result** of each operation will be a GEOM_Object (edge).

**Polyline**

![polyline.png](https://docs.salome-platform.org/latest/gui/GEOM/polyline.png)

Polyline or polygonal chain is a connected series of line segments. It can be defined by the following parameters:

![curve2.png](https://docs.salome-platform.org/latest/gui/GEOM/curve2.png)

- **Points** at least 2 points which will serve as nodes on the curve.
- **Build a closed wire** checkbox allows creating the curve as closed wire.

**TUI Command:** *geompy.MakePolyline(ListOfShapes,isClosed)*

**Bezier**

![bezier.png](https://docs.salome-platform.org/latest/gui/GEOM/bezier.png)

Bezier curve is a curve completely contained in a convex hull of its control points. It can be defined by the following parameters:

![curve3.png](https://docs.salome-platform.org/latest/gui/GEOM/curve3.png)

- **Points** at least 2 points used to approximate the curve.
- **Build a closed edge** checkbox allows creating the curve as closed edge.

**TUI Command:** *geompy.MakeBezier(ListOfShapes,isClosed)*

**B-spline**

![interpol.png](https://docs.salome-platform.org/latest/gui/GEOM/interpol.png)

B-spline is a union of curve segments defined at each node span. It can be defined by the following parameters:

![curve4.png](https://docs.salome-platform.org/latest/gui/GEOM/curve4.png)

- **Points** at least 2 points which will serve as nodes on the curve.
- **Build a closed edge** checkbox allows creating the curve as closed edge.
- If **Reorder vertices taking into account distances** is checked, the interpolation algorithm does not follow the order of vertices but searches for the closest vertex.
- **Tangents** are two vectors, defining the direction at the ends of the curve. It is necessary to set both vectors or none. This option is available only if both above check boxes are not checked.

**TUI Command:**   
*geompy.MakeInterpol(ListOfShapes,isClosed,doReordering)*   
*geompy.MakeInterpolWithTangents(ListOfShapes,Vector1,Vector2)*

**Analytical Definition**

The input parameters for analytical definition are common for all types of curves.

![curve1.png](https://docs.salome-platform.org/latest/gui/GEOM/curve1.png)

- **X(t)equation, Y(t)equation, Z(t)equation** are python expressions for X, Y and Z coordinates of the basic points of the curve.
- **Min t, Max t** are minimum and maximum values of the parameter **t**.
- **Step** is the number of steps of the parameter **t**.

**TUI Command:** *geompy.MakeCurveParametric(XExpr, YExpt, ZExpt, tMin, tMax, nbSteps, curveType, True)*

**Advanced options** [Preview](restore_presentation_parameters_page.md#preview_anchor)

Our **TUI Scripts** provide you with useful examples of creation of [Basic Geometric Objects](tui_basic_geom_objs_page.md#tui_creation_curve).
