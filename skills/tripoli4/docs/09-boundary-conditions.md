# BOUNDARY CONDITIONS
<!-- source PDF pages 121-126 -->

<!-- page 121 -->
Chapter 9
BOUNDARY CONDITIONS

## 9.1 DEFINING BOUNDARY CONDITIONS

The boundary conditions correspond to a specific sampling of the trajectories through the boundary sides of
a volume in the outward direction. They are, therefore, given in pairs (volume, side or surface bounding the
volume). Some conditions are not yet implemented (see Table 9.1).
The allowed types of boundary conditions are as follows:

### 9.1.1 LEAKAGE

Particles are abandoned after having passed through the surface (this is the default option for outer surfaces
of the geometry).
volume 1
outside geometry
side 2
numvol = -1
Figure 9.1: Leakage
By default, the particle is in volume 1 and intersects surface 2 (the geometrical boundary, which is indicated
by the number -1 for the neighboring volume) then disappears.
In the particular case of a source resulting from a source file (see section 12.6), a leakage condition may need
to be applied to a surface in the interior of the geometry. In such a case, this must be specified in the syntax
of the boundary conditions for the surfaces involved.

<!-- page 122 -->
### 9.1.2 REFLECTION

This corresponds to optical reflection on a surface of the volume (see Figure 9.2).
volume 1
outside geometry
side 2
numvol = -1
Figure 9.2: Reflection

### 9.1.3 ALBEDO

For all the surfaces on which the reflection boundary conditions can be defined, it is alternatively possible
to attribute an albedo boundary condition. The kinematics of the albedo condition is exactly the same as for
the reflection condition, i.e., it coincides with a mirror reflection on the surface of the volume as shown in
Figure 9.2. However, an albedo value 0 < β < ∞is applied as a weight multiplier to each particle undergoing
this kind of boundary condition. The special case of β = 1 corresponds to the standard reflection boundary
condition. If β < 1 the particle weight after the boundary condition will be smaller, and for β > 1 it will be
larger. A distinct albedo value β can be assigned to each face of the volume. The albedo boundary condition
needs thus the albedo value β to be specified by the user for every surface where the condition is applied (see
below).

### 9.1.4 TRANSLATION

This boundary condition is applicable to a combinatorial volume of one of the following shapes: BOX,
PARALLELEPIPEDE, HEXAX, HEXAY, HEXAZ, CYLX, CYLY, CYLZ, or CYL.
Let (M,Ω) be the position and direction pair of a particle on side f of the box. The translation application
transforms pair (M,Ω) into (M′,Ω) where M′ is the point corresponding to M on the side of the box opposite
to f. It effectively corresponds to a translation of the constant vector MM′ , which is parallel to an edge and
of the same length.
For a cylinder, the situation is similar, except that one of the two cylinder faces must be used. The other face
is then reached, with the translation being performed parallel to the axis of the cylinder.

### 9.1.5 ROTATION

This boundary condition should be applicable to any volume (combinatorial, surface based or ROOT). When
a particle meet the conditions required for the boundary, it will be rotated according to the rotation elements

<!-- page 123 -->
outside geometry
side 2
numvol = -1
volume 1
translation vector
Figure 9.3: Translation
(axis and angle). Currently, only 90 degrees rotations are available. After the rotation, the particle must be
inside the geometry but need not be inside the same volume.
The rotation boundary condition needing more specifications than usual boundary conditions follows a different
sequence of instruction (see further section).

### 9.1.6 COSINE

This boundary condition will be used (with certain volumes) to simulate an isotropic incoming current in a
volume (white boundary condition). For a particle leaving a volume at point M, with direction Ωvia a side
to which this boundary condition has been applied, the particle is re-emitted from the same point M, with a
direction of Ω′ The direction Ω′ possesses an angle with respect to the normal inward vector with the cosine
of the angle being computed with a uniform probability.
volume 1
outside geometry
side 2
numvol = -1
Figure 9.4: Cosine reflection

<!-- page 124 -->
## 9.2 SEQUENCE OF INSTRUCTIONS

The boundary conditions are defined using the keyword BOUNDARY_CONDITION followed by the number of
sides of the geometry that have boundary conditions. There is no need to specify a leakage condition for
outer surfaces of the geometry since it is the default boundary condition. For each side, the number of the
volume, the name of the boundary condition, and, finally, a number identifying the side are given. For albedo
boundary conditions, the specific albedo value β must be provided before the number identifying the face on
which the condition is imposed.
The boundary condition instruction sequence is as follows:
BOUNDARY_CONDITION
nb(conditions)
# num(vol1) <TYPE_CONDITION> num(face1)
# num(vol1) ROTATION <rotation data>
# num(vol1) ALBEDO < β1 > num(face1)
...
# num(voln) <TYPE_CONDITION> num(facen)
# num(voln) ROTATION <rotation data>
# num(voln) ALBEDO < βn > num(facen)
END_BOUNDARY_CONDITION
The possible values for <TYPE_CONDITION> are: REFLECTION, TRANSLATION, COSINUS, or LEAKAGE. The
latter may be used when a source resulting from dump files is defined (see section 12.6.2).
For ALBEDO boundary conditions, the albedo value βi for each face i must be given before the face number.
Supplemental data for rotation is given with the following syntax:
num(voli) ROTATION Xc Yc Zc ux uy uz α num(facei)
The values Xc, Yc, and Zc specify the location of any point of the axis. The values ux, uy, uz specify a vector
defining the axis with the previous point. The α value is obviously the angle of the rotation. num(facei)
specifies the face or surface from which particle are caught to be rotated.
Important notes:
* The boundary condition is oriented and applied only to particles that get out of a specified volume number
through a specified surface number. In particular, this implies that a particle inside a volume is not affected
by boundary conditions defined to immediate neighboring volumes.

<!-- page 125 -->
* If the volume is defined by equations (surface-based geometry), the number of the side is the number of
the surface given in the volume definition.
* If the volume is a pure combinatorial type volume (i.e., not altered by any other volume by means of
operators), then the number of the side depends on a side numbering convention for the volumes of each
shape. The numbering conventions are then:
• for volumes with one side (spheres and toroids) the side number is 1;
• for cones, the number of the base is 1 and that of the body is 2;
• for cylinders with an axis u, the lower base is number 1, the upper base is number 2, and the cylindrical
side is number 3;
• for boxes, sides are numbered from 1 to 6 in the order -x, +x, -y, +y, -z, +z;
• for parallelepipeds, the sides are numbered from 1 to 6 in the order -u, +u, -v, +v, -w, +w, for u, v, and
w the three axes of the parallelepiped;
• for hexagonal prisms, the sides are numbered from 1 to 8. The sides orthogonal to the axis of the prism
are numbered 7 and 8 as axis (X, Y, or Z, depending on the case) increases. The other numbers are given
in a diagram for a HEXAZ. For HEXAX and HEXAY figures, circular permutation of the axes is required.
It is possible to use the POSITION option in the geometry command in order to establish a surface number
associated with a boundary point (the surface number is then given to the user).
Y
X
1
2
3
4
5
6
1
2
5
6
4
3
Figure 9.5: Numbering of sides for HEXAZ hexagons with angles θ = 0 and θ = 90
If the volume is a modified combinatorial volume (i.e., modified by operators), it only has the sides or
surfaces of the pure volume, i.e., the volume unmodified by operators apart from rotation and lattice (SMASH,
etc.).
Important: If the volume is a lattice type volume, it is now possible to specify side numbers. The combinatorial
definition conventions are re-used.

<!-- page 126 -->
VOLUME
ESCAPE(default)
ESCAPE interior
REFLECTION or ALBEDO
TRANSLATION
COSINE
EQUA (pure)
yes
yes
yes
no
yes
TORUS[X,Y,Z ]
yes
no
yes
no
yes
COMBI (pure)
yes
yes
yes
no
yes
SPHERE
yes
yes
yes
no
yes
BOX
yes
yes
yes
yes
yes
PARALLELEPIPEDE
yes
yes
yes
yes
yes
HEXA[X,Y,Z ]
yes
yes
yes
yes
yes
CYL[X,Y,Z]
yes
yes
yes
yes (bases)
yes
CYL
no (body)
CONE
yes
yes
yes
no
yes
TORUS
yes
no
no
no
no
RESC (pure)
yes
no
yes
no
yes
RESH (pure)
yes
no
yes
no
yes
ROTATION (pure)
yes
no
no
no
no
Table 9.1: Implemented boundary conditions
A surface can bound a large number of volumes. To avoid having to write a list of all the conditions for all
the volumes defined using a surface-based geometry and bounded by this surface, it is possible to use the
keyword ALL instead of the volume number. The code determines which volumes contain the surface and
assigns the appropriate conditions to them.
Starting from version 10, it is possible to use the keyword ALL_COMPLETE instead of the volume number. The
code applies the boundary condition to all the volumes including surface-based volumes, combinatorial type
volumes, lattice type volumes and rotation type volumes, even if the surface is crossing the volume. In other
words, with this keyword, the surface has the same properties than an additional surface.

## 9.3 ADDITIONAL BOUNDARY SURFACES

When a quarter or eighth of a geometry is to be defined (fuel assembly or reactor for instance), the surfaces
at which reflections are to occur may not be natural surfaces if volumes are pure combinatorial types. To
obtain the required volume, it would be necessary to use the VMINUS or SMASH operators. To avoid this
inconvenience, it is now possible to apply boundary conditions on surfaces that are not part of the volume
definition.
In such cases, the user must simply input the opposite of the number of the surface (the surface being defined
in the geometry, such as surfaces determining a surface-based volume). The code recognizes a surface with a
negative number as an additional surface.
A negative surface number can not be detected with ALL REFLECTION.
However, starting from version 10, this possibility is compatible with the keyword ALL_COMPLETE, see previous
section.
Criticality case of chapter 5
In the case of the criticality calculation described in chapter 5, all the boundary conditions are leakage, and
there is no BOUNDARY_CONDITION command.
