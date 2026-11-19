<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/transformationFeature.html -->

# Scale

**Scale** feature makes a scaled shape basing on the initial shape.

To create a Scale in the active part:

1. select in the Main Menu *Features - > Scale* item or
2. click ![scale.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/scale.png) **Scale** button in the toolbar

Two Scale algorithms are:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/scale_factor_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/scale_factor_32x32.png)

by one common factor

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/scale_dimensions_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/scale_dimensions_32x32.png)

by different factors along axes

---

## Scale by one common factor

Scale by one common factor scales the entire object without modification the geometry of the shape: dimensions change evenly in all three orthogonal directions.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Scale1.png)

Scale by one common factor property panel

Input fields:

- **Main objects** panel contains shapes to be scaled. Shapes are selected in 3D OCC viewer or object browser; [Transformation of COMPSOLID subshapes is prohibited.](translationFeature.md#transformation-subshapes)
- **Center point** defines the point relatively to which the object is scaled. Point is selected in 3D OCC viewer or object browser;
- **Scale factor** defines the multiplier of axial dimensions. If Scale Factor is negative, the object is mirrored through the Central Point.

**TUI Command**:

model.addScale(*Part_doc*, [*shape*, ]*center*, *factor*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes in format *model.selection(TYPE, shape)*.
        - **object** – A center point in format *model.selection(TYPE, shape)*.
        - **real** – Scale factor.

    Returns:
    :   Result object.

### Result

Result of operation is transformed initial shape shown in wireframe mode together with initial shape in shading mode.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Scale_common_factor.png)

Scale by one common factor

**See Also** a sample TUI Script of [Scale by one common factor](TUI_scalefactorFeature.md#tui-scale-common-factor) operation.

## Scale by different factors along axes

Scale by different factors along axes is a general transformation, which can modify the geometry, for example, a sphere can be transformed into an ellipsoid.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Scale2.png)

Scale: define by different factors property panel

Input fields:

- **Main objects** panel contains shapes to be scaled. Shapes are selected in 3D OCC viewer or object browser; [Transformation of COMPSOLID subshapes is prohibited.](translationFeature.md#transformation-subshapes)
- **Center point** defines the point relatively to which the object is scaled. Point is selected in 3D OCC viewer or object browser;
- **Scale factor in X**, **Scale factor in Y**, **Scale factor in Z** define the the multipliers of axial dimensions. If Scale Factor is negative, the object is mirrored through the Central Point.

**TUI Command**:

model.addScale(*Part_doc*, [*shape*, ]*center*, *factors*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes in format *model.selection(TYPE, shape)*.
        - **object** – A center point in format *model.selection(TYPE, shape)*.
        - **list** – A list of three scale factor values along X. Y, Z axes.

    Returns:
    :   Result object.

### Result

Result of operation is transformed initial shape.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Scale_XYZ.png)

Scale by different factors

**See Also** a sample TUI Script of [Scale by different factors along axes](TUI_scaleXYZFeature.md#tui-scale-xyz) operation.
