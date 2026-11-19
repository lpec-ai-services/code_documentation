<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/revolutionFuseFeature.html -->

# Revolution Fuse

Revolution Fuse feature revolves the selected objects around the selected axis and fuses the result with other objects.

To perform Revolution Fuse in the active part:

1. select in the Main Menu *Features - > Revolution Fuse* item or
2. click ![revolution_fuse_btn.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_fuse_btn.png) **Revolution Fuse** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/StartSketch.png)

Start sketch

There are three variants of the property panel for Revolution Fuse depending on the chosen option:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_by_angles.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_by_angles.png)

**By Angles** revolves objects by specifying angles.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_by_bounding_planes.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_by_bounding_planes.png)

**By Bounding Planes** revolves objects by specifying bounding planes and angles.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_through_all.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_through_all.png)

**Through All** revolves objects by 360 degrees.

---

## By angles

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/RevolutionFuse1.png)

Revolution Fuse: definition by angles

- **Base objects** - contains a list of objects selected in the Object Browser or in the Viewer, which will be revolved.
- **Axis** - axis of revolution.
- **To angle** - end angle of revolution.
- **From angle**- start angle of revolution.
- **Fuse with** contains a list of objects which will be fused with the result of revolution.

**TUI Command**:

model.addRevolutionFuse(*part*, *objectsToRevolve*, *axis*, *angle*, *objectToFuse*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for revolution.
        - **object** – An axis.
        - **real** – Angle.
        - **list** – A list of objects to fuse with.

    Returns:
    :   Created object.

model.addRevolutionFuse(*part*, *objectsToRevolve*, *axis*, *toAngle*, *fromAngle*, *objectToFuse*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for revolution.
        - **object** – An axis.
        - **real** – To angle.
        - **real** – From angle.
        - **list** – A list of objects to fuse with.

    Returns:
    :   Created object.

### Result

The Result of the operation will be a revolved shape:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_fuse_by_angles_result.png)

**Revolution Fuse created**

**See Also** a sample TUI Script of [Create Revolution Fuse by angles](TUI_revolutionFuseByAngles.md#tui-create-revolution-fuse-by-angles) operation.

## By bounding planes

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/RevolutionFuse2.png)

Revolution Fuse: definition by bounding planes

- **Base objects** - contains a list of objects selected in the Object Browser or in the Viewer, which will be revolved.
- **Axis** - axis of revolution.
- **To plane** - a planar face can be selected to bound revolution from one side.
- **To offset** - offset for revolution or for bounding plane, if selected.
- **From plane** - a planar face can be selected to bound revolution from other side.
- **From offset** - offset for revolution or for bounding plane, if selected.
- **Fuse with** - contains a list of objects which will be fused with the result of revolution.

**TUI Command**:

model.addRevolutionFuse(*part*, *objectsToRevolve*, *axis*, *toObject*, *toOffset*, *fromObject*, *fromOffset*, *objectToFuse*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for revolution.
        - **object** – An axis.
        - **object** – To object.
        - **real** – To offset.
        - **object** – From object.
        - **real** – From offset.
        - **list** – A list of objects to fuse with.

    Returns:
    :   Created object.

### Result

The Result of the operation will be a revolved shape:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_fuse_by_bounding_planes_result.png)

**Revolution Fuse created**

**See Also** a sample TUI Script of [Create Revolution Fuse by bounding planes](TUI_revolutionFuseByBoundingPlanes.md#tui-create-revolution-fuse-by-bounding-planes) operation.

## Through All

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/RevolutionFuse3.png)

Revolution Fuse: definition by bounding planes

- **Base objects** - contains a list of objects selected in the Object Browser or in the Viewer, which will be revolved.
- **Axis** - axis of revolution.
- **Fuse with** - contains a list of objects which will be fused with the result of revolution.

**TUI Command**:

model.addRevolutionFuse(*part*, *objectsToRevolve*, *axis*, *objectToFuse*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for revolution.
        - **object** – An axis.
        - **list** – A list of objects to fuse with.

    Returns:
    :   Created object.

### Result

The Result of the operation will be a revolved shape:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_fuse_through_all_result.png)

**Revolution Fuse created**

**See Also** a sample TUI Script of [Create Revolution Fuse by 360 degrees](TUI_revolutionFuseThroughAll.md#tui-create-revolution-fuse-through-all) operation.
