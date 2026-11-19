<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/bsplineFeature.html -->

# B-spline and periodic B-spline

The feature creates a free form spline curve in the current Sketch.

To add a new B-spline to the Sketch:

1. select in the Main Menu *Sketch - > B-spline* item or
2. click ![bspline.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bspline.png) **B-spline** button in the Sketch toolbar.

To add a periodic B-spline to the Sketch:

1. select in the Main Menu *Sketch - > Periodic B-spline* item or
2. click ![bspline_p.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bspline_p.png) **Periodic B-spline** button in the Sketch toolbar.

## Creation of B-spline curve

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bspline_creation_panel.png)

Click in the view to specify the control polygon of B-spline curve. The curve will be shown after the second point is initialized. To stop adding new poles, click **Esc** button or **Apply** the operation.

**TUI Command**:

Sketch_1.addSpline(*degree*, *poles*, *weights*, *knots*, *multiplicities*, *periodic*)
:   Parameters:
    :   - **integer** – degree of B-spline.
        - **array** – list of poles [(x1, y1), (x2, y2), …].
        - **array** – list of weights for corresponding poles.
        - **array** – parametric knots of B-spline curve.
        - **array** – multiplicity of each knot.
        - **boolean** – True mentions that the B-spline curve is periodic.

    Returns:
    :   Result object.

Each parameter is optional.

## Result

Created B-spline curve appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bspline_result.png)

Non-periodic B-spline created

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bspline_periodic_result.png)

Periodic B-spline created

**See Also** a sample TUI Script of [Create Sketch B-spline](TUI_bsplineFeature.md#tui-create-bspline) operation.

## Modification of B-spline curve

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bspline_modification_panel.png)

Modification panel for B-spline curve

The following options are provided to modify the already created B-spline curve:

1. Change weight of each pole.
2. Add new pole.

The new pole is added after the current by pressing on the corresponding ![add_pole.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/bspline_add_pole.png) button. The default weight for the new pole is 1.

**Note:** adding the new pole after the last for non-periodic B-spline will not change the last point of the curve to avoid modification of full sketch.
