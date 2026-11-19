<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_hemisphere_rind.html -->

# Hemisphere Grid Construction

## Sphere

### Simple Sphere

To create a Simple Sphere Grid in python mode, you need the following arguments:

- *nbR* : number of hexahedra on radial.
- *nbA* : number of hexahedra along the perimeter of the sphere.
- *nbH* : number of hexahedra along the axis of the sphere.

Use the function **makeSphereTop**:

```python
elts = doc.makeSphereTop(nbR, nbA, nbH)
```

GUI command: [Simple Sphere and Simple Rind](gui_hemisphere.md#guisphereandrindsimple)

### Uniform Sphere

The following data are required:

- *center*: center coordinates of the sphere (a vertex).
- *vx* : the base of the sphere (a vector).
- *vz* : the axis of the hole (a vector).
- *rtrou* : the radius of the hole in the sphere.
- *rext* : the radius of the sphere.
- *angle* : angle of the sphere around the Z axis.
- *vplan* : the vertex along the vertical axis where the rind will be cut.
- *nr* : number of hexahedra on radial.
- *na* : number of hexahedra along the perimeter of the sphere.
- *nh* : number of hexahedra along the axis of the sphere.

Use the function **makeSphereUni** to make a uniform sphere grid:

```python
elts = doc.makeSphereUni (center, vx, vz, rtrou, rext, angle, vplan, nr, na, nh)
```

GUI command: [Uniform Sphere](gui_hemisphere.md#guisphereuniform)

### Custom Sphere

The following data are required:

- *center*: center coordinates of the sphere (a vertex).
- *vx* : the base of the sphere (a vector).
- *vz* : the axis of the sphere (a vector).
- *trad* : a list of radiuses in ascendant order.
- *tang* : a list of angles in ascendant order.
- *tphi* : a list of heights in ascendant order.

Use the function **makeSphere** to make a custom sphere:

```python
elts = doc.makeSphere(center, vx, vz, trad, tang, tphi)
```

GUI command: [Custom Sphere](gui_hemisphere.md#guispherecustom)

Operations on *elts*: [Elements](tui_elements.md#tuielements2)

### Example

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

####### Sphere Grid Test ##########

import hexablock

doc  = hexablock.addDocument ("Sphere Grid Test")

# Simple Sphere -----

nr = 4
na = 8
nh = 12

sphere0 = doc.makeSphereTop(nr, na, nh)
sphere0.saveVtk("makeSphereTop.vtk")

# Uniform Sphere -----

center  = doc.addVertex (0, 0, 0)
vplan = doc.addVertex (0, 0, -0.5)
vx    = doc.addVector (1, 0, 0)
vz    = doc.addVector (0, 0, 1)
rtrou = 1
rext  = 10
angle = 180

sphere1 = doc.makeSphereUni (center, vx, vz, rtrou, rext, angle, vplan, nr, na, nh)
sphere1.saveVtk("makeSphereUni.vtk")

# Custom Sphere -----

dr     = (rext-rtrou)/nr
dtheta = angle/na
dphi   = 180.0/nh
trad = []
tang = []
tphi = []

for nro in range(nr+1):
  trad.append(rtrou + nro*dr)
  
for nro in range(na+1):
  tang.append(nro*dtheta)
  
for nro in range(nh+1):
  tphi.append(-90 + nro*dphi)

sphere2 = doc.makeSphere (center, vx, vz, trad, tang, tphi)
sphere2.saveVtk("makeSphere.vtk")
```

## Rind

### Simple Rind

To create a Simple Rind Grid in python mode, you need the following arguments:

- *nbR* : number of hexahedra on radial.
- *nbA* : number of hexahedra along the perimeter of the rind.
- *nbH* : number of hexahedra along the axis of the rind.

Use the function **makeRindTop**:

```python
elts = doc.makeRindTop(nbR, nbA, nbH)
```

GUI command: [Simple Sphere and Simple Rind](gui_hemisphere.md#guisphereandrindsimple)

### Uniform Rind

The following data are required:

- *center*: center coordinates of the rind (a vertex).
- *vx* : the base of the rind (a vector).
- *vz* : the axis of the hole (a vector).
- *rtrou* : the radius of the hole in the rind.
- *rint* : the internal radius.
- *rext* : the radius of the rind.
- *angle* : angle of the rind around the Z axis.
- *vplan* : the vertex along the vertical axis where the rind will be cut.
- *nr* : number of hexahedra on radial.
- *na* : number of hexahedra along the perimeter of the rind.
- *nh* : number of hexahedra along the axis of the rind.

Use the function **makeRindUni** to make a uniform rind grid:

```python
elts = doc.makeRindUni(center, vx, vz, rtrou, rint, rext, angle, vplan, nr, na, nh)
```

GUI command: [Uniform Rind](gui_hemisphere.md#guirinduniform)

### Custom Rind

The following data are required:

- *center*: center coordinates of the rind grid (a vertex).
- *vx* : the base of the rind grid (a vector).
- *vz* : the axis of the rind (a vector).
- *trad* : a list of radiuses in ascendant order.
- *tang* : a list of angles in ascendant order.
- *tphi* : a list of heights in ascendant order.

Use the function **makeRind** to make a custom rind grid:

```python
elts = doc.makeRind(center, vx, vz, trad, tang, tphi)
```

GUI command: [Custom Rind](gui_hemisphere.md#guirindcustom)

Operations on *elts*: [Elements](tui_elements.md#tuielements2)

### Example

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

####### Rind Grid Test ##########

import hexablock

doc  = hexablock.addDocument ("Rind Grid Test")

# Simple Rind -----

nr = 4
na = 8
nh = 12

rind0 = doc.makeRindTop(nr, na, nh)
rind0.saveVtk("makeRindTop.vtk")

# Uniform Rind -----

center  = doc.addVertex (0, 0, 0)
vplan = doc.addVertex (0, 0, -0.5)
vx    = doc.addVector (1, 0, 0)
vz    = doc.addVector (0, 0, 1)
rtrou = 1
rint  = 8
rext  = 10
angle = 180

rind1 = doc.makeRindUni(center, vx, vz, rtrou, rint, rext, angle, vplan, nr, na, nh)
rind1.saveVtk("makeRindUni.vtk")

# Custom Rind -----

dr     = (rext-rtrou)/nr
dtheta = angle/na
dphi   = 180.0/nh
trad = []
tang = []
tphi = []

trad.append(rtrou)
for nro in range(nr+1):
  trad.append(rint + nro*dr)
  
for nro in range(na+1):
  tang.append(nro*dtheta)
  
for nro in range(nh+1):
  tphi.append(-90 + nro*dphi)

rind2 = doc.makeRind(center, vx, vz, trad, tang, tphi)
rind2.saveVtk("makeRind.vtk")
```

## Concentric (Spherical) Grid

### Simple Concentric

To create a Simple Concentric Grid in python mode, you need the following arguments:

- *nbLayers*: the number of nested hexahedra.
- *crit* : the criteria.

Use the function **makeSphericalTop**:

```python
elts = doc.makeSphericalTop(nbLayers, crit)
```

GUI command: [Simple Concentric (Spherical)](gui_hemisphere.md#guiconcentricsimple)

### Uniform Concentric

The following data are required:

- *center* : center coordinates of the concentric.
- *vx* : the base of the concentric (a vector).
- *vz* : the axis of the concentric (a vector).
- *rayon* : the radius.
- *nbLayers*: the number of nested hexahedra.
- *crit* : the criteria.

Use the function **makeSphericalUni** to make a uniform concentric:

```python
elts = doc.makeSphericalUni(center, vx, vz, rayon, nbLayers, crit)
```

GUI command: [Uniform Concentric (Spherical)](gui_hemisphere.md#guiconcentricuniform)

### Custom Concentric

The following data are required:

- *center* : center coordinates of the concentric.
- *vx* : the base of the concentric (a vector).
- *vz* : the axis of the concentric (a vector).
- *tr* : a list of radiuses in ascendant order.
- *crit* : the criteria.

Use the function **makeSpherical** to make a custom concentric grid:

```python
elts = doc.makeSpherical (center, vx, vz, tr, crit)
```

GUI command: [Custom Concentric (Spherical)](gui_hemisphere.md#guiconcentriccustom)

Operations on *elts*: [Elements](tui_elements.md#tuielements2)

### Example

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

####### Concentric (Spherical) Grid Test ##########

import hexablock

doc  = hexablock.addDocument ("Spherical Grid Test")

# Simple Spherical Grid -----

nbLayers = 3
crit = 0

grid0 = doc.makeSphericalTop(nbLayers, crit)
grid0.saveVtk("makeSphericalTop.vtk")

# Uniform Spherical Grid -----

center = doc.addVertex (0, 0, 10)
vx     = doc.addVector (1, 0, 0)
vz     = doc.addVector (0, 1, 1)
rayon  = 1

grid1 = doc.makeSphericalUni(center, vx, vz, rayon, nbLayers, crit);
grid1.saveVtk("makeSphericalUni.vtk")

# Custom Spherical Grid-----

tr = [10, 20, 30, 40] # a list of radiuses (one radius for each layer)

grid2 = doc.makeSpherical (center, vx, vz, tr, crit)
grid2.saveVtk("makeSpherical.vtk")
```
