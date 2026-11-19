<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/gui_hemisphere.html -->

# Create Hemispherical Grid

To create an **Hemispherical Grid** in the **Main Menu** select **Model -> Construction -> Make Hemisphere**.

## Simple Sphere and Simple Rind

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_spheresimple.png)

**Parameters for a Simple Sphere or Rind**

The following data are required:

- *nb Radial* : number of hexahedra on radial.
- *nb Angular* : number of hexahedra along the perimeter of the sphere.
- *nb Height* : number of hexahedra along the axis of the sphere.

The result of this action is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/spheresimple.png)

**Simple Sphere**

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/rindsimple.png)

**Simple Rind**

TUI command: [Simple Sphere](tui_hemisphere_rind.md#tuispheresimple)

TUI command: [Simple Rind](tui_hemisphere_rind.md#tuirindsimple)

## Uniform Sphere

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_sphereuniform.png)

**Parameters for an Uniform Sphere**

The following data are required:

- *center* : center coordinates of the sphere (select a vertex).
- *axis* : the axis of the hole (select a vector).
- *base* : the base of the sphere (select a vector).
- *external radius*: the radius of the sphere.
- *hole radius*: the radius of the hole in the sphere .
- *slice angle*: angle of the sphere around the Z axis.
- *vertex for cut plan*: the vertex along the vertical axis where the rind will be cut.
- *nb Radial* : number of hexahedra on radial.
- *nb Angular* : number of hexahedra along the perimeter of the sphere.
- *nb Height* : number of hexahedra along the axis of the sphere.

The result of this action is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/sphereuniform.png)

**Uniform Sphere**

TUI command: [Uniform Sphere](tui_hemisphere_rind.md#tuisphereuniform)

## Custom Sphere

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_spherecustom.png)

**Parameters for a Custom Sphere**

The following data are required:

- *center*: center coordinates of the sphere (select a vertex).
- *axis* : the axis of the hole (select a vector).
- *base* : the base of the sphere (select a vector).
- *radius*: a list of radiuses in ascendant order.
- *angle* : a list of angles in ascendant order.
- *height*: a list of heights in ascendant order.

The result of this action is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/spherecustom.png)

**Custom Sphere**

TUI command: [Custom Sphere](tui_hemisphere_rind.md#tuispherecustom)

## Uniform Rind

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_rinduniform.png)

**Parameters for a Uniform Rind**

The following data are required:

- *center* : center coordinates of the rind (select a vertex).
- *axis* : the vertical axis of the rind (select a vector).
- *base* : the base of the rind (select a vector).
- *external radius*: the radius of the rind.
- *internal radius*: the internal radius.
- *hole radius*: the radius of the hole.
- *slice angle*: angle of the rind around the Z axis.
- *vertex for cut plan*: the vertex along the vertical axis where the rind will be cut.
- *nb Radial* : number of hexahedra on radial.
- *nb Angular* : number of hexahedra along the perimeter.
- *nb Height* : number of hexahedra along the axis of the rind.

The result of this action is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/rinduniform.png)

**Uniform Rind**

TUI command: [Uniform Rind](tui_hemisphere_rind.md#tuirinduniform)

## Custom Rind

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_rindcustom.png)

**Parameters for a Custom Rind**

The following data are required:

- *center*: center coordinates of the rind (select a vertex).
- *axis* : the vertical axis (select a vector).
- *base* : the base of the rind (select a vector).
- *radius*: a list of radiuses in ascendant order.
- *angle* : a list of angles in ascendant order.
- *height*: a list of heights in ascendant order.

The result of this action is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/rindcustom.png)

**Custom Rind**

TUI command: [Custom Rind](tui_hemisphere_rind.md#tuirindcustom)

## Simple Concentric (Spherical)

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_concentricsimple.png)

**Parameters for a Simple Concentric**

The following data are required:

- *nb Layers*: the number of nested hexahedra.
- *Criteria*

The result of this action is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/concentricsimple.png)

**Simple Concentric**

TUI command: [Simple Concentric](tui_hemisphere_rind.md#tuiconcentricsimple)

## Uniform Concentric (Spherical)

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_concentricuniform.png)

**Parameters for a Uniform Concentric**

The following data are required:

- *center*: the center’s coordinates (select a vertex).
- *axis* : the vertical axis (select a vector).
- *base* : the base of the concentric (select a vector).
- *external radius*: the radius of the concentric.
- *nb Layers*: the number of nested hexahedra in the concentric.
- *Criteria*.

TUI command: [Uniform Concentric](tui_hemisphere_rind.md#tuiconcentricuniform)

## Custom Concentric (Spherical)

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_concentriccustom.png)

**Parameters for a Custom Concentric**

The following data are required:

- *center*: the center’s coordinates (select a vertex).
- *axis* : the vertical axis (select a vector).
- *base* : the base of the concentric (select a vector).
- *criteria*.
- *radius*: a list of radiuses in ascendant order.

The result of this action is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/concentriccustom.png)

**Custom Concentric**

TUI command: [Custom Concentric](tui_hemisphere_rind.md#tuiconcentriccustom)
