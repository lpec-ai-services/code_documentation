<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/symmetryFeature.html -->

# Symmetry

**Symmetry** feature makes a symmetrical copy of the selected shape.

To create a Symmetry in the active part:

1. select in the Main Menu *Part - > Symmetry* item or
2. click ![symmetry.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/symmetry.png) **Symmetry** button in the toolbar

Symmetrical copy of an Object can be mirrored in three different ways:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/symmetry_point_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/symmetry_point_32x32.png)

through a Point of symmetry

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/symmetry_axis_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/symmetry_axis_32x32.png)

through an Axis of symmetry

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/symmetry_plane_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/symmetry_plane_32x32.png)

through a Plane of symmetry

---

## Symmetry through a Point of symmetry

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/symmetryPoint.png)

Symmetry through a Point of symmetry property panel

Input fields:

- **Main objects** panel contains shapes to be translated. Shapes are selected in 3D OCC viewer or object browser; [Transformation of COMPSOLID subshapes is prohibited.](translationFeature.md#transformation-subshapes)
- **Point** defines a point of symmetry selected in 3D OCC viewer or object browser;
- **Create a copy** checkbox preserves/removes the initial object.

**TUI Command**:

model.addSymmetry(*Part_doc*, [*shape*, ]*point*, *copy*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes in format *model.selection(TYPE, shape)*.
        - **object** – A point in format *model.selection(TYPE, shape)*.
        - **boolean** – A flag to create a copy.

    Returns:
    :   Result object.

### Result

The result of operation is a mirrored initial shape with **Create a copy** = *True*.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/symmetryPointres.png)

Symmetry through a Point of symmetry

**See Also** a sample TUI Script of [Symmetry through a Point of symmetry](TUI_symmetrypointFeature.md#tui-symmetry-point) operation.

## Symmetry through an Axis of symmetry

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/symmetryAxis.png)

Symmetry through an Axis of symmetry property panel

Input fields:

- **Main objects** panel contains shapes to be translated. Shapes are selected in 3D OCC viewer or object browser; [Transformation of COMPSOLID subshapes is prohibited.](translationFeature.md#transformation-subshapes)
- **Axis** defines an axis of symmetry selected in 3D OCC viewer or object browser;
- **Create a copy** checkbox preserves/removes the initial object.

**TUI Command**:

model.addSymmetry(*Part_doc*, [*shape*, ]*axis*, *copy*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes in format *model.selection(TYPE, shape)*.
        - **object** – An axis in format *model.selection(TYPE, shape)*.
        - **boolean** – A flag to create a copy.

    Returns:
    :   Result object.

### Result

The result of operation is a mirrored initial shape with **Create a copy** = *False*.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/symmetryAxisres.png)

Symmetry through an Axis of symmetry

**See Also** a sample TUI Script of [Symmetry through an Axis of symmetry](TUI_symmetryaxisFeature.md#tui-symmetry-axis) operation.

## Symmetry through a Plane of symmetry

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/symmetryPlane.png)

Symmetry through a Plane of symmetry property panel

Input fields:

- **Main objects** panel contains shapes to be translated. Shapes are selected in 3D OCC viewer or object browser; [Transformation of COMPSOLID subshapes is prohibited.](translationFeature.md#transformation-subshapes)
- **Plane** defines a plane of symmetry selected in 3D OCC viewer or object browser;
- **Create a copy** checkbox preserves/removes the initial object.

**TUI Command**:

model.addSymmetry(*Part_doc*, [*shape*, ]*plane*, *copy*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes in format *model.selection(TYPE, shape)*.
        - **object** – A plane in format *model.selection(TYPE, shape)*.
        - **boolean** – A flag to create a copy.

    Returns:
    :   Result object.

### Result

The result of operation is a mirrored initial shape with **Create a copy** = *False*.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/symmetryPlaneres.png)

Symmetry through a Plane of symmetry

**See Also** a sample TUI Script of [Symmetry through a Plane of symmetry](TUI_symmetryplaneFeature.md#tui-symmetry-plane) operation.
