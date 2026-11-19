<!-- source: https://docs.salome-platform.org/latest/gui/GEOM/geompy_doc/group__l3__3d__primitives.html -->

# Creating 3D Primitives geomBuilder Python module » All package methods, grouped by their purpose » Creating geometrical objects

## Detailed Description

## Function Documentation

### MakeBox()

```python
def MakeBox(self, x1, y1, z1, x2, y2, z2, theName = None)
```

Create a box by coordinates of two opposite vertices.

Parameters
:   |  |  |
    | --- | --- |
    | x1,y1,z1 | double values, defining first point it. |
    | x2,y2,z2 | double values, defining first point it. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created box.

[Example](../tui_primitives_page.md#tui_creation_box)

### MakeBoxDXDYDZ()

```python
def MakeBoxDXDYDZ(self, theDX, theDY, theDZ, theName = None)
```

Create a box with specified dimensions along the coordinate axes and with edges, parallel to the coordinate axes.

Center of the box will be at point (DX/2, DY/2, DZ/2).

Parameters
:   |  |  |
    | --- | --- |
    | theDX | Length of Box edges, parallel to OX axis. |
    | theDY | Length of Box edges, parallel to OY axis. |
    | theDZ | Length of Box edges, parallel to OZ axis. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created box.

[Example](../tui_primitives_page.md#tui_creation_box)

### MakeBoxTwoPnt()

```python
def MakeBoxTwoPnt(self, thePnt1, thePnt2, theName = None)
```

Create a box with two specified opposite vertices, and with edges, parallel to the coordinate axes.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1 | First of two opposite vertices. |
    | thePnt2 | Second of two opposite vertices. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created box.

[Example](../tui_primitives_page.md#tui_creation_box)

### MakeFaceHW()

```python
def MakeFaceHW(self, theH, theW, theOrientation, theName = None)
```

Create a face with specified dimensions with edges parallel to coordinate axes.

Parameters
:   |  |  |
    | --- | --- |
    | theH | height of Face. |
    | theW | width of Face. |
    | theOrientation | face orientation: 1-OXY, 2-OYZ, 3-OZX |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

[Example](../tui_topological_geom_objs_page.md#tui_creation_face)

### MakeFaceObjHW()

```python
def MakeFaceObjHW(self, theObj, theH, theW, theName = None)
```

Create a face from another plane and two sizes, vertical size and horisontal size.

Parameters
:   |  |  |
    | --- | --- |
    | theObj | Normale vector to the creating face or the face object. |
    | theH | Height (vertical size). |
    | theW | Width (horisontal size). |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created face.

[Example](../tui_topological_geom_objs_page.md#tui_creation_face)

### MakeDiskPntVecR()

```python
def MakeDiskPntVecR(self, thePnt, theVec, theR, theName = None)
```

Create a disk with given center, normal vector and radius.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Disk center. |
    | theVec | Vector, normal to the plane of the disk. |
    | theR | Disk radius. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created disk.

[Example](../tui_primitives_page.md#tui_creation_disk)

### MakeDiskThreePnt()

```python
def MakeDiskThreePnt(self, thePnt1, thePnt2, thePnt3, theName = None)
```

Create a disk, passing through three given points.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt1,thePnt2,thePnt3 | Points, defining the disk. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created disk.

[Example](../tui_primitives_page.md#tui_creation_disk)

### MakeDiskR()

```python
def MakeDiskR(self, theR, theOrientation, theName = None)
```

Create a disk with specified dimensions along OX-OY coordinate axes.

Parameters
:   |  |  |
    | --- | --- |
    | theR | Radius of Face. |
    | theOrientation | set the orientation belong axis OXY or OYZ or OZX |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created disk.

[Example](../tui_topological_geom_objs_page.md#tui_creation_face)

### MakeCylinder()

```python
def MakeCylinder(self, thePnt, theAxis, theR, theH, theName = None)
```

Create a cylinder with given base point, axis, radius and height.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Central point of cylinder base. |
    | theAxis | Cylinder axis. |
    | theR | Cylinder radius. |
    | theH | Cylinder height. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created cylinder.

[Example](../tui_primitives_page.md#tui_creation_cylinder)

### MakeCylinderA()

```python
def MakeCylinderA(self, thePnt, theAxis, theR, theH, theA, theName = None)
```

Create a portion of cylinder with given base point, axis, radius, height and angle.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Central point of cylinder base. |
    | theAxis | Cylinder axis. |
    | theR | Cylinder radius. |
    | theH | Cylinder height. |
    | theA | Cylinder angle in radians. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created cylinder.

[Example](../tui_primitives_page.md#tui_creation_cylinder)

### MakeCylinderRH()

```python
def MakeCylinderRH(self, theR, theH, theName = None)
```

Create a cylinder with given radius and height at the origin of coordinate system.

Axis of the cylinder will be collinear to the OZ axis of the coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | theR | Cylinder radius. |
    | theH | Cylinder height. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created cylinder.

[Example](../tui_primitives_page.md#tui_creation_cylinder)

### MakeCylinderRHA()

```python
def MakeCylinderRHA(self, theR, theH, theA, theName = None)
```

Create a portion of cylinder with given radius, height and angle at the origin of coordinate system.

Axis of the cylinder will be collinear to the OZ axis of the coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | theR | Cylinder radius. |
    | theH | Cylinder height. |
    | theA | Cylinder angle in radians. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created cylinder.

[Example](../tui_primitives_page.md#tui_creation_cylinder)

### MakeSpherePntR()

```python
def MakeSpherePntR(self, thePnt, theR, theName = None)
```

Create a sphere with given center and radius.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Sphere center. |
    | theR | Sphere radius. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created sphere.

[Example](../tui_primitives_page.md#tui_creation_sphere)

### MakeSphere()

```python
def MakeSphere(self, x, y, z, theR, theName = None)
```

Create a sphere with given center and radius.

Parameters
:   |  |  |
    | --- | --- |
    | x,y,z | Coordinates of sphere center. |
    | theR | Sphere radius. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created sphere.

[Example](../tui_primitives_page.md#tui_creation_sphere)

### MakeSphereR()

```python
def MakeSphereR(self, theR, theName = None)
```

Create a sphere with given radius at the origin of coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | theR | Sphere radius. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created sphere.

[Example](../tui_primitives_page.md#tui_creation_sphere)

### MakeCone()

```python
def MakeCone(self, thePnt, theAxis, theR1, theR2, theH, theName = None)
```

Create a cone with given base point, axis, height and radiuses.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Central point of the first cone base. |
    | theAxis | Cone axis. |
    | theR1 | Radius of the first cone base. |
    | theR2 | Radius of the second cone base. |

Note
:   If both radiuses are non-zero, the cone will be truncated.
:   If the radiuses are equal, a cylinder will be created instead.

Parameters
:   |  |  |
    | --- | --- |
    | theH | Cone height. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created cone.

[Example](../tui_primitives_page.md#tui_creation_cone)

### MakeConeR1R2H()

```python
def MakeConeR1R2H(self, theR1, theR2, theH, theName = None)
```

Create a cone with given height and radiuses at the origin of coordinate system.

Axis of the cone will be collinear to the OZ axis of the coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | theR1 | Radius of the first cone base. |
    | theR2 | Radius of the second cone base. |

Note
:   If both radiuses are non-zero, the cone will be truncated.
:   If the radiuses are equal, a cylinder will be created instead.

Parameters
:   |  |  |
    | --- | --- |
    | theH | Cone height. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created cone.

[Example](../tui_primitives_page.md#tui_creation_cone)

### MakeTorus()

```python
def MakeTorus(self, thePnt, theVec, theRMajor, theRMinor, theName = None)
```

Create a torus with given center, normal vector and radiuses.

Parameters
:   |  |  |
    | --- | --- |
    | thePnt | Torus central point. |
    | theVec | Torus axis of symmetry. |
    | theRMajor | Torus major radius. |
    | theRMinor | Torus minor radius. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created torus.

[Example](../tui_primitives_page.md#tui_creation_torus)

### MakeTorusRR()

```python
def MakeTorusRR(self, theRMajor, theRMinor, theName = None)
```

Create a torus with given radiuses at the origin of coordinate system.

Parameters
:   |  |  |
    | --- | --- |
    | theRMajor | Torus major radius. |
    | theRMinor | Torus minor radius. |
    | theName | Object name; when specified, this parameter is used for result publication in the study. Otherwise, if automatic publication is switched on, default value is used for result name. |

Returns
:   New [GEOM.GEOM_Object](interfaceGEOM_1_1GEOM__Object.md), containing the created torus.

[Example](../tui_primitives_page.md#tui_creation_torus)
