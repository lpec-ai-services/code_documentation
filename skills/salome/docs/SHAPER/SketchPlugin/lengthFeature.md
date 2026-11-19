<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/lengthFeature.html -->

# Length constraint

Length constraint fixes the length of lines, such as standalone line or rectangle side.

To create a Length constraint in the active Sketch:

1. select in the Main Menu *Sketch - > Length* item or
2. click ![length.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Length.png) **Length** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Length_panel.png)

Input fields:

- **Line** is the the line object selected in the view;
- **Value** is a line length, can be modified to set the desirable value;
- **Text location** is a position of the length value label relating to extension line (in the view):
  :   ![location_left](https://docs.salome-platform.org/latest/gui/SHAPER/_images/location_left.png) **Left** inserts text to the left of the length extension line;

      ![location_auto](https://docs.salome-platform.org/latest/gui/SHAPER/_images/location_automatic.png) **Automatic** inserts text in the middle of the length extension line if it has enough length, otherwise - to the left;

      ![location_right](https://docs.salome-platform.org/latest/gui/SHAPER/_images/location_right.png) **Right** inserts text to the right of the length extension line.

When the line is selected, the length value is displayed in the property panel and in the view.

When creating the constraint, after selection of a line for the first time:

- drag the length presentation in the view to the desired position and click once;
- set desirable length value in the input field in the view and press **Enter** or just press **Enter** to keep the current length.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Length_field_view.png)

Length input in the view

**TUI Command**:

Sketch_1.setLength(*LineObject*, *Value*)
:   Parameters:
    :   - **object** – A line.
        - **real** – Length value.

    Returns:
    :   Result object.

## Result

Created Length appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Length_res.png)

Length created

**See Also** a sample TUI Script of [Create Length constraint](TUI_length.md#tui-create-length) operation.
