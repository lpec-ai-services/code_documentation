<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l3__sketcher.html -->

# Sketcher geomBuilder Python module » All package methods, grouped by their purpose » Creating geometrical objects

## Detailed Description

## Function Documentation

### MakeSketcher()

```python
def MakeSketcher(self, theCommand, theWorkingPlane = [0, theName = None)
```

Create a sketcher (wire or face), following the textual description, passed through *theCommand* argument.

Edges of the resulting wire or face will be arcs of circles and/or linear segments.   
Format of the description string have to be the following:

"Sketcher[:F x1 y1]:CMD[:CMD[:CMD...]]"

Where:

- x1, y1 are coordinates of the first sketcher point (zero by default),
- CMD is one of
  - "R angle" : Set the direction by angle
  - "D dx dy" : Set the direction by DX & DY  
  - "TT x y" : Create segment by point at X & Y
  - "T dx dy" : Create segment by point with DX & DY
  - "L length" : Create segment by direction & Length
  - "IX x" : Create segment by direction & Intersect. X
  - "IY y" : Create segment by direction & Intersect. Y  
  - "C radius length" : Create arc by direction, radius and length(in degree)
  - "AA x y": Create arc by point at X & Y
  - "A dx dy" : Create arc by point with DX & DY
  - "UU x y radius flag1": Create arc by point at X & Y with given radiUs
  - "U dx dy radius flag1" : Create arc by point with DX & DY with given radiUs
  - "EE x y xc yc flag1 flag2": Create arc by point at X & Y with given cEnter coordinates
  - "E dx dy dxc dyc radius flag1 flag2" : Create arc by point with DX & DY with given cEnter coordinates  
  - "WW" : Close Wire (to finish)
  - "WF" : Close Wire and build face (to finish)
- Flag1 (= reverse) is 0 or 2 ...
  - if 0 the drawn arc is the one of lower angle (< Pi)
  - if 2 the drawn arc ius the one of greater angle (> Pi)
- Flag2 (= control tolerance) is 0 or 1 ...
  - if 0 the specified end point can be at a distance of the arc greater than the tolerance (10^-7)
  - if 1 the wire is built only if the end point is on the arc with a tolerance of 10^-7 on the distance else the creation fails

Parameters
:   |  |  |
    | --- | --- |
    | theCommand | String, defining the sketcher in local coordinates of the working plane. |
    | theWorkingPlane | Nine double values, defining origin, OZ and OX directions of the working plane. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created wire.

[Example](../tui_sketcher_page.md)

### MakeSketcherOnPlane()

```python
def MakeSketcherOnPlane(self, theCommand, theWorkingPlane, theName = None)
```

Create a sketcher (wire or face), following the textual description, passed through *theCommand* argument.

For format of the description string see [MakeSketcher()](group__l3__sketcher.md#ga1919f8064bbf98d13d063d167bc344ec) method.

Parameters
:   |  |  |
    | --- | --- |
    | theCommand | String, defining the sketcher in local coordinates of the working plane. |
    | theWorkingPlane | Planar Face or LCS(Marker) of the working plane. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created wire.

[Example](../tui_sketcher_page.md)

### Sketcher2D()

```python
def Sketcher2D(self)
```

Obtain a 2D sketcher interface.

Returns
:   An instance of [Sketcher2D](classgsketcher_1_1Sketcher2D.md) interface

### Make3DSketcher()

```python
def Make3DSketcher(self, theCoordinates, theName = None)
```

Create a sketcher wire, following the numerical description, passed through *theCoordinates* argument.

Parameters
:   |  |  |
    | --- | --- |
    | theCoordinates | double values, defining points to create a wire, passing from it. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created wire.

[Example](../tui_3dsketcher_page.md)

### Sketcher3D()

```python
def Sketcher3D(self)
```

Obtain a 3D sketcher interface.

Returns
:   An instance of [Sketcher3D](classgsketcher_1_1Sketcher3D.md) interface

[Example](../tui_3dsketcher_page.md)

### Polyline2D()

```python
def Polyline2D(self)
```

Obtain a 2D polyline creation interface.

Returns
:   An instance of [Polyline2D](classgsketcher_1_1Polyline2D.md) interface

[Example](../tui_3dsketcher_page.md)
