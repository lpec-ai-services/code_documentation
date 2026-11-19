<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/FeaturesPlugin/removeExtraEdgesFeature.html -->

# Remove Extra Edges

**Remove Extra Edges** feature eliminates seam and degenerated edges from faces that lie on spherical surfaces. Also it merges adjacent same-domain edges and, optionally, adjacent same-domain faces in the same way as [Fuse Faces](fuseFeatureFaces.md#fuse-faces) .

This feature is useful for processing the results of **Fuse**, **Union** or **Partition** operations.

To perform **Remove Extra Edges** in the active part:

1. select in the Main Menu *Features - > Remove Extra Edges* item or
2. click ![remove_extra_edges.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/remove_extra_edges.png) **Remove Extra Edges** button in the toolbar

The following property panel appears:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/RemoveExtraEdgesPP.png)

**Remove Extra Edges** property panel

Input fields:

- **Shape** - contains object selected in the Object Browser or in the Viewer, on which extra edges will be removed.
- **Unite faces** - check it to merge adjacent same-domain faces.

**TUI Command**:

model.addRemoveExtraEdges(*Part_doc*, *shape*, *doUniteFaces*)
:   Parameters:
    :   - **part** – The current part object.
        - **shape** – A shape in format model.selection(TYPE, shape).
        - **bool** – True to merge faces. False by default.

    Returns:
    :   Created object.

## Result

The Result of the operation will be a shape with some eliminated edges:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/RemoveExtraEdgesResult.png)

Shape before and after operation **Remove Extra Edges**

**See Also** a sample TUI Script of [Remove Extra Edges](TUI_removeExtraEdgesFeature.md#tui-remove-extra-edges) operation.
