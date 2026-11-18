# ACTIVATION CALCULATION
<!-- source PDF pages 469-478 -->

<!-- page 469 -->
Chapter 41
ACTIVATION CALCULATION
The goal of activation calculations is typically to compute the dose delivered by photons due to the decay of
matter that underwent neutron activation. TRIPOLI-4 implements the Rigorous 2-Step scheme (R2S), which
consists of the following steps:
Step 1: neutrons are transported throughout the geometry. During this step, neutron fluxes and reaction rates
are scored. The fluxes and reaction rates feed the source term of a system of Bateman equations for
the concentrations of all the possible activation products. The Bateman equations are solved and the
activities are determined at all the requested times. The neutron flux is allowed to vary in intensity over
the activation time range, but it is assumed that the shape of the flux does not change (so that only one
neutron transport calculation is necessary).
Step 2: For each activation time, the code computes the photon spectra emitted by the activation products.
These spectra are used as the source of a photon-transport calculation.
Contrary to depletion calculations (see Chapter 40), the neutron flux, the reaction rates are not homogenized
over the volumes of the TRIPOLI-4 geometry. The user is expected to define a mesh over the region of interest
for activation and to specify the materials whose activation needs to be considered. Each mesh cell is then
separately activated and represents a distinct radiation source for the second calculation step.

## 41.1 INPUT FOR AN ACTIVATION CALCULATION

An input deck for a depletion calculation is structured as follows :
• a TRIPOLI-4 static input file with some modifications explained below;
• an input file to specify the irradiation history, in the format specified in Section 40.1.4.

### 41.1.1 TRIPOLI-4 INPUT FILE

The format of the TRIPOLI-4 input file for the first calculation step is very similar to the format required for
depletion calculations. Compared to a static TRIPOLI-4 input file, a few modifications are necessary.
First, the RESPONSES and SCORE blocks have to be replaced by FILE commands pointing to specific files:

<!-- page 470 -->
FILE
directorypath/result/reponses.jdd
FILE
directorypath/result/scores.jdd
• result is the output directory. It is specified by the RESULT_DIRECTORY keyword in the DEPLETION
block. By default it is called “result";
• The files reponses.jdd and scores.jdd contain respectively the RESPONSES and SCORE block. These files
are automatically generated in the output directory from the list of depleted compositions, the depletion
chain and reaction rates calculation options. No custom scores can be added to these files.
Second, the GRID_LIST block must contain at least three grids. The first one must be a one-group grid over the
whole calculation energy range. The second one must be a two-group grid over the whole calculation energy
range. Finally, the third grid must be the group structure associated with the multi-group cross sections
provided in the GENDF files (specified by the GENDF keyword; see Chapter 40). The EAF-2010 GENDF
file provided in the TRIPOLI-4 installation is associated with the 175-group VITAMIN-J structure. The
GRID_LIST definition is provided in the TRIPOLI-4 installation, as well as in Figure 41.1.
Note that, contrary to depletion calculations, nothing special needs to be done about the composition files,
because feedback from the compositions on neutron transport is assumed to be negligible.
Like in depletion calculations, the user needs to define a DEPLETION block. However, the syntax is slightly
different, as shown below.

<!-- page 471 -->
DEPLETION
MENDEL_LIBRARY librarypath
ACTIVATION
EXTENDED_MESH
Specification of the mesh for the activation calculation
PARALLEL <n_threads>
#
EDITION <n_editions>
DEPLETION_DIRECTORY directorypath
IRRADIATION_HISTORY TIME ihfilename
Specification of the file describing irradiation history
RENORMALIZATION
FIXED_SOURCE
END_RENORMALIZATION
DEPLETED_COMPOSITIONS
List of depleted compositions
#
HOMOGENIZE
#
SOBOL_POINTS <n_points>
#
RANDOM_POINTS <n_points>
CHAIN
Depletion chain / depleted compositions association
POINTWISE_REACTION_RATES
Selection of nuclides whose reaction rates are computed directly by TRIPOLI-4
GENDF
GENDF cross-sections / depleted compositions association
ESTIMATOR <TYPE>
Estimator to be used for computing flux and reaction rates (track length or collision
estimators)
RESULTS
Files and directory results specifications
END_RESULTS
END_DEPLETION
Here:

<!-- page 472 -->
• librarypath is the path to the Mendel library file (MendelLibrary_V0.1.BBL), which is installed
along with TRIPOLI-4;
• n_cores is the number of CPU cores to use to parallelize the solution of the Bateman equations. Parallelization
is handled by OpenMP;
• directorypath is the calculation directory; due to current limitations, this directory must be the current
directory (. or the absolute path to the current directory);
• ihfilename is the name of the file containing irradiation history (see 40.1.4). The full path name is
therefore directorypath/ihfilename;
• The unit for the irradiation history must be TIME, in days (contrast this with Section 40.1.4);
• The only allowed keyword for RENORMALIZATION is FIXED_SOURCE (see Section 40.1).
The extended mesh must be specified according to the format of Section 15.8. It may contain the optional
NORMALIZE keyword, but none of the other ones (TRIANGLEZ, ENTROPY...). If NORMALIZE is given, then
the score given in the standard TRIPOLI-4 output is the integral of the neutron flux over the activation mesh
cells. Independently of the presence of the NORMALIZE keyword, the reaction rates for the activation step are
correctly calculated using the neutron flux. Finally, the user must make sure that the mesh properly covers all
the materials that need to be activated.
For the PARALLEL keyword, see the explanations in Section 41.2.3 below. For the syntax of the remaining
options, see Chapter 40.

### 41.1.2 HOMOGENIZED CELLS

The list of activated materials is provided by the user with the keyword DEPLETED_COMPOSITIONS. The user
can control the mapping between mesh cells and compositions with the HOMOGENIZE keyword. Two strategies
are available:
• If the HOMOGENIZE keyword is specified, each mesh cell is assumed to be homogeneously filled with the
material found at the centre1 of the cell. The user must either ensure that cells are really homogeneous,
or check that the error introduce by this assumption is negligible for their purpose.
• If the HOMOGENIZE keyword is not specified, TRIPOLI-4 treats the mesh cells as heterogeneous, but
in order to do so it needs to draw a number of quasi-random or pseudo-random points in each cell
to estimate the fraction of volume occupied by each composition. By default, TRIPOLI-4 uses 104
points per cell. If further precision is required, the user may increase the number of points, at the
expense of a larger initialization time, using the optional SOBOL_POINTS (for quasi-random sampling)
or RANDOM_POINTS (for pseudo-random sampling) keywords.
The two homogenization options have different requirements in terms of mesh coarseness. If the mesh cells
are homogenized, a fine mesh is required to accurately follow the concentration gradients of activation products
over the geometry. Heterogeneous cells are less sensitive to the mesh fineness. On the other hand, the
1Note that the centre of spherical and cylindrical mesh cells is not defined as their centre of mass (which may lie outside the cell if the latter is not convex), but
as the point corresponding to the midpoint of the range of spherical/cylindrical coordinates for the cell.

<!-- page 473 -->
memory footprint for homogeneous cells is proportional to the number of mesh cells, while the footprint for
heterogeneous cells is proportional to the number of mesh cells times the number of activated compositions,
regardless of the number of compositions actually present in a single cell. Therefore, there is a trade-off
associated with this option.

## 41.2 CALCULATION STEPS

As outlined above, the R2S calculation proceeds in two steps.

### 41.2.1 STEP 1: ACTIVATION

The first step includes the neutron-transport calculation and the solution of the Bateman equations for the
concentrations of the activation products. The first calculation step produces several results, which are stored
in the directory specified by the RESULT_DIRECTORY keyword:
• the ROOT output file aggregating all the simulation results (see Section 41.2.4 below)
• the files reponses.jdd and scores.jdd respectively contain the RESPONSES and SCORE blocks. They are
automatically built from the depletion chain, the list of depleted compositions and the calculation options
for the reaction rates.
• the output of the transport calculation (t4output file).

### 41.2.2 STEP 2: PHOTON TRANSPORT

The second calculation step samples photons according to the activities calculated in the first step and stored
in the ROOT output file. These photons are used as the source of a photon transport calculation for which
users are free to define their scores (fluxes, doses, etc.).
The TRIPOLI-4 input file for the second step is a normal input file, except for the definition of the source.
The SOURCE block needs to be defined as follows:

<!-- page 474 -->
SOURCES_LIST
SOURCE
PHOTON
ACTIVATION
<root_file>
TIME_STEP <n_time_step>
FILTER_BY_ISOTOPE
Specification for the filtered isotopes
ENERGY_THRESHOLD <e_threshold> // in MeV
ACTIVITY_THRESHOLD <a_threshold> // in Bq/cm3
END_ACTIVATION
END_SOURCE
END_SOURCES_LIST
Here:
• root_file is the name of the ROOT file produced by the first calculation step;
• n_time_step is the index of the time step for the photon transport calculation. The photon source
will be taken from the activities of the material compositions calculated at the given time step number.
Note that the index is zero-based, but n_time_step=0 refers to the initial compositions, before neutron
activation. Therefore, useful values of n_time_step range from 1 to the number of time steps in the
irradiation file (Section 40.1.4);
• The (optional) FILTER_BY_ISOTOPE keyword can be used to limit the activation products that will be
sampled. This may be useful, for instance, to ascertain the contribution of a particular isotope to the
sought photon response. By default, all isotopes are accounted for (see below however for energy and
activity cuts). Specifying FILTER_BY_ISOTOPE, followed by the number of isotopes, followed by the
list of desired isotopes, will limit photon sampling to de-excitation photons of the isotopes included in
the list.
• The (optional) keywords ENERGY_THRESHOLD and ACTIVITY_THRESHOLD may be used to cut deexcitation
photons emitted below a given energy or activity threshold, respectively. By default, the
energy threshold is 1 keV and the activity threshold is 0 Bq/cm3, meaning that photons with energy
below 1 keV will not be transported. Note: this means that their energy is neglected. It is not locally
deposited.
If
part
of
the
source
activity
is
cut
by
the
FILTER_BY_ISOTOPE,
ENERGY_THRESHOLD
and
ACTIVITY_THRESHOLD keywords, TRIPOLI-4 will automatically renormalize the source intensity to account
for the missing activity. The output log will summarize the source normalization and the effect of the
cuts with a message like the following:

<!-- page 475 -->
integrated intensity = 5.630501e+11 Bq
(this value will be used as the source normalisation)
energy threshold = 1.000000e+00 keV
activity threshold = 0.000000e+00 Bq/cmˆ3
neglected intensity (below energy and activity thresholds) = 2.916902e+09 Bq
ratio neglected/total = 5.153837e-01%

### 41.2.3 PARALLELIZATION OF THE ACTIVATION CALCULATION

Both steps of the R2S scheme may be run in parallel, using TRIPOLI-4’s traditional parallelization techniques
(Chapter 33).
Additionally, TRIPOLI-4 offers the possibility to parallelize the solution of the Bateman equations using
OpenMP. The number of OpenMP threads can be controlled using the PARALLEL option. TRIPOLI-4 splits
the activation calculation over the threads, assigning a certain number of activated cells to each OpenMP
thread. When the activation calculations for a cell is completed, it is stored in a temporary memory buffer,
waiting to be written to disk. Periodically (every 500 activated mesh cells by default), all the computed
activation results are written to the ROOT output file; the buffer is cleared and a new batch of cell activation
calculations starts.
Since I/O cannot be performed in parallel, the OpenMP threads must synchronize when the ROOT file is
written. If the frequency of these rendez-vous points is too high, I/O will introduce some significant overhead
and the efficiency of the parallel calculation will degrade. If the frequency is too low, the temporary buffer
will need to be very large to accommodate all the calculated activation results, and the memory footprint
might become unmanageable. The default interval (500 cells) is a good all-round compromise, but the user
has the possibility to adjust the interval with the EDITION keyword.

### 41.2.4 CONTENT OF THE ROOT OUTPUT FILE

The ROOT file produced by the first calculation step is organized in two main TTree structures. The evolflux
structure is similar to the one used in depletion calculations and described in Section 40.5.2. It is written only
if the WRITE_FLUX keyword is specified in the DEPLETION block and it contains the flux computed on the
DEC_FLUX_MULTIG energy grid for each depleted composition. It contains the following branches:
step_num : the activation time step index;
compo_name : the name of the activated composition;
compo_vol : the volume in cm3 occupied by the current activated composition in the current mesh cell;
renormfact : the factor by which the reaction rates and fluxes are multiplied to obtain the normalization
specified with the RENORMALIZATION command;
cell_num : the index of the cell;
i, j, k : the indices of the activated mesh cell along the three mesh axes;

<!-- page 476 -->
umin, vmin, wmin : the lower bounds of the mesh cell coordinates, in the mesh coordinate system (cartesian,
spherical or cylindrical);
ulength, vlength, wlength : the size of the mesh cell along the three directions of the mesh coordinate system
(cartesian, spherical or cylindrical);
group_id : the index of the group;
energy1 : the lower energy for the current group, in MeV;
energy2 : the upped energy for the current group, in MeV;
flux_val : the value of the flux in the current group, in neutrons·cm−2 ·s−1;
This tree may require a great deal of disk space for large systems. In these cases, it is recommended to set
WRITE_FLUX to 0.
The other relevant TTree structure is gammaraystree. This structure will always be present in activation
calculations because it contains the necessary information for the second calculation step. It contains the
following branches:
step_num : see evolflux above;
irradtime : cumulative amount of irradiation time, in seconds;
coolingtime : cumulative amount of cooling time, in seconds;
compo_name : see evolflux above;
compo_vol : see evolflux above;
cell_num : see evolflux above;
i, j, k : see evolflux above;
umin, vmin, wmin : see evolflux above;
ulength, vlength, wlength : see evolflux above;
Egamma : energy of the emitted photon line, in MeV;
Igamma : activity of the emitted photon line, in Bq/cm3;
isotope_name : name of the isotope emitting the current photon line;
isotope_conc : concentration of the isotope emitting the current photon line, in 1024 cm−3.

<!-- page 477 -->
## 41.3 UNCERTAINTIES

Since R2S calculations are very similar to depletion calculations, one should apply the same caveats concerning
the calculation of the statistical uncertainties on the calculation results. A single two-step calculation
(neutron activation + photon transport) cannot possibly yield any estimate of the uncertainty. The only rigorous
way to estimate the uncertainty is to observe a number of independent calculation replicas. One can
then estimate the standard error from the dispersion of the sample. Assume N independent R2S calculations
(neutron activation + photon transport) were performed, and let Di be the photon dose (for example) resulting
from the ith independent calculation. Then the average photon dose ¯D and its standard error s ¯D are given by
the traditional formulas
¯D = 1
N
N
∑
i=1
Di
s2
¯D =
1
N(N −1)
N
∑
i=1
(Di −¯D)2
In practice, for the moment there are no pre- and post-processing tools that automate the tasks of creating
the independent replicas, seeding them with different random numbers, running the two calculation steps,
collecting the results and analyzing them. However, the launch scripts for depletion calculations can easily
be repurposed for launching independent replicas for the first calculation step.

<!-- page 478 -->
GRID_LIST
3
DEC_1G
2
2.0000E+01
1.0000E-11
DEC_2G
3
2.0000E+01
2.578840E-03
1.0000E-11
DEC_FLUX_MULTIG
176
1.0000000e-11
1.0000000e-07
4.1399000e-07
5.3158000e-07
6.8256000e-07
8.7642000e-07
1.1254000e-06
1.4450000e-06
1.8554000e-06
2.3824000e-06
3.0590000e-06
3.9279000e-06
5.0435000e-06
6.4760000e-06
8.3153000e-06
1.0677000e-05
1.3710000e-05
1.7603000e-05
2.2603000e-05
2.9023000e-05
3.7267000e-05
4.7851000e-05
6.1442000e-05
7.8893000e-05
1.0130000e-04
1.3007000e-04
1.6702000e-04
2.1445000e-04
2.7536000e-04
3.5358000e-04
4.5400000e-04
5.8295000e-04
7.4852000e-04
9.6112000e-04
1.2341000e-03
1.5846000e-03
2.0347000e-03
2.2487000e-03
2.4852000e-03
2.6126000e-03
2.7465000e-03
3.0354000e-03
3.3546000e-03
3.7074000e-03
4.3074000e-03
5.5308000e-03
7.1017000e-03
9.1188000e-03
1.0595000e-02
1.1709000e-02
1.5034000e-02
1.9305000e-02
2.1875000e-02
2.3579000e-02
2.4176000e-02
2.4788000e-02
2.6058000e-02
2.7000000e-02
2.8500000e-02
3.1828000e-02
3.4307000e-02
4.0868000e-02
4.6309000e-02
5.2475000e-02
5.6562000e-02
6.7379000e-02
7.2000000e-02
7.9500000e-02
8.2500000e-02
8.6517000e-02
9.8037000e-02
1.1109000e-01
1.1679000e-01
1.2277000e-01
1.2907000e-01
1.3569000e-01
1.4264000e-01
1.4996000e-01
1.5764000e-01
1.6573000e-01
1.7422000e-01
1.8316000e-01
1.9255000e-01
2.0242000e-01
2.1280000e-01
2.2371000e-01
2.3518000e-01
2.4724000e-01
2.7324000e-01
2.8725000e-01
2.9452000e-01
2.9720000e-01
2.9850000e-01
3.0197000e-01
3.3373000e-01
3.6883000e-01
3.8774000e-01
4.0762000e-01
4.5049000e-01
4.9787000e-01
5.2340000e-01
5.5023000e-01
5.7844000e-01
6.0810000e-01
6.3928000e-01
6.7206000e-01
7.0651000e-01
7.4274000e-01
7.8082000e-01
8.2085000e-01
8.6294000e-01
9.0718000e-01
9.6164000e-01
1.0026000e+00
1.1080000e+00
1.1648000e+00
1.2246000e+00
1.2873000e+00
1.3534000e+00
1.4227000e+00
1.4957000e+00
1.5724000e+00
1.6530000e+00
1.7377000e+00
1.8268000e+00
1.9205000e+00
2.0190000e+00
2.1225000e+00
2.2313000e+00
2.3069000e+00
2.3457000e+00
2.3653000e+00
2.3852000e+00
2.4660000e+00
2.5924000e+00
2.7253000e+00
2.8650000e+00
3.0119000e+00
3.1664000e+00
3.3287000e+00
3.6788000e+00
4.0657000e+00
4.4933000e+00
4.7237000e+00
4.9659000e+00
5.2205000e+00
5.4881000e+00
5.7695000e+00
6.0653000e+00
6.3763000e+00
6.5924000e+00
6.7032000e+00
7.0469000e+00
7.4082000e+00
7.7880000e+00
8.1873000e+00
8.6071000e+00
9.0484000e+00
9.5123000e+00
1.0000000e+01
1.0513000e+01
1.1052000e+01
1.1618000e+01
1.2214000e+01
1.2523000e+01
1.2840000e+01
1.3499000e+01
1.3840000e+01
1.4191000e+01
1.4550000e+01
1.4918000e+01
1.5683000e+01
1.6487000e+01
1.6905000e+01
1.7333000e+01
1.9640000e+01
END_GRID_LIST
Figure 41.1: An example of GRID_LIST block for R2S, with the 176 group boundaries of the VITAMIN-J structure (175 groups).
