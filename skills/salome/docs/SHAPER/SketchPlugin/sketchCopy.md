<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/sketchCopy.html -->

# Sketch Copy

This macro will just copy the selected sketch feature into a new sketch feature and disappear.
So, the new sketch feature will be placed into the current history location with all sub-elements
of the sketch copied.

To start a Sketch Copy operation:

1. select in the Main Menu *Macros - > Sketch Copy* item or
2. click ![SketchCopy.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/SketchCopy.png) **Sketch Copy** button in Macros toolbar:

The following property panel appears:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/SketchCopy_panel.png)

Sketch copy panel

Select a sketch feature to copy. On Apply button press the copied sketch will be created in the Object Browser tree.

**TUI Command**:

model.copySketch(*Doc*, *Sketch*)
:   Parameters:
    :   - **document** – A document where to copy the sketch.
        - **object** – A sketch to be copied.

    Returns:
    :   Copied sketch.

**See Also** a sample TUI Script of [Sketch copy](TUI_sketchCopy.md#tui-copy-sketch) operation.
