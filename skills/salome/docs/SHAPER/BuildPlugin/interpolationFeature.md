<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/interpolationFeature.html -->

# Interpolation

Interpolation feature creates an interpolated curve (edge) based on existing points/vertices or based on analytical mathematical expression.

To create an interpolation in the active part:

1. select in the Main Menu *Build - > Interpolation* item or
2. click ![feature_interpolation.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/feature_interpolation.png) **Interpolation** button in the toolbar

There are two creation modes of an interpolation:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/feature_interpolation_by_selection.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/feature_interpolation_by_selection.png)

Interpolation by selection

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/feature_interpolation_analytical.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/feature_interpolation_analytical.png)

Interpolation analytical

## Interpolation by selection

The property panel is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Interpolation.png)

Create an interpolation by selection

Select one or several vertices or points in the viewer.

- **Closed** makes the interpolation curve closed.
- **Reorder** reorders the selected points to minimize the length of curve.
- **Tangents** makes start and end of the curve tangent to the selected edges. The user has to select start and end edges in the corresponding fields.

**Apply** button creates an interpolation.

**Cancel** button cancels the operation.

**TUI Commands**:

model.addInterpolation(*Part_doc*, *Points*, *IsClosed*, *IsReordered*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of points.
        - **boolean** – Is closed.
        - **boolean** – Is reordered.

    Returns:
    :   Result object.

model.addInterpolation(*Part_doc*, *Points*, *StartEdge*, *EndEdge*, *IsClosed*, *IsReordered*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of points.
        - **object** – Start point.
        - **object** – End point.
        - **boolean** – Is closed.
        - **boolean** – Is reordered.

    Returns:
    :   Result object.

## Result

The result of the operation will be a curve created from the selected shapes:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreateInterpolation.png)

Result of the operation.

**See Also** a sample TUI Script of [Create Interpolation by selection](TUI_interpolationBySelection.md#tui-create-interpolation-by-selection) operation.

## Interpolation analytical

The property panel is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/InterpolationAnalytical.png)

Create an interpolation analytical

- **Curves parameters** panel allows to define the mathematical expression for creating the interpolated curve.
  :   - **X(t) equation** define the expression of X with t variable.
      - **Y(t) equation** define the expression of Y with t variable.
      - **Z(t) equation** define the expression of Z with t variable.
- **Min t** define the minimum of t.
- **Max t** define the maximum of t.
- **Number of steps** define the number of steps.

**Apply** button creates an interpolation.

**Cancel** button cancels the operation.

**TUI Commands**:

model.addInterpolation(*Part_doc*, *xt*, *yt*, *zt*, *mint*, *maxt*, *nbSteps*)
:   Parameters:
    :   - **part** – The current part object.
        - **string** – Expression of x.
        - **string** – Expression of y.
        - **string** – Expression of z.
        - **number** – Minimum value of t.
        - **number** – Maximum value of t.
        - **number** – Number of steps.

    Returns:
    :   Result object.

## Result

The result of the operation will be a curve created from analytical expressions for x,y and z as functions of variable t:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreateInterpolationAnalytical.png)

Result of the operation.

**See Also** a sample TUI Script of [Create Interpolation analytical](TUI_interpolationAnalytical.md#tui-create-interpolation-analytical) operation.
