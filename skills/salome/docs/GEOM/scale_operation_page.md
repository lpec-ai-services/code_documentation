<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/scale_operation_page.html -->

# Scale Transform

To produce a **Scale Transform** in the **Main Menu** select **Operations - > Transformation - > Scale Transform**

This operation creates a scaled shape basing on the initial shape.

**Simple scale** scales the entire object (i.e. its dimensions change evenly in all three orthogonal directions). It does not modify the geometry of the shape.

![transformation10.png](https://docs.salome-platform.org/latest/gui/GEOM/transformation10.png)

The following parameters and options can be defined in this dialog:

- **Result Name**;
- One or several  **Objects**  to be scaled;
- **Central Point** (optional) - relatively to which the object is scaled. If the **Central Point** is not defined, the scaling will be performed relatively the origin of the global coordinate system.
- **Scale Factor** - the multiplier of axial dimensions. If **Scale Factor** is negative, the object is mirrored through the **Central Point**.
- [Advanced options](restore_presentation_parameters_page.md).

**TUI Command:** *geompy.MakeScaleTransform(Shape, CenterOfScale, Factor)*   
**Arguments:** Name + 1 shape(s) + 1 vertex + 1 Scale Factor.

**Multiple scale** allows scaling by different factors along axes. This is a general transformation, which can modify the geometry, for example, a circle can be transformed into an ellipse.

![transformation10a.png](https://docs.salome-platform.org/latest/gui/GEOM/transformation10a.png)

The following parameters and options can be defined in this dialog:

- **Result Name**;
- One or several  **Objects**  to be scaled;
- **Central Point** (optional) - relatively to which the object is scaled.
- **Scale Factor X/Y/Z** - the multipliers of axial dimensions.   
  - [Advanced options](restore_presentation_parameters_page.md).

**TUI Command:** *geompy.MakeScaleAlongAxes(Shape, CenterOfScale, FactorX, FactorY, FactorZ)*   
**Arguments:** Name + 1 shape(s) + 1 vertex + 3 Scale Factors.

**Example of simple scaling:**

![scale_transformsn1.png](https://docs.salome-platform.org/latest/gui/GEOM/scale_transformsn1.png)

The initial object

![scale_transformsn2.png](https://docs.salome-platform.org/latest/gui/GEOM/scale_transformsn2.png)

The resulting object (resized)

**Example of scaling by different factors along axes:**

![scale_transformsn3.png](https://docs.salome-platform.org/latest/gui/GEOM/scale_transformsn3.png)

The initial object

![scale_transformsn4.png](https://docs.salome-platform.org/latest/gui/GEOM/scale_transformsn4.png)

The resulting object (resized and distorted)

Our **TUI Scripts** provide you with useful examples of the use of [Scale Transformation](tui_transformation_operations_page.md#tui_scale) and of [Scale Along Axes Transformation](tui_test_all_page.md#swig_scale)
