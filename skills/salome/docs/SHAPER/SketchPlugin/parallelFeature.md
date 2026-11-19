<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/SketchPlugin/parallelFeature.html -->

# Parallel constraint

Parallel constraint fixes two lines as parallel to one another.

To create a Parallel constraint in the active Sketch:

1. select in the Main Menu *Sketch - > Parallel* item or
2. click ![parallel.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Parallel.png) **Parallel** button in Sketch toolbar:

Property panel:

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Parallel_panel.png)

Input fields:

- **First line** is the first line selected in the view.
- **Second line** is the second line selected in the view.

After the lines are selected **||** sign will be added to each of them in the view.

**TUI Command**:

Sketch_1.setParallel(*Line1*, *Line2*)
:   Parameters:
    :   - **object** – Line 1.
        - **object** – Line 2.

    Returns:
    :   Result object.

## Result

Created Parallel constraint appears in the view.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Parallel_res.png)

Created parallel constraint

**See Also** a sample TUI Script of [Create Parallel constraint](TUI_parallel.md#tui-create-parallel) operation.
