# DEFINING GRIDS
<!-- source PDF pages 212-214 -->

<!-- page 212 -->
Chapter 14
DEFINING GRIDS
Grids are defined between the keywords GRID_LIST and END_GRID_LIST.
Grids need to be specified for tallying and homogenization. A grid is a set of energy, angle, or time intervals,
a response function is calculated for each of those intervals. A grid can also be used for ranges of number of
fission neutrons.
A list of grids is defined using:
• the number of grids
• the data for each grid
A grid is defined using:
• the name of the grid
• the number of bounds for the grid
• the values of the bounds
For a pre-defined grid, the number of bounds and their values need not be indicated. The grids are referred to
by their names: 3_GRS (3 groups), SAILOR (47 groups), APOLLO_94_GAMMA (94 groups from 5 keV to
20 MeV, for gamma transport), APOLLO_99 (99 groups), GAM2 (100 groups), APOLLO_172 (172 groups),
APOLLO_281 (281 groups, SHEM) and TRIPOLI_315 (315 groups). The TRIPOLI-4® code adds a group
above the highest energy of the grid up to 104 MeV and a group below the lowest energy of the grid down to
10−11 MeV (if necessary) (in order to overlap the simulation domain in every case).
All of the intervals comprising an energy grid must cover the simulation domain of the problem
([Einf,Esup] by default 10−11 MeV - 20 MeV for neutron). Otherwise, the TRIPOLI-4® code fails. For
known grids, the additional high-energy and low energy groups guarantee that the upper and lower boundary
of the simulation domain are within the grid.
The grids are defined for any type of particle (NEUTRON, PHOTON, ELECTRON and POSITRON).

<!-- page 213 -->
Linear or log spacing grids can be defined automatically using the keywords IN_LIN or IN_LOG. For example
v1 IN_LIN n v2 defines n values linearly interpolated between v1 and v2, the total number of values is then
n+2.
The sequences v1 IN_LIN n v2 and v1 IN_LOG n v2 can be inserted everywhere in grid, the total bound
number must take into account all the interpolated values.
The grids for energy, angle, time and number of fission neutrons are defined in the same way. A keyword is
not necessary to define the type of grid.
Important: there is one more bound than the number of intervals. A grid can be input with increasing or
decreasing values, but the list must be monotonic (always increasing or always decreasing).
The grid definition syntax is, therefore, as follows:
GRID_LIST
nb(grids)
name(grid1)
nb(bounds)
bound(1)...bound(n)
...
name(known_gridi)
...
name(gridj)
nb(bounds)
bound(j1) ...
bound(jk) IN_LIN mk bound(jk+mk+1) ...
bound(jl) IN_LOG ml bound(jl+ml+1) ...
bound(jn)
...
name(gridn)
nb(bounds)
bound(1)...bound(n)
END_GRID_LIST
Defining grids for the criticality calculation of chapter 5
GRID_LIST 6
GRID_FLUX 10
20.
5.
1.
0.1 0.01
1.E-3 1.E-4 1.E-5 1.E-6 1.E-11
GRID_ABSORPTION 6
20.
4.086771E-2 9.119000E-3
1.433817E-3 1.101044E-4 1.E-11
GRID_TIME 5

<!-- page 214 -->
1.
0.1 0.01 1.E-5 1.E-7
GRID_ANGLE 5
-1.
0.5 0.
0.5 1.
GAM2
GRID_NU 11
0.
0.9999 1.9999 2.9999 3.9999
4.9999 5.9999 6.9999 7.9999 8.9999 9.9999
GRID_INTERPOL 15
1.E-11 1.E-10 IN_LOG 4 1.
1.5 2.
IN_LIN 5 20.
END_GRID_LIST
The third grid in the above example is a time grid. It is, of course, not subject to the energy simulation
domain constraints.
Angle grids such as the grid GRID_ANGLE are given in terms of cosines and must cover the domain [-1, 1].
Cosine is the angle between particle’s vector ω and the normal vector of the surface crossed by the particle.
The normal vector is the one used to build the surface. It means that it could be the opposite direction of the
out going normal direction of the volume that surface belongs.
Grids such as GRID_NU are used for ranges of number of fission neutrons and are not subject to the
energy simulation domain constraints since they should encompass the zero value (they are used with the
WHOLE_GRID keyword instead of the standard GRID keyword for energy grid, see section 15.7).
The last grid GRID_INTERPOL is equivalent to :
GRID_INTERPOL 15
1.E-11 1.E-10 1.E-8 1.E-6 1.E-4 1.E-2 1.
1.5 2.
5.
8.
11.
14.
17.
20.
Important:
• The time (or angle) specification grid is optional.
• Angular grid can only be used with surface-based estimators (see section 15.2).
• When a grid for the number of fission neutrons is used, it replaces the use of the energy grid (see Section
15.7), with the difference that it can encompass the zero value.
