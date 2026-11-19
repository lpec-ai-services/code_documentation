<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/mirrorFeature.html -->

# Mirror copy

Mirror copy operation mirrors sketch entities across a line.

To create a Mirror copy in the active Sketch:

1. select in the Main Menu *Sketch - > Mirror copy* item or
2. click ![mirror.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Mirror.png) **Mirror copy** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Mirror_panel.png)

Mirror copy

Input fields:

- **Mirror line** is the mirror line selected in the view.
- **Segments** is the list of segments (lines, circles, arcs) selected in the view.

**TUI Command**:

Sketch_1.addMirror(*MirrorLine*, *Objects*)
:   Parameters:
    :   - **object** – A mirror line.
        - **listg** – A list of objects.

    Returns:
    :   Result object.

## Result

Created Mirror copy appears in the view.

The original and the mirror copy objects are marked with a special sign.

Copy object is drawn with a thinner line.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Mirror_res.png)

Mirror copy created

**See Also** a sample TUI Script of [Create Mirror copy](TUI_mirror.md#tui-create-mirror) operation.
