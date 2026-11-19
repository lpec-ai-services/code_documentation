<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/placementFeature.html -->

# Placement

Placement defines position of an object relatively to another object. To make a placement:

1. select in the Main Menu *Part - > Placement* item or
2. click ![placement_btn.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/placement_btn.png) **Placement** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Placement.png)

**Placement operation**

In this property panel, it is necessary to:

- Select objects which will be moved; [Transformation of COMPSOLID subshapes is prohibited.](translationFeature.md#transformation-subshapes)
- Select a face, edge or vertex as a start for moving;
- Select a face, edge or vertex as an end of moving;
- Define state of **Reverse** and **Centering** check boxes.

**Apply** button creates the placement.

**Cancel** button cancels the operation.

**TUI Command**:

model.addPlacement(*Part_doc*, *placeObjects*, *startShape*, *endShape*, *isReverse*, *isCentering*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects to move.
        - **object** – A start shape.
        - **object** – A end shape.
        - **bool** – Is reverse flag.
        - **bool** – Is centering flag.

    Returns:
    :   Created object.

## Result

The Result of the operation will be a new placement of selected objects:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedPlacement.png)

**Placement created**

**See Also** a sample TUI Script of [Create Placement](TUI_placementFeature.md#tui-create-placement) operation.
