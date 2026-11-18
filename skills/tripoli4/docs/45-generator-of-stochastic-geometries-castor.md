# GENERATOR OF STOCHASTIC GEOMETRIES (CASTOR)
<!-- source PDF pages 495-511 -->

<!-- page 495 -->
Chapter 45
GENERATOR OF STOCHASTIC
GEOMETRIES (CASTOR)
CASTOR (Construction and Analysis of STOchastic Realizations) is a code written in C++ and developed
at CEA. The executable can be found at the following path: CODE/<OpSys>/tools/Castor/bin/castor,
where <OpSys> denotes the operating system.

## 45.1 INTRODUCTION

CASTOR is devoted to the Monte Carlo sampling of three types of stochastic geometries [49]:
1. three-dimensional isotropic and homogeneous Poisson tessellations (n-ary mixtures);
2. three-dimensional Poisson-Box tessellations (n-ary mixtures);
3. three-dimensional spherical inclusions (non-overlapping spheres with low packing-fraction) in a background
matrix (binary mixtures).
The spheres of the spherical inclusions can be either mono-dispersed (constant radius) or poly-dispersed
(radius sampled according to a probability law).
Currently, the sampled random geometry can be exported to three differents types of outputs:
1. ASCII files corresponding to different blocks to be inserted into a datafile for the Monte Carlo transport
code TRIPOLI-4. The code can generate between two and three blocks and one connectivity map
(according to the options chosen by the user):
• GEOMETRY block: describes the whole geometry with a combinatorial or surface-based description
(see also Chapter 7);
• GEOMCOMP block: associates the compositions (identified by a label/color) and volumes (see also
Chapter 11);
• BOUNDARY_CONDITION block (optional): describes the boundary conditions applied to the geometry
(see also Chapter 9);

<!-- page 496 -->
• a connectivity map (optional): contains the list of neighbors for each volume and is included in the
GEOMETRY block (see also Subsection 7.14.1).
A full dataset for TRIPOLI-4 can be then completed by the user via the keyword FILE (see Subsection
6.2).
2. An ASCII file corresponding to an input file for the TRIPOLI-4 visualizer T4G (see Chapter 38), in order
to visualize the geometry directly.
3. A file with VtK format to visualize the geometry in three dimensions with a software such as ParaView.
The export to VtK of one given geometry is based on the tetrahedral decomposition of polyhedra composing
the tessellation or on the discretization of spheres.
For very large geometries, we recommend to add the following options to the command line calling the
TRIPOLI-4 executable (in order to speed-up the initialization of the geometry):
-a -T notest -T decresponse -T decresponse
As a verification of generated geometries, the code can also compute ensemble-averaged stastical properties
over the geometries, namely the stereological properties (chord length moments and distributions). The code
computes the average chord lengths:
• across the volumes composing the geometry (average uncolored chord length CL)
• across compositions of label i (average colored chord length CLi)
for a given number of test lines sampled with µ-randomness property and exports corresponding histograms
on pre-defined grids.

## 45.2 CONSTRUCTION OF RANDOM GEOMETRIES

### 45.2.1 TYPE OF GEOMETRIES (MANDATORY)

The type of stochastic geometries is the single mandatory argument. It should be provided by this command:
./castor --poisson3d
for Poisson tessellations,
./castor --poissonbox3d
for Poisson-Box tessellations,
./castor --inclusions3d
for spherical inclusions.

<!-- page 497 -->
### 45.2.2 NUMBER OF REALIZATIONS

The number of geometries to generate is given by the option -N or --number. This number is set to 5 by
default.
Example:
./castor --poisson3d -N 1000
to generate 1000 realizations.

### 45.2.3 CONTAINER

The shape of the container containing the geometry is given by the option -C or --container. The container
is always centered at the origin (0,0,0). Several types of containers can be used:
• a parallepipedic box by using:
./castor --poisson3d -C box,10.,25.,6.
for a box of side Lx = 10, Ly = 25 and Lz = 6;
• a cube by using:
./castor --poisson3d -C box,20.
for a cube of side L = 20;
• a sphere by using:
./castor --poisson3d -C sphere,20.
for a sphere of radius R = 20;
• a cylinder parallel to x-axis by using:
./castor --poisson3d -C xcylinder,5.,20.
for a cylinder of radius R = 5 and of length Lx = 20;
• a cylinder parallel to y-axis by using:
./castor --poisson3d -C ycylinder,5.,20.
for a cylinder of radius R = 5 and of length Ly = 20;
• a cylinder parallel to z-axis by using:
./castor --poisson3d -C zcylinder,5.,20.
for a cylinder of radius R = 5 and of length Lz = 20;
By default, the container is a squared box of side 10.

<!-- page 498 -->
Figure 45.1: Different containers for spherical inclusions: cube, parallelepipedic box, x-cylinder, sphere.

<!-- page 499 -->
### 45.2.4 COLORING PROBABILITIES (VOLUME RATIOS)

For Poisson and Poisson-Box tessellations, a step of coloring is performed after the decomposition of the
domain with random hyperplanes: each volume of the tessellation is assigned a label i with a probability pi
(1 ≤i ≤n), to obtain a n-ary mixture (n being a arbitray integer). In an infinite domain, this probability pi
would correspond to the volume ratio for composition i.
For spherical inclusions, no random coloring process is used, since we consider the binary mixture matrix/-
spheres: in this case, the geometry is decomposed into a background matrix (filled with composition 0) and
a set of non-overlapping spheres (filled with composition 1). The target volume ratio (corresponding to p1)
for spheres is also denoted by the packing fraction.
In both cases, the user can provide the target volume ratios for each composition by using the option -P or
--probabilities.
Examples:
• tessellation (binary mixture):
./castor --poissonbox3d -P 0.7,0.3
where the label 0 is assigned with probability p0 = 7 and the label 1 assigned with probability p1 = 0.3;
• tessellation (ternary mixture):
./castor --poisson3d -P 0.4,0.5,0.1
where the label 0 is assigned with probability p0 = 0.4, the label 1 assigned with probability p1 = 0.5
and the label 2 assigned with probability p2 = 0.1;
• spherical inclusions (by construction, binary mixture):
./castor --inclusions3d -P 0.9,0.1
for a target packing fraction equal to 0.1.
By default, the geometry is a binary mixture with p0 = 0.8 and p1 = 0.2.
Please note that the maximal packing fraction in CASTOR is 0.37 because of the underlying algorithm (Random
Sequential Addition).

<!-- page 500 -->
45.2.5
GEOMETRICAL SPECIFICATIONS (TESSELLATION DENSITY OR RADIUS DISTRI-
BUTION)

#### 45.2.5.1 Poisson and Poisson-Box geometries

For Poisson and Poisson-Box tessellations, the geometries are generated for a given (positive) free parameter
corresponding to the tessellation density, denoted ρ (see illustration in Figure 45.2). In infinite geometries,
the average chord length is equal to:
• 1
ρ in Poisson tessellations;
• 2
3ρ in Poisson-Box tessellations.
The user can provide this parameter using -R or --rho.
Figure 45.2: Example of realization of a Poisson tessellation in a cube of side L = 10, with coloring probabilities p0 = 0.8 (red)
and p1 = 0.2 (blue), with a tessellation density ρ = 5.0 (left) and ρ = 10.0 (right).
Examples:
• The tessellation density ρ is set to 5 (theoretical chord length equal to 0.2).
./castor --poisson3d -R 5.
• The tessellation density ρ is set to 2 (theoretical chord length equal to 0.333333).
./castor --poissonbox3d -R 2.
The default density is equal to 2.

<!-- page 501 -->
#### 45.2.5.2 Spherical inclusions

For spherical inclusions, the geometries are generated for a given radius distribution. The user can provide
this parameter using -D or --distribution. So far, three types of distributions are available:
• radius following a constant distribution by using:
./castor --inclusions3d -D constant,0.1
for a radius r = 0.1;
• radius following a uniform distribution by using:
./castor --inclusions3d -D uniform,0.05,0.3
for a uniform distribution between rmin = 0.05 and rmax = 0.3;
• radius following an exponential distribution by using:
./castor --inclusions3d -D exponential,0.2
for exponential distribution with mean r = 0.2.
Figure 45.3: Example of realization of spherical inclusions in a cube of side L = 10, with a packing fraction ξ = 0.2, with a constant
distribution r = 0.2 (left) and a uniform distribution between rmin = 0.1 and rmax = 0.6 (right).
The default distribution is a constant distribution with radius r = 0.5.

### 45.2.6 CONSTRUCTION ALGORITHM

For Poisson tessellations, several algorithms can be used to build the geometry. The naive algorithm being
time-consuming, other algorithms have been proposed to speed-up the construction. The following options
(that exclude each other) can be chosen:

<!-- page 502 -->
• naive algorithm (algorithm A) by using:
./castor --poisson3d --naive
• algorithm B (ascending hierrachy), by using:
./castor --poisson3d --opt
• Edelbrunner’s algorithm (algorithm C) by using:
./castor --poisson3d --edelsbrunner
• mesh-based algorithm D by using:
./castor --poisson3d --meshing -M 10,20,30
for a mesh 10×20×30.
• hybrid algorithm E (hydrid algorithm between algorithms B and D) by using:
./castor --poisson3d --hybrid -M 10,20,30
for a mesh 10×20×30.
By default, the algorithm B is used.
Geometries produced by these different algorithms are assumed to be identical for uncolored geometrical
properties. Nevertheless, please note that the indexation of volumes can be different since volumes can be
created in a different order as a function of the algorithm. Thus, coloring properties can differ from one
algorithm to another.
The construction of spherical inclusions (based on a Random Sequential Addition algorithm) can be accelerated
by a mesh-based method (bounding box). Therefore, the user can provide a mesh as follows:
./castor --inclusions3d -M 10,15,20
for a mesh 10×15×20. By default, the mesh-based algorithm is not applied.
There is no option concerning the algorithm for Poisson-Box tessellations.

## 45.3 EXPORT INPUT FILES FOR TRIPOLI-4 AND T4G

### 45.3.1 ACTIVATION AND TARGET REPOSITORY

The option -T or --tripoli4 activates the generation of inputs files for TRIPOLI-4.
The option -t or --tpath specifies a repository where outputs will be exported.
Example:

<!-- page 503 -->
./castor --inclusions3d -T -t repo_t4
By default, output files will be exported into the current directory.
For the block GEOMETRY, each output file is called geometry_i (where i corresponds to the index of the
realization).
For the block GEOMCOMP, each output file is called geomcomposition_i.
For the block
BOUNDARY_CONDITION, each output file is called limit_i. The output file for the connectivity map is called
map_i.

### 45.3.2 START RANK AND END RANK

The start rank and end rank for the production of TRIPOLI-4 output files can be chosen by the user with
options --tstartrank and --tendrank.
Example: TRIPOLI-4 input files are produced between the 21st and the 30th realization:
./castor --inclusions3d -N 100 -T -t repo_t4 --tstartrank 21 --tendrank 30
By default, all generated geometries are exported to TRIPOLI-4 files if -T is activated, i.e. the start rank is
equal to 1 and the end rank is equal to N, where N is the number of generated geometries.

### 45.3.3 NAME OF MIXTURE COMPOSITIONS

The specification of the name of each composition (such as they appear within the block GEOMCOMP) is done
by using the option -c or --compositions.
The list provided with this option must have the same size as the list provided with the option -P (volume
ratios).
Examples:
• Composition with 35% FUEL, 55% WATER and 10% CLADDING:
./castor --poisson3d -T -P 0.35,0.55,0.1 -c FUEL,WATER,CLADDING
• Composition with 10% FUEL and 90% WATER:
./castor --inclusions3d -T -P 0.1,0.9 -c FUEL,WATER
The list is set to WATER,FUEL by default, i.e. the composition 0 is named WATER and the composition 1 is
named FUEL.

### 45.3.4 TRANSLATION

As explained in Subsection 45.2.3, the geometries are always centered at the origin. However, it is possible
to apply a translation to the center for the export to TRIPOLI-4. In order to move the center to the position

<!-- page 504 -->
(Px,Py,Pz), the user can use the commande -p or --translation.
Example: geometry centered at (0.5,−4.5,32.3) within the block GEOMETRY:
./castor --poisson3d -T -p 0.5,-4.5,32.3
By default, no translation is applied to the center of the geometry.

### 45.3.5 BOUNDARY CONDITIONS

The user can add boundary conditions (see also Chapter 9) all around the container by two possible options :
• the option -r for reflections everywhere;
• the option -b for a flexible set of boundary conditions.
Please note that:
1. the options -b and -r exclude each other;
2. if none of these options is used, no file is produced for the block BOUNDARY_CONDITION.
First, the option -r or --reflection adds reflective boundaries conditions to the whole container.
Examples:
./castor --poisson3d -C sphere,10. -T -r
./castor --poisson3d -C box,10. -T -r
Then, the option -b or --boundaries enables to apply specific boundary conditions on each boundary, with
TRIPOLI-4 keywords (consistent with the language selected as an option for TRIPOLI-4).
For a sphere, a list of one single boundary conditions has to be provided.
Examples:
• apply leakage on the sphere:
./castor --poisson3d -C sphere,10. -T -b LEAKAGE
• apply reflection on the sphere:
./castor --poisson3d -C sphere,10. -T -b REFLECTION
For a cylinder, a list of 3 boundary conditions has to be provided (lower surface, upper surface, lateral surface).
Examples:
• apply leakage on x = xmin, leakage on x = xmax and reflection on the lateral surface:
./castor --poisson3d -C xcylinder,20.,5. -T -b LEAKAGE,LEAKAGE,REFLECTION

<!-- page 505 -->
• apply leakage on y = ymin, reflection on y = ymax and leakage on the lateral surface:
./castor --poisson3d -C ycylinder,20.,5. -T -b LEAKAGE,REFLECTION,LEAKAGE
• apply reflection on z = zmin, reflection on z = zmax and leakage on the lateral surface:
./castor --poisson3d -C zcylinder,20.,5. -T -b REFLECTION,REFLECTION,LEAKAGE
For a box, a list of 6 boundary conditions has to provided (xmin, xmax, ymin, ymax, zmin, zmax).
Examples:
• apply reflection on x = xmin, leakage on x = xmax, leakage on y = ymin, reflection on y = ymax, leakage
on z = zmin, leakage on z = zmax :
./castor --poisson3d -C box,10. -T
-b REFLECTION,LEAKAGE,LEAKAGE,REFLECTION,LEAKAGE,LEAKAGE
• apply leakage on x = xmin, leakage on x = xmax, leakage on y = ymin, reflection on y = ymax, leakage on
z = zmin, leakage on z = zmax :
./castor --poisson3d -C box,10. -T
-b LEAKAGE,LEAKAGE,LEAKAGE,REFLECTION,LEAKAGE,LEAKAGE

### 45.3.6 LANGUAGE

The outputs exported for TRIPOLI-4 contain specific keywords that should be consistent with the language
selected as an option for TRIPOLI-4. This is why it can be necessary to use the option -l or --language.
Three languages are possible: english, french or old.
Examples:
./castor --poisson3d -T -l english
./castor --poisson3d -T -l french
./castor --poisson3d -T -l old
By default, the language is set to old.

### 45.3.7 EXPORT FOR THE VISUALIZER T4G

The export of input files (concatenation of GEOMETRY and GEOMCOMP blocks) for the visualizer T4G is
optional. The user can activate the production of such files with the option -g or --t4g.
Example:
./castor --poisson3d -T -g
Each output file is called t4g_i (where i corresponds to the index of the realization).

<!-- page 506 -->
### 45.3.8 CONNECTIVITY MAP

A connectivity map is produced by default. The user can deactivate the connectivity map in the GEOMETRY
block with the option ‘-n‘ or ‘–no-map‘.
Example:
./castor --poisson3d -T -n

### 45.3.9 MESH (SPHERICAL INCLUSIONS ONLY)

Finally, for the specific case of spherical inclusions, the option -m or --mesh-t4 enables to:
• reset a new mesh for the export to TRIPOLI-4 or T4G if a previous mesh has already been used for the
construction;
• add a mesh for the export to TRIPOLI-4 or T4G if no mesh has been used for the construction (see
Figure 45.4).
The option -d or --no-mesh-t4 enables to remove the mesh that has been used for the construction
(for the export to TRIPOLI-4/T4G). If none of these two options (-m or -d) is added, the input files for
TRIPOLI-4/T4G are obtained with the mesh used during the construction.
Examples:
• a mesh 20 ×20 ×20 is used to speed-up the construction and a mesh 50 ×50 ×50 is used to speed-up
the transport in TRIPOLI-4:
./castor --poisson3d -T -M 20,20,20 -m 50,50,50
• no mesh is used to speed-up the construction and a mesh 50×50×50 is used to speed-up the transport
in TRIPOLI-4:
./castor --poisson3d -T -m 50,50,50
• a mesh 20 × 20 × 20 is used to speed-up the construction and no mesh is used for the transport in
TRIPOLI-4:
./castor --poisson3d -T -M 20,20,20 --no-mesh-t4
• a single mesh 20×20×20 is used to speed-up both the construction and the transport in TRIPOLI-4:
./castor --poisson3d -T -M 20,20,20

<!-- page 507 -->
Figure 45.4: Examples of mesh in the visualizer T4G for spherical inclusions: 4 ×4 ×4 (left) and 10 ×10 ×10 (right), for a box
container (top) or a spherical container (bottom).

<!-- page 508 -->
## 45.4 EXPORT INPUT FILES FOR VTK

### 45.4.1 ACTIVATION AND TARGET REPOSITORY

The option -V or --vtk activates the generation of inputs files for VtK.
The option -v or --vpath specifies a repository where outputs will be exported.
Example:
./castor --inclusions3d -V -v repo_vtk
By default, output files will be exported into the current directory.
Each output file is named paraview_i.vtk where i corresponds to the index of the realization.
It is important to note that:
• for spherical inclusions, only spheres are visible on the visualization, but not the container itself;
• for Poisson or Poisson-Box tessellations, the spherical/cylindrical container is applied a posteriori by
adding a wrapping surface (only for the export for TRIPOLI-4). Indeed, the (vertex-based) construction
of the geometry is based on the smallest bounding box containing the spherical/cylindricalcontainer.
Since the representation of the geometry in VtK is also vertex-based, the export for VtK enables to show
the full geometry within the parallelepedic box and not within the container used for TRIPOLI-4.

### 45.4.2 START RANK AND END RANK

The start rank and end rank of generation of these output files can be chosen by the user with options
--vstartrank and --vendrank (or -i).
Examples:
• VtK files are produced between the 21st and the 30th realization:
./castor --inclusions3d -N 100 -V -v repo_vtk --vstartrank 21 --vendrank 30
• Only 5 first VtK files will be produced:
./castor --inclusions3d -N 100 -V -v repo_vtk -i 5
Please note that VtK files can be quite heavy, given the geometrical parameters, whence the possibility to
export only a selection of geometries into VtK format. By default, all the generated geometries are exported
to VtK files if -V is activated.

### 45.4.3 VISUALIZATION OPTION

By default, the geometry is visualized with a given color for each composition. However, the user can
choose to visualize "uncolored" geometries with the option -u or --randomize-color (see illustration in

<!-- page 509 -->
Figure 45.5). That requires to randomize the labels for the visualization, in order to remove correlations
between labels and indices of volumes.
Example:
./castor --poisson3d -N 100 -V -v repo_vtk -u
Warning: this option leads to an offset of the random seed of the generator.
Figure 45.5: Visualization with ParaView without (left) and with (right) option -u activated.

### 45.4.4 RESOLUTION OF THE SPHERES (SPHERICAL INCLUSIONS ONLY)

Finally, a specific option -k or --resolution can be used for spherical inclusions only. This option enables
to choose the number of discretized angles for the decomposition of any spherical inclusion (the minimal
value being 4).

<!-- page 510 -->
Example:
./castor --inclusions3d -V -v repo_vtk -k 20
By default, this option is equal to 10.
Nevertheless, if the exported file is too heavy (which depends directly on the number of spheres), it could be
necessary to reduce this parameter of resolution. Conversely, it could be useful to increase the resolution in
order to improve the visualization (see Figure 45.6.
Figure 45.6: Visualization with ParaView with -r 10 (left) and with -r 40 (right).

## 45.5 STATISTICAL PROPERTIES

### 45.5.1 ACTIVATION AND TARGET REPOSITORY

The option -S or --statistics activates the calculation of statistical properties related to generated
geometries (i.e. chord length first-order moments and distributions).
The option -s or --spath specifies a repository where outputs will be exported.
Example:
./castor --inclusions3d -S -s repo_stats
By default, output files will be exported into the current directory.
This option does not work for spherical/cylindrical containers.
At the end of the calculation, the following ensemble-averaged quantities are displayed (in the console):

<!-- page 511 -->
• the average chord length through volumes and the associated standard deviation;
• the average chord length through each composition i and the associated standard deviation.
The corresponding histograms are exported to the target repository. They are named as follows:
• histogram_chord_length.txt for the uncolored chord length;
• histogram_chord_length_color_i.txt for the chord length through composition i.

### 45.5.2 NUMBER OF TEST LINES

The number of test lines used to compute the chord length per realization can be chosen with the option -j
or --nb-lines.
Example for 100 test lines:
./castor --poissonbox3d -S -j 100
The number of test lines is equal to 1 by default.

### 45.5.3 OPTIONS FOR PRE-DEFINED GRIDS

The user can define grids used to tally the chord length distribution, with the options --minima, --maxima
and --nb-bins. For a n-ary mixture, the user has to provide a list of size n+1 for each of these options.
In the following example:
./castor --poissonbox3d -S --minima 0.,1.,4.5 --maxima 40.,80.,100.
--nb-bins 1500,500,200
• the grid used for the scoring of the uncolored chord length distribution ranges from 0 to 40 with 1500
bins;
• the grid used for the scoring of the colored chord length distribution through composition 0 ranges from
1 to 80 with 500 bins;
• the grid used for the scoring of colored chord length distribution through composition 1 ranges from 4.5
to 100 with 200 bins.
By default, all grids range from 0 to Lmax with 1000 bins, where Lmax corresponds to the maximal chord
length in the container.
