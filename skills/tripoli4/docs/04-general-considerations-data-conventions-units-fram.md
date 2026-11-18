# GENERAL CONSIDERATIONS : DATA, CONVENTIONS, UNITS, FRAMES
<!-- source PDF pages 32-42 -->

<!-- page 32 -->
Chapter 4
GENERAL CONSIDERATIONS : DATA,
CONVENTIONS, UNITS, FRAMES
In this chapter, we give the conventions for writing the data file and describe its general structure. This file consists of a number of
modular commands, each indicating an instruction.
First of all, it must be pointed out that the input data is in free format: the number of white spaces after the first is not meaningful.
It is therefore possible to indent the data file in order to make it more legible. In addition, empty lines can be inserted anywhere.
The keywords must be entered in UPPERCASE.

## 4.1 THE DEFAULT UNITS

The units in the data file are as follows:
• Length: centimeters;
• Time: seconds;
• Temperature: Kelvin (note: the temperature read from an APOLLO2 file for multigroup cross-sections is in degrees Celsius);
• Energy: MeV (important: data on ENDF tapes are expressed in eV);
• Angles: degrees for the definition of the cone surface and shape, and of rotation volumes, radians for the definition of
sources and frames;
• The cross-sections entered by the user (DATA option) are in barns (10−24 cm2);
• The number of atoms in the compositions are given in 10−24 cm3;
• The calculated densities are in g/cm3;
• The unit for particle sources is the number of particles (this value is integrated in volume, directions, energy, and time).

<!-- page 33 -->
## 4.2 UNIT CHANGES

It is possible to change some units (length and energy). Care is required when changing the unit of length, as the cross-sections
remain in barns, the number of atoms for 10−24 cm3, and the densities in g/cm3. Beware that it also affects the display of results.
For example, the fluxes are by default in length units so a change of length unit will have a direct change on fluxes.
Changes are made as follows:
UNITS
LENGTH
x <UNIT>
ENERGY
y <UNIT>
END_UNITS
where
• x is a decimal value;
• <UNIT>: is the name of the unit. For length, the choices are {mm, cm, dm, m, dam, hm, km}, and for energy the choices
are {eV, keV, MeV, GeV}. Names of units in uppercase only can be used.
Thus, 2.54 cm means that the unit of length is 1 inch.

## 4.3 CONVENTIONS USED IN THIS MANUAL

The basic syntax of a command (or sets of commands) is given in a bold framebox.
The basic syntax of a sub-command is shown in a double frame.
The basic syntax of a lower level command is shown is in a single frame.
Examples are given on the next page.

<!-- page 34 -->
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
TYPE
num(type)
<SHAPE>
Descriptive data
BOX hx hy hz

<!-- page 35 -->
## 4.4 CHARACTER STYLE CONVENTIONS

This convention applies to frameboxes used in describing a syntax. In ordinary text, entries of code are given in typewriter-style
characters (font: Courier).
Letters are:
• In bold and
– in UPPERCASE for keywords. e.g.,
GEOMETRY
Exception: apart from the keywords X, Y, Z, E, and T, used for specifying sources or the GRAPH sub-command of
VARIANCE_REDUCTION, a single letter in uppercase corresponds to the coordinate of a point (to be replaced by its
value).
– in UPPERCASE and between < >: to be replaced by a keyword.
E.g. <SHAPE> is to be replaced by BOX , SPHERE , CYLX ...
– in lowercase: an item of data, e.g.
numXXX to be replaced by number of XXX
nbXXX to be replaced by number of XXX
• Non-bold for definitions related to data whose structure is given elsewhere in the manual, e.g.
<SHAPE> Definition
After the keyword has been selected from the available range, the characteristics of the shape must be entered. The syntax is
given, below (for instance, in the frame defining BOX).
• In italics for non-mandatory lines.
If an asterisk is placed to the left of the line, it means that the line itself is not mandatory but a choice must be made between it and
the other asterisked lines included in the data set.
If several sets of choice are placed on consecutive lines, the asterisks are subscripted by an integer in order to indicate the extent of
each set.
E.g.
* TYPE numtype
* SURF numsurf
it is possible to define a geometry without calling TYPE or without calling SURF, but one of the two must be called.
If there is a hash mark at the beginning of the line, it means that the line is not mandatory and is also incompatible with the other
lines beginning with a «#». e.g.
# CRITICALITY
# FIXED_SOURCES_CRITICALITY
it is not possible to carry out a calculation designated as both a criticality calculation and a sub-criticality calculation with sources.

<!-- page 36 -->
## 4.5 DEFINING FRAMES

The frame definition is introduced using the keyword FRAME followed by :
• a frame type.
• an origin O′;
• three vectors defining an orthonormal frame: i, j, k; The j axis is only specified in the case of Cartesian coordinates
All these data are given in the cartesian reference frame (X,Y,Z), see figures 4.1, 4.2 and 4.3.
The syntax is as follows :
FRAME
<FRAME_TYPE>
O’x O’y O’z
ix iy iz
(jx jy jz) if cartesian
kx ky kz
The frame type can be Cartesian: a vector O’M is defined by its coordinates (x,y,z), projections of O’M along axes i, j, k (see
Figure 4.1) :
O′M = xi+yj+zk.
It can also be cylindrical, in which case the vector O’M is defined by its coordinates (r,θ,z) where r is the normal of the projection
O’M on the plane (i, j), θ is the angle between the projection (between 0 and 2π) and the vector i, and z is the projection of O’M
along axis k (see Figure 4.2) :
O′M = rcosθi+rsinθj+zk.
Finally, the frame type can be spherical, in which case the vector O’M is defined by its coordinates (r,φ,θ) where r is the normal
of O’M, φ is the angle (between 0 and 2π) between the projection of O’M on the plane (i, j) and the vector i, and θ is the angle
between OM and the axis (i, k) (between 0 and π) (see Figure 4.3) :
O′M = rcosφsinθi+rsinφsinθj+rcosθk.
Note: when a non-unit vector is entered to specify the reference frame, TRIPOLI-4® automatically renormalizes it to 1.

<!-- page 37 -->
X
Y
Z
k
j
i
O
O’
x
y
z
Figure 4.1: Cartesian coordinates
X
Y
Z
k
j
i
O
O’
z
θ
Figure 4.2: Cylindrical coordinates

<!-- page 38 -->
X
Y
Z
k
j
i
O
O’
φ
θ
r
Figure 4.3: Spherical coordinates

<!-- page 39 -->
## 4.6 LIST LAYOUT

A list of items or a list of sets of items is written as follows:
item(1) ... item(n)
or
set_of_items(1)
...
set_of_items(n)
or
set_of_items
...

## 4.7 LIST OF CALCULATION COMMANDS

A definition of the TRIPOLI-4 data file is now given.
TRIPOLI4 calculation input data consist of the following commands:
• geometry definition.
GEOMETRY ... ENDGEOM
This section defines the geometrical items used in the calculation.
• values of areas and volumes
VOLSURF ... END_VOLSURF
This section provides volume and area values.
• boundary condition definition.
BOUNDARY_CONDITION ... END_BOUNDARY_CONDITION
This section defines calculation boundary conditions.
• medium and composition definition
COMPOSITION ... END_COMPOSITION
This section sets calculation media isotopic compositions.
• association of volumes and compositions
GEOMCOMP ... END_GEOMCOMP
This section is used to associate each geometry volume with the isotopes composing it. The geometry and compositions
must be defined beforehand.
• source definition
SOURCES_LIST ... END_SOURCES_LIST
This phase defines the emission densities of the source particles used in the calculation.
• response definition
RESPONSES ... END_RESPONSES
The responses are physical quantities calculated by the code (flux, current, reaction rates etc.).
• grid definition
GRID_LIST ... END_GRID_LIST
Grids correspond to time, angle, or energy intervals in the simulation domain for which the responses are calculated. They
include homogenization grid.

<!-- page 40 -->
• score definition
SCORE ... END_SCORE
A score corresponds to a combination including an estimator, grids, and geometrical units determining the calculation of a
response function. The geometry, composition, division, and response definitions must be completed beforehand.
• perturbation definition
PERTURBATION_LIST ... END_PERTURBATION_LIST
• biasing definition
VARIANCE_REDUCTION ... END_VARIANCE_REDUCTION
Biasing relates to the use of variance reduction techniques in the simulation. The geometry and composition definitions must
have been completed beforehand.
• simulation definition
SIMULATION ... END_SIMULATION
This section deals with the simulation itself. It sets the simulation parameters.
• announcing the use of collision tapes
COLLISION_TAPE ... END_COLLISION_TAPE
This command enables dumping to a listing file events undergone by particles or, conversely, re-using such a file to obtain
new scores.
• announcing the use of Green’s function files
GREEN_FUNCTION_TAPE ... END_GREEN_FUNCTION_TAPE
This command enables storing source information and tallying information for particles contributing to the score, and then
allows the re-use of this information. Possible uses and applications include parametric studies with source modification, or
calculations of scores from different source regions.
• announcing homogenization
HOMOGENIZE ... END_HOMOGENIZE
This section sets the compositions to be homogenized and the corresponding volumes.
• verification calculation definition
CALCULATION ... END_CALCULATION
This section sets the volume and density of the compositions to be calculated.
• special output definition
OUTPUT ... END_OUTPUT
This section sets special outputs (XVGR graphs).
• particles to be stored
STORAGE ... END_STORAGE
This section specifies the contingent storage of particle data in files, for subsequent processing (SN code etc.).
• assigning data for subsequent depletion calculations
PEPIN ... END_PEPIN
This section can be used to create files for DARWIN-PEPIN2.
• ROOT coupling
ROOT_GEOMETRY ... END_ROOT_GEOM
ROOT_LIMIT ... END_ROOT_LIMIT
TRACKS ... END_TRACKS
These sections can be used to define a ROOT geometry and ROOT boundary conditions, and to record particle tracks for
ROOT post-processing.

<!-- page 41 -->
The following definitions are mandatory:
• geometry;
• compositions;
• associations of volumes and compositions;
• sources;
• simulation criteria.
For a radiation shielding calculation, scores must be demanded by specifying the following items:
• grids (energy, space, angle, and time discretizations);
• responses;
• scores.
The following settings are optional:
• boundary conditions (leakage is the default);
• biasing;
• homogenization request (requiring an energy grid);
• perturbations;
• collision bands;
• verification calculations;
• DARWIN-PEPIN2 and ROOT couplings.
The dependences between definitions are symbolized by arrows in the following (simplified) diagram (an arrow from A to B means
that A must be set before B).
The following pages show how a file is composed (options in dotted lines).

<!-- page 42 -->
COMPOSITION
GEOMETRY
GEOMCOMP
VOLSURF
CALCULATION
GRID_LIST
RESPONSES
SCORE
PERTURBATION_LIST
PEPIN
ROOT
Couplings
SOURCES_LIST
BOUNDARY_CONDITION
Physical data
HOMOGENIZE
VARIANCE_REDUCTION
Results data
Simulation data
SIMULATION
Validation
CALCULATION
Figure 4.4: Commands
