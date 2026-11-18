# DEFINING PERTURBATIONS
<!-- source PDF pages 352-361 -->

<!-- page 352 -->
Chapter 28
DEFINING PERTURBATIONS

## 28.1 GENERAL

Apart from the usual scores, it is possible to calculate scores for materials with different compositions (although
the nuclei must be the same).
A number of perturbations can be requested in the same calculation. Theses perturbations can be calculated
either by the correlated sampling method (keyword PERTURBATION) or by the Taylor series approach
(keyword TAYLOR_PERTURBATION).
The syntax of the command is as follows:
PERTURBATION_LIST
nb(perturb)
PERTURBATION
Data on perturbation 1
END_PERTURBATION
TAYLOR_PERTURBATION
Data on perturbation 2
END_TAYLOR_PERTURBATION
...
PERTURBATION
Data on perturbation nb(perturb)
END_PERTURBATION
END_PERTURBATION_LIST
where nb(perturb) is the number of perturbations.

## 28.2 DATA ON A PERTURBATION

A perturbation is characterized by:
• a type (see below);

<!-- page 353 -->
• a list of volumes with an identical composition, which corresponds to the composition to be perturbed
(only these volumes are affected by the perturbation);
• perturbation data (multiplication factors);
• a list of the scores for which outputs are required (neutron scores only can be requested);
• a mode used to output the results (value of score or difference compared to the unperturbed score).
The TRIPOLI-4® code can calculate two types of perturbed scores:
• perturbations for given concentrations,
• perturbations for total density of materials.
It is not possible to mix density and concentration perturbations in a single perturbation.
The point-based estimator FLUX_PT is not compatible with any perturbation.

## 28.3 DENSITY AND CONCENTRATION PERTURBATIONS

For perturbations with the correlated sampling method (default), the syntax is as follows:
PERTURBATION
<CONCENTRATION_OR_DENSITY> nb(compo)
name_compo(1) VOLUME LIST nb(volu)
num_volu(1) ...num_volu(n)
FACT fact(1)...fact(n)
...
name_compo[nb(compo)] VOLUME LIST nb(volu)
num_volu(1) ...num_volu(n)
FACT fact(1)...fact(n)
SCORE LIST nb(scores)
num_score(1) ...num_score(n)
MODE DELTA or MULTI
END_PERTURBATION
while for the Taylor series approach, the syntax is:

<!-- page 354 -->
TAYLOR_PERTURBATION
<CONCENTRATION_OR_DENSITY> nb(compo)
name_compo(1) VOLUME LIST nb(volu)
num_volu(1) ...num_volu(n)
FACT fact(1)...fact(n)
...
name_compo[nb(compo)] VOLUME LIST nb(volu)
num_volu(1) ...num_volu(n)
FACT fact(1)...fact(n)
ORDER order
SCORE LIST nb(scores)
num_score(1) ...num_score(n)
MODE DELTA or MULTI
END_TAYLOR_PERTURBATION
where:
• <CONCENTRATION_OR_DENSITY> is CONCENTRATION for concentration perturbations or DENSITY for
density perturbations;
• nb(compo) is the number of compositions to be perturbed;
• name_compo(i) is the name of the material of the ith perturbation;
• nb(volu) is the number of volumes associated with the composition;
• num_volu(1) ...num_volu(n) is a list of the volumes affected by the perturbation;
• fact(1)...fact(n) is a list
– with one multiplication factor for each nucleus in the case of a concentration perturbation: for three
nuclei, list 1.1 0.9 1.0 means that the concentration of the first nucleus defined is increased by
10 per cent, that of the second one reduced by 10 per cent, and that of the third remains unchanged.
– a single element for a density perturbation: the multiplication factor for the perturbation (1.1 means
that the density is increased by 10 per cent).
• order is the order of the Taylor series (1 or 2).
• nb(scores) and {num_score(i)} are, respectively, the number and indices for the scores (in the input
order of the SCORE command, counting from 1) for which the outputs are required;
• line MODE DELTA or MULTI means that differential results are requested (difference relative to the unperturbed
score) DELTA instead of absolute results MULTI.
In criticality mode, available only for the correlated sampling method, the code calculates the perturbed values
for keff. If there are no options, this corresponds to a criticality calculation, and only the perturbed keff values
are calculated.

<!-- page 355 -->
Important:
At the present time, the concentration perturbation can only relate to one material (nb(compo)=1).
The concentration perturbation is not available for a composition using natural elements, i.e. with the -NAT
or -NAT-SPLIT suffix.

## 28.4 PARTIAL CROSS-SECTION PERTURBATION

### 28.4.1 SYNTAX

It is possible to perturb the cross-sections of all interaction types (elastic, discrete inelastic, etc.). These
perturbations can be defined for several energy ranges, i.e., in an energy grid, and, as such, can differ by group.
However, the perturbations of differential cross-sections (with respect to anisotropy or energy transfer) are
not (yet) implemented. These perturbations are qualified as deterministic as opposed to a random perturbation
of these cross-sections (see next section) to allow for uncertainty concerning the cross-sections.
Since the code deals with point-wise cross-sections, the perturbed cross-sections are defined by multiplication
coefficients applied to the original cross-sections. It is important to guarantee consistency (the total crosssection
must be equal to the sum of the cross-sections). If, for example, an absorption cross-section is
increased (for example, n →γ), it is possible to accordingly increase the total cross-section or, conversely,
to accordingly reduce the cross-sections of other interactions (for example a n →p) in order to maintain
consistency in the cross sections. These carry-over rules are left to the discretion of the user and are given in
a file whose path is included in the perturbation command.
The syntax is as follows:

<!-- page 356 -->
PERTURBATION
DETERMINISTIC
NUCLEI nb(nuclei)
nb_compo(nucleus-1)
name_compo(1,1) VOLU LIST nb(volu)
num_volu(1) ...num_volu(n)
...
name_compo[nb(compo),1] VOLU LIST nb(volu)
num_volu(1) ...num_volu(n)
NUCLEUS name_nucleus(1)
DATA name(file-1)
...
nb_compo(N)
name_compo(1,N) VOLU LIST nb(volu)
num_volu(1) ...num_volu(n)
...
name_compo[nb(compo),N] VOLU LIST nb(volu)
num_volu(1) ...num_volu(n)
name_nucleus(1) DATA name(file)
NUCLEUS name_nucleus(N)
DATA name(file-N)
SCORE LIST nb(scores)
num_score(1) ...num_score(n)
MODE DELTA
END_PERTURBATION
The definitions of the terms are as follows:
• DETERMINISTIC is a keyword specifying deterministic perturbations.
• NUCLEI nb(nuclei) corresponds to the number of nuclei to be perturbed (two in the example below
involving iron-56 and iron-54).
• Then, a list of the perturbations is given (for each nucleus). The following are indicated for each: the
number of compositions (here, the two compositions that contain iron-56 for the first perturbation), the
names of the compositions (IRON_BULK and IRON), the volumes associated with the compositions (18 in
the case of IRON_BULK and 2 in that of IRON), the name of the nucleus (after the keyword NUCLEUS), a
data file defining carry-over between the sections (after the keyword DATA).
• Then a list of the perturbed scores is given with the quantity and the numbers of the scores (16 scores in
this case). Even for a criticality calculation, at least one score must be specified.
• Then, the perturbation mode (absolute value by default);

<!-- page 357 -->
Example:
PERTURBATION
DETERMINISTIC
NUCLEI 2
2
IRON_BULK VOLUME LIST 18
8 20 21 22 23 24 25 255 26 27 28 29 30 31 32 33 34 35
IRON VOLUME LIST 2
9 12
NUCLEUS FE56 DATA Tripoli4/Test/Pertu/Det/fe56
2
IRON_BULK VOLUME LISTE 18
8 20 21 22 23 24 25 255 26 27 28 29 30 31 32 33 34 35
IRON VOLUME LIST 2
9 12
NUCLEUS FE54 DATA Tripoli4/Test/Pertu/Det/fe54
SCORE LIST 16 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
END_PERTURBATION

### 28.4.2 THE CARRY-OVER FILE

Here is an example of a carry-over file.
O16 300 endfb6
3 1.0000E-05 2.40000E+06 2.90000E+06 20.E+06
PERTU 2 2 102
CARRY_OVER 1 51
1.
0
1.
0
1.01 0
1.
0

<!-- page 358 -->
1.01 0.1
1.
0
The file contains five different pieces of information, described below:
• The first line contains three fields that respectively specify the perturbed nucleus, the temperature of the
nucleus, and the library from which the nucleus is derived.
• The next two lines contain the energy grid used for defining the perturbation.
Important:
– when defining the grid, the number of groups is given (and not the number of bounds to be read),
then the bounds of the grid.
– the energy must be in eV and not in MeV.
• The word PERTU precedes the list of the perturbed interactions. It is followed by the number of perturbed
interactions, then by the number used by NJOY to encode each interaction. Important: these
codes are not those used for referencing interactions in scores, but those given in the NJOY manual [35].
In the example, two interactions are perturbed, corresponding to elastic scattering (NJOY number 2) and
n →γ capture (NJOY number 102).
• The keyword CARRY_OVER (required even if carry-over is not used) here defines carry-over relating
to the NJOY 51 interaction code (discrete inelastic level 1). When carry-over is not used, one must
nevertheless give an interaction code (for example 51), but then all carry-overs should be zero.
• Finally, there are the carry-overs. They are given for each group in the order in which the grid is given
at the top of the file, then, for each perturbed interaction, in the order in which it is given after keyword
PERTU. The factor by which the original cross-section is multiplied must be specified in order to yield
the perturbed cross-section and the extent to which the perturbation is carried over to interaction 51.
Thus:
– In the first group, no perturbations apply to the cross-sections (factor of first column equal to 1) and
the carry-overs are zero.
– In the second group, the elastic scattering cross-section is increased by 1% and there is a zero carryover
to discrete inelastic level 1, thus the increase in the scattering cross-section is reflected in the
total. Radiative capture is unchanged.
– In the last group, the elastic scattering cross-section is increased by 1%. But 10% of the crosssection
increase is removed from the discrete inelastic level 1, and the remaining 90% is carried
over to the total which is increased accordingly.
Note: If a carry-over is too large, it may result in negative cross-sections. In such cases, the code breaks and
displays a message indicating the energy and cross-sections involved. In such cases, it is necessary to change
the carry-over or the perturbation.

<!-- page 359 -->
Interaction
Code Particle
Elastic scattering
2
neutron
Discrete inelastic and continuous scattering
4
neutron
n→2n
16
neutron
n→fission
18
neutron
Level 1 discrete inelastic scattering
50+1
neutron
Level i discrete inelastic scattering
50+i
neutron
Level 40 discrete inelastic scattering
90
neutron
Continuous inelastic scattering
91
neutron
Absorption. Photon emission
102
neutron
Absorption. Proton emission
103
neutron
Absorption. Alpha emission
107
neutron
Table 28.1: NJOY interaction codes for carry-over file

<!-- page 360 -->
## 28.5 COVARIANCE PERTURBATIONS

The syntax is as follows:
PERTURBATION
COVARIANCE
NUCLEI nb(nuclei)
nb_compo(nucleus-1)
name_compo(1,1) VOLUME LIST nb(volu)
num_volu(1) ...num_volu(n)
...
name_compo[nb(compo),1] VOLUME LIST nb(volu)
num_volu(1) ...num_volu(n)
NUCLEUS name_nucleus(1)
DATA name(file-1)
...
nb_compo(N)
name_compo(1,N) VOLUME LIST nb(volu)
num_volu(1) ...num_volu(n)
...
name_compo[nb(compo),N] VOLUME LIST nb(volu)
num_volu(1) ...num_volu(n)
name_nucleus(1) DATA name(file)
NUCLEUS name_nucleus(N)
DATA name(file-N)
SCORE LIST nb(scores)
num_score(1) ...num_score(n)
MODE DELTA
PERTU_PERIOD nb(batch)
END_PERTURBATION
Where:
• COVARIANCE is a keyword indicating covariance perturbations;
• NUCLEInb(nuclei) is the number of nuclei to be perturbed (2 in the example below involving iron-56
and iron-54);
• Then a list of the perturbations is given (for each nucleus). For each, the following is given: the number
of compositions (here the two compositions that contain iron-54 for the first perturbation), the name
of the compositions (IRON_BULK and IRON), the volumes associated with the composition (18 in the
IRON_BULK case and 2 in the IRON case), the name of the nucleus (after keyword NUCLEUS), and the
covariance data file (after the keyword DATA).
• Then a list is given of the perturbed scores with the number and the indices for the scores (16 scores in
this case);

<!-- page 361 -->
• Then the perturbation mode (absolute value by default);
• Then the sampling period (as a number of batches).
Example:
PERTURBATION
COVARIANCE NUCLEI 2
2
IRON_BULK VOLUME LIST 18
8 20 21 22 23 24 25 255 26 27 28 29 30 31 32 33 34 35
IRON VOLUME LIST 2
9 12
NUCLEUS FE56 DATA Test/Pertu/Covar/fe56.cov.user.data.2
2
IRON_BULK VOLUME LISTE 18
8 20 21 22 23 24 25 255 26 27 28 29 30 31 32 33 34 35
IRON VOLUME LIST 2
9 12
NUCLEUS FE54 DATA Test/Pertu/Covar/fe54.cov.user.data.2
SCORE LIST 16 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
PERTU_PERIOD 400
END_PERTURBATION
