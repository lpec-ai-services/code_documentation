<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/splitFeature.html -->

# Split

The Split operation splits sketch curve into multiple segments.

The curve should have points lying on it.

Open curves (line or arc) require one or more points to split with; closed curves (circle) require two or more points.

To create a Split in the active Sketch:

1. select in the Main Menu *Sketch - > Split* item or
2. click ![split.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Split.png) **Split** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Split_panel_Sketch.png)

Split

Input fields:

- **Segment** is used to select a segment to be split off in the view.

The selected segment is highlighted in the view:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Split_segment_sel.png)

The segment to split off

**TUI Command**:

Sketch_1.addSplit(*Feature*, *PositionPoint*)
:   Parameters:
    :   - **object** – Line, arc or circle.
        - **object** – Position point (a point on the segment to split off or closest to it).

    Returns:
    :   Result object.

## Result

Created Split appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Split_res.png)

Created split

**See Also** a sample TUI Script of [Create Split](TUI_split.md#tui-create-split) operation.
