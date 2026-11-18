# DATA ENTRY SEQUENCE
<!-- source PDF pages 525-551 -->

<!-- page 525 -->
Appendix B
DATA ENTRY SEQUENCE
A) GEOMETRY
B) TITLE title (mandatory)
C) If required to specify
• a TYPE, go to C-1
• a surface SURF, go to C-2
• a volume VOLU, go to C-3
If all descriptions have been given, go to E (or D then E) for a 2D-view, otherwise directly to G.
C-1) TYPE numtype (Defines the type of number numtype) In order to obtain:
• a BOX go to C-1.a,
• a SPHERE go to C-1.b,
• a cylinder with axis X, Y or Z: CYLX, CYLY or CYLZ go to C-1.c,
• a cylinder with any axis: CYL, go to C-1.d,
• a CONE, go to C-1.e,
• a hexagonal prism HEXAX, HEXAY or HEXAZ, go to C-1.f,
• a PARALLELEPIPEDE, go to C-1.g,
• a TORUS, go to C-1.h.
Then return to C.
C-1.a) BOX sidex sidey sidez.
C-1.b) SPHERE radius.
C-1.c) CYL[X,Y,Z] half-height_radius.
C-1.d) CYL half-height_radius ux uy uz with (ux,uy,uz) an axis director.
C-1.e) CONE apex_angle ux uy uz with (ux,uy,uz) apex director.
C-1.f) HEXA[X,Y,Z] inscribed_diameter height angle.

<!-- page 526 -->
C-1.g) PARALLELEPIPEDE side(1) side(2) side(3)
axis1(x) axis1(y) axis1(z)
axis2(x) axis2(y) axis2(z)
axis3(x) axis3(y) axis3(z).
C-1.h) TORUS ux uy uz major-radius minor-radius.
C-2) SURF numsurf (Defines the surface of number numsurf). In order to obtain:
• a plane parallel to the planes of reference frame PLANE[X,Y,Z], go to C-2.a,
• any plane PLANE, go to C-2.b,
• a SPHERE, go to C-2.c,
• a cylinder of axis X, Y or Z: CYL[X,Y,Z], go to C-2.d,
• a cone of axis X, Y or Z: CONE[X,Y,Z], go to C-2.e,
• any quadratic QUAD, go to C-2.f.
Then return to C.
C-2.a) PLANE[X,Y,Z] side where side is the side of the plane (if, for example, PLANEX: X=side).
C-2.b) PLANE a b c d plane of equation ax+by+cz+d = 0.
C-2.c) SPHERE x y z radius with (x,y,z) the coordinates of the center and radius the radius of the
sphere.
C-2.d) CYL[X,Y,Z] coordinate1 coordinate2 radius
where coordinate1 and coordinate2 are the coordinates of a point on the axis
(coordinate1,coordinate2)= (y,z) for CYLX, (x,z) for CYLY, (x,y) for CYLZ.
C-2.e) CONE[X,Y,Z] xc yc zc half-angle.
C-2.f) QUAD a b c d e f g h i j quadratic equation ax2+by2+cz2+dxy+eyz+ fxz+gx+hy+
iz+ j = 0.
C-3) VOLU numvolu (Defines a volume of number numvolu) In order to obtain:
• a combinatorial geometry, go to C-3.a,
• a surface-based geometry, go to C-3.b,
• a rotation, go to C-3.c,
• a lattice, go to C-3.d,
• a particular cell, go to C-3.e.
C-3.a) COMBI numtype (Defines a volume on the basis of the type of number numtype)
C-3.a.1) If the type is not based on a cone
centrex centrey centrez (coordinates of center of volume created).
Go to C-3.f.
C-3.a.2) If the type is based on a cone
sommetx sommety sommetz height (coordinates of the cone apex + height of cone).
Go to C-3.f.
C-3.a.3) To center the volume relative to another one, add V_ORIGIN numvol.

<!-- page 527 -->
C-3.a.4) To centre the volume relative to a cell of a lattice, add
M_ORIGIN ni nj nk LATTICE numlattice.
C-3.b) EQUA (Defines a volume using equations)
C-3.b.1) PLUS nbplus (with nbplus the number of surfaces with respect to which the volume is
considered positive, if nbplus=0 do not write this line and go to C-3.b.2) surf1...surfn
(list of the surfaces by number). Go to C-3.b.2.
C-3.b.2) MINUS nbmoins (with nbmoins the number of surfaces with respect to which the volume is
considered negative, if nbmoins=0 do not write this line and go to C-3.f) surf1...surfn
(list of the surfaces by number).
Go to C-3.f.
C-3.c) ROTATION (Defines a rotation)
VOLU numvolu ux uy uz θ Ωx Ωy Ωz.
Rotation of the volume of number numvolu of an angle θ around the axis described by the point
(Ωx,Ωy,Ωz) and the vector (ux,uy,uz).
Go to C-3.f.
C-3.d) If the cell is parallelepipedic, go to C-3.d.1, if hexagonal go to C-3.d.2.
C-3.d.1) RESC VOLU numvolu-ele nx ny nz. Repetition of the volume of number numvolu-ele
nx (ny and nz respectively) times along axis X (Y and Z, respectively).
C-3.d.2) RESH VOLU numvolu-ele n1 n3. Repetition of the volume n1 (n2=n1 and n3, respectively
) times along axis 1 (2 and 3, respectively).
Add MATCH if only complete cells are required.
C-3.d.3) Add EXCEPT nbcells ni(1) nj(1) nk(1) ni(2) nj(2) nk(2) ...
to delete certain
cells.
C-3.d.4) Add KEEP nbcells ni(1) nj(1) nk(1) ni(2) nj(2) nk(2) ... to only keep certain
cells.
C-3.e) In order to redescribe a cell, go to C-3.e.1, for a sub-cell (lattice of lattices), go to C-3.e.2
C-3.e.1) CELL ni nj nk LATTICE numlattice REPLACE numvol
C-3.e.2) LOWER_CELL DEPTH depth
LATTICE numlattice(the-smallest) VOLU numvol CELL ni nj nk
...
LATTICE numlattice(the-greatest) VOLU numvol CELL ni nj nk
C-3.f) Choice of an operator
C-3.f.1) If the volume being defined overrides the volumes already described (the non-zero intersection
case), continue; otherwise, go directly to C-3.f.2.
SMASH nbvolu (overrides nbvolu volumes)
volu1...volun (list of the volumes by number)
C-3.f.2) If the volume being defined is overridden by volumes that were previously defined (the nonzero
intersection case), continue; otherwise, go directly to C-3.f.3.

<!-- page 528 -->
VMINUS nbvolu (truncation of intersections with nbvolu volumes)
volu1...volun (list of the volumes by number)
C-3.f.3) If the volume being defined only retains its intersection with previously defined (virtual)
volumes, continue; otherwise, go directly to C-3.f.4.
INTE nbvolu (intersection with a set of nbvolu volumes)
volu1...volun (list of the volumes by number)
C-3.f.4) If the volume being defined is increased by the union with previously defined (virtual) volumes
, continue; otherwise, go directly to C-3.f.5
UNION nbvolu (union with a set of nbvolu volumes)
volu1...volun (list of the volumes by number)
C-3.f.5) If the volume is virtual, add
FICTIVE;
otherwise, go directly to C-3.f.6.
C-3.f.6) If the volume is to be excluded in a lattice add
VOL_EXCEPT;
otherwise, go directly to C-3.f.7.
C-3.f.7) End of volume definition
ENDV.
If another structure is defined, go to C (for another volume, directly to C-3); otherwise, go
to D.
D) In order to define the colors, continue; otherwise, go directly to E.
COLOR nb-colors
namecolor(1) nbvol(1) list-volumes(1)...
namecolor(n) nbvol(n) list-volumes(n)
E) GRAPH
Px Py Pz (origin of the 2D-cut)
Ux Uy Uz Vx Vy Vz (vectors defining the 2D-view)
LU LV (size of the window)
Flag (to generate a Postscript file, 1 (with captions) or 2 (without), 3 (with captions) or 4 (without) for
encapsulated PostScript, otherwise 0)
F) POSITION x y z (point position request)
G) ENDGEOM

<!-- page 529 -->
A) VOLSURF
B) To define surfaces, go to B-1); otherwise, go directly to B-2).
B-1) SURFACE nb(surfaces)
numvol1(1) numvol2(1) surface(1)...
numvol1(n) numvol2(n) surface(n)
(a surface is described by two volumes)
B-2) VOLUME nb(volumes)
numvol(1) volume(1)...
numvol(n) volume(n)
C) END_VOLSURF

<!-- page 530 -->
A) BOUNDARY_CONDITION
B) number_of_conditions
C) number_of_volume(i) then one of the following options:
C-1) REFLECTION surface(j) (Reflection on surface j of volume i)
C-2) TRANSLATION surface(j) (Translation from surface j of i)
C-3) COSINUS surface(j) (Emission of uniform cosine from surface j of i) Return to C for another
condition.
D) END_BOUNDARY_CONDITION

<!-- page 531 -->
A) COMPOSITION
B) number_of_compositions
C) A composition is entered in one of the following ways
C-1) ) POINT_WISE
Electronic properties, optional, only to overwrite Tripoli automatic choice in electron/positron
transport mode:
C-1.a ) NONPOLARIZABLE (non polarizable medium, insulator)
C-1.b ) CONDUCTOR (electric conductor medium)
C-1.c ) GASNTP (gaseous medium at normal temperature and pressure conditions, 1 atm-0°C)
temperature (pointwise cross-sections, ENDF format)
composition_name nb(isotopes)
isotope(1) nb_atoms(1)... (isotope(i) should be included in the library)
isotope(n) nb_atoms(n)
C-2) MULTIGROUP_HOMOGENEOUS temperature (APOLLO2 cross-sections)
composition_name APOLLO2 burnup
apollo2_cross-section_file_name
C-3) MULTIGROUP_HOMOGENEOUS temperature (TRIPOLI-4®cross-sections)
composition_name T4HOMOT4 0
TRIPOLI_cross-section_file_name
C-4) FILE
Electronic properties, optional, only to overwrite Tripoli automatic choice in electron/positron
transport mode
C-4.a ) NONPOLARIZABLE (non polarizable medium, insulator)
C-4.b ) CONDUCTOR (electric conductor medium)
C-4.c ) GASNTP (gaseous medium at normal temperature and pressure conditions, 1 atm-0°C)

<!-- page 532 -->
temperature
composition_name file_name
C-5) Return to C for another composition. If all compositions have been defined, go to D.
D) END_COMPOSITION

<!-- page 533 -->
A) GEOMCOMP
B) Define a combination for a composition:
composition_name (name of a composition as set in COMPOSITION)
volume_number_of_composition
volu1...
volun (list of the volumes by number)
Return to B for a new composition, go to C to end.
C) END_GEOMCOMP

<!-- page 534 -->
A) SOURCES_LIST in order to impose the total norm to go to B; otherwise, go to C.
B) NORM norm
C) nbsources Go to D once for each source.
D) SOURCE
D-1) NORM norm. Only in order to normalize the source; otherwise, pass.
D-2) COEFF coeff. Only in order to multiply the norm by coeff; otherwise, pass.
D-3) NEUTRON or PHOTON, depending on the type of particle.
D-4) Point source, go to D-4.a; otherwise, to D-4.b
D-4.a) POINT x y z Source at (x,y,z)
D-4.b) FACTORIZED FRAME Choose one of the following:
• CARTESIAN
• SPHERE
• CYLINDER
then enter
Ox Oy Oz
ix iy iz
(jx jy jz) for CARTESIAN only
kx ky kz
VOLUME nbvolumes volume1 ...
volumen
GEOMETRIC_DISTRIBUTION
In order to obtain a tabular source, go to C-4.b.2.1; for an analytical source go to C-4.b.2.2.
D-4.b.1.1) TABULATED
TYPE choose
F_U_V_W or F_U_VW or F_UVW
VAR_U then choose X or Y or Z
nb(u)
u[1] ...
u[nb(u)]
VAR_V then choose X or Y or Z
nb(v)
v1 ...
v[nb(v)]
VAR_W then choose X or Y or Z
nb(w)
w[1] ...
w[nb(w)]
Depending on the TYPE choice:
F_U value[1] ...
value[nb(u)-1]
F_V value[1] ...
value[nb(v)-1]
F_W value[1] ...
value[nb(w)-1]

<!-- page 535 -->
or
F_U value[1] ...
value[nb(u)-1]
F_VW value[1] ...
value{[nb(v)-1]*[nb(w)-1]}
or
F_UVW value[1] ...
value{[nb(u)-1]*[nb(v)-1]*[nb(w)-1]}
D-4.b.1.2) ANALYTICAL
FUNCTION=...;
DOMAIN=...;
D-5) ANGULAR_DISTRIBUTION Choose one of the following options:
D-5.a) MONO_DIR Ωx Ωy Ωz
D-5.b) ISOTROPIC
D-5.c) INTERPOLATED nbpoints nbinter
<MODE_INTERPOLATION>(1) numlim sup(1)
....
<MODE_INTERPOLATION>(nbinter) numlim sup(nbinter)
µ(0) value(0)
....
µ(nbpoints-1) value(nbpoints-1)
D-5.d) ANALYTICAL
FUNCTION=...;
DOMAIN=...;
D-6) ENERGETIC_DISTRIBUTION
SPECTRUM Choose one of the following options:
D-6.a) MONOKINETIC E0
D-6.b) BAND Esup Einf
D-6.c) WATT_SPECTRUM E0
PARAM Esup Einf a b (optional)
D-6.d) MAXWELL_SPECTRUM θ Esup Einf
D-6.e) INTERPOLATED nbpoints nbinter
<MODE_INTERPOLATION>(1) numlim sup(1)
....
<MODE_INTERPOLATION>(nbinter) numlim sup(nbinter)
E(0) value(0)
....
E(nbpoints-1) value(nbpoints-1)
D-6.f) ANALYTICAL
FUNCTION=...;
DOMAIN=...;
D-6.g) RAY_SPECTRUM nblines
E(0) I(0)

<!-- page 536 -->
...
E(nblines-1) I(nblines-1)
D-7) TIME_DISTRIBUTION Choose one of the following options:
D-7.a) DIRAC t0
D-7.b) UNIFORM tinf tsup
D-7.c) INTERPOLATED nbpoints nbinter
<MODE_INTERPOLATION>>(1) numlim sup(1)
....
<MODE_INTERPOLATION>>(nbinter) numlim sup(nbinter)
t(0) value(0)
....
t(nbpoints-1) value(nbpoints-1)
D-7.d) ANALYTICAL
FUNCTION=...;
DOMAIN=...;
D-8) EXTERNAL
D-8.a) source.so file name of the source function dynamically linked
D-8.b) NO_GEOMSOURCE_WARNING optional, if present, doesn’t stop calculation if sampling
efficiency too low (< 10%)
D-8.c) SOBOL_POINTS nbsampling optional, nb of sampling for testing the source function
(default=1000)
D-8.d) VOLUME nbvolumes volume1 ...
volumen optional
D-8.e) PARAM nbparam param1 ...
paramn
optional, numerical parameters transmitted to
source function
D-9) END_SOURCES
Go back to D until all the sources are defined, then go to E.
E) END_SOURCES_LIST

<!-- page 537 -->
A) RESPONSES
B) nbresponses
C) Choose one of the following options and return to C to define another response. Go to D to end.
C-1) FLUX particle_type (NEUTRON or PHOTON)
C-2) CURRENT particle_type (NEUTRON or PHOTON or ELECTRON or POSITRON)
C-3) REACTION particle_type (NEUTRON or PHOTON)
C-4) DEPOSITED_ENERGY particle_type (NEUTRON or PHOTON or ELECTRON or POSITRON)
C-5) DEPOSITED_SPECTRUM particle_type (PHOTON or PHOTON ELECTRON POSITRON)
C-6) DEPOSITED_SPECTRUM_WEIGHTED_ENERGY
particle_type
(PHOTON
or
PHOTON
ELECTRON POSITRON) If there is a single nucleus, go to C-3.a, if there are many go to C-3.b.
C-3.a) NUCLEUS, go to C-3.c
C-3.b) NUCLEI nbnuclei, go to C-3.c
C-3.c) name_of_nucleus
• If the nucleus belongs to a composition, go to C-3.d
• If the nucleus does not belong to a composition, but is in the library, go to C-3.e
• If the nucleus is to be described, go to C-3.f
In the NUCLEI case, C-3.c is done once for each nucleus.
C-3.d) COMPOSITION composition_name
INTERACTION nbinteractions
interaction1 ...interactionn
C-3.e) FICTIVE temperature (integer)
INTERACTION nbinteractions
interaction1 ...interactionn
C-3.f) (COEFF coeff) DATA
nbpoints nbinter (number of points, interpolation intervals)
<MODE_INTERPOLATION>(1) upper_limit(1)
....
<MODE_INTERPOLATION>(nbinter) upper_limit(nbinter)
Energy(0) cross-section(0)
....
Energy(nbpoints-1) cross-section(nbpoints-)1
D) END_RESPONSES

<!-- page 538 -->
A) GRID_LIST
B) nbgrids
C) name_of_grid
nbbounds
bounds1 ...
boundsi IN_LIN p boundsi+p+1 ...
boundsj IN_LOG q boundsj+q+1 ...
boundsn (list of bounds)
Return to C for a new grid; otherwise, go to D to end.
D) END_GRID_LIST

<!-- page 539 -->
A) SCORE
B) nbscores
C) Define a score
associated_response_number
Choose one of the following options (track length estimator: TRACK, collision estimator: COLLISION,
surface-based estimator: SURF or point estimator: FLUX_PT) and return to C to describe another score.
Go to D to end.
C-1) TRACK associated_energy_grid_name If a time grid is required (angular) go to C-1.a (C-1.b); otherwise
, go directly to B-1.b.
C-1.a) TIME GRID associated_time_grid_name
Go to C-1.b.
C-1.b) ANGULAR GRID associated_angle_grid_name
Go to C-1.c.
C-1.c) GRID associated_energy_grid_name
Go to C-1.c.2 by default, or C-1.c.1 if specific properties are required.
B-1.c.1) COMPLETE or BOOTSTRAP
COMPLETE enables all results to be preserved (by default the average value is preserved),
and BOOTSTRAP enables calculation of the confidence interval. Go to C-1.c.2.
C-1.c.2) For a list of volumes (C-1.c.2.1), for a sum of volumes (C-1.c.2.2), for a list of cells (C-
1.c.2.3), for a sum of cells (C-1.c.2.4).
C-1.c.2.1) VOLUME LIST nbvolu
volume1...volumen
C-1.c.2.2) VOLUME SUM nbvolu
volume1...volumen
C-1.c.2.1) CELL LIST nbcells
numvol1 numlattice1 cell1(i) cell1(j) cell1(k)...
numvoln numlatticen celln(i) celln(j) celln(k)
C-1.c.2.2) CELL SUM nbcells
numvol1 numlattice1 cell1(i) cell1(j) cell1(k)...
numvoln numlatticen celln(i) celln(j) celln(k)
C-2) COLLISION associated_energy_grid_name
If a time (and/or angle) grid is required, go to C-2.a; otherwise, go directly to C-2.b.
C-2.a) TIME GRID associated_time_grid_name
and/or ANGULAR GRID associated_angle_grid_name
Go to C-2.b.
C-2.b) GRID associated_energy_grid_name
For a list of volumes (C-2.b.1), for a sum of volumes (C-2.b.2), for a list of cells (C-2.c.3), for
a sum of cells (C-2.c.4)

<!-- page 540 -->
C-2.b.1) VOLUME LIST nbvolumes
volume1...volumen
C-2.b.2) VOLUME SUM nbvolu
volume1...volumen
C-2.c.3) CELL LIST nbcells
numvol1 numlattice1 cell1(i) cell1(j) cell1(k)...
numvoln numlatticen celln(i) celln(j) celln(k)
C-2.c.4) CELL SUM nbcells
numvol1 numlattice1 cell1(i) cell1(j) cell1(k)...
numvoln numlatticen celln(i) celln(j) celln(k)
C-3) SURF associated_energy_grid_name
If time (and/or angle) grid is required, go to B-3.a; otherwise, go directly to B-3.b.
C-3.a) TIME
GRID
associated_time_grid_name
and/or
ANGULAR
GRID
associated_angle_grid_name
Go to B-3.b.
C-3.b) GRID associated_energy_grid_name
For a list go to C-3.b.1, for a sum C-3.b.2 (surface i is defined as the boundary between
volumei1 and volumei2 where volumei2=-1 for an escape surface)
C-3.b.1) FRONTIER LIST nbsurfaces
volume11 volume12
...
volumen1 volumen2
C-3.b.2) FRONTIER SUM nbsurfaces
volume11 volume12
...
volumen1 volumen2
(surface i is defined as the boundary between volumei1 and volumei2 where volumei2=-1
for an escape surface)
C-4) FLUX_PT associated_energy_grid_name
If a time (and/or angle) grid is required, go to B-4.a; otherwise, go directly to B-4.b.
C-4.a) TIME GRID associated_time_grid_name
and/or ANGULAR GRID associated_angle_grid_name
Go to C-4.b.
C-4.b) GRID associated_energy_grid_name
POINT LIST nbpoints
x1 y1 z1
...
xn yn zn
D) END_SCORE

<!-- page 541 -->
A) VARIANCE_REDUCTION (to be performed twice for a combined neutron-gamma problem)
B) NEUTRON or PHOTON
C) GRID nbbounds
energy1 ...
energyn
D) For a point detector, go to D-1, for a surface-based detector, go to D-2.
D-1) DETECT nbdetectors
D1x D1y D1z (coordinates of detector)
β1 (associated coefficient)
...
Dnx Dny Dnz
βn
If mesh, go to E.
D-2) DETECT_RHO 1 ρ(D) βD
E) MESH
E-1) Nx’ Ny’ Nz’(number of cells)
dx’ dy’ dz’(sizes of cells)
3
E-2) FRAME (associated with mesh)
E-2.a)
CARTESIAN
O’x O’y O’z
ix iy iz
jx jy jz
kx ky kz
E-2.b)
CYLINDER
O’x O’y O’z
ix iy iz
kx ky kz
In order to refine the mesh by 8 in a zone, go to E-3; otherwise, go to E-4.
E-3) DIVISION WINDOW
X’min Y’min Z’min
X’max Y’max Z’max (description of window)
E-4) END_MESH
F) INIPOND
For automatic biasing, go to F-1, for manual biasing, go to F-2.

<!-- page 542 -->
F-1) AUTO, go to F-3.
F-2) DATA nomcompo(1)
k(1) ...
k(nbgroups)
...
nomcompo(n)
k(1) ...
k(nbgroups)
F-3) OMEGA
Case of surface-based detector biasing. If the direction is calculated by gradient, go to F-3.1; if the
direction is set by the user, go to F-3.2.
F-3.1) GRAD_I
F-3.2) SET_OMEGA
CYLINDER
ux uy uz
cx cy cz
Go to F-4.
F-4) END_INIPOND
G) Optional case of energy biasing in exp(−α(i)E):
ALFA α(1). ..α(n).
There is one value for each energy group.
H) Optional case of time biasing in exp(−λt):
TIME λ
I) GRAPH
Ox Oy Oz (origin of the 2D-view in geometry reference frame)
Lgraf(1) Lgraf(2) (size of window)
X or Y or Z (direction normal to the 2D-view in mesh reference frame)
J) END_VARIANCE_REDUCTION

<!-- page 543 -->
A) HOMOGENIZE
B) NBMAT nbcompo
B-1) nomcompo
VOLUME LIST nbvolu
volu1 ...
volun
name(grid)
Continue to B-1 until all the compositions have been defined.
B-2) FILE name(cross-sections_file)
C) DIFFUSION 1
D) END_HOMOGENIZE

<!-- page 544 -->
A) SIMULATION
B) Mandatory data
BATCH nbbatches
SIZE number_of_particles_per_batch
PARTICLE number_of_types_of_particles
If there are neutrons, go to B-1; otherwise, go directly to B-2.
B-1) NEUTRON
If there are photons go to B-2; otherwise, go directly to C.
B-2) PHOTON
If there are also electrons and positrons go to B-3; otherwise, go directly to C.
B-3) ELECTRON POSITRON
C) Optional data
ENERGY_INF NEUTRON Einf(neutron)
ENERGY_SUP NEUTRON Esup(neutron)
ENERGY_INF PHOTON Einf(photon)
ENERGY_SUP PHOTON Esup(photon)
ENERGY_INF ELECTRON Einf(electron)
ENERGY_INF POSITRON Einf(positron)
ENERGY_SUP ELECTRON Esup(electron)
ENERGY_SUP POSITRON Esup(positron)
EDITION frequency
For a criticality problem, go to C-1; for a fixed source sub-criticality problem, go to C-2. For a shielding
problem, leave blank, go to D.
C-1) ) CRITICALITY
If it is wished to delete batches
DISCARD number_of_batches_to_be_discarded
C-2) FIXED_SOURCES_CRITICALITY
D) Other optional data
TRACK_INTEGRATION 1 in order to use the track integration option
MONITORING 0 in order to eliminate monitoring
COLLISION 1 Einf(coll) in order to bias collision above Einf(coll)
KEEP_RESULT in order to keep the results to continue the calculation
RANDOM in order to give an initial random number
XML_EXPORT in order to write results in xml file
XML_NOCOMPLETE in order to reduce xml output to EDITION

<!-- page 545 -->
D) Optional data concerning electromagnetic shower
ELECTRON_INELASTIC_CUTOFF energy
ELECTRON_BREMS_CUTOFF energy
NO_ELECTRON_MULTIPLE_SCATTERING
ELECTRON_TOTAL_STOPPING_POWER
F) END_SIMULATION

<!-- page 546 -->
A) CALCULATION If a volume calculation is required, go to B; otherwise, go to C.
B) Calculation of volumes
(SET) VOLUME (SETis used to initialize the volumes for the value calculated)
FRAME
Choice of coordinated system (U,V,W) associated with origin O’ and vectors i, j and k.
B-1) CARTESIAN
O’x O’y O’z
ix iy iz
jx jy jz
kx ky kz
B-2) CYLINDER
O’x O’y O’z
ix iy iz
kx ky kz
B-3) SPHERE
O’x O’y O’z
ix iy iz
kx ky kz
WINDOW
Umin, Vmin, Wmin
Umax, Vmax, Wmax
PRECISION precision
END_VOLUME
If a density calculation is required go to C; otherwise, go to D.
C) Calculation of densities
DENSITY
If the densities of all the compositions are required go to C-1; otherwise, go to C-2.
C-1) ALL Go to C-3.
C-2) LIST nbcompo name_composition1...name_compositionn Go to C-3.
C-3) ) END_DENSITY
D) END_CALCULATION

<!-- page 547 -->
A) PEPIN
B) GRID name(grid)
In order to rebuild the materials with the natural composition, go to E.
C) ISOTOPES (to not rebuild the materials)
D) SCORE_MODE mode (with mode equating to TRACK or COLLISION)
E) HISTORY nb(steps)
time(init) <UNIT>
time(1) <UNIT> value(1)
...
time(final) <UNIT> value(final)
F) VOLUME nbvolu
volu1...volun
G) END_PEPIN

<!-- page 548 -->
A) STORAGE
B) nb(instances_of_storage)
C) name(file)
NEUTRON or PHOTON
Emax Emin
FRONTIER volu1 volu2
Do C once for each request, then go to D.
D) END_STORAGE

<!-- page 549 -->
A) PERTURBATION_LIST
B) nb(perturbations)
C) PERTURBATION
Go to C-1) for a concentration perturbation, go to C-2 for a density perturbation (only one factor must
be given in C-3).
C-1) CONCENTRATION. Go to C-3.
C-2) DENSITY. Go to C-3.
C-3) nb(compositions)
VOLUME LIST nb(volu) volu(1)...volu(N)
FACT fact(1)...fact(N)
SCORE LIST nb(scores) numscore(1)...numscore(n)
Go to C-5 for a differential mode; otherwise, go directly to C-6.
C-4) DETERMINISTIC
NUCLEI nb(nuclei)
C-4.a) number of composition of nucleus1
name of composition
VOLUME LIST nb_volu
numvol1 ...
numvoln
NUCLEUS nucleus name DATA filename
Do C-4.a once for every disturbed nucleus
C-5) MODE DELTA. Go to C-6.
C-6) END_PERTURBATION
Do C once for every perturbation request, then go to D.
F) END_PERTURBATION_LIST

<!-- page 550 -->
A) OUTPUT
B) LANGUAGE (optional, English by default).
C) For XVGR outputs go to C-1).
C-1) XVGR
ENERGY_INF Einf
ENERGY_SUP Esup
TYPE interpolation_type (where interpolation_type equates to LIN_LIN, LIN_LOG,
LOG_LIN, LOG_LOG).
END_XVGR
F) END_OUTPUT

<!-- page 551 -->
A) VOLENERCUT
B) type_of_particle
C) ALL default_energy_cut set a default energy threshold for all volumes (optional)
D) numvol_i energy_cut_i set energy_cut_i to numvol_i.
Do D for each volume requested.
Go to B for every particle requested.
F) END_VOLENERCUT
