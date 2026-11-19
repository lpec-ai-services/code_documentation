<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_cylgrid.html -->

# Make cylindrical grids

To add a regular cylindrical grid, the following data are required:

- the coordinates (vertex) of the cylinder base center: *pt*
- the vectors defining the axis and the direction of the cylinder: *vex, vez*
- the radial, angular and axial sizes: *dr, da, dl*
- the radial, angular and axial elements number: *nr, na, nl*
- to fill or not the central part of hexahedra: *fill*

To add an irregular cylindrical grid, the following data are required:

- the coordinates (vertex) of the cylinder base center: *pt*
- the vectors defining the axis and the direction of the cylinder: *vex, vez*
- the radial, angular and axial sizes: *dr (a list of radius), da (a list of angles), dl (a list of heights)*
- to fill or not the central part of hexahedra: *fill*

Make a regular cylindrical grid:

```python
elts = doc.makeCylindrical(pt, vex, vez, dr, da, dl, nr, na, nl, fill)
```

Make an irregular cylindrical grid:

```python
elts = doc.makeCylindricals (pt, vex, vez, dr, da, dl, False)
```

Operations on *elts*: [Elements](tui_elements.md#tuielements2)

The result is an array of hexahedra which are arranged along the
radial axis first, then the angular axis, then according to the layers
and then possibly hexahedra filling the central part.

The filling the central part of the cylinder is made ​accordingly to the two following cases:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/cyl_grid2.png)

**Filling of the central part of the cylinder in the case the number of angular elements is odd na = 5.**

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/cyl_grid1.png)

**Filling of the central part of the cylinder in the case the number of angular elements is even na = 4.**

## Example (regular mode)

Filling rule is illustrated by different case-tests:

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/cylindrical_grids.png)

**Cylindrical Grids (regular)**

## Example (irregular mode)

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/irregular_cylindrical.png)

**Irregular cylindrical grid**

GUI command: guicylgrid
