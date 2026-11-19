<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/angularCopyFeature.html -->

# Angular copy

The feature **Angular copy** makes a compound of several rotated shapes basing on the initial shape.

To create an Angular copy in the active part:

1. select in the Main Menu *Part - > Angular copy* item or
2. click ![multirotation.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/multirotation.png) **Angular copy** button in the toolbar

The following property panel appears.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/angularcopy.png)

Angular copy property panel

Input fields:

- **Main objects** panel contains shapes to be rotated. The shapes are selected in 3D OCC viewer or object browser; [Transformation of COMPSOLID subshapes is prohibited.](translationFeature.md#transformation-subshapes)
- **Vector of rotation** defines the axis of rotation. The vector of rotation is an edge, axis selected in 3D OCC viewer or object browser;
- **Angular Step** check-box turns on/off definition of the angle by which the object is rotated. By default (if the checkbox is not checked), **Angular Step** = 2 * PI / NbTimes;
- **Nb. Copies** defines the number of rotated shape copies in the resulting compound. If **Nb. Copies** = 1, the result contains only the initial shape.

**TUI Command**:

model.addMultiRotation(Part_doc, [shape], axis, step, Nb)*
:   Parameters:
    :   - **part** – The current part object
        - **list** – A list of shapes in format *model.selection(TYPE, shape)*
        - **object** – An axis in format *model.selection(TYPE, shape)*
        - **real** – a step value
        - **integer** – A number of copies

    Returns:
    :   Created object

## Result

Result of cylinder rotation is a compound.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/angularcopycyl.png)

Angular copy

**See Also** a sample TUI Script of [Create Angular copy](TUI_angularcopyFeature.md#tui-create-angularcopy) operation.
