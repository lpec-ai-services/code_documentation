<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/intersectionFeature.html -->

# Intersection

The Intersection operation creates an intersection of a 3D edge and the sketch plane.
The result of the intersection is a point.

To create an Intersection in the active Sketch:

1. select in the Main Menu *Sketch - > Intersection* item or
2. click ![intersection.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Intersection.png) **Intersection** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Intersection_panel.png)

Intersection

Input fields:

- **Object** is the 3D edge to intersect with the sketch plane.
- **Include into the sketch result** option defines whether to include the intersection point into the sketch result.

**TUI Commands**:

Sketch_1.addIntersectionPoint(Edge, IncludeIntoResult)*
:   Parameters:
    :   - **object** – An edge.
        - **boolean** – Include into the result flag.

    Returns:
    :   Result object.

Sketch_1.addIntersectionPoint(EdgeName, IncludeIntoResult)*
:   Parameters:
    :   - **object** – An edge name.
        - **boolean** – Include into the result flag.

    Returns:
    :   Result object.

## Result

Created Intersection appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Intersection_res.png)

Created intersection (purple point)

**See Also** a sample TUI Script of [Create Intersection](TUI_intersection.md#tui-create-sketch-intersection) operation.
