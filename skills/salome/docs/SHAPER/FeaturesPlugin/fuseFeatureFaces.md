<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/fuseFeatureFaces.html -->

# Fuse Faces

**Fuse Faces** feature eliminates the edges between adjacent same-domain faces lying on the same geometrical surface. This feature is useful for processing the results of **Fuse**, **Union** or **Partition** operations.

To perform **Fuse Faces** in the active part:

1. select in the Main Menu *Features - > Fuse Faces* item or
2. click ![fusion_faces.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/fusion_faces.png) **Fuse Faces** button in the toolbar

The following property panel appears:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/FuseFaces.png)

**Fuse Faces** property panel

Input fields:

- **Shape** - contains object selected in the Object Browser or in the Viewer, on which faces will be fused.

**TUI Command**:

model.addFusionFaces(*Part_doc*, *shape*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A shape in format *model.selection(TYPE, shape)*.

    Returns:
    :   Created object.

## Result

The Result of the operation will be a shape with eliminated edges:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreatedFuseFaces.png)

Shape before and after operation **Fuse Faces**

**See Also** a sample TUI Script of [Fuse Faces](TUI_fusefacesFeature.md#tui-create-fuse-faces) operation.
