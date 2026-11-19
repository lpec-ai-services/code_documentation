<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/gui_cut_hexa.html -->

# Cut hexahedra

This method allows to cut in two (or more) a series of hexahedra
using a series of edges propagation.

To cut an hexahedra in the **Main Menu** select **Model -> Operation -> Cut Edge**.

## Uniform Cut

The dialogue box to make a uniform cut of an hexahedra is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_cuthexauniform.png)

**Uniform Cut**

**Arguments:**

- *Edge* : an edge on the hexahedra to cut.
- *Nb layers*: the number of cuts.

TUI command: [Uniform Cut](tui_cut_hexa.md#tuicuthexauniform)

## Custom Cut

The dialogue box to make a custom cut of an hexahedra is:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/gui_cuthexacustom.png)

**Custom Cut**

**Arguments:**

- *Edge* : an edge on the hexahedra to cut.
- *length* : the list of the lengths of the layers in ascendant order.

TUI command: [Custom Cut](tui_cut_hexa.md#tuicuthexacustom)
