<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/linearCopyFeature.html -->

# Linear copy

**Linear copy** feature makes several translations of a selected shape in one or two directions.

To create a Linear copy in the active part:

1. select in the Main Menu *Part - > Linear copy* item or
2. click ![multitranslation.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/multitranslation.png) **Linear copy** button in the toolbar

The following property panel appears.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/LinearCopy.png)

Linear copy property panel

Input fields:

- **Main objects** panel contains shapes to be translated. Shapes are selected in 3D OCC viewer or object browser; [Transformation of COMPSOLID subshapes is prohibited.](translationFeature.md#transformation-subshapes)
- **First direction** defines translation in the first direction:

  - **Vector of translation** defines vector along which the object will be translated. Vector is edge, axis selected in 3D OCC viewer or object browser;
  - **Step** defines the distance between the shape copies;
  - **Nb. Copies** is the number of shape copies;
- **Second direction** check-box turns on/off translation in the second direction:

  - **Vector of translation** defines vector along which the object will be translated. Vector is edge, axis selected in 3D OCC viewer or object browser;
  - **Step** defines the distance between the shape copies;
  - **Nb. Copies** defines the number of shape copies.

**TUI Command**:

model.addMultiTranslation(*Part_doc*, [*shape*, ]*axis1*, *step1*, *Nb1*, *axis2*, *step2*, *Nb2*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes in format *model.selection(TYPE, shape)*.
        - **object** – A first axis in format *model.selection(TYPE, shape)*.
        - **real** – The first step value.
        - **integer** – The first number of copies.
        - **object** – A second axis in format *model.selection(TYPE, shape)*.
        - **real** – The second step value.
        - **integer** – The second number of copies.

    Returns:
    :   Created object.

## Result

Result of operation is a compound.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/linearcopyres.png)

Linear copy

**See Also** a sample TUI Script of [Create Linear copy](TUI_linearcopyFeature.md#tui-create-linearcopy) operation.
