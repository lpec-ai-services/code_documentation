<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/gui_prism_join_quad.html -->

# Extrude and join quadrangles

## Extrude Quadrangles

To extrude from quadrangles in the **Main Menu** select **Model -> Operation -> Extrude Quadrangles**.

From a list of quadrangles, a set of hexahedra is created.

### Simple Extrude

The dialogue box to make a simple extrude of quadrangles is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_extrudequadssimple.png)

**Simple Extrude From Quadrangles**

**Arguments:**

- *Quad(s)* : the list of quadrangles to be extruded.
- *Nb layers* : the number of layers of hexahedra resulting from the extrusion.

The direction of the extrusion is the vertical axis (Z axis).

TUI command: [Simple Extrude](tui_prism_join_quad.md#tuiextrudequadssimple)

### Uniform Extrude

The dialogue box to make a uniform extrude of quadrangles is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_extrudequadsuniform.png)

**Uniform Extrude From Quadrangles**

**Arguments:**

- *Quad(s)* : the list of quadrangles to be extruded.
- *dircection*: the direction of the extrusion.
- *length* : the length of hexahedra resulting from the extrusion.
- *Nb layers* : the number of layers of hexahedra resulting from the extrusion.

TUI command: [Uniform Extrude](tui_prism_join_quad.md#tuiextrudequadsuniform)

### Custom Extrude

The dialogue box to make a custom extrude of quadrangles is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_extrudequadscustom.png)

**Custom Extrude From Quadrangles**

**Arguments:**

- *Quad(s)* : the list of quadrangles to be extruded.
- *direction* : the direction of the extrusion.
- *height* : a list of heights (in ascendant order because the size is computed from the origin) to specify the size of each layer of extrusion.

TUI command: [Custom Extrude](tui_prism_join_quad.md#tuiextrudequadscustom)

## Join Quadrangles

To join quadrangles in the **Main Menu** select **Model -> Operation -> Join Quadrangles**.

### Uniform Join Quadrangles

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_joinquadsuniform.png)

**Uniform Join Quadrangles Dialog Box**

**Arguments:**

- *Quad(s)* : the set of quadrangles to be joined and from which hexahedra will be created.
- *From point a*: a vertex belonging to the first quadrangle of the set of quadrangles.
- *From point b*: a vertex, consecutive to previous Point a, belonging to the first quadrangle.
- *Quadrangle* : a quadrangle from the set of targeted quadrangles.
- *To point a* : the target vertex (in the target quadrangle) for *From point a*.
- *To point b* : the target vertex (in the target quadrangle) for *From point b*.
- *Nb layers* : number of layers of hexahedra issued from the operation.

TUI command: [Uniform Join](tui_prism_join_quad.md#tuijoinquadsuniform)

### Custom Join Quadrangles

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_joinquadscustom.png)

**Custom Join Quadrangles Dialog Box**

**Arguments:**

- *Quad(s)* : the set of quadrangles to be joined and from which hexahedra will be created.
- *From point a*: a vertex belonging to the first quadrangle of the set of quadrangles.
- *From point b*: a vertex, consecutive to previous Point a, belonging to the first quadrangle.
- *Quadrangle* : a quadrangle from the set of targeted quadrangles.
- *To point a* : the target vertex (in the target quadrangle) for *From point a*.
- *To point b* : the target vertex (in the target quadrangle) for *From point b*.
- *height* : a list of heights to specify the size of each layer of hexahedra issued from the operation.

TUI command: [Custom Join](tui_prism_join_quad.md#tuijoinquadscustom)
