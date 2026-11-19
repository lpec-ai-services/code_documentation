<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/translationFeature.html -->

# Linear copy

Linear copy operation creates one or multiple copies of the sketch entities along a vector defined by two points.

To create a Linear copy in the active Sketch:

1. select in the Main Menu *Sketch - > Linear copy* item or
2. click ![translate.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/translate.png) **Linear copy** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Linear_panel.png)

Linear copy

Input fields:

- **Segments** is the list of segments (lines, circles, arcs) selected in the view.
- **Single value/Full value** option:
  :   ![single_value](https://docs.salome-platform.org/latest/gui/SHAPER/_images/translate_32x32.png) **Single value**: step of translation is equal to the distance between the start and the end point.

      ![full_value](https://docs.salome-platform.org/latest/gui/SHAPER/_images/translate_full_32x32.png) **Full value**: distance from the originals to the farthest copies is equal to the distance between the start and the end point.
- **Start point** is the initial point of translation vector.
- **End point** is the terminal point of translation vector.
- **Total number of objects** is the total number of objects including the original one.

**TUI Command**:

Sketch_1.addTranslation(*Objects*, *Point1*, *Point2*, *NumberOfObjects*, *FullValue*)
:   Parameters:
    :   - **list** – A list of objects.
        - **object** – Start point.
        - **object** – End point.
        - **integer** – Number of objects.
        - **boolean** – Full value flag.

    Returns:
    :   Result object.

## Result

Created Linear copy appears in the view.

The original and a linear copy objects are marked with a special sign.

Copy objects are drawn with a thinner line.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Linear_res.png)

Linear copy created

**See Also** a sample TUI Script of [Create Linear copy](TUI_translation.md#tui-create-translation) operation.
