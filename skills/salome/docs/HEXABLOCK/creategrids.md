<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/creategrids.html -->

# Create cartesian grids

To create a **Cartesian Grid** in the **Main Menu** select **Model -> Construction -> Make Grid**.

Three kinds of grid can be created:

- simple cartesian grid (see [Simple cartesian grid](#guicartgridsimple)),
- uniform cartesian grid (see [Uniform cartesian grid](#guicartgriduniform)),
- custom cartesian grid (see [Custom cartesian grid](#guicartgridcustom)).

## Simple cartesian grid

To create a simple cartesian grid, select radio button **Simple**:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_make_cart_grid_simple.png)

**Dialogue Box for a Simple cartesian grid**

The following data are required:

- *nb X*: The number of hexahedra along the X axis
- *nb Y*: The number of hexahedra along the Y axis
- *nb Z*: The number of hexahedra along the Z axis

The result of this action is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/cartgridsimple.png)

**Simple Cartesian Grid**

TUI command: [Simple Cartesian Grid](tui_cartgrid.md#tuicartgridsimple)

## Uniform cartesian grid

To create an uniform cartesian grid, select radio button **Uniform**:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_make_cart_grid_uniform.png)

**Dialogue Box for an Uniform cartesian grid**

The following data are required:

- *origin*: The vertex of the origin
- *vec X* : The X vector
- *vec Y* : The Y vector
- *vec Z* : The Z vector
- *len X* : The length of an hexahedra on the X axis
- *len Y* : The length of an hexahedra on the Y axis
- *len Z* : The length of an hexahedra on the Z axis
- *nb X* : The number of hexahedra on the X axis
- *nb Y* : The number of hexahedra on the Y axis
- *nb Z* : The number of hexahedra on the Z axis

Clicking on “Apply” on the previous dialog box will produce the following grid (Uniform hexahedra, different sizes on the three axis):

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/cartgriduniform.png)

**Unfiorm cartesian grid**

TUI command: [Uniform Cartesian Grid](tui_cartgrid.md#tuicartgriduniform)

## Custom cartesian grid

To create a Custom cartesian grid, select radio button **Custom**:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_make_cart_grid_custom.png)

**Dialogue Box for a Custom cartesian grid**

The following data are required:

- *origin*: The vertex of the origin
- *vec X* : The X vector
- *vec Y* : The Y vector
- *vec Z* : The Z vector
- *X* : A list of x values in ascendant order
- *Y* : A list of y values in ascendant order
- *Z* : A list of z values in ascendant order

A value on each axis gives the length of an hexahedra on that axis from the origin of the grid.
For example the first value in the list of x values is the length on X axis of the first hexahedra from the origin.

The result of this action is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/cartgridcustom.png)

**Custom cartesian grid**

TUI command: [Custom Cartesian Grid](tui_cartgrid.md#tuicartgridcustom)
