<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_cartgrid.html -->

# Make cartesian grids

## Simple Cartesian Grid

To add a simple cartesian grid to the model, the following data are required:

- *nb X*: The number of hexahedra along the X axis
- *nb Y*: The number of hexahedra along the Y axis
- *nb Z*: The number of hexahedra along the Z axis

Make a Simple Cartesian Grid:

```python
elts = doc.makeCartesianTop(nbX, nbY, nbZ)
```

GUI command: [Simple cartesian grid](creategrids.md#guicartgridsimple)

## Uniform Cartesian Grid

To add a uniform cartesian grid to the model, the following data are required:

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

Make a Uniform Cartesian Grid:

```python
elts = doc.makeCartesianUni(orig, vecX, vecY, vecZ, lenX, lenY, lenZ, nbX, nbY, nbZ)
```

GUI command: [Uniform cartesian grid](creategrids.md#guicartgriduniform)

## Custom Cartesian Grid

To add a custom cartesian grid to the model, the following data are required:

- *origin*: The vertex of the origin
- *vec X* : The X vector
- *vec Y* : The Y vector
- *vec Z* : The Z vector
- *tx* : A list of x coordinates in ascendant order
- *ty* : A list of y coordinates in ascendant order
- *tz* : A list of z coordinates in ascendant order

Make a Custom Cartesian Grid:

```python
elts = doc.makeCartesian(orig, vecX, vecY, vecZ, tx, ty, tz)
```

GUI command: [Custom cartesian grid](creategrids.md#guicartgridcustom)

Operations on *elts*: [Elements](tui_elements.md#tuielements2)

## Example

```python
# -*- coding: utf-8 -*-
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

####### Test Cartesian Grid #################    
    
import hexablock

doc  = hexablock.addDocument ("Cartesian Grid Test")

# Simple Cartesian Grid

nbX = 3
nbY = 4
nbZ = 5

grid0 = doc.makeCartesianTop(nbX, nbY, nbZ)
grid0.saveVtk("makeCartesianTop.vtk")

# Uniform Cartesian Grid

orig1 = doc.addVertex(10, 0, 0)

vecX = doc.addVector(1, 0, 0)
vecY = doc.addVector(0, 1, 0)
vecZ = doc.addVector(0, 0, 1)

lenX = 5 
lenY = 3.5
lenZ = 2

grid1 = doc.makeCartesianUni(orig1, vecX, vecY, vecZ, lenX, lenY, lenZ, nbX, nbY, nbZ)
grid1.saveVtk("makeCartesianUni.vtk")

# Custom Cartesian Grid

orig2 = doc.addVertex(20, 0, 0)

tx = [] # a list of x coordinates
ty = [] # a list of y coordinates
tz = [] # a list of z coordinates
for i in range(6):
  tx.append(i+1)
  ty.append(i+1)
  tz.append(i+1)
# tx=ty=tz=[1,2,3,4,5,6]

grid2 = doc.makeCartesian(orig2, vecX, vecY, vecZ, tx, ty, tz)
grid2.saveVtk("makeCartesian.vtk")
```
