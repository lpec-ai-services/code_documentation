# GEOMETRY DEFINITIONS
<!-- source PDF pages 47-118 -->

<!-- page 47 -->
Chapter 7
GEOMETRY DEFINITIONS
A geometry command is introduced by the keyword GEOMETRY and ends with the keyword ENDGEOM. Volume definitions corresponding
to the given geometry are placed between these two keywords.
IMPORTANT: The whole geometry must be convex. If the geometry is not convex, some particles may prematurely be lost and
some scores may be underestimated. Note that, by default, there is no check on convexity or connectedness of the geometry. This
may be performed using the CHECK_GEOM option (see 7.13.2).
Boundary conditions are defined after the geometry definition, in the BOUNDARY_CONDITION command.
For complex cases (lattices etc.), it may be necessary to review this section twice in order to clearly understand the cross-references.
Recommendations:
The particularities of the geometrical operators need to be taken into account:
• a lattice cannot be rotated : it must be aligned with the axis of the reference frame.
The particularities of the other commands are important (detailed below):
• BOUNDARY_CONDITION: the boundary conditions are given on a side or a surface of a volume. Important: Only the sides
associated with the TYPE (combinatorial geometry) or surfaces SURF (surface-based geometry) explicitly included in the
definition can identify a surface associated with the volume. In particular, when a first volume is modified by an operator
(SMASH, VMINUS, INTE and UNION) and a second volume (as argument), the first volume will not know the sides or surfaces
of the second after the operation;
• SCORE: a surface-based score is defined at the interface between two volumes and not at the side or surface of a volume;
• SOURCES_LIST: for a point source, the angular distribution is defined with respect to a spherical reference frame whose Z
axis is the Z axis of the global geometry reference frame;
The choice between a combinatorial or a surface-based geometry is not without consequences in the running time of the simulation.
Some advice concerning the optimal choices that can be made are given at the end of this section.
A number of error diagnostics are implemented in combinatorial geometries to avoid errors in the definitions, but it is indispensable
, in complex cases, to verify by graphical display that the geometry given to the code corresponds to the user intentions. It
should be noted that geometry errors can also be detected if automatic biasing takes place (see, below). It is therefore sometimes
advisable to launch a dry run with biasing, just to verify the geometry, with no connection to the actual calculation.
In this section, we consider the following points in detail:

<!-- page 48 -->
• Different ways of defining volumes
Volumes can be defined in five different ways: combinatorial, surface-based, through repetition of simple volumes, through
replacement of cells of a lattice, or through rotation of simple volumes;
• Defining data for combinatorial geometries
The shape data, introduced by the keyword TYPE, is the basic component of a geometrical definition in combinatorial form;
• Surface-Based data definition
Surface-based data, introduced by the keyword SURF, is the basic component of a geometrical definition in surface-based
form;
• Simple volume definition.
Volume definitions, introduced by the keyword VOLU, on the basis of types (combinatorial) or surfaces (surface-based);
• Rotation-type volume definition;
• Definition of different operators acting on volumes;
• Definition of lattice-type volumes;
• Definition of cell or sub-cell type volumes;
• Syntax of a display request (2D-cross section view).

<!-- page 49 -->
## 7.1 GEOMETRICAL ACCURACY

Note: Lengths are expressed in centimeters and angles are expressed in degrees in the geometry.
The accuracy used in calculating distances is εgeo = 10−4 cm. In order to find out which volume will be entered next, the code
temporarily advances the particle position by a value of εgeo cm along the particle line of flight.
It is, therefore, pointless to attempt to create a volume with a length less than this threshold, particularly in an attempt to impose a
boundary condition.
Precision is, however, required for entering coefficients that define the volume.

<!-- page 50 -->
## 7.2 GLOBAL STRUCTURE

The whole geometry is defined in a Cartesian reference frame of origin O and axes OX, OY and OZ.
The structure command is as follows:
GEOMETRY
TITLE title
*
TYPE num(type)
Definition for type num(type)
...
*
SURF num(surf)
Definition for surface num(surf)
...
VOLU num(volu)
Definition for volume num(volu)
ENDV
...
POSITION x y z
COLOR
Colormap
GRAPH
Data on 2D-cut
ENDGEOM
where:
• title is any chain of characters (a maximum of 256);
• as many TYPE, SURF, and VOLU as desired;
• VOLU defined for a TYPE or a SURF that already exists;
• any numbering for num(type), num(surf), and num(volu), but num(volu) must not begin with a “0”;
• assignment of colors to volumes (these assignments are used for 2D-cross sectional views declared after the association is
made). It is possible to change the colors of the different views. In such cases, it is necessary to make as many COLOR
commands as required (see 7.12.1);
• one (or more) 2D-views, i.e., geometrical 2D-views.
It is possible to request the position of a point (x,y,z) using POSITION x y z: in this case, the code returns the volume where the
point is located at the time the request is made (which is not necessarily at the end of construction. The current position may also
be requested). The code states the cell in the case of a lattice, and the number of the side if the point is on a numbered surface (for
boundary conditions, see the corresponding section).

<!-- page 51 -->
## 7.3 DIFFERENT WAYS TO DEFINE VOLUMES

A TRIPOLI-4® geometry corresponds to an ensemble of volumes.
In this version, there are five possible kinds of volumes, the first two correspond to “simple” volumes, the third is used to create
volumes by rotation and the last two relate to the possibilities available with lattices.
It is possible to mix combinatorial and surface-based geometries. A volume created from surfaces may also be introduced into the
cell of a lattice (but the cell used to create the lattice must be COMBI, RESC, or RESH).

### 7.3.1 COMBINATORIAL GEOMETRY

A first option consists of creating volumes using predetermined geometrical shapes. These are introduced by the keyword COMBI.
The TYPE for these volumes must have been previously declared in the data. The type corresponds to a predetermined geometrical
shape (sphere, cylinder, box, etc.) plus descriptive data (for instance, for a sphere, a type is obtained by setting its radius).

### 7.3.2 SURFACE-BASED GEOMETRY

A second possibility is to specify the volumes using equations. They are introduced by the keyword EQUA. These volumes are
defined in terms of equations of surfaces (SURF), which must have been previously declared, setting the boundary of the volume
and the position of the volume with respect to the surface (the process used for TRIPOLI-2 and TRIPOLI-3.)
Geometry error diagnostics are not available in this type of definition (no overlap tests done by default).

### 7.3.3 DEFINITION USING A ROTATION

There is a third possibility, consisting of creating volumes using a rotation operator with a predetermined volume. These volumes
are introduced by the keyword ROTATION.

### 7.3.4 DEFINING A LATTICE

The final method consists of repeating a pre-existing volume in order to create a lattice. This volume thus constitutes the reference
cell. Only orthorhombic lattices (i.e. parallelepipedic) and hexagonal lattices are implemented. The reference volume has:
• either a parallelepipedic shape (BOX or PARALLELEPIPEDE) repeated using the RESC operator along the three axes of the
parallelepiped;
• or one of the hexagonal shapes HEXAX, HEXAY, or HEXAZ: in which case it is repeated using the operator RESH.

### 7.3.5 REDEFINING A CELL

Once the lattice is created, it is possible to redefine, for a specific cell, all or part of the volumes comprising it. This is accomplished
using the keyword CELL and specifying the volume to be replaced. In this case, the code itself creates a volume with the
characteristics (shape and center) of the volume to be replaced. It is possible to replace a volume of the COMBI type only in this
manner (see example in Appendix 2).
In the case of a lattice of lattices, it is also possible to exclude a specific cell from a lattice that is itself contained in a specific cell
of a sub-lattice. This is effected using the keyword LOWER_CELL and specifying the volumes, cells, and lattices involved. Again, it
is possible to replace a volume of the COMBI type only in this manner.

<!-- page 52 -->
### 7.3.6 OPERATORS, VIRTUAL VOLUMES, AND SYNTAX FOR A VOLUME

A volume can be specified with respect to other volumes in the event of intersection (or union) using the operators SMASH, VMINUS,
INTE, and UNION.
Operators can be introduced for volumes that are defined by surfaces.
In addition, a volume can have the attribute FICTIVE. In this case, the volume is virtual and is only used as an
argument for operators, thus making it possible to modify the volumes during definition, or to override part
of a volume (see below). In no case can a point in a geometry be specified as belonging to a virtual volume.
A simple example is given to illustrate the UNION case.
Note: Operators are covered in this document before lattices, as it is important to clearly understand the
concept of overriding (operator SMASH).
The general form of a volume definition is as follows:
VOLU
num(volu)
<VOL_DEF>
Volume description data
<OPERATOR_NAME(1)>
Operator 1 data
...
<OPERATOR_NAME(n)>
Operator n data
FICTIVE
VOL_EXCEPT
ENDV
where:
• num(volu) is the volume number. It will be used as the volume identifier in the rest of the input file.
This number must not begin with a “0”;
• <VOL_DEF> is one of the following keywords: COMBI, EQUA, RESC, RESH, CELL, LOWER_CELL, or
ROTATION, depending on the mode of representation selected;
• <OPERATOR_NAME(i)> corresponds to one of the following keywords: SMASH, VMINUS, INTE, or UNION;
• FICTIVE indicates that the volume is virtual and is only used for purposes of modifying other volumes;
• VOL_EXCEPT indicates, if the volume belongs to the lattice, that it would be excluded for a set of cells
(refer to 7.10.7.4, page 91 for information on when to use this option).
We will now consider how to specify the types and surfaces necessary for creating a simple volume.

<!-- page 53 -->
## 7.4 DEFINING A TYPE

A type is a geometrical element used in a combinatorial definition (COMBI) of a volume. It consists of a shape
and some additional descriptive data. Each type is associated with a specific number (integer). Any number
can be used: the order is not important and skips in the numbering are allowed.
Note: A type can be defined at any time in the GEOMETRY module but must always precede the definition of a
volume using it.
The declaration is made using the keyword TYPE, as follows:
TYPE
num(type)
<SHAPE>
Descriptive data
The type number num(type) is arbitrary and can be chosen by the user. It will be used as the type identifier
in the rest of the input file.
The value of <SHAPE> is a geometry keyword, which may be one of the following:
• SPHERE;
• CYLX, CYLY or CYLZ (cylinder whose axis is parallel to an axis of the reference frame);
• CYL (any cylinder);
• BOX (parallelepiped along X, Y and Z);
• CONE ;
• HEXAX, HEXAY or HEXAZ (hexagonal prism whose axes are parallel to an axis of the reference frame);
• PARALLELEPIPEDE (any);
• TORUS.
For all of the shapes allowed, we list the data needed to define a type and indicate their meanings.

### 7.4.1 SPHERES

SPHERE r
r is the radius of the sphere.

<!-- page 54 -->
### 7.4.2 BOXES

BOX hx hy hz
hx, hy, hz are the lengths of the sides of the box (hx parallel to OX etc.)

<!-- page 55 -->
X
Y
Z
hz
hy
hx
Figure 7.1: The BOX type

### 7.4.3 CYLINDERS PARALLEL TO AN AXIS

CYLX r h
2 or
CYLY r h
2 or
CYLZ r h
2
r is the radius of the cylinder
h is the height of the cylinder (h/2 half-height).
The cylinder is parallel to OX, OY or OZ.

### 7.4.4 GENERIC CYLINDERS

h
u
X
Y
Z
Figure 7.2: The CYL type

<!-- page 56 -->
CYL r h
2 ux uy uz
r is the radius of the cylinder
h is the height of the cylinder (h/2 half-height).
ux, uy, uz are the components in the geometry reference frame of a vector (not necessarily a unit vector) giving
the direction of the axis of the cylinder.

### 7.4.5 CONES

CONE θ ux uy uz
θ is the angle (in degrees) of the apex of the cone.
ux, uy, uz are the coordinates in the geometry reference frame of a vector (not necessary a unit vector) giving
the direction of the axis of the cone, oriented from the apex to the base.
Note: The cone is the only TYPE that is not of a bounded volume, as the base of the cone is only determined
when the VOLU command is input. When using the VOLU command, only the height of the cone needs to be
given (the base being orthogonal to the axis).
X
Y
Z
u
θ
Figure 7.3: The CONE type

<!-- page 57 -->
### 7.4.6 GENERIC PARALLELEPIPEDS

PARALLELEPIPEDE
Lu Lv Lw
ux uy uz
vx vy vz
wx wy wz
A parallelepiped is defined using three unit vectors u, v, and w (not necessary orthogonal or normalized).
The values Lu , Lv, and Lw give the lengths of the sides along the vectors that define the parallelepiped.
Y
X
Z
w
u
v
Lu
Lw
Lv
Figure 7.4: The PARALLELEPIPEDE type

### 7.4.7 HEXAGONAL PRISMS

HEXAX or HEXAY or HEXAZ
diameter
height
θ
A HEXA[XYZ] is a hexagonal prism with an X, Y, or Z axis, depending on the keyword chosen. The diameter
is that of the circle inscribed in the hexagon used to construct the prism. It is also the distance between two
sides parallel to the axis (D in the drawing below), the height (h in the drawing) is the dimension of the prism
along the axis and θ is an angle indicating the orientation of the hexagon. Currently, it can only be 0 or 90.
• In the case of a HEXAX, angle θ is “0” if the prism has two planes parallel to plane OZX and “90” if it
contains two planes parallel to plane OYX;

<!-- page 58 -->
• In the case of a HEXAY, angle θ is “0” if the prism has two planes parallel to plane OXY and “90” if it
contains two planes parallel to plane OZY;
• In the case of a HEXAZ, angle θ is “0” if the prism has two planes parallel to plane OYZ and “90” if it
contains two planes parallel to plane OXZ.
X
Y
Z
D
h
Figure 7.5: The HEXAZ type with θ = 0

### 7.4.8 TORI

TORUS
ux uy uz
R
r
where:
• the values ux, uy, and uz are the components in the geometry reference frame of a vector (not necessarily
a unit vector) giving the direction of the axis of the torus;
• R is the major radius, as shown in the following sketch,
• r is the minor radius, as shown.

<!-- page 59 -->
X
Y
Z
R
r
u
Figure 7.6: The data of the TORUS type

## 7.5 SURFACE DATA DEFINITIONS

A surface is declared using the keyword SURF in the following syntax:
SURF
num(surf)
<SURFNAME>
TRANSFORM transformation_identifier
Descriptive data
The number of the surface num(surf) is arbitrarily chosen by the user. It will be used as the surface identifier
in the rest of the input file. A surface can be declared at any time, but its definition must precede its use
for a volume.
An optional keyword TRANSFORM with a transformation identifier can be specified. The transformation must
have been declared anywhere before in the geometry (see 7.5.16).
The surfaces recognized by the geometry are:
• PLANEX, PLANEY, or PLANEZ (planes parallel to planes of the geometry reference frame);
• PLANE(general);
• SPHERE;
• CYLX, CYLY, or CYLZ (cylinders with axes parallel to the axes of the geometry reference frame);

<!-- page 60 -->
• CONEX, CONEY or CONEZ (cones with axes parallel to the axes of the geometry reference frame);
• TORUSX, TORUSY or TORUSZ (torus with axes parallel to the axes of the geometry reference frame);
• QUAD (generic quadratics).
Each of the preceding surfaces divides the space into two regions: a positive region and a negative region.
This property is used to define volumes of the EQUA type (surface-based).
In the following, we will give, for each type of surface, the appropriate keyword, the data required, as well as
the relevant explanations. The sign convention for determining the position of a point relative to the surface
is also indicated.

### 7.5.1 PLANE PARALLEL TO (OY,OZ)

PLANEX x0
x0 is the location of the plane.
A point P = (x,y,z) is in the positive region if x > x0.

### 7.5.2 PLANE PARALLEL TO (OX,OZ)

PLANEY y0
y0 is the location of the plane.
A point P = (x,y,z) is in the positive region if y > y0.

### 7.5.3 PLANE PARALLEL TO (OX,OY)

PLANEZ z0
z0 is the location of the plane.
A point P = (x,y,z) is in the positive region if z > z0.

<!-- page 61 -->
X
Y
Z
z=z0
Figure 7.7: Example of a plane PLANEZ parallel to plane (Ox,Oy).

### 7.5.4 GENERIC PLANES

PLANE a b c d
a, b, c, and d are such that the equation of the defined plane is:
ax+by+cz+d = 0.
A point P = (x,y,z) is in the positive region if ax+by+cz+d > 0.

### 7.5.5 SPHERES

SPHERE x0 y0 z0 R
(x0,y0,z0) are the coordinates of the center of a sphere in the geometry reference frame, and R is the radius of
the sphere.
A point P = (x,y,z) is in the positive region if it is outside the sphere.

### 7.5.6 A CYLINDER THAT IS PARALLEL TO AXIS OX

CYLX y0 z0 R

<!-- page 62 -->
(y0,z0) are the coordinates of a point on the axis of the cylinder in the (OY,OZ) reference frame, and R is the
radius of the cylinder.
A point P = (x,y,z) is in the positive region if it is outside the cylinder.

### 7.5.7 A CYLINDER THAT IS PARALLEL TO AXIS OY

CYLY x0 z0 R
(x0,z0) are the coordinates of a point on the axis of the cylinder in the (OX,OZ) reference frame, and R is the
radius of the cylinder.
A point P = (x,y,z) is in the positive region if it is outside the cylinder.

### 7.5.8 A CYLINDER THAT IS PARALLEL TO AXIS OZ

CYLZ x0 y0 R
(x0,y0) are the coordinates of a point on the axis of the cylinder in the (OX,OY) reference frame, and R is the
radius of the cylinder.
A point P = (x,y,z) is in the positive region if it is outside the cylinder.

### 7.5.9 A CYLINDER WITH A GENERIC AXIS

CYL x0 y0 z0 R ux uy uz
(x0,y0,z0) are the coordinates of a point on the axis of the cylinder and R is the radius of the cylinder. The
axis of the cylinder is given by ux, uy, uz.
A point P = (x,y,z) is in the positive region if it is outside the cylinder.

### 7.5.10 A CONE WHOSE AXIS IS PARALLEL TO AXIS OX

CONEX x0 y0 z0 θ
(x0,y0,z0) are the coordinates of the apex of the cone; θ is half the apex angle.
A point P = (x,y,z) is in the positive region if it is outside the cone.

<!-- page 63 -->
### 7.5.11 A CONE WHOSE AXIS IS PARALLEL TO AXIS OY

CONEY x0 y0 z0 θ
(x0,y0,z0) are the coordinates of the apex of the cone; θ is half the apex angle. A point P = (x,y,z) is in the
positive region if it is outside the cone.

### 7.5.12 A CONE WHOSE AXIS IS PARALLEL TO AXIS OZ

CONEZ x0 y0 z0 θ
(x0,y0,z0) are the coordinates of the apex of the cone; θ is half the apex angle. A point P = (x,y,z) is in the
positive region if it is outside the cone.

### 7.5.13 A CONE WITH A GENERIC AXIS

CONE x0 y0 z0 θ ux uy uz
(x0,y0,z0) are the coordinates of the apex of the cone; θ is half the apex angle. The axis of the cone is given
by ux, uy, uz.

### 7.5.14 AN ELLIPTIC TORUS

• whose axis is parallel to axis OX
TORUSX x0 y0 z0 R a b
• whose axis is parallel to axis OY
TORUSY x0 y0 z0 R a b
• whose axis is parallel to axis OZ

<!-- page 64 -->
TORUSZ x0 y0 z0 R a b
with :
(x0, y0, z0) : center coordinates of the torus;
R
: main radius (also called ring radius) (circular);
a
: semiaxis of the circular or elliptical section, perpendicular to⃗R;
b
: semiaxis of the circular or elliptical section, parallel to⃗R;
M (x0, y0, z0)
R
a
b
Figure 7.8: Schematic of the torus.
Thus, if a = b, the section is circular, otherwise the section is elliptical. It is authorized to choose b > R, the
resulting volume can be seen as an apple. A point P=(x,y,z) is in the positive region if it is outside the torus.
-50
0
50
100
150
200
250
50
100
150
200
250
300
350
150
200
250
300
350
400
450
-50
0
50
100
150
200
250
50
100
150
200
250
300
350
150
200
250
300
350
400
450
Figure 7.9: Examples of elliptical torus, with a > b (left figure), and b > R (right figure).

<!-- page 65 -->
### 7.5.15 GENERIC QUADRATIC SURFACE

QUAD a b c d e f g h i j
a, b, c, d, e, f, g, h, i, j are the coefficients of the quadric equations:
ax2 +by2 +cz2 +dxy+eyz+ fxz+gx+hy+iz+ j = 0.
A point P=(x,y,z) is in the positive region if ax2 +by2 +cz2 +dxy+eyz+ fxz+gx+hy+iz+ j > 0.

### 7.5.16 SURFACE TRANSFORMATION

A surface transformation is available applicable on all types of surface. It must be given in the form of a
unitary matrix transformation and a change of origin.
TRANSFORM
transformation_identifier
MATRIX
x0 y0 z0
m11 m12 m13
m21 m22 m23
m31 m32 m33
The transformation is done to the point in the space before checking if the implicit equation is verified. If you
want the transformation to be done on the object, you have to give the matrix of the inverse transformation.
For example, the following declarations are equivalent
TRANSFORM 2
MATRIX
-2
0
0
0
1
0
-1
0
0
0
0
1
SURF 1 TRANSFORM 2 SPHERE 4 0 0 16
and
SURF 1 SPHERE -2 -6 0 16

<!-- page 66 -->
## 7.6 DEFINING SIMPLE VOLUMES

It should be noted that all volume definitions should take the following form (exluding operators with other
volumes and the virtual attribute):
VOLU
num(volu)
...
ENDV
where num(volu) is the number of the volume being defined.
A simple volume can be defined in two ways:
• combinatorial, mainly used for repetitive geometries (a single type is defined to create as many volumes
as required).
In certain cases, it is necessary to define virtual volumes (e.g., in the case of sectors) to cut the real
volumes. On the other hand, it is then not possible to set boundary conditions on a virtual surface.
Numerous consistency tests are available in this case (overlap testing, etc.).
• surface-based, adapted to geometries in which certain dimensions are often modified (depth of critical
solution, for example). In the case of a combinatorial geometry, it is necessary to recenter the volumes
for each calculation. The choice of a surface-based geometry usually allows faster execution than an
equivalent combinatorial case involving a large number of operators. Unfortunately, there is no way to
assure that the geometry is properly defined. It is entirely up to the user to define a consistent geometry
(note that it is possible to request automatic biasing to provide some degree of testing).

### 7.6.1 DEFINING SIMPLE VOLUMES USING PREDETERMINED TYPES

A simple volume is defined on the basis of a type as follows:
VOLU
num(volu)
COMBI
num(type)
Additional data on volume
ENDV
where:
• num(volu) is the number of the volume being defined;
• num(type) is the number of the type (from a previously set) of the volume being defined.
The additional data concerning volume are identical for all types, exception cones. Cones are a special case
and require some additional data.

<!-- page 67 -->
#### 7.6.1.1 Sphere, cylinder with axis parallel to Ox, cylinder with axis parallel to Oy, cylinder with axis parallel to Oz, box

Such volumes can be defined using types as follows:
VOLU
num(volu)
COMBI
num(type)
cx cy cz
#
V_ORIGIN num(vol-orig)
#
M_ORIGIN
ni nj nk
LATTICE numres
ENDV
where:
• (cx,cy,cz) are the coordinates of the center of the volume;
• V_ORIGIN num(vol-orig) means that the coordinates (cx,cy,cz) are given with respect to the center of
the volume num(vol-orig) (or the apex in the case of a cone), and not with respect to the origin O of
the reference frame;
• M_ORIGIN (ni,nj,nk) LATTICE numres means that the coordinates (cx,cy,cz) are given with respect
to the center of the cell (ni,nj,nk) of the lattice volume numres (see below).
Example:
TYPE 3 BOX 4 4 4
VOLU 7 COMBI 3 -2.
0.
0.
ENDV
VOLU 9 COMBI 3 4.
0.
0.
V_ORIGIN 7 ENDV
Two volumes (7 and 9) are built from a cube with 4 cm sides (TYPE 3). Volume 7 is centered at (−2,0,0) and
volume 9, positioned with respect to the center of 7, is centered at (2,0,0) = (4,0,0)+(−2,0,0). Thus, by
changing the coordinates of 7, volume 9 is also moved.

<!-- page 68 -->
#### 7.6.1.2 Cone

VOLU
num(volu)
COMBI
num(type)
sx sy sz
height
#
V_ORIGIN num(vol-orig)
#
M_ORIGIN
ni nj nk
LATTICE numres
ENDV
where:
• (sx,sy,sz) are the coordinates of the apex S of the cone;
• height is the distance between the apex and the base of the cone, the base being orthogonal to the axis;
• V_ORIGIN and M_ORIGIN, along with their arguments, are used to give the coordinates of the apex with
respect to the center of a volume or a cell, as with other combinatorial volumes.

### 7.6.2 DEFINING SIMPLE VOLUMES USING SURFACES

Simple volumes are defined in terms of surface as follows:
VOLU
num(volu)
EQUA
PLUS posnum
surf(1) ... surf(posnum)
MINUS negnum
surf(1) ... surf(negnum)
ENDV
where:
• posnum (or negnum) is the total number of surfaces with respect to which any point in the volume has a
positive (or negative) sign (the sign determines which side of the surface contains the point);

<!-- page 69 -->
• surf(1) surf(2) ...
surf(posnum) (or surf(1) surf(2) ...
surf(negnum)) is the list of
surfaces (identified by their numbers) with respect to which the volume belongs to the positive (or
negative) region. For the sign conventions, refer to the section on surfaces;
• the line PLUS posnum is not included when no surfaces are concerned (posnum = 0). The same applies
to MINUS negnum.
Example:
SURF 11 PLANEX -4
SURF 12 PLANEX 0
SURF 13 PLANEY -2
SURF 14 PLANEY 2
SURF 15 PLANEZ -2
SURF 16 PLANEZ 2
VOLU 7 EQUA PLUS 3
11 13 15 MINUS 3
12 14 16 ENDV
The volume obtained is a cube with 4 cm sides centered on (−2,0,0).

<!-- page 70 -->
## 7.7 DEFINING ROTATION TYPE VOLUMES

This type of volume is called ROTATION. The necessary data include:
• the number for the volume used to create the current volume by rotation;
• the axis of rotation;
• the angle of rotation in degrees;
• the center of rotation.
The syntax is, therefore, as follows:
VOLU
num(volu)
ROTATION
VOLU num(volu-rot)
ux uy uz
θ
Ωx Ωy Ωz
ENDV
where:
• num(volu) is the number of the volume being defined;
• num(volu-rot) is the number of the simple volume to be rotated (volume COMBI or EQUA only, but not
necessarily virtual);
• (ux,uy,uz) are the coordinates of a vector carrying the axis of rotation in the geometry reference frame;
• θ is the angle of rotation (in degrees);
• (Ωx,Ωy,Ωz) are the coordinates of the center of rotation in the geometry reference frame.
Restrictions on rotation: A volume obtained by ROTATION must conform to certain restrictions
• it must be obtained from an element defined with a combinatorial or surface-based geometry (it is not
possible to effect rotation on a lattice);
• it cannot override the volume from which it is derived (but the latter can be virtual);
• it cannot be augmented by the UNION operator (see below).

<!-- page 71 -->
There is currently no checking of non-overlap for a ROTATION volume.
Examples:
TYPE 3 BOX 4 4 4
VOLU 7 COMBI 3 -2.
0.
0.
ENDV
VOLU 9 ROTATION VOLU 7
0 0 1
45
10 0 0
ENDV
Two volumes are created: volume 7, a cube with 4 cm sides centered on (−2,0,0), and volume 9, obtained
by rotation of volume 7. The rotation is about axis Z = (0,0,1) with a center at (10,0,0) and an angle of 45
degrees.
SURF 11 PLANEX -4
SURF 12 PLANEX 0
SURF 13 PLANEY -4
SURF 14 PLANEY 0
SURF 15 PLANEZ -4
SURF 16 PLANEZ 0
VOLU 7 EQUA PLUS 3
11 13 15 MINUS 3
12 14 16 FICTIVE ENDV
VOLU 9 ROTATION VOLU 7
0 0 1
45
10 0 0
ENDV
A single volume 9 is actually created. Volume 7 (a cube centered on (−2,−2,−2) with 4 cm sides), is a
virtual volume used to construct other volumes (9 in this case). Volume 9 is obtained by rotating volume 7.
The rotation is about axis Z = (0,0,1) with a center at (10,0,0) and an angle of 45 degrees.

## 7.8 DEFINING OPERATORS RELATED TO VOLUMES

Operators can appear before the keyword ENDV, as they participate to the definition of a volume.
Several operators can appear in the definition of a single volume.
The following operators are currently known by the geometry:
• SMASH enabling one volume to override another;
• VMINUS, which has the opposite effect of SMASH;
• INTE for volume intersection;
• UNION for volume unions.

<!-- page 72 -->
### 7.8.1 THE SMASH OPERATOR

The SMASH operator is used to indicate, in the event of intersection of two volumes, to which volume the
intersection belongs.
SMASH
nb(volu)
volu(1) ... volu(n)
where:
• nb(volu) is the number of volumes overridden by the volume being defined;
• volu(1) ...
volu(n) is a list of the nb(volu) numbers (separated by spaces) of previously defined
volumes overridden by the current volume.
The following figure illustrates the use of the SMASH operator (volume A overrides volume B if the intersection
of A and B belongs to A. The grey part represents the result of A overriding B):
A
B
Example:
TYPE 3 BOX 4 4 4
TYPE 5 BOX 1 1 1
VOLU 7 COMBI 3 -2.
0.
0.
ENDV
VOLU 8 COMBI 5 -2.
0.
0.
SMASH 1 7 ENDV
Two cubes are created, centered on (−2,0,0). The first, 7, has 4 cm sides (TYPE 3), the second, 8, has 1 cm
sides (TYPE 5). Volume 8 is included in 7 and overrides it. The central part no longer belongs to 7.

<!-- page 73 -->
#### 7.8.1.1 Properties of SMASH

Transitivity:
If A overrides B and B overrides C, then the part of A included in B overrides C. For example, if A is totally
included in B, it is enough to state that B overrides C and it will make the code run faster.
On the other hand, if there is a part of A not included in B but overriding C, then it is necessary to add that A
overrides C.
C
B
A
Figure 7.10: Here A overrides B and B overrides C implying that A overrides C
Important Restriction: if A and B are tangent, then the above property remains valid if and only if A and B are
simple volumes, ie not constructed themselves with operators. If A and/or B are constructed with operators,
then again it is necessary to add that A overrides C.

#### 7.8.1.2 The SMASH operator and virtual volumes

The SMASH operator is mandatory when two non-virtual volumes overlap. In the case where one of the two
volumes is virtual and the other is not, the real volume overrides the virtual volume by default (as the latter
does not physically exist), and it is not necessary to use the SMASH operator.
However, it is possible to make a virtual volume B override a real volume A to reduce it: in which case the
common part P no longer belongs to the real volume. If volume A were to override volume C, part P would
once again belong to C, otherwise care would be required to fill the space to obtain convex geometry.
Let us consider the following case:

<!-- page 74 -->
C
B
A
Figure 7.11: A overrides B and B overrides C AND A and B are tangent, CAUTION when using the transitivity property
TYPE 1 BOX 4 4 4
VOLU 1 COMBI 1 0 0 0 ENDV
TYPE 2 BOX 2 2 2
VOLU 2 COMBI 2 0 0 0 SMASH 1 1 ENDV
TYPE 3 BOX 1 1 1
VOLU 3 COMBI 3 0 0 0 SMASH 1 2 FICTIVE ENDV
Despite the transitivity, 3 does not override 1. As 3 is virtual, a “gap” remains at the center, which becomes
part of 1 again.

#### 7.8.1.3 Rotation and operator SMASH

The volume of the rotation type cannot override the volume it is derived from.

### 7.8.2 THE VMINUS OPERATOR

This operator corresponds to the opposite of the SMASH operator. It can be used to truncate a volume by
removing those areas where it intersects with other volumes. This operator is used as follows:
VMINUS
nb(volu)
volu(1) ... volu(n)

<!-- page 75 -->
where:
• nb(volu) is the number of volumes truncating the volume defined.
• volu(1) ...
volu(n) is the list of nb(volu) numbers of previously defined volumes truncating the
current volume (at their intersection).
Figure 7.12 shows the operation performed by VMINUS.
A
B
Figure 7.12: The grey part represents the results of A VMINUS B. A−(A∩B)
is retained.

<!-- page 76 -->
Example:
TYPE 3 BOX 4 4 4
TYPE 5 BOX 1 1 1
VOLU 8 COMBI 5 -2.
0.
0.
ENDV
VOLU 7 COMBI 3 -2.
0.
0.
VMINUS 1 8 ENDV
Two cubes are created, centered on (−2,0,0). The first cube, named 8, has 1 cm sides (TYPE 5), the second
cube, named 7, has 4 cm sides (TYPE 3). The central part does not belong to 7, as it is removed by VMINUS.

#### 7.8.2.1 Restrictions on the SMASH and VMINUS operators

It is not possible to have two overriding definitions that are contradictory: if A overrides B and B overrides
C, then C cannot override A (using the VMINUS operator).
B
C
A
Figure 7.13: A overrides B, B overrides C, and C overrides A
The following approach at entering a geometry corresponding to Figure 7.13 is incorrect:
VOLU 1 (definition of A)
ENDV
VOLU 2 (definition of B)
VMINUS 1 1
ENDV
VOLU 3 (definition of C)
VMINUS 1 2
SMASH 1 1

<!-- page 77 -->
ENDV
To define Figure 7.13 it is necessary, for instance, to back up volume B with a virtual volume D (same
definition as B but with a different number and with the FICTIVE attribute).
VOLU 1 (definition of A)
ENDV
VOLU 2 (definition of B)
VMINUS 1 1
ENDV
VOLU 20 (definition of D identical to that of B)
FICTIVE
ENDV
VOLU 3 (definition of C)
VMINUS 1 20
SMASH 1 1
ENDV

#### 7.8.2.2 Transitivity, link with the SMASH and FICTIVE operators

Real volumes
The VMINUS operator is almost symmetrical to SMASH. One peculiarity of the resulting transitivity is that if
volume B cuts off part of volume A with VMINUS, then all of the volumes (C, ...) contained in B (as a result
of SMASH or VMINUS) also cut off part of A, as shown in the following examples. (In certain cases, it would
make more sense if only the part of C remaining in volume B made the cutting.)
Examples
Given that the following types are available:
TYPE 1 BOX 1 1 1
TYPE 2 BOX 2 2 2
TYPE 3 BOX 3 3 3
There are four possible ways to create drawing 7.14:
Possibility 1: two SMASH operations
VOLU 3 COMBI 3 0 0 0 ENDV
VOLU 2 COMBI 2 0 0 0 SMASH 1 3 ENDV
VOLU 1 COMBI 1 0 0 0 SMASH 1 2 ENDV

<!-- page 78 -->
3
2
1
Figure 7.14: SMASH and VMINUS transitivity: the real volume case
Possibility 2: two VMINUS operations
VOLU 1 COMBI 1 0 0 0 ENDV
VOLU 2 COMBI 2 0 0 0 VMINUS 1 1 ENDV
VOLU 3 COMBI 3 0 0 0 VMINUS 1 2 ENDV
Possibility 3: one SMASH operation and one VMINUS operation
VOLU 2 COMBI 2 0 0 0 ENDV
VOLU 1 COMBI 1 0 0 0 SMASH 1 2 ENDV
VOLU 3 COMBI 3 0 0 0 VMINUS 1 2 ENDV
Possibility 4: one VMINUS operation and two SMASH operations
VOLU 3 COMBI 3 0 0 0 ENDV
VOLU 1 COMBI 1 0 0 0 SMASH 1 3 ENDV
VOLU 2 COMBI 2 0 0 0 VMINUS 1 1 SMASH 1 3 ENDV
Note that an additional operator is required in this case, as 1 is defined before 2.
3
2
3
Figure 7.15: SMASH and VMINUS transitivity: the virtual volume case
Introducing virtual volumes

<!-- page 79 -->
In the case where the central part is removed by virtual volume 1, the symmetry between SMASH and VMINUS
remains, and there are still four possible ways to recreate the situation shown in 7.15: adding FICTIVE to the
volume 1 definition (in the fourth case the additional operator is not required).
In all cases, the central part becomes part of volume 3.
Restrictions on the VMINUS and lattice operators
VMINUS must not be part of the definition of the reference cell of a lattice (see below).

### 7.8.3 THE INTE OPERATOR

This operator is used to define a volume as the intersection of the volume being defined with one or more
previously defined volumes. The volumes with which the current volume intersects must be virtual. The part
of the current volume not included in the intersections disappears from the geometry. This operator is used
as follows:
INTE
nb(volu)
volu(1) ... volu(n)
where:
• nb(volu) is the number of volumes to intersect the volume being defined;
• volu(1) ...
volu(n) is a list of the nb(volu) numbers (separated by spaces) of previously defined
virtual volumes.
Example:
TYPE 3 BOX 4 4 4
TYPE 5 SPHERE 2
VOLU 8 COMBI 5 -2.
0.
0.
FICTIVE ENDV
VOLU 7 COMBI 3 0.
0.
0.
INTE 1 8 ENDV
Volume 8, which is virtual, is only used in the construction of volume 7.
Volume 7 corresponds to the intersection between a cube with 4 cm sides centered on (0,0,0) and a sphere
with a radius of 2 cm centered on (−2,0,0).

### 7.8.4 THE UNION OPERATOR

This operator is used to define a volume as the union of the volume being defined with one or more previously
defined volumes. The volumes that are joined in the current volume must be virtual. This operator is used as
follows:
where:

<!-- page 80 -->
UNION
nb(volu)
volu(1) ... volu(n)
• nb(volu) is the number of volumes to be joined with the volume being defined;
• volu(1) ...
volu(n) is the list of nb(volu) numbers (separated by spaces) of previously defined
virtual volumes.
Verification of non-overlap for a volume with UNION is not currently implemented.
Note: UNION cannot be used with a ROTATION volume.
Example:
TYPE 3 BOX 4 4 4
TYPE 5 BOX 1 1 1
VOLU 8 COMBI 5 -2.
0.
0.
FICTIVE ENDV
VOLU 7 COMBI 3 0.5.
0.
0.
UNION 1 8 ENDV
A single volume, 7, is created. It consists of a cube with 1 cm sides, centered on (0.5,0,0), which constitutes
the simple volume. The UNION operator is used to add a cube with 4 cm sides centered on (−2,0,0). Volume
8 is virtual and its only purpose is the construction of 7.
Important note: If the volume being defined is to override other volumes, then the SMASH operator (and its
arguments) must not be included in the definitions of added virtual volumes. This is because they would, in
this case, override the volumes as virtual ones.
Example:
Volume A results from the union of 1 (virtual) and 2, which overrides volume 10. The following syntax is
correct
TYPE 100 BOX 5 5 5
VOLU 100 COMBI 100 0 0 0 ENDV
TYPE 10 BOX 4 4 4
VOLU 10 COMBI 10 0 0 0 SMASH 1 100 ENDV
TYPE 1 BOX 1 1 1
VOLU 1 COMBI 1 -1 0 0 FICTIVE ENDV
VOLU 2 COMBI 1 1 0 0 UNION 1 1 SMASH 1 10 ENDV
However,
TYPE 100 BOX 5 5 5
VOLU 100 COMBI 100 0 0 0 ENDV

<!-- page 81 -->
TYPE 10 BOX 4 4 4
VOLU 10 COMBI 10 0 0 0 SMASH 1 100 ENDV
TYPE 1 BOX 1 1 1
VOLU 1 COMBI 1 -1 0 0 SMASH 1 10 FICTIVE ENDV
VOLU 2 COMBI 1 1 0 0 UNION 1 1 SMASH 1 10 ENDV
is not correct and will return an error.

## 7.9 OPERATOR PRIORITY

The code first searches for the presence of VMINUS, INTE, and/or UNION.

### 7.9.1 PRIORITIZATION OF VMINUS, INTE, AND UNION

If a number of UNION, INTE, and VMINUS operators are present, the operations are parsed from left to right.
Thus, to obtain
(1∩2)∪3
it is necessary to write VOLU 1 COMBI num x y z INTE 1 2 UNION 1 3 ENDV.
However, to obtain
(1∪2)∩3
it is necessary to write VOLU 1 COMBI num x y z UNION 1 2 INTE 1 3 ENDV.

### 7.9.2 PRIORITIZATION OF (INTE, UNION, VMINUS), AND SMASH

The code analyzes the SMASH operator differently from the others, as if it came last. This means that the
volume that overrides is the simple volume modified by VMINUS, UNION, and INTE, even if these operations
are given afterwards:
For
VOLU 1 COMBI num x y z SMASH 1 4 INTE 1 2 UNION 1 3 ENDV
it is the entire volume [(1 INTE 2) UNION 3] that overrides volume 4.

<!-- page 82 -->
## 7.10 DEFINING A LATTICE

### 7.10.1 THE CONCEPT OF LATTICES

The GEOMETRY command is used to define orthorhombic lattices (parallelepipeds with individual patterns)
and hexagonal lattices.
This type of volume is referred to as RESC (parallelepipeds) or RESH (hexagons). The data required to define
these lattices are:
• the number of the volume establishing the reference cell;
• the number of repetitions of the volume along the three axes of the lattice.
The reference cell associated with the volume Vbase can only be a BOX, a PARALLELEPIPEDE, or a hexagonal
prism (HEXAX, HEXAY, HEXAZ), defined using combinatorial geometry (no rotation, for instance). The sides
(defined in the TYPE declaration) and the center of the volume determine the reference cell.
The pattern consists of all the elements located in the cell (and not only in the reference volume, as the box
may have been overridden by other volumes) at the time of creation of the lattice. If another volume is located
in the cell, it is also repeated.
For a RESC, the lattice consists of nx × ny × nz cells, numbered along the axes associated with the reference
cell:
• In the case of a BOX, the indices of the cells along the axes increase as the axes increase;
• In the case of a PARALLELEPIPEDE, the indices increase in the direction of the descriptive vectors (see
7.4.6).
For a RESH, extension is more complex (see below).
At this point, a number of important remarks need to be made concerning the structure of this type of lattice.
The lattice volume created is an extension of the reference cell and does not actually bear the volume number
num(volu) that was declared when defining the RESC (or RESH). The lattice is similar to a virtual volume.
Each volume belonging to the reference cell is duplicated with its virtual or real attribute intact (adding
FICTIVE to the lattice definition does not change this).
When overriding a lattice, the number to be given to the SMASH operator is the number of the lattice and not
the number of the reference cell (or the volumes included in the cell). However, when associating compositions
with volumes, materials are assigned to reference cell volumes, the composition of the lattice being
unspecified. The volume of an element in the reference cell is multiplied by its occurrence in the lattice.

<!-- page 83 -->
### 7.10.2 SYNTAX

The syntax used in defining a lattice differs slightly depending on whether the reference cell is a parallelepiped
or a hexagonal prism. In the second case, it is necessary to create a lattice included in a large regular hexagon,
which leads to restrictions concerning the number of repetitions. In both cases, it is possible to exclude cells,
or only keep certain ones.
VOLU
num(volu)
<RESCH>
VOLU volume-cell
ni (nj) nk
BASIS
nbase(i) nbase(j) nbase(k)
#
EXCEPT cellcount
ni(1) nj(1) nk(1)
...
ni(n) nj(n) nk(cellcount)
#
KEEP cellcount
ni(1) nj(1) nk(1)
...
ni(n) nj(n) nk(cellcount)
MATCH
ENDV
where:
• num(volu) is the number of the volume being defined;
• <RESCH> is equal to RESC for a BOX or PARALLELEPIPEDE lattice or RESH for a HEXA[XYZ] lattice;
• volume-cell is the number of the simple volume to be repeated in the lattice;
• ni,nj,nk are the numbers of repetitions of the reference cell in the three directions of the geometrical
reference frame for a BOX, or in directions (u,v,w) for a PARALLELEPIPEDE. In the case of hexagonal
lattices, nk refers to the axis and does not give n j (which is necessarily equal to ni). These integers are
always positive (see drawings below);
• the optional command BASIS indicates the indices of the cell to form the reference cell of the lattice. By
default, the indices are (1,1,1). For a 5 × 5 × 5 lattice, BASIS 3 3 3 enables the initial volume to be
obtained (reference cell) at the center of the lattice;
• the optional command EXCEPT specifies the cellcount cells to be given special treatment:

<!-- page 84 -->
– either the volume of the reference cell is subsequently to be replaced by invoking the keyword CELL
(see below) and the volume as well as all those that override it (directly or as a result of transitivity)
are excluded from the lattice for the cells concerned (see 7.10.7.4, “Case 1” example on page 92).
– or a volume belonging to the reference cell has been marked with VOL_EXCEPT (see 7.10.7.4 for
meanings below, and the “Case 3” example on page 95); it will be excluded from the lattice (but
not those that override it) for the cells concerned. If several volumes are marked, then they are all
excluded;
• the optional command KEEP specifies the cellcount cells (integers, with all volumes) to be retained. By
default, all cells are retained. This command is incompatible with the command EXCEPT. It is mandatory
to retain the reference cell;
• the optional command MATCH, in the case of a hexagonal lattice, can be used to obtain lattice bounds that
are always the bounds of a cell (see drawings 7.17 and 7.18).
Example:
TYPE 3 BOX 4 4 4
TYPE 5 BOX 1 1 1
VOLU 7 COMBI 3 -2.
0.
0.
ENDV
VOLU 8 COMBI 5 -2.
0.
0.
SMASH 1 7 ENDV
VOLU 10 RESC VOLU 7 3 2 2 ENDV
The reference cell consists of volume 7, a cube with 4 cm sides, centered on (−2,0,0). As this volume
contains volume 8 (as a result of SMASH), the latter is also repeated as part of the cell.
The lattice created is a 3×2×2 lattice which extends over the parallelepiped −4 < x < 8,−4 < y < 4,−4 <
z < 4.

### 7.10.3 LATTICE RESTRICTIONS

• The reference volume used to create the lattice obtained using RESC must not contain the VMINUS operator
.
• The volumes to be repeated, as they are contained in the reference volume, must not extend beyond the
cell (they must be completely contained within it).
• If the cells are not defined (deleted using EXCEPT or KEEP), it is necessary to redefine the missing region
to ensure there are no gaps.
• Boundary conditions cannot be applied to hexagonal lattices defined with the MATCH keyword.

<!-- page 85 -->
### 7.10.4 LATTICES AND THE SMASH OPERATOR

Suppose that volume 1, overridden by volume 2, is repeated as a result of the definition of a lattice 10. It is to
be noted that the lattice has no physical existence: the particles belong to a volume of the reference cell (in
this case, 1 or volume 2 included in 1).
However, as soon as the lattice has been defined, if volume 3 overrides part of the lattice, it must also override
lattice 10 and not a volume (1 or 2) of the cell.
Syntax for the above example
TYPE 1 BOX 1 1 1
TYPE 2 BOX 2 2 2
TYPE 3 BOX 3 1 5
VOLU 1 COMBI 1 0 0 0 ENDV
VOLU 2 COMBI 2 0 0 0 SMASH 1 1 ENDV
VOLU 10 RESC VOLU 1
18 18 18 ENDV
VOLU 3 COMBI 3 5 5 2 SMASH 1 10 ENDV
If volume 1 overrides volume 2, it is not necessary to state that lattice 10, built from 1, overrides volume 2.
Important: If the MATCH option has been used, this is, in fact, impossible.
(There are however a few particularities for lattices of lattices, as is indicated below.)

### 7.10.5 CELL NUMBERING

The numbering system is shown in the following figures. It is obvious for parallelepipeds and boxes, but
more complex in the case of hexagons.
113
111
211
311
112
212
213
313
312
Z  or  w
X or u
Y  or  v
Figure 7.16: RESC lattice composed of boxes or parallelepipeds
An example is given of a hexagon of axis Z. The conventions for the other hexagons are obtained by circular

<!-- page 86 -->
permutation (when in doubt, the user can use the POSITION option described at the beginning of this section).
211
131
321
221
121
231
331
111
axis X
axis 2
311
Figure 7.17: RESH lattice composed of HEXAZ hexagons (angle θ null), section along z: ni = nj = 2.
211
131
321
121
231
331
111
axis 2
311
221
axis 1
X
Y
Figure 7.18: RESH lattice composed of HEXAZ hexagons (angle θ = 90), section along z: ni = nj = 2.
The cells that do not belong to the lattice if the MATCH option has been indicated are shown in dotted lines. The
boundaries of the hexagonal box surrounding the lattice are shown in lines of dashes: these are the boundaries
if the MATCH option has not been selected. Indices of cells are determined by taking the coordinates of the
center of the cell in the reference frame (non-orthogonal) defined by the axes (X,Y): the dotted lines for the
cell (3,3,1).
In the hexagonal case, if the MATCH option has not been indicated, then the lattice will be a hexagon rotated
by 90 degrees with respect to the cell orientations.

<!-- page 87 -->
### 7.10.6 LATTICE OF LATTICES

It is now possible to create lattices of lattices, lattices of lattices of lattices etc. whenever required.
Let volume 1 be repeated in lattice 10 (all within volume 11):
TYPE 1 BOX 1 1 1
TYPE 2 BOX 0.5 0.5 0.5
TYPE 11 BOX 100 100 100
VOLU 11 COMBI 11 0 0 0 ENDV
VOLU 1 COMBI 1 0 0 0 SMASH 1 11 ENDV
VOLU 2 COMBI 2 0 0 0 SMASH 1 1 ENDV
VOLU 10 RESC VOLU 1 2 2 1 (SMASH 11) ENDV
Two possibilities are available:
• repeating lattice 10 in lattice 100 (inside box 11 or slightly spilling over 11) by
VOLU 100 RESC VOLU 10 3 2 1 ENDV.
In this case, (SMASH 11) is not required;
• repeating volume 11, which contains lattice 10.
VOLU 100 RESC VOLU 11 3 2 1 ENDV.
In this case (SMASH 11) is required.
Restriction: In order to be repeated, a volume must override, either directly or by transitivity, the reference
cell M. However, this is not necessary for lattice volume R (which makes it possible to use option MATCH, as
in the example in the appendix). If, however, volume V overrides lattice volume R, difficulties can arise:
• Lattice R is the reference cell of the higher level lattice or overrides this reference cell. In this case there
is no problem;
• Lattice R is in the reference cell of the higher level lattice, but does not override it (use of MATCH, for
instance). Volume V must then explicitly override it (even if V is entirely within R) in order to be
repeatable.
These restrictions also apply when the cells are defined using the options CELL and LOWER_CELL, which are
covered at the end of this section. It is not necessary to state that these cells override a volume when the latter
is overridden by the reference cell of a lattice R. This becomes necessary when R is inscribed, in a volume to
be used as the reference cell of a lattice, without overriding it.

<!-- page 88 -->
1
2
3
20
Lattice 10
4
Figure 7.19: Here, volumes 1 and 2 are repeated in lattice 10, which is included in volume 20. Volume 3 re-defines part of a cell
(via CELL) and volume 4 overrides 10. If volume 20 is used as the reference cell of a lattice and 10 does not override it, it is then
necessary to specify that 3 and 4 override 20.

### 7.10.7 VOLUME DEFINITIONS BASED ON CELLS

#### 7.10.7.1 Replacing a volume of a cell

In order to replace a particular volume in one or more specific cells, the volume can be redefined. To do so,
it is necessary to indicate the lattice and cell involved, as well as the type of the volume to replace.
Using the cell indices supplied, the code then creates a volume of the combinatorial type. It is then no longer
necessary for the user to worry about the coordinates of the center nor the dimensions of this combinatorial
volume, which are calculated using the characteristics of the reference cell and the cell indices. The volume
created can replace the entire cell or only part of it.
Given the case shown in Figure 7.20, corresponding to the following syntax:
TYPE 1 BOX 1 1 1
TYPE 2 BOX 0.5 0.5 0.5
VOLU 1 COMBI 1 0 0 0 ENDV
VOLU 2 COMBI 2 0 0 0 SMASH 1 1 ENDV
VOLU 10 RESC VOLU 1 3 3 1 ENDV
VOLU 11 COMBI 2 1 1 0 SMASH 1 10 ENDV

#### 7.10.7.2 Replacing a cell of a lattice

It is possible to replace the cell containing volume 11 using the CELL command, by specifying that the cell
(2,2,1) of lattice 10 must be re-defined with another volume.

<!-- page 89 -->
1
2
Lattice 10
11
Figure 7.20: Redefining a cell
The syntax is:
VOLU
num(volu)
CELL ni nj nk
LATTICE num(lattice)
REPLACE num(volu-replaced)
ENDV
where:
• num(volu) is the number of the created volume;
• num(lattice) is the number of the lattice in which the replacement is made;
• (ni,nj,nk) are the indices of the cell for which the replacement is made;
• num(volu-replaced) is the number of the volume defining the cell in the lattice which will be replaced
by the volume num(volu) in the cell (ni,nj,nk) specified.
This volume replaces volume V numbered num(volu-replaced) as well as all the volumes that override the
latter. It is, therefore, necessary that all the volumes that override (either directly or through transitivity) the
volume V to be removed, be totally included within V.
The introduction example corresponds to the definition:

<!-- page 90 -->
VOLU 11 CELL 2 2 1
LATTICE 10
REPLACE 1
ENDV
Note:
• If the lattice is used as the reference cell of a lattice of lattices, the replacement volume must be defined
before reproducing the lattice. The replacement volume is also duplicated by the lattice operator. However
, in this case it is necessary for either the lattice or the cell to explicitly override one of the volumes
of the cell (see example in appendix).
• If the replaced volume overrode other volumes, the definition of the new replacing volume must take
this into account.
Important restriction:
As stated, it is possible to exclude only a part of the cell rather than excluding the entire cell. However, when
a volume (and all those that override it) is excluded, it will be excluded in all of the excluded cells of the
lattice.
In particular, it is not possible, for instance, to exclude the totality of cell (2,2,2) while only excluding part
of cell (3,3,3).
The exception property is a property associated with that volume, and not the cells that replace it.

#### 7.10.7.3 Replacing a sub-cell of a lattice of lattices

The situation is equivalent to that of replacement of cells, but, in this case, it applies to lattices of lattices.
VOLU
num(volu)
LOWER_CELL DEPTH depth
LATTICE num(lattice,depth)
VOLU num(depth)
CELL ni nj nk
...
LATTICE num(lattice,1)
VOLU num(depth=1)
CELL ni nj nk
ENDV
where:
• num(volu) is the number of the volume being defined;

<!-- page 91 -->
• depth is the depth of the sublattice for which the replacement takes place. depth = 1 corresponds to
the largest lattice, depth = 2 to the next one etc. (see example below);
• num(lattice,depth) corresponds to the number of the lattice directly containing the volume to be
replaced: it is necessary to give the number num(depth) of the reference cell volume to be replaced, as
well as the indices of the cells;
• num(lattice,i) corresponds to the number of an intermediate lattice: it is necessary to give the number
num(i) of the volume to be replaced, which is num(lattice,i-1), as well as the indices of the
cells;
• num(lattice,1) corresponds to the number of the largest lattice.
Unlike CELL, here it is the entire cell that must be replaced (not just a part).
Example:
Suppose that 1000 is a 3×3×2 lattice of lattice 100, itself a 2×2×2 lattice of lattice 10, which is finally a
5×4×3 lattice of reference volume 1. If, in addition, volume 2 overrides volume 1, then we have:
TYPE 1 BOX 1 1 1
TYPE 2 BOX 0.5 0.5 0.5
VOLU 1 COMBI 1 0 0 0 ENDV
VOLU 2 COMBI 2 0 0 0 SMASH 1 1 ENDV
VOLU 10 RESC VOLU 1 5 4 3 ENDV
VOLU 100 RESC VOLU 10 2 2 2 ENDV
VOLU 1000 RESC VOLU 100 3 3 2 ENDV
There are three levels of numbered lattices ranging from the largest to the smallest lattice:
• depth 1: lattice 1000, consisting of 3×3×2 = 18 cells replicating 100;
• depth 2: lattice 100, consisting of 2×2×2 = 8 cells replicating 10;
• depth 3: lattice 10, consisting of 5×4×3 = 60 cells replicating 1 and 2.
There is a total of 18×8×60 replications of 1 and 2.
If it is required to change sub-cell (2,1,1) of lattice 100 for cell (3,2,1) of lattice 1000 (depth depth = 2) by
a volume num(volu)=102 (important: this sub-cell (2,2,1) consists of 60 cells of 1 and 2), it is necessary to

<!-- page 92 -->
indicate the lattice, the volume to be replaced, and the cells for each level, as many times as the requested
depth.
The syntax is then (from the smallest lattice to the largest, i.e., in the order of their definition):
VOLU 102
LOWER_CELL DEPTH 2
LATTICE 100 VOLU 10 CELL 2 1 1
LATTICE 1000 VOLU 100 CELL 3 2 1
ENDV
Restriction:
The same restriction applies as in a definition using CELL: it is not possible to retain part of a cell for certain
indices and to retain another part for other indices. If CELL and LOWER_CELL are used at the same time, the
restrictions that hold for one also hold for the other.

#### 7.10.7.4 Replacing a cell using EXCEPT and VOL_EXCEPT

The user may wish to do one of the following:
• replace a set of cells using the same configuration;
• replace a volume without excluding the volumes that override it (replacement of a cladding, as in the
example in 7.10.7.4 on page 97);
• replace a EQUA or ROTATION type volume.
Replacement using CELL or LOWER_CELL would be inadequate in the first case, inappropriate in the second (it
would be necessary to redefine the overriding volumes), and impossible in the third.
These problems can be overcome using EXCEPT and VOL_EXCEPT:
By using the command EXCEPT, it is possible to exclude the same volume (or set of volumes) in a number
of cells. However, if the cells are excluded using EXCEPT, it is necessary to know which volumes are to be
excluded. There are two possible cases:
• redefining a cell by means of CELL or LOWER_CELL when the volume to be excluded is specified during
the construction of the new volume and the overriding volumes are excluded by transitivity;
• neither CELL nor LOWER_CELL is subsequently called when it is necessary to specify the volumes to
be excluded at the time of their construction using VOL_EXCEPT and the overridden volumes are not
automatically excluded.

<!-- page 93 -->
Note: If a volume is defined using CELL or LOWER_CELL, it must not be included in the list of excluded cells
(otherwise the tests will be carried out twice on the same cell).
Restrictions:
The restrictions are the same as for CELL and LOWER_CELL: a volume marked by VOL_EXCEPT will always be
eliminated from the excluded cells.
Examples:
Case 1
A case of two nested lattices.
In the case of a 5×5×1 block (see Figure 7.21), 20 cells belong to lattice 10 and 5 to lattice 20.
By numbering the lower left-hand cell (1,1,1), the cells of lattice 20 are (2,2,1), (3,3,1), (3,4,1), (4,3,1), and
(4,4,1).
2
1
3
: Lattice 20
Figure 7.21: Lattice 10 (white) and 20 (gray) on a 5×5×1 block, 2D-view on OXY
The largest lattice (in this case, lattice 10) is used as a reference. It is defined by repeating volume 1 containing
volume 2. Note that, by default, the lower left-hand cell is number (1,1,1).
Then, the cells of lattice 20 are excluded (retaining 20 cells would be more expensive in terms of calculation
time than excluding 5 cells would be). Cell (2,2,1) is re-defined using the CELL option, the 5 cells being
explicitly excluded from lattice 10.
Cell (2,2,1) is re-defined (volume 3, which replaces volume 1). It is used as a reference cell for lattice 20.

<!-- page 94 -->
Lattice 20 is defined, retaining only 5 cells (including the reference cell). Note that, by default, when a lattice
is constructed, this cell is numbered (1,1,1) and it would, therefore, be possible to define lattice 20 by building
a 3 × 3 × 1 lattice, whose volume 3 is the reference cell (1,1,1) and for which only the cells (1,1,1), (2,2,1),
(2,3,1) (3,2,1), and (3,3,1) are retained.
To simplify the numbering and construction of lattice 20, it is advisable to define a 5×5×1 lattice with 3 as
the reference cell but considered to be cell numbered (2,2,1) (using option BASIS). In this case, the indices of
lattices 10 and 20 coincide and the cells to be retained have the same indices as those deleted in lattice 10.
TYPE 1 BOX 2 2 2
TYPE 2 BOX 1 1 1
VOLU 1 COMBI 1 0 0 0 ENDV
VOLU 2 COMBI 2 0 0 0 SMASH 1 1 ENDV
VOLU 10 RESC VOLU 1 5 5 1
EXCEPT 5
2 2 1
3 3 1
3 4 1
4 3 1
4 4 1
ENDV
VOLU 3 CELL 2 2 1 LATTICE 10
REPLACE 1
ENDV
VOLU 20 RESC VOLU 3 5 5 1
BASIS 2 2 1
KEEP 5
2 2 1
3 3 1
3 4 1
4 3 1
4 4 1
ENDV
Case 2
Suppose that only volume 2 is to be replaced, rather than the entire cell. By using VOL_EXCEPT, it is possible
to dispense with the transitivity laws of CELL. In this case, the user must:
• use VOL_EXCEPT to indicate that volume 2 is to be replaced;

<!-- page 95 -->
• create a virtual volume 12, of the same size as volume 1, which “occupies” the place of cell (2,2,1). This
volume is used as the reference cell of the lattice. This is because the translation vectors for the lattice
must have the dimensions of the pitch of the first lattice;
• use V_ORIGIN to position volume 3 with respect to the origin of volume 12 and specify that volume 3
overrides the virtual volume, which, as a result of transitivity, means that 3 is in the virtual cell and may
be translated;
• create a cell from virtual box 12.
It should be noted that the possibility of creating a lattice from the virtual cell only exists because the boundaries
of lattice 12 coincide with the existing boundaries. If lattice 10 did not exist, then this construction
would not be allowed.
2
1
3
: Lattice 20
TYPE 1 BOX 2 2 2
TYPE 2 BOX 1 1 1
VOLU 1 COMBI 1 0 0 0 ENDV
VOLU 2 COMBI 2 0 0 0 SMASH 1 1 VOL_EXCEPT ENDV
VOLU 10 RESC VOLU 1 5 5 1
EXCEPT 5
2 2 1
3 3 1
3 4 1

<!-- page 96 -->
4 3 1
4 4 1
ENDV
VOLU 12 COMBI 1 0 0 0
M_ORIGIN 2 2 1
LATTICE 10 FICTIVE
ENDV
VOLU 3 COMBI 2 0 0 0
V_ORIGIN 12
SMASH 1 12
ENDV
VOLU 20 RESC VOLU 12 5 5 1
BASIS 2 2 1
KEEP 5
2 2 1
3 3 1
3 4 1
4 3 1
4 4 1
ENDV
Case 3
Let us now consider the case where volume 1, rather than volume 2, is to be replaced. The user must:
• use VOL_EXCEPT to specify that volume 1 is to be replaced ;
• exclude the cells where volume 1 is to be replaced as well ;
• create a virtual volume 12 of the same size as volume 2, centered on cell (2,2,1),
• create a volume 3 of the same size as volume 1, from which volume 12 has been removed (it is not
possible to use 12 SMASH 1, as the removal would be performed after the definition of volume 3 and,
therefore, after the overlap tests were run: volume 10 and volume 3 would thus not have a zero intersection
);
• create a lattice 20 from box 3.
TYPE 1 BOX 2 2 2

<!-- page 97 -->
2
1
: Lattice 20
3
TYPE 2 BOX 1 1 1
VOLU 1 COMBI 1 0 0 0 VOL_EXCEPT ENDV
VOLU 2 COMBI 2 0 0 0 SMASH 1 1 ENDV
VOLU 10 RESC VOLU 1 5 5 1
EXCEPT 5
2 2 1
3 3 1
3 4 1
4 3 1
4 4 1
ENDV
VOLU 12 COMBI 2 0 0 0
M_ORIGIN 2 2 1
LATTICE 10 FICTIVE
ENDV
VOLU 3 COMBI 1 0 0 0
VMINUS 1 12
V_ORIGIN 12
ENDV

<!-- page 98 -->
VOLU 20 RESC VOLU 3 5 5 1
BASIS 2 2 1
KEEP 5
2 2 1
3 3 1
3 4 1
4 3 1
4 4 1
ENDV
Case 4
Let us now consider the case where volume 2 has a cladding 200 that is to be replaced by cladding 300. Here,
it is necessary to:
• use VOL_EXCEPT to specify that volume 200 is to be replaced;
• exclude the cell (2,2,1) of lattice 10 as well;
• create a virtual volume 22 of the same size as volume 2, centered on cell (2,2,1);
• create a virtual volume 12 of the same size as volume 1, centered on cell (2,2,1);
• create a volume 300, of the same size as volume 200, from which volume 22 has been removed and
which overrides volume 12 (in order to be translated);
• create a lattice from virtual box 12.
1
2
cladding 200
cladding 300

<!-- page 99 -->
TYPE 1 BOX 2 2 2
TYPE 2 BOX 1 1 1
TYPE 200 BOX 1.1 1.1 1.1
VOLU 1 COMBI 1 0 0 0 ENDV
VOLU 200 COMBI 200 0 0 0 SMASH 1 1 VOL_EXCEPT ENDV
VOLU 2 COMBI 2 0 0 0 SMASH 1 200 ENDV
VOLU 10 RESC VOLU 1 5 5 1
EXCEPT 5
2 2 1
3 3 1
3 4 1
4 3 1
4 4 1
ENDV
VOLU 22 COMBI 2 0 0 0
M_ORIGIN 2 2 1
LATTICE 10
FICTIVE
ENDV
VOLU 12 COMBI 1 0 0 0
V_ORIGIN 22
FICTIVE
ENDV
VOLU 300 COMBI 200 0 0 0
V_ORIGIN 12
SMASH 1 12
VMINUS 1 22
ENDV
VOLU 20 RESC VOLU 12 5 5 1
BASIS 2 2 1
KEEP 5
2 2 1
3 3 1
3 4 1
4 3 1
4 4 1

<!-- page 100 -->
ENDV

### 7.10.8 THE VIRTUAL CELL TRICK

It should be noted that a lattice of virtual cells cannot be used to create volumes, except under certain very
special circumstances (such as Case 2 above).
However, it is possible to use such lattices to avoid lengthy calculations.
In the case of hexagonal arrays, when the prisms are not contiguous, the lattice operators become less efficient
(too many cells have to be eliminated). Since calculating the positions of the centers can, nevertheless, be
fairly arduous, the following solution can be used to facilitate the construction:
1. create a virtual volume of the size and position of the lattice cell;
2. create a lattice from the virtual cell;
3. arrange the volumes related to the lattice using the M_ORIGIN option.
The code then calculates the coordinates of the centers.

<!-- page 101 -->
## 7.11 COPIES OF VOLUMES

It is possible for complete patterns to be identical in a geometry definition. If the patterns are not connected,
if they are not numerous, or if surface-based scores are required, the lattice approach is not the solution. An
option is available that avoids having to cut and paste within the data set (with the high risk of errors). This
option consists of copying all the volumes contained in a given volume.
The syntax is as follows:
COPY
num(vol-to-copy)
X Y Z
PLUS
increment
...
ENDC
where:
• num(vol-to-copy) is the number of the volume to be copied (all the included volumes are also copied);
• increment is used to associate a number with the new volumes: if the volume to be copied is numbered
10 and it contains volume 12, and the increment is 100, the volumes duplicated are then numbered 110
and 112;
• X Y Z is the center of the volume copied in the geometry reference frame. Note: for a cone, it is the
apex and not the center.
Restrictions:
Currently, only combinatorial volumes (conventional volumes or those generated by rotation, but not lattices)
can be copied. They must not contain any lattice or surface-based volumes.

## 7.12 2D-VIEW DISPLAY

### 7.12.1 CHOICE OF COLORS

By default, 2D-graph colors are determined by the code. There is a limited number of colors, and it is,
therefore, possibile for two adjacent regions to have the same color. To avoid this possible inconvenience
and to associate colors with the composition and displays, the user can set volume colors using the COLOR
command.

<!-- page 102 -->
COLOR
nb(colors)
<COLOR(1)> nb(volu)
volu(1)...volu(n)
...
<COLOR(N)> nb(volu)
volu(1)...volu(n)
where:
• nbcolors is the number of colors selected.
• <COLOR(i)> is one of the following: BLACK, BLUE, BROWN, CORAL, CYAN, GOLD, GRAY, GREY, GREEN,
MAGENTA, NAVY, ORANGE, PINK, PLUM, RED, SALMON, VIOLET, WHITE, YELLOW.
Each color name is followed by the number of volumes and a list of their indices.
Note: the syntax is identical to that of the GEOMCOMP command, which defines composition-volume combinations
. For combinations of colors by composition, the GEOMCOMP command can be duplicated and the
composition names replaced by color names.

### 7.12.2 2D-CROSS SECTIONAL GRAPH REQUEST

The keyword GRAPH is used to create one or more 2D-graphs of the geometry.
The GRAPH command is executed directly after it is called. Invoking GRAPH between two volume definitions
results in the display of a stage in the construction of the geometry; the volume definitions following the
GRAPH call are not included. It is thus possible, in the same data set, to request 2D-graphs at a number of
different angles or stages.
The results can be stored in the form of a PostScript file, which may be encapsulated or non-encapsulated. In
this case, the user may choose whether or not the 2D-graph is to be displayed on the screen. This allows the
user to obtain a graph of the geometry without stalling the calculation with a screen display.
The syntax is as follows:
GRAPH
Px Py Pz
Ux Uy Uz
Vx Vy Vz
Lu Lv
Flag
FILE filename

<!-- page 103 -->
2D-graphs are displayed in a plane containing the point P =(Px,Py,Pz) and defined by two vectors
U=(Ux,Uy,Uz) and V=(Vx,Vy,Vz).
The window is determined by point P (bottom left) and length Lu along U and Lv along V.
Flag is set to:
• 0 for no PostScript file;
• 1 for a PostScript file with a caption in the drawing;
• 2 for a PostScript file without a caption;
• 3 for an encapsulated PostScript file with a caption;
• 4 for an encapsulated PostScript file without a caption;
• 5 for a Postscript file with a caption and with no screen display.
• 6 for a PostScript file without a caption and with no screen display;
• 7 for an encapsulated PostScript file with a caption and with no screen display;
• 8 for an encapsulated PostScript file without a caption and with no screen display.
The option FILE allows for the user to specify the file name associated to the graph : PostScript files are
named “filename.ps”, and encapsulated PostScript files are named “filename.eps”.
By default, PostScript files are named “graphicN.ps”, and encapsulated PostScript files are named “graphic
N.eps” (these can be embedded in text), where N is the number of the graph. They are numbered in the
order in which they are requested.
When Flag is set to 0, 1, 2, 3, or, 4, once the display is complete, the user must press the
“ENTER” key to continue. To interrupt the calculations at this point, the 2D-graph window can simply be
closed. This makes it possible for a “core dump” not to be generated if the following data is missing, for
instance.
Note: The geometry is displayed by means of two functions (position and distance calculations) used in the
tracking of particles. The sweep is made by a line parallel to axis U.
As during calculation, a particle leaving the geometry cannot return to it. Therefore, if the geometry is
non-convex (which is not the normal case), the display can “cut” a volume.
In the example in Figure 7.22, line L sweeps the domain (fromleft to right) as follows:
• calculating the point of entry P(0), defining the entrance volume (1, in this case);
• calculating the point of exit P(1) of volume 1;
• determining the new volume (2, in this case);

<!-- page 104 -->
• calculating the point of exit P(2) from volume 2;
• determining the new volume, in this example, leakage out of the geometry;
• moving on to ray trace the next line.
L
P(2)
P(1)
P(0)
L’
Volume 3
Volume 1
Volume 2
Outside Geometry
Figure 7.22: The non-convex geometry problem. Undisplayed part in dotted lines
As such, volume 3 is not encountered. However, it is on line L′, as there is no gap in the line ray tracing.

## 7.13 GEOMETRY CHECKS

### 7.13.1 COMBINATORIAL GEOMETRY CHECKS

When a combinatorial geometry is defined, the code always performs a test for volume overlapping as the
geometry is read.
It is possible to adjust the number of points generated when testing for combinatorial volume non-overlaping.
When the keyword "TEST_GENERATED_POINTS n" is not used, the default value for n is 200.
It can be set in two ways:
• only once at the beginning of the geometry definition (after the directive TITLE)
• or as many times as necessary in the directive GEOMETRY, preceding the keyword VOLUME (for
each combinatorial volume, the number of generated points refers to the previous value of
TEST_GENERATED_POINTS).

### 7.13.2 REQUESTING CHECKS

No matter how the volumes of the geometry are defined, the user may request checks on either a part or all of
the geometry using the command CHECK_GEOM. This is particularly useful in surface mode where the default

<!-- page 105 -->
check (see $ 7.13.1) is not performed. The check is performed in a window defined by coordinates specified
by the user.
The syntax, to be placed after the keyword ENDGEOM, is as follows :
CHECK_GEOM
FRAME
<FRAME_TYPE>
Ox Oy Oz
ix iy iz
(jx jy jz)
kx ky kz
WINDOW
Umin Vmin Wmin
Umax Vmax Wmax
SOBOL_POINTS nb(points)
LIST nb(points)
CHECK_HOLES
END_CHECK_GEOM
where:
• the window is defined by specifying the type of coordinates (CARTESIAN, CYLINDER, or SPHERE), the
origin O and the associated axes i, j, k. The j axis is only specified in the case of Cartesian coordinates
(see section 4.5 for a complete explanation of frames).
• the window for the checks is defined by two minimum and maximum side points, with coordinates
as follows: (Umin, Vmin, Wmin), and (Umax, Vmax, Wmax) expressed in the desired type of coordinates
(respectively (x,y,z), (r,θ,z) and (r,φ,θ)).
This functionality performs a check for overlapping volumes using a number of points randomly sampled
in the geometry. The default value for this number of points is 50, but may be modified using the optional
keyword SOBOL_POINTS.
The set of sampled points belonging to at least two volumes is displayed. For each of these points, the
overlapping volumes are identified. If the list of overlapping points is large, the user can reduce the display
by setting the number of elements in the list using the keyword LIST. If at least one point is found to lie
within overlapping volumes, the calculation will not be performed.
The keywords SOBOL_POINTS and LIST can be used independently. Nevertheless, if both of the keywords are
specified, they must be entered in the order shown above.
Finally, the user may also specify the CHECK_HOLES option, which is used to check for the existence of holes
in the geometry. In such a case, the complete list of points not belonging to any volume of the geometry
is provided and the calculation is stopped. For this option, the user must ensure that the defined window is
indeed included in the geometry.

<!-- page 106 -->
When the keyword CHECK_HOLES is not used, a check is performed to search for holes, but only a list of
approximately ten points is displayed. This allows the user to define a window (for the overlapping check)
containing the whole geometry, without stopping the procedure due to the hole checks.
Note : For a combinatorial geometry, the CHECK_GEOM command is especially useful in verifying the convexity
of the geometry (absence of holes).

### 7.13.3 1D SCAN OF GEOMETRY

This functionality enables to scan geometry along n paths. For each path, the user has to give the coordinates
of the starting point and of the arrival point. For each path, it gives boundary points, crossed volumes, and
distances in these volumes. It only requires geometry, as in CHECK_GEOM.
The syntax, to be placed after the keyword ENDGEOM, is as follows :
SCAN_GEOM_1D
PATH nb(paths)
Xstart(path(1))
Ystart(path(1))
Zstart(path(1))
Xstop(path(1))
Ystop(path(1))
Zstop(path(1))
... start(path(i))
... stop(path(i))
Xstart(path(n))
Ystart(path(n))
Zstart(path(n))
Xstop(path(n))
Ystop(path(n))
Zstop(path(n))
END_SCAN_GEOM_1D

### 7.13.4 1D SCAN OF GEOMETRY-COMPOSITION ASSOCIATION

This functionality enables to scan geometry-composition association along n paths. For each path, the user
has to give the coordinates of the starting point and of the arrival point. For each path, it gives boundary
points, crossed volumes, distances in these volumes and compositions. It requires a complete data file. It
gives the results after reading materials.
The syntax, to be placed after the keyword ENDGEOM, is as follows :

<!-- page 107 -->
SCAN_GEOMCOMP
1D_SCAN
PATH nb(paths)
Xstart(path(1))
Ystart(path(1))
Zstart(path(1))
Xstop(path(1))
Ystop(path(1))
Zstop(path(1))
... start(path(i))
... stop(path(i))
Xstart(path(n))
Ystart(path(n))
Zstart(path(n))
Xstop(path(n))
Ystop(path(n))
Zstop(path(n))
END_1D_SCAN
END_SCAN_GEOMCOMP

### 7.13.5 REQUESTING CHECKS USING TRACKING ROUTINES

This functionality enables to check geometry using tracking routines, while CHECK_GEOM functionality
(see $ 7.13.2) uses positioning routines. Therefore, CHECK_GEOM and CHECK_TRACKING are redundant and
complementary functionalities that help the user to check the geometry in an exhaustive way. In the case
of CHECK_TRACKING, the user will detect the straight-line paths along which tracking is not correct, if any.
For example, this can be induced by an overlap between two or more volumes or by a hole in the geometry.
The check is performed in a sphere specified by the user, inside which a user-defined number of straight-line
paths are sampled and tested for tracking in both directions. The syntax, to be placed after the keyword
ENDGEOM, is as follows :
CHECK_TRACKING
∗
SPHERE
∗
POINT
X0 Y0 Z0
R
nb(paths)
END_CHECK_TRACKING
where:
• SPHERE or POINT indicates the type of test to be performed (see below)
• X0, Y0, and Z0 is the center of the sphere
• R is the radius of the sphere
• nb(paths) is the number of straight-line paths to be sampled and tested

<!-- page 108 -->
The user must choose between a “sphere-sphere" test using SPHERE keyword and a “point-sphere" test using
POINT keyword. In the former case, the starting point and the arrival point of the sampled paths belong to
the sphere surface. In the latter case, one of the two points is the center of the sphere, allowing the user
to focus on a region. If the result of CHECK_TRACKING is positive (indicating that the geometry contains
some errors), the code will give the starting point and the arrival point of all paths along which the tracking
is not coherent and will try to identify the volume that needs to be fixed (it can be a neighbour of this volume).
Comments:
An error can be detected several times, thus producing a long listing. An error might affect a small spatial
region, and thus have negligible consequences on the calculation (this depends also on the features of the
system and the desired scores). The impact of the detected errors is therefore to be evaluated according to
the distinct system under investigation and general conclusions can not be drawn. In order to support the
geometry analysis, one can then use SCAN_GEOM_1D or SCAN_GEOMCOMP in both directions.
Advanced use:
The user can specify multiple CHECK_TRACKING in the same input deck.
The user can run CHECK_TRACKING in parallel mode. In this case, the results of the process with rank 2 in
parallel mode will give the same results than the single process in mono-process mode.
An interesting post-processing of the results consists in plotting a 3D graph of all paths along which an error
occured: in the case of errors concerning small regions, one can detect many intersecting paths lying within
a small region of space, showing the location of the problem.

## 7.14 INFLUENCE OF DATA INPUT ON CALCULATION TIME

Calculation time during simulation (and not only during data verification) depends on the number of operators
(SMASH, UNION, etc.). A geometry input in combinatorial form can, therefore, require more time than a
surface-based geometry.
It is, however, necessary to find a suitable compromise between the time necessary for the user to define a
surface-based geometry, which can be longer (and without the combinatorial definition verifications) and the
longer calculation time using the combinatorial approach.

### 7.14.1 CONNECTIVITY MAPS

#### 7.14.1.1 Usage

The optimisation algorithm for resolving geometry calls is based on memorising neighbours of each volume.
When particles get out of a volume and the code needs to find the next volume, a search is first done inside
a table of nearest neighbours. If it fails, a new search is then done inside all the other volumes (excluding
previous searches in simplest cases). When working with large geometries (more than 50000 volumes for
example), and if neighbour tables have not been built efficiently, the search may lead to large simulation time.

<!-- page 109 -->
In the case of combinatorial geometries, the neighbours table is usually efficiently computed during the
initialisation. With some surface based geometries, the neighbours table is not very efficiently done during
the initialisation.
In any case, when a volume is found by a search in the whole geometry, the volume is then added to the
neighbours table so the code is optimising itself during the simulation.
It may be interesting to provide a neighbours table for the code. The table needs not to be complete. In this
case, the user must invoke the keyword USE_CONNECTIVITY_MAP with the filename. Important: the user
must place the use call when all volume cited in the file are defined. The most convenient place is in general
at the end of the geometry block.
Alternatively, the user may store the connectivity map built inside the code at the end of the simulation using
the keyword STORE_CONNECTIVITY_MAP with the filename. This command has to be placed at the end of
the geometry block. Note that the file will be created at the end of the simulation. If the calculation is
replayed using the exact same geometry and the geometry contains a very large number of volumes, the
second simulation will be much faster.
This can for example be useful when calculating a very large number of scores (so that the calculation will not
fit into memory). The user may split the scores in several parts and rerun the same simulation with different
scores.
The connectivity map loading has been made recursive, thus it is possible to load multiple connectivity maps.
The user can produce some connectivity maps in parallel (that is with independent simulations), and load
them all in a second parallel simulation providing some bootstrapping parallelisation effect.
The syntax, for using or creating connectivity maps, is as follows :
USE_CONNECTIVITY_MAP <filename>
STORE_CONNECTIVITY_MAP <filename>

#### 7.14.1.2 Map Format

Please note this format is subject to change after version 12 of the code, in order to address reading performance
issues when there are many volumes (>100000).
The present format is as follows:
has_stat|no_stat
iVol0 iNbNei0 iNei0,0 iCnt0,0 iNei0,1 iCnt0,1 ...
iVol1 iNbNei1 iNei1,0 iCnt1,0 iNei1,1 iCnt1,1 ...
...

<!-- page 110 -->
The first line is either has_stat or no_stat depending on if we give the visiting count (or an integral number
increasing with the probability to visit this neighbour). iVol0 is the identifier of the first volume, followed
by a table of its neighbours for the rest of the line. INei0 is the number of neighbours of iVol0. Following
this are all the neighbours of iVol0 one by one, with the identifier (iNei0,0 for the first) and the number of
times this neighbour has been visited (iCnt0,0).
It is possible to set the visit count to zero at the cost of a performance decrease (likely slight and forgotten
after a few batches). The most important is to have a table that includes the majority of frequently visited
neighbours, possibly sorted in descending order of visit counts.
Generally, this table will be sorted in descending order of visits within the first hundred batches to optimize the
searches. In cases where the number of neighbours is exceptionally large, sorting this table will be disabled
as it would be counterproductive.

### 7.14.2 SURFACE-BASED GEOMETRIES

The keyword HASH_TABLE at the beginning of the geometry can be used to speed-up the reading of large
surface-based geometries. Very small geometries (requiring for instance less than a second to initialize) may
be slower, but large geometries (bigger than 100000 volumes for example) will be faster. Speed-up factors
larger than 10 for the initialization time have been observed on large geometries. This option does not affect
the transport (simulation time and results).

### 7.14.3 COMBINATORIAL GEOMETRIES

Care should also be taken to avoid superfluous operators: not to have one volume override another when it is
possible to use the benefits of transitivity and to avoid unnecessary unions when the intersection is empty.
One important implication concerns lattice-based geometries. The user may wish to calculate a surface-based
flux or current or a surface-based reaction rate in part of the lattice. It is possible to override the part involved
(shown in gray in the diagram) by one or more other volumes, in order to differentiate them.
Example: The above sketch corresponds to the following sequence:
TYPE 1 BOX 2 1 1
VOLU 1 COMBI 1 1 0.5 0 ENDV
TYPE 2 SPHERE 0.4
VOLU 2 COMBI 2 1 0.5 0 SMASH 1 1 ENDV
VOLU 3 RESC VOLU 1 2 3 1
ENDV
VOLU 4 COMBI 1 3 1.5 0 SMASH 1 3 ENDV
VOLU 5 COMBI 2 3 1.5 0 SMASH 2 3 4 ENDV

<!-- page 111 -->
2
1
4
5
Lattice 3
x = 0
x = 1
x = 2
y = 0
y = 1
y = 2
y = 3
reference cell,
contains 1 and 2
flux between volumes 4 and 5 can be requested (see section on scores).
It is, however, possible to redefine the cells or parts of them without resorting to using the SMASH
operator. Preference should be given to this approach (i.e., redefinition of the cells).
With large lattices, use of SMASH is to be avoided.
Calculation time depends on operators and, in this case, for each point of the lattice, the code tests whether
the part involved is not overridden by other volumes. The time lost is considerable if a large number of points
are involved. When the SMASH operator has been used, the user must attempt to split the lattice and
define several different lattices: the lattices that are to be overridden and those that are never overridden. In
this manner, the latter group of lattices does not slow down the calculation because of unneccessary tests to
determine whether something is being overridden or not.
The example shown in the figure above (limited to a two dimensional example of 24x36 cells for the sake of
simplicity) in which the results in cell (1,1) are requested constitutes an extreme case. Rather than having a

<!-- page 112 -->
complete lattice overridden in a single cell, it is better to define this cell (1,1) separately, then a 1x23 lattice
(the first line minus the cell shown in black) with cells of (2,1) to (24,1) and a lattice of 23x36 (above the
dotted line (2,1) of cell (2,1) to cell (24,36). This avoids using the operator SMASH completely.
Of course, avoiding the use of SMASH altogether would compromise of the power of RESC, but an effort should
be made to limit the number of operators on a lattice (particularly by avoiding setting the bounds of a complete
lattice using INTE and VMINUS if the central part of the lattice is to be retained as a “pure” lattice and only set
the bounds on the periphery with a second lattice).
Finally, one thing that is common in both surface-based and combinatorial geometries, is that the calculation
time depends on the number of potential neighbors the volumes have. For example, if a reactor core is
naively defined using a surface-based geometry, the result is a cylinder for the vessel and tens of thousands of
cylinders for each cell (3 per cell). A neutron moving through the moderator could then encounter each cell on
its trajectory and thus result in the code making tens of thousands of unnecessary intersection calculations (as
the probability of a neutron seeing a cell from more than one fuel assembly away is very slight). Calculation
time would be equivalent to that obtained using a combinatorial geometry with each cell overriding the vessel.

<!-- page 113 -->
Surface-based geometry definition for the criticality example of chapter 5
GEOMETRY
TITLE Criticality configuration chap 5 surface-based
SURF 1 PLANEZ 0.
SURF 2 PLANEZ 60.
SURF 3 PLANEZ 185.
SURF 4 PLANEZ 185.3
SURF 5 PLANEZ 213.84
SURF 6 PLANEZ 284.2
SURF 7 PLANEZ 284.8
SURF 8 PLANEZ 300.
SURF 9 CYLZ -15.1 0.
14.55
SURF 10 CYLZ -15.1 0.
14.85
SURF 11 CYLZ 15.1 0.
14.55
SURF 12 CYLZ 15.1 0.
14.85
SURF 13 PLANEX -150.
SURF 14 PLANEX 150.
SURF 15 PLANEY -150.
SURF 16 PLANEY 150.
VOLU 11 EQUA PLUS 3 2 13 15 MINUS 3 3 14 16 FICTIVE ENDV
VOLU 12 EQUA PLUS 3 7 13 15 MINUS 3 8 14 16 FICTIVE ENDV
VOLU 1 EQUA PLUS 5 10 12 3 13 15 MINUS 3 7 14 16
UNION 2 11 12
ENDV
VOLU 2 EQUA PLUS 3 1 13 15 MINUS 3 2 14 16 ENDV
VOLU 31 EQUA PLUS 1 3 MINUS 2 4 10 FICTIVE ENDV
VOLU 32 EQUA PLUS 2 4 9 MINUS 2 6 10 FICTIVE ENDV
VOLU 3 EQUA PLUS 1 6 MINUS 2 10 7
UNION 2 31 32
ENDV
VOLU 4 EQUA PLUS 1 5 MINUS 2 6 9 ENDV
VOLU 5 EQUA PLUS 1 4 MINUS 2 9 5 ENDV

<!-- page 114 -->
VOLU 61 EQUA PLUS 1 3 MINUS 2 4 12 FICTIVE ENDV
VOLU 62 EQUA PLUS 2 4 11 MINUS 2 6 12 FICTIVE ENDV
VOLU 6 EQUA PLUS 1 6 MINUS 2 12 7
UNION 2 61 62
ENDV
VOLU 7 EQUA PLUS 1 5 MINUS 2 6 11 ENDV
VOLU 8 EQUA PLUS 1 4 MINUS 2 11 5 ENDV
COMMENT
2D-view xz x from -160 to 160 and z from -10 to 310 in y=0 plane
no Postcript file generated
COMMENT
GRAPH
-160.
-10.
0.
1 0 0
0 0 1
320.
320.
0
ENDGEOM
Note: by using the UNION operator, it is possible to combine 11, 12, and 13 into volume 1, 31, 32, and 33 into
volume 3, and, finally, 61, 62, and 64 into volume 6. The volumes could have been left uncombined, but this
is not only interesting for a surface flux or current (the surface is, indeed, defined as the boundary between
the two volumes), but above all the “unnecessary” union would result in a calculation time penalty. In
the present case, we retain the union in order to have the same numbers of volumes as in the combinatorial
definition and to provide an example of a union.

<!-- page 115 -->
Vol 5
Volume 2
Volume 11
Volume 12
Volume 1
Vol 62
Vol 3
Vol 6
Vol 32
Vol 7
Vol 8
Vol 4
Vol 61
Vol 31
Figure 7.23: Surface-based geometry

<!-- page 116 -->
Combinatorial geometry definition for the criticality example of chapter 5
GEOMETRY
TITLE Criticality configuration chap 5 combinatorial
TYPE 1 BOX 300 300 300
TYPE 2 CYLZ 14.85 49.90
TYPE 3 CYLZ 14.55 35.18
TYPE 4 CYLZ 14.55 14.27
TYPE 5 BOX 300 300 60
COMMENT
z=0 bottom of the geometry
COMMENT
VOLU 1 COMBI 1 0 0 150 ENDV
COMMENT
concrete volume
COMMENT
VOLU 2 COMBI 5 0 0 30
SMASH 1 1
ENDV
COMMENT
a container :
3 cylinders
COMMENT
VOLU 3 COMBI 2 -15.1 0 234.75
SMASH 1 1
ENDV
VOLU 4 COMBI 3 -15.1 0 249.02
SMASH 1 3
ENDV
VOLU 5 COMBI 4 -15.1 0 199.57
SMASH 1 3
ENDV
COMMENT
the other container :
3 cylinders
COMMENT
VOLU 6 COMBI 2 15.1 0 234.75
SMASH 1 1
ENDV
VOLU 7 COMBI 3 15.1 0 249.02

<!-- page 117 -->
SMASH 1 6
ENDV
VOLU 8 COMBI 4 15.1 0 199.57
SMASH 1 6
ENDV
COMMENT
2D-view xz x from -160 to 160 and z from -10 to 310 in y=0 plane
no Postcript file generated
COMMENT
GRAPH
-160.
-10.
0.
1 0 0
0 0 1
320.
320.
0
ENDGEOM

<!-- page 118 -->
Vol 5
Volume 2
Vol 7
Vol 8
Vol 4
Vol 3
Vol 6
Volume 1
Figure 7.24: Combinatorial geometry
