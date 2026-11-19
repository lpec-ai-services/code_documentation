<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/gui_quad_revolution.html -->

# Quad revolution

To make a **Quad revolution** in the **Main Menu** select **Model -> Operation -> Quad Revolution**.

## Uniform Quad Revolution

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_quadsrevolutionuniform.png)

**Dialog Box to make a uniform quadrangle revolution**

**Arguments:**

- *Quad(s)* : a set of quadrangles from which hexahedrons will be created (select quads).
- *center* : center of rotation (select a vertex).
- *axis* : axis of rotation (select a vector).
- *angle* : Specify the rotation’s angle at each step.
- *Nb layers*: the number of steps.

TUI command: [Uniform Quad Revolution](tui_quad_revolution.md#tuiquadsrevolutionuniform)

## Custom Quad Revolution

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_quadsrevolutioncustom.png)

**Dialog Box to make a custom quadrangle revolution**

**Arguments:**

- Quad(s): a set of quadrangles from which hexahedrons will be created (select quads).
- center: center of rotation (select a vertex).
- axis: axis of rotation (select a vector).
- angle: a set of angle (in degrees). Specify the rotation’s angle at each step.

TUI command: [Custom Quad Revolution](tui_quad_revolution.md#tuiquadsrevolutioncustom)
