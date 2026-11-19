<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/edgeFeature.html -->

# Edge

Edge feature creates one or several edges using shapes already existing in other objects.

To create edges in the active part:

1. select in the Main Menu *Build - > Edge* item or
2. click ![feature_edge.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/feature_edge.png) **Edge** button in the toolbar

The options to create edges:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/edge_by_segments_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/edge_by_segments_32x32.png)

**By edges** creates edges using already existing edges in other shapes or full sketches.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/edge_by_points_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/edge_by_points_32x32.png)

**By points** creates segment between two points.

---

## By edges

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Edge.png)

Create by edges

Select one or several edges in the viewer. Also, the full sketch can be selected. In this case, all edges of the sketch will be processed.
Checkbox **Compute intersections** forces to split sketch edges in the points of intersection.

**Apply** button creates edges.

**Cancel** button cancels the operation.

**TUI Command**:

model.addEdge(*Part_doc*, *Shapes*, *Intersect*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes.
        - **bool** – Split edges by intersection points. False by default.

    Returns:
    :   Result object.

### Result

The result of the operation will be a set of edges created from the selected shapes:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreateEdge.png)

Result of the operation.

**See Also** a sample TUI Script of [Create Edge](TUI_edgeFeature.md#tui-create-edge) operation.

## By two points

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/EdgeByTwoPoints.png)

Create by points

Select two points in the viewer.

**Apply** button creates a segment.

**Cancel** button cancels the operation.

**TUI Command**:

model.addEdge(*Part_doc*, *Point_1*, *Point_2*)
:   Parameters:
    :   - **part** – The current part object.
        - **object** – First point.
        - **object** – Second point.

    Returns:
    :   Result object.

### Result

The result of the operation will be a segment bounded by selected points:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreateEdgeByPoints.png)

Result of the operation.

**See Also** a sample TUI Script of [Create Edge by Points](TUI_edgeSegmentFeature.md#tui-create-segment) operation.
