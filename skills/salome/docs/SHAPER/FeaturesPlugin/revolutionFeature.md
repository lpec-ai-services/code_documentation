<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/revolutionFeature.html -->

# Revolution

Revolution feature revolves selected objects around selected axis.

To perform a Revolution in the active part:

1. select in the Main Menu *Features - > Revolution* item or
2. click ![revolution_btn.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_btn.png) **Revolution** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/StartSketch.png)

Start sketch

There are two variants of the property panel for Revolution depending on the chosen option:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_by_angles.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_by_angles.png)

**By Angles** revolves objects by specifying angles.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_by_bounding_planes.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_by_bounding_planes.png)

**By Bounding Planes** revolves objects by specifying bounding planes and angles.

---

## By angles

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Revolution1.png)

Revolution: definition by angles

- **Base objects** - contains a list of objects selected in the Object Browser or in the Viewer, which will be revolved.
- **Axis** - axis of revolution.
- **To angle** - end angle of revolution.
- **From angle** - start angle of revolution.

**TUI Commands**:

model.addRevolution(*part*, *objects*, *axis*, *angle*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for revolution.
        - **object** – An axis.
        - **real** – An angle.

    Returns:
    :   Created object.

model.addRevolution(*part*, *objects*, *axis*, *toSize*, *fromSize*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for revolution.
        - **object** – An axis.
        - **real** – To angle.
        - **real** – From angle.

    Returns:
    :   Created object.

### Result

The Result of the operation will be a revolved shape:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_by_angles_result.png)

**Revolution created**

**See Also** a sample TUI Script of [Create Revolution by angles](TUI_revolutionByAngles.md#tui-create-revolution-by-angles) operation.

## By bounding planes

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Revolution2.png)

Revolution: definition by bounding planes

- **Base objects** - contains a list of objects selected in the Object Browser or in the Viewer, which will be revolved.
- **Axis** - axis of revolution.
- **To plane** - a planar face can be selected to bound revolution from one side.
- **To offset** - offset for revolution or for bounding plane, if selected.
- **From plane** - a planar face can be selected to bound revolution from other side.
- **From offset** - offset for revolution or for bounding plane, if selected.

**TUI Command**:

model.addRevolution(*part*, *objects*, *axis*, *toObject*, *toOffset*, *fromObject*, *fromOffset*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for revolution.
        - **object** – An axis.
        - **object** – To object.
        - **real** – To offset.
        - **object** – From object.
        - **real** – From offset.

    Returns:
    :   Created object.

### Result

The Result of the operation will be a revolved shape:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/revolution_by_bounding_planes_result.png)

**Revolution created**

**See Also** a sample TUI Script of [Create Revolution by bounding planes](TUI_revolutionByBoundingPlanes.md#tui-create-revolution-by-bounding-planes) operation.
