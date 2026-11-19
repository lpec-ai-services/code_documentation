<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/shape_processing_operation_page.html -->

# Shape Processing

To produce a **Shape Processing** operation in the **Main Menu** select **Repair - > Shape Processing**.   
This operation processes one or more shapes using various operators.

The **Result** will be a **[GEOM.GEOM_Object](../GEOM/geompy_doc/interfaceGEOM_1_1GEOM__Object.md)**.

**TUI Command:** *geompy.ProcessShape(Shape, Operators, Parameters, Values),* where *Shape* is a processed shape, *Operators* is a list of operators ("FixShape", "SplitClosedFaces", etc.), *Parameters* is a list of parameters ("FixShape.Tolerance3d", etc), *Values* is a list of values of parameters placed in the same order as in the list of Parameters.

Note
:   **Shape Processing** is useful not only on invalid shapes, but also on the shapes, that are classified as valid by the **Check** functionality. Use it, if an operation (for example, **Partition**) fails. Example of usage:

    1. Try to partition objects obj1 and obj2.
    2. Partition fails.
    3. Perform Shape Processing on objects obj1 and obj2.
    4. Try to partition them again.

    See also [TUI example](tui_repairing_operations_page.md#tui_limit_tolerance).

In this dialog box you can select the object that you need to process, define its name and operators applied to it during processing.

![repair1.png](https://docs.salome-platform.org/latest/gui/GEOM/repair1.png)

**Operators and Parameters** (TUI names are given in brackets):

- **Fix Shape** (FixShape) - corrects invalid shapes.
  - **3D Tolerance** (FixShape.Tolerance3d) - work tolerance for detection of the problems and correction of them.
  - **Max 3D Tolerance** (FixShape.MaxTolerance3d) - maximal possible tolerance of the shape after correction.
- **Fix Face Size** (FixFaceSize) - removes small faces, such as spots and strips.
  - **Tolerance** (FixFaceSize.Tolerance) - defines minimum possible face size.
- **Drop Small Edges** (DropSmallEdges) - removes edges, which merge with neighboring edges.
  - **3D Tolerance** (DropSmallEdges.Tolerance3d) - defines minimum possible distance between two parallel edges.
- **Drop Small Solids** (DropSmallSolids) - removes small solids or merges them with neighboring ones.
  - **Width factor tol.** (DropSmallSolids.WidthFactorThreshold) - defines the maximum value of *2V/S* of a solid, which is considered small, where *V* is the volume and *S* is the surface area of the solid.
  - **Volume tol.** (DropSmallSolids.VolumeThreshold) - defines the maximum volume of a solid, which is considered small.
  - **To merge solids** (DropSmallSolids.MergeSolids) - if activated, small solids are removed, else small solids are merged to adjacent non-small solids or left untouched if they cannot be merged.If the both tolerances are activated a solid is considered small if it meets both criteria.
- **Split Angle** (SplitAngle) - splits faces based on conical surfaces, surfaces of revolution and cylindrical surfaces in segments using a certain angle.
  - **Angle** (SplitAngle.Angle) - the central angle of the resulting segments (i.e. we obtain two segments if Angle=180, four if Angle=90, etc).
  - **Max. Tolerance** (SplitAngle.MaxTolerance) - maximum possible tolerance among the resulting segments.
- **Split Closed Faces** (SplitClosedFaces) - splits closed faces in segments. The number of segments depends on the number of splitting points.
  - **Number of splitting points** (SplitClosedFaces.NbSplitPoints) - the number of splitting points.
- **Split Continuity** (SplitContinuity) - splits shapes to reduce continuities of curves and surfaces.
  - **3D Tolerance** (SplitContinuity.Tolerance3d) - 3D tolerance for correction of geometry.
  - **Surface Continuity** (SplitContinuity.SurfaceContinuity) - required continuity for surfaces.
  - **Curve Continuity** (SplitContinuity.CurveContinuity) - required continuity for curves.  
  This and the previous parameters can take the following values:

  :   **Parametric Continuity**   
      **C0** (Positional Continuity): curves are joined (the end positions of curves or surfaces are coincidental. The curves or surfaces may still meet at an angle, giving rise to a sharp corner or edge).   
      **C1** (Tangential Continuity): first derivatives are equal (the end vectors of curves or surfaces are parallel, ruling out sharp edges).   
      **C2** (Curvature Continuity): first and second derivatives are equal (the end vectors of curves or surfaces are of the same magnitude).   
      **CN** N-th derivatives are equal (both the direction and the magnitude of the Nth derivatives of curves or surfaces (d/du C(u)) are the same at junction.

  :   **Geometric Continuity**   
      **G1:** first derivatives are proportional at junction.   
      The curve tangents thus have the same direction, but not necessarily the same magnitude. i.e., C1'(1) = (a,b,c) and C2'(0) = (k*a, k*b, k*c).   
      **G2:** first and second derivatives are proportional at junction.   
      As the names imply, geometric continuity requires the geometry to be continuous, while parametric continuity requires that the underlying parameterization was continuous as well.   
      Parametric continuity of order n implies geometric continuity of order n, but not vice-versa.
- **Bspline Restriction** (BsplineRestriction) - converts curves and surfaces to Bsplines and processes them with the following parameters:
  - **Surface Mode** (BSplineRestriction.SurfaceMode) - approximation of surfaces if restriction is necessary.
  - **3D Curve Mode** (BSplineRestriction.Curve3dMode) - conversion of any 3D curve to BSpline and approximation.
  - **2D Curve Mode** (BSplineRestriction.Curve2dMode) - conversion of any 2D curve to BSpline and approximation.
  - **3D Tolerance** (BSplineRestriction.Tolerance3d) - defines the possibility of surfaces and 3D curves approximation with the specified parameters.
  - **2D Tolerance** (BSplineRestriction.Tolerance2d) - defines the possibility of surfaces and 2D curves approximation with the specified parameters.
  - **Required Degree** (BSplineRestriction.RequiredDegree) - required degree of the resulting BSplines.
  - **Required number of segments** (BSplineRestriction.RequiredNbSegments) - required maximum number of segments of resultant BSplines.
  - **3D Continuity** (BSplineRestriction.Continuity3d) - continuity of the resulting surfaces and 3D curves.
  - **2D Continuity** (BSplineRestriction.Continuity2d) - continuity of the resulting 2D curves.
- **To Bezier** (ToBezier) - converts curves and surfaces of any type to Bezier curves and surfaces.
  - **Surface Mode** (ToBezier.SurfaceMode) - if checked in, allows conversion of surfaces.
  - **3D Curve Mode** (ToBezier.Curve3dMode) - if checked in, allows conversion of 3D curves.
  - **2D Curve Mode** (ToBezier.Curve2dMode) - if checked in, allows conversion of 2D curves.
  - **Max Tolerance** (ToBezier.MaxTolerance) - defines tolerance for detection and correction of problems.
- **Same Parameter** (SameParameter) - fixes edges of 2D and 3D curves not having the same parameter.
  - **3D Tolerance** (SameParameter.Tolerance3d) - defines tolerance for fixing of edges.

**Example:**

![image154.png](https://docs.salome-platform.org/latest/gui/GEOM/image154.png)

*Shape before applying Shape Processing (FixShape operator). View # 1.*

![image156.png](https://docs.salome-platform.org/latest/gui/GEOM/image156.png)

*Shape before applying Shape Processing (FixShape operator). View # 2.*

![image160.png](https://docs.salome-platform.org/latest/gui/GEOM/image160.png)

*The same shape after applying Shape Processing.*

Our **TUI Scripts** provide you with useful examples of the use of [Repairing Operations](tui_repairing_operations_page.md#tui_shape_processing).
