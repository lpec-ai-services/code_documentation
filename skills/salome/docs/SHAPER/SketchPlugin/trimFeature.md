<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/trimFeature.html -->

# Trim

The Trim operation trims away the specified segment of the curve.

The curve should have points lying on it or intersections with other curves.

Open curves (line or arc) require one or more points; closed curves (circle) require two or more points.

To create a Trim in the active Sketch:

1. select in the Main Menu *Sketch - > Trim* item or
2. click ![trim.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Trim.png) **Trim** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Trim_panel.png)

Trim

Input fields:

- **Segment** is used to select a segment to remove in the view.

The selected segment is highlighted in the view:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Trim_segment_sel.png)

The segment to remove

**TUI Command**:

Sketch_1.addTrim(*Feature*, *PositionPoint*)
:   Parameters:
    :   - **object** – Line, arc or circle.
        - **object** – Position point.

    Returns:
    :   Result object.

**Arguments**: feature (line, arc or circle) and position point (a point on or closest to the segment to remove)

## Result

Created Trim appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Trim_res.png)

Created trim

**See Also** a sample TUI Script of [Create Trim](TUI_trim.md#tui-create-trim) operation.
