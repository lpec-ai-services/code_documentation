# CALCULATION VERIFICATION DEFINITIONS
<!-- source PDF pages 330-335 -->

<!-- page 330 -->
Chapter 23
CALCULATION VERIFICATION
DEFINITIONS
Definitions begin with the keyword CALCULATION.
This command is used to make a number of checks regarding:
• problem geometry (sub-command VOLUME);
• problem compositions (sub-command DENSITY).
• problem mass (sub-command MASS).
CALCULATION
*
(SET) VOLUME
Volume calculation parameters
END_VOLUME
*
DENSITY
Density calculation parameters
END_DENSITY
*
MASS
Mass calculation parameters
END_MASS
END_CALCULATION
where the keyword SET means that the values found by the calculation are assigned to volumes for the score
results (which are then given per cm3 for volume-based scores and by cm2 for surface-based scores).

## 23.1 VOLUME CALCULATIONS

To define calculation verifications, it is possible to request a calculation of the volumes defined in GEOMETRY
command. The volumes to be calculated are contained in a window defined in a reference frame specified by
the user.

<!-- page 331 -->
The syntax is as follows:
VOLUME
FRAME <FRAME_TYPE>
Ox Oy Oz
ix iy iz
(jx jy jz)
kx ky kz
WINDOW
Umin Vmin Wmin
Umax Vmax Wmax
PRECISION precision
MAX_POINTS maxpoints
SUM
Volume sum parameters
STORE_IN_FILE Flag
END_VOLUME
It is necessary to define:
• the window definition reference frame, defined using the type of coordinates (Cartesian, cylindrical or
spherical), the origin O, and the associated axes i, j, and k (see section 4.5);
• two points, corresponding to the minimum and maximum dimensions, define the window. These points
are Umin, Vmin, Wmin on the one hand and Umax, Vmax, Wmax on the other, with U, V, W being the
coordinates (x,y,z), (r,θ,z) or (r,φ,θ) depending on the type of reference frame selected;
• precision of the calculation relatively to the volume values;
• maximal number of sobol points for the volumes calculation. The default value for maxpoints is 109
points.
• SUM triggers the sum of volumes calculation. Volume sum parameters are needed for this option.
• STORE_IN_FILE is an optional keyword. If used calculated values are then stored in an ASCII file.
Flag is set to 0 to create a file with data stored in VOLSURF format suffixed by ".vs". Flag is set to 1
to create in input file of T4G suffixed by ".vvls". However values calculated with the SUM option are
not stored.
The calculation of the volumes is not exact but corresponds to an estimate of the actual volume with the
calculation based on an algorithm involving pseudo-random numbers.
The calculation is performed in reference frame (O,i,j,k), with the type of coordinates chosen. (Preference
shall be given to a calculation reference frame adapted to the geometry.): <FRAME_TYPE> can be CARTESIAN,
SPHERE, or CYLINDER.
The line jx jy jz is only given in the CARTESIAN case.

<!-- page 332 -->
In the case where the SUM is triggered, Volume sum parameters can be defined as follows:
SUM
nb-volu(1)
volu(1)...volu[nb-volu(1)]
SUM ALL
• The keyword SUM can be called as many times as wanted.
• The keyword ALL implies that there is nothing after except another SUM or END_VOLUME

## 23.2 DENSITY CALCULATIONS

It is also possible to request calculation of densities (in g/cm3) of compositions defined as the number of
atoms in the COMPOSITION command. It is necessary to determine whether the calculation relates to:
• all the compositions;
• only part of them.
The density calculation is an exact one:
ρ = ∑
isotopes
NiAi
N
where:
• Ni is the number of atoms per unit volume of isotope i;
• Ai is the atomic weight of isotope i;
• N is Avogadro’s number.
The densities of all the compositions can be requested:

<!-- page 333 -->
DENSITY
ALL
END_DENSITY
or requested only for nb(compo) compositions:
DENSITY
LIST
nb(compo)
name(compo1)
...
name(compon)
END_DENSITY

## 23.3 MASS CALCULATIONS

It is also possible to request calculation of mass (in g). The mass calculations are based on the previous
results of volume values and densities. Therefore theses calculations have to be defined before.
In particular one must be aware that the calculated mass are only the mass which are inside the window
defined in the volume calculation section.
Three different kinds of mass can be calculated. The mass of :
• a volume.
• a composition.
• a nucleus.
• an element.
The calculation parameters can be the keywords ALL or LIST following the syntax described in the density
section.

<!-- page 334 -->
MASS
COMPOSITION
Compositon calculation parameters
END_COMPOSITION
NUCLEI
Nuclei calculation parameters
END_NUCLEI
ELEMENT
Element calculation parameters
END_ELEMENT
END_MASS
Defining calculations for the criticality calculation example of chapter 5
CALCULATION
VOLUME
FRAME
CARTESIAN
0.
0.
0.
1.
0.
0.
0.
1.
0.
0.
0.
1.
WINDOW
-150.
-150.
-150
150.
150.
150.
PRECISION 0.01
END_VOLUME
DENSITY
LIST 4
INOX_STEEL
AIR
SOLUTION_U
CONCRETE
END_DENSITY
MASS
VOLUME
ALL
END_VOLUME
COMPOSITION
LIST 4
INOX_STEEL
AIR

<!-- page 335 -->
SOLUTION_U
CONCRETE
END_COMPOSITION
NUCLEI
ALL
END_NUCLEI
ELEMENT
LIST 2
U
O
END_ELEMENT
END_MASS
END_CALCULATION
