<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/BuildPlugin/vertexFeature.html -->

# Vertex

Vertex feature creates one or several vertices using vertices already existing in other objects.

To create vertices in the active part:

1. select in the Main Menu *Build - > Vertex* item or
2. click ![feature_vertex.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/feature_vertex.png) **Vertex** button in the toolbar

The following property panel will be opened:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Vertex.png)

Create vertices

Select one or several vertices in the viewer. It is also possible to select a whole sketch result or feature in the object browser, then all start and end points of the sketch segments will be added into result. Checkbox **Compute intersections** forces to include intersection vertices of edges of the selected sketch.

**Apply** button creates vertices.

**Cancel** button cancels operation.

**TUI Command**:

model.addVertex(*Part_doc*, *Shapes*, *Intersect*)
:   Parameters:
    :   - **part** – The current part object.
        - **list** – A list of shapes.
        - **bool** – Intersect edges (applicable for sketch only). False by default.

    Returns:
    :   Result object.

## Result

The result of the operation will be a set of vertices created from the selected shapes:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/CreateVertex.png)

Result of the operation.

**See Also** a sample TUI Script of [Create Vertex](TUI_vertexFeature.md#tui-create-vertex) operation.
