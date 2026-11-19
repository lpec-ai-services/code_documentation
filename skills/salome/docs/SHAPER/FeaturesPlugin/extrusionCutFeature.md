<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/extrusionCutFeature.html -->

# Extrusion Cut

Extrusion Cut feature extrudes selected objects along their normals or selected axis and cuts the result from other objects.

To perform Extrusion Cut in the active part:

1. select in the Main Menu *Features - > Extrusion Cut* item or
2. click ![extrusion_cut_btn.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_cut_btn.png) **Extrusion Cut** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/StartSketch.png)

Start sketch

There are three variants of the property panel for Extrusion Cut depending on the chosen option:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_by_sizes.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_by_sizes.png)

**By Sizes** extrudes objects by specifying sizes.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_by_bounding_planes.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_by_bounding_planes.png)

**By Bounding Planes** extrudes objects by specifying bounding planes and offsets.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_through_all.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_through_all.png)

**Through All** extrudes base objects through all objects to be cut.

---

## By sizes

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/ExtrusionCut1.png)

Extrusion Cut: definition by sizes

- **Base objects** - contains a list of objects selected in the Object Browser or in the Viewer, which will be extruded.
- **Axis** - if selected, it will be the direction of extrusion, otherwise objects normals will be used.
- **To size** - size for extrusion in the direction.
- **From size** - size for extrusion in the opposite direction.
- **Cut from** - contains a list of objects to be cut by the result of extrusion.

**TUI Commands**:

model.addExtrusionCut(*part*, *objectsToExtrude*, *size*, *objectsToCut*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **number** – Size of extrucion.
        - **list** – A list of objects to cut from.

    Returns:
    :   Created object.

model.addExtrusionCut(*part*, *objects*, *direction*, *size*, *objectsToCut*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **object** – A direction of extrusion
        - **number** – Size of extrucion.
        - **list** – A list of objects to cut from.

    Returns:
    :   Created object.

model.addExtrusionCut(*part*, *objects*, *toSize*, *fromSize*, *objectsToCut*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **number** – “Size to” value.
        - **number** – “Size from” value.
        - **list** – A list of objects to cut from.

    Returns:
    :   Created object.

model.addExtrusionCut(*part*, *objects*, *direction*, *toSize*, *fromSize*, *objectsToCut*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **object** – A direction of extrusion
        - **number** – “Size to” value.
        - **number** – “Size from” value.
        - **list** – A list of objects to cut from.

    Returns:
    :   Created object.

### Result

The Result of the operation will be an extruded shape:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_cut_by_sizes_result.png)

**Created Extrusion Cut**

**See Also** a sample TUI Script of [Create Extrusion Cut by sizes](TUI_extrusionCutBySizes.md#tui-create-extrusion-cut-by-sizes) operation.

## By bounding planes

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/ExtrusionCut2.png)

Extrusion Cut: definition by bounding planes

- **Base objects** - contains a list of objects selected in the Object Browser or in the Viewer, which will be extruded.
- **Axis** - if selected, it will be the direction of extrusion, otherwise objects normals will be used.
- **To plane** - a planar face can be selected to bound extrusion from one side.
- **To offset** - offset for extrusion or for a bounding plane, if selected.
- **From plane** - a planar face can be selected to bound extrusion from the other side.
- **From offset** - offset for extrusion or for a bounding plane, if selected.
- **Cut from** - contains a list of objects which will be cut by the result of extrusion.

**TUI Commands**:

model.addExtrusionCut(*part*, *objects*, *toObject*, *toOffset*, *fromObject*, *fromOffset*, *objectsToCut*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **object** – “To object”.
        - **number** – “Offset to” value.
        - **object** – “From object”.
        - **number** – “Offset from” value.
        - **list** – A list of objects to cut from.

    Returns:
    :   Created object.

model.addExtrusionCut(*part*, *objects*, *direction*, *toObject*, *toOffset*, *fromObject*, *fromOffset*, *objectsToCut*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **object** – A direction of extrusion
        - **object** – “To object”.
        - **number** – “Offset to” value.
        - **object** – “From object”.
        - **number** – “Offset from” value.
        - **list** – A list of objects to cut from.

    Returns:
    :   Created object.

### Result

The Result of the operation will be an extruded shape:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_cut_by_bounding_planes_result.png)

**Created Extrusion Cut**

**See Also** a sample TUI Script of [Create Extrusion Cut by bounding planes](TUI_extrusionCutByBoundingPlanes.md#tui-create-extrusion-cut-by-bounding-planes) operation.

## Through all

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/ExtrusionCut3.png)

Extrusion Cut: definition through all objects

- **Base objects** - contains a list of objects selected in the Object Browser or in the Viewer, which will be extruded.
- **Axis** - if selected, it will be the direction of extrusion, otherwise objects normals will be used.
- **Cut from** - contains a list of objects to be cut by the result of extrusion.

**TUI Commands**:

model.addExtrusionCut(*part*, *objectsToExtrude*, *objectsToCut*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **list** – A list of objects to cut from.

    Returns:
    :   Created object.

model.addExtrusionCut(*part*, *objects*, *direction*, *objectsToCut*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **object** – A direction of extrusion
        - **list** – A list of objects to cut from.

    Returns:
    :   Created object.

### Result

The Result of the operation will be an extruded shape:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_cut_through_all_result.png)

**Created Extrusion Cut**

**See Also** a sample TUI Script of [Create Extrusion Cut through all objects](TUI_extrusionCutThroughAll.md#tui-create-extrusion-cut-through-all) operation.
