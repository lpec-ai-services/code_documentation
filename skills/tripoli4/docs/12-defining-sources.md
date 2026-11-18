# DEFINING SOURCES
<!-- source PDF pages 139-189 -->

<!-- page 139 -->
Chapter 12
DEFINING SOURCES
Calculation sources are defined between the keywords SOURCES_LIST and END_SOURCES_LIST.
The number of sources nb(sources) is then given, and each source is defined independently.
The structure is as follows:
SOURCES_LIST
nb(sources)
NORM norm(list)
SOURCE
Description of first source
END_SOURCE
...
SOURCE
Description of last source
END_SOURCE
END_SOURCES_LIST
Adding NORM norm(list) indicates the value of the norm for the entire system of nb(sources) sources.
If this instruction is not used, the norm equals Nlist = ∑i Ni where Ni is the norm (calculated or imposed) of
each source.

## 12.1 DEFINING A SOURCE

TRIPOLI-4® sources are factorized as follows:
S(r,Ω,E,t) = C ·S(r)·S(Ω)·S(E)·S(t)

<!-- page 140 -->
An exception to this scheme is the external source, see paragraph 12.8.
For each source, the spatial S(r), angular S(Ω), energy S(E), and time S(t) distributions are defined independently
. It is also possible to enter a normalization factor Ni for each source i, such that
Z Z Z Z
Si(r,Ω,E,t)drdΩdEdt = Ni.
If a global norm Nlist has been defined for the system, then the norms for each sources are relative ones. As
such, the norm of the source is:
Nsource =
Ni
∑i Ni
Nlist.
The syntax used to define a source is as follows:
SOURCE
#
INTENSITY norm(source)
#
COEFF coeff(source)
<PARTICLE_TYPE>
Description of spatial distribution: POINT or FACTORIZED
ANGULAR_DISTRIBUTION
Description of angular distribution
ENERGETIC_DISTRIBUTION
Description of energy distribution
TIME_DISTRIBUTION
Description of time distribution
END_SOURCE
where <PARTICLE_TYPE> equals NEUTRON, PHOTON, ELECTRON, or POSITRON. By default, the norm of the
source is the product of
Nsource = I(geometrical)·I(angular)·I(energy)·I(time)
where:
• the geometrical intensity I(geometrical) is the integral of the spatial distribution S(r) over the source
domain definition (intersection of volumes and the definition domain):
I(geometrical) =
Z
V(source) S(r)dr;
• angular intensity I(angular) is the integral of the angular distribution S(Ω):
I(angular) =
Z
4π S(Ω)dΩ;

<!-- page 141 -->
• energy intensity I(energy) is the integral of energy distribution S(E):
I(energy) =
Z
S(E)dE;
• time intensity I(time) is the integral of time distribution S(t):
I(time) =
Z
S(t)dt.
It is possible to impose a normalisation on a source (for source particles) using the keyword INTENSITY
followed by the norm. The user must then specify the norms of all the sources to ensure a consistent calculation
. It is also possible to modify the norm calculated by the code by a coefficient using the keyword COEFF.
INTENSITY and COEFF cannot be used simultaneously.

## 12.2 SPATIAL DISTRIBUTION

The source can be:
• a point source (a Dirac distribution);
• a tabulated spatial distribution source (discrete values);
• an analytical spatial distribution source (continuous values).
• a surface spatial distribution source (discrete values).
In the first case, the definition is extremely simple, in the other three it is necessary to specify an associated
reference frame.

### 12.2.1 POINT SOURCES

For a point source, it is sufficient to give the coordinates r0 = (X,Y,Z) of the source.
Syntax is as follows:
POINT X Y Z
Note: The source must not be placed on a boundary of the volume.
There are no other geometrical data (no VOLUME to be specified nor GEOMETRIC_DISTRIBUTION to be entered).
The geometrical intensity is 1 in this case, the distribution S(r) being a Dirac δ(r−r0).

### 12.2.2 DISTRIBUTED SOURCES

A factorized distributed source is introduced using the keyword FACTORIZED.

<!-- page 142 -->
#### 12.2.2.1 Definition context

A source is defined (with the exception of the point source case covered above) in a context created by a list
of volumes and a definition domain. The spatial extension of the source is the intersection of the volumes and
the domain. A particle is, therefore, emitted if it belongs to the definition domain and to a volume on the list.
An option ALL_VOLUMES_INSIDE_MESH allows any volume inside the domain to be an allowed emitter; this
allows for easy flat source definition in criticality calculations.
The domain is defined in a reference frame specific to each source, characterized by:
• an origin O′;
• three vectors defining an orthonormal reference frame: i, j, k;
• a reference frame associated with the vectors.
The reference frame can be Cartesian: a vector O’M is defined by its coordinates (x,y,z), projections of
O’M along axes i, j, k:
O′M = xi+yj+zk.
It can also be cylindrical, in which case the vector O’M is defined by its coordinates (r,θ,z) where r is the
normal of the projection O’M on the plane (i, j), θ is the angle between the projection (between 0 and 2π)
and the vector i, and z is the projection of O’M along axis k:
O′M = rcosθi+rsinθj+zk.
Finally, the reference frame can be spherical, in which case the vector O’M is defined by its coordinates
(r,φ,θ) where r is the normal of O’M, φ is the angle (between 0 and 2π) between the projection of O’M on
the plane (i, j) and the vector i, and θ is the angle between OM and the axis (i, k) (between 0 and π):
O′M = rcosφsinθi+rsinφsinθj+rcosθk.
See figures 4.1, 4.2 and 4.3.
Note: when a non-unit vector is entered to specify the reference frame, TRIPOLI-4® automatically renormalizes
it to 1.

#### 12.2.2.2 Syntax for a factorized source

The reference frame definition is introduced using the keyword FRAME, followed by the type of system chosen
(CARTESIAN, CYLINDER, or SPHERE), the coordinates of the origin of O’, and the vectors defining the
axes. It continues with either the keyword VOLUME (resp COMPOSITION) followed by the number of volumes
(resp number of compositions) and a list of volumes (resp list of compositions), or by the keyword
ALL_VOLUMES_INSIDE_MESH, or by the keyword ALL_FISSILE_VOLUMES_INSIDE_MESH. The definition of
the spatial distribution is then given along with associated description domain.
It can be followed by the keyword OPENMP and the number of processors intended for the calculation using
shared memory parallelism. This feature has a very specific usage. It can not currently be mixed with the
usual parallel mode of TRIPOLI-4. It can be used to accelerate the calculation of the norm of the factorized

<!-- page 143 -->
sources in mono-processor mode. The remaining part of the calculation will be in mono-processor. Using
shared memory parallelism, this option can only use the cores available on the launching node.
Syntax is as follows for a distributed source:
FACTORIZED
FRAME
<FRAME_TYPE>
O’x O’y O’z
ix iy iz
(jx jy jz)
kx ky kz
*
VOLUME
nb(volumes) volume(1)...volume(n)
*
COMPOSITION
nb(compositions) composition(1)...composition(n)
*
ALL_VOLUMES_INSIDE_MESH
*
ALL_FISSILE_VOLUMES_INSIDE_MESH
OPENMP nb_procs
GEOMETRIC_DISTRIBUTION
Description of geometrical distribution:
NO_GEOMSOURCE_WARNING
SOBOL_POINTS nb(points)
TABULATED or ANALYTICAL or TRIANGLE
where <FRAME_TYPE> equals CARTESIAN, CYLINDER, or SPHERE. The line jx jy jz is only required if
CARTESIAN is chosen.
Note:
Starting from TRIPOLI-4® version 9, points are sampled uniformly in the Physical (Euclidean) space for all
types of frames; previously they were distributed uniformly in the space of parameters U, V, W.
It is possible to use a virtual number for the source volume. In this case, the source is the intersection of
the virtual volume and the domain. This makes it possible to avoid defining a geometry only for the purpose
of defining sources when the domain cannot be given analytically. Extreme care is required, however, with
this property, since virtual volume definition errors are detected neither in the running of the code nor in the
display. Manipulation of the operators must be avoided.
The user must, however, check the volume of the source (volume-domain intersection) using the geometrical
intensity, given in the output.
Important special application:
In the case of a lattice, it should be noted that:

<!-- page 144 -->
• a volume contained in a reference cell is repeated: the numbers of the volumes of the reference cell are
used for all the repeated cells of the lattice. It is not possible to distinguish a particular cell, including
the reference cell;
• the lattice number can be used: this number then corresponds to all the volumes making up the lattice.
This is because the lattice case is similar to the virtual volume case. It does, however, include the benefits
of tests and a display.
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
Figure 12.1: Source in a lattice
Example: drawing 12.1 corresponds to the sequence
TYPE 1 BOX 2 1 1
VOLU 1 COMBI 1 1 0.5 0 ENDV
TYPE 2 SPHERE 0.4
VOLU 2 COMBI 2 1 0.5 0 SMASH 1 1 ENDV
VOLU 3 RESC VOLU 1 2 3 1
ENDV
The volume is defined as the intersection of the domain (0 < x < 1,0 < y < 2,−0.5 < z < 0.5) and one of the
following:
• volumes 1 and 2 (VOLU 2 1 2 ), as they are repeated in the lattice. If the sphere were to be the only
emitting body, this would be replaced by VOLU 1 2
• lattice 3 (VOLU 1 3 ), which in this case represents all the volumes of a lattice

<!-- page 145 -->
#### 12.2.2.3 Surface, analytical and tabulated distributions

Once the reference frame has been specified, a set of coordinates (u,v,w) is available, in either Cartesian
(x,y,z), cylindrical (r,θ,z), or spherical (r,φ,θ) form. A distribution can be defined by tabulated values, by
an analytical function or with surface sources.
The optional keyword SOBOL_POINTS is used to refine the calculation of the geometric distribution. The
default value for the number of points (produced from a sobol generator) used in this calculation is 50000 for
the three different sources.
When the intersection between the volumes and the domain of the source is small with respect to the
source domain, the code will generate a warning message each time more than 100 consecutive sampled
source points are not in the intersection.
It is possible to deactivate these messages using the
NO_GEOMSOURCE_WARNING command.
This may result from an inconsistency between the source domain and the volumes, but it may also result
from a very fragmented source structure. In the latter case, it may prove advantageous to enhance the source
estimation precision using the command SOBOL_POINTS.
Tabulated distribution.
This is introduced using the keyword TABULATED.
A tabulated distribution is a distribution in discrete form in a mesh that describes the definition domain of the
source.
The number of neutrons or photons emitted per unit volume in the cell is associated with each cell.
The user must indicate the discretization for each component (u,v,w).
Tabulation can be specified in three different manners:
• the data for intensity I(cell) is factorized over three components Iu, Iv, Iw.
I(cell) = Iu(ucentre)×Iv(vcentre)×Iw(wcentre)×Volumeemitter(cell);
• the data for intensity on a component and a plane
I(cell) = Iu(ucentre)×Iv,w(vcentre,wcentre)Volumeemitter(cell);
• the data for intensity in space (to be given for each cell)
I(cell) = Iu,v,w(ucentre,vcentre,wcentre)×Volumeemitter(cell).
The data for Iu ×Iv ×Iw , Iu ×Iv,w, or Iu,v,w is in particles per cm3 (and in steradians per MeV per second).
Volumeemitter(cell) is the intersection volume of the cell and the source volumes.
The intersection of the cell and the source volumes, therefore, homogeneously emits particles with a total
intensity of I(cell). The non-source part of the cell does not contribute to the emission.
In Figure 12.2, cells a1, b1, c1, a2, b2, c2, a3, b3, c3 emit particles. Only in cell b2 are particles emitted
at all points (for simplification, the third component is discarded), the other cells only emit particles in their
shaded areas. Cells d1,d2, and d3 do not emit any particles.

<!-- page 146 -->
3
a
b
c
d
1
2
Figure 12.2: The volume is shown in yellow, and the grid represents the domain
The coordinate system can be Cartesian, cylindrical, or spherical in the tabulated case.
A) Intensity data given on the three components
This possibility is selected using the keyword: TYPE F_U_V_W .
Important: It must be borne in mind that nb(u) coordinates along the u axis means nb(u)-1 intervals, hence
nb(u)-1 intensity values along the axis. The same applies to the other coordinates.
GEOMETRIC_DISTRIBUTION
SOBOL_POINTS nb(points)
TABULATED
TYPE F_U_V_W
VAR_U <NAME_U>
nb[coord(u)]
u1...unb(u)
VAR_V <NAME_V>
nb[coord(v)]
v1...vnb(v)
VAR_W <NAME_W>
nb[coord(w)]
w1...wnb(w)
F_U Iu(1)...Iu(nb(u)−1)
F_V Iv(1)... Iv(nb(v)−1)
F_W Iw(1)... Iw(nb(w)−1)
Where <NAME_U>, <NAME_V> and <NAME_W> are equal to X, Y, or Z in Cartesian coordinates, to R, RTHETA, or
RPHI in Spherical coordinates, or to R, RTHETA, or Z in Cylindrical coordinates .
The value of the source distribution S(r) in a cell (i, j,k) is given by Iu(i) × Iv(j) × Iw(k). When the source
distribution is integrated over the cell volume, it is weighted by the portion of volumes selected for source
emission (see the definition of FACTORIZED, page 142).

<!-- page 147 -->
Example with Cartesian coordinates:
GEOMETRIC_DISTRIBUTION
TABULATED
TYPE F_U_V_W
VAR_U X
3
1 2 3
VAR_V Y
3
1.5 3.5 4.5
VAR_W Z
2
0 10
F_U 1 0.5
F_V 0.8 0.3
F_W 1
B) Intensity data given for 1 component and 1 plane
This possibility is selected using the keyword: TYPE F_U_VW.
GEOMETRIC_DISTRIBUTION
SOBOL_POINTS nb(points)
TABULATED
TYPE F_U_VW
VAR_U <NAME_U>
nb[coord(u)]
u1...unb(u)
VAR_V <NAME_V>
nb[coord(v)]
v1...vnb(v)
VAR_W <NAME_W>
nb[coord(w)]
w1...wnb(w)
F_U Iu(1)...Iu(nb(u)−1)
F_VW Ivw(1,1)...Ivw(nb(v)−1,nb(w)−1)
Where <NAME_U>, <NAME_V>, and <NAME_W> are equal to X, Y or Z in Cartesian coordinates, to R, RTHETA, or
RPHI in Spherical coordinates, or to R, RTHETA, or Z in Cylindrical coordinates .
The value of the source distribution S(r) in a cell (i, j,k) is given by Iu(i) × Ivw(j,k). When the source
distribution is integrated over the cell volume, it is weighted by the portion of volumes selected for source
emission (see the definition of FACTORIZED, page 142).

<!-- page 148 -->
This is similar to the F_U_V_W case, but instead of nb(v)-1 values of F_V and nb(w)-1 values of F_W, the
[nb(v)-1]×[nb(w)-1] values of F_VW are given. The values F_VW(v,w) are to be entered in the following
order (with constant W and V varied, see Figure 12.3):
F_VW(1,1) F_VW(2,1)...F_VW(nb(v)-1,1) then
F_VW(1,2) F_VW(2,2)...F_VW(nb(v)-1,2) then
...
F_VW(1,nb(w)-1) F_VW(2,nb(w)-1)...F_VW(nb(v)-1,nb(w)-1)
W
V
1,1
2,1
3,1
4,1
4,2
4,3
3,3
3,2
2,2
2,3
1,3
1,2
Figure 12.3: The data are entered from left to right and from bottom to top: (1,1), (2,1), (3,1), (4,1), (1,2), (2,2), etc.

<!-- page 149 -->
C) Intensity data given per cell
This possibility is selected using the keyword: TYPE F_UVW.
GEOMETRIC_DISTRIBUTION
SOBOL_POINTS nb(points)
TABULATED
TYPE F_UVW
VAR_U <NAME_U>
nb[coord(u)]
u1...unb(u)
VAR_V <NAME_V>
nb[coord(v)]
v1...vnb(v)
VAR_W <NAME_W>
nb[coord(w)]
w1...wnb(w)
F_UVW Iuvw(1,1,1)...Iuvw(nb(u)−1,nb(v)−1,nb(w)−1)
Where <NAME_U> , <NAME_V> , <NAME_W> are equal to X , Y, or Z in Cartesian coordinates, to R, RTHETA, or
RPHI in Spherical coordinates, or to R, RTHETA, or Z in Cylindrical coordinates .
The value of the source distribution S(r) in a cell (i, j,k) is given by Iuvw(i, j,k). When the source distribution
is integrated over the cell volume, it is weighted by the portion of volumes selected for source emission (see
the definition of FACTORIZED, page 142).
Once again, this is similar to the F_U_V_W case, but instead of nb(u)-1 values of F_U, nb(v)-1 values of
F_V and nb(w)-1 values of F_W, the
[nb(u)-1]×[nb(v)-1]×[nb(w)-1]
values of F_UVW are given. The values F_UVW(u,v,w) are to be entered in the following order (see Figures
12.4 and 12.5):
F_UVW(1,1,1) F_VW(2,1,1)...F_VW(nb(u)-1,1,1)
F_UVW(1,2,1) F_VW(2,2,1)...F_VW(nb(u)-1,2,1)
...
F_UVW(1,nb(v)-1,1) F_VW(2,nb(v)-1,1)...F_VW(nb(u)-1,nb(v)-1,1)
then
F_UVW(1,1,2) F_VW(2,1,2)...F_VW(nb(u)-1,1,2)
F_UVW(1,2,2) F_VW(2,2,2)...F_VW(nb(u)-1,2,2)
...
F_UVW(1,nb(v)-1,2) F_VW(2,nb(v)-1,2)...F_VW(nb(u)-1,nb(v)-1,2)
then...
F_UVW(1,1,nb(w)-1) F_VW(2,1,nb(w)-1)...F_VW(nb(u)-1,1,nb(w)-1)
F_UVW(1,2,1) F_VW(2,2,1)...F_VW(nb(u)-1,2,1)
...

<!-- page 150 -->
F_UVW(1,nb(v)-1,nb(w)-1)
F_VW(2,nb(v)-1,nb(w)-1)...F_VW(nb(u)-1,nb(v)-1,nb(w)-1)
W
V
U
1,1,1
1,2,1
1,3,1
2,3,1
2,2,1
3,2,1
2,1,1
3,1,1
3,3,1
4,3,1
4,2,1
4,1,1
Figure 12.4: First from left to right and from bottom to top (first sweep along U, line by line). Top view
W
U
V
1,1,2
2,2,2
3,3,2
4,3,2
3,2,2
3,1,2
4,2,2
4,1,2
2,3,2
1,3,2
1,2,2
2,1,2
Figure 12.5: Then from left to right and from bottom to top (first sweep along U, line by line). Top view
Helpers for syntax entry.
In order to simplify the data entry in the sources and thus to simplify the consistency
between the mesh of sources and the mesh of the KIJ matrix feature (optional), two keywords has been added:
UPTO_LIN and REPEAT.
The use of "x UPTO_LIN n y" replaces in input the part "UPTO_LIN n" by n values linearly interpolated between
x, excluded and y included. It leads, thus, to n+1 values regularly disposed between x and y included.
The use of "x REPEAT n" replaces in input the part "REPEAT n" by n values of x, thus leading to n + 1 times
the value x.
For example, we could express a source with a uniform density on a grid of 11x11x9 (=1089) cells between
[0, 275] in x, [0, 275] in y, and [0, 100] in z using the following syntax:
TYPE F_UVW

<!-- page 151 -->
VAR_U X 12 0 UPTO_LIN 11 275
VAR_V Y 12 0 UPTO_LIN 11 275
VAR_W Z 10 0. UPTO_LIN 9 100.
F_UVW
1. REPEAT 1088

<!-- page 152 -->
Analytical distribution.
An analytical distribution is a continuous distribution in the source definition domain.
This distribution S(r) is defined by an algebraic formula and a definition domain for the formula. The syntax
is as shown in the box, below
GEOMETRIC_DISTRIBUTION
ANALYTICAL
FUNCTION = ...;
DOMAIN = ...;
and using the following variable names
• in a Cartesian reference frame: X , Y , Z;
• in a cylindrical reference frame: R, RTHETA, Z (RTHETA must be between 0 and 2π);
• in a spherical reference frame: R, RPHI, RTHETA (RPHI must be between 0 and 2π and RTHETA between
0 and π).
Notes:
The code does not check the consistency of the definition domain with the algebraic formula. This task is left
to the user. In each reference frame, formulas and domains are expressed using variables.
The source distribution S(r) is given, not its volume-integrated value.
The default number of points used in the geometrical source distribution is now 50000, whereas it was 5000
in version 4.4 (and earlier versions) of TRIPOLI-4®. The processing of the factorized source initialization for
an analytical distribution is thus more precise, but may also be relatively slow. For comparisons with earlier
versions, set the SOBOL_POINTS value to 5000. See in subsection 12.2.2 how to change the SOBOL_POINTS
default value.
Important: If an expression begins with a −sign, a 0 must be placed before it: EXP(0-X), for exp(−x) for
instance.
The allowed operators in the formula expression are (LOG is the natural logarithm):
+ , - , *, /, SH, CH, SIN, COS, EXP, LOG, SQRT, ().
The relationships accepted in domains definitions are: < and >.
Inputs are separated by commas.
Examples
Source in exp[−(x+y)] (Cartesian coordinates):
GEOMETRIC_DISTRIBUTION
ANALYTICAL
FUNCTION= EXP(0-(X+Y));
DOMAIN=0<X<1,0<Y<2,0<Z<1;

<!-- page 153 -->
Source in exp(−r) (cylindrical coordinates):
GEOMETRIC_DISTRIBUTION
ANALYTICAL
FUNCTION= EXP(0-R);
DOMAIN=0<R<1,0<RTHETA<6.28,0<Z<1;
Source in exp(−r) (spherical coordinates):
GEOMETRIC_DISTRIBUTION
ANALYTICAL
FUNCTION= EXP(0-R);
DOMAIN=0<R<1,0<RPHI<6.28,0<RTHETA<3.14;
Note: Care must be taken not to omit the semi-colons after the FUNCTION and DOMAIN commands.
Surface distribution.
A surface distribution can be defined thanks to a tessalation process. The idea consists in
building a surface source by splitting this source into (small) triangles. Therefore, to declare a surface source,
a file with an arbitrary name (called here surface_source_file.txt) has to be present together with TRIPOLI-4
input file in the current directory. This surface file is given here:
t4 triangular mesh file
version 1.0
NUMBER_OF_TRIANGLES 2
0.
30.
30.
0.
-30.
30.
0.
-30.
-30.
0.
30.
30.
0.
30.
-30.
0.
-30.
-30.
where the two first lines contain arbitrary comments, the third line contains the keyword
NUMBER_OF_TRIANGLES followed by the number of triangles used to describe the source (here 2) and all the
other lines contain the triangles definitions thanks to the 9 coordinates of their angles. Those coordinates are
the one of the three vertices, each one being described by its position in (x,y,z). In the previous example, if
one consider the first triangle, its first vertex is located in (x=0.,y=30.,z=30.), its second vertex is located in
(x=0.,y=-30.,z=30.) and its last vertex is located in (x=0.,y=-30.,z=-30.). Fig. 12.6 illustrates this example.
Once this surface source file defined, the syntax used in the TRIPOLI-4 input file is (with the SOBOL_POINTS
value set to 5000):
GEOMETRIC_DISTRIBUTION
SOBOL_POINTS 5000
TRIANGLE
FILE surfacic_source_file.txt

<!-- page 154 -->
(0,−30,30)
(0,30,30)
(0,30,−30)
(0,−30,−30)
z
y
Figure 12.6: Square source made by two triangles
Note: The intensity is uniform over all triangles of a same source. To declare triangles with different intensities
, different sources have to be declared.

## 12.3 ANGULAR DISTRIBUTION

There are five different types of angular distribution (Dirac, isotropic, rays, tabulated and analytical). An
explanation of variables and angles definitions for the different types of frame can be found in section 4.5.

### 12.3.1 DIRAC

This is the single emission direction expressed in the form of a vector of coordinates (ωx,ωy,ωz) given in
the geometrical reference frame in the case of a point source, or given in the source frame in the case of a
spatially distributed source. The syntax is as follows:
ANGULAR_DISTRIBUTION
MONO_DIR
ωx ωy ωz
The distribution S(Ω) is a Dirac distribution, whose integral over the solid angle (angular intensity) is equal
to 1.

<!-- page 155 -->
### 12.3.2 UNIFORM DISTRIBUTION

Important: The distribution S(Ω) is a constant such that the angular intensity equals 4π.
This corresponds to an isotropic emission, written as follows:
ANGULAR_DISTRIBUTION
ISOTROPIC

### 12.3.3 RAY DISTRIBUTION

This option can be used to define a source distributed on a list of discrete angles. It is introduced using
DISCRETE_PROBABILITY.
12.3.3.1
Discrete µ
The source is defined as a function of µ = cos(θ), where the variable θ is the angle relative to axis Oz:
• for a point source: axis OZ of the geometrical reference frame;
• for a spatially distributed source, the axis carried by k (see figure 4.3).
The syntax is as follows :
ANGULAR_DISTRIBUTION
DISCRETE_PROBABILITY
DISCRETE_MU
nb(angles)
µ0 I0
...
µnb(angles)−1 Inb(angles)−1
The angular distribution is the sum of Dirac distributions whose total intensity is 1.
S(µ) = ∑nb
i=0 Iiδ(µ−µi)/∑nb
i=0 Ii
12.3.3.2
Discrete φ
The source is defined as a function of φ. φ is the angle relative to axis Ox:
• for a point source: axis OX of the geometrical reference frame;
• for a spatially distributed source, the axis carried by i (see figure 4.3).

<!-- page 156 -->
The syntax is as follows :
ANGULAR_DISTRIBUTION
DISCRETE_PROBABILITY
DISCRETE_PHI
nb(angles)
φ0 I0
...
φnb(angles)−1 Inb(angles)−1
The angular distribution is the sum of Dirac distributions whose total intensity is 1.
S(φ) = ∑nb
i=0 Iiδ(φ−φi)/∑nb
i=0 Ii

### 12.3.4 TABULATED DISTRIBUTIONS

This is introduced using (TABULATED or) MU_TABULATED or PHI_TABULATED.
12.3.4.1 µ tabulated distribution
Tabulation provides the discretized distribution over an interval of µ = cos(θ). Here, the variable θ is the
angle with respect to axis Oz:
• for a point source: axis OZ of the geometrical reference frame;
• for a spatially distributed source, the axis carried by k (see figure 4.3).

#### 12.3.4.2 Syntax

The principle of definition is identical to that for the input of a tabulated response function, as described in
Section 13.4, option DATA, containing a precise definition. The variable µ = cosθ replaces the energy, and
the angular distribution values replace the cross-sections. The syntax is, therefore, as follows (the µ must be
given in increasing order) :

<!-- page 157 -->
ANGULAR_DISTRIBUTION
MU_TABULATED
SOURCE_WEIGHTING
nb(points) nb(inter)
<MODE_INTERPOLATION(1)> num[limsup(1)]
...
<MODE_INTERPOLATION(nbinter)> num[limsup(nbinter)]
µ0 value0 F0
...
µnb(points)−1 valuenb(points)−1 Fnb(points)−1
Notes:
• Starting from TRIPOLI-4v8, new keyword MU_TABULATED is available allowing the user to be explicit
about the chosen angle. However, keyword TABULATED is still available (designating µ angle).
• The keyword SOURCE_WEIGHTING is optional and only available for the interpolation mode
IN_NO_INTERPOLATION (histogram). It allows for source angle biasing: the sampling of certain µ angle
ranges of the tabulated distribution can be enhanced in this way. When this option is requested, Fx
parameters have to be input at the end of the present command block. Note that the biased distribution
can then be checked by requesting a FIXED_SOURCE_EMISSION score (see chapters 13 and 15). Standard
variance reduction techniques (see chapter 17) are not compatible with the SOURCE_WEIGHTING
option, whereas source energy biasing (see subsection 12.4.7) and source angle biasing can be requested
together.
• Fx values have to be given only when the keyword SOURCE_WEIGHTING is present in the command block.
These values are multiplicative factors weighting the natural probabilities of the angle distribution. For
example a factor 10 makes the sampling of the given angle range 10 times more probable than with the
natural probability. These factors have to be defined for each angle range x of the tabulated distribution
and are 1 by default if the keyword SOURCE_WEIGHTING is not used. To deal with the resulting lower
weights of certain particles, the Russian roulette threshold of the simulation may be lowered (see chapter
22, an order of magnitude being 0.8/Fmax if the biggest factor defined Fmax is bigger than 1).
• <MODE_INTERPOLATION> belongs to the list {IN_NO_INTERPOLATION, IN_LIN_LIN, IN_LIN_LOG,
IN_LOG_LIN, IN_LOG_LOG};
• nb(points) is the number of points, and nb(inter) the number of different interpolation ranges;
• Mode <MODE_INTERPOLATION(1)> applies from µ0 to µnum[limsup(1)];
• Mode <MODE_INTERPOLATION(j)> applies from µnum[limsup(j−1)] to µnum[limsup(j)]
where num[limsup(i)] is an integer, the index to the point in the list of given (µi,valuei) pairs pairs
(Caution: the numbering begins at 0).

<!-- page 158 -->
• The value of the last couple (µnb(points)−1, valuenb(points)−1) is untapped when <MODE_INTERPOLATION>
is IN_NO_INTERPOLATION.
It is the angular distribution S(Ω) which is tabulated, and not the angular intensity.
12.3.4.3 φ tabulated distribution
Tabulation provides the discretized distribution over an interval of φ. Here, the variable φ is the angle with
respect to axis Ox:
• for a point source: axis OX of the geometrical reference frame;
• for a spatially distributed source, the axis carried by i (see figure 4.3).

#### 12.3.4.4 Syntax

The principle of definition is identical to that for the input of a tabulated response function, as described in
Section 13.4, option DATA, containing a precise definition. The variable φ replaces the energy, and the angular
distribution values replace the cross-sections. The syntax is, therefore, as follows (the φ must be given in
increasing order).
ANGULAR_DISTRIBUTION
PHI_TABULATED
SOURCE_WEIGHTING
nb(points) nb(inter)
<MODE_INTERPOLATION(1)> num[limsup(1)]
...
<MODE_INTERPOLATION(nbinter)> num[limsup(nbinter)]
φ0 value0 F0
...
φnb(points)−1 valuenb(points)−1 Fnb(points)−1
Notes:
• The keyword SOURCE_WEIGHTING is optional and only available for the interpolation mode
IN_NO_INTERPOLATION (histogram). It allows for source angle biasing (the meaning is similar as for
the previous µ tabulated distribution).
• Fx values have to be given only when the keyword SOURCE_WEIGHTING is present in the command block
and their meaning is similar as for the previous µ tabulated distribution).
• <MODE_INTERPOLATION> belongs to the list {IN_NO_INTERPOLATION, IN_LIN_LIN, IN_LIN_LOG,
IN_LOG_LIN, IN_LOG_LOG};

<!-- page 159 -->
• nb(points) is the number of points, and nb(inter) the number of different interpolation ranges;
• Mode <MODE_INTERPOLATION(1)> applies from φ0 to φnum[limsup(1)];
• Mode <MODE_INTERPOLATION(j)> applies from φnum[limsup(j−1)] to φnum[limsup(j)]
where num[limsup(i)] is an integer, the index to the point in the list of given (φi,valuei) pairs pairs
(Caution: the numbering begins at 0).
• The value of the last couple (φnb(points)−1, valuenb(points)−1) is untapped when <MODE_INTERPOLATION>
is IN_NO_INTERPOLATION.
It is the angular distribution S(Ω) which is tabulated, and not the angular intensity.

### 12.3.5 2D TABULATED DISTRIBUTION

This is introduced using 2D_TABULATED. 2D Tabulation provides the discretized distribution over a grid of
µ = cos(θ) and of φ.
Here, the variable θ is the angle with respect to axis Oz:
• for a point source: axis OZ of the geometrical reference frame;
• for a spatially distributed source, the axis carried by k (see figure 4.3).
The variable φ is the angle with respect to axis Ox:
• for a point source: axis OX of the geometrical reference frame;
• for a spatially distributed source, the axis carried by i (see figure 4.3).

#### 12.3.5.1 Syntax

The syntax is as follows :
ANGULAR_DISTRIBUTION
2D_TABULATED
nb(bounds(µ grid)) nb(bounds(φ grid))
bound(1(µ grid)) ...bound(n(µ grid))
bound(1(φ grid)) ...bound(n(φ grid))
value(µ0,φ0) value(µ0,φ1) ... value(µ0,φ(nb(bounds(φ grid))−1))
value(µ1,φ0) value(µ1,φ1) ... value(µ1,φ(nb(bounds(φ grid))−1))
...
value(µ(nb(bounds(µ grid))−1),φ0) value(µ(nb(bounds(µ grid))−1),φ1) ... value(µ(nb(bounds(µ grid))−1),φ(nb(bounds(φ grid))−1))
Note:
• value(µx,φx) is the angular distribution corresponding to the cell (µx,φx).

<!-- page 160 -->
### 12.3.6 ANALYTICAL DISTRIBUTION

The distribution S(Ω) is expressed using an algebraic formula described in a manner similar to that used for
geometrical distribution. In each reference frame, the formulas and domains are expressed using variables:
PHI and THETA (or MU = cos(THETA )).
These variables correspond to the angles φ (between 0 and 2π) and θ (between 0 and π) defined for a spherical
reference frame, whatever the reference frame chosen. The axes are those of reference frame OX,OY,OZ in
the case of a point source. Furthermore:
PHI is the angle with respect to Ox:
• for a point source: axis OX of the geometrical reference frame;
• for a spatially distributed source: the axis carried by i (see reference frame figures)
THETA is the angle with respect to Oz:
• for a point source: axis OZ of the geometrical reference frame;
• for a spatially distributed source: the axis carried by k (see reference frame figures).
Notes:
In the case of variables θ and φ, the integral of the sources is calculated as:
I(angular) =
Z 2π
φ=0
Z π
θ=0 S(θ,φ)dθdφ
where S(θ,φ) is given by the user.
An isotropic distribution is, therefore, defined by a function S(θ,φ) = sinθ, and not S(θ,φ) = 1.
In the case of variables µ = cosθ and φ, the integral of the sources is calculated as:
I(angular) =
Z 2π
φ=0
Z 1
µ=−1 S(µ,φ)dµdφ
Here the isotropic distribution is defined by a function S(µ,φ) = 1.
A distinction must be made between PHI and THETA on the one hand and RPHI and RTHETA on the other. The
latter are only used when the definition reference frame is spherical. In the case of a cylindrical reference
frame, the user must distinguish between the cylindrical definition of angle θ for spatial distribution (RTHETA)
and the spherical definition for angular distribution (THETA ): these are not the same angles.
The operators in the formula expression are the following (LOG is the natural logarithm):
+ , -, * , /, SH, CH, SIN, COS, EXP, LOG, SQRT, (). The acceptable relationships in domain definitions are: <,
>.
Important: If an expression begins with a −sign, a 0 must be placed before it: EXP(0-X), for exp(−x) for
instance.

<!-- page 161 -->
ANGULAR_DISTRIBUTION
ANALYTICAL
FUNCTION = ...;
DOMAIN = ...;
Example (source in sin(θ), φ between 0 and 2π, θ between 0 and π):
ANGULAR_DISTRIBUTION
ANALYTICAL
FUNCTION= SIN(THETA);
DOMAIN=0<PHI<6.28,0<THETA<3.14;

<!-- page 162 -->
## 12.4 ENERGY DISTRIBUTION

Distributions can be expressed in seven different ways (Dirac, line spectrum, band emission, Gauss Spectrum,
Watt spectrum, Maxwell spectrum, tabulated spectrum, and analytical spectrum).

### 12.4.1 DIRAC

This corresponds to a mono-kinetic source, given by a real number. The syntax is as follows:
ENERGETIC_DISTRIBUTION
SPECTRUM
MONOKINETIC
E0
The energy distribution is a Dirac S(E) = δ(E −E0), whose intensity is 1.

### 12.4.2 LINE SPECTRUM

This corresponds to a list of Dirac distributions and expressed using a series of real number pairs (Energy-
Intensity). The syntax is as follows:
ENERGETIC_DISTRIBUTION
SPECTRUM RAY_SPECTRUM
nb(of lines)
E0 I0
...
Enb(lines)−1 Inb(lines)−1
The energy distribution is the sum of Dirac distributions.
S(E) = ∑nb
i=0 Iiδ(E −Ei)

### 12.4.3 UNIFORM DISTRIBUTION

This corresponds to a uniform energy emission distribution between two energy values that are specified by
the user. The syntax is as follows:

<!-- page 163 -->
ENERGETIC_DISTRIBUTION
SPECTRUM
BAND
Esup Ein f
The energy distribution is S(E) = U(Esup,Ein f ), such that S(E) = 1 if the energy is between the bounds, and
S(E) = 0 otherwise. The intensity, therefore, equals Esup −Ein f .

### 12.4.4 GAUSS SPECTRUM

This corresponds to a Gauss energy emission distribution at the energy Emean with a standard deviation σ.
The energy distribution is S(E) = N (Emean,σ). N is the normal distribution centered on Emean with the
standard deviation σ. Emean and σ are specified by the user using the following directives:
N (Emean,σ) =
1
√
2πσe−(E−Emean)2
2σ2
=
1
√πae−(E−Emean)2
a2
The syntax is as follows:
ENERGETIC_DISTRIBUTION
SPECTRUM
GAUSS_SPECTRUM
a Emean

### 12.4.5 WATT SPECTRUM

This corresponds to a distribution expressed in the form of a Watt spectrum, i.e.,
S(E) = C ·e−aEsh
√
bE
where C = 2e−b
4a a
3
2
√
πb.
ENERGETIC_DISTRIBUTION
SPECTRUM
WATT_SPECTRUM
PARAM Esup Ein f a b

<!-- page 164 -->
It is possible to input the a and b coefficients (both expressed in MeV−1) of the spectrum (warning: it is
common to find "1
a" in other codes instead of the definition of "a"), and the energy range for the particle
emission. For further information on the subject refer to [1].
By default:
Esup=20 MeV ,
Einf =1.E-11 MeV,
a=1.02 MeV−1 and
b=2.286 MeV−1.
This corresponds to a fast 235U spectrum.
Other common examples of choice for a and b parameters are as follows:
a=1.012 MeV−1 and b=2.249 MeV−1 for a thermal 235U spectrum
a=1.035 MeV−1 and b=2.842 MeV−1 for a thermal 239Pu spectrum
a=1.02 MeV−1 and b=2.12 MeV−1 for a 238U spectrum
a=1.02 MeV−1 and b=2.328 MeV−1 for a 233U spectrum
a=1.02 MeV−1 and b=1.496 MeV−1 for a 232Th spectrum.
It should be noted that the option of fission spectrum from the evaluation may also be a way to define
a Watt spectrum (see subsection 12.4.9).

### 12.4.6 MAXWELL SPECTRUM

This corresponds to a distribution expressed as a Maxwell spectrum between energy bounds Esup and Einf.
S(E) = C ·e−E
θ √
E
where C = 1
It is necessary to use θ = kT, with θ being the temperature of the spectrum translated into MeV. The energy
bounds are Esup and Einf.
ENERGETIC_DISTRIBUTION
SPECTRUM
MAXWELL_SPECTRUM
θ Esup Ein f

### 12.4.7 TABULATED SPECTRUM

This corresponds to a distribution whose values are given at a certain number of points and interpolated
between them. The syntax used to define such a spectrum corresponds to that used for tabular angular distri-

<!-- page 165 -->
bution (based on the input of a response function with DATA, as described in full in Chapter 13). Distribution
is given as a function of energy (by order of increasing energy).
ENERGETIC_DISTRIBUTION
SPECTRUM INTERPOLATED
SOURCE_WEIGHTING
GROUP_PROBABILITY
nb(points) nb(inter)
<MODE_INTERPOLATION(1)>
num[limsup(1)]
...
<MODE_INTERPOLATION(nbinter)>
num[limsup(nbinter)]
E0 value0 F0
...
Enb(points)−1 valuenb(points)−1 Fnb(points)−1
• the keyword SOURCE_WEIGHTING is optional and only available for the interpolation mode
IN_NO_INTERPOLATION (histogram). It allows for source energy biasing: the sampling of certain energy
groups of the tabulated distribution can be enhanced in this way. When this option is requested, Fx
parameters have to be input at the end of the present command block. Note that the biased distribution
can then be checked by requesting a FIXED_SOURCE_EMISSION score (see chapters 13 and 15). Standard
variance reduction techniques (see chapter 17) are not compatible with the SOURCE_WEIGHTING
option, whereas source energy biasing and source angle biasing (see subsection 12.3.4) can be requested
together.
• the keyword GROUP_PROBABILITY is optional and only available for the interpolation mode
IN_NO_INTERPOLATION (histogram).
It is used in order to enter directly the values in particles/s.
SOURCE_WEIGHTING and GROUP_PROBABILITY options can be used together.
• Fx values have to be given only when the keyword SOURCE_WEIGHTING is present in the command block.
These values are multiplicative factors weighting the natural probabilities of the energy distribution. For
example a factor 10 makes the sampling of the given group 10 times more probable than with the natural
probability. These factors have to be defined for each energy group x of the tabulated distribution and
are 1 by default if the keyword SOURCE_WEIGHTING is not used. To deal with the resulting lower weights
of certain particles, the Russian roulette threshold of the simulation may be lowered (see chapter 22, an
order of magnitude being 0.8/Fmax if the biggest factor defined Fmax is bigger than 1).
• <MODE_INTERPOLATION>
belongs
to
list
{IN_NO_INTERPOLATION,
IN_LIN_LIN,
IN_LIN_LOG,
IN_LOG_LIN, IN_LOG_LOG};
• nb(points) is the number of points, and nb(inter) the number of different interpolation ranges;

<!-- page 166 -->
• Mode <MODE_INTERPOLATION(1)> applies to E0 at
Enum[limsup(1)];
• Mode <MODE_INTERPOLATION(j)> applies to Enum[limsup(j−1)] at
Enum[limsup(j)] where num[limsup(i)] is the index in the list of given (Ei,valuei) pairs. (Caution: numbering
begins at 0).
• The value of the last couple (Enb(points)−1, valuenb(points)−1) is untapped when <MODE_INTERPOLATION>
is IN_NO_INTERPOLATION.
If the keyword GROUP_PROBABILITY is not used, the tabulated values must be expressed in particles/MeV/s.
Warning: The units conventions for TRIPOLI-3 correspond to use of the keyword GROUP_PROBABILITY.
If the user wants to use a spectrum such as S(E) ∝1
E , the most accurate way is to define a tabulated source
with two points and the IN_LOG_LOG interpolation.
Example (source in 1.
E between 10−5 and 10 MeV):
ENERGETIC_DISTRIBUTION
SPECTRUM
INTERPOLATED
2 1
IN_LOG_LOG 1
1.E-5 1.E5
10.

### 0.1 12.4.8 ANALYTICAL DISTRIBUTION

The distribution is expressed by an algebraic formula identical to that used for geometrical distribution.
Expression of the formulas and domains involves the use of the variable E.
The operators used in the formula expression are (LOG is the natural logarithm):
+ , - , *, /, SH, CH, SIN, COS, EXP, LOG, SQRT, ().
The relationships accepted in domain definitions are: < and >.
Note: If an expression begins with a −sign, a 0 must be placed before it: EXP(0-X), for exp(−x) for instance.
ENERGETIC_DISTRIBUTION
SPECTRUM
ANALYTICAL
FUNCTION = ...;
DOMAIN = ...;

<!-- page 167 -->
WARNING ! If the user wants to use a spectrum such as S(E) ∝1
E , with a domain going over several orders
of magnitude, the sampling of the analytical dirtibution is not accurate to do this. In this case, it is advised to
use a tabulated source with the IN_LOG_LOG interpolation as specified in the example above.
Example (source in exp(−E) between 1 and 2 MeV):
ENERGETIC_DISTRIBUTION
ANALYTICAL
FUNCTION= EXP(0-E);
DOMAIN=1<E<2;

### 12.4.9 FISSION SPECTRUM FROM THE EVALUATION

The distribution is the fission spectrum read in the evaluation for a given nuclide at 300 K and a given incident
energy. If the energy is not directly tabulated in the evaluation an interpolation is made according to the
interpolation scheme also given in the evaluation.
This option is available only when the fission spectrum is given as a tabulated law or a Maxwell law distribution
in the evaluation ("LF1" and "LF7" laws of the "file 5" in the ENDF/B format). Otherwise a message
error is produced by the code.
The syntax is as follows:
ENERGETIC_DISTRIBUTION
SPECTRUM
FISSION_FROM_EVALUATION isotope
*
THERMAL
*
FAST
*
ENERGY E0
where:
• isotope is one of the nuclide names given in the dictionary file (see chapter 3)
• THERMAL is equivalent to ENERGY 2.5E-6
• FAST is equivalent to ENERGY 2.
• E0 is an energy chosen by the user in MeV. It is not an energy bound of the spectrum, but an incident
energy for fission, as tabulated in the evaluation.

## 12.5 TIME DISTRIBUTION

Time distribution can be expressed in five different ways (Dirac, uniform, Gauss, tabulated, or analytical).
Warning: particle sources extending into negative times are allowed, but it is the user’s responsibility to lower
the value of the initial simulation time correspondingly (see keyword TIME_INF in Chapter 22). TRIPOLI-4

<!-- page 168 -->
cannot automatically detect the problem and will silently kill any particle that undergoes a collision below
the initial time.

### 12.5.1 DIRAC

This corresponds to a source at a given time input as a real number. The time distribution is a Dirac S(t) =
δ(t −t0), and the Dirac value is 1 when t = t0.
The syntax is as follows:
TIME_DISTRIBUTION
DIRAC t0
Important example:
In the case of a problem that is not time dependent, the following is selected:
TIME_DISTRIBUTION DIRAC 0

### 12.5.2 UNIFORM DISTRIBUTION

This corresponds to uniform time distribution between two values specified by the user. The syntax is as
follows:
TIME_DISTRIBUTION
UNIFORM
tin f tsup
The time distribution is S(t) = U(tsup,tinf ), such that S(t) = 1 if the time is within the bounds, and S(t) = 0
otherwise. The intensity, therefore, is equal to tsup −tin f .

### 12.5.3 GAUSS DISTRIBUTION

This corresponds to a Gauss time distribution centred around time tmean with a standard deviation σ. The time
distribution is
S(t) =
1
√
2πσe−(t−tmean)2
2σ2
=
1
√πae−(t−tmean)2
a2
The quantities tmean and a are specified by the user using the following syntax:
TIME_DISTRIBUTION
GAUSS
a tmean

<!-- page 169 -->
### 12.5.4 TABULATED DISTRIBUTION

This corresponds to a distribution whose values are given at a certain number of points and interpolated
between them. The syntax used to define this type of distribution is similar to that of a response function
expressed in the form of data (Section 13.4), or energy or angular tabulated distributions (with the times
being given in increasing order).
TIME_DISTRIBUTION
INTERPOLATED
nb(points) nb(inter)
<MODE_INTERPOLATION(1)>
num[limsup(1)]
...
<MODE_INTERPOLATION(nbinter)>
num[limsup(nbinter)]
t0 value0
...
tnb(points)−1 valuenb(points)−1
• <MODE_INTERPOLATION>
belongs
to
list
{IN_NO_INTERPOLATION,
IN_LIN_LIN,
IN_LIN_LOG,
IN_LOG_LIN, IN_LOG_LOG};
• nb(points) is the number of points, and nb(inter) the number of different interpolation ranges;
• Mode <MODE_INTERPOLATION(1)> applies from t0 to
tnum[limsup(1)];
• Mode <MODE_INTERPOLATION(j)> applies from tnum[limsup(j−1)] to
tnum[limsup(j)] where num[limsup(i)] is an integer, the index to the point in the list of given pairs (Caution:
the numbering begins at 0).
• The value of the last couple (tnb(points)−1, valuenb(points)−1) is untapped when <MODE_INTERPOLATION>
is IN_NO_INTERPOLATION.

### 12.5.5 ANALYTICAL DISTRIBUTION

The distribution is expressed by an algebraic formula of the same type as that used for geometrical distribution
. Expression of formulas and domains involves the use of variable T.
The operators in the expression of the formula are (LOG is the natural logarithm):
+ , - , *, /, SH, CH, SIN, COS, EXP, LOG, SQRT, ().
Relationships accepted in domain definitions are: < and >.
Note: If an expression begins with a −sign, a 0 must be placed before it: EXP(0-X), for exp(−x) for instance.

<!-- page 170 -->
TIME_DISTRIBUTION
ANALYTICAL
FUNCTION = ...;
DOMAIN = ...;
Example (source in exp(−t), t from 0 to 30 seconds)
TIME_DISTRIBUTION
ANALYTICAL
FUNCTION= EXP(0-T);
DOMAIN=0<T<30;

## 12.6 SOURCES TAKEN FROM SOURCE FILES

### 12.6.1 VOLUME PARTICLE SOURCES

Volume particle sources can be dumped using the STORE_*_IN_FILE directives in the simulation block (see
section 22.20).
Each file corresponds to events (sources, collisions, leaks) throughout the simulation for a given list of
batches. We can store the source events from a first calculation and restart them in a second calculation.
The command used in the second calculation is as follows:
SOURCES_LIST
1
SOURCE
NEUTRON
USE_FILE
*
ASCII
*
BINARY
firstrun.t4.sources LIST n i0 ... in−1
END_SOURCE
END_SOURCES_LIST
where n is the number of batches stored in the first run, i0 ...
in−1 are the batch numbers and
firstrun.t4.sources is the prefix of the source event files.
The user must maintain the statistical normalization of the batches. If the first run used n particles per batch,
and p restart files are loaded, the second run must use n.p particles per batch (cf. keyword SIZE in the
SIMULATION block, see chapter 22).

<!-- page 171 -->
This allows, for example, preparing several storage files at the end of a first simulation of several batches
apart (to reduce correlations) on a single processor and then resuming with a second calculation in parallel
with a roughly converged source of larger batches. This minimizes the computational effort for the source
convergence in criticality and maximizes performance of the parallelism of the second run.

### 12.6.2 SURFACE PARTICLE SOURCES

#### 12.6.2.1 Syntax

This type of source is used to perform simulations on “ local ” geometries after the characteristics of the
particles have been stored in source files during a simulation on the “ global ” geometry (using the STORAGE
command, or else the SCORE command with the STORAGE option). By re-using the source files during a local
simulation, the source particles are directly injected using the batch by batch source. This may follow the
order in which the batches were stored or else a random sampling of batches. This “zooming ” approach
is used in certain situations in order to obtain statistics where the global simulation alone does not yield
satisfactory results. It also decreases calculation time when performing a parametric study concerning the
geometry of the local simulation. Two figures illustrating this approach are presented at the end of this
section.
The syntax used in defining a surface source taken from a source file is as follows:
SOURCES_LIST
1
SOURCE
INTENSITY 1
<PARTICLE>
SOURCE_STORAGE LIST nb(fichiers)
file-name(1)
...
file-name(n)
<MODE>
TIME_DISTRIBUTION
Description of time distribution
END_SOURCE
END_SOURCES_LIST
• a single source must be defined: nb(sources) equals 1
• the norm for sources given after the keyword INTENSITY is 1 (the correct value for this variable is
actually read directly from the header of the source files)
• <PARTICLE> may be NEUTRON, PHOTON, or ALL_PARTICLE (the last option must be used if the data dump
was created with these particles: neutrons and photons stored in the same source file)

<!-- page 172 -->
• the file names file-name(i) are the complete names (including the suffixes when several files have been
created due to exceeding the size limit for the source files). There must not be more than 256 files.
• restart
in
parallel
mode
should
invoke
a
filename
with
the
following
syntax
source_filename.%SIMRANK%th_task_<istock>_.stock .
See section 12.6.2.3 for more details
.
• <MODE> equals:
– ORDERED n_discard, if the source of each batch is to be constituted following the order in which the
batches were stored.
The integer n_discard is the number of batches to be skipped at the beginning of the first file. This
number must be greater than or equal to 1 (the first batch read will, therefore, be the n_discard + 1
th. This first batch read may be empty or factitious). If biasing was used in the storage phase, it is
recommended that n_discard be set greater than or equal to 2.
– REPLICATE n, if each source particle is to be split in n particles with a statistical weight divided by
n. In this case the batches are read sequentially and in order (as in the ORDERED option). This option
will increase the simulation time but allows to have a better precision in the whole phase space,
especially when only few particles have been stored.
– RANDOM, if the batches are to be chosen at random. Warning: Extra care must be taken in this mode
as the sources may be sampled multiple times leading to an underestimated standard deviation. The
user is advised not to use this mode or to check he will not ask for more batches than available in
the source file.
• the syntax used in defining the time distribution is the same as for other types of sources.
Notes:
• In order for the source particles coming from the source files to be created strictly inside the geometry,
these particles are “pushed” forward by the code by a quantity εgeo.
• In order not to count particles twice, the surface where the stored particles are re-introduced should have
a leakage boundary condition. This is the default boundary condition in TRIPOLI-4® for surfaces at the
boundary of the geometry, but it is also possible to use a leakage boundary condition on a surface inside
the geometry (see chapter 9);
• In the SIMULATION command, the simulation mode must be set to SHIELDING (default simulation
mode in TRIPOLI-4®);

<!-- page 173 -->
#### 12.6.2.2 Zooming approach principle

Volume 2
Volume 1
Volume 2
             Leakage
             condition
Storage
surface
"Global" simulation
"Local" simulation

#### 12.6.2.3 Parallel mode

The parallel version of this feature will restart each stored file on each processor as if the calculation was
not interrupted. That means that the sources produced on the simulator i in the first pass will be used on the
simulator i in the second pass.
In this case, the number of processors in the second pass should be less or equal than the number of processors
in the first pass.
In previous versions, the user may be tempted to use all the sources produced in the first pass to restart a second
pass (with the RANDOM option or not). It is considered potentially harmful as it can introduce correlations
between the samples leading to underestimated variances.
In parallel, the syntax is almost identical except the source filename should be specified with the following
syntax source_filename.%SIMRANK%th_task_<istock>_.stock. The special token %SIMRANK% in the
filename will be replaced with the index of the task.

<!-- page 174 -->
## 12.7 COMPLETE SOURCE EXAMPLES

### 12.7.1 ISOTROPIC POINT SOURCE WITH NO TIME DEPENDENCE

A one particle per second source is required. A temporal Dirac is chosen. The source is, therefore, normalized
to one particle (the integral of the Dirac is 1). It is placed at the origin of the reference frame.

#### 12.7.1.1 Line spectrum

A source whose relative strength is known is given at 3 energies: a relative strength of 1 at 2 MeV, a relative
strength of 3 at 4 MeV, and a relative strength of 2 at 6 MeV. The spectrum is then the sum of three Diracs,
and the source has to be divided into three contributions.
Intensity
of the
source
Energy
4 MeV
2 MeV
6 MeV
The total source is written as follows (the first source has a normalisation of 1, the second a normalisation of
3 and the third a normalisation of 2)
SOURCES_LIST
3
SOURCE INTENSITY 1 NEUTRON
POINT 0 0 0
ANGULAR_DISTRIBUTION ISOTROPIC
ENERGETIC_DISTRIBUTION
SPECTRUM MONOKINETIC 2
TIME_DISTRIBUTION DIRAC 0.
END_SOURCES
SOURCE INTENSITY 3 NEUTRON
POINT 0 0 0
ANGULAR_DISTRIBUTION ISOTROPIC
ENERGETIC_DISTRIBUTION
SPECTRUM MONOKINETIC 4
TIME_DISTRIBUTION DIRAC 0.
END_SOURCES
SOURCE INTENSITY 2 NEUTRON

<!-- page 175 -->
POINT 0 0 0
ANGULAR_DISTRIBUTION ISOTROPIC
ENERGETIC_DISTRIBUTION
SPECTRUM MONOKINETIC 6
TIME_DISTRIBUTION DIRAC 0.
END_SOURCES
END_SOURCES_LIST
A more concise formulation of this is obtained using a line spectrum.
SOURCES_LIST
1
SOURCE INTENSITY 1 NEUTRON
POINT 0 0 0
ANGULAR_DISTRIBUTION ISOTROPIC
ENERGETIC_DISTRIBUTION
SPECTRUM RAY_SPECTRUM 3
2 1
4 3
6 2
TIME_DISTRIBUTION DIRAC 0.
END_SOURCES
END_SOURCES_LIST

<!-- page 176 -->
#### 12.7.1.2 Interpolated spectrum

If the user wishes to interpolate the spectrum between these points linearly, a single INTERPOLATED source is
selected. There are three interpolation points and a single interpolation type (linear-linear), which ends at the
last energy (the last energy bound is number 2 because the numbering starts at 0).
Intensity
of the
source
Energy
2 MeV
4 MeV
6 MeV
SOURCES_LIST
1
SOURCE INTENSITY 1 NEUTRON
POINT 0 0 0
ANGULAR_DISTRIBUTION ISOTROPIC
ENERGETIC_DISTRIBUTION
SPECTRUM INTERPOLATED 3 1
IN_LIN_LIN 2
2 1
4 3
6 2
TIME_DISTRIBUTION DIRAC 0.
END_SOURCES
END_SOURCES_LIST

### 12.7.2 DISTRIBUTED ISOTROPIC SOURCE WITHOUT TIME DEPENDENCE

Suppose we wish to simulate a one-dimensional cylindrical case (for instance, a comparison using a SN code),
in which the source is “linear”, i.e., contained within a cylinder with a small radius. TRIPOLI-4® requires a
three-dimensional geometry. For simplicity, an isotropic mono-kinetic source can be considered. To ensure
that the domain is not larger than the emission volume, it is best to consider the case where it is the domain
that sets the bounds for the source and that allows for the geometry definition. In any case, the domain must
not be substantially larger than the volume. The implicit convention in the example is that volume 1 contains
the domain, and the z-axis geometry is bounded by −10 < z < 10.

<!-- page 177 -->
Example: Radius of cylinder 1: 0.05 cm and the following definition:
SOURCES_LIST
1
SOURCE INTENSITY 1 NEUTRON
FACTORIZED
FRAME CYLINDER
0 0 0
1.
0.
0.
0.
0.
1.
VOLUME 1 1
GEOMETRIC_DISTRIBUTION
ANALYTICAL
FUNCTION = 1.;
DOMAIN = 0.< R < 0.05, 0 < RTHETA < 6.2832,-10.< Z < 10 ;
ANGULAR_DISTRIBUTION ISOTROPIC
ENERGETIC_DISTRIBUTION
SPECTRUM MONOKINETIC 1
TIME_DISTRIBUTION
DIRAC 0.
END_SOURCES
END_SOURCES_LIST
But certainly not radius of cylinder 1: 0.05 cm and the following defintion
SOURCES_LIST
1
SOURCE INTENSITY 1 NEUTRON
FACTORIZED
FRAME CYLINDER
0 0 0
1.
0.
0.
0.
0.
1.
VOLUME 1 1
GEOMETRIC_DISTRIBUTION
ANALYTICAL
FUNCTION = 1.;
DOMAIN = 0.< R < 5, 0 < RTHETA < 6.2832,-10.< Z < 10 ;
ANGULAR_DISTRIBUTION
ISOTROPIC
ENERGETIC_DISTRIBUTION
SPECTRUM MONOKINETIC 1
TIME_DISTRIBUTION
DIRAC 0.

<!-- page 178 -->
END_SOURCES
END_SOURCES_LIST
For the calculation of the source normalization, points are quasi-randomly sampled throughout the definition
domain. But only the points belonging to the intersection of the domain and volume 1 will be used. If this
intersection is too small, the number of points retained will be small, and the volume calculation (and hence
the source normalization) may be inaccurate.

<!-- page 179 -->
Defining the sources for the criticality calculation example of chapter 5
SOURCES_LIST
2
SOURCE NEUTRON
POINT -15.1 0.
199.57
ANGULAR_DISTRIBUTION
ISOTROPIC
ENERGETIC_DISTRIBUTION
SPECTRUM WATT_SPECTRUM
TIME_DISTRIBUTION
DIRAC 0.
END_SOURCES
SOURCE NEUTRON
FACTORIZED
FRAME CYLINDER
15.1 0.
185.3
1.
0.
0.
0.
0.
1.
VOLUME 1 8
GEOMETRIC_DISTRIBUTION
ANALYTICAL
FUNCTION = 1.;
DOMAIN = 0.
< R < 14.55, 0 < RTHETA < 6.2832, 0.
< Z < 28.54;
ANGULAR_DISTRIBUTION
ISOTROPIC
ENERGETIC_DISTRIBUTION
SPECTRUM WATT_SPECTRUM
TIME_DISTRIBUTION
DIRAC 0.
END_SOURCES
END_SOURCES_LIST

<!-- page 180 -->
## 12.8 EXTERNAL SOURCES

### 12.8.1 DESCRIPTION

The feature external source allows the user to supply any source using a source function written in C or
Fortran language and dynamically linked to TRIPOLI-4® at the beginning of the run. The user can define
a source as complex as desired, with energy-angle-position correlations (as in bremsstrahlung showers for
example). This feature is reserved to advanced Tripoli users as they have to provide their own sampling
algorithm.
The general syntax is as follows:
SOURCE
#
INTENSITY norm(source)
#
COEFF coeff(source)
<PARTICLE_TYPE>
EXTERNAL source.so
NO_GEOMSOURCE_WARNING
SOBOL_POINTS nb(points)
VOLUME nb(volumes)
volume(1) ...volume(n)
PARAM nb(params)
param(1) ...param(n)
END_SOURCE
where :
INTENSITY same meaning than previously (see section 12.1)
COEFF same meaning than previously (see section 12.1)
<PARTICLE_TYPE> can be NEUTRON, PHOTON, ELECTRON, POSITRON or ALL_PARTICLE
If it is ALL_PARTICLE, no rejection test on particle type is carried out
EXTERNAL source.so source.so is the name of the dynamic loading library containing the source function.
Its path must be included in $LD_LIBRARY_PATH environment variable.
NO_GEOMSOURCE_WARNING optional keyword, if present it disables low sampling efficiency test (by default
, the calculation is stopped if efficiency < 10%)
SOBOL_POINTS nb(points) optional, sets the number of sampling tests to nb(points), default=1000
VOLUME nb(volumes) volume(1) ...volume(n) optional, sets the volumes in which sources must be
sampled and calculates a sampling efficiency.

<!-- page 181 -->
If not present, all volumes are accepted.
PARAM nb(param) param(1) ...param(n)(n) List of numerical parameters transmitted to source function
( max = 10 ).
The function name must be necessary source and the call arguments have to be :
int *ipt
type of particle to create
•
1 = neutron
•
2 = photon
•
3 = electron
•
4 = positron
double *x
x position of the new particle created
double *y
y position of the new particle created
double *z
z position of the new particle created
double *u
direction cosine along x
double *v
direction cosine along y
double *w
direction cosine along z
double *e
particle energy
double *we
particle statistical weight
double *t
particle time
double *param
list of parameters from input TRIPOLI-4® file
double (*randtri)(void)
pointer to TRIPOLI-4®’s pseudo-random-number generator
By default, at each function call, the variables are initialized :
• ipt=1 (neutron)
• x=y=z=0.
• u, v, w isotropic
• e=14 MeV
• we=1.
• t=0.
Compilation options depend on the operating system, in some cases (eg AIX), it may be necessary to call
fortran functions via C function interfaces. During the TRIPOLI-4® source initialization phase, some verification
calculations are provided to the user (means, standard deviations, sampling efficiency). They are
performed on a sample of 1000 particles by default.

<!-- page 182 -->
### 12.8.2 EXAMPLE

This example defines a linear source from x=-10 cm to 0, in volumes 10 and 11 (possible rejection) of 1.33
MeV photons. The direction is inside a cone with an opening angle of ± 5 degrees along z. Source location
on x, particle type and energy are set from TRIPOLI-4® input data file.
For the sake of reproducibility, the pseudo-random numbers are drawn from TRIPOLI-4®’s generator.
Listings 12.1 and 12.2 show identical source functions written in C and Fortran.
The source definition in the input data file is as follows :
SOURCES_LIST
1
SOURCE ALL_PARTICLE
EXTERNAL source.so
VOLU 2 10 11 // source must be in volume 10 or 11 (or it will be resampled)
PARAM 4 -5.0 10.
2 1.33 // center, length, particle (2=photon), energy (MeV)
END_SOURCES
END_SOURCES_LIST
NOTES :
• The Fortran source subroutines used for MCNP are compatible with those of TRIPOLI-4® after updating
the call arguments and random number generator. It is not necessary to recompile the TRIPOLI-4® code.
• Be careful if point estimators (FLUX_PT) are used in the response list. The direct contribution from the
sources is assumed to be isotropic.
• When used in parallel calculation, if one considers that the sequence of random source sampling is of
importance on scores in relation to the transport part, it is recommended to use the TRIPOLI-4® randomnumber
generator passed as parameter randtri. Alternatively, the user has to manage the initialization
of source function random generator for each process.
// compilation on linux os via "gcc source.c -fPIC -shared -o source.so"
#include <stdlib.h>
#include <math.h>
void source(int *ipt ,double *x,double *y,double *z,double *u,double *v,double *w,
double *e,double *we,double *t,double *param , double (*randtri)(void)) {
double phi ,costheta ,sintheta ,cos5 ;
// by default x=0, y=0, z=0
*x= (param[0]-param [1]*0.5) + randtri()*param[1] ; // param[0]=center ,
param[1]= length
// (u,v,w) isotropic by default
cos5=cos (5./360.*6.283185);
phi=randtri ()*6.283185 ;

<!-- page 183 -->
costheta=randtri ()*(1.0 - cos5)
+ cos5 ;
sintheta=sqrt(1.0 - costheta*costheta);
*u=costheta;
*v=sintheta*sin(phi);
*w=sintheta*cos(phi);
// by default ipt=1 (neutron), e = 14 MeV , we = weight = 1, t = time = 0
*ipt=param[2]; // particle 1=neutron , 2=photon , 3=electron , 4=positron
*e=param[3];
// energy (MeV)
return ;
}
Listing 12.1: Example of C function source.
c compilation on linux os via "gfortran -fno -underscoring source.f -fPIC -shared -o source.so"
subroutine source(ipt ,x,y,z,u,v,w,e,we,t,param ,randtri)
double precision x,y,z,u,v,w,e,we,t,param ,randtri
double precision phi ,costheta ,sintheta ,cos5
dimension param(*)
c by default x=0, y=0, z=0
x= (param(1) - param (2)*0.5) + randtri()*param(2) ! param(1)=center ,
param(2)=length
c (u,v,w) isotropic by default
cos5 = cos(5./360.*6.283185)
phi=randtri ()*6.283185
costheta=randtri ()*(1.0 - cos5) + cos5
sintheta=sqrt(1.0 - costheta*costheta);
u=costheta
v=sintheta*sin(phi)
w=sintheta*cos(phi)
c by default ipt=1 (neutron), e = 14 MeV , we = weight = 1, t = time = 0
ipt=param(3)
! particle 1=neutron , 2=photon , 3=electron , 4=positron
e=param(4)
! energy (MeV)
end
Listing 12.2: Example of Fortran function source.

## 12.9 MULTI-PARTICLE SOURCES

Standard TRIPOLI-4 sources generate one particle per history. For the purpose of calculating average quantities
like fluxes or reaction rates, the correlations between source particles are immaterial; even if the Monte
Carlo simulation does not account for them, the calculated quantities are only sensitive to the singles distributions
(energy spectra, angular distributions, etc.). However, for the calculation of some observables,
correlations between source particles are crucial.
One example of such observables is given by the distribution of events with respect to the energy deposited
in a gamma spectrometer. For instance, consider the simultaneous emission of 1.17 and 1.33 MeV photons
arising from the decay of 60Co. If both photons are absorbed by the spectrometer, the detector will see the
sum of their energies. Clearly, a simulation where each photon energy appears independently of the other can

<!-- page 184 -->
SOURCES_LIST 2
NORM 1
SAME_HISTORY
SOURCE
PHOTON
POINT 0 0 0
ANGULAR_DISTRIBUTION ISOTROPIC
ENERGETIC_DISTRIBUTION SPECTRUM MONOKINETIC 1.17
TIME_DISTRIBUTION DIRAC 0.
END_SOURCE
SOURCE
PHOTON
POINT 0 0 0
ANGULAR_DISTRIBUTION ISOTROPIC
ENERGETIC_DISTRIBUTION SPECTRUM MONOKINETIC 1.33
TIME_DISTRIBUTION DIRAC 0.
END_SOURCE
END_SOURCES_LIST
Figure 12.7: Example of SOURCES_LIST block that generates uncorrelated photons from the decay of 60Co.
never reproduce the occurrence of the sum peak.
Multi-particle sources are a TRIPOLI-4® feature that make it possible to model correlated or uncorrelated
creation of multiple particles in the same history.

### 12.9.1 UNCORRELATED SOURCE PARTICLES

The simplest way to activate this feature is to use the SAME_HISTORY keyword in the SOURCES_LIST; this tells
TRIPOLI-4 to seed histories by sampling one particle from each defined source, instead of one particle from a
randomly-chosen source. When using SAME_HISTORY, all the sources in SOURCES_LIST must have the same
intensity.
An example SOURCES_LIST producing two uncorrelated 60Co gamma rays is shown in Figure 12.7.

### 12.9.2 CORRELATED SOURCE PARTICLES

More complex multi-particle sources (e.g. sources emitting correlated particles) can be introduced using
external sources (see Section 12.8 above) with the MULTIPLE keyword, like in Figure 12.8.
Here multi_ext.so is a shared library that must contain an external C++ source function (see Section 12.8)
with the following name and signature:

<!-- page 185 -->
SOURCES_LIST 2
SOURCE
PHOTON
EXTERNAL multi_ext.so
MULTIPLE
END_SOURCE
END_SOURCES_LIST
Figure 12.8: Example of SOURCES_LIST block that generates correlated source particles by calling an external source function.
extern "C"
void source_multiple(std::vector <int> &ipts ,
std::vector <double> &xs,
std::vector <double> &ys, std::vector <double> &zs,
std::vector <double> &us, std::vector <double> &vs,
std::vector <double> &ws, std::vector <double> &es,
std::vector <double> &wes , std::vector <double> &ts,
const double * const params , void (*randtri)(void));
The source_multiple function may take parameters through the params array, may call the randtri()
function to generate pseudo-random numbers and must fill the argument vectors ipts, xs, etc. with the characteristics
of the sampled particles. The meaning of the arguments are the same as in the case of traditional
single-particle external sources (function source, Section 12.8). Note that the source file for a multi-particle
external source cannot be written in C or Fortran.
An example of source file for a multi-particle external source is shown in Listing 12.3.

<!-- page 186 -->
// compilation on linux os via "g++ source_multiple.cc -fPIC -shared -o source.so"
#include <vector >
#include <cmath >
#include <iostream >
const double pi = 3.14159265359;
typedef double random_fct_type(void);
typedef void source_multiple_fct_type(std::vector <int> &,
std::vector <double> &,
std::vector <double> &, std::vector <double> &,
std::vector <double> &, std::vector <double> &,
std::vector <double> &, std::vector <double> &,
std::vector <double> &, std::vector <double> &,
const double * const, random_fct_type);
/* The angular distribution is taken to be
*
*
W(theta) = N ( 1 + a2 cos(theta)^2 + a4 cos(theta)^4 )
*
* with a2=9e-3 and a4=8e-3. The normalisation constant is
*
*
N = 8 / (8 + 4 a2 + 3 a4)
*
* and the maximum occurs at 0, pi:
*
*
W(0) = W(pi) = norm * ( 1 + a2 + a4 )
*
* Since the CDF cannot be analytically inverted , we sample the PDF by
* rejection.
*/
const double a2 = 9e-2;
const double a4 = 8e-2;
const double norm = 8. / (8. + 4.*a2 + 3.*a4);
double dist(const double cosx)
{
const double cosx2 = cosx*cosx;
const double cosx4 = cosx2*cosx2;
return norm * (1 + a2 * cosx2 + a4 * cosx4);
}
const double distmax = dist(1.);
template<typename T> struct Vec {
T x;
T y;
T z;
Vec(const T &ax, const T &ay, const T &az) : x(ax), y(ay), z(az) {}
T dot(const Vec <T> &other) const { return x*other.x + y*other.y + z*other.z; }
Vec <T> vector(const Vec <T> &other) const {
return Vec( y * other.z - z * other.y,
z * other.x - x * other.z,

<!-- page 187 -->
x * other.y - y * other.x );
}
Vec <T> operator*(const T &a) const { return Vec <T>(a*x, a*y, a*z); }
Vec <T> operator+(const Vec <T> &other) const { return Vec <T>(x+other.x, y+other.y, z+other.z); }
};
extern "C" {
void source_multiple(std::vector <int> &ipts ,
std::vector <double> &xs,
std::vector <double> &ys, std::vector <double> &zs,
std::vector <double> &us, std::vector <double> &vs,
std::vector <double> &ws, std::vector <double> &es,
std::vector <double> &wes , std::vector <double> &ts,
const double * const params , random_fct_type randtri);
}
void source_multiple(std::vector <int> &ipts ,
std::vector <double> &xs,
std::vector <double> &ys, std::vector <double> &zs,
std::vector <double> &us, std::vector <double> &vs,
std::vector <double> &ws, std::vector <double> &es,
std::vector <double> &wes , std::vector <double> &ts,
const double * const params , random_fct_type randtri) {
const double e1 = 1.17;
const double e2 = 1.33;
const double x = 0.;
const double y = 0.;
const double z = 0.;
const double costheta1 = std::min(std::max(2.* randtri()-1., -1.), 1.);
const double sintheta1 = std::sqrt((1. - costheta1 )*(1. + costheta1));
const double phi1 = 2. * pi * randtri();
const Vec <double> v1 =
Vec <double>(sintheta1 * std::cos(phi1),
sintheta1 * std::sin(phi1),
costheta1);
double costheta12 , xi;
do { // rejection loop
costheta12 = std::min(std::max(2.* randtri()-1., -1.), 1.);
xi = distmax * randtri();
} while(xi >= dist(costheta12));
const double sintheta12 = std::sqrt((1. - costheta12 )*(1. + costheta12));
const double phi12 = 2. * pi * randtri();
const Vec <double> v12 =
Vec <double>(sintheta12 * std::cos(phi12),
sintheta12 * std::sin(phi12),
costheta12);
Vec <double> v2(0., 0., 0.);
if(sintheta1 ==0.) { // degenerate case
v2 = v12;
} else {
Vec <double> k = Vec <double>(0., 0., 1./std::fabs(sintheta1)).vector(v1);

<!-- page 188 -->
// Rodrigues’ rotation formula
v2 = v12 * costheta1 + k.vector(v12) * sintheta1 + k * (k.dot(v12)*(1. - costheta1));
}
ipts.push_back (2); // photon
xs.push_back(x); ys.push_back(y); zs.push_back(z);
us.push_back(v1.x); vs.push_back(v1.y); ws.push_back(v1.z);
es.push_back(e1); wes.push_back (1.); ts.push_back (0.);
ipts.push_back (2); // photon
xs.push_back(x); ys.push_back(y); zs.push_back(z);
us.push_back(v2.x); vs.push_back(v2.y); ws.push_back(v2.z);
es.push_back(e2); wes.push_back (1.); ts.push_back (0.);
}
Listing 12.3: Example C++ source listing for a multi-particle external source. The source produces two correlated photons from the
decay of 60Co; the angle θ between the photon emission directions is assumed to follow the distribution W(θ) = N ·(1+a2 cos2 θ+
a4 cos4 θ), with N = 8/(8+4a2 +3a4) being a normalization constant.

## 12.10 SOURCES FOR ACTIVATION CALCULATIONS

In the second step of Rigorous Two-Step (R2S) activation calculations, a special activation source must be
defined. Please refer to Section 41.2.2 for further details.

## 12.11 GEANT4 PARTICLE SOURCES

The TRIPOLI-4/GEANT4 coupling makes it possible to directly use particle sources from a GEANT4 simulation
in TRIPOLI-4. For further details, please consult Section 42.5.

## 12.12 SPONTANEOUS FISSION SOURCES WITH THE FIFRELIN FISSION MODEL

A spontaneous fission source can be defined using fission event files produced by the FIFRELIN fission
model code (see also Section 22.1 for details on the coupling between TRIPOLI-4® and FIFRELIN codes by
external files). The syntax is as follows:

<!-- page 189 -->
SOURCE
ALL_PARTICLE SPONTANEOUS_FISSION FIFRELIN za
USE_FILE format n(files)
path_to_file_1
...
path_to_file_n
RADIUS R
HEIGHT h
TIME_INF Tin f
TIME_SUP Tsup
END_SOURCE
with the same conventions after FIFRELIN keyword as for induced fission (see Section 22.1). The keyword
ALL_PARTICLE has to be used for the particle type, so as to sample fission neutrons and photons. The emission
point coordinates are sampled in the sphere of radius R and center x = 0, y = 0, z = h. Emission times are
between Tin f and Tsup.
