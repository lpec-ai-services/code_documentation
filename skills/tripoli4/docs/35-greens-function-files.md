# GREEN'S FUNCTION FILES
<!-- source PDF pages 403-409 -->

<!-- page 403 -->
Chapter 35
GREEN’S FUNCTION FILES

## 35.1 OBJECTIVE

This feature allows for parametric studies where the aim is to determine the incidence of a source variation
on the scores (for example, a parametric study related to a new loading of the core).
This feature also allows for the contribution of the source areas for a required response to be determined (in
this case, there is no variation of the source). The goal is to obtain scores that are conditional to the creation
of particles in these source areas.

## 35.2 PRINCIPLE

During a reference simulation performed once for all, “Green’s functions” (or “transfer functions”) are stored
in files. These files are then re-used in a suitable way (renormalization of sources, reconstitution of scores)
in order to process a different configuration than the reference configuration (first type of exploitation) or to
re-express scores as conditional scores to the sources (second type of exploitation).
The denomination “Green’s function” includes several pieces of information stored when a particle contributes
to the score in the reference simulation:
1. “initial” information: the number of the source where the particle is created, coordinates, energy, statistical
birth weight (removed since version 12), and source amplitude at the particle initial position and
energy.
2. “final” information: particle energy and statistical weight when the particle contributes to the score in
the required tallying area, its contribution (quantity χ defined in chapter 15 on scores, whose expression
depends on the required type of estimator).
One interest of this approach is the reduction in the computation time (because the history of particles is not
simulated during the exploitation phase ) with a satisfactory quality for the results. The drawback is the huge
amount of storage volume required.

<!-- page 404 -->
## 35.3 LIMITATIONS AND HYPOTHESES

1. Processed particles are either NEUTRONS or PHOTONS. Combined NEUTRONS-PHOTONS problems are also
possible.
2. We must treat a SHIELDING or a FIXED_SOURCES_CRITICALITY type problem (CRITICALITY computations
are excluded).
3. This feature can be used only for tabulated sources. Thus, analytic sources and point sources are
excluded.
4. When using the EXPLOITATION mode, geometric data, composition, and biasing (if defined, in case
of use of a variance reduction technique) have to be strictly the same as the ones defined during the
CREATION phase.
5. Constraints on the possibilities of modification of the source : if we use a new source during the exploitation
(second mode of use), only the geometric distribution intensity and/or the value of the coefficient
COEFF can be modified. The spatial distribution of the source and the energetic, angular, and time
distributions must remain identical. However, these constraints are not tested by the code during the
exploitation phase. This is the user’s responsability.
6. The allowed types of geometric elements for the tallying of scores are only VOLUMES or FRONTIERS (no
points and lattice cells). During the exploitation of the files, the scores can be required by LIST and/or
SUM; on the other hand, during the creation phase each file corresponds to only one VOLUME or FRONTIER.
7. Currently, the only allowed response during exploitation are fluxes, reaction rates, and the H*(10) dose
equivalent rate (user can still use ANS77). Current requests are not possible.
8. Each created file corresponds to a useful tallying area and to a given type of estimator.
9. It is necessary to keep in mind the following approximation, in the case of an exploitation of the files
with a change of source (second mode of use) : the transport in the modified source is supposed to be
the same as in the original source.
10. The biasing, used during the exploitation phase with a change of source, is the same as the one used
for the original source (the code doesn’t need a second definition of the biasing during the exploitation
phase, and doesn’t check the existence or the coherence of the biasing). During the exploitation phase,
the new source initialization, biased if there is biasing, is indeed computed with the biasing defined in
the data file of the creation phase.
11. Finally, for this same exploitation mode, a part of the phase space that has been less fully explored
during the original simulation will obviously give a poor precision in the exploitation phase. It is thus
appropriate to use a biasing of the original simulation that is adapted as much as possible to the various
cases of exploitation under investigation.
12. Starting from version 12, Green’s function files are compatible with AMS variance reduction technique
(see Chapter 18). It should be noted that a significant increase of the Green’s function files size might

<!-- page 405 -->
occur when AMS technique is used compared to the Green’s function files size when INIPOND is used
(see Chapter 17) for the same configuration. By construction of the AMS algorithm, more particles
might, indeed, reach score zones and be stored in the Green’s function files. The number of simulated
particles in creation phase should therefore be chosen carefully.
13. Warning : the format for Green’s function files was modified from version 5 to version 6 and from
version 11 to version 12, the compatibility with the previous format is kept nevertheless. However,
concerning version 4, starting from version 4.3, the format of these files is incompatible with earlier
versions (4.2 to 4.0).

## 35.4 COMMAND STRUCTURE FOR USER DATA

### 35.4.1 CREATION PHASE

The structure command is as follows:
GREEN_FUNCTION_TAPE
XDR_BUFFER buffer_size
CREATION
n
FILE_NAME filename_1
<PARTICLE_TYPE>
<ESTIM_NAME>
*
VOLUME numvol_1
*
FRONTIER numvol_1(1) numvol_1(2)
...
FILE_NAME filename_n
<PARTICLE_TYPE>
*
VOLUME numvol_n
*
FRONTIER numvol_n(1) numvol_n(2)
<ESTIM_NAME>
END_CREATION
END_GREEN_FUNCTION_TAPE
where:
- n is the number of required files
- buffer_size is the size of the buffer used for the Green’s function files dump. The keyword XDR_BUFFER is
optional. When it is not used, the default buffer size is set to 2.109.
- <PARTICLE_TYPE> is either NEUTRON for pure neutron problems, PHOTON for pure photon problems or
PHOTON_FROM_NEUTRON_SOURCE for coupled neutron-photon problems (“initial” information are then
related to the source neutrons and “final” information are related to the elementary contributions to the

<!-- page 406 -->
photon scores; in this case, when these Green’s function files are re-used, the user will just have to define
photon responses in the directive RESPONSES).
- filename_i is the name (chosen by the user) of the file associated to the ith requested file.
The files are created in the tree structure, at the level of the call to TRIPOLI-4® in mono-processor
mode. If the creation takes place in parallel mode, the code will automatically open one file for each
simulator, with the appropriate parallel suffix < j >th_task (for the jth simulator). The use of the graph
file command RUN_DIRECTORY enables to create the files in a requested directory in parallel mode (see
chapter 33).
- <ESTIM_NAME> is the type of estimator. It can only be COLL, TRACK, or SURF.
- The volumes are defined by their number numvol_i and the surfaces are defined by the numbers of the two
delimiting volumes, numvol_i1 and numvol_i2.
Note: In addition to the creation of Green’s function files, the user can use the simulation performed during
the creation phase to ask for standard scores (using the SCORE command).

### 35.4.2 EXPLOITATION PHASE

The structure command is as follows:
GREEN_FUNCTION_TAPE
EXPLOITATION
n
FILE_NAME filename_1 filename_2...filename_n
*
NEW_SCORES
*
SOURCES_CONTRIBUTIONS
...
END_EXPLOITATION
END_GREEN_FUNCTION_TAPE
where:
- n is the number of files to be exploited.
- filename_1 to filename_n are the exploited files.
It is highly recommended that the filenames of the creation and exploitation blocks are exactly the same.
Specifically, if the creation phase took place in a parallel run, the code will automatically open the files
with the parallel suffix < j >th_task appended to the user filenames (i.e., the suffix must not be present
in the filenames given by the user).
The code searches for these files in the tree structure where the call to TRIPOLI-4® is made. Among

<!-- page 407 -->
these n files, only those corresponding to the tallying area of the scores required in the phase of exploitation
are really used.
- There are two kinds of exploitation:
1. The keyword NEW_SCORES corresponds to a change of sources. Then, we use the Green’s function files
to compute new scores corresponding to this new source.
2. The keyword SOURCES_CONTRIBUTIONS corresponds to the computation of conditional scores taken
from the simulation of the files creation. The source may be changed or remain the same as in the
creation phase; however, we look for scores conditional to different cells of the tabulated source and to
different energy groups of the source particles.
In this last case of exploitation, additional data have to be given as follows:
SOURCES_CONTRIBUTIONS
GRID n
val1 val2...valn
*
SOURCES_NUMBER <LIST_OR_SUM> m
num1 num2 ...numm
*
SOURCES_INTER_VOLU <LIST_OR_SUM> m
volunum1 volunum2 ...volunumm
*
SOURCES_ALL_TABULATIONS m
num1 num2 ...numm
where :
- GRID gives the energy grid of the source (in n - 1 groups). The grid has to be in a decreasing order.
- <LIST_OR_SUM> equates to LIST or SUM. m is the number of volumes in the list or the sum required;
- With respect to spatial considerations, the user can either:
1. use the keyword SOURCES_NUMBER to input the numbers of the sources (index from 0 to the number of
sources in the directive SOURCES_LIST - 1). The conditional score will be given for each source (case
LIST) or for the full set (case SUM).
2. use the keyword SOURCES_INTER_VOLU to define the volumes (with any of the forms known by the geometry
of TRIPOLI-4®) including sources or parts of sources. Only the intersection of these volumes
(for which the number is given) and the sources are retained.
Be careful, these volumes have to be defined before in the geometry as virtual volumes (with the keyword
FICTIVE) and are put on top of the geometry. Moreover, these volumes have to be disconnected.
The conditional score will be given for each virtual volume (case LIST) or globally for the full set (case
SUM).

<!-- page 408 -->
3. use the keyword SOURCES_ALL_TABULATIONS to request contributions on all cells of the tabulated
sources whose numbers are mentioned from num1 to numm (index from 0 to the number of sources
in the directive SOURCES_LIST - 1); this is implicitly a list of sources, since the sum has no meaning
here.
Note: During the exploitation phase of Green’s function files, the user can request the display of source
sites (see subsection 25.1.6) in order to analyze the birth sites of particles involved in the data storage of the
Green’s function files.

## 35.5 USE OF PARALLELISM

Working in parallel mode is similar to working in a single-processor mode. It should be noted, however, that
the exploitation phase is always performed in mono-processor mode.
Warning: It is necessary to request at least one score in parallel mode. In this version of Tripoli4, the parallel
mode does not work unless a result is requested.
As previously noted, the directory for Green’s function files is the same as that where the simulators were
executed. In parallel mode, this directory may vary depending upon the execution mode. The RUN_DIRECTORY
command must be used in the graph file (see chapter 33) in order to indicate this specific directory.

## 35.6 ASPECT OF THE OUTPUT FILE

### 35.6.1 CREATION PHASE

After the standard printing of the required scores is completed, the output file contains information about the
number of particles collected for each file (i.e., each potential tallying area for the exploitation phase). This
information is introduced using “NUMBER OF CONTRIBUTING PARTICLES” at the end of the output file.

### 35.6.2 EXPLOITATION PHASE

The information (present or absent) used to indicate a file exploitation instead of a real simulation is as
follows:
1. absence of statistical information on the biasing (in the case where a variance reduction technique is
used) for the first six batches, usually tallied at the beginning of the simulation.
2. “mean weight leakage : unknown”: before the printout of the scores (in fact, the statistics about particles
leakage cannot be input since there is no simulation of the particles trajectories)
3. “exploitation time” instead of “simulation time” at the end of the output file.
- Case NEW_SCORES : The printing of new scores is done in the standard form because these scores have the
same structure as the usual scores.

<!-- page 409 -->
- Case SOURCES_CONTRIBUTIONS : In this case, the printing of scores changes. For each required score, the
different tallying variables are given in the following order:
1. first, by group of energy sources (outer loop): this is introduced using “SOURCE SPECTRUM STEP
NUMBER”
2. then, by source number “SOURCE NUMBER” or by virtual source volume “SOURCE VOLUME” (for a LIST)
or globally for the full set with “SUM ON SPECIAL SOURCE NUMBERS” or “SUM ON SPECIAL SOURCE
VOLUMES” (for a SUM)
3. then by (U,V,W) cell indices (relatively to the VAR_U, VAR_V and VAR_W variables defined in the syntax
of the tabulated sources, cf. section 12.2.2.3) if the option SOURCES_ALL_TABULATIONS is used
4. then, by group of tallying energy (inner loop): this is introduced using “SPECTRUM RESULTS”, as for
usual scores.
The energy integrated scores are written only when a single source number or a single virtual volume number
is mentioned in LIST or when a SUM is used. They are not written if the option SOURCES_ALL_TABULATIONS
is used.

## 35.7 INCOMPATIBILITIES

The following features are incompatible with the Green band calculations:
• VOV, BOOTSTRAP, and COMPLETE options of the scores;
• current scores.
Some other incompatibilities may be found in the section limitations (35.3).
