<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/PrimitivesPlugin/boxFeature.html -->

# Box

Box feature creates a box solid.

To create a Box in the active part:

1. select in the Main Menu *Primitives - > Box* item or
2. click ![Box_button.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Box_button.png) **Box** button in the toolbar:

There are 3 algorithms for creation of a Box:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/box_dxyz_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/box_dxyz_32x32.png)

**By dimensions**

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/box_2pt_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/box_2pt_32x32.png)

**By two points**

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/box_pt_dxyz_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/box_pt_dxyz_32x32.png)

**By coordinates of a point and dimensions**

---

## By dimensions

Box is created by dimensions along X, Y, Z axis starting from the origin.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Box_dimensions.png)

Input fields:

- **DX**, **DY**, **DZ** define dimensions of the box along the corresponding coordinate axes.

**TUI Command**:

model.addBox(*Part_doc*, *DX*, *DY*, *DZ*)
:   Parameters:
    :   - **part** – The current part object.
        - **real** – Size along X.
        - **real** – Size along Y.
        - **real** – Size along Z.

    Returns:
    :   Result object.

### Result

A solid box based on the origin of coordinates and with edges parallel to the coordinate axes.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Box1.png)

**See Also** a sample TUI Script of a [Create Box by dimensions](TUI_boxDimensions.md#tui-create-boxdim) operation.

## By two points

Box is created by two points of the box diagonal.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Box_2points.png)

Input fields:

- **Point 1** and **Point 2** define diagonal points of the box selected in 3D OCC viewer or object browser.

**TUI Command**:

model.addBox(*Part_doc*, *point1*, *point2*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – First vertex of diagonal.
        - **object** – Second vertex of diagonal.

    Returns:
    :   Result object.

### Result

A solid box based on two points and with edges parallel to the coordinate axes.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Box2.png)

Created boxes

**See Also** a sample TUI Script of [Create Box by points](TUI_boxByPoints.md#tui-create-boxpnt) operation.

## By coordinates of a point and dimensions

Box is created by dimensions along X, Y, Z axis starting from the point of coordinates (x,y,z).

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Box_ptAndDims.png)

Input fields:

- **OX**, **OY**, **OZ** define coordinates of the center of box.
- **DX**, **DY**, **DZ** define dimensions (hafl length) of the box along the corresponding coordinate axes.

**TUI Command**:

model.addBox(*Part_doc*, *OX*, *OY*, *OZ*, *DX*, *DY*, *DZ*)
:   Parameters:
    :   - **part** – The current part object.
        - **real** – X coordinate of the center point
        - **real** – Y coordinate of the center point
        - **real** – Z coordinate of the center point
        - **real** – Half size along X.
        - **real** – Half size along Y.
        - **real** – Half size along Z.

    Returns:
    :   Result object.

### Result

A solid box whose point coordinates are the center and the dimensions are half lengths on one side and the other on the axes relative to the center.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Box3.png)

Created boxes

**See Also** a sample TUI Script of [Create Box coordinates of a point and dimensions](TUI_boxByPtDims.md#tui-create-boxptdim) operation.
