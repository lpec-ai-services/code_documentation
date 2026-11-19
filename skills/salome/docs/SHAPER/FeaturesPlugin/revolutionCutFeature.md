<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/revolutionCutFeature.html -->

# Revolution Cut

Revolution Cut feature revolves the selected objects around the selected axis and cuts the result from other objects.

To perform a Revolution Cut in the active part:

1. select in the Main Menu *Features - > Revolution Cut* item or
2. click ![revolution_cut_btn.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_cut_btn.png) **Revolution Cut** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/StartSketch.png)

Start sketch

There are three variants of the property panel for Revolution Cut depending on the chosen option:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_by_angles.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_by_angles.png)

**By Angles** revolves objects by specifying angles.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_by_bounding_planes.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_by_bounding_planes.png)

**By Bounding Planes** revolves objects by specifying bounding planes and angles.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_through_all.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_through_all.png)

**Through All** revolves objects by 360 degrees.

---

## By angles

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/RevolutionCut1.png)

Revolution Cut: definition by angles

- **Base objects** - contains a list of objects selected in the Object Browser or in the Viewer, which will be revolved.
- **Axis** - axis of revolution.
- **To angle** - end angle of revolution.
- **From angle** - start angle of revolution.
- **Cut from** - contains a list of objects which will but cut with the result of revolution.

**TUI Commands**:

model.addRevolutionCut(*part*, *objectsToRevolve*, *axis*, *angle*, *objectToCut*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for revolution.
        - **object** – An axis.
        - **real** – An angle.
        - **list** – A list of objects to cut from.

    Returns:
    :   Created object.

model.addRevolutionCut(*part*, *objectsToRevolve*, *axis*, *toAngle*, *fromAngle*, *objectToCut*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for revolution.
        - **object** – An axis.
        - **real** – To angle.
        - **real** – From angle.
        - **list** – A list of objects to cut from.

    Returns:
    :   Created object.

### Result

The Result of the operation will be a revolved shape:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_cut_by_angles_result.png)

**Revolution Cut created**

**See Also** a sample TUI Script of [Create Revolution Cut by angles](TUI_revolutionCutByAngles.md#tui-create-revolution-cut-by-angles) operation.

## By bounding planes

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/RevolutionCut2.png)

Revolution Cut: definition by bounding planes

- **Base objects** - contains a list of objects selected in the Object Browser or in the Viewer, which will be revolved.
- **Axis** - axis of revolution.
- **To plane** - a planar face can be selected to bound revolution from one side.
- **To offset** - offset for revolution or for bounding plane, if selected.
- **From plane** - a planar face can be selected to bound revolution from the other side.
- **From offset** - offset for revolution or for bounding plane, if selected.
- **Cut from** - contains a list of objects from which the result of revolution will be cut.

**TUI Command**:

model.addRevolutionCut(*part*, *objectsToRevolve*, *axis*, *toObject*, *toOffset*, *fromObject*, *fromOffset*, *objectToCut*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for revolution.
        - **object** – An axis.
        - **object** – To object.
        - **real** – To offset.
        - **object** – From object.
        - **real** – From offset.
        - **list** – A list of objects to cut from.

    Returns:
    :   Created object.

### Result

The Result of the operation will be a revolved shape:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_cut_by_bounding_planes_result.png)

**Revolution Cut created**

**See Also** a sample TUI Script of [Create Revolution Cut by bounding planes](TUI_revolutionCutByBoundingPlanes.md#tui-create-revolution-cut-by-bounding-planes) operation.

## Through all

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/RevolutionCut3.png)

Revolution Cut: revolving through all the space

- **Base objects** - contains a list of objects selected in the Object Browser or in the Viewer, which will be revolved.
- **Axis** - axis of revolution.
- **Cut from** - contains a list of objects which will but cut with the result of revolution.

**TUI Commands**:

model.addRevolutionCut(*part*, *objectsToRevolve*, *axis*, *objectToCut*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for revolution.
        - **object** – An axis.
        - **list** – A list of objects to cut from.

    Returns:
    :   Created object.

### Result

The Result of the operation will be a revolved shape:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_cut_through_all_result.png)

**Revolution Cut created**

**See Also** a sample TUI Script of [Create Revolution Cut by 360 degrees](TUI_revolutionCutThroughAll.md#tui-create-revolution-cut-through-all) operation.
