<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/gui_blocks_for_cyl_pipe.html -->

# Cylinders and Pipes Construction

## Cylinder

To make a **Cylinder** in the **Main Menu** select **Model -> Construction -> Make Cylinder**.

### Simple Cylinder

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_cylindersimple.png)

**Dialog Box to make a Simple Cylinder**

The following data are required:

- *nb Radial* : number of hexahedra on radial.
- *nb Angular* : number of hexahedra along the perimeter of the cylinder.
- *nb Height* : number of hexahedra along the axis of the cylinder.

Clicking on “Apply” on the previous dialog box will produce the following result:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/cylindersimple.png)

**Simple Cylinder**

The result is an array of hexahedral ranked first by following the
radial direction and the angular direction, then according to the
layers in the cylinder axis.

TUI command: [Simple Cylinder](tui_blocks_for_cyl_pipe.md#tuicylindersimple)

### Uniform Cylinder

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_cylinderuniform.png)

**Dialog Box to make a Uniform Cylinder**

The following data are required:

- *origin* : origin’s coordinates of the cylinder (select a vertex).
- *axis* : the axis of the cylinder (select a vector).
- *base* : the base of the cylinder (select a vector).
- *radius* : the radius of the cylinder.
- *hole radius*: the radius of the hole in the cylinder .
- *slice angle*: angle of the cylinder around the Z axis.
- *height* : the height of the cylinder.
- *nb Radial* : number of hexahedra on radial.
- *nb Angular* : number of hexahedra along the perimeter of the cylinder.
- *nb Height* : number of hexahedra along the axis of the cylinder.

Clicking on “Apply” on the previous dialog box will produce the following result:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/cylinderuniform.png)

**Uniform Cylinder**

TUI command: [Uniform Cylinder](tui_blocks_for_cyl_pipe.md#tuicylinderuniform)

### Custom Cylinder

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_cylindercustom.png)

**Dialog Box to make a Custom Cylinder**

The following data are required:

- *origin* : origin’s coordinates of the cylinder (select a vertex).
- *axis* : the axis of the cylinder (select a vector).
- *base* : the base of the cylinder (select a vector).
- *radius* : a list of radiuses in ascendant order.
- *angle* : a list of angles in ascendant order.
- *height* : a list of heights in ascendant order.

Clicking on “Apply” on the previous dialog box will produce the following result:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/cylindercustom.png)

**Custom Cylinder**

TUI command: [Custom Cylinder](tui_blocks_for_cyl_pipe.md#tuicylindercustom)

## Cylinders

To make **two cylinders in T shape** in the **Main Menu** select **Model -> Construction -> Make Cylinders**

The dialogue box to make cylinders is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_cylinders.png)

**Make Cylinders**

The following data are required:

- *origin* : the origin of the cylinder (select a vertex).
- *axis* : the axis of the cylinder (select a vector).
- *radius* : the radius of the cylinder.
- *height* : the height of the cylinder.

Those arguments must be filled for the **Big Cylinder** and the **Small Cylinder**.

Clicking on “Apply” on the previous dialog box will produce the following result:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/cylinders.png)

**Make Cylinders (T Shape)**

TUI command: [Make Cylinders](tui_blocks_for_cyl_pipe.md#tuicylinders)

## Pipe

To make a **Pipe** in the **Main Menu** select **Model -> Construction -> Make Pipe**.

### Simple Pipe

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_pipesimple.png)

**Dialog Box to make a Simple Pipe**

The following data are required:

- *nb Radial* : number of hexahedra on radial.
- *nb Angular* : number of hexahedra along the perimeter of the pipe.
- *nb Height* : number of hexahedra along the axis of the pipe.

TUI command: [Simple Pipe](tui_blocks_for_cyl_pipe.md#tuipipesimple)

### Uniform Pipe

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_pipeuniform.png)

**Dialog Box to make a Uniform Pipe**

The following data are required:

- *origin* : origin’s coordinates of the pipe (select a vertex).
- *axis* : the axis of the pipe (select a vector).
- *base* : the base of the pipe (select a vector).
- *radius* : the radius of the pipe.
- *hole radius*: the radius of the hole in the pipe.
- *slice angle*: angle of the pipe around the Z axis.
- *height* : the height of the pipe.
- *nb Radial* : number of hexahedra on radial.
- *nb Angular* : number of hexahedra along the perimeter of the pipe.
- *nb Height* : number of hexahedra along the axis of the pipe.

TUI command: [Uniform Pipe](tui_blocks_for_cyl_pipe.md#tuipipeuniform)

### Custom Pipe

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_pipecustom.png)

**Dialog Box to make a Custom Pipe**

The following data are required:

- *origin* : origin’s coordinates of the pipe (select a vertex).
- *axis* : the axis of the pipe (select a vector).
- *base* : the base of the pipe (select a vector).
- *radius* : a list of radiuses in ascendant order.
- *angle* : a list of angles in ascendant order.
- *height* : a list of heights in ascendant order.

TUI command: [Custom Pipe](tui_blocks_for_cyl_pipe.md#tuipipecustom)

## Pipes

To make **two intersect pipes** in the **Main Menu** select **Model -> Construction -> Make Pipes**.

The dialogue box to make pipes is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_pipes.png)

**Make Pipes**

You can make **Pipes** (T Shape) through a **Big Pipe** and a **Small Pipe**.

The following data are required:

- *origin* : the origin of the pipe (select a vertex).
- *axis* : the axis of the pipe (select a vector).
- *radius* : the radius of the pipe.
- *hole radius*: the radius of the hole in the pipe.
- *height* : the height of the pipe.

Those arguments must be filled for the **Big Pipe** and the **Small Pipe**.

TUI command: [Make Pipes](tui_blocks_for_cyl_pipe.md#tuipipes)
