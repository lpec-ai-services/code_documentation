# DEFINING SCORES
<!-- source PDF pages 215-235 -->

<!-- page 215 -->
Chapter 15
DEFINING SCORES
Scores are defined between the keywords SCORE and END_SCORE. The syntax is as follows:
SCORE
nb(scores)
Descriptions of scores
END_SCORE

## 15.1 NOTES REGARDING SCORE DEFINITIONS

A score is defined using:
• the type of response function to be calculated, designated by an integer corresponding to the order of
appearance of the response in the RESPONSES command or by its name if it was given in the RESPONSES
command;
• an energy grid, designated by its name in the GRID_LIST command;
• an optional angle grid designated by its name in the GRID_LIST command;
• an optional time grid (only used in kinetic calculations) also designated by its name in the GRID_LIST
command;
• an estimator defined in the SCORE command.

## 15.2 STANDARD MONTE CARLO ESTIMATORS

### 15.2.1 VOLUME-BASED ESTIMATORS

For volume tallies, the following estimators are available:

<!-- page 216 -->
• the track length estimator TRACK
χ = ω·L
where:
– ω is the statistical weight of the particle;
– L is the length of the trajectory.
• the collision estimator COLL
χ =
ω
Σ(E)
where:
– ω is the weight of the particle;
– Σ(E) is the total cross-section of the composition.

### 15.2.2 SURFACE-BASED ESTIMATORS

The following estimator is available for a tally on a surface:
• the surface-based estimator SURF.
For a flux:
χ =
ω
∥Ω·n∥
For a current (outgoing current):
χ = ω
where:
• ω is the weight of the particle;
• Ωis the direction of the particle;
• n is the surface normal unit vector.

## 15.3 NEXT-EVENT ESTIMATORS

### 15.3.1 POINT-BASED ESTIMATORS

For tallying at a point (flux or reaction rate), the point-based estimator FLUX_PT is available with a point
definition.

### 15.3.2 SURFACE-BASED ESTIMATORS

For tallying at a surface (flux or reaction rate), the estimator FLUX_PT must be used with a target surface
definition.

<!-- page 217 -->
### 15.3.3 REMARKS

At the present time, the next-event estimators are only unbiased for vacuum boundary conditions. They can
be used with anisotropic sources.
Next-event estimators are performing a full virtual transport from each collision to one of the scoring points.
If the number of collision is important (as in some neutron calculations), it can be very time consuming.

## 15.4 VARIANCE EVALUATION

For each score, a mean value is estimated from the simulation. A standard deviation of this mean is also
given to estimate the fluctuations of the score. Since version 12, the Welford algorithm is used in place of the
standard algorithm (see [46, 101]) to evaluate the variance (and then the standard deviation).

## 15.5 GEOMETRICAL ELEMENTS

Such elements can be volumes (volume-based estimators), surfaces (surface-based estimators), points (pointbased
estimators) or a regular spatial mesh tally.
• A volume is designated by its definition number.
• A surface is designated by the interface between two volumes. An escape surface is designated by a
volume number and virtual number -1. In the case of a target surface with a next-event estimator, a
special syntax will be given below.
• A point is designated by its coordinates (X,Y,Z).
• A spatial mesh independent of the geometry is defined with a syntax detailed below.
Important:
• a surface cannot be defined by a virtual volume (the result would be a zero score; the test is made on
the basis of the particle belonging to a volume and a particle cannot belong to a virtual volume);
• for the CURRENT option, it is an exiting current from the first volume given towards the second
volume that is calculated. It is not a net value, and only the particles leaving the first volume and
entering the second are counted.
• for the FLUX with a surface estimator, see remarks on the associated geometrical element types in subsection
15.7.

## 15.6 FILTERING

It is possible to tally only the results for particles that have passed through certain volumes (conditional
tallying or filtering). In this case, it is necessary to use the FILTER option.
Note: This option is incompatible with the collision band command.

<!-- page 218 -->
## 15.7 DEFINING THE SCORE

A score is defined using the following syntax:
NAME <score_name>
∗1
num(response)
∗1
<response_name>
<ESTIMATOR_NAME>
FILTER VOLU
LIST nb(volu)
vol(1)...vol(n)
FILTER_BY_COMPOSITION nb(compo) compo(1) ...compo(nb)
TIME GRID name(time grid)
#
ANGULAR GRID name(µ angle grid)
#
2D_ANGULAR GRID name(µ angle grid) name(φ angle grid)
∗2
GRID name(energy grid)
∗2
WHOLE_GRID name(grid encompassing 0)
∗2
2D_GRID min1 max1 min2 max2
<RESULTS>
STORAGE
filename
LIMIT_SIZE nb_Mo
GAUSSIAN_BROADENING a b c
<GEOMETRICAL_ELEMENT_TYPE>
STORE_IN_FILE
<LIST_OR_SUM> nb(elements)
element(1)
...
element(n)
where:
1. The score name is optional. In the case of a neutronic-shielding coupling calculation (see also chapter
22), this data must be given in order to determinate in which simulation mode this score is to be
performed.
2. The associated response is given either:
(a) by num(response), the response number given in the RESPONSES command: the first response
defined is number 1, the second number 2, etc.
Important: Number n is not specifically indicated in the command; adding a response can offset the
numbering.
(b) by the name of the response given in the RESPONSES directive (by NAME)
3. < ESTIMATOR_NAME > is one of the following keywords:

<!-- page 219 -->
• TRACK for a track length estimator
• COLL for a collision estimator
• SURF for a surface estimator
• FLUX_PT <score_choice> for a point estimator
<score_choice> is an optional parameter which specifies the scored data. It can be :
– COLLIDED all contributions to flux point have at least one collision.
– UNCOLLIDED all contributions to flux point come directly from source without collision.
– TOTAL all contributions are take into account, this is the default.
• MACROSCOPIC_REACTION_RATE for macroscopic reaction rates. This mode of estimation is necessary
for scores associated with MACROSCOPIC_REACTION_RATE response.
• LOCAL_ENERGY_DEPOSITION for energy deposition. This mode of estimation is necessary for scores
associated with DEPOSITED_ENERGY response.
• KINEMATIC_LIMITS for kinematic limits. This mode of estimation is necessary for scores associated
with KINEMATIC_LIMITS response.
• DPA for calculation of Displacements Per Atom (DPA). This mode of estimation is necessary for
the scores associated with DPA response.
• PRODUCTION for production of particles.
This mode is necessary for scores associated with
PRODUCTION response functions (PHOTON_REPARTITION and ELECTRON_REPARTITION keywords
from versions earlier than 7 are still allowed with the same keyword in response command block,
and are actually particular cases for the calculation of a photon source or an electron source, see
chapter 13).
• GAS_PRODUCTION for calculation of gas production. This mode of estimation is necessary for the
scores associated with GAS_PRODUCTION response.
• FISSION_SPECTRUM for calculation of fission spectra. This mode of estimation is necessary for the
scores associated with FISSION_SPECTRUM response.
• DEPOSITED_SPECTRUM for detector response calculation.
This estimation mode is necessary

for
scores
associated
with
the
DEPOSITED_SPECTRUM_WEIGHTED_ENERGY
or
the
DEPOSITED_SPECTRUM response functions.
• FIXED_SOURCE_EMISSION for fixed source emission calculations. This mode of estimation is necessary
for scores associated with FIXED_SOURCE_EMISSION response. Note that this score does not
need any geometrical element definition since it applies to the whole source. The request of this
type of score ends up then with a grid name.
• DEPOSITED_CHARGE for the calculation of the charge-deposition response. This estimation mode is
necessary for scores associated with the DEPOSITED_CHARGE response function.
• NU_FISSION for the calculation of a histogram of number of fission neutrons per fission. This mode
of estimation is necessary for the scores associated with the NU_FISSION response. In addition,
the WHOLE_GRID keyword must be used instead of the standard GRID energy-grid keyword, so as to
encompass the 0 value.

<!-- page 220 -->
• FISSION_N_SUM_SPECTRUM for the calculation of the sum of fission neutron energies per fission.
This mode of estimation is necessary for the scores associated with the FISSION_N_SUM_SPECTRUM
response. In addition, the WHOLE_GRID keyword must be used instead of the standard GRID energygrid
keyword, so as to encompass the 0 value.
• FISSION_ZA_DISTRIBUTION for the calculation of the (Z,A) distribution of the fission products
(after emission of prompt neutrons). This mode of estimation is necessary for the scores associated
with the FISSION_ZA_DISTRIBUTION response. In addition, the 2D_GRID keyword must be used
for the definition of the (Z,A) 2D mesh with a cell size of 1 in Z and A, and with Zmin, Zmax, Amin
and Amax bounds respectively defined with min1 max1 min2 max2 values. The end of the syntax is
the standard one with volumes as geometrical elements (followed by <LIST_OR_SUM>).
4. name(time grid) (or name(µ angle grid) or name(φ angle grid)) is the name of a time (or angle
) grid given in GRID_LIST. The distinction between energy and time (or angle) grids is made using
the keyword TIME (or ANGULAR or 2D_ANGULAR), preceding GRID. Note: The time (or angle) grid specification
is optional.
Important:
• ANGULAR refers to µ angle, where µ is defined with repect to the normal to the surface used with the
surface-based estimator SURF.
• 2D_ANGULAR refers to both : µ and φ, defined in the global frame of the geometry.
• The name of the φ grid (e.g. : DEC_PHI_ANGLE) must then contain the string “PHI".
5. name(energy grid) is the name of an energy grid given in GRID_LIST.
6. name(grid encompassing 0) is the name of a grid, given in GRID_LIST, replacing the energy
grid and encompassing the zero value.
For example it can be used for a NU_FISSION or a
FISSION_N_SUM_SPECTRUM response.
7. <RESULTS> is an optional keyword which can be BOOTSTRAP for confidence interval calculations or
COMPLETE for complete storage of the results, or VOV for "on the fly" information on variance jumps. By
default, the results stored are average values. The utilisation of BOOTSTRAP or COMPLETE options can
take a lot of memory. Indeed, a floating point variable is allocated for each batch, each score and each
energy group. These options may cause problems in parallel mode.
8. <FILTER> is an optional keyword indicating that a conditional tally is required. It can be one of the
following keywords:
• FILTER_OR: the particle must have previously passed through one of the specified volume list;
• FILTER_AND: the particle must have previously passed through every volumes of the specified volume
list;
• FILTER_SEQ: the last volumes through which the particle has passed must be equal to the specified
list in the specified order;
• FILTER_TARGET: the direction of the particle must have crossed one of the specified volume list.

<!-- page 221 -->
If the FLUX_PT estimator has been chosen, only FILTER_OR or FILTER_TARGET are available.
9. FILTER_BY_COMPOSITION is an optional keyword to be used with extended mesh geometrical elements.
It allows to filter scoring events by the belonging to a list of compositions. All events occurring in a
composition cited in this list will be used for scoring in the extended mesh.
10. STORAGE is an optional keyword only available with the FLUX_PT estimator and the TARGET_SURF geometrical
element type (see below). Characteristics of the particles reaching the surface defined by
TARGET_SURF are then stored. Similarly to the STORAGE command (see chapter 27), the user must provide
a file name which will be suffixed by "_<i>_fxpt_target_stock". The variable i is initialized
to 1 and incremented each time the limit size nb_Mo (in Mega bytes) is reached. (The storage is then
going on in a new file.)
11. GAUSSIAN_BROADENING is an optional keyword to be used together with DEPOSITED_SPECTRUM scores.
It allows for Gaussian Energy Broadening (GEB), so as to approximate the behaviour of real-life radiation
detectors. Indeed, the energy peaks in a physical radiation detector suffer a broadening effect which can
be reproduced through Gaussian sampling.
Whenever a contribution of energy E is to be deposited in the spectrum, it is replaced by an energy E∗
sampled from the Gaussian of mean E:
f(E∗|E,σ) =
1
σ
√
2πe−(E∗−E)2
2σ2
where the standard deviation σ of the Gaussian is:
σ = FWHM
2
√
2ln2
The FWHM (Full Width at Half Maximum) is used to describe the physical detector behaviour. It is
computed using three parameters a, b and c provided by the user, according to:
FWHM = a+b
p
E +cE2
12. <GEOMETRICAL_ELEMENT_TYPE> is one of the following keywords:
• VOLUME or CELL, to be used with the track length estimator TRACK and the collision estimator COLL;
• FRONTIER or ORIENTED_FRONTIER, to be used with the SURF estimator.
When ORIENTED_FRONTIER is used together with FLUX, only the exiting flux from the first volume
towards the second volume is calculated;
When FRONTIER is used together with FLUX, a scalar flux is calculated as the sum of fluxes in both
directions of the frontier (provided that each requested frontier is not requested twice in a LIST,
in one direction and then the opposite: in this case the user is invited to use ORIENTED_FRONTIER
keyword instead);
• POINT or TARGET_SURF if FLUX_PT has been chosen: next-event estimator toward one or several
points or toward a single rectangular target surface;

<!-- page 222 -->
• EXTENDED_MESH for extended functionalities of scores on meshes. See section 15.8 for details.
• MESH if the user requests a COLL tally on a regular mesh (defined independently of the geometry).
This mesh of Nx ×Ny ×Nz cells of sizes dx, dy, dz must be defined as follows:
MESH ENTROPY MESH_INFO
Nx Ny Nz
dx dy dz
FRAME
Ox Oy Oz
where (Ox,Oy,Oz) is the center of the reference cell.
Important note: This option is unavailable for the current version. The user can use the extended
mesh feature instead. See section 15.8 for details on the extended mesh.
The following example defines a mesh of 20×20×1 cells each of sizes 10∗10∗300, the reference
cell being centered in (5,5,150):
1 COLL
GRID DEC_ABSORPTION
MESH
20 20 1
10 10 300
FRAME 5 5 150
(subsection 15.9.2). The MESH_INFO option gives additional information about the mesh’s specification
displaying the volume and centers of all cells.
13. STORE_IN_FILE: when the score is required on a list of volumes using VOLUME and LIST keywords,
the STORE_IN_FILE option stores the list of the requested volumes and associated results in a separate
ASCII file.
The following example requests a score in volumes 5 and 7:
VOLUME
STORE_IN_FILE
LIST 2 5 7
14. <LIST_OR_SUM> is either LIST or SUM. This keyword is omitted in the cases of the mesh tally and the
TARGET_SURF geometrical element type.
15. nb(elements) is the number of geometrical elements for which the results are requested. The result is
given for each element on the list when the LIST option is selected, but it is the sum of the scores for the
elements on the list when the SUM option is selected.
For choice VOLUME this number can be replaced by the keyword ALL. The results will then be given for
each volume of the geometry.

<!-- page 223 -->
The DEPOSITED_SPECTRUM and DEPOSITED_CHARGE scores can be used with LIST or SUM of
nb(elements) volumes.
16. element(1)...element(n) is a list of elements, with an element(i) consisting of:
• a) a volume number for choice VOLUME.
Examples:
2 TRACK
GRID GRID_ABSORPTION
VOLUME LIST 2 5 7
Response 2 is requested with estimator TRACK for the grid indicated in two volumes: in volume 5
and in volume 7.
2 TRACK
GRID GRID_ABSORPTION
VOLUME SUM 2 5 7
Here, the response is requested in volume 5+7 (consisting of two volumes).
2 TRACK
GRID GRID_ABSORPTION
VOLUME LIST ALL
Here, the response is requested in all the volumes.
• b) a volume number, the depth and the three cell indices for each lattice (from the coarsest to the
smallest) to the desired depth, for choice CELL. It is, therefore, possible to extract cells from cells
in the case of a lattice of lattices. It should be noted that in version 4.1, it was the lattice number
and not the depth that was requested. The presence of the additional keyword DEPTH ensures
compatibility with older data sets.
Examples:
2 COLL
GRID GRID_ABSORPTION
CELL LIST 2
5 50 1 2 3
4 40 5 2 3
Response 2 is requested, with the COLL estimator for the grid indicated in two cells: in volume 5
(lattice 50), for cell (1,2,3) and in volume 4 (lattice 40), cell (5,2,3).
2 COLL
GRID GRID_ABSORPTION
CELL SUM 2

<!-- page 224 -->
5 DEPTH 1 1 2 3
4 DEPTH 1 1 2 3
Here the response is requested in volume 5+4, only in cell (1,2,3).
2 COLL
GRID GRID_ABSORPTION
CELL LIST 1
5 DEPTH 2 1 2 3 1 1 1 Here the response is requested in volume 5, only in cell (1,1,1) of cell
(1,2,3) of the largest lattice.
Notes: the sum of the results can be made in a cell and in a volume. In this case, for a volume sum,
it is necessary to declare a depth of 0.
• c) two volume numbers, defining a surface, for the SURF option. It should be noted that the area
outside the geometry is numbered -1 (a surface bounding the geometry therefore has a surface
between a volume of a given number and -1).
It must be borne in mind that the number of
the volume is that of the volume to which the particle belongs, and not a construction volume.
Consequently, the volume cannot be a lattice. This excludes the possibility of surface-based flux
(or current) between a lattice and a volume.
Example:
1 SURF
GRID GRID_FLUX
FRONTIER LIST 4
1 2
3 4
5 6
7 8
Response number 1 is requested, with the SURF estimator for the grid indicated and for four surfaces:
the surface between volumes 1 and 2, the surface between 3 and 4, the surface between 5 and 6,
and the surface between 7 and 8. For calculation of flux or surface-based reaction rate (but not for
a current), it is necessary to be able to calculate the normal unit vector.
This is not currently possible in TRIPOLI-4® for a surface that results from the application of an
operator (UNION, INTE, etc.). It is nonetheless sufficient to calculate the normal vector for one of
the two volumes that define the surface.
Note: each element is defined by two volume numbers. For the case of escape, the number of the
volume and the number -1 are given. No verification is made and the surface that is defined may
not exist.
• d) the coordinates (X,Y,Z) of a point, for the FLUX_PT option. Warning: the position of this point is
surrounded by an exclusion sphere that should not cut separating surfaces of different compositions
volumes. By default, the radius of this exclusion sphere is set to 0.5 cm. The user can modify it

<!-- page 225 -->
when using the keyword EXCLUSION followed by the radius, to be placed before the coordinates of
the first point. In this case the choice of a suitable value is left to the user’s responsability.
Examples:
1 FLUX_PT
GRID GRID_FLUX
POINT LIST 1 0 0 0
Response 1 is requested, with estimator FLUX_PT for the grid indicated at the point: (0,0,0). The
radius of the exclusion sphere is 0.5 cm.
1 FLUX_PT
GRID GRID_FLUX
POINT LIST 1 EXCLUSION 0.2 0 0 0
In this case the radius of the exclusion sphere is 0.2 cm.
• e) data of the target surface with the FLUX_PT estimator and TARGET_SURF geometrical element.
The syntax is as follows:
TARGET_SURF
dimension_V dimension_W
POSITION Px Py Pz
ORIENTATION
Ux Uy Uz
Vx Vy Vz
Wx Wy Wz
where:
– dimension_V and dimension_W are the sizes or the rectangular surface;
– Px Py Pz are the coordinates of the center of the target surface;
– Ux Uy Uz , Vx Vy Vz , Wx Wy Wz are the coordinates of the orthogonal vectors. U must be
orthogonal to the target surface.

## 15.8 EXTENDED MESHES

This provides extended functionalities of scores on meshes.
Both TRACK and COLLISION estimators can be used, and available frames are CARTESIAN, CYLINDER and
SPHERE.

<!-- page 226 -->
The syntax is as follows :
EXTENDED_MESH
MESH_INFO
MERGE_ENERGIES
TRIANGLEZ
ENTROPY
NORMALIZE
STORE_IN_FILE
∗
WINDOW
Uniform window data
∗
WINDOW_VARIABLE
Nonuniform window data
FRAME
<FRAME_TYPE>
O’x O’y O’z
ix iy iz
(jx jy jz) if cartesian
kx ky kz
The MESH_INFO option gives additional information about the mesh’s specification displaying the volume and
centers of all cells.
The MERGE_ENERGIES option allows to store all the meshes for the different energy bins to be merged inside
one unique file. The number of bins and the energy limits of the bins will be found in the grid and positions
parameters of the .general header.
The TRIANGLEZ option allows the user to split each parallelepiped in two prisms in order to calculate scores
on hexagonal lattices. It will thus double the number of cells in the V direction. See figure 15.1 for numbering
convention. Note that this option cannot be used on a nonuniform window.
The NORMALIZE option divides each output by the volume of each individual cell.
The use of the optional keyword ENTROPY is detailled below (subsection 15.9.2).
The STORE_IN_FILE option stores the result in a separate ASCII file. This file may be used by the T4G tool
(see chapter 38). If MED keyword is specified after this option the result is stored in a separate MED format file
including mean values and sigma values. The three usual coordinate systems are available with this feature:
cartesian, cylindrical, and spherical.
As well as describing mesh for biasing, it can be useful to use uniform or nonuniform window depending on
the problem. The window is defined after the keyword WINDOW for a uniform window, or WINDOW_VARIABLE
for a nonuniform window.
The definition of a FRAME is explained in section 4.5.

<!-- page 227 -->
0,0,k
0,1,k
0,2,k
0,3,k
0,4,k
0,5,k
1,0,k
1,1,k
1,2,k
1,3,k
1,4,k
1,6,k
2,0,k
2,1,k
U
V
Figure 15.1: TRIANGLEZ numbering convention

### 15.8.1 UNIFORM WINDOW SYNTAX

The syntax for a window of Nu′ × Nv′ × Nw′ regular cells uses the same conventions as those used for the
keyword CHECK_GEOM (see section 7.13.2), except for the additional arguments indicating the number of cells
in each dimension:
WINDOW
Umin Vmin Wmin
Umax Vmax Wmax
Nu Nv Nw

### 15.8.2 NONUNIFORM WINDOW SYNTAX

The syntax for a variable window of Nu′ ×Nv′ ×Nw′ cells is:
WINDOW_VARIABLE
Nu Nv Nw
u0 N1 u1 N2 u2 ... Nn un
v0 M1 v1 M2 v2 ... Mm vm
w0 P1 w1 P2 w2 ... Pp wp
where :
• u0,...,un,v0,...,vm,w0,...,wp are given in the mesh frame

<!-- page 228 -->
• Ni is the number of regular cells between coordinates ui−1 and ui
• M j is the number of regular cells between coordinates vj−1 and vj
• Pk is the number of regular cells between coordinates wk−1 and wk
• moreover, these data must verify :
N1 +N2 +...+Nn = Nu
M1 +M2 +...+Mm = Nv
P1 +P2 +...+Pp = Nw

### 15.8.3 VARIANCE REDUCTION AND TRACK ESTIMATORS

Along with the TRACK estimator, the user wanting to use the standard variance reduction method of the code
(based on the Exponential Transform) must place the statement "MAX_SPLITTING_PARTICLE_NUMBER 1" in
the SIMULATION block (see Section 22.2). This option disables the quota sampling inside the simulation. The
most important tool for variance reduction (the Exponential Transform) is still in function when using this
option.

### 15.8.4 NOTE ON COLLISION ESTIMATOR

Using the COLLISION estimator with cells astride on compositions with both very low and high optical density
is statistically ill conditioned: it may yield false results without warning (that is, with an underestimated
standard deviation).
Other remarks:
• Umin can be non-zero in any frame. For example, in CYLINDER mode, it allows to have scores on
cylinders not including the origin.
• basis vectors need not to be orthogonal in the cartesian frame, thus enabling scores on one third of an
hexagonal domain. You can use three meshes to have scores on a full hexagonal domain (figure 15.2).
Using the TRIANGLEZ mode allows to get scores on all of the 6 triangles composing any hexagonal cell.
Some post-processing by the user is necessary to get the value of scores on each hexagonal cell.

### 15.8.5 NOTE ON MESH EDITION RESULTS

The simulation keywords MESH_EDITION and SUPPRESS_MESH_EDITION_TEXT can be used to reduce the size
of the results file when requesting results in meshes (see chapter 22).

<!-- page 229 -->
Figure 15.2: Hexagonal domain decomposition

<!-- page 230 -->
## 15.9 EXAMPLES OF SCORE REQUESTS

### 15.9.1 EXAMPLE ON A SIMPLE GEOMETRY

In the case of a geometry consisting of a box with 10 cm sides along x and 20 cm sides along y and z, centered
at the origin:
GEOMETRY
TITLE test
TYPE 1 BOX 10 20 20
VOLU 1 COMBI 1 0 0 0 ENDV
ENDGEOM
Assuming that it is empty:
COMPOSITION 1
POINT_WISE 300 VIDE 1
H1 1.E-20
END_COMPOSITION
GEOMCOMP
VIDE 1 1
END_GEOMCOMP
For a mono-kinetic source to 1 MeV centered on the origin (5 cm from the sides along x) and normalized to
three particles, the particles being directed with an angle of 45 degrees with respect to the normal of one side:
SOURCES_LIST 1
NORM 3
SOURCE
NEUTRON POINT 0 0 0
ANGULAR_DISTRIBUTION MONO_DIR 1 0 1
ENERGETIC_DISTRIBUTION
SPECTRUM MONOKINETIC 1
TIME_DISTRIBUTION DIRAC 0
END_SOURCES
END_SOURCES_LIST
To simulate 50 batches of 100 particles each (see the command syntax, below in the manual, monitoring is
disabled (it is pointless because no variance reduction technique is used), in order not to have 500 particles in
the first batch):
SIMULATION
BATCH 50
SIZE 100

<!-- page 231 -->
x
z
O (source)
10 cm
20 cm
Figure 15.3: Example for score requests
PARTICLE 1 NEUTRON
MONITORING 0
END_SIMULATION
All the particles will therefore travel 5×
√
2 ≃7.071 cm in the box (volume 1) then escape without collision
out of the geometry (volume number -1 by definition) through the surface (defined as the boundary between
volumes 1 and -1), from 1 to -1.
Each source particle has an initial weight of 1. As they all escape without a change in their weight (no
fractioning or roulette), the average weight of escape is 100 per batch.
For a one-group grid covering the domain (with a simulation default of 20 to 10−11 MeV):
GRID_LIST
1
GRID_INTEGRAL
2
20.
1.E-11
END_GRID_LIST
We seek the flux and a virtual microscopic reaction (fission) rate for uranium-235 (at 300 K):
RESPONSES
4
FLUX NEUTRON
CURRENT NEUTRON
REACTION NEUTRON

<!-- page 232 -->
NUCLEUS U235 FICTIVE 300 INTERACTION 1 33
DOSE_H*(10) NEUTRON
END_RESPONSES
Let us request the volume-based flux (response number 1) using the volume-based track length and collision
estimators in volume 1 and by the surface-based estimator between 1 and -1. Let us also request the current
(response number 2) between 1 and -1. (Note that the code forbids requesting a current from -1 to 1,
corresponding to an inward current.)
Finally, we request the reaction rate (response number 3) in volume 1 by collision and track length volumebased
estimators:
SCORE
7
1 TRACK GRID GRID_INTEGRAL
VOLUME LIST 1 1
1 COLL GRID GRID_INTEGRAL
VOLUME LIST 1 1
1 SURF GRID GRID_INTEGRAL
FRONTIER LIST 1 1 -1
2 SURF GRID GRID_INTEGRAL
FRONTIER LIST 1 1 -1
3 TRACK GRID GRID_INTEGRAL
VOLUME LIST 1 1
3 COLL GRID GRID_INTEGRAL
VOLUME LIST 1 1
4 TRACK GRID GRID_INTEGRAL
VOLUME LIST 1 1
END_SCORE
The results are:
• The flux and reaction rates requested using the collision estimator give zero values. This is because there
is no collision in the empty space and the estimator can therefore not operate.
• The track length estimator uses the fraction of the trajectories that pass through volume 1 for the energies
in the grid interval. For the unique interval of this example, these fractions are 5×
√
2 ≃7.071 cm
for each neutron. We must, therefore, have a flux (integrated in volume) of 7.071 neutrons·centimeters,
given a source normalized to 1 neutron (the weight being 1 each time). Since the source is actually normalized
to 3, the following volume integrated flux is obtained: 3×7.071 ≃21.2 neutrons·centimeters.

<!-- page 233 -->
• The surface-based flux depends on the order in which the volumes are given for determining the area.
The flux is calculated by dividing the weight (1 in this case) of the particle passing through by the
cosine of the angle (45 degrees here) with the normal to the surface (a cosine of 1/
√
2 here). There
should, therefore, be a flux (integrated over a surface) of
√
2 ≃1.41 neutrons for a source normalized
to 1 neutron. As the source is actually normalized at 3; hence, the following flux is obtained (integrated
over a surface) of 3×
√
2 ≃4.24 neutrons·centimeters.
• The current depends on the order in which the volumes are given to define the surface. It is zero from -1
to 1 since no particles come from outside the geometry. It is calculated by taking the weight (here 1) of
the particle passing through the surface. There should, therefore, be a current (integrated over a surface)
of 1 neutron for a source normalized to 1 neutron. As the source is in fact normalized to 3, a neutron
current of 3 is obtained.
• Reaction rates are calculated by weighting the flux by a function. Here, the weighting is performed using
the microscopic fission cross-section of uranium-235 (1.196 barns, i.e., 1.196 × 10−24 cm2 at 1 MeV
with ENDF B-VI, see MF=3,MT=18 in the evaluation file). What is obtained is, therefore, a microscopic
fission rate (integrated in volume) of 21.2×1.196×10−24 = 25.39×10−24 particles created by fission
in the volume. Usually, the particles do not have the same energy, and appropriate weighting is required.
• The dose equivalent rate is calculated by weighting the flux by a function.
Here the function is
1.51 (µSv/h)(n/cm2-s) at 1 MeV. What is, therefore, obtained is a dose equivalent rate (integrated in
volume) of 21.2 × 1.51 = 32.01 µSv/h. Usually, the particles do not have the same energy, and appropriate
weighting is required.
Note: if surface values had been given (100 cm2) and volumes (1000 cm3) by:
VOLSURF
SURFACE 1
1 -1 100
VOLUME 1
1 1000
END_VOLSURF
it would have been necessary to divide the obtained values by the volume or the surface data. Thus, the
volume-based flux would have been 0.0212 neutrons per cm2. The surface-based flux would have been
0.0424 neutrons per cm2 and the current 0.03 neutrons per cm2. The volume-based fission rate would have
been 0.02539 × 10−24 particles created by fission per unit of volume (for a 3-neutron source). The dose
equivalent rate would then have been 3.2×10−2 µSv/(h · cm2).
Defining scores for the criticality calculation example of chapter 5
SCORE 5
1 COLL
GRID GRID_FLUX

<!-- page 234 -->
VOLUME LIST 2 4 7
1 SURF
GRID GRID_FLUX
FRONTIER LIST 1 1 2
2 TRACK
GRID GRID_ABSORPTION
VOLUME LIST 2 5 8
3 TRACK
GRID GRID_ABSORPTION
VOLUME LIST 3 1 4 7
4 TRACK
GRID GRID_ABSORPTION
VOLUME LIST 8 1 2 3 4 5 6 7 8
END_SCORE
Important: in the case of surface-based definition of volumes, the boundary plane between volumes 1 and
2 is, in fact, the boundary between volumes 12 (virtual and joined at 1, see section on geometry) and 2.
Consequently, the code cannot calculate the normal vector for volume 1 on this boundary. But, it can calculate
the normal vector to volume 2, TRIPOLI-4® can indeed compute the normal vector at the 1-2 interface.

### 15.9.2 USING THE KEYWORD ENTROPY

Using the keyword ENTROPY in the MESH command or in the EXTENDED_MESH command is optional. When
using it, two values are printed in the output file: the Shannon and the Boltzmann entropies[28]. This values
are not integrated over every batches but are those calculated at the current batch. Thus, if the user wants to
proceed a detailed study of the evolution of entropy, he has to request a batch by batch edition. Moreover,
the computation of entropy of sources has a physical meaning in criticality only if it is based on a fission rate
(code 33, cf 13.4).
Warning: the Shannon entropy is not computed in parallel mode. Alternatively, the user can temporarily
run in monoprocessor mode since the behaviour of the source convergence is similar in both modes: when
studying the entropy in monoprocessor mode, it is possible to find out the number of batches necessary to
reach the source convergence and discard then as many batches in the parallel run.
Example:
RESPONSES 1
REACTION NEUTRON
NUCLEUS U235 COMPOSITION FUEL
INTERACTION 1 33
END_RESPONSES

<!-- page 235 -->
SCORE 1 COLL
GRID DEC_INTEGRAL
MESH
ENTROPY 20 20 1 10 10 300
FRAME 5 5 150 END_SCORE
This command block activates the computation of fission rates in each cell of the 20×20×1 mesh of cell sizes
10 ∗10 ∗300 with the reference cell being centered in (5,5,150). The energy grid used is DEC_INTEGRAL.
The entropy computation is usually based on one group.
Theses fission rates are computed only on the U235 nucleus of the FUEL composition.
Then, the code computes the entropy of the source distribution (i.e. ν-fission rates) on the requested mesh.
The result is thus a scalar value, its batch by batch evolution is used to guess the fission source stability. The
code uses two different expressions of entropy: - the Shannon entropy - and a first order correction of the
latter: the Boltzmann entropy. Important variations of entropy can reveal source convergence problems in
criticality studies.
