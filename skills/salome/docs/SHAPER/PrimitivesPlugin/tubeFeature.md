<!-- source: https://docs.salome-platform.org/latest/gui/SHAPER/PrimitivesPlugin/tubeFeature.html -->

# Tube

Tube feature creates a tube solid.

To create a Tube in the active part:

1. select in the Main Menu *Primitives - > Tube* item or
2. click ![Tube_button.icon](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Tube_button.png) **Tube** button in the toolbar

The following property panel appears.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Tube.png)

Tube

Input fields:

- **rmin** defines the inner radius of the the tube;
- **rmax** defines the outer radius of the the tube;
- **height** defines the height of the the tube;

**TUI Command**:

model.addTube(*Part_doc*, *rmin*, *rmax*, *height*)
:   Parameters:
    :   - **part** – The current part object.
        - **real** – rmin.
        - **real** – rmax.
        - **real** – height.

    Returns:
    :   Result object.

## Result

An example is shown below.

![figure](https://docs.salome-platform.org/latest/gui/SHAPER/_images/Tube_res.png)

Tube created

**See Also** a sample TUI Script of [Create Tube](TUI_tubeFeature.md#tui-create-tube) operation.
