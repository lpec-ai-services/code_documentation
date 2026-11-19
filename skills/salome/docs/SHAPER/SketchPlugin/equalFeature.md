<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/equalFeature.html -->

# Equal constraint

Equal constraint makes lines, circles or arcs equal.

Lines become equal in length, circles and arcs - equal in radius.

To create an Equal constraint in the active Sketch:

1. select in the Main Menu *Sketch - > Equal* item or
2. click ![equal.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Equal.png) **Equal** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Equal_panel.png)

Input fields:

- **First object** is a line, a circle or an arc selected in the view.
- **Second object** is a line, a circle or an arc selected in the view.

Note that a line can be equal to a line only, a circle - to a circle or an arc.

After the objects are selected, the object sizes become equal.

The equal objects are marked with **=** sign.

**TUI Command**:

Sketch_1.setEqual(*Object1*, *Object2*)
:   Parameters:
    :   - **object** – First object.
        - **object** – Second object.

    Returns:
    :   Result object.

## Result

Created Equal constraint appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Equal_res.png)

Created equal constraint

**See Also** a sample TUI Script of [Create Equal constraint](TUI_equal.md#tui-create-equal) operation.
