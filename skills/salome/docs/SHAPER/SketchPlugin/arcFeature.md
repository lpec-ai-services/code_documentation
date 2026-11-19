<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/arcFeature.html -->

# Arc

Arc feature creates an arc segment in the current Sketch.

To add a new Arc to the Sketch:

1. select in the Main Menu *Sketch - > Arc* item or
2. click ![arc.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/arc.png) **Arc** button in Sketch toolbar:

There are 4 algorithms for creation of an Arc:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/arc_base_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/arc_base_32x32.png)

**By center and two points** creates an arc segment with the given center passing from the start point to the end point on the circle.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/arc_3pt_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/arc_3pt_32x32.png)

**By three points** creates an arc segment passing from the start point to end point through another point on the circle.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/arc_tang_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/arc_tang_32x32.png)

**By tangent point and end point** creates an arc segment with the tangent point and the end point.

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/arc_perp_32x32.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/arc_perp_32x32.png)

**By point on perpendicular line and end point** creates an arc segment perpendicular to a straight line with the start point, connected with boundary of this line, and the end point.

---

## By center and two points

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Arc_panel_base.png)

Click in the view once to set the center point, then move the mouse and click a second time to set the start point
and finally move the mouse and click a third time to set the last passed point.

- When entering a center or start point by selecting either a point or a segment, a Coincident constraint is created.
- When entering an end point by selecting a segment, a Coincident constraint is created.
- When entering an end point, only segments are selectable.

**TUI Command**:

Sketch_1.addArc(*CenterX*, *CenterY*, *StartX*, *StartY*, *EndX*, *EndY*, *Inversed*)
:   Parameters:
    :   - **real** – Center X.
        - **real** – Center Y.
        - **real** – Start X.
        - **real** – Start Y.
        - **real** – End X.
        - **real** – End Y.
        - **boolean** – Is inversed.

    Returns:
    :   Result object.

## By three points

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Arc_panel_3pt.png)

Click in the view once to set the start point, then move the mouse and click a second time to set the end point
and finally move the mouse and click a third time to set the passed point.

- When entering a start or end point by selecting either a point or a segment, a Coincident constraint is created.
- When entering a passing point by selecting a point, a Coincident constraint is created.
- When entering a passing point by selecting a segment, a Tangent constraint is created.

**TUI Command**:

Sketch_1.addArc(*StartX*, *StartY*, *EndX*, *EndY*, *PassedX*, *PassedY*)
:   Parameters:
    :   - **real** – Start X.
        - **real** – Start Y.
        - **real** – End X.
        - **real** – End Y.
        - **real** – Passed X.
        - **real** – Passed Y.

    Returns:
    :   Result object.

## By tangent point and end point

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Arc_panel_tang.png)

Select a point on segment in the view to set the tangent point, then move the mouse and click to set the end point.
The tangent point by itself is a start point. The edge on which it lies will be tangent to the arc.

- When entering a tangent point by selecting a point on segment, a Tangent constraint is created.
- When entering an end point by selecting a segment, a Coincident constraint is created.
- When entering an end point, only segments are selectable.

**TUI Command**:

Sketch_1.addArc(*TangentPoint*, *EndX*, *EndY*, *Inversed*)
:   Parameters:
    :   - **object** – Tangent Point.
        - **real** – End X.
        - **real** – End Y.
        - **boolean** – Is inversed.

    Returns:
    :   Result object.

## By point on perpendicular line and end point

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Arc_panel_perp.png)

Select a point on a straight segment in the view to set the start point, then move the mouse and click to set the end point.
The edge on which the start point lies will be perpendicular to the arc (the center of the arc is lying on the edge).

- When entering a start point by selecting a point on segment, a Perpendicular constraint is created.
- When entering an end point by selecting a segment, a Coincident constraint is created.
- When entering an end point, only segments are selectable.

**TUI Command**:

Sketch_1.addArc(*StartPoint*, *EndX*, *EndY*, *Inversed*, *True*)
:   Parameters:
    :   - **object** – Start Point.
        - **real** – End X.
        - **real** – End Y.
        - **boolean** – Is inversed.
        - **boolean** – Arc is perpendicular (always True).

    Returns:
    :   Result object.

## Result

Created arc appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Arc_res.png)

Arc created

**See Also** a sample TUI Script of [Create Sketch Arc](TUI_arcFeature.md#tui-create-arc) operation.
