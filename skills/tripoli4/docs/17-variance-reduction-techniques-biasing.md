# VARIANCE REDUCTION TECHNIQUES (BIASING)
<!-- source PDF pages 239-261 -->

<!-- page 239 -->
Chapter 17
VARIANCE REDUCTION TECHNIQUES
(BIASING)
Variance
reduction
techniques
are
defined
between
the
keywords
VARIANCE_REDUCTION
and END_VARIANCE_REDUCTION. This command must be called once for a purely neutron (or purely gamma)
problem with the keyword NEUTRON (or PHOTON). The command must be called twice for a combined neutron
and gamma problem: once using the keyword NEUTRON and once with the keyword PHOTON. For other types
of particles, it is not possible (with this version of the code) to define a variance reduction technique.
Variance reduction is defined by inputting:
• a particle type;
• a biasing energy grid;
• one or more targets determining the zone of maximum importance;
• a biasing mesh containing the geometry of the problem;
• a biasing type (user or automatic).
Visual output can be requested.
Notes:
• Variance reduction techniques are not implemented for homogenized multigroup cross-sections.
• Adaptive Multilevel Splitting (AMS) and weight windows can also be used as variance reduction technique
and are detailed in Chapters 18 and 19.
• The CADIS variance reduction scheme is available through a coupling with the IDT deterministic solver,
and is detailed in Chapter 20.

<!-- page 240 -->
The syntax is as follows:
VARIANCE_REDUCTION
NAME <biasing_name>
<PARTICLE_TYPE>
GRID
Grid data
∗1
DETECTOR
Discrete detector data
∗1
DETECT_RHO
Detection surface data (cylindrical)
∗2
MESH
Uniform mesh data
END_MESH
∗2
MESH_VARIABLE
Nonuniform mesh data
END_MESH_VARIABLE
INTERPOLATION flag
INIPOND
Biasing type data
END_INIPOND
ALFA
Energy biasing data
TIME
Time biasing data
#
STORE_IN_FILE <format>
#
USE_FILE <format> filename
GRAPH
Display data
END_VARIANCE_REDUCTION
• The name of the biasing is optional. In the case of a coupled radiation shielding-criticality simulation
(see chapter 22), this data is mandatory in order to specify in which type of simulation the biasing must
be used.
• The possible values for <PARTICLE_TYPE> are NEUTRON or PHOTON.
• Grid data, detector data, mesh data, inipond data and optional ALFA, TIME, and GRAPH data are detailed
in the following sections of this chapter.
• The optional keyword INTERPOLATION enables to deactivate (if flag equals 0) or to force (if flag equals
1) the spatial interpolation on the importance map (see section 17.2), for each biasing group (by default,
the code tries, for each group, to verify a criterion on the variation of the importance of more than 20
between the centers of neighbor cells, and activates or not the interpolation on the whole mesh, for the
current biasing group).

<!-- page 241 -->
• STORE_IN_FILE allows for the spatial importance map to be stored in a file. Its format is given by the
keyword <format> which can be either ASCII, ASCIIG or XDR.
– In the ASCII case, an ASCII file filename.importanceMap.bcd is dumped, where filename is
the name of the input deck data file. It contains keywords readable by the code, user’s data on the
biasing energy grid and mesh, and values produced by the code : the spatial importance values by
group and cell, the k factors (see section 17.2) by material and group and the adjusting factors by
group. This file can be used in subsequent TRIPOLI-4® simulations, e.g., in parallel mode (see
chapter 33) in order to impose the same importance map to all simulators.
– In the ASCIIG case, a file filename.importanceMap-group<igroup>.general is dumped for
each group (as also obtained with the keyword STORE_IMPOR_IN_FILE of version 7 of the code),
with a general ASCII format usable by tools such as OpenDX, where filename is the name of the
input deck data file.
– In the XDR case (XDR meaning processor independent binary format), the file is named
filename.importances<pid> for neutrons and filename.importances_g<pid> for photons,
where filename is the name of the input deck data file and the number <pid> is the process
id that is found at the beginning of the results file. This case is equivalent to the keyword
STORE_IMPOR_IN_FILE of TRIPOLI-4® versions up to 7.
• USE_FILE allows the user to load a file previously generated either by TRIPOLI-4® (with the
STORE_IN_FILE option) or by another code and related to the same geometry and materials. The format
of the file must be specified by the keyword <format> which can be either ASCII or XDR. The name of
the file is filename.
– The ASCII case should be used together with the keyword MONITORING 0 in the SIMULATION command
block (see chapter 22) in order to avoid the calculation of new adjusting factors by TRIPOLI-
4®. The structure of the file is that produced by the STORE_IN_FILE keyword, however, the k
factors are optional and can be recomputed by the code on the given biasing mesh when missing.
– The XDR case is equivalent to the keyword USE_IMPOR_FILE of TRIPOLI-4® versions up to 7.
Geometry, materials, and biasing must be left unchanged between the storage and use modes. This
old option enables only to save the cost of initializing biasing data in memory.

## 17.1 THE CONCEPT OF A WEIGHT

For radiation shielding problems with strong attenuation, it is possible to bias the transport of the particles
emitted in order to mainly simulate trajectories whose contribution to the expected result is the greatest [9],
[13], [14], [78], [79]. Each particle is assigned a weight, the inverse of the weight being importance.
Weight Π of the particle is factorized as follows:
Π(r,Ω,E,t) = Π1(r)·Π2(Ω)·Π3(E)·Π4(t)
where:

<!-- page 242 -->
• the spatial dependence Π1(r) is calculated by INIPOND, either automatically or with data supplied by
the user for a selected mesh. In reality, an energy dependence is still present in the spatial biasing (see
below) and Π1(r) = Π1(r,Eg).
• the dependence on direction Π2(Ω) is calculated by the code;
• the energy dependence Π3(E) is of the form
1
Eα;
• the time dependence Π4(t) is of the form
1
(1+λt).

## 17.2 SPATIAL BIASING

The values of Π1(r) are calculated to establish importance maps. An importance map consists of the importance
values (inverse of the particle weight) given at the center of each cell of a cylindrical or parallelepipedic
mesh. Importances are calculated using bias parameter values k (homogeneous to a cross-section) for each
composition and either point detector positions or a cylindrical detector surface. The code calculates the
importance maps for a number of energy ranges Eg. For each energy range or biasing energy group there is
a corresponding value of k, hence a map.

### 17.2.1 BIASING ENERGY GROUPS

The user must indicate the grid of biasing energy groups: each group is associated with an importance
map. There is, therefore, an energy dependence of the spatial biasing. It is necessary for the biasing grid
to contain the simulation energy domain. The number of groups for neutrons is typically 3 to 5 in order to
obtain satisfactory results, e.g.,
• one group for E > 2 MeV;
• one group for 5 eV < E < 2 MeV;
• one group for E < 5 eV.
With INIPOND, there must be at least two biasing groups.
The lowest bound of the given groups must be less than 10−10MeV.
The user enters the data as follows:
GRID
nb(bounds)
energy(1)...energy(n)

### 17.2.2 DETECTORS

At the present time, two types of biasing are available: either the results are optimized at discrete points of the
geometry (detectors, specified in the DETECT command) or a specific analytical form is imposed for the equi-

<!-- page 243 -->
importances (available forms are plane, cylindrical, and spherical), then complementary data for detection
surfaces are input using the DETECT_RHO command (for the cylindrical and spherical cases) or the DETECT
command (for the planar case).
• The discrete detector case:
This corresponds to the type of biasing already used in code versions 3 and earlier. For each detector
there is a corresponding coefficient β that specifies, when using automatic biasing with INIPOND, the
degree of biasing (i.e., the value of bias parameter k). The coefficient is between 0 and 1. The higher the
value of β is, the stronger the attraction of the particles towards that point is. The value of k is calculated
using the value of β1 for the first detector. A value of β1 = 0.5 for the first detector is sufficient for
typical cases. The other values of β can give the value close to the detector (in reality, for each group g,
the value of Ig that plays a role in the importance formula). Similarly, when user biasing is utilized in
INIPOND, the coefficient plays a role for the values close to the detector (factor Ig).
The values of k in the biasing groups corresponding to the user choice, as well as other values for
different choices, are indicated in the TRIPOLI-4® output file.
The syntax is as follows:
DETECTOR
nb(detectors)
D1x D1y D1z
β1
...
Dnx Dny Dnz
βn
where (Dix, Diy, Diz) are the coordinates (in the reference frame of the geometry) of the ith detector
and βi is the corresponding coefficient.
These points are used to create the importance maps, and have no connection with physical detectors
(for measuring flux for instance). They are used to attract particles to a specific point.
• The splitting sphere case:
It may be helpful, in neutronic calculations, to increase the number of neutrons about an instrumentation
point/detector, for instance.
The syntax is as follows:
CENTRAL_SPLITTING
weight_min
radius
where weight_min is the minimum weight authorized for a neutron and radius is the radius of the
(fictitious) splitting sphere about each of the detector points given in the DETECT command.

<!-- page 244 -->
• Case of a detection surface of an imposed analytical form:
This applies to plane, cylindrical, or spherical forms.
For the cylindrical and spherical cases, the user indicates the cylindrical or spherical detection surface
radius and the coefficient β, the degree of biasing, which is used (as in the case of discrete detectors) to
calculate the values of k for the different groups.
The syntax is as follows:
DETECT_RHO
1
ρ(D)
βD
where data item 1 must always be present: number of detection surfaces, where ρ(D) designates the
radius of the detection surface and βD designates the associated coefficient related to the degree of
biasing.
For the plane case, the syntax of the DETECT command is the same as in the case of discrete detectors,
but, in this case, nb(detectors) is 1 and (D1x, D1y, D1z) are the coordinates of a point on the
detection plane.
For these three analytical cases, the other data concerning the surface (for example, in the cylindrical
case: the axis of the cylinder for positioning it in the geometry) are included in the INIPOND command.

### 17.2.3 CALCULATION OF SPATIAL IMPORTANCE

#### 17.2.3.1 For biasing with discrete detectors

The spatial importance at point r for an energy group g ([Eg,Eg+1]) is given by:
I1(r) =
1
Π1(r) = Ige−min(Pi) ∑
ni
j=1 k[C(i,j)]·d(i,j)
where:
• Pi is one of the possible trajectories between the current point r and the detector point r0 determining
the zone of maximum importance;
• ni is the number of compositions passed through by trajectory Pi;
• C(i, j) is the jth composition passed through by trajectory Pi;
• d(i, j) is the distance travelled in composition C(i, j) by trajectory Pi.

<!-- page 245 -->
Close to the detector I1(r) = Ig. The value is calculated as follows:
Ig =
1
β+1
Eβ+1
g+1 −Eβ+1
g
Eg+1 −Eg
.
Thus, for a single composition, thus a single possible k, the importance at any point is proportional to
exp(−kd), where d is the distance between the point and the detector (minimum trajectory).

#### 17.2.3.2 For an analytical biasing (plane, cylindrical, or spherical)

The spatial importance at point r for energy group g ([Eg,Eg+1]) is given by:
I1(r) =
1
Π1(r) = Ige−∑n
j=1 k[C(j)]·d(j)
with notations analogous to those used in usual discrete detector biasing, except that only one trajectory is
possible (hence no index i). The trajectory is:
• orthogonal to the plane for a plane detection surface,
• radial with respect to the axis of the cylinder of biasing for a cylindrical detection surface,
• radial with respect to the center of the sphere of biasing for a spherical detection surface.
The trajectory goes from point r to the detection surface. As such, for a single composition, thus one k
possible, the importance at any point is proportional to exp(−kd), where d is the distance between the point
and the detection surface. This trajectory is along the normal unit vector of the plane (in plane biasing), the
radius vector with respect to the axis of the cylinder in cylindrical coordinates, and the radius vector relative
to the center of the detection sphere in spherical coordinates.

#### 17.2.3.3 For biasing with a splitting sphere

The spatial importance at point r is given by:
I1(r) =
1
Π1(r) = Ige
−∑n
j=1 min(
1
weight_min, radius2
d j(r)2 )
where:
• j is the index of the detector,
• n is the number of detectors,
• d j(r) is the distance between point r and detector j,
• radius is the radius of the splitting sphere.

<!-- page 246 -->
### 17.2.4 MESH AND IMPORTANCE MAPS IN TRIPOLI-4®

A mesh is defined between the keywords MESH and END_MESH for a uniform mesh, or MESH_VARIABLE and
END_MESH_VARIABLE for a nonuniform mesh.
For each case, two options are possible: a Cartesian mesh and a cylindrical mesh.

#### 17.2.4.1 Cartesian mesh

The Nx′ × Ny′ × Nz′ parallelepipedic cells are directed along the axes of an orthonormal reference frame
(O′x′,O′y′,O′z′) = (O′,i′,j′,k′) that is distinct from that of the geometry and larger than it. The dimensions
of each cell are dx′, dy′ and dz′ along the three directions of the reference frame.
The origin point corresponds to the minimum coordinate point (Xmin, Ymin, Zmin) of the region in which
the mesh extends, and the axes give the directions of the sides of the cells.
X
Y
Z
O
X’
O’
Z’
Y’
Figure 17.1: Example of a uniform Cartesian mesh of 2×2×2 cells in a (O′x′,O′y′,O′z′)
reference frame

#### 17.2.4.2 Cylindrical mesh

The reference frame associated with the cylindrical mesh makes it possible to access the cylindrical coordinates
(ρ,θ,z) of the points (and the centers of the cells). The orthonormal reference frame associated with
the cylindrical mesh is of the same type as that used to define distributed sources: the coordinates of a vector
O′M are:
O′M = ρcosθi′ +ρsinθj′ +zk′.

<!-- page 247 -->
The user gives the origin O′ and the vectors i′ and k′, the second vector j′ of the orthonormal reference frame
being calculated automatically by vector product. The angles are defined counter-clockwise with respect to
axis (O′,i′). The size of the Nρ′ ×Nθ′ ×Nz′ cells are: dρ′, dθ′, and dz′ along the three coordinates, respectively
(the angles are in radians).
In both the Cartesian and cylindrical cases, importances are calculated at the centers of the cells
thus constructed. However, the center does not mean the center of gravity of the cell but the geometrical
center, or the midpoint in each discretization, (in ρ, in θ, and in z, for the cylindrical case).
A neighborhood degree (neighborhood) can be specified, a value of 3 must always be entered.
Important:
• The mesh must contain the geometry, and can, therefore, extend beyond it. However, the centers of the
cells containing a discrete detector must belong to the geometry. In addition, the planes that define the
cells must differ from the planes bounding the volumes, and the centers of the cells must not be on the
boundaries of the geometry.
• Regarding the cylindrical detection surface, it must be included in the geometry over a height (coordinate
z) that is significant (greater than 10−3 centimeters). If it extends beyond the geometry, the optical
distances calculated between certain cell centers and the part of the detection surface outside the geometry
will be set to infinity (zero importance at the centers of these cells). It should be noted that the
code can stop (and display an error message) if it samples these points during the source normalization
calculation or if, during the simulation, it evaluates the inverse of the importance at these points.
• Finally, again in the case of a cylindrical mesh, the mesh can extend beyond the geometry (centers
of cells outside the geometry, for which the importance will be zero), provided that the geometrical
boundaries are included in cells whose centers belong to the geometry.
Note:
The user can combine a Cartesian mesh with usual discrete detector biasing or with analytical biasing. Similarly
, it is possible to combine the cylindrical mesh with any of the available biasings. The following cases
are of particular interest: cylindrical biasing with a cylindrical mesh (making it possible to obtain cylindrical
equi-importances highly smoothed over the mesh) and biasing with discrete detectors and a cylindrical mesh
(cylindrical geometry but the points for which the results are to be optimized remain discrete). The case with
a single cell in the θ variable can also be useful in attracting particles uniformly to rings, in each of which the
user has placed a discrete detector.
In the other cases of analytical biasing, best results will be obtained using the most suitable mesh. Cartesian
mesh will be well adapted to plane biasing, for example.

#### 17.2.4.3 Refining the mesh

In the case of a uniform mesh, it is possible to refine the mesh in certain particularly sensitive areas using the
DIVISION WINDOW command.
The number of cells is then multiplied by 8 (a factor of 2 for each of the 3 coordinates) in the region involved,

<!-- page 248 -->
limited by two points whose coordinates are given in the new reference frame: (X′min,Y ′min,Z′min) and
(X′max,Y ′max,Z′max) if Cartesian, (ρ1,θ1,z1) and (ρ2,θ2,z2) if cylindrical, with the indices 1 (or 2) corresponding
to the minimum (or maximum) coordinates for coordinates ρ and z; however, for angular definition,
θ1 and θ2 are given counter-clockwise (it may be that θ1 > θ2, if the initial mesh extends fully in [0,2π],).

<!-- page 249 -->
#### 17.2.4.4 Uniform mesh syntax

The syntax for Nx′ ×Ny′ ×Nz′ regular cells of dimension dx′, dy′, dz′ is :
MESH
Nx′ Ny′ Nz′
dx′ dy′ dz′
neighborhood
FRAME
<FRAME_TYPE>
O’x O’y O’z
i’x i’y i’z
(j’x j’y j’z)
k’x k’y k’z
DIVISION WINDOW
X’min Y’min Z’min
X’max Y’max Z’max
END_MESH
where (x′,y′,z′) are either Cartesian coordinates in the case of a Cartesian mesh, or cylindrical coordinates of
the (ρ,θ,z) type in the case of a cylindrical mesh.
The definition of a frame is explained in section 4.5. Important From version 3, the reference frame type
<FRAME_TYPE> must be specified. It may be either CARTESIAN or CYLINDER. Data files made for earlier
versions than 3 must be modified accordingly.
From version 8 on, the cell size can be defined inferior to 0.1 cm.
It must also be borne in mind (note previous remark) that, in the block DIVISION WINDOW, θmin < θmax is not
necessarily true if the reference frame is cylindrical.
At the present time, neighborhood must equal 3.

#### 17.2.4.5 Nonuniform mesh syntax

For certain problems it can be useful to define fine cells in certain areas of the geometry (around the detector,
on the contributing paths between the source and the detector ...). A uniform mesh even with a local refinement
may not be sufficient then, or could lead to simulation time problems because of the too large number
of cells. This can happen particularly :
• for large geometries, when tallying in a precise zone is requested,
• in configurations where there is locally a strong attenuation in certain compositions.
It can thus be judicious to use a nonuniform mesh.
The syntax for a nonuniform mesh of Nx′ ×Ny′ ×Nz′ cells is :

<!-- page 250 -->
MESH_VARIABLE
Nx′ Ny′ Nz′
0 N1 x’1 N2 x’2 ... Nn x’n
0 M1 y’1 M2 y’2 ... Mm y’m
0 P1 z’1 P2 z’2 ... Pp z’p
neighborhood
FRAME
Mesh data
END_MESH_VARIABLE
where :
• x′
1,...,x′
n,y′
1,...,y′
m,z′
1,...,z′
p are given in the mesh frame (Cartesian or cylindrical);
• N1 is the number of regular cells between coordinates 0 and x′
1
• Ni is the number of regular cells between coordinates x′
i−1 and x′
i
• M1 is the number of regular cells between coordinates 0 and y′
1
• M j is the number of regular cells between coordinates y′
j−1 and y′
j
• P1 is the number of regular cells between coordinates 0 and z′
1
• Pk is the number of regular cells between coordinates z′
k−1 and z′
k
• moreover, these data must verify :
N1 +N2 +...+Nn = Nx′
M1 +M2 +...+Mm = Ny′
P1 +P2 +...+Pp = Nz′
From version 8 on, the resulting cell sizes can be inferior to 0.1 cm.
• the data on the neighborhood degree and the frame are the same as for the uniform mesh.

### 17.2.5 BIAS PARAMETER k

After establishing the mesh, it is necessary to give the parameters for the weight calculation. TRIPOLI-4®
provides two options for bias parameter k, either:
• the values of k are given by the user for each composition (from 1 to n) and each biasing group (from 1
to nbgroups) in order of decreasing energy (corresponding to the order in which the bounds have been
entered). This is written as follows:

<!-- page 251 -->
INIPOND
DATA
name(compo1)
k1...knbgroups
...
name(compon)
k1...knbgroups
END_INIPOND
• the values of k are calculated by solving the Placzek equation, after collapsing the pointwise crosssections
in each composition and each biasing group. The syntax is:
INIPOND
AUTO
END_INIPOND
If the name of the material is VOID, the value of k is set by taking the lowest value among the other
values of k and dividing it by two.

### 17.2.6 SMOOTHING OPTION

INIPOND is designed to compute importance maps optimized for the use of the Exponential Transform variance
reduction technique. Amongst other optimizations, INIPOND smoothes importance values to prevent
weight discrepancies in the simulation. This behaviour is the default behaviour. However, it can be useful to
deactivate this option, for example in case of using the AMS (see Chapter 18) variance reduction technique with
an INIPOND importance map. This can be done by inserting the optional line SMOOTHING 0 in the INIPOND
command block:
INIPOND
...
SMOOTHING 0
END_INIPOND

## 17.3 DIRECTIONS OF INTEREST

• In the case of biasing with discrete detectors (block DETECT already given), the directions of interest are
constructed by calculating the gradients of the spatial importance.

<!-- page 252 -->
• If the detection surface is of the analytical type (cylindrical or spherical, with a radius already given in
block DETECT_RHO, or plane, with a point belonging to the plane already given in block DETECT), it is
supplemented here with data making it possible to establish the detector surface (example: in cylindrical,
we set the axis of the cylinder) and hence to establish the directions of interest, pointing from the point
of calculation to the detection surface (in this case, the directions of interest are, therefore, independent
of the energy group). When a mesh cell is crossed by the detection surface, the null vector is assigned
to the direction of interest associated with that cell.
The syntax is as follows, again within the INIPOND block:
INIPOND
*
DATA
*
AUTO
OMEGA
#
GRAD_I
#
SET_OMEGA
<ANALYTICAL_BIASING_TYPE>
Analytical biasing type data
END_INIPOND
The option GRAD_I in the OMEGA command is also the default option, taken into account if the two keywords
OMEGA and GRAD_I are not given (for reasons of backward compatibility, for data files corresponding to
versions preceding version 3).
The option SET_OMEGA indicates that a specific analytical form is to be set for the directions of interest (this
option requires setting the analytical form for the directions of interest and for the spatial importances).
Currently, the possible options for <ANALYTICAL_BIASING_TYPE> are CYLINDER, PLANE, or SPHERE. The
data for this analytical biasing type are then specified:
• For cylindrical biasing:
SET_OMEGA
CYLINDER
ux uy uz
cx cy cz
where ux, uy and uz are the components of the unit vector for the axis of the biasing cylinder and cx, cy
and cz are the coordinates of a point on the axis. All the coordinates are given in the Cartesian reference
frame of the geometry.
If the mesh is cylindrical, the two Z-axes of the cylinders (defining both mesh and biasing) must have
parallel unit vectors.

<!-- page 253 -->
SET_OMEGA
PLANE
ux uy uz
• For plane biasing:
Coordinates of the vector normal to detection plane (ux, uy and uz) are given here in the geometry frame.
This vector must not be zero, but need not be normalized.
• for spherical biasing:
SET_OMEGA
SPHERE
cx cy cz
Coordinates (cx, cy and cz) of the point C, center of the biasing sphere, are given in the geometry frame.
This point must be included in the biasing mesh defined earlier using the keyword MESH.

## 17.4 ENERGY BIASING

As indicated previously, the importance (inverse of weight), in each group, takes the form of Eα and is written
as follows, in the case of n biasing groups:
ALFA
α1...αn
The data for this biasing is optional and by default αi = 0.

## 17.5 TIME BIASING

As indicated previously, the importance (inverse of weight), in each group, takes the form of 1 +λt and a λ
parameter. It is written as follows:
TIME
λ
The data for this biasing is optional and by default λ = 0.

<!-- page 254 -->
## 17.6 SPECIAL BIASING

Use of these types of biasing is reserved to very special cases and to expert users only. We advise exhausting
all of the other biasing settings options previously described in this chapter rather than using these "special
case" options.

### 17.6.1 SPLITTING WHEN ENTERING SPECIFIC VOLUMES VOLUME_SPLITTING

This type of biasing splits the particles entering one or more particular volumes in cases where the user is
aware that the passage of these particles in these volumes is of interest for the requested scores. As such, the
statistics for the requested scores are improved.
This type of biasing has only been developped for neutrons and requires working in simulation mode
CROSS_SPLIT specified in the directive SIMULATION (this option is used to treat the transport between two
collisions with sampling performed volume by volume, and is more costly in terms of simulation time than
the default option QUOTA_SAMPLING).
The syntax for the data of the VOLUME_SPLITTING biasing option is as follows:
VARIANCE_REDUCTION
<PARTICLE_TYPE>
VOLUME_SPLITTING LIST nb(volumes)
volume(1) weight(1)
volume(2) weight(2)
...
volume(n) weight(n)
END_VARIANCE_REDUCTION
where:
• <PARTICLE_TYPE> equals NEUTRON
• volume(i) is a volume number
• weight(i) is the associated reference weight. The reference weight Πre f is used to set the number n of
particles to be split.
n = (int) Πre f / W with W being the simulation weight for the particle before the splitting is performed.
Volumes that do not figure on the list have a default reference weight of 1.

<!-- page 255 -->
### 17.6.2 OPTICAL BIASING

This type of biasing modifies the total macroscopic cross-section for certain volumes by multiplying the total
cross-section by a factor. This factor β is defined by the user for each volume such that:
Σ∗
t =Σt×(1 - β)
• If β < 0, the cross-section is increased. For example, if β = -9, the cross section is multiplied by 10.
• If β > 0, the cross-section is decreased. For example, if β = 0.5, the cross-section is divided by 2.
The syntax is as follows:
VARIANCE_REDUCTION
<PARTICLE_TYPE>
OPTICAL_VARIANCE_REDUCTION LIST nb(volumes)
volume(1) beta(1)
volume(2) beta(2)
...
volume(n) beta(n)
END_VARIANCE_REDUCTION
where:
• <PARTICLE_TYPE> equals NEUTRON or PHOTON
• volume(i) is a volume number
• beta(i) is the associated beta coefficient.

### 17.6.3 RUSSIAN ROULETTE CONTROL

When a INIPOND type biasing is defined, the splitting and Russian roulette are automatically managed by the
code.
When no biasing is defined, a Russian roulette process is nevertheless used in order to manage small weights
before the sampling of each collision (by default, it is used when the simulation weight for the particle is less
than 0.8).
The user has now the option to control the Russian roulette process:
• the user may define the global threshold of the Russian roulette (the global value replaces the default
threshold of 0.8)
• the user may define a threshold for each volume of a volume list
• the user may completely suppress the Russian roulette (global threshold is 0).

<!-- page 256 -->
This mode of biasing has only been developped for neutrons.
The user may also refer to the global
RUSSIAN_ROULETTE option of the simulation command block, available for all particles (see chapter 22).
The syntax for the data is as follows:
VARIANCE_REDUCTION
<PARTICLE_TYPE>
CONTROL_RUSSIAN_ROULETTE
*
LIST nb(volumes)
volume(1) threshold(1)
volume(2) threshold(2)
...
volume(n) threshold(n)
*
GLOBAL_VALUE threshold
END_VARIANCE_REDUCTION
where:
• <PARTICLE_TYPE> equals NEUTRON
• volume(i) is a volume number
• threshold(i) is the associated threshold.
All of the threshold values are real numbers.

### 17.6.4 SPECIAL SOURCE BIASING

The TRIPOLI-4® variance reduction scheme yields to a biased transport but also a biased source distribution.
For special cases where no biased transport is needed but a biased source distribution is needed to enhance
particular source energies or angles, it can be more convenient to directly adjust biasing parameters for the
source. In such cases the user may refer to subsections 12.3.4 and 12.4.7. Note that the source energy and/or
angle biasing defined in these subsections are not compatible with the variance reduction techniques defined
in the present chapter.

## 17.7 VARIANCE REDUCTION TECHNIQUES FOR COUPLED NEUTRON PHOTON SIMULATIONS

The use of variance reduction techniques for neutrons only is not always sufficient when simulating a coupled
neutron photon problem : biasing for both neutrons and photons may then be defined. In this case, the
difficulty relies in defining a proper neutron biasing, so as to sample important photons in appropriate areas
of the phase space, in terms of photon tallies.

<!-- page 257 -->
A diagnosis tool can be used to ease the adjustment of this neutron biasing. It enables to find out the highest
neutron importances (based on the photon production data given by the nuclear data and the user’s defined
photon biasing). The diagnosis is done at the end of the biasing initialization, during the initialization step
of the run and before stopping: no simulation follows, so as to enable the user to modify the neutron biasing
parameters, in the light of the diagnosis results, and rerun without this option.
To request this diagnosis, two VARIANCE_REDUCTION command blocks have to be defined, one for neutrons
and one for photons, in the way described in this chapter. As a restriction, biasing energy grids must be the
same for neutrons and photons. The special option AUTO_COUPLING has to be requested in the INIPOND part
of the neutron command block with the following syntax:
INIPOND
AUTO_COUPLING
HEIGHT height
*
GRAPH_CONTOURS
*
GRAPH_NO_CONTOUR
Px Py Pz
Lu Lv
<AXIS>
Flag
FILE filename
THRESHOLD_RATIO threshold
END_AUTO_COUPLING
END_INIPOND
A list of cells of highest neutron importances (ordered from 1 to a given threshold ratio of the maximal
importance) is edited for each biasing group in the results file (the coordinates of their center and the ratio
of their importance over the maximum neutron importance of the group are given) and a coupled neutron
importance map file is produced (named "<inputdeck>.importanceCoupledMap.bcd" in monoprocessor
mode and "<inputdeck>.importanceCoupledMap.<n>th_task.bcd" in parallel mode, where
<inputdeck> stands for the name of the TRIPOLI-4® input deck file). The option THRESHOLD_RATIO enables
to modify the threshold for the edition of cells of highest importance. The value of threshold must be
between 0 and 1, the default value being 0.5.
The calculation is then stopped. Therefore, it should be noted that no result needing the simulation of batches
(even the first ones) can be obtained when requesting this diagnosis (e.g., score editions or importance maps
dumped after monitoring of the first 5 batches, such as requested by the STORE_IN_FILE option with the
ASCII format). If needed, these results and dumps should be requested in the next run.
When the optional graphical output is requested in addition, the cell centers of highest neutron importance
are displayed on 2D-views. height is the projection height on these 2D-views, GRAPH_CONTOURS enables to
display also the geometry contours, whereas GRAPH_NO_CONTOUR displays none of them. The parameters of
the window are input in the same way as for the display of importance maps (see section 17.8).
Several graphs may be requested with several GRAPH_CONTOURS or GRAPH_NO_CONTOUR commands. Flag is
0 if a Postscript file is not required. In this case, a window is displayed and if the user a posteriori decides

<!-- page 258 -->
to dump the associated Postscript file, he can do it with the Shift-P command in the graphical window.
Otherwise Flag is 1 and there is no display window but the associated Postscript file is dumped.
The option FILE allows for the user to specify the associated file name. By default, PostScript files are named
"<inputdeck>_highest_I_groupM_N.ps", otherwise they are named "filename_groupM_N.ps" where
M is the number of the neutron biasing group and N is the number of the graph. They are numbered in the
order in which the graphs are requested.
The colors of the displayed points are {red; orange; yellow; green; cyan; blue} for a ratio to the maximal
importance of {1 to 0.99; 0.99 to 0.9; 0.9 to 0.8; 0.8 to 0.7; 0.7 to 0.6; 0.6 to 0.5} respectively.
The user can then perform a complete coupled neutron photon simulation by using the diagnosis results to
adjust the neutron biasing parameters (position of the INIPOND detectors, β factors).

## 17.8 GRAPHICAL DISPLAY

It is possible to monitor the importance maps by a 2D-view of the geometry. The view is orthogonal to one
of the axes (O′x′, O′y′ or O′z′) of the biasing reference frame. The display window is defined by a point (the
point at the bottom left of the window) and by its dimensions along the two axes defining the 2D-view. The
contours plotted correspond to lines of equal importance. The code plots one graph per biasing group. The
syntax is as follows:
GRAPH
Px Py Pz
Lu Lv
<AXIS>
Flag
FILE filename
where <AXIS> = X, Y or Z and (Px,Py,Pz) is the lower left-hand point of the window, the coordinates being
given in the geometry reference plane OX,OY,OZ. Lu and Lv are the dimensions of the display window.
In the X case: Lu is along y′ and Lv along z′. In the Y case: Lu is along x′ and Lv along z′. In the Z case: Lu is
along x′ and Lv along y′.
If the mesh is cylindrical, the syntax is exactly the same, with X, Y, and Z respectively corresponding to the
three axes of the orthonormal reference frame associated with the cylindrical coordinates.
Note: Once again, for a cylindrical mesh, if the user requests a 2D-view perpendicular to the X or Y axis, it is
necessary for its angular discretization Nθ′ to be adequate, which, in practice, means at least 5 for complete
angular coverage of [0,2π]; otherwise, there is a risk of too many cells being projected onto the 2D view and
the map obtained being illegible (too dark).
Several graphs may be requested. Flag is 0 if a Postscript file is not required. In this case, a window is
displayed and if the user a posteriori decides to dump the associated Postscript file, he can do it with the
Shift-P command in the graphical window. Otherwise Flag is 1 and there is no display window but the
associated Postscript file is dumped.
The option FILE allows for the user to specify the associated file name. By default, PostScript files are named

<!-- page 259 -->
"importance_map_view.groupM_N.ps", otherwise they are named "filename.groupM_N.ps" where M
is the number of the energy group and N is the number of the graph. They are numbered in the order in which
the graphs are requested.
The importance maps are useful for checking the data. However, the 2D-views can give the impression
that several surfaces of equal weight intersect (which is obviously impossible). This is merely a problem of
graphical representation (“spider web” effects can occur).
It is possible to obtain importance maps for several 2D-views.

## 17.9 HINTS CONCERNING BIASING

### 17.9.1 HINTS CONCERNING INIPOND MODULE

Care must be taken not to place the detectors in regions diametrically opposite in the phase space (neutrons
and photons cannot be efficiently driven in opposite directions). If necessary, it is perfectly possible to perform
two different calculations for requested tallying in the neighboring regions with biasings corresponding
to the tallies requested. Consideration should also be given to using symmetry of the problem and cylindrical
meshes.

#### 17.9.1.1 The automatic case

In this case, the code collapses the cross-sections of different media in the multigroup grid of the biasing.
Then, it deduces from these multigroup cross-sections an “opacity” (or attenuation coefficient) for the medium
in each group as a function of the multigroup transport cross-sections and the slowing structure.
• The biasing grid must, therefore, be adapted to the case in point. In a conventional reactor physics
problem covering energies from 20 MeV to 1.E-11 MeV, a basic biasing grid limited to 6 groups
[20.,4.5,2,0.5,1.E −3,5E −6,1.E −11] is recommended by default. The principle is to properly see
the different energy components of the problem, i.e., the region above the fission spectrum, then the
high, medium, and low parts of the fission spectrum, then an epithermal component and, finally, a thermal
group. On the other hand, there should not be too many groups as the cost of biasing (initialization
and storage in memory of the biasing maps) is proportional to the number of groups. However, for a fast
problem, for example, with a lower bound energy of 1 MeV, case corresponding to a n →p reaction for
sulphur), the proposed grid is inefficient. In such cases, it is better to adopt a grid of type [20.,8,4.5,2,1].
The grid has fewer groups and therefore is less costly, and in addition variance reduction will be more
effective for fast neutrons.
• Media that are empty or of very low density must be handled carefully. The collapsing mechanism
generates very low attenuation coefficients (smaller by several orders of magnitude) than those of other
media. This results in importance functions that vary greatly from one medium to another, and hence in
splitting which degrades calculation quality (sometimes up to a point where convergence is prevented).
It is, therefore, recommended to give the compositions a name beginning with the string “VOID”. The
code then calculates the attenuations in these media as a function of the other media, in order to smooth
the importance gradients.

<!-- page 260 -->
#### 17.9.1.2 Mesh

• The cost in terms of memory and cpu time is proportional to the number of cells. It is, therefore, required
to optimize the mesh size for the problem. With more than 10,000 cells, the cost of biasing can become
prohibitive. However, there must be a sufficient number of cells for the paths linking the cell centers to
see the paths taken by particles migrating in the geometry. Accordingly, the DIVISION WINDOW option
makes it possible to locally refine the size of the mesh and thus achieve substantial savings. Or else,
the MESH_VARIABLE command allows a better adjustment of the cells sizes with respect to the different
compositions associated to the volumes of the geometry.
• The geometry must be convex. More precisely, if two cell centers are internal to the geometry, the edge
linking them must be included in the geometry. (If the geometry of the problem is not naturally convex,
it is then necessary to contain it in a box or cylinder, depending on whether a cartesian or cylindrical
mesh is planned.) The mesh must cover all the geometry and should not be tangential to the boundary
of the geometry. It must, therefore, extend beyond it, but by the least possible amount.
• For cylindrical meshes, the value of π used for defining the angular component of the mesh must be precise
to avoid the code stopping with messages indicating overlapping of meshes or, conversely, meshes
indicating that the range [0,2π] is not covered by the mesh. It is, furthermore, strongly recommended to
verify that in the part of the output file relating to the initialization phase, there is no message that diagnoses
this case. This is because, in such a case, a calculation may end up with particles in the angular
zone that is not covered by the mesh, causing the code to stop at that point. It is, therefore, advisable to
have an angular mesh that extends very slightly beyond the zone to be covered (as for Cartesian meshes)
but without causing overlapping of meshes at 2π (which cannot arise in the Cartesian case). The value
used internally by the code is π = 3.14159265. Usually, a value of 3.141593 is adequate for defining the
cells while ensuring that the angular mesh does not extend much beyond [0,2π].

<!-- page 261 -->
A biasing definition (different from the criticality case of the chapter 5)
VARIANCE_REDUCTION
NEUTRON
GRID
4
20.
3.
5.E-6 1.E-11
DETECT
1
0.
407.
0.
0.20
MESH
10 40 10
110.1 50.5 110.1
3
FRAME
CARTESIAN
-550.1 -1000.1 -458.
1.
0.
0.
0.
1.
0.
0.
0.
1.
DIVISION WINDOW
-300 -107 -200
300 107 200
END_MESH
INIPOND
AUTO
END_INIPOND
END_VARIANCE_REDUCTION
