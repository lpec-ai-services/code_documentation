# DISPLAY OF COLLISIONS SITES
<!-- source PDF pages 338-343 -->

<!-- page 338 -->
Chapter 25
DISPLAY OF COLLISIONS SITES
This feature allows for the display of the locations where collisions occur during a simulation. For example,
the aim can be to display the efficiency of a chosen variance reduction technique. The simulation is carried
out on a relatively few number of particles and the display carried out on 2D-views of the geometry. Thus
we have to keep in mind that this feature only gives the user an indication of the collision site locations to be
used for checks or adjustments (to the chosen variance reduction technique for example). Several options can
help the user to analyze the current simulated case.

## 25.1 SYNTAX

The general syntax used to define collisions sites is as follows:

<!-- page 339 -->
COLLISION_SITES
<PARTICLE_TYPE>
height
DISCARD nb(batches)
#
SCORE
#
SCORE_SEGMENTS
#
SOURCE
#
NB_COLLISION nb(collisions)
GRID
nb(bounds)
energy(1).. .energy(nb(bounds))
COLOR
nb(colors)
<COLOR(1)> nb(groups_1)
group(1)...group(nb(groups_n))
...
<COLOR(nb(colors))> nb(groups_n)
group(1)...group(nb(groups_n))
*
GRAPH
Px Py Pz
Lu Lv
<AXIS>
Flag
FILE filename
*
GRAPH_CONTOURS
Px Py Pz
Lu Lv
<AXIS>
Flag
FILE filename
END_COLLISION_SITES

### 25.1.1 TYPES OF PARTICLES

Presently, <PARTICLE_TYPE> can be NEUTRON or PHOTON.
In order to obtain plots of collisions sites, for either neutrons or photons, the data block COLLISION_SITES
... END_COLLISION_SITES must first be written for neutrons and a second block for photons. During the
execution, a message specifies which particle is related to each plot.

<!-- page 340 -->
### 25.1.2 VARIATION OF THE PARAMETER HEIGHT

This parameter refers to the maximal distance to the view plane (defined by GRAPH or GRAPH_CONTOURS)
on which the point (collision site) will be projected. This value is specified by the user. For geometries of
about one meter, a choice between 1 and 10 for this parameter gives satisfactory results. Of course, the larger
height is, the more points there will be on the graphic. So, we have to find a compromise between visual
quality and the representation of reality. However, the user may want to deliberately project a full part of a
geometry on this 2D-view plane...
25.1.3
DISPLAY FOR “FULL” 2D-VIEWS OR CONTOUR-2D-VIEWS OF THE GEOMETRY
• The keyword GRAPH indicates that a “full” 2D-view is requested (it is the same type of 2D-view that we
can obtain for the drawing of equi-importance, for example). The volumes are colored.
• the keyword GRAPH_CONTOURS indicates that we are asking for a 2D-view with only the geometry contours
. On the screen, we see white contours on a black background, in Postscript files we see black
contours on a white background. On the screen, the contours are plotted point by point through two
scannings (one vertically and one horizontally).
• Superimposed on these 2D-view are the points showing the collisions sites.
Restrictions:
• One of the two keywords GRAPH or GRAPH_CONTOURS must be present.
• Several 2D-views may be requested using several GRAPH or GRAPH_CONTOURS commands. However,
in a COLLISION_SITES command, the 2D-view type must be the same (we cannot mix GRAPH and
GRAPH_CONTOURS).
The data in the GRAPH or GRAPH_CONTOURS blocks are of the same type as the data used for the drawing of
equi-importance maps:
• Px Py Pz indicates the coordinates (in the geometric frame) of the point in the bottom left part of the
display window ;
• Lu and Lv indicate this window dimensions ;
• <AXIS> is X for a yPz window, Y for a xPz window, and Z for a xPy window;
• Several graphs may be requested. Flag is 0 if a Postscript file is not required. In this case, a window
is displayed and if the user a posteriori decides to dump the associated Postscript file, he can do it with
the Shift-P command in the graphical window. Otherwise Flag is 1 and there is no display window but
the associated Postscript file is dumped.
• The option FILE allows for the user to specify the associated file name. By default, PostScript files
are named "collisions_sites_N.ps", otherwise they are named "filename_N.ps" where N is the
number of the graph. They are numbered in the order in which the graphs are requested.

<!-- page 341 -->
The following keywords (DISCARD, SCORE, SCORE_SEGMENTS, SOURCE, NB_COLLISION, GRID and COLOR) are
optional. They allow for additional conditions on the projected points and additional display options useful
for more detailed analyses.

### 25.1.4 OPTION DISCARD

The optional keyword DISCARD enables to avoid the display of the collision sites of the nb(batches) first
batches. This can be useful :
• in SHIELDING mode : setting nb(batches) to 5 enables to discard the 5 first batches during which adjustments
of importance maps are performed by the code (simulation with an importance map non fixed
group to group),
• in CRITICALITY mode : nb(batches) can be set to the number of batches needed for the convergence of
the source.
Using the option DISCARD enables to simulate more particles (since the collision sites of the first batches are
not stored), cf. sub-section 25.3. This option is compatible with options SOURCE, SCORE and SCORE_SEGMENTS
detailed in the following sub-sections.

### 25.1.5 OPTIONS SCORE AND SCORE_SEGMENTS

The SCORE and SCORE_SEGMENTS options enable to display the whole particle history (birth site, collision
sites and boundary condition sites) only for particles eventually contributing to the scores.
• The SCORE option displays only points (projections of the collision sites) and is compatible with COLOR
and DISCARD options. When this option is used simultaneously with the SOURCE option (see sub-section
25.1.6), only source sites of contributing trajectories are displayed. When it is used simultaneously with
the NB_COLLISION option and "0" as nb(collisions) (see sub-section 25.1.7), displayed points are source
sites of contributing trajectories and production sites of secondary particles which eventually contribute
to the scores.
• The SCORE_SEGMENTS option also displays segments between the different sites. It can be used with
the DISCARD option and must be used with the GRAPH_CONTOURS keyword (see sub-section 25.1.3).
When using the SCORE_SEGMENTS option, the COLOR option is not allowed. The user must keep in mind
that among displayed trajectories, if all points are not projected on the 2D-view window (regardless its
dimensions and the height parameter), some of the displayed segments may then not be real trajectory
parts of the simulation because two non-consecutive sites may be joined.

### 25.1.6 OPTION SOURCE

This option enables the display of source sites instead of collision sites. It is also compatible with DISCARD
and COLOR options. When this option is used simultaneously with the SCORE option, only source sites of
contributing trajectories are displayed. Other options of this chapter are incompatible. The SOURCE option
is also available simultaneously with the EXPLOITATION mode of Green’s function files (see chapter 35) and
can thus help to analyze the contents of Green’s function files.

<!-- page 342 -->
### 25.1.7 OPTION NB_COLLISION

This option enables the display of sites of the nb(collision)-th collisions only. The score estimator (see chapter
15) must be TRACK, SURF or COLL. When this option is used with "0" as nb(collision) and simultaneously
with the SCORE option, displayed points are source sites of contributing trajectories and production sites of
secondary particles which eventually contribute to the scores. Other options of this chapter are incompatible.

### 25.1.8 OPTIONAL DEFINITIONS FOR AN ENERGY GRID AND RELATED COLORS

The keywords GRID and COLOR are optional; however, COLOR is defined only if GRID is defined.

#### 25.1.8.1 Definition of an energy grid, keyword GRID :

The definition of a grid in the COLLISION_SITES command is made in exactly the same way as in the
GRID_LIST and VARIANCE_REDUCTION commands. Remember that the list of energies has to be monotonic
decreasing and that the number of bounds is the number of groups plus one.
The grid may or may not be same as that of the biasing grid. The advantage in defining the grid here is that it
can exist even if no variance reduction technique is defined.
Some further indications regarding the aspect and the number of graphics :
• if GRID is not defined, we only have a graphic for all the energies of the simulation;
• if GRID is defined but COLOR isn’t defined, we have a graphic for each group of the grid;
• if GRID and COLOR are defined, we have only one graphic and the colors of the points are defined by the
user for each group.

#### 25.1.8.2 Color definition, keyword COLOR :

The number of colors defined here, nb(colors), has to be lower or equal to the total number of groups in the
grid (nb(bounds)-1). If it is strictly lower, it means that the user has used the same color for several groups.
The choice of the colors is the same as for the optional definition of the colors of volumes for the geometry.
The possible values for <COLOR(i)> are as follows: BLACK, BLUE, BROWN, CORAL, CYAN, GOLD, GRAY, GREY,
GREEN, MAGENTA, NAVY, ORANGE, PINK, PLUM, RED, SALMON, VIOLET, WHITE, YELLOW.
Each color name (nb(colors) altogether) is followed by the number of groups to be displayed using this color
and their list. The number of the groups is taken between 1 and nb(bounds)-1. These numbers match the
order of user’s input into the GRID command.
• When COLOR is defined, all the groups must have a color (whether or not it is shared by other groups).
• If COLOR is not defined, collisions sites will be dark points for GRAPH and red points for
GRAPH_CONTOURS.

<!-- page 343 -->
## 25.2 ORDER OF APPARITION FOR THE DISPLAY WINDOWS

The display windows appear on the screen at the end of the simulation and in the following order:
• exterior loop : for each particle type corresponding to a COLLISION_SITES command;
• intermediary loop : for each 2D-view type defined by the GRAPH (or GRAPH_CONTOURS) command;
• interior loop : for each group of the associated GRID (if defined and if COLOR is not).

## 25.3 NUMBER OF PARTICLES IN THE SIMULATION

By default, when the COLLISION_SITES command is used, the maximum allowed number of particles for the
simulation is 1000 in the SIMULATION command of the data files.
The data fields BATCH (number of simulated batches) and SIZE (number of particles for each batch) must
verify :
BATCH ⋆SIZE ≤1000
We will use, for example, a maximum of 10 batches with 100 particles.
When the option DISCARD is used, the maximal number of simulated batches can then be increased by the
number nb(batches) discarded within this graphical command block : we will use, for example, a maximum
of 10 + nb(batches) batches with 100 particles.
The simulation is performed with a small number of particles in order to obtain a reasonable number of
points to store for the display. However, if the user wants to obtain collisions sites for more particles, the
following keyword is added to the SIMULATION command:
MAXP_FOR_COLLISION_SITES m
The threshold will then be m instead of 1000 particles (consequently, the user will have to manage his free
memory space).

## 25.4 NUMBER OF PROJECTED POINTS

The number of projected points on the display window appears in the execution window when each graphic
is drawn. It should be compared, for example, to the collision number indicated in the result file of the
simulation (before the printout of the scores).
