<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_make_symmetry.html -->

# Make Symmetry

There are three differents ways to make the symmetry of an element:

- Symmetry by point
- Symmetry by line
- Symmetry by plane

## Symmetry by point

To make the symmetry of an element by point, you need to define:

- the element
- the symmetry center

```python
elts = doc.makeSymmetryPoint (grid, orig)
```

Operations on *elts*: [Elements](tui_elements.md#tuielements2)

Here is an example where we make the symmetry of a grid:

### Example

```python
# -*- coding: latin-1 -*-
# Copyright (C) 2009-2026  CEA, EDF
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#

######## Make Symmetry Point ########

import hexablock

# ======================================================= make_grid
def make_grid (doc) :

    ori  = doc.addVertex ( 0, 0, 0)
    vz   = doc.addVector ( 0, 0, 1)
    vx   = doc.addVector ( 1 ,0, 0)

    dr = 1
    da = 360
    dl = 1

    nr = 1
    na = 6
    nl = 1
    grid = doc.makeCylindrical (ori, vx,vz, dr,da,dl, nr,na,nl, False)
    #####  doc .saveVtk ("cyl_grid.vtk")
    return grid

# ======================================================= test_sym_point
def test_sym_point () :

    doc  = hexablock.addDocument ("default")
    grid = make_grid (doc)

    orig = grid.getVertex(3)
    grid2 = doc.makeSymmetryPoint (grid, orig)

    #####  doc .saveVtk ("sym_point.vtk")
    return doc
    

# ================================================================= Begin
doc = test_sym_point  ()
```

### Result

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/grid.png)

**Initial**

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/make_sym_point.png)

**Symmetry of a grid by point**

## Symmetry by line

To make the symmetry of an element by line, you need to define:

- the element
- a point and a direction to define the line of symmetry

```python
elts = doc.makeSymmetryLine (grid, orig, dir)
```

Operations on *elts*: [Elements](tui_elements.md#tuielements2)

### Example

### Code

```python
# -*- coding: latin-1 -*-
# Copyright (C) 2009-2026  CEA, EDF
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#

######## Make Symmetry Line ########

import hexablock

# ======================================================= make_grid
def make_grid (doc) :

    ori  = doc.addVertex ( 0, 0, 0)
    vz   = doc.addVector ( 0, 0, 1)
    vx   = doc.addVector ( 1 ,0, 0)

    dr = 1
    da = 360
    dl = 1

    nr = 1
    na = 6
    nl = 1
    grid = doc.makeCylindrical (ori, vx,vz, dr,da,dl, nr,na,nl, False)
    #####  doc .saveVtk ("cyl_grid.vtk")
    return grid

# ======================================================= test_sym_line
def test_sym_line () :

    doc  = hexablock.addDocument ("default")
    grid = make_grid (doc)

    orig = grid.getVertex(3)
    dir   = doc.addVector (0, 0, 1);
    grid2 = doc.makeSymmetryLine (grid, orig, dir)

    #####  doc .saveVtk ("sym_line.vtk")
    return doc

# ================================================================= Begin
doc = test_sym_line  ()
```

### Result

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/make_sym_line.png)

**Symmetry of a grid by line**

## Symmetry by plane

To make the symmetry of an element by plane, you need to define:

- the element
- a point and a direction to define the plane of symmetry

```python
elts = doc.makeSymmetryPlane (grid, orig, dir)
```

Operations on *elts*: [Elements](tui_elements.md#tuielements2)

### Example

### Code

```python
# -*- coding: latin-1 -*-
# Copyright (C) 2009-2026  CEA, EDF
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#

######## Make Symmetry Plane ########

import hexablock

# ======================================================= make_grid
def make_grid (doc) :

    ori  = doc.addVertex ( 0, 0, 0)
    vz   = doc.addVector ( 0, 0, 1)
    vx   = doc.addVector ( 1 ,0, 0)

    dr = 1
    da = 360
    dl = 1

    nr = 1
    na = 6
    nl = 1
    grid = doc.makeCylindrical (ori, vx,vz, dr,da,dl, nr,na,nl, False)
    #####  doc .saveVtk ("cyl_grid.vtk")
    return grid

# ======================================================= test_sym_plane
def test_sym_plane () :

    doc  = hexablock.addDocument ("default")
    grid = make_grid (doc)

    orig = grid.getVertex(3)
    dir   = doc.addVector (0, 1, 0);
    grid2 = doc.makeSymmetryPlane (grid, orig, dir)

    #####  doc .saveVtk ("sym_plane.vtk")
    return doc

# ================================================================= Begin
doc = test_sym_plane  ()
```

### Result

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/make_sym_plane.png)

**Symmetry of a grid by plane**

GUI command: [Make elements by symmetry](gui_make_symmetry.md#guimakesymmetry)
