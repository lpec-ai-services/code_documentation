<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_make_elmts.html -->

# Make elements by transforming elements

Rotate and translate for any kind of elements:

```python
elts = doc.makeTranslation(elements, vec)
elts = doc.makeRotation(elements, ver, vec, angle)
elts = doc.makeScale (elements, destination_point, k)
```

and “element” could be Vertex, Edge, Quadrangle, Hexahedeon, Vector, Cylinder,
Pipe and Elements and the result “elts” is always an object of type
“Elements”.

Operations on *elts*: [Elements](tui_elements.md#tuielements2)

## Example

### Translation

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

####### Test make translation ###############

import hexablock

doc = hexablock.addDocument("default")

size_x = 1
size_y = 1
size_z = 2

orig = doc.addVertex(0, 0, 0)
dirVr = doc.addVector(1, 1, 1)

grid = doc.makeCartesian1(orig, dirVr, size_x, size_y, size_z, 0, 0, 0)

#####  doc.saveVtk ("cartesian.vtk")

devant = doc.addVector(5, 0, 0)
grid1 = doc.makeTranslation(grid, devant)

#####  doc.saveVtk ("translation.vtk")
```

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/make_translation.png)

**Translation**

### Rotation

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

####### Test make rotation ###############

import hexablock

doc = hexablock.addDocument("default")

size_x = 1
size_y = 1
size_z = 2

orig = doc.addVertex(0, 0, 0)
dirVr = doc.addVector(1, 1, 1)

grid = doc.makeCartesian1(orig, dirVr, size_x, size_y, size_z, 0, 0, 0)
#####  grid.saveVtk ("initial.vtk")

orig.setScalar(2)
grid1 = doc.makeRotation(grid, orig, dirVr, 60)

#####  grid1.saveVtk ("rotation.vtk")
```

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/cartesian.png)

**Initial**

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/make_rotation.png)

**Rotation**

### Scale

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

####### Test make scale ###############

import hexablock

doc  = hexablock.addDocument ("default")
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

dest   = doc.addVertex (15, 0, 0)
grid2  = doc.makeScale (grid, dest, 0.5)

#####  doc .saveVtk ("make_scale.vtk")
```

![figure](https://docs.salome-platform.org/latest/gui/HEXABLOCK/_images/make_scale.png)

**Scaling**

GUI command: [Make elements by transforming elements](gui_make_elmts.md#guimakeelements)
