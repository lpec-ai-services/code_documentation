<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/extrusionFuseFeature.html -->

# Extrusion Fuse

Extrusion Fuse feature extrudes selected objects along their normals or the selected axis and fuses the result with other objects.

To perform Extrusion Fuse in the active part:

1. select in the Main Menu *Features - > Extrusion Fuse* item or
2. click ![extrusion_fuse_btn.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_fuse_btn.png) **Extrusion Fuse** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/StartSketch.png)

Start sketch

There are three variants of the property panel for Extrusion Fuse depending on the chosen option:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_by_sizes.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_by_sizes.png)

**By Sizes** extrudes objects by specifying sizes.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_by_bounding_planes.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_by_bounding_planes.png)

**By Bounding Planes** extrudes objects by specifying bounding planes and offsets.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_through_all.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_through_all.png)

**Through All** extrudes base objects to pass through all objects fuse with.

---

## By sizes

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/ExtrusionFuse1.png)

Extrusion Fuse: definition by sizes

- **Base objects** - contains a list of objects selected in the Object Browser or in the Viewer, which will be extruded.
- **Axis** - if selected, it will be the direction of extrusion, otherwise objects normals will be used.
- **To size** - size for extrusion in the direction.
- **From size** - size for extrusion in the opposite direction.
- **Fuse with** - contains a list of objects which will be fused with the result of extrusion.

**TUI Commands**:

model.addExtrusionFuse(*part*, *objectsToExtrude*, *size*, *objectsToFuse*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **number** – Size of extrucion.
        - **list** – A list of objects to fuse with.

    Returns:
    :   Created object.

model.addExtrusionFuse(*part*, *objects*, *direction*, *size*, *objectsToFuse*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **object** – A direction of extrusion
        - **number** – Size of extrucion.
        - **list** – A list of objects to fuse with.

    Returns:
    :   Created object.

model.addExtrusionFuse(*part*, *objects*, *toSize*, *fromSize*, *objectsToFuse*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **number** – “Size to” value.
        - **number** – “Size from” value.
        - **list** – A list of objects to fuse with.

    Returns:
    :   Created object.

model.addExtrusionFuse(*part*, *objects*, *direction*, *toSize*, *fromSize*, *objectsToFuse*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **object** – A direction of extrusion
        - **number** – “Size to” value.
        - **number** – “Size from” value.
        - **list** – A list of objects to fuse with.

    Returns:
    :   Created object.

### Result

The Result of the operation will be an extruded shape:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_fuse_by_sizes_result.png)

**Extrusion Fuse created**

**See Also** a sample TUI Script of [Create Extrusion Fuse by sizes](TUI_extrusionFuseBySizes.md#tui-create-extrusion-fuse-by-sizes) operation.

## By bounding planes

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/ExtrusionFuse2.png)

Extrusion Fuse: definition by bounding planes

- **Base objects** - contains a list of objects selected in the Object Browser or in the Viewer, which will be extruded.
- **Axis** - if selected, it will be the direction of extrusion, otherwise objects normals will be used.
- **To plane** - a planar face can be selected to bound extrusion from one side.
- **To offset** - offset for extrusion or for bounding plane, if selected.
- **From plane** - a planar face can be selected to bound extrusion from the other side.
- **From offset** - offset for extrusion or for bounding plane, if selected.
- **Fuse with** - contains a list of objects which will be fused with the result of extrusion.

**TUI Commands**:

model.addExtrusionFuse(*part*, *objects*, *toObject*, *toOffset*, *fromObject*, *fromOffset*, *objectsToFuse*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **object** – “To object”.
        - **number** – “To offset”.
        - **object** – “From object”.
        - **number** – “From offset”.
        - **list** – A list of objects to fuse with.

    Returns:
    :   Created object.

model.addExtrusionFuse(*part*, *objects*, *direction*, *toObject*, *toOffset*, *fromObject*, *fromOffset*, *objectsToFuse*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **object** – A direction of extrusion
        - **object** – “To object”.
        - **number** – “To offset”.
        - **object** – “From object”.
        - **number** – “From offset”.
        - **list** – A list of objects to fuse with.

    Returns:
    :   Created object.

### Result

The Result of the operation will be an extruded shape:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_fuse_by_bounding_planes_result.png)

**Extrusion Fuse created**

**See Also** a sample TUI Script of [Create Extrusion Fuse by bounding planes](TUI_extrusionFuseByBoundingPlanes.md#tui-create-extrusion-fuse-by-bounding-planes) operation.

## Through all

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/ExtrusionFuse3.png)

Extrusion Fuse: definition through all objects

- **Base objects** - contains a list of objects selected in the Object Browser or in the Viewer, which will be extruded.
- **Axis** - if selected, it will be the direction of extrusion, otherwise objects normals will be used.
- **Fuse with** - contains a list of objects which will be fused with the result of extrusion.

**TUI Commands**:

model.addExtrusionFuse(*part*, *objectsToExtrude*, *objectsToFuse*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **list** – A list of objects to fuse with.

    Returns:
    :   Created object.

model.addExtrusionFuse(*part*, *objectsToExtrude*, *direction*, *objectsToFuse*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of objects for extrusion.
        - **object** – A direction of extrusion
        - **list** – A list of objects to fuse with.

    Returns:
    :   Created object.

### Result

The Result of the operation will be an extruded shape:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/extrusion_fuse_through_all_result.png)

**Extrusion Fuse created**

**See Also** a sample TUI Script of [Create Extrusion Fuse through all objects](TUI_extrusionFuseThroughAll.md#tui-create-extrusion-fuse-through-all) operation.
