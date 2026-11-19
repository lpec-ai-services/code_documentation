<!-- source: https://docs.salome-platform.org/latest/gui/HEXABLOCK/tui_blocks_for_cyl_pipe.html -->

# Cylinders and Pipes Construction

## Cylinder

### Simple Cylinder

To make a simple cylinder grid in python mode, the following data are required:

- *nbR* : number of hexahedra on radial.
- *nbA* : number of hexahedra along the perimeter of the cylinder.
- *nbH* : number of hexahedra along the axis of the cylinder.

Use the function **makeCyinderTop**:

```python
elts = doc.makeCylinderTop(nbR, nbA, nbH)
```

GUI command: [Simple Cylinder](gui_blocks_for_cyl_pipe.md#guicylindersimple)

### Uniform Cylinder

The following data are required:

- *origin* : origin’s coordinates of the cylinder (select a vertex).
- *vx* : the base of the cylinder (select a vector).
- *vz* : the axis of the cylinder (select a vector).
- *rint* : the radius of the hole in the cylinder .
- *rext* : the radius of the cylinder.
- *angle* : angle of the cylinder around the Z axis.
- *hauteur*: the height of the cylinder.
- *nbR* : number of hexahedra on radial.
- *nbA* : number of hexahedra along the perimeter of the cylinder.
- *nbH* : number of hexahedra along the axis of the cylinder.

Use the function **makeCylinderUni** to make a uniform cylinder:

```python
elts = doc.makeCylinderUni(origin, vx, vz, rint, rext, angle, hauteur, nbR, nbA, nbH)
```

GUI command: [Uniform Cylinder](gui_blocks_for_cyl_pipe.md#guicylinderuniform)

### Custom Cylinder

The following data are required:

- *origin* : origin’s coordinates of the cylinder (select a vertex).
- *vx* : the base of the cylinder (select a vector).
- *vz* : the axis of the cylinder (select a vector).
- *tr* : a list of radiuses in ascendant order.
- *ta* : a list of angles in ascendant order.
- *th* : a list of heights in ascendant order.

Use the function **makeCylinder** to make a custom cylinder:

```python
elts = doc.makeCylinder(origin, vx, vz, tr, ta, th)
```

GUI command: [Custom Cylinder](gui_blocks_for_cyl_pipe.md#guicylindercustom)

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

####### Make Cylinder Test ########## 

import hexablock

# Simple Cylinder -----

doc  = hexablock.addDocument ("Make Cylinder Test")

nbR = 8
nbA = 10
nbH = 8

cylinder0 = doc.makeCylinderTop (nbR, nbA, nbH)
cylinder0.saveVtk ("makeCylinderTop.vtk")
   
# Uniform Cylinder -----

origin = doc.addVertex (0, 0, 5)
vx     = doc.addVector (1, 0, 0)
vz     = doc.addVector (0, 0, 1)
rint   = 2
rext   = 4
angle  = 300
hauteur = 1

cylinder1 = doc.makeCylinderUni (origin, vx, vz, rint, rext, angle, hauteur, nbR, nbA, nbH)
cylinder1.saveVtk ("makeCylinderUni.vtk")

# Custom Cylinder

origin = doc.addVertex (5, 0, 0)
tr = [10, 20, 30, 40]
ta = [45, 90, 135, 180, 225]
th = [5, 30, 40, 60]

cylinder2 = doc.makeCylinder(origin, vx, vz, tr, ta, th)
cylinder2.saveVtk("makeCylinder.vtk")
```

## Make Cylinders

To make **two cylinders in T shape** the following data are required for each cylinder:

- *orig* : the origin of the cylinder (select a vertex).
- *vz* : the axis of the cylinder (select a vector).
- *rext* : the radius of the cylinder.
- *h* : the height of the cylinder.

*One of the two cylinders must be bigger than the other.*

Use the function **makeCylinders**:

```python
elts = doc.makeCylinders (orig1, vz1, rext1, h1, orig2, vz2, rext2, h2)
```

GUI command: [Cylinders](gui_blocks_for_cyl_pipe.md#guicylinders)

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

####### Make Cylinders Test ########## 

import hexablock
import math

    
doc  = hexablock.addDocument ("Make Cylinders Test")

rext1 =  2*math.sqrt (2.0)
rext2 =  3*math.sqrt (2.0)
h1   =  16
h2   =  16
xl1  =  -8

orig1  = doc.addVertex ( 0, 0,  xl1)
orig2  = doc.addVertex (-8, 0,  0)
vz1   = doc.addVector ( 0, 0,  1)
vz2   = doc.addVector ( 1, 0,  0)
   
cylinders = doc.makeCylinders (orig1, vz1, rext1, h1, orig2, vz2, rext2, h2)
cylinders.saveVtk("makeCylinders.vtk")
```

## Pipe

### Simple Pipe

To make a simple pipe grid in python mode, the following data are required:

- *nbR* : number of hexahedra on radial.
- *nbA* : number of hexahedra along the perimeter of the pipe.
- *nbH* : number of hexahedra along the axis of the pipe.

Use the function **makePipeTop**:

```python
elts = doc.makePipeTop(nbR, nbA, nbH)
```

GUI command: [Simple Pipe](gui_blocks_for_cyl_pipe.md#guipipesimple)

### Uniform Pipe

The following data are required:

- *origin* : the origin’s coordinates of the pipe (select a vertex).
- *vx* : the base of the pipe (select a vector).
- *vz* : the axis of the pipe (select a vector).
- *rint* : the radius of the hole in the pipe .
- *rext* : the radius of the pipe.
- *angle* : angle of the pipe around the Z axis.
- *hauteur*: the height of the pipe.
- *nbR* : number of hexahedra on radial.
- *nbA* : number of hexahedra along the perimeter of the pipe.
- *nbH* : number of hexahedra along the axis of the pipe.

Use the function **makePipeUni** to make a uniform pipe:

```python
elts = doc.makePipeUni(origin, vx, vz, rint, rext, angle, hauteur, nbR, nbA, nbH)
```

GUI command: [Uniform Pipe](gui_blocks_for_cyl_pipe.md#guipipeuniform)

### Custom Pipe

The following data are required:

- *origin* : origin’s coordinates of the pipe (select a vertex).
- *vx* : the base of the pipe (select a vector).
- *vz* : the axis of the pipe (select a vector).
- *tr* : a list of radiuses in ascendant order.
- *ta* : a list of angles in ascendant order.
- *th* : a list of heights in ascendant order.

Use the function **makePipe** to make a custom pipe:

```python
elts = doc.makePipe(origin, vx, vz, tr, ta, th)
```

GUI command: [Custom Pipe](gui_blocks_for_cyl_pipe.md#guipipecustom)

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

####### Make Pipe Test ########## 

import hexablock
        
doc  = hexablock.addDocument ("Make Pipe Test")

# Simple Pipe -----

nbR = 8
nbA = 10
nbH = 8

pipe0 = doc.makePipeTop (nbR, nbA, nbH)
pipe0.saveVtk ("makePipeTop.vtk")

# Uniform Pipe -----

orig = doc.addVertex (0, 0, 0)
vx   = doc.addVector (1, 0, 0)
vz   = doc.addVector (0, 0, 1)
rint = 1
rext = 3
angle = 360
hauteur = 2

pipe1 = doc.makePipeUni (orig, vx, vz, rint, rext, angle, hauteur, nbR, nbA, nbH)
pipe1.saveVtk ("makePipeUni.vtk");
   

# Custom Pipe -----

origin = doc.addVertex (0, 5, 0)
tr = [10, 20, 30, 40]
ta = [45, 90, 135, 180, 225]
th = [5, 30, 40, 60]

pipe2 = doc.makePipe(origin, vx, vz, tr, ta, th)
pipe2.saveVtk("makePipe.vtk")
```

## Make Pipes

To make **two pipes in T shape** the following data are required for each pipe:

- *orig* : the origin of the pipe (select a vertex).
- *vz* : the axis of the pipe (select a vector).
- *rint* : the internal radius of the pipe.
- *rext* : the radius of the pipe.
- *h* : the height of the pipe.

*One of the two pipes must be bigger than the other.*

Use the function **makepipes**:

```python
elts = doc.makePipes(orig1, vz1, rint1, rext1, h1, orig2, vz2, rint2, rext2, h2)
```

GUI command: [Pipes](gui_blocks_for_cyl_pipe.md#guipipes)

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

####### Make Pipes Test ########## 

import hexablock
import math

    
doc  = hexablock.addDocument ("Make Pipes Test")

rext1 =  2*math.sqrt (2.0)
rext2 =  3*math.sqrt (2.0)
rint1 =  rext1/2
rint2 =  rext1
h1   =  16
h2   =  16
xl1  =  -8

orig1  = doc.addVertex ( 0, 0,  xl1)
orig2  = doc.addVertex (-8, 0,  0)
vz1   = doc.addVector ( 0, 0,  1)
vz2   = doc.addVector ( 1, 0,  0)
   
pipes = doc.makePipes (orig1, vz1, rint1, rext1, h1, orig2, vz2, rint2, rext2, h2);
pipes.saveVtk("makePipes.vtk")
```
