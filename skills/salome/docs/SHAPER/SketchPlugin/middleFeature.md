<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/middleFeature.html -->

# Middle point constraint

Middle point constraint forces a point to middle of a line.

To create a Middle point in the active Sketch:

1. select in the Main Menu *Sketch - > Middle point* item or
2. click ![middlepoint.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/MiddlePoint.png) **Middle point** button in Sketch toolbar:

There are 2 algorithms for creation of a middle constraint:

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/MiddlePoint.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/MiddlePoint.png)

**By object and point** create a middle constraint by object (segment or arc) and point

[![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/MiddlePoint_obj.png)](https://docs.salome-platform.org/latest/gui/SHAPER/_images/MiddlePoint_obj.png)

**By object** create a middle point on the object (segment or arc)

---

## By object and point

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Middlepoint_obj_point_panel.png)

Input fields:

- **First object** is a point or a line selected in the view.
- **Second object** is a point or a line selected in the view.

Note that one of two objects should be a line and the other a point (i.e. a point, a line or an arc end point, a center of a circle or an arc).

After the objects are selected, the point is moved to the middle of the line.

The middle points are marked with a special sign.

**TUI Command**:

Sketch_1.setMiddlePoint(*Point*, *Line*)
:   Parameters:
    :   - **object** – A point.
        - **object** – A line.

    Returns:
    :   Result object.

## Result

Created Middle point constraint appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Middlepoint_obj_point_res.png)

Created middle point constraint

## By object

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Middlepoint_obj_panel.png)

Input fields:

- **Object** is a line selected in the view.

After the object are selected, will be created auxiliary point on the middle of the line.

The middle points are marked with a special sign.

**TUI Command**:

SketchPoint_1 = Sketch_1.setMiddlePoint(Line)
:   Parameters:
    :   **object** – A line.

    Returns:
    :   Created middle point.

## Result

Created Middle point constraint appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Middlepoint_obj_res.png)

Created middle point constraint

**See Also** a sample TUI Script of [Create Middle point constraint](TUI_middle.md#tui-create-middle) operation.
