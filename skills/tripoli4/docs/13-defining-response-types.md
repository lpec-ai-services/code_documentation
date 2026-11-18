# DEFINING RESPONSE TYPES
<!-- source PDF pages 190-211 -->

<!-- page 190 -->
Chapter 13
DEFINING RESPONSE TYPES
Calculating a score requires knowledge of the following:
• the type of the response function (flux, current, reaction rate, ...);
• the energy, angle, or time grid on which the results are required;
• the points, surfaces, or volumes of the geometry in which the response is to be computed, and the chosen
estimator.
The tasks are divided among three modules: the RESPONSES module, which defines the type of the responses,
the GRID_LIST module, which defines the grids, and the SCORE module, which specifies the geometrical data
and the estimators and uses the data previously described in the RESPONSES and GRID_LIST modules. The
responses are defined between the RESPONSES and END_RESPONSES keywords.

## 13.1 THE AVAILABLE RESPONSES

Responses are physical quantities calculated by the code during a simulation.
Responses can be of the following types:
• a flux (in neutronics, this corresponds to a density multiplied by a speed);
• a current;
• a dose equivalent rate H*(10), 1997 (ICRP-74 standard) [45];
• a dose equivalent rate ANS, 1977 [3] (this is for backward compatibility only);
• a reaction rate (to be specified);
• a macroscopic reaction rate (to be specified);
• an energy deposition in matter;
• a kinematic limit;

<!-- page 191 -->
• a Displacement Per Atom (DPA);
• a gas production;
• a fission spectrum;
• a production of particles of a given type (for example a photon source or an electron source);
• a histogram of deposited energy per source particle (gamma detector spectrum for example);
• a histogram of deposited charge per source particle;
• a total deposited energy per source particle (gamma dose for example);
• a fixed source emission;
• a histogram of number of fission neutrons sampled per fission;
• a histogram of the sum of fission neutron energies per fission;
• a (Z,A) distribution of the fission products (after emission of prompt neutrons).
The units are for:
• volume flux: by default, the volume-integrated flux values are given in the number of particles times
the unit length per unit time (neutron·cm/s); if the volume is given, the values will be in the number of
particles per unit area per unit time (neutron/(cm2·s));
• surface flux: by default, the surface-integrated flux values are given in the number of particles per unit
time (neutron/s); if the surface area is given, the values will be given in the number of particles per unit
area per unit time (neutron/(cm2·s));
• point flux: the values are in number of particles per unit area per unit time (neutron/(cm2·s));
• current: same units as for surface flux;
• energy deposition in the material or kinematic limits: MeV/s;
• dpa: (displaced atoms)/s;
• reaction rate or macroscopic reaction rate: same as flux, but with the conversion factor (flux, rate);
• dose equivalent rate H*(10): µSv/h if the volume is given;
• dose equivalent rate ANS: rem/h if the volume is given;
• production of particles and gas production: particle_type/s (for example photon/s for a photon source,
or alpha particles/s for gas production);
• detector spectrum : counts/s;
• charge deposition spectrum: the score result is given as charge deposition (in units of the elementary
charge) per unit time and unit volume: charge/(s cm3);

<!-- page 192 -->
• fixed source emission: the same units as for the source definition;
• histogram of number of fission neutrons: neutron/s;
• (Z,A) distribution: the same units as for the source definition.
Each response corresponds to a type of particle (NEUTRON, PHOTON, ELECTRON, or POSITRON).
However, the concept of flux as used in neutron and photon transport is not meaningful for charged particles.
One exception is DEPOSITED_SPECTRUM and DEPOSITED_SPECTRUM_WEIGHTED_ENERGY if PHOTON,
ELECTRON and POSITRON are included in the simulation. There is no difference between deposited energy by
these particles, then the response particle must be the list PHOTON ELECTRON POSITRON.
Responses are defined sequentially after giving the number of total responses. There can be several reaction
rates. The syntax is as follows:
RESPONSES
nb(responses)
NAME <name1>
<type1> <particle1>
<additional data>
...
NAME <nameN>
<typeN> <particleN>
<additional data>
END_RESPONSES
Available responses <types> are:
1. FLUX
2. DOSE: equivalent to DOSE_H*(10) (DOSE_ANS77 is still available)
3. CURRENT
4. WEIGHTED_COURANT (see sections 13.4 and 13.5 for the additional data)
5. REACTION (see sections 13.2 to 13.4 for the additional data)
6. MACROSCOPIC_REACTION_RATE (see section 13.6 for more information)
7. DEPOSITED_ENERGY (see section 13.7 for more information)
8. KINEMATIC_LIMITS (see section 13.8 for more information)
9. DPA (see section 13.9 for more information)
10. GAS_PRODUCTION (see section 13.10 for more information)

<!-- page 193 -->
11. FISSION_SPECTRUM (see section 13.11 for more information)
12. PRODUCTION (see the following notes for more information)
13. DEPOSITED_SPECTRUM
14. DEPOSITED_SPECTRUM_WEIGHTED_ENERGY
15. DEPOSITED_CHARGE (see section 13.13 for more information)
16. FIXED_SOURCE_EMISSION (see section 13.12 for more information)
17. NU_FISSION
18. FISSION_N_SUM_SPECTRUM
19. FISSION_ZA_DISTRIBUTION
It is possible to assign a name to the responses (using the keyword NAME).
Additional data are required only for reaction rates and weighted currents (WEIGHTED_COURANT).
Notes:
• The flux per unit area (or current) cannot be calculated for all of the surfaces (see SCORE);
• For the DOSE_H*(10) response, only particle types NEUTRON or PHOTON can be specified;
• The DEPOSITED_SPECTRUM response is used to calculate the spectrum of electromagnetic deposited
energy in a detector. This response can be used with or without the electromagnetic shower option (in
the SIMULATION command, see chapter 22), however if PHOTON, ELECTRON and POSITRON are included
in SIMULATION command, then all these particles have to be included also in response particle data
whereas if only PHOTON is present, then only PHOTON is needed in response.
Note also that if a variance reduction technique is needed together with this specific response, the only
available technique is the AMS technique (see Chapter 18).
• The DEPOSITED_SPECTRUM_WEIGHTED_ENERGY response is used to calculate electromagnetic deposited
energy per source particle in a detector (γ dose). It’s a physical reference calculation of γ dose without
tabulated response function but may be time consuming. The same DEPOSITED_SPECTRUM remarks
apply to DEPOSITED_SPECTRUM_WEIGHTED_ENERGY. The integral values over all energy domain of
DEPOSITED_SPECTRUM_WEIGHTED_ENERGY and DEPOSITED_ENERGY must be equal (in γe± problems)
but the energy grid meaning differs: it is incident energy in DEPOSITED_ENERGY and deposited energy
in DEPOSITED_SPECTRUM_WEIGHTED_ENERGY.
• The PRODUCTION response gives the production of secondary particles of a given type 2 (neutron, photon,
electron or positron), produced by particles of a given type 1 (neutron, photon, electron or positron).
Additional data must be defined with the following syntax:
PRODUCTION <particle_type_2> FROM <particle_type_1> <spectrum_type>

<!-- page 194 -->
where <spectrum_type> is either SECONDARY_SPECTRUM or INCIDENT_SPECTRUM, corresponding to
results requested in an energy grid relatively to the secondary particle or to the incident particle.
Note that:
– keywords PHOTON_REPARTITION and ELECTRON_REPARTITION (available from earlier versions
than 7) are still available and are equivalent to the syntax : PRODUCTION PHOTON FROM NEUTRON
SECONDARY_SPECTRUM and PRODUCTION ELECTRON FROM PHOTON SECONDARY_SPECTRUM.
– when <particle_type_2> = <particle_type_1>, all reactions with one or several outgoing particles
of the required type are taken into account (for example, for the case <particle_type_2> =
<particle_type_1> = NEUTRON, all scattering and fission neutrons are collected).
– if the THICK_TARGET_BREMSSTRAHLUNG option is used, photons produced by Bremsstrahlung are
collected by PHOTON as <particle_type_1> of the PRODUCTION response (and not ELECTRON, which
has to be used in the frame of the full electromagnetic shower only).
• For scores associated with the PHOTON_REPARTITION response function (or its equivalent with the
PRODUCTION keyword), the only gamma data taken into account are those given in the evaluations associated
with the collided nucleus undergoing interactions processed in simulations (gamma productions
associated with possible products of reactions are not taken into account).
• The NU_FISSION and FISSION_N_SUM_SPECTRUM responses are used to calculate a histogram of the
number of fission neutrons per fission event, and a histogram of the sum of fission neutron energies
per fission event, as sampled during the simulation. These responses are of interest when fission is
sampled from a fission model (see Section 22.1). The distribution of the neutron multiplicity is then
different from the two-group histogram of integer numbers surrounding the mean value provided by the
evaluated data, produced when no fission model is used. The particle type must be NEUTRON. These
responses are available only with the analog simulation mode for neutrons, with or without a fission
model (see Section 22.1).
• The FISSION_ZA_DISTRIBUTION response is available with analog neutron transport with a fission
model (LLNL_FISSION or FIFRELIN in the SIMULATION command block, see Section 22.1). The Z
and A values of the fission products, after emission of prompt neutrons, are given by the fission model to
TRIPOLI-4®. When the TRIPOLI-4® results are edited, the distribution is provided in a 2D (Z,A) mesh
defined by the user in the SCORE command block (see Section 15.7). The particle type of the RESPONSES
command block must be NEUTRON.

<!-- page 195 -->
## 13.2 ADDITIONAL DATA FOR REACTION RATES

For a reaction rate, it is also necessary to provide data concerning the reaction rate to be calculated. First, the
nucleus name name(nucleus) is given after the keyword NUCLEUS. This name must be one of the nucleus
names in the library, unless the reaction is defined by DATA. This data may be given in three different forms:
• A nucleus in a composition and one or more interactions (introduced using COMPOSITION).
This corresponds to a macroscopic reaction rate.
If several interactions are required, they will be
combined to give the reaction rate sought;
• A virtual nucleus and one or more interactions (introduced using FICTIVE). This corresponds to a microscopic
reaction rate. Here again, the reaction rate is the sum of the reaction rates of the different
interactions requested. A virtual nucleus is defined as a nucleus which is not found in any of the combinations
in the problem. The temperature must be indicated, in the form of an integer.
Important: in the above two cases, the code seeks the nucleus in the ENDF files. But to be able to access
it, it is necessary for the particle concerned (NEUTRON , PHOTON, ELECTRON, or POSITRON) to be declared
in the SIMULATION command. Therefore, if a neutron reaction is requested for a gamma only problem,
the code will fail, even if the response is not used;
• A nucleus (any name is acceptable) and cross-section data tabulated with an interpolation mode. In this
case, the user inputs the cross-section to be used in the reaction rate calculation. The cross-section value
data are stored internally according to an NJOY cross-section model.
The syntax is, therefore, as follows:
REACTION <PARTICLE_TYPE>
NUCLEUS name(nucleus)
*
COMPOSITION name(compo)
INTERACTION nb(interactions)
codeinteractions(1)...codeinteractions(n)
*
FICTIVE temperature
INTERACTION nb(interactions)
codeinteractions(1)...codeinteractions(n)
*
( COEFF coeff) DATA
DATA additional data
*
( COEFF_NB_ISOTOPES name-compo) DATA
DATA additional data
where:
• <PARTICLE_TYPE> is NEUTRON or PHOTON.
• The available interaction codes are given in Tables 13.1 and 13.2.
• For the DATA choice, it is possible to multiply the values by a coefficient coeff. In the absence of the
words COEFF coeff, the coefficient equals 1.

<!-- page 196 -->
With COEFF_NB_ISOTOPES followed by the name of a composition, the coefficient is calculated internally
and equals the number of atoms of the isotope in this composition for 10−24 cm3.
Important warning for International Reactor Dosimetry Files (IRDF) reaction rates:
When requesting an IRDF reaction rate (from the related dosimetry nuclear data files), it is recommended
to use DATA (instead of FICTIVE) option.
Otherwise, if the energy grid of the reaction of interest is
different from the total cross-section energy grid (which may happen only for these specific dosimetry files),
cross-section values may be linearly interpolated on the missing energies of the total cross-section energy
grid, which could lead to different reaction rate results.
Notes for Table 13.1:
• code 105 refers to the sum of all other neutron interactions that are not mentioned by another code (in
order to be consistent with the total neutron cross-section).
• codes 40 and 41 refer to nuclide transmutation, outside the unresolved range for code 40, in the unresolved
range for code 41. Both reaction rates can be requested with or without probability tables.
Reaction rate 41 is always zero when probability tables are missing. When probability tables are used,
the response function has zero values for energies outside the unresolved range. Conversely for response
40, when probability tables are used, the response function has zero values for energies in the
unresolved range. The non-zero values are equivalent to the summation of reaction rates 58, 24, 25 and
26. Summation of both reaction rates 40 and 41 can be useful.
• code 42 refers to the sum of the following neutron scattering interactions: elastic, total inelastic (discrete
and continuous), (n,nα), (n,np) and the three thermal scattering interactions (codes 30 to 32).
• reaction rates available only from version 7 on (interaction codes 242000 to 242016, 53000 to 53049,
54000 to 54049, 55000 to 55049, 56000 to 56049, 57000 to 57049, 245, 543 and 552) cannot be requested
with the execution option -k which disables the reading of cross-sections for these interactions
(see chapter 1).
Notes for Table 13.2:
• code 142 refers to the sum of all other photonuclear interactions that are not mentioned by another code
(in order to be consistent with the total photonuclear cross-section).
• code 145 refers to the neutron production rate from photonuclear reactions, defined as the sum of the
νi ∗σi for the interactions i producing photoneutrons (note that neutrons produced by photofission are
not taken into account).
• the request of photonuclear reaction rates needs the keyword PHOTO_NUCLEAR in the SIMULATION command
block (see chapter 22).

<!-- page 197 -->
NEUTRON INTERACTION
CODE
Total
104
Elastic scattering
21
Discrete inelastic scattering
22
Level i disc. inel. scat., (i) from 01 to 40
220(i)
Continuous inelastic scattering
23
n →N·n
24
n →2n
242
Level i disc. n →2n, (i) from 00 to 16
2420(i)
n →3n
243
n →4n
244
n →2n + α
245
n →n + 2α
272
n →n + α
25
n →n + p
26
Discrete and continuous inelastic scattering
28
Coherent elastic scattering
30
Incoherent elastic scattering
31
Incoherent inelastic scattering
32
Fission
33
ν·σf
34
νprompt ·σf
35
νdelayed ·σf
36
Nuclide transmutation outside URR
40
Nuclide transmutation in URR
41
Total neutron scattering
42
n →γ absorption
52
n →p absorption
53
Level i disc. n →p absorption, (i) from 00 to 49
530(i)
n →2p absorption
532
n →t absorption
54
Level i disc. n →t absorption, (i) from 00 to 49
540(i)
n →t + 2 α absorption
543
n →α absorption
55
Level i disc. n →α absorption, (i) from 00 to 49
550(i)
n →2α absorption
552
n →3He absorption
56
Level i disc. n →3He absorption, (i) from 00 to 49
560(i)
n →d absorption
57
Level i disc. n →d absorption, (i) from 00 to 49
570(i)
Total absorption
58
Other interactions
105
Table 13.1: Data file interaction codes for neutron reactions.

<!-- page 198 -->
PHOTON INTERACTION
CODE
Total
106
Coherent scattering
100
Incoherent scattering
101
Photoelectric effect
102
Pair production
103
Total photonuclear
130
γ →N·n
131
γ →2n
1312
γ →3n
1313
γ →n + p
132
γ →n + α
133
γ →n + 2α
1332
Discrete and continuous γ →n
135
Discrete γ →n
136
Level i disc. γ →n, (i) from 00 to 40 1360(i)
Continuous γ →n
137
Photofission
138
ν·σphotofission
139
νprompt ·σphotofission
140
νdelayed ·σphotofission
141
Other photonuclear interactions
142
Photoneutron production rate
145
Table 13.2: Data file interaction codes for photon (photoatomic and photonuclear) reactions.

<!-- page 199 -->
## 13.3 SUM OF REACTION RATES

It is possible to define a reaction rate as the sum of nb(taux) reaction rates on different nuclei. The syntax
is as follows.
REACTION <PARTICLE_TYPE>
NUCLEI nb(rate)
name(nucleus1)
Additional data
for nucleus 1
name(nucleus2)
Additional data
for nucleus n
The additional data for a given nucleus are COMPOSITION etc., FICTIVE etc. or DATA etc. It is thus possible to
sum the reaction rates of different nuclei. It is also possible to mix the different types of nuclei (FICTIVE for
one nucleus, DATA for another, etc. But care must be exercised as FICTIVE gives microscopic cross-sections
and COMPOSITION gives macroscopic cross-sections, which must not be mixed!).
• It is possible to use NUCLEI 1 instead of NUCLEUS;
• Rather than requesting, for instance:
REACTION NEUTRON
NUCLEI 2
O16 FICTIVE 300 INTERACTION 1 22
O16 FICTIVE 300 INTERACTION 1 23
it is better to write:
REACTION NEUTRON
NUCLEUS
O16 FICTIVE 300 INTERACTION 2 22 23
This is because certain incompatibilities are detected in the second case and not in the first (for instance,
the total cross-section cannot be added to a partial cross-section of the same material, see Tables 13.1
and 13.2).

## 13.4 DATA ADDITIONAL DATA

The keyword DATA introduces a cross-section definition.
Note: The cross-sections are input in the same manner as the tabulated source.
When defining cross-sections, the following information is mandatory:

<!-- page 200 -->
Interpolation mode
Associated code
Histogram
IN_NO_INTERPOLATION
Linear
IN_LIN_LIN
Linear-log
IN_LIN_LOG
Log-linear
IN_LOG_LIN
Log-log
IN_LOG_LOG
Table 13.3: Possible Interpolation Types
• the number of nb(points) pairs defining the cross-sections for the (energy, cross-section) pairs;
• the number of intervals nb(inter) for which it is necessary to specify the type of interpolation (if
two intervals are defined using the same interpolation mode, but they are discontinuous, then they are
counted as two distinct intervals);
• the interpolation modes for the intervals;
• the cross-section values at the given energies.
The modes of interpolation and their codes are given in Table 13.3.
For a histogram input, the cross-section value in a [E(inf),Esup] interval is the one corresponding to
E(inf).
The meanings of the modes of interpolation are as follows (where y is the cross-section data and x the energy):
• IN_NO_INTERPOLATION
y = constant;
• IN_LIN_LIN
y = a∗x+b;
• IN_LIN_LOG
y = a∗log(x)+b;
• IN_LOG_LIN
log(y) = a∗x+b;
• IN_LOG_LOG
log(y) = a∗log(x)+b.
The user must indicate how to make the intervals corresponding to interpolation mode j coincide with the
energies supplied.
Let E(i) be a list of the energies (in MeV) for which the cross-section is known, i varying between 0 and
nb(points)-1. The list, with the cross-section values associated with each energy, must be in increasing order
. After giving the mode of interpolation for interval j, the index of the upper energy limit num[limsup(j)]
is given for this interval (the energy must, of course, belong to the list of E(i) and num[limsup(j)] must be
between 1 and nb(points)-1).

<!-- page 201 -->
• The first interpolation interval extends from E(0) to E{num[limsup(1)]};
• The j-th interpolation interval extends from E{num[limsup(j-1)]} to E{num[limsup(j)]};
• The last interpolation interval extends from E{num[limsup(nbinter-1)]} to
E{num[limsup(nbinter)]} = E[nb(points)-1].
Finally, the (E(i), section(i)) pairs are given, with i varying from 0 to nb(points)-1.
The syntax is as follows:
DATA
nb(points) nb(inter)
<MODE_INTERPOLATION(1)> num[limsup(1)]
...
<MODE_INTERPOLATION(nbinter)> num[limsup(nbinter)]
E0 section0
...
Enb(points)−1 sectionnb(points)−1
A file can also be used. It must contain all of the data of the previous syntax, starting with nb(points). The
syntax is then:
DATA
FILE filename
where filename is the name of the data file.
Example of a cross-section definition given using the keyword DATA
2
4
6
8
10
0
0
10
20
30
40
50
60
70
80
0
1
2
3
4
5
Energy in MeV
cross section in barns
Thus, if the user wishes to define the cross-section shown in the figure above, six points need to be entered:
(0,10), (2,20), (4,50), (6,30), (8,30),(10,10) (nb(points)=6). There are three (nb(inter)=3) interpolation
intervals, i.e., (with number num[limsup(j)] of the last point in bold).

<!-- page 202 -->
• interval [0,4] (from point 0 to point 2), for which linear interpolation between the points is required;
• interval [4,8] (from point 2 to point 4) with histogram interpolation;
• interval [8,10] (from point 4 to point 5) with linear interpolation once again.
This gives:
DATA
6 3
IN_LIN_LIN 2
IN_NO_INTERPOLATION 4
IN_LIN_LIN 5
0.
10.
2.
20.
4.
50.
6.
30.
8.
30.
10.

## 10. 13.5 ADDITIONAL DATA FOR A WEIGHTED CURRENT

It is possible to weight each current tally by a function of the energy, defined by the user. The syntax is as
follows:
WEIGHTED_COURANT <PARTICLE_TYPE>
DATA
Additional data
The command block DATA is the same as for the reaction rates (see section 13.4). Nevertheless, in the (energy,
section) pairs, the “section” here actually refers to any variable weighting the current.
A special case of this kind of response is the calculation of energy balance: for that, the user only has to give
to the “section” variable the same values as for the energy.

## 13.6 MACROSCOPIC REACTION RATES

Sometimes, computing macroscopic reaction rates including several isotopes and reactions might become
cumbersome. For this reason, the response MACROSCOPIC_REACTION_RATE allows the user to compute some
predefined macroscopic reaction rates by direcly averaging over the reactions contributing to the desired rate.
The MACROSCOPIC_REACTION_RATE response is thus a macroscopic reaction rate summing all the isotopes in
a given composition and all the reactions for a specific type.

<!-- page 203 -->
The particle type must be NEUTRON, followed by the desired reaction type: TOTAL (all possible reaction
types), CAPTURE (all non fissile absorptions), TOTAL_FISSION (all fission events), PROMPT_NUSIGF (prompt
neutron production events), DELAYED_NUSIGF (delayed neutron production events), YIELD_SIGMA_N2N (yield
times (n,2n) events), YIELD_SIGMA_N3N (yield times (n,3n) events) YIELD_SIGMA_N4N (yield times (n,4n)
events).
WARNING ! The user is advised not to use macroscopic reaction rates in very diluted media or with very thin
volumes (fission chambers, homogenized materials of very small volumes). In these cases, the collision-based
estimator for macroscopic reaction rates might display a slow convergence, and the user should preferentially
use the standard method to calculate reaction rates, as given in Sec. 13.2.

## 13.7 DEPOSITED ENERGY

This response computes the Kinetic Energy Release in MAtter (KERMA), i.e., the energy ED deposited by
charged particles (emitted following collisions induced by a given particle type) in the traversed medium.
The particle type following the keyword DEPOSITED_ENERGY can be NEUTRON, PHOTON, ELECTRON or
POSITRON: this defines the particle that is responsible for a specific contribution to the energy deposition.
The deposited energy ED depends on whether other particles than the requested particle type are simulated:
by convention, it is assumed that, if a particle is transported, its associated energy is subtracted from the
energy balance, since it will be deposited elsewhere. On the contrary, if a particle is not simulated, its energy
is assumed to be deposited locally at the collision event. For instance, when the particle type is NEUTRON,
• in pure neutron tranport, the energy carried by the photons emitted in nuclear reactions is assumed to be
deposited locally the reaction event: ED = Eneutron
D
• in coupled neutron-photon tranport, the energy carried by the photons emitted in a given reaction is
subtracted from the energy balance: ED = Eneutron
D
−E photon
D
.
If electrons and positrons are not simulated, their energy is analogously assumed to be deposited locally (this
energy is usually smaller than that of neutrons or photons). For photon energy deposition, only the sum of
the energies deposited by PHOTON, ELECTRON and POSITRON is meaningful.
When photons are transported, by default only photoatomic reactions contribute to the calculation of deposited
energy. The user may be interested in including the contribution of photonuclear reactions to deposited
energy: this is achieved by the use of the keyword PHOTO_NUCLEAR in the SIMULATION block.
For scores associated with the DEPOSITED_ENERGY response function, it is important to note that the energy
grid associated with the energy deposition response function corresponds to the energy of the incident particle
inducing the reaction. Therefore, the deposited energy varies as a function of the energy of the incident
particle.

### 13.7.1 REACTION Q-VALUES FOR ENERGY DEPOSITION

The nuclear reaction Q-values (other than fission or photofission Q-values) are by default computed (from
mass differences) by reading in the file giving the atomic weights of the nuclei. For some isotopes, however,
this is not possible (or leads to wrong results): this is the case for

<!-- page 204 -->
• (n,2n) reaction of 9Be: this leads to a resonant nucleus 8Be that immediately decays to 2α. For a proper
calculation of the deposited energy, the associated Q-value must be read in the evaluation file
• the Q-values of metastable nuclei (e.g., 110MAg) can not be computed based on mass differences and
must be read in the evaluation file
• the Q-values of natural elements (e.g., C −NAT) can not be computed based on mass differences and
must be read in the evaluation file.
For (n,2n) reaction of 9Be, the user can resort to the dictionary file and specify a Q-value flag 2 so as to read
the reaction Q-value in the evaluation file (see chapter 3). This is the option by default in the dictionary file.
Analogously, for metastable isotopes, the user can resort to the dictionary file and specify a Q-value flag 1
so as to read the reaction Q-values in the evaluation file (see chapter 3). This is the option by default in the
dictionary file. Finally, for natural elements, TRIPOLI-4® reads the Q-values in the evaluation file.

### 13.7.2 FISSION ENERGY

For neutron-induced fission, we adopt the convention that in SHIELDING mode the secondary fission neutrons
(prompt and delayed) are not transported, so that their energy is assumed to be deposited locally, whereas in
FIXED_SOURCES_CRITICALITY or CRITICALITY the secondary neutrons are transported and their energy is
therefore subtracted from the energy balance.
By default, the fission energy is given by the sum of prompt and delayed contributions, so as to preserve the
same conventions as in TRIPOLI-4® version 7.
Finally, the user interested in computing the fission energy alone can do so by resorting to the optional
keyword FROM_FISSION in the response DEPOSITED_ENERGY. This keyword can be used in addition to either
ONLY_PROMPT_ENERGY, ONLY_PROMPT_GAMMA_ENERGY, or RESCALE_DELAYED_FISSION_PHOTONS, that are
global options of the SIMULATION block (see Sec. 22).
Neutron-induced fission Q-values are by default read in the file giving the energies released by fissile isotopes
during fission for the different particles emitted (see chapter 3). If this information is missing, to perform
a deposited energy calculation the user must provide himself a fission Q-value (in MeV) for the isotope.
For photofissions (if any) a photofission Q-value must be provided as well to perform a deposited energy
calculation when the keyword PHOTO_NUCLEAR is specified in the SIMULATION block. This is achieved by
resorting to a separate block in the form
This block can be placed at any position in the input file. Here NEUTRON is the keyword that defines neutroninduced
fissions, and nb_isotopes_for_neutron_induced_fissions is the number of isotopes for which fission
energy is provided by the user. Then, isotopei is the name of the ith isotope and fission_energyi is the
corresponding fission energy in MeV. Analogously, PHOTON is the keyword that defines photofissions, and
nb_isotopes_for_photofissions is the number of isotopes for which photofission energy is provided by the
user. In absence of precise information, a fission (or photofission) Q-value of 200MeV should provide a
rough order-of-magnitude of the energy release in matter.

<!-- page 205 -->
QFISSION
NEUTRON nb_isotopes_for_neutron_induced_fissions
isotope1 fission_energy1
isotope2 fission_energy2
...
PHOTON nb_isotopes_for_photofissions
isotope1 fission_energy1
isotope2 fission_energy2
...
END_QFISSION

## 13.8 KINEMATIC LIMITS

The response KINEMATIC_LIMITS is provided to guide the user in the estimation of the deposited energy in
specific coupled neutron-photon calculations. When the user demands the energy deposited by neutrons in
such coupled calculations, the energy carried away from photons is subtracted, so that two major problems
may arise: first, the quantity to be estimated is generally affected by large fluctuations (which stems from
being basically the difference between the available energy, E +Q, and the energy of the photons, which are
usually of comparable order of magnitude); second, inconsistencies in the nuclear data libraries may become
more apparent in this configuration, since energy or momentum balance errors (typically in the secondary
photon productions) are emphasized when taking these differences. The KINEMATIC_LIMITS response allows
the users to compute the energy deposited by neutrons in coupled neutron-photon calculations without
actually having to simulate photons, based on the laws of kinematics: as such, this response may
• provide a robust estimation of the deposited energy, only minimally dependent on nuclear data
• serve as a tool for nuclear data analysis/verification.
In the former case, the user computes kinematic limits as an alternative to the DEPOSITED_ENERGY response
in a coupled neutron-photon transport, which is based on energy balance and thus dependent on nuclear data
libraries. In the latter, a comparison between the KINEMATIC_LIMITS and the DEPOSITED_ENERGY responses
(on the very same configuration) provides the user with test of consistency of the nuclear data library under
examination.
The particle type must be NEUTRON, and it must be followed by the kinematic limit type, which is
UPPER_LIMIT (upper boundary) or LOWER_LIMIT (lower boundary). The basic coherence verification is
that the DEPOSITED_ENERGY response for neutrons in a coupled neutron-photon transport lies above the
LOWER_LIMIT and below the UPPER_LIMIT of the KINEMATIC_LIMITS response. Whenever these boundaries
are not respected, the deposited energy response obtained from DEPOSITED_ENERGY in coupled neutronphoton
transport might become questionable because of possible inconsistencies in nuclear data libraries.
Remark that these constraints hold only for the responses as a function of the incident neutron energy, and do
not generally apply also to energy-integrated values. Observe that KINEMATIC_LIMITS depends only on neutron
transport parameters, and this response will be the same whether neutron only or neutrons and photons

<!-- page 206 -->
are simulated: we stress that KINEMATIC_LIMITS yields the energy deposited by neutrons as if photons were
transported.
For scores associated with the KINEMATIC_LIMITS response function, it is important to note that the energy
grid associated with the KINEMATIC_LIMITS response corresponds to the neutron incident energy, exactly as
in the case of DEPOSITED_ENERGY.
The (n,2n) reaction of 9Be leads to a resonant nucleus 8Be that immediately decays to 2α. For a proper
calculation of the kinematic limit, the user can resort to the dictionary file and specify a Q-value flag 2 so
as to read the reaction Q-value in the evaluation file and at the same time adopt special kinematics for this
reaction (see chapter 3). This is the option by default in the dictionary file.

## 13.9 DPA

This response computes the number of displaced atoms per unit time (DPA), in agreement with the specifications
in the HEATR module of the NJOY code [36, 35]. The available energy Ea per unit time, i.e., the
energy that is available to create an atomic displacement is computed via the model proposed by Norgett,
Robinson and Torrens (NRT). The NRT model roughly says that Ea is proportional to the primary knoked-on
atom (PKA) energy, and has a nonlinear saturation at higher energies.
DPA response is meaningful only for neutrons. If coupled neutron-photon calculations are performed, the
response will be the same as in the case of a pure neutron transport: photonuclear reactions are ignored. The
effects of (n,γ) reactions are nonetheless taken into account through the residual nucleus recoil energy.
The particle type following the keyword DPA must be NUCLEUS.
For DPA calculations, the user must specify the displacement (threshold) energies Ed associated to any material
composition for which a DPA is requested. In its simplest definition (linear response), the DPA response is an
available energy Ea per unit time, divided by 2Ed : the result
DPA = Ea
2Ed
(13.1)
carries therefore the units of (displaced atoms)/s.
The displacement energies Ed (in MeV) must be provided with a separate block in the form
DISPLACEMENT_ENERGY
COMP1 nb_isotopes_for_comp1
isotope1 displacement_energy1
isotope2 displacement_energy2
...
COMPN nb_isotopes_for_compN
isotope1 displacement_energy1
isotope2 displacement_energy2
...
END_DISPLACEMENT_ENERGY

<!-- page 207 -->
This block can be placed at any position in the input file. Here COMPi is the name of the ith composition,
and nb_isotopes_for_compi is the number of isotopes for this composition for which a displacement energy
is provided; then, isotopei is the name of the ith isotope, and displacement_energyi is the corresponding
displacement energy in MeV. If, for a given isotope of a composition for which a DPA is requested, the
displacement energy Ed is not given, it is assumed that this isotope does not contribute to the creation of
displacements.
Element
Ed [eV]
Element
Ed [eV]
C graphite
28-31
C diamond
80
Si
11-22
Ge
12-30
GaAs
9 (Ga) 9 (As)
ZnS
10 (Zn) 15 (S)
CdS
7 (Cd) 9 (S)
Cu
19-29
Al
19-27
Ni
23-33
Pt
33-44
SiC
45-90
MgO
64 (Mg) 60 (O)
Al2O3
18 (Al) 76 (O)
MgAl2O4
56 (O)
ZnO
40 (Zn) 57 (O)
UO2
40 (U) 20 (O)
BeO
76 (O)
Fe
17-44
Mo
33-65
Zn
19-29
Au
35-49
Be
31
Co
40
Mg
25
Zr
40
Nb
40
Ca
40
V
40
Ta
90
Cr
40
W
90
Mn
40
Pb
25
Table 13.4: Typical values for displacement energies Ed.
A modified saturation function for DPA calculations can be obtained by resorting to the optional keyword
KINCHIN_PEASE_MODEL, following which the modified Kinchin Pease model is applied instead of the linear
response defined above: in this case, the number of displacements per atom is defined as
• DPA = 0 for Ea < Ed,
• DPA = 1 for Ea < 2.5Ed,
• DPA = 0.8Ea/(2Ed) otherwise.
Typical values of the displacement energies Ed are given in Table 13.4 (we refer the reader to the HEATR
documentation for more information [35, 36]). In absence of precise information, a displacement energy of
Ed = 25·10−6MeV should provide a rough order-of-magnitude for performing DPA calculations.
The (n,2n) reaction of 9Be leads to a resonant nucleus 8Be that immediately decays to 2α. For a proper
calculation of the DPA, the user can resort to the dictionary file and specify a Q-value flag 2 so as to read
the reaction Q-value in the evaluation file and at the same time adopt special kinematics for this reaction (see
chapter 3). This is the option by default in the dictionary file.
For scores associated with the DPA response function, it is important to note that the energy grid associated
with the DPA response corresponds to the neutron incident energy. Therefore, DPA vary as a function of the
energy of the incident neutron.

<!-- page 208 -->
By default, the DPA response is summed over all atoms in the composition, and carries the units of total
displacements in the volume (per unit time). The optional keyword NORMALIZE_TO_ONE_ATOM can be used
to express DPA in units of displacements per atom (per unit time), by normalizing to the number density in
the volume.

## 13.10 GAS PRODUCTION

The production of light particles (the isotopes of hydrogen and helium, also called gas particles) may affect the
structural properties of traversed materials, and are of utmost importance for radiation shielding (especially
in the case of tritium). The GAS_PRODUCTION response allows the user to compute the production rate of
such particles, coming from neutron and photon contributions. In both cases, we consider direct reactions (a
gas particle in the exit reaction channel) as well as indirect reactions (the gas particle is the recoil nucleus
itself: this happens only for light target nuclei). Photons can induce gas production only via photonuclear
reactions, which demand the optional PHOTO_NUCLEAR keyword in the SIMULATION block; otherwise, the gas
production rate from photon reactions will be zero.
The particle type following the keyword GAS_PRODUCTION must be NEUTRON or PHOTON. The user can specify
the gas particle type by using the keyword: NEUTRON (1H), DEUTERON (2H), TRITON (3H), HELIUM (3He), or
ALPHA (4He).
For fissile nuclei, gas production typically comes from ternary fission leading to light nuclei: special nuclear
data for ternary fission (MF8, MT454) have been included in the Q-fission folder for convenience.
The (n,2n) reaction of 9Be leads to a resonant nucleus 8Be that immediately decays to 2α. For a proper
calculation of the gas production, the user can resort to the dictionary file and specify a Q-value flag 2 so as
to adopt special kinematics for this reaction (see chapter 3). This is the option by default in the dictionary
file.
For scores associated with the GAS_PRODUCTION response function, it is important to note that the energy
grid associated with the GAS_PRODUCTION response corresponds to the neutron or photon incident energy.
Therefore, the gas production varies as a function of the energy of the incident particle.

## 13.11 FISSION SPECTRUM

The response FISSION_SPECTRUM allows the user to compute the fission energy spectrum, averaged over
all isotopes in a given composition. The particle type following the keyword FISSION_SPECTRUM must be
NEUTRON. The kind of desired spectrum is to be defined by the user: available keywords are TOTAL (sum of
prompt and delayed contributions), PROMPT (only prompt component) and DELAYED (only delayed component
). The integral of the TOTAL sums up to the PROMPT plus DELAYED components. Moreover, the integral
PROMPT component equals the total prompt β (prompt from prompt plus prompt from delayed), whereas the
integral DELAYED component equals the total delayed β (delayed from prompt plus delayed from delayed).
Prompt and delayed components are expressed in units of [105 pcm]. See the section 22.6 for more details
about effective-β calculations.

<!-- page 209 -->
## 13.12 FIXED SOURCE EMISSION

The response FIXED_SOURCE_EMISSION enables to check the energy and/or angle source distribution as simulated
by the code (the associated energy and/or angle grids have to be defined in the GRID_LIST command
block, see chapter 14). This response is available for fixed source simulations only. The origin of the delivered
information differs from the source normalization information given in the results file at the end of
the initialization step : the information delivered by the present response is collected by an estimation calculated
from the real sampling of source particles during the simulation. When source biasing options are
used (see subsections 12.3.4 and 12.4.7), this response allows the user to check the resulting simulated source
distribution. The syntax is as follows:
FIXED_SOURCE_EMISSION <particle_type> <mode>
where <particle_type> is the particle type and <mode> is either DENSITY or FREQUENCY.
When the keyword DENSITY is chosen, the distribution of the sampled source is estimated. The mean value
can be compared with the source norm, as given by the code in the initialization step (and output in the results
file as "SIMULATION INTENSITY"). If no variance reduction technique and no source biasing is used, the
variance of the score associated to this response is null.
When the keyword FREQUENCY is chosen, the information delivered is the frequency of the sampling and
enables to check for example that certain energy groups enhanced by the user through a source energy biasing
(see subsection 12.4.7) are sampled more frequently. If no variance reduction technique and no source
biasing is used, both options DENSITY and FREQUENCY are equivalent. Otherwise the mean value of the score
associated with the FREQUENCY option response can be compared with the biased source norm, as given by
the code in the initialization step (and output in the results file as "BIASED SIMULATION INTENSITY").

## 13.13 DEPOSITED CHARGE

The DEPOSITED_CHARGE response is used to calculate the spectrum of charge deposition in a given volume.
Note that this makes sense only if charged particles (ELECTRON and POSITRON) are transported at all; no
charge deposition can occur otherwise.
The particle type for this response must be ATOM.
For scores based on the DEPOSITED_CHARGE response function, the associated grid has the meaning of chargedeposition
grid. Therefore, if one wishes to estimate the average deposited charge in a given volume, the grid
must span negative and positive values, or else the final result will be biased. It is recommended to use unit
bins centered on integer values.
In addition, each bin of the resulting histogram contains the product of the charge deposition frequency and
the bin charge. Specifically, if a bin ranging from −2.5 to −1.5 contains a score result of −0.6 charge/(cm3
source), it means that the simulation resulted in a −2 charge deposition in 30% of the histories (assuming unit
volume for the sake of simplicity). This is done so that the average charge deposition can be straightforwardly
calculated as the integral of the histogram. The average values are available for the user in the score output.
Note also that the “score/lethargy” output values have no meaning for this response.
Finally, note that charged source particles are not tallied by this response function.

<!-- page 210 -->
## 13.14 SPECIAL OPTION TO EXCEPT A PART OF THE CONTRIBUTION FOR SECONDARY PARTICLES

For a given response, the user has the possibility to except the tally contributions of secondary particles
produced by certain interactions (for example the user can request a photon response in a coupled neutrongamma
simulation with a neutron source, excepting the contribution of the photons produced by fission).
Note that those secondary particles are nevertheless simulated and can contribute to other tallies for which
this option is not activated. The syntax in the RESPONSES command block for the current response is:
<response_type> <particle_type> <additional_data>
#
NOT_INDUCED_BY_INTERACTION nb(interactions) code_1 ... code_n
#
INDUCED_BY_INTERACTION nb(interactions) code_1 ... code_n
where the nb(interactions) interaction codes are chosen among those listed in Tables 13.1 and 13.2.
When the keyword NOT_INDUCED_BY_INTERACTION is chosen, the secondary contributions of the following
interactions are excepted, whereas when the keyword INDUCED_BY_INTERACTION is chosen, secondary contributions
are taken into account only for the interactions mentioned.
Possible particle types are NEUTRON and PHOTON.
Calculations in several steps are not compatible with this option (e.g. KEEP_RESULT option, Green function
files, collision files, source files ...).
Response definition (optional) for the criticality calculation example
of chapter 5
RESPONSES 4
NAME FLUX_NEUTRON
FLUX NEUTRON
NAME U238_TOTAL_REACTION_RATE_NEUTRON
REACTION NEUTRON
NUCLEUS U238 COMPOSITION SOLUTION_U
INTERACTION 1 104
NAME O16_TOTAL_REACTION_RATE_NEUTRON
REACTION NEUTRON
NUCLEI 2
O16 FICTIVE 300 INTERACTION 1 22
O16 FICTIVE 300 INTERACTION 1 23
NAME BIDON_REACTION_RATE_NEUTRON

<!-- page 211 -->
REACTION NEUTRON
NUCLEUS BIDON
DATA
6 3
IN_LIN_LIN 2
IN_NO_INTERPOLATION 4
IN_LIN_LIN 5
0.
10.
2.
20.
4.
50.
6.
30.
8.
30.
10.
10.
END_RESPONSES
