# DEFINING NUMERICAL SIMULATION PARAMETERS
<!-- source PDF pages 287-329 -->

<!-- page 287 -->
Chapter 22
DEFINING NUMERICAL SIMULATION
PARAMETERS
Simulation parameters are defined between the keywords SIMULATION and END_SIMULATION.
This section of the TRIPOLI-4® data relates to the simulation phase itself and allows for the simulation
parameters to be defined.

## 22.1 SIMULATION PARAMETERS

Some parameters must be specified (see syntax in section 22.2):
• the number of batches ;
• the number of particles per batch ;
• the type of particles to be tracked (NEUTRON, PHOTON, ELECTRON and POSITRON).
Other parameters are optional:
• the simulation mode: radiation shielding, criticality, fixed-source sub-criticality, multiple, critical parameter
search or adjoint criticality (default: SHIELDING). It should be noted that prompt fission
gamma are simulated for all problem types, including radiation shielding, whenever photons are tracked.
For further details on the multiple simulation mode, see Section 22.19.
• DISCARD <n>, used in criticality mode (and for the critical parameter search), allows the code to discard
n batches in the calculation of scores (only for the scores associated with responses like flux, reaction
rates,..., but not for keff). For the keff, an automatic convergence is used. The optimal number of
batches to discard in order to satisfy the convergence criteria is calculated, even if the keyword DISCARD
is present (see complements in section 33.4).
• it is possible to request convergence to a given precision, over a part of the score.
In this case,
CONVERGENCE 0.05 0.80 means that convergence is required for the scores at 5%, over 80% of the
score integrated over the entire energy domain. For instance, in the case of a grid with three groups,

<!-- page 288 -->
two fast and one thermal, if the fast groups have results with standard deviations of 2% and 4% but the
thermal group has results with a standard deviation of 20%, it may be due to the fact that the fast groups
are substantially more important for that particular score. In this case, if they represent more than 80%
of the total score, the code will stop as it considers that convergence has been achieved (each fast group
must have converged). This presentation applies to as many groups as there are in the grid. It must be
noted that the code does not check that the groups are contiguous. Furthermore, a score of zero with a
standard deviation of zero is considered not to have converged: it is, therefore, important not to use a
convergence request if the score or standard deviation is expected to be zero (which can occur with void
media). The code stops when convergence is achieved, or when the total number of batches is reached
(a large batch number must, therefore, be given).
• PACKET_LENGTH <n> allows the code to average n batches in a packet before averaging again or sending
the value to the collector. This leads to several advantages.
– Used in parallelism, it considerably reduces the amount of communications and can therefore improve
the performance of parallelism runs.
– For performance purpose, the user should request as big as possible batches. Nevertheless, large
batches in criticality calculations lead to a longer source convergence phase. The PACKET_LENGTH
option allows then both constraints to be satisfied.
– In some cases of criticality calculations, the estimation of the variance is improved. This is especially
the case if there are strong inter-cycle correlations. [39, 43, 93]
• The EDITION keyword defines the frequency of output results. The default is every 100 batches.
• The MESH_EDITION keyword defines the frequency of mesh output results. This option is useful to
prevent too large mesh outputs. The default is the EDITION value, otherwise MESH_EDITION must be a
multiple of EDITION.
• The SUPPRESS_MESH_EDITION_TEXT keyword allows the user to suppress the edition of mesh results in
TRIPOLI-4® listing results file only. The VTK, MED and ASCII files are normally filled. This option is
useful to prevent too large TRIPOLI-4® listing results files while keeping other outputs.
• lower energy and upper energy for the simulation of each particle type (default: Einf(neutron) =
10−11 MeV, Esup(neutron)= 20 MeV, Einf(photon) = 10−3 MeV, Esup(photon) = 20 MeV. For
electrons and positrons:
Einf = 10−3 MeV, Esup = 20 MeV). Warning: for neutrons, electrons and
positrons the kinetic energy must be given;
• for a time dependent problem only : lower time and upper time for the simulation of each particle type
(default: Tinf = 0 s, Tsup = 1035 s for neutrons, photons, electrons and positrons).
• storing of the results of each batch (default: not stored);
• biasing of collision if a variance reduction technique is specified (default: no biasing);
• integration of the path (default: no integration);

<!-- page 289 -->
• monitoring: in shielding mode, 500 particles are simulated in the first batch (instead of a number of
particles set by SIZE, kept for the following batches) and, in case of variance reduction usage, a fine
improvement of the importance map is performed by using statistical information from the simulation
of the first 5 batches (default: monitoring, see also section 22.2 to deactivate this option);
• for a criticality problem (or a critical parameter search), the number of batches not to be retained (default
: automatic).
• it is possible to obtain the Kij fission matrix using the KIJ_MATRIX option.
• it is possible to activate photonuclear reactions using the PHOTO_NUCLEAR option. In this case the
PHOTONUCLEAR_ROULETTE option of the present command block should also be used in conjunction, so
as to lower the default threshold of the Russian roulette for neutrons produced by photonuclear reactions
only (in order to deal with very low simulation weights of photoneutrons). The RUSSIAN_ROULETTE
keyword can be used together for all other neutrons.
• VOLUMIC_SCORES can be used when all scores are volumic (based on TRACK or COLL estimator) to
speed-up the calculation of scores. It may be very efficient when using more than 1000 scores and/or
responses. The potential gain can simply be estimated by running two short simulations: one without
any scores, and another one with all the needed scores. If they yield very different simulation times, then
the keyword VOLUMIC_SCORES may be of some use. This option is now enabled by default. If needed it
can be disabled by using the keyword DISABLE_VOLUMIC_SCORES.
• GLOBAL_SCORES
can be used to calculate the following responses: Production, Absorption, Leakage,
NXN excess, Total flux. Such scores are the sum of these responses on the whole geometry.
• with EPITHERMAL_BROADENING it is possible to activate user-defined models for the Doppler broadening
of the elastic scattering kernel in the epithermal range (1 eV - 1 keV): see section 22.13
• the RUSSIAN_ROULETTE option enables to change the default simulation weight threshold of 0.8 (under
which the Russian roulette is played). This option is available when no variance reduction command
block is present in the input deck. The user may also refer to the Russian roulette control option defined
for neutrons only in subsection 17.6.3.
• the PHOTONUCLEAR_ROULETTE option enables to change the default simulation weight threshold of 0.8
(under which the Russian roulette is played) only for neutrons produced by photonuclear reactions.
• the MAX_SPLITTING_PARTICLE_NUMBER option enables to limit the number of split particles to an integer
N during each splitting operation. When a TRACK estimator is requested on an extended mesh
together with the standard Exponential Transform variance reduction method of TRIPOLI-4®, N has to
be set to 1 (see Section 15.8.3). When used together with weight windows, N can be changed by the
user, the default value being 1000 (see Section 19.4).
• the ABORT_ON_LEAKAGE option enables to stop the calculation if too many neutrons leak out of the
geometry. Once the limit is reached, the calculation is stopped (in parallel mode the limit is to be
reached for each simulator).

<!-- page 290 -->
• the FORCED_UNIT_BASE_INTERPOL option enables to force the unit-base interpolation type on nuclear
data for outgoing particle energy sampling. This is equivalent to the choice made by default by the MCNP
code.
• the INELASTIC_THRESHOLD_CORRECTION option enables to correct the threshold of neutron discrete
inelastic scattering reactions: with this keyword, the threshold taken into account by the code is -QI of
the considered inelastic level, instead of the reaction threshold taken from the evaluated data (but kept
as default option).
• the ANALOG option enables to perform a fully analog simulation (regarding collisions and transport between
collisions). It cannot be used with criticality calculations and only NEUTRON or PHOTON are allowed
as particle type for this option (but both cannot be used together since analog photon production induced
by neutron interactions is not available yet). Note that in case of electromagnetic shower simulations,
photon transport is already analog, hence the ANALOG option does not need to be added.
• the FISSION_MODEL option enables to simulate analog fission by sampling a full fission neutron multiplicity
distribution. It allows addressing time nuclear instrumentation applications needing detailed
correlations between neutrons of fission chains. Since useful data for this fission sampling are not provided
by the standard nuclear data librairies (which provide averaged neutron multiplicities only), this
option activates a coupling between TRIPOLI-4® and an external fission model code. Two fission models
are available as fission model type: LLNL_FISSION and FIFRELIN.
The LLNL_FISSION option gives access to the event-by-event FREYA fission model which is directly
called by TRIPOLI-4®.
Downloading of the LLNL Fission Library package version 2.0.5
(http://nuclear.llnl.gov/simulation/) is required to perform such simulations. Note that for spontaneous
fission an external source can be used, that directly calls FREYA (see Section 12.8).
The FIFRELIN option has to be used with specific event files produced by FIFRELIN code [72] for a
given nuclide concerned with induced fission. The FIFRELIN keyword has then to be followed by:
– the za number of this isotope (where za = 1000∗Z +A)
– the USE_FILE keyword, the format number (1 for the n-γ uncoupled mode, 2 for the n-γ coupled
mode without angular data and 3 for the n-γ coupled mode with angular data)
– the number of files (integer n)
– the n absolute paths to these files.
It should be noted that a FIFRELIN event file is valid for a given energy domain only. For spontaneous
fission, a specific keyword SPONTANEOUS_FISSION has to be used in the SOURCE command block (see
Section 12.12).
Whatever the fission model is, detailed information on simulated fission neutrons is then available
through the ROOT TRACKS options of TRIPOLI-4®: see section 36.3. It should be noted that for the
time being, this coupling has not been fully validated, results are thus not guaranteed and should be
handled for R&D purposes only.
It can be useful, when using a fission model, to change the upper bound of energy accepted in the fission
energy sampling with the keyword FISSION_ENERGY_SUP followed by the appropriate energy value (by
default, this upper bound is the upper energy of the simulation).

<!-- page 291 -->
• Un-weighted and adjoint-weighted kinetics parameters can be computed in criticality calculations: see
Sec. 22.6.
• The neutron importance function (the adjoint fundamental mode) can be computed by using the keyword
ADJOINT_CRITICALITY: see Sec. 22.7.
• Special simulation modes are available so as to determine some adjustable parameters (albedo boundary
conditions and Boron concentration) that make the system exactly critical: see Sec. 22.8.
• The users interested in computing only the prompt fission energy contribution to deposited energy
(which is for instance the choice in the HEATR module of the NJOY code [36, 35]) can resort to the
following additional optional keywords. With ONLY_PROMPT_ENERGY, delayed beta and delayed gamma
contributions are subtracted from the fission Q-value; with ONLY_PROMPT_GAMMA_ENERGY, delayed beta
energy is deposited locally, whereas delayed gamma contribution is subtracted from the fission Q-value
(i.e. it is neglected). These keywords are mutually exclusive. An alternative treatment of delayed fission
photons is possible with the the RESCALE_DELAYED_FISSION_PHOTONS keyword, which activates transport
of delayed fission photons under the assumption that their spectrum is the same as the spectrum of
prompt photons. The RESCALE_DELAYED_FISSION_PHOTONS and ONLY_PROMPT_GAMMA_ENERGY keywords
are mutually exclusive.
An important remark is due: when the user demands only prompt neutrons to be transported, via the
PROMPT_FISSION_ONLY keyword in the SIMULATION block, all delayed contributions to the deposited
energy are ignored to preserve coherence. See Sec. 13.7.2 for further details.
• If needed, it is possible to normalise the average number of fission neutrons (¯ν) by a coefficient (typically
the keff coming from a preliminary criticality calculation). This is achieved by using the keyword
RESCALE_NU_BY_KEFF followed by COEFF and the value of the coefficient by which we want to divide
¯ν.
• Calculation of the global slowing down current integrated over the geometry is available via the
SLOWING_DOWN_CURRENT keyword: see Sec. 22.9 for further details.
• The reactor physics parameters appearing in the six factor formula can be computed in criticality calculation
via the SIX_FACTOR_FORMULA keyword: see Sec. 22.10.
• The migration area can be computed in criticality calculations: see Sec. 22.6.
• The Diven dispersion factor can be computed in criticality calculations: see Sec. 22.11.
• If the simulation involves nuclide temperatures that are not available in the neutron nuclear data library,
the user has the possibility to request a temperature interpolation between the two nearest temperatures
available in the library. A stochastic interpolation of the neutron cross-sections is then performed during
the simulation. The related keyword is TEMPERATURE_INTERPOL, followed by the type of interpolation,
which can be either LINEAR (for linear interpolation) or SQRT (for square root interpolation). For version
12 of the code, the current usage restrictions are the following: stochastic temperature interpolation
cannot be used together with analog transport, perturbations, microscopic multigroup transport (GENDF
format), special outputs of cross-sections or nuclei information, SPEED_UP simulation option and adjoint

<!-- page 292 -->
IFP. It is recalled that integer values must be given by the user when defining the material temperatures
(see Chapter 10) and the temperatures for reaction rates on fictive nuclides (see Section 13.2). It should
also be noted that the speed up option (see Section 2.2) is deactivated when using the temperature
interpolation option (no unionized energy-grid is used).
• The SUPER_HISTORY keyword allows to trigger the Super-History method when performing a
CRITICALITY calculation (see Section 22.17).
• The WIELANDT_METHOD keyword allows to trigger the Wielandt simulation method when performing a
CRITICALITY calculation. This keyword is followed by one of the options CONSTANT, DEFAULT, LINEAR
or USER (see Section 22.18).
• The
particle
histories
can
be
stopped
at
the
k-th
collision
by
using
the
keyword
KTH_COLLISION_SOURCE, with the number of collisions as a free parameter.
The syntax is as
follows: KTH_COLLISION_SOURCE NB_COLLISION <Collision_order>. This option allows computing
the partial contribution to the scores up to the k-th collision source. Setting <collision_order> can be
helpful to compute un-collided, first-collision, second-collision, ···, scores (flux, reaction rates, etc.)
for neutrons and photons.
All the calculation parameter keywords are read by the code in a non-specific order, except for the command
indicating the number of batches to be discarded, which, since it is valid only for a criticality calculation (or
critical parameter searches), requires prior definition of the type of problem.

## 22.2 SYNTAX

The simulation data syntax is as follows, from keyword SIMULATION to keyword END_SIMULATION :

<!-- page 293 -->
SIMULATION
/// Statistics
BATCH nb(batches)
EDITION frequency
SIZE nb(particles per batch)
CONVERGENCE precision factor
PACKET_LENGTH nb(batches per packet)
KEEP_RESULT
RANDOM Additional data
/// Particle energy domains
PARTICLE nb(types of particles) <TYPE_OF_PARTICLES>
ENERGY_INF <TYPE_OF_PARTICLES 1> Ein f (1)
ENERGY_SUP <TYPE_OF_PARTICLES 1> Esup(1)
TIME_INF <TYPE_OF_PARTICLES 1> Tin f (1)
TIME_SUP <TYPE_OF_PARTICLES 1> Tsup(1)
...
ENERGY_INF <TYPE_OF_PARTICLES n> Ein f (n)
ENERGY_SUP <TYPE_OF_PARTICLES n> Esup(n)
TIME_INF <TYPE_OF_PARTICLES n> Tin f (n)
TIME_SUP <TYPE_OF_PARTICLES n> Tsup(n)
/// Mesh related keyword
MESH_EDITION mesh_frequency
SUPPRESS_MESH_EDITION_TEXT
/// XML related keyword
XML_EXPORT
XML_NOCOMPLETE
SERMA_XML_EXPORT
/// Transport modes and options
#
SHIELDING
#
CRITICALITY
DISCARD nb(batches to be eliminated)
#
FIXED_SOURCES_CRITICALITY
#
MULTIPLE
#
ADJOINT_CRITICALITY Additional data
#
ALBEDO_SEARCH Additional data
#
CRITICAL_BORON_SEARCH Additional data
#
DYNAMIC Additional data

<!-- page 294 -->
MONITORING 0
TRANSPORT_BIASING
*
CROSS_SPLIT
*
QUOTA_SAMPLING
COLLISION 1 Einf (coll)
RUSSIAN_ROULETTE threshold
PHOTONUCLEAR_ROULETTE threshold’
MAX_SPLITTING_PARTICLE_NUMBER <N>
ABORT_ON_LEAKAGE limit
FORCED_UNIT_BASE_INTERPOL
INELASTIC_THRESHOLD_CORRECTION
ANALOG <TYPE_OF_PARTICLES>
FISSION_MODEL <TYPE>
FISSION_ENERGY_SUP Esup(fiss)
WIELANDT_METHOD Additional data
SUPER_HISTORY Additional data
/// Special scores or transport options
DISABLE_VOLUMIC_SCORES
GLOBAL_SCORES
KIJ_MATRIX
KINETIC_PARAMETERS
IFP_KINETIC_PARAMETERS Additional data
NAUCHI_KINETIC_PARAMETERS
DIVEN_DISPERSION_FACTOR Additional data
PROMPT_FISSION_ONLY
ONLY_PROMPT_GAMMA_ENERGY
ONLY_PROMPT_ENERGY
RESCALE_DELAYED_FISSION_PHOTONS
RESCALE_NU_BY_KEFF Additional data
SLOWING_DOWN_CURRENT Additional data
EPITHERMAL_BROADENING Additional data
ALL_COLLIDED_FLUX_PT_POINTS
SIX_FACTOR_FORMULA Additional data
TEMPERATURE_INTERPOL <TYPE>
KTH_COLLISION_SOURCE NB_COLLISION Collision_order

<!-- page 295 -->
/// EM Cascade
PHOTO_NUCLEAR
PHOTON_NEUTRON_RATIO Additional data
ELECTRON_INELASTIC_CUTOFF Ec
ELECTRON_BREMS_CUTOFF Ec
THICK_TARGET_BREMSSTRAHLUNG
NO_ELECTRON_MULTIPLE_SCATTERING
ELECTRON_TOTAL_STOPPING_POWER
ELECTRON_PHOTON_BALANCE
NO_ANOMALOUS_SCATTERING_FACTOR
ELECTRON_MIN_STEP_LENGTH step
/// particle event files
STORE_SOURCES_IN_FILE
STORE_COLLISIONS_IN_FILE
STORE_LEAKAGE_IN_FILE
/// Debug features
#
HOLE_COUNT
#
HOLE_MAP
#
HOLE_VOLU_MAP
LAMBDA_HOLE lambda_hole
END_SIMULATION
Monitoring is enabled by default in shielding mode, which automatically results in simulating 500 particles
in the first batch of a shielding calculation. In this case, the total number of simulated particles is
nb(batches)-1 multiplied by nb(particles per batch) plus 500. To deactivate the monitoring option,
see at the end of this section.
<TYPE_OF_PARTICLES> may have the following values:
• NEUTRON and/or PHOTON and/or ELECTRON and POSITRON, depending on the value of nb(types of
particles), which can range from 1 to 4.
To activate the PHOTO_NUCLEAR option, at least PHOTON and NEUTRON types must be present.
Photons, electrons and positrons have to be simulated together.
If a criticality calculation is chosen (introduced using the keyword CRITICALITY):
• the entire neutron energy domain is necessary (from 1.E-11 to 20. MeV);
• it is possible to eliminate a certain number of batches, the nb batches to be discarded, to achieve equilibrium
and eliminate the transient regime. This is introduced using the keyword DISCARD. By default,
the code automatically determines the number of batches to discard.

<!-- page 296 -->
If kef f is close to 1, the FIXED_SOURCES_CRITICALITY mode is not appropriate. In this case all single source
neutron progeny is simulated in each batch, therefore the calculation time may be very long, or even possibly
infinite if the ke f f is greater than or equal to 1. Good practices with ke f f is close to criticality:
• make a test of simulation within a CRITICALITY mode to assess the value of ke f f ;
• if ke f f is confirmed close to 1 and still a FIXED_SOURCES_CRITICALITY run is needed, considerably
decrease the size of batch (divide by
k
1−k the size of batch for example);
Note: In FIXED_SOURCES_CRITICALITY mode the ke f f result in TRIPOLI-4® output is NOT a real ke f f
but rather a multiplication factor: it is the average number of the overall generation of any fission neutron
(kef f =
ρ
1−ρ).
The keyword DYNAMIC is used to activate time-dependent (kinetic) simulations, including neutrons and
delayed neutron precursors. See Sec. 22.12 for more details and a thorough description of the associated
syntax and options.
The keyword SHIELDING is optional in a radiation shielding problem (as it is the default option).
The monitoring option can be deactivated with MONITORING 0. In this case, the number of particles of the
first batch is set by SIZE and no improvement of the importance map is sought by the code, particularly the
downscattering of particles towards lower energy groups is not favoured. Deactivating this option can be
useful when using the AMS variance reduction technique (see Chapter 18). Otherwise, it is intended for skilled
users only (it is adviced to keep the default monitoring option).
COLLISION 1 Einf(coll) means that the collision is biased at energies higher than Einf(coll). Currently,
collision biasing is only possible in neutron problems. It is not possible for combined neutron-gamma problems
. This option is also intended for skilled users (the default, no collision biasing, is typically used).
The keyword TRANSPORT_BIASING is optional and allows the user to choose between two options for the
transport when a variance reduction technique is used. When biasing is used, the default option for the
transport is QUOTA_SAMPLING. The keyword CROSS_SPLIT is used to treat the transport between two collisions
with sampling performed volume by volume (i.e. the particle is stopped each time it crosses a surface, and the
distance to next collision sampled again). This option is implemented for neutrons only, and is more costly
in terms of simulation time than the default option QUOTA_SAMPLING.

## 22.3 OPTION KEEP_RESULT

Long calculations can be broken up into smaller pieces. First N1 batches are calculated with the option
KEEP_RESULT.
In this case, if the data file is tripoli4.data, a file named tripoli4.data.RESU is created containing the results
of each batch.
If the calculation is resumed (once again using the option KEEP_RESULT) with N2 batches, without deleting
the file named tripoli4.data.RESU, the calculation continues from the last batch. The results are obtained
by taking into account the N1 previous batches; therefore, for N2 (> N1) batches. (Warning: this is a change

<!-- page 297 -->
from versions of the code earlier to tripoli4-version5.)
Important: in this case, the simulation results file must be given a name other than tripoli4.data.RESU (this
name is given at the execution call).
This option is available in parallel mode starting with version 4.5 of the code. For parallel runs, dump files
will be generated for the collector process as well as for each simulator process using a name in the following
form: tripoli4.data.< n >th_task.RESU.
These dump files are not compatible with versions of the code before version 4.5.

## 22.4 OPTION XML_EXPORT

The keyword XML_EXPORT is used to request that the code generates a XML results file during the simulation.
TRIPOLI-4® produces then a file named <data_file>.xml. This file can then be processed by any XML parser
(rather SAX than DOM). It provides a structured and standard access to the values computed by the code.
Results are recorded every batch by default, but if additional keyword XML_NOCOMPLETE is given, only mean
results are recorded at editions.
SERMA_XML_EXPORT produces another type of XML output. It provides only mean results.

## 22.5 OPTION RANDOM

By default, the TRIPOLI-4® code handles management of the first random number. The user can choose
another random number using RANDOM. The additional data have a syntax that depends on the implementation
of the random number generator. This syntax is used when printing out the properties of the random number
generator for each batch (it is the last line of the results file).
The three available random generators are the drand48, the GFSR, and the Mersenne-Twister 19937.
The drand48 is the unix standard random generator (see manpage). This generator is only used in monoprocessor
mode. Its period is 248. The seed can be changed using the following statement:
RANDOM DRAND48_RANDOM 4125 45310 47934
The GFSR random generator is the historical random generator for the parallel mode in TRIPOLI-4® [94].
Its seed can not be changed. Its period is about 2607. The generator can be called in parallel mode using the
syntax:
RANDOM GFSR_RANDOM
The Mersenne-Twister 19937 is a well-known random generator [75]. It can be used both in parallel and in
monoprocessor mode. Its period is 219937 −1. Since version 10, it becomes the default generator in parallel.
It can be seeded with the following statement:
RANDOM MT19937_RANDOM SEED 8191

## 22.6 COMPUTING THE KINETICS PARAMETERS

Knowledge of kinetics parameters is key to the study of nuclear reactor dynamics, in connection with transient
behavior due to normal operation or accidents. Usually, kinetics parameters stem from integrating the full

<!-- page 298 -->
time-dependent Boltzmann and precursors equations over the space, energy and angle variables: after various
algebraic manipulations, they take the general form of a ratio of dot products, namely, ⟨ψ,Fϕ⟩/⟨ψ,Gϕ⟩,
where F and G are operators acting on the neutron flux ϕ, and ψ is a weighting function depending on specific
choices associated to the system under analysis [98]. Essential to reactor control are the mean generation time
Λ of a neutron within a reactor, which is expressed as
Λ = ⟨ψ, 1
vϕ⟩
⟨ψ,Pϕ⟩,
(22.1)
where P is the total fission operator (including prompt and delayed productions) and v is the neutron speed;
and the delayed neutron fraction β, which is expressed as
β = ⟨ψ,Bϕ⟩
⟨ψ,Pϕ⟩,
(22.2)
where B is the fission operator corresponding to delayed neutrons alone. Most often, the weighting function
ψ is either taken to be ψ = 1, in which case the kinetics parameters are said to be un-weighted, i.e.,
Λ0 = ⟨1, 1
vϕ⟩
⟨1,Pϕ⟩, β0 = ⟨1,Bϕ⟩
⟨1,Pϕ⟩
(22.3)
or ψ = ϕ† (ϕ† denoting the adjoint neutron flux), in which case the kinetics parameters are said to be adjointweighted
, or effective, namely,
Λef f = ⟨ϕ†, 1
vϕ⟩
⟨ϕ†,Pϕ⟩, βe f f = ⟨ϕ†,Bϕ⟩
⟨ϕ†,Pϕ⟩.
(22.4)
The un-weighted neutron removal time T0 is related to the un-weighted generation time by Λ0 = T0/ke f f .
The units of kinetics parameters are coherent with those used in the code. The effective mean generation time
Λef f is expressed in [s], and these units apply to all kinetics parameters homogeneous to a time (for instance
the removal time, the leakage time, the absorption time, etc.). The effective delayed neutron fraction βe f f
is given in (dimensionless) units of [105 pcm], and these dimensionless units apply also to the un-weighted
delayed neutron fraction β0. In criticality calculations, it is possible to compute adjoint-weighted and unweighted
kinetics parameters. The specific syntax is the following.

<!-- page 299 -->
SIMULATION
...
KINETIC_PARAMETERS
...
NAUCHI_KINETIC_PARAMETERS
...
IFP_KINETIC_PARAMETERS
IFP_CYCLE_LENGTH
<NB_CYCLES>
<CONVERGENCE_STATISTICS>
<NUCLEI_CONTRIBUTIONS>
LIST
<NB_NUCLEI> NUC_1 ··· NUC_NB_NUCLEI
or
<NUCLEI_CONTRIBUTIONS>
ALL
...
END_SIMULATION
Un-weighted kinetics parameters are activated by resorting to the keyword KINETIC_PARAMETERS. This
option yields the average delayed neutron fraction β0, the generation time Λ0, the removal time T0, the
average time to leakage and the average time to absorption.
Adjoint-weighted kinetics parameters can be computed by resorting to either exact or approximated methods.
The IFP method allows estimating the adjoint neutron flux in criticality simulations by resorting to the
importance approximation [98]: this yields an exact weighting factor for kinetics parameters, provided that
the neutron importance is measured after a sufficiently large number of cycles. The IFP ponderation is
activated by the keyword IFP_KINETIC_PARAMETERS, followed by IFP_CYCLE_LENGTH and the number of
cycles for the estimation of the asymptotic neutron importance. A suggested value for IFP_CYCLE_LENGTH is
20. Adjoint-weighted parameters include the effective delayed neutron fraction βe f f , the effective generation
time Λe f f , and their ratio αRossi = −βef f /Λe f f , which is called Rossi alpha or alpha value at delayed
criticality. The Rossi alpha is expressed in units of the inverse of time, i.e., [s−1].
As an option, the keyword IFP_CONVERGENCE_STATISTICS displays the convergence of the IFP kinetics
parameters as a function of the number of IFP cycles, from 1 to the maximum value defined by the keyword
IFP_CYCLE_LENGTH. See [98] for more details.
Until very recently, the exact weighting method by the adjoint neutron flux was not available in Monte
Carlo codes, and approximated methods were available to estimate the adjoint-weighted kinetics parameters.
Among these techniques, one of the the most successful is the so-called Nauchi’s method, which can now

<!-- page 300 -->
be seen as a first-order approximation of the IFP ponderation [87]. The Nauchi’s kinetics parameters can be
computed by resorting to the keyword NAUCHI_KINETIC_PARAMETERS (the keyword BETA_EFFECTIVE works
also, for retro-compatibility with previous versions of the code). The option NAUCHI_KINETIC_PARAMETERS
will yield the effective delayed neutron fraction βe f f and the effective generation time Λe f f weighted
by the first-order importance function (this corresponds by definition to the use of the IFP method with
IFP_CYCLE_LENGTH equal to 1). Moreover, the option NAUCHI_KINETIC_PARAMETERS will also provide
estimates of the kinetics parameters by the so-called prompt method in a single criticality simulation.
The three keywords for kinetics parameters, namely, KINETIC_PARAMETERS, IFP_KINETIC_PARAMETERS and
NAUCHI_KINETIC_PARAMETERS, are compatible with each other and can be used together in a criticality
simulation.
Observe that in principle it would be also possible to use the PROMPT_FISSION_ONLY keyword to run a
criticality simulation without delayed neutrons. In this case, the delayed neutron fraction could be roughly
estimated by simply taking the difference between the βe f f value with and without delayed neutrons. Observe
however that, when the PROMPT_FISSION_ONLY keyword is activated, the behaviour of the Kstep and Kcoll
estimators for Keff is as expected, i.e., delayed neutron contributions are ignored. As for the Ktrack estimator,
we use the total number of neutrons (νt) and we attribute to those neutrons the prompt energy spectrum.
See also section 13.11 for more details about the relation between β0 calculations and prompt/delayed fission
spectra.
In addition to global parameters such as βef f and Λe f f , the kinetics parameters pertaining to each precursor
family j are also provided. The number of families depends on the specific nuclear data library. When computing
un-weighted kinetics parameters with the keyword KINETIC_PARAMETERS, these include the precursor
decay constants λj (in units of [s−1]) and the natural proportions of delayed neutrons βj for each family (in
units of [105 pcm]). The quantities βj satisfy the relation
∑
j
βj = β0.
(22.5)
Moreover, the β j-weighted average decay constant
¯λ =
β0
∑j
βj
λj
(22.6)
is also computed. The quantity ¯λ is also given in units of [s−1]. When computing adjoint-weighted kinetics
parameters with the keyword IFP_KINETIC_PARAMETERS, the code provides the effective delayed neutron
fractions βe f f,j for each precursor family (in units of [105 pcm]). The quantities βe f f,j satisfy the relation
∑
j
βe f f,j = βe f f .
(22.7)
Finally, for some applications it is interesting to further decompose the kinetics parameters over the
contributions of each fissile isotope.
This can be achieved either by using the optional keyword
NUCLEI_CONTRIBUTIONS followed by LIST, plus the number of isotopes for which the decomposition

<!-- page 301 -->
is sought, and the list of the names of the chosen isotopes; or by using NUCLEI_CONTRIBUTIONS followed
by ALL in the case where the user wants to analyze the contributions of all fissile isotopes that are present
in the simulation. The optional keyword NUCLEI_CONTRIBUTIONS applies to both adjoint-weighted and
un-weighted kinetics parameters, if requested.
The keyword KINETIC_PARAMETERS activates also the calculation of the migration area, which is a useful
parameter in reactor physics. Actually, the code computes the average square distance ⟨r2⟩that a neutron
travels within a single fission generation, from birth to disappearance, weighted by the forward critical flux.
The displayed quantity is thus the average square distance, in units of [cm2]. The migration area can be then
estimated by dividing the obtained score by a factor of 6, as suggested in the framework of the diffusion
theory. When using the IFP_KINETIC_PARAMETERS keyword, the computed average square distance is also
weighted by the adjoint critical flux.
Note: the migration area takes into account the true boundary conditions chosen by the user. For instance,
if the user specifies reflecting boundary conditions on a given surface, the particles will be reflected by
this boundary and the migration area will correspondingly take into account the presence of a reflection.
Therefore, the use of reflection to mimic an infinite medium cannot be properly taken into account in the
migration area calculation.

## 22.7 NEUTRON IMPORTANCE (CRITICAL ADJOINT FLUX)

The critical adjoint (angular) neutron flux ϕ†(r0,Ω0,E0), as a function of position r0, energy E0 and direction
Ω0, physically represents the asymptotic importance of a neutron injected into a multiplying system with
coordinates r0, E0 and Ω0. The formal identification between the neutron importance and the adjoint flux
lies at the basis of the so-called Iterated Fission Probability method [85]. In order to explicitly compute
the importance function, in the ADJOINT_CRITICALITY simulation mode the code runs an ensemble of M
fixed-source batches over L fission generations. For each batch, neutrons start with coordinates r0, E0 and
Ω0. The quantity L defines the IFP cycle length.
More generally, one is possibly led to computing scalar products of the kind ⟨ϕ†,S⟩, where S is an arbitrary
user-defined source. The scalar products are then decomposed on a spatial, energetic and angular
user-defined mesh with respect to the initial coordinates of the neutrons. In particular, by taking a delta-like
source S = δ(r −r0)δ(Ω−Ω0)δ(E −E0) at a given point of the phase space, the scalar product precisely
defines the adjoint flux ϕ†(r0,Ω0,E0).
The critical adjoint flux calculation is activated by the keyword ADJOINT_CRITICALITY, with the following
syntax:

<!-- page 302 -->
SIMULATION
...
ADJOINT_CRITICALITY
DISCARD 0
...
END_SIMULATION
Since the adjoint flux calculation is formally of the fixed source type, DISCARD must be set to zero. The only
allowed particle type for the simulation is NEUTRON. The scalar product ⟨ϕ†,S⟩corresponding to the source S
defined by the user (by using the customary source block; see Chapter 12) is then projected over user-defined
meshes by using special scores designed for the adjoint calculations. An arbitrary number of such ad-hoc
scores are introduced by the block:
IFP_SCORES
<IFP_SCORE_TYPE_1>
NAME <SCORE_NAME_1>
IFP_CYCLE_LENGTH <CYCLE_LENGTH_1>
<SCORING_DATA_1>
ENERGY DECOUPAGE <ENERGY_DECOUPAGE_NAME_1>
<OPTIONAL_KEYWORDS_1>
...
<IFP_SCORE_TYPE_M>
NAME <SCORE_NAME_M>
IFP_CYCLE_LENGTH <CYCLE_LENGTH_M>
<SCORING_DATA_M>
ENERGY DECOUPAGE <ENERGY_DECOUPAGE_NAME_M>
<OPTIONAL_KEYWORDS_M>
END_IFP_SCORES
Two kinds of adjoint scores can be computed, either adjoint fluxes or adjoint reaction rates: correspondingly,
the keyword IFP_SCORE_TYPE can be set to be either IFP_ADJOINT_FLUX for the adjoint flux ⟨ϕ†,S⟩, or
IFP_REACTION_RATE for ⟨ϕ†,ΣtS⟩, where Σt is the total cross section having the coordinates of the neutron
at emission. This latter quantity sometimes appears in reactor physics calculations.
The user must then define the name of the score via the keyword NAME and the length of the IFP cycle for
each score via the keyword IFP_CYCLE_LENGTH. The recommended value is 20.
In order to properly decompose the scalar product between the source and the adjojnt flux, the user must
ensure that the score mesh covers the emission space of the source, . For instance, in order to compute
ϕ†(r0,Ω0,E0) over a given spatial range [xmin, xmax], [ymin, ymax] and [zmin, zmax], an angular range [θmin,
θmax] and [φmin, φmax] and an energy range [Emin, Emax], the user must take a spatially uniform source,

<!-- page 303 -->
isotropic in angle and uniform in energy over the same domain. In this case, the adjoint flux decomposed
over the grid will precisely define ϕ†(r0,Ω0,E0) for each phase space point r0, E0 and Ω0, integrated over
each cell of the mesh. For very fine meshes, we can thus recover ϕ†(r0,Ω0,E0).
The block SCORING_DATA is used in order to define the spatial and angular meshes over which the adjoint
scores are to be projected. This can be defined by using:
• CARTESIAN, in which case the user provides a Cartesian mesh in space. The keyword is followed by the
coordinates and the number of meshes for each coordinate, in the form:
Xmin Xmax nb_mesh_X Ymin Ymax nb_mesh_Y Zmin Zmax nb_mesh_Z
It is implicitly assumed that the scores are integrated with respect to the emission angles, i.e., we score
ϕ†(r0,E0);
• CARTESIAN_ANGULAR, in which case the user provides a Cartesian mesh in space and an angular grid
for φ and θ. The keyword is followed by the coordinates and the number of meshes for each coordinate,
in the form:
Xmin Xmax nb_mesh_X Ymin Ymax nb_mesh_Y Zmin Zmax nb_mesh_Z
φmin φmax nb_mesh_φ θmin θmax nb_mesh_θ
• VOLUMES, in which case the user provides the list of volumes over which the adjoint flux is decomposed.
It is implicitly assumed that the scores are integrated with respect to the emission angles and over each
volume of the list.
Finally, the user must provide the energy mesh over which the adjoint score is computed, by using the
keywords ENERGY GRID, followed by the name of the energy mesh (which must be declared in the usual mesh
block).
IMPORTANT. In the ADJOINT_CRITICALITY simulation mode, all other kinds of scores are forbidden.
Similarly as in the case of the forward critical flux that is computed in regular criticality calculations, the
adjoint critical flux is defined up to a normalization constant. The optional keyword NORMALIZE can be used
in order to normalize each adjoint score to unit.
In addition, the user can define the optional keyword ENTROPY to analyze the convergence of the IFP scores
by computing the relative entropy with respect to the score that has the highest IFP cycle length [85].
An example of adjoint scores is provided here:
IFP_SCORES
IFP_ADJOINT_FLUX
NAME FluxAdj
IFP_CYCLE_LENGTH 20
CARTESIAN -6 +6 10 -3 +3 10 -5 +5 10

<!-- page 304 -->
ENERGY GRID DEC_281G
NORMALIZE
IFP_REACTION_RATE
NAME ReactionAdj
IFP_CYCLE_LENGTH 20
CARTESIAN -6 +6 10 -3 +3 10 -5 +5 10
ENERGY GRID DEC_33G
END_IFP_SCORES

## 22.8 CRITICAL PARAMETER SEARCH

When the fundamental k-eigenvalue depends on a single free control parameter p, the k-eigenvalue equation
can be solved for the fundamental eigenvalue k = k(p) by power iteration for a given p. We can then search
the value p = pc that makes the system exactly critical, with k(p) = k(pc) = 1 [26].

### 22.8.1 ALBEDO SEARCH

The critical albedo search consists in imposing albedo conditions on the boundaries (or part of the boundaries
) of the system, and determining the albedo value β (if any) that makes the reactor critical (i.e., keff = 1).
Such problems emerge for instance in connection with Monte Carlo depletion calculations at the lattice scale,
as a way of reproducing whole-core effects at the boundaries of the assembly. The albedo search simulation
mode is activated with the keyword ALBEDO_SEARCH.
For each of the boundary surfaces where albedo is to be adjusted, the user must apply an ALBEDO boundary
condition (see Sec. 9.1.3) and set the initial albedo value βj
0 for the search (j being the index of the surface),
with a minus sign. Surfaces having an albedo boundary condition with a positive albedo value will not
be adjusted during the critical albedo search: this allows providing adjustable and non-adjustable albedo
conditions in the same geometry, for the sake of generality. During the albedo search procedure, the albedo
βj of each adjustable surface (i.e., those whose initial value was set with a minus sign) will be updated as
βj = β×|βj
0|,
(22.8)
where β is the global multiplier that is sought by the code by using the update law
β(g+1) =
β(g)
 k(g)γ,
(22.9)
where g is the index of the current batch (generation) of the power iteration, and k(g) is the dominant
k-eigenvalue determined at the current batch based on the global albedo value β(g). The exponent 0 < γ ≤1
is used in order to adjust the speed of convergence of the search. The suggested value is γ = 0.5.
The code will provide the global albedo value β and the resulting k-eigenvalue, which should be very close
to 1. The actual albedo value of each surface j is then determined by multiplying the obtained global value β

<!-- page 305 -->
by the absolute value of the initial βj
0 that he user has assigned to each adjustable boundary condition.
The syntax for the albedo search is given as follows:
SIMULATION
...
ALBEDO_SEARCH
INITIAL_GUESS
<VAL>
POWER
<VAL>
<LOWER_LIMIT>
<VAL>
<UPPER_LIMIT>
<VAL>
...
END_SIMULATION
The initial value for the global albedo multiplier β(0) that is used for the iterative search is introduced by
the keyword INITIAL_GUESS and must be positive. The POWER keyword is used to set the exponent γ. Two
optional keywords UPPER_LIMIT and LOWER_LIMIT can be used in order to restrict the search within a given
interval: if the value β(g+1) at a given generation lies beyond the limits, the search is aborted. In this case the
initial value for the search must be also chosen within the bounds. By default, the lower limit is set to zero
and the upper limit is set to infinity.
Similarly as in criticality calculations, a number of batches to be discarded must be assigned by using the
keyword DISCARD.

### 22.8.2 BORON SEARCH

The critical Boron search simulation mode aims at finding the Boron concentrations in one or more userdefined
material compositions such that the reactor is critical (i.e., keff = 1). The Boron concentration search
is activated with the keyword CRITICAL_BORON_SEARCH.
For each of the material compositions where the Boron concentration is to be adjusted, the user must introduce
the additional keyword ADJUSTABLE_BORON before the temperature value. This keyword is used in order to
specify that the concentration of the 10B and/or 11B nuclides contained in the material composition must be
adjusted. An example is provide here:
COMPOSITION <NB_COMPOSITIONS>
...

<!-- page 306 -->
POINTWISE ADJUSTABLE_BORON <TEMP> COMPOSITION_NAME <NB_NUCLEI>
NUC_1
<NUC_1_CONC>
...
...
NUC_M
<NUC_M_CONC>
B10
<INITIAL_B10_CONC>
B11
<INITIAL_B11_CONC>
...
END_COMPOSITION
Material
compositions
containing
10B
and/or
11B
nuclides
and
not
displaying
the
keyword
ADJUSTABLE_BORON will not be adjusted during the critical Boron search:
this allows providing adjustable
and non-adjustable material compositions in the same geometry, for the sake of generality. The
initial (guess) concentrations cj
0 > 0 for 10B and/or 11B nuclides must be provided by the user. During the
Boron search procedure, the 10B and/or 11B nuclide concentration cj of each adjustable material composition
j will be updated as
cj = c×cj
0,
(22.10)
where c is the (dimensionless) global multiplier that is sought by the code by using the update law
c(g+1) = c(g) ×k(g),
(22.11)
where g is the index of the current batch (generation) of the power iteration, and k(g) is the dominant
k-eigenvalue determined at the current batch based on the global Boron concentration c(g). Observe that the
initial ratio between 10B and 11B nuclide concentrations will be exactly preserved during the iterations.
The code will provide the global Boron concentration multiplier c and the resulting k-eigenvalue, which
should be very close to 1. The actual concentration of the 10B and/or 11B nuclides in material composition j
must be then determined by multiplying the obtained global value c by the initial concentrations cj
0 that the
user has assigned.
The syntax for the Boron search is given as follows:
SIMULATION
...
CRITICAL_BORON_SEARCH
INITIAL_GUESS
<VAL>
<LOWER_LIMIT>
<VAL>
<UPPER_LIMIT>
<VAL>
...
END_SIMULATION

<!-- page 307 -->
The initial value for the global concentration multiplier c(0) that is used for the iterative search is introduced
by the keyword INITIAL_GUESS and must be positive. Two optional keywords UPPER_LIMIT and
LOWER_LIMIT can be used in order to restrict the search within a given interval: if the value c(g+1) at a given
generation lies beyond the limits, the search is aborted. In this case the initial value for the search must
be also chosen within the bounds. By default, the lower limit is set to zero and the upper limit is set to infinity.
Similarly as in criticality calculations, a number of batches to be discarded must be assigned by using the
keyword DISCARD.

## 22.9 SLOWING DOWN CURRENT

The slowing down current is an important parameter in neutron transport problems, yielding a global estimate
of the ‘hardness’ of the energy spectrum. The slowing down current exceeding a given energy Et can be computed
by resorting to the keyword SLOWING_DOWN_CURRENT, followed by ENERGY and the threshold energy
value Et, expressed in units of MeV. This reponse will automatically provide as an output three components,
i.e., the slowing down current (taking into account only neutrons traversing the threshold energy from higher
to lower energies), the upscattering current (taking into account only neutrons traversing the threshold energy
from lower to higher energies), and finally the net slowing down current (the net balance of the two previous
currents, with the positive sign for slowing down and the negative sign for upscattering).

## 22.10 SIX FACTOR FORMULA

In criticality calculations, it is possible to decompose the ke f f into six factors accounting for separate effects
analysis:
• χn,xn for the excess weight due to (n,xn) reactions;
• εeven for fast fission on even actinides (236U, 238U, 238Pu, 240Pu, etc.);
• εodd for fast fission on odd actinides (235U, 239Pu, 241Pu, 241Am, etc.);
• p for fhe resonance escape probability;
• f for the thermal utilization factor;
• η for the thermal fission factor.
In order to account for possible leakage, we have introduced a seventh factor PNL expressing the probability
that a neutron will not leak from the multiplying system. The multiplication factor is then expressed as the
product
kef f = χn,xnεevenεodd pfηPNL.
(22.12)
The terms introduced above are defined by setting two energy groups, say 2 for thermal and 1 for fast, with a
boundary at E0. Typically, E0 = 0.625×10−6 [MeV]. Let us set S for the fission source, Pi for the production

<!-- page 308 -->
terms in group i, with P = P1 + P2, Ai for the absorption terms in group i, with A = A1 + A2, and Fi for the
fission terms in group i, with F = F1 +F2. Furthermore, denote by L the leakage term. Then we have
εeven = P
A
A−F1,even
P1,odd +P2,
(22.13)
εodd = P1,odd +P2
A−F1,even
A−F1
P2
,
(22.14)
p =
A2
A−F1
,
(22.15)
f = A2,fuel
A2
,
(22.16)
η =
P2
A2,fuel
,
(22.17)
PNL =
A
A+L,
(22.18)
χn,xn = A+L
S
,
(22.19)
whence
kef f = χn,xnεevenεodd pfηPNL = P
S .
(22.20)
The six factor formula can be computed by resorting to the keyword SIX_FACTOR_FORMULA , followed by
ENERGY and the threshold energy value E0 between thermal and fast groups, expressed in units of MeV.

## 22.11 DIVEN DISPERSION FACTOR

In reactor physics, the Diven dispersion factor D expresses the dispersion of the number of prompt neutrons
at each fission event and is typically used in order to calibrate the experimental measurements of the kinetics
parameters based on the reactor noise theory. It is usually defined as
D = ⟨νp(νp −1)⟩
⟨νp⟩2
= DνDs,
(22.21)
where Dν expresses the contribution purely due to fluctuations in the prompt neutron number (which would
correspond to the point-kinetics approximation) and Ds is a spatial correction factor that takes into account
the shape of the fundamental and adjoint mode within the core. Both coefficients are computed by the code.
The adjoint-weighting procedure is based on the IFP method and the Diven factor calculation is available in
CRITICALITY simulation mode only. The specific syntax is the following.

<!-- page 309 -->
SIMULATION
...
DIVEN_DISPERSION_FACTOR
IFP_CYCLE_LENGTH
<NB_CYCLES>
FILE
Filename
<CONVERGENCE_STATISTICS>
...
END_SIMULATION
The keyword IFP_CYCLE_LENGTH is used to provide the number of cycles for the estimation of the asymptotic
neutron importance. A suggested value for IFP_CYCLE_LENGTH is 20.
The definition of the Diven factor implies the use of the probability P(νp) of obtaining νp prompt neutrons at
fission events, for each fissile nucleus. Since nuclear data libraries typically provide only the average value
⟨νp⟩, the calculation of the Diven factor requires additional information from the user. The distribution P(νp)
can be provided by the user by using the keyword FILE, followed by the file name. (See also Section 3.1.2
for the AdditionalData/P_NU_DATA directory provided with the code). Probability data in the file must be
organized by isotope and energy intervals. Values of P(νp) are given from P(νp = 0) to P(νp = νp,max). The
structure of the distribution for each fissile nuclide must be the following:
NUCLEUS <NUC_NAME_1>
ENERGY <E0> <E1>
0
P(0)
...
nu_max_nuc_1_E_1
P(nu_max_nuc_1_E_1)
ENERGY <E1> <E2>
0
P(0)
...
nu_max_nuc_1_E_2
P(nu_max_nuc_1_E_2)
...
NUCLEUS <NUC_NAME_M>
ENERGY <E0> <E1>
0
P(0)
...

<!-- page 310 -->
nu_max_nuc_M_E_1
P(nu_max_nuc_M_E_1)
ENERGY <E1> <E2>
0
P(0)
...
nu_max_nuc_M_E_2
P(nu_max_nuc_M_E_2)
...
where the distribution values are given for each energy interval defined by the user. The distribution must
be provided for each fissile nucleus that is present in the simulation by writing the corresponding sections
consecutively in the data file.
As an option, the keyword IFP_CONVERGENCE_STATISTICS displays the convergence of the Diven factor
as a function of the number of IFP cycles, from 1 to the maximum value defined by the keyword
IFP_CYCLE_LENGTH.

## 22.12 DYNAMIC (TIME-DEPENDENT SIMULATION) OPTIONS

Time-dependent neutron transport, taking into account the presence of the delayed neutron precursors, is
activated using the keyword DYNAMIC in the simulation block. The goal of kinetic Monte Carlo methods is to
address the solution of the full time-dependent Boltzmann equation, coupled to the M precursor equations,
one for each delayed neutron precursor family. The number of families depends on the nuclear data library:
for instance, in ENDF/B-VIII (and previous versions) there exist 6 families, and each fissile isotope has its
own set of decay constants λ j, j = 1,...,6; in JEFF3.1.1, on the contrary, the number of families has been
increased to 8 and all fissile isotopes have the same set of decay constants λj, j = 1,...,8. When running a
time-dependent simulation with neutrons and precursors, a few issues must be taken into account:
• The characteristic time scale of the precursor population (i.e., the average decay time ∼10 s) is much
longer than that of neutrons (i.e., the mean generation time, 10−5 s in a typical PWR), and the delayed
neutron fraction is very small (∼0.7%). This implies that at the critical regime, when the neutron
and precursor populations are in equilibrium, precursors are considerably more abundant than neutrons
within the core, by a factor ∼104. This makes the use of special variance-reduction techniques mandatory
to deal with the presence of two very different time scales in the simulation;
• Population control should be ensured to prevent the neutron and precursor populations from shrinking
to zero or growing unbounded. This is true even for the stationary regime, where the variance of the
population grows linearly in time if population control is not enforced (the ‘critical catastrophe’);
• If the initial conditions correspond to a critical (i.e., equilibrium) regime, the particle source must be prepared
in the equilibrium state before running the kinetic Monte Carlo simulation for the time-dependent
transport.

<!-- page 311 -->
The precursor particles do not directly contribute to Monte Carlo scores during the simulation: their role is
to provide a ‘buffer’ for delayed neutrons and regulate the statistical weight of the neutron population that
is physically transported and thus directly contributes to Monte Carlo scores. Precursors can be created at
fission events and can possibly also be present at the beginning of the simulation in the case of a critical
source. All possible precursors associated to a given fission event are combined into a single representative
precursor particle carrying the total statistical weight, for the purpose of reducing the variance due to the
dispersion of the decay constants. This method ensures unbiased estimates for the average scores. For more
details, we refer the reader to Ref. [37].
The syntax for the DYNAMIC simulation mode is as follows:
SIMULATION
...
DYNAMIC
GRID
time_mesh_name
POPULATION_CONTROL
population_control_option
POPULATION_IMPORTANCE_RATIO
population_importance_options
CRITICALITY_SOURCE
inactive_cycles decorrelation_cycles
CRITICALITY_GEOM
geom_name
TIME_GEOMETRY LIST n_geometries
time_1 geom_name_1 ... time_n geom_name_n
BRANCHLESS
...
PARTICLES
2 NEUTRON PRECURSOR
TIME_INF
NEUTRON time_inf
TIME_SUP
NEUTRON time_sup
END_SIMULATION

### 22.12.1 TIME MESH FOR FORCED PRECURSOR DECAY

In order to cope with the separation of the neutron and precursor time scales, the code uses a variance reduction
method called ‘forced decay’: the idea is to modify the decay probability of the precursor particles,
and yet preserve an unbiased Monte Carlo game by correspondingly modifying the statistical weight of the
delayed neutrons emitted upon decay. This ensures a larger fraction of neutrons in the fission chains and thus

<!-- page 312 -->
a reduced variance in the total population per unit time. Several choices are possible, the simplest being to
introduce an arbitrary time mesh t0 < t1 < ··· < tN: the code will force precursors to decay uniformly in each
bin of the mesh.
The time mesh must be defined in the GRID_LIST block and its name must be given as an argument to the
GRID keyword, which must immediately follow the DYNAMIC keyword.

### 22.12.2 POPULATION CONTROL

Depending on the reactivity of the system, the population size (number of neutrons and precursors) may
shrink to zero (subcritical case) or grow without bounds (supercritical case). Both scenarios are problematic
and thus require some control mechanisms to the population size during the calculation (detailed below). For
the sake of simplicity, population control is enforced at the end of the time intervals selected for forced decay.
This has two advantages: the user only needs to input one time grid, and it does not introduce additional
stopping times for the precursors. While the time steps are in principle arbitrary, in practice population
control restricts the choice of the interval boundaries: if the system is super-critical, the population might
diverge within a step; conversely, if the system is sub-critical the population might disappear within a step.
Two population control methods are available in the code: Russian roulette & splitting, and combing.

#### 22.12.2.1 Russian roulette & splitting

The Russian roulette and splitting can be separately applied to the neutron and precursor populations banked
at the end of each time step. The roulette is straightforward for neutrons. Concerning precursors, the roulette
is applied on the basis of the expected delayed neutron weight that can be emitted during the following time
step.
This choice corresponds to the use of POPULATION_CONTROL RUSSIAN_ROULETTE.

#### 22.12.2.2 Combing

The aim of combing is to normalize the number of transported particles while preserving their total weight
and possibly the proportion of respective weights in the case of multiple particle species. For kinetic simulations
, combing can achieve variance reduction and save computer time by keeping the population size
approximately constant over time steps.
This choice corresponds to the use of POPULATION_CONTROL COMBING.

### 22.12.3 TIME MESH FOR SCORES

In addition to the simulation time grid for forced decay, a scoring time grid must also be defined. By construction
, the contents of each bin [τq,τq+1] will yield the ensemble-averaged time integral of the corresponding
Monte Carlo score, between time τq and τq+1. Unlike the time grid for precursor decay (and for population
control), the time mesh for scoring is arbitrary, and the bins can be irregularly spaced and have any size.
Scoring time grids are specified in the SCORE block with the TIME GRID keywords (see Chapter 15).

<!-- page 313 -->
### 22.12.4 RELATIVE PARTICLE IMPORTANCE

The kinetic simulation of fast transients requires a finely discretized time mesh in order to capture the fast
time variations of the population. However, if the simulation time steps are too small, ordinary roulette
will kill most of the delayed neutrons, even when forced decay is applied. Indeed, for small time steps, the
statistical weight of delayed neutrons is proportional to the time interval τq+1 −τq. For small time intervals,
the weight of the delayed neutrons generated by forced decay is also small and particles will not survive the
roulette. With no delayed neutrons to initiate new fission chains, the simulation will then suffer from severe
under-sampling issues. In order to increase the number of neutrons present in the simulation and therefore
improve the efficiency of simulations over short time scales, a time-dependent importance scheme can be
used in the dynamic simulation. For each time step i, the user can provide an importance ratio Ri = IN,i/IC,i,
where IN,i is the importance of neutrons and IC,i is the importance of precursors for tha step. At the beginning
of a time step, including the first one, the code uses the current particle weights to estimate IN,i and IC,i, in
such a way that the ‘physical’ weights are preserved.
Note that the population weights are only adjusted if the importance ratio changes (nothing needs to be done
if Ri+1 = Ri).
The choice of this ratio should depend on the time step and the reactivity. In order to observe both fast and
slow transients, one needs a non-uniform simulation time grid and importance factors. On one hand, fast
transients can exclusively be observed over very short times (time steps should be of the order of the mean
generation time); on the other hand, delayed neutrons need several seconds to be emitted. Hence, short time
grids should be associated with the application of an importance factor to favour the forced decay of delayed
neutrons. On the contrary, importance is not necessary for wide time grids since delayed neutrons are emitted
with a large statistical weight.
The relative particle importance is defined on the time mesh for forced precursor decay (DYNAMIC GRID). If
the user wants to specify a single importance value for the whole simulation, the syntax is as follows:
POPULATION_IMPORTANCE_RATIO <value>
If a time-dependent importance ratio needs to be specified, the syntax is the following:
POPULATION_IMPORTANCE_RATIO
LIST <n_values> <value_1> ...<value_n>
Here it is understood that the first value of the importance ratio refers to the first time step of the time grid
for forced precursor decay, the second value refers to the second time step, and so on. If the number of
values given here is smaller than the number of time steps in the time grid for forced precursor decay, then
the importance ratio is assumed to take the last value, value_n, until the last time step.

<!-- page 314 -->
Batch 1
Criticality source computation
Dynamic simulation
Fission neutrons
Dynamic source particles
All neutrons transfer
Fission neutrons transfer
Inactive cycles
Time steps
Batch 2
Batch 3
. . .
. . .
. . .
Batch M
Figure 22.1: Kinetic simulation process with M batches. A complete power iteration is performed once by the first batch. During
the final cycle, precursors are sampled so that the dynamic simulation can begin while the generated fission neutrons are transferred
to the second batch which runs a few additional power iterations in order to ensure reasonable decorrelation. The third batch gets
the fission neutrons generated by the second one, and so on. In a parallel run, each processor would apply this scheme.

### 22.12.5 CRITICAL SOURCE

The typical configuration at the initial time for a kinetic Monte Carlo simulation is either a system containing
only a neutron source (e.g., for reactor start-up calculations), or a system in a critical state (e.g., for the
departure from a stationary regime). For the latter, the code applies the power iteration algorithm (i.e., a
k-eigenvalue calculation) over a large number of inactive cycles, with neutrons alone, in order to obtain an
estimate of the fundamental mode. During the last inactive cycle, neutron and precursor sources for the
dynamic phase are sampled at each collision, based on the fundamental mode: the critical neutron flux is
converted into a neutron and precursor population, whose time is set to t = 0. These ‘critical’ sources are
then used for the dynamic simulation.
The code averages the dynamic calculation results over consecutive batches. Ideally, each batch should represent
a genuine independent replica of the full calculation, namely a source-convergence phase followed by
a kinetic phase. In order to reduce the number of inactive cycles, the fission neutrons generated in the last
inactive cycle of the current batch are injected in the inactive cycles of the following one. This reduces the
overhead of inactive cycles, at the cost of introducing correlations among batches (the estimation of the statistical
uncertainty over the calculation results can be thus affected). Note, however, that this is essentially the
same difficulty that one faces in conventional criticality calculations. A scheme of this process is illustrated
in Fig. 22.1.
The number of inactive cycles and the number of additional decorrelation cycles between batches are specified
with the CRITICALITY_SOURCE keyword:

<!-- page 315 -->
CRITICALITY_SOURCE inactive_cycles decorrelation_cycles
The example of Fig. 22.1 corresponds to inactive_cycles=16 and decorrelation_cycles=4.

### 22.12.6 ADJUSTING THE REACTIVITY

The simulation of a nuclear reactor is necessarily affected by uncertainties on geometry details and on nuclear
data. For this reason, the effective multiplication factor for nominally critical conditions may fail to be equal
to 1. Even small deviations from 1 may be important in kinetic Monte Carlo simulations, because the system
will drift away from the stationary state during the dynamic simulation. For this reason, in order to minimize
these deviations, we propose a simulation option to rescale the average number of neutrons produced by
fission by the multiplication factor (obtained by a preliminary criticality calculation). To use this option, use
the optional RESCALE_NU_BY_KEFF keyword, which is detailed in Sec. 22.1.

### 22.12.7 CHANGING GEOMETRIES

In order to simulate transients involving moving reactor parts, the code allows modifying the geometry and
material compositions at each time step. As long as all the geometries have the same bounding box, there is
no constraint on their internal structure (number of volumes, composition of volumes, etc.). This new option,
which for the moment is only available for ROOT geometries, paves the way for all types of time-dependent
simulations: different geometries can be defined for the criticality step and for each time step of the dynamic
simulation.
The use of multiple ROOT geometries requires the MULTI_GEOM block, which replaces the usual
ROOT_GEOMETRY block at the beginning of the input file. The syntax of MULTI_GEOM is the following:
MULTI_GEOM
NAME geom_name_1
ROOT_geometry_specification_1
NAME geom_name_2
ROOT_geometry_specification_2
...
END_MULTI_GEOM
Any number of geometries can be defined. Each geometry must be given a unique name with the NAME
keyword. The specification of the ROOT geometry may take any of the forms allowed in the ROOT_GEOMETRY
block, which are described in Chapter 36. In practice, the geometry specification may be any of the following:
the name of a ROOT file containing a geometry, a CPP_ROOT_GEOM block, or a PYTHON_ROOT_GEOM block.
The geometries defined in the MULTI_GEOM block can be used in dynamic simulations with the
CRITICALITY_GEOM and TIME_GEOMETRY keywords. For the former, the syntax is:

<!-- page 316 -->
CRITICALITY_GEOM geometry_name
Here geometry_name must be the name of one of the geometries in MULTI_GEOM. It identifies the geometry
that will be used for the criticality part of the dynamic simulation, if CRITICALITY_SOURCE is specified. The
syntax of the TIME_GEOMETRY keyword is:
TIME_GEOMETRY LIST n_geometries
time_1 geom_name_1 ... time_n geom_name_n
The time_i values must be part of the time grid for forced precursor decay; they indicate the times at which
the geometry changes. The geom_name_i strings must be geometry names, as declared in MULTI_GEOM, and
they indicate the geometry that will be used for time_i < t < time_i+1. The last geometry is assumed to last
until the end of the last time step.

### 22.12.8 BRANCHLESS COLLISIONS

The fission chains in Monte Carlo transport are responsible for increased variance and spatial correlations
in multiplying media with respect to the case of purely diffusing and absorbing configurations. These fluctuations
, whose origin lies in the fission-induced spatial correlations between successive generations, might
globally hinder the convergence of the kinetic Monte Carlo calculations. In TRIPOLI-4 we have chosen
to cope with the variance associated to fission chains by implementing the branchless collisions method.
The idea behind this algorithm is to suppress the variability due to the simultaneous propagation of the several
branches associated to a fission event (i.e., the histories of all the neutrons descending from a common
ancestor) and to collapse all the contributions into a single history carrying the average weight of all the descendants
. In principle, the branchless transport has been shown to be quite effective in reducing the variance
in multiplying systems [97, 38].
Branchless collisions can be activated with the optional BRANCHLESS keyword. This mode is only available
in DYNAMIC mode.

## 22.13 EPITHERMAL BROADENING OPTIONS

In the context of neutron interactions with matter, it may become necessary to take into account relative
velocity effects between the incident neutron and the collided nucleus at thermal equilibrium. The thermal
agitation of collided nuclei is indeed responsible for Doppler broadened cross sections as well as scattering
kernels. Doppler broadening of cross sections at a given medium temperature is typically taken into account
by the external preprocessing of nuclear data, whereas Doppler broadening of the scattering kernels must
be taken into account by the Monte Carlo code itself. This is usually required for elastic collisions in the
epithermal region, say in the range from 1 eV to 1 keV, where the two energies become comparable.
Below the epithermal region, interactions are either dominated by 1/v radiative capture (so that there is no
re-emitted neutron), or assumed to be described by more sophisticated models, such as elastic or inelastic

<!-- page 317 -->
thermal kernels (of the S(α,β) kind, for instance, which take into account lattice structures and/or molecular
bonds).
Above the epithermal region, on the contrary, the neutron energy is larger than the typical nucleus (Maxwell-
Boltzmann) energy, so that the nucleus can be considered at rest as seen from the incoming neutron: in this
case, standard two-body kinematics can be applied for the elastic collisions, which results in the so-called
asymptotic elastic scattering kernel.
The intermediate epithermal region needs to be described by a specific model that takes into account relative
velocity effects on the behavior of elastic cross sections and elastic scattering kernel (this latter being the
double differential component of the former). The Doppler broadening of elastic scattering kernels must be
consistent with that of the associated cross sections.
The default model for the Doppler broadening of elastic scattering kernels in TRIPOLI-4® is the so-called
SVT (Sampling of the Velocity of the Target nucleus), which assumes that nuclei are at thermal equilibrium
with a Mawxell-Boltzmann velocity distribution and derives the scattered neutron parameters (direction and
speed) from two-body kinematics [4].
The SVT model is based on the hypothesis that the elastic cross sections in the epithermal region are approximately
flat, which is true for light nuclei, but breaks down for heavy resonant nuclei such as 238U. If no
optional keyword for Doppler broadening is specified in the SIMULATION block, then TRIPOLI-4® implicitly
adopts the SVT model in the region from 10−5 eV to an upper threshold energy Ethreshold for the incident neutron
, with Ethreshold = 400kBT, kB = 8.617 · 10−5 [eV/K] being the Boltzmann constant, and T the medium
temperature in Kelvin. Above Ethreshold the asymptotic scattering kernel is used instead.
If in the thermal region (say between 10−5 eV and Etherm, with Etherm typically of the order of 5 eV) thermal
elastic cross sections are available, TRIPOLI-4® uses these thermal sections up to Etherm, and above Etherm
chooses the SVT or the asymptotic elastic kernel according to whether the incident neutron energy is below
or above Ethreshold, respectively.
If the user needs to specify a different Doppler broadening treatment, then the optional keyword
EPITHERMAL_BROADENING must be declared in the SIMULATION block. The syntax then depends on which
model the user wants to adopt, and what are the parameters to be defined for the chosen model. The possible
(mutually exclusive) options are the following:
22.13.1
SVT MODEL WITH A DIFFERENT THRESHOLD ENERGY Ethreshold
The syntax for using the SVT model with a different threshold energy Ethreshold is
SIMULATION
...
EPITHERMAL_BROADENING
SVT UPPER_ENERGY Ethreshold
ONLY_SVT
...
END_SIMULATION

<!-- page 318 -->
where Ethreshold is the user-defined energy threshold that applies to all the isotopes, expressed in units of MeV.

### 22.13.2 DOPPLER BROADENING REJECTION CORRECTION (DBRC)

The Doppler Broadening Rejection Correction (DBRC) has been especially conceived for improving the
SVT model in presence of heavy nuclei, whose elastic cross sections typically display strong resonances
in the epithermal region [5]. The DBRC model is implemented as follows: up to 0.1 eV, standard SVT is
applied, since it is assumed that in this region there are no resonances in the elastic cross section. Above 0.1
eV, and up to a threshold energy Edbrc defined by the user (usually at some hundreds of eV), the DBRC is
applied. Above Ethreshold, the asymptotic elastic kernel is applied.
The user can further specify a list of nuclei for which the DBRC correction is to be used. For the isotopes that
are not in the list, standard SVT is applied instead, up to an energy Ethreshold. The syntax for DBRC depends
on whether the user wants to give an exhaustive list of isotopes or prefers to give a window of atomic weights
(this latter option is preferable when writing down the entire list might be too cumbersome).
In the former case, the syntax is
SIMULATION
...
EPITHERMAL_BROADENING
SVT UPPER_ENERGY Ethreshold
DBRC UPPER_ENERGY Edbrc
NUCLEI NBnuclei NUC1 ··· NUCn
...
END_SIMULATION
The values Ethreshold and Edbrc are to be expressed in MeV.
In the latter case, the DBRC model is applied to all nuclei whose atomic weight A lies between Amin and Amax,
and the syntax is
SIMULATION
...
EPITHERMAL_BROADENING
SVT UPPER_ENERGY Ethreshold
DBRC UPPER_ENERGY Edbrc
ATOMIC_WEIGHT_WINDOW Amin Amax
...
END_SIMULATION

<!-- page 319 -->
### 22.13.3 WEIGHT CORRECTION METHOD (WCM)

The Weight Correction Method (WCM) model has been conceived as an alternative to DBRC for improving
the SVT model in presence of heavy resonant nuclei [25]. The WCM model is implemented as follows: up to
0.1 eV, standard SVT is applied, since it is assumed that in this region there are no resonances in the elastic
cross section. Above 0.1 eV, and up to a threshold energy Ewcm defined by the user (usually at some hundreds
of eV), the WCM is applied. Above Ethreshold, the asymptotic elastic kernel is applied. The user can further
specify a list of nuclei for which the WCM correction is to be used.
The user can further specify a list of nuclei for which the WCM correction is to be used. For the isotopes that
are not in the list, standard SVT is applied instead, up to an energy Ethreshold. The syntax for WCM depends
on whether the user wants to give an exhaustive list of isotopes or prefers to give a window of atomic weights
(this latter option is preferable when writing down the entire list might be too cumbersome).
In the former case, the syntax is
SIMULATION
...
EPITHERMAL_BROADENING
SVT UPPER_ENERGY Ethreshold
WCM UPPER_ENERGY Ewcm
NUCLEI NBnuclei NUC1 ··· NUCn
...
END_SIMULATION
The values Ethreshold and Edbrc are to be expressed in MeV.
In the latter case, the WCM model is applied to all nuclei whose atomic weight A lies between Amin and Amax,
and the syntax is
SIMULATION
...
EPITHERMAL_BROADENING
SVT UPPER_ENERGY Ethreshold
WCM UPPER_ENERGY Ewcm
ATOMIC_WEIGHT_WINDOW Amin Amax
...
END_SIMULATION
Remark: setting for instance an atomic weight window with Amin = 0.5 and Amax = 300 would mean that all
nuclei are to be corrected with either DBRC or WCM models.

<!-- page 320 -->
## 22.14 ELECTROMAGNETIC SHOWER OPTIONS

The keywords related to the electromagnetic shower are:
• ELECTRON_INELASTIC_CUTOFF defines the inelastic cut-off. Only electrons with energies higher than
this threshold are produced. By default, the code sets the threshold at 0.001 MeV.
• THIN_LAYER_SUBSTEP < n > allows changing the number by which the transport step is divided when
a particle approaches a frontier. Making substeps allows a more rigorous processing of frontier approaches
. The default value is 8.
• ENERGY_LOSS_BY_STEP < p > allows changing the parameter used to estimate step size in lepton transport
. This step corresponds to the length when the electrons or positrons have lost a proportion < p >
of their energy by collisions. This length is calculated using CSDA models (Continuous Slowing Down
Approximation). The default value is currently 0.02.
• ELECTRON_BREMS_CUTOFF defines the bremsstrahlung cut-off. Only photons with energies higher than
the threshold are produced. By default, the code sets the threshold at 0.001 MeV.
• THICK_TARGET_BREMSSTRAHLUNG activates a simplified simulation mode for the electromagnetic
shower. When this option is used, secondary electrons and positrons produced by photon collisions
are not transported, but part of their energy is converted into new bremsstrahlung photons. This is much
faster (but slightly less accurate) than the full simulation of the electromagnetic shower. This option
requires electron and positron transport to be activated in the SIMULATION block. Note that it can be
used even with electron/positron sources.
• BREMSSTRAHLUNG_MODEL selects the model to be used for the bremsstrahlung cross section. Until version
10.2, TRIPOLI-4® used Berger and Seltzer’s 1970 bremsstrahlung model [6]. This model is still
available and can be selected with the BREMSSTRAHLUNG_MODEL 0 keyword.
Starting with TRIPOLI-4® version 11, the code uses Seltzer and Berger’s 1986 model by default [96]
(keyword: BREMSSTRAHLUNG_MODEL 1). This model requires external cross-section files, which are
shipped with the TRIPOLI-4® installation. TRIPOLI-4® will first search for the cross-section files in the
electron directory specified in the path file (see Section 3.1). If they are not found there, if the path file
is specified in the new format (Section 3.1.2), and if it contains the electron_bremsstrahlung_xs
key, TRIPOLI-4® will look in that directory, too. An error will be raised if the cross-section files cannot
be found. The new path file format makes it possible to use the new bremsstrahlung model even if the
cross-section files are not yet included in the nuclear data library.
• NO_ELECTRON_MULTIPLE_SCATTERING disables the multiple scattering simulation operation. This function
is not available in this version of the code.
• ELECTRON_TOTAL_STOPPING_POWER makes energy losses due to inelastic collisions continuous
throughout the energy domain. Secondary particles are produced independently. By default, this option
is not enabled.

<!-- page 321 -->
• Combined with the previous option, NO_ELECTRON_STRAGGLING allows disabling the fluctuations on
energy losses of the particles. The default CSDA mode (Continuous Slowing Down Approximation) of
TRIPOLI-4® includes these fluctuations. The default mode includes more physics, but CSDA without
straggling may be better suited for comparisons with other codes.
• ELECTRON_PHOTON_BALANCE is an option that activates the calculation of the balance (in terms of number
of particles, weight and energy) of the simulation. The balance is produced each time results are
produced. By default, this option is not activated in the code.
• NO_ANOMALOUS_SCATTERING_FACTOR set all photon anomalous scattering factors to 0. This option can
be useful to carry out comparisons to other calculation codes.
• ELECTRON_MIN_STEP_LENGTH sets the value of the minimum length for electron/positron steps. If the
stopping power or the cross sections for hard collisions suggest a step length shorter than this value, then
the step length is artificially extended, and the energy loss along the step is adjusted accordingly. This
option affects the collision density and the energy deposition in thin layers. The default value is 1e-4
(cm), but smaller values may yield slightly better predictions, especially for low-energy electrons.
Important notes concerning electromagnetic showers :
1. Due to interaction relationships, it is not possible to simulate electrons or positrons alone.
2. The minimal photon, electron, positron kinetic energy is about 1 keV, below this energy atomic shell
models currently implemented become inadequate.
3. In the current version of TRIPOLI-4®, if NJOY cross section option is used (see chapter 1), neutron data
are always loaded even if no neutron is transported.
In order to avoid this, use ENDL cross section option (and then ENDL photon data).
4. Fluorescence photons are emitted after photoelectron emission, then, currently, there is fluorescence
only if electrons are tracked.
5. If no DEPOSITED_SPECTRUM score is present, then photoelectric interaction is modelized as non analog
by weight reduction.
6. Be careful when comparing TRIPOLI-4® results in photon-only transport mode with other codes.
Other codes can include bremsstrahlung photons even if electrons are not transported (thick-target
bremsstrahlung).
This feature is present in TRIPOLI-4®, but needs to be activated with the
THICK_TARGET_BREMSSTRAHLUNG option.
7. Due to the minimal photon/electron/positron energy of 1 keV, the minimal group energy width (in
DEPOSITED_SPECTRUM spectrum for example) is also 1 keV.
8. Currently, DEPOSITED_SPECTRUM scores are incompatible with biasing techniques. In case of necessity,
in first approximation, one can couple by hand a photon flux calculation (FLUX_PT for example) at the
entrance of the detector area and a DEPOSITED_SPECTRUM calculation.

<!-- page 322 -->
9. Electron and positron transport is very time consuming. To speed up the calculation, taking into account
the low electron/positron range, one can set high energy cut on electron/positron/photon in low interest
volumes (far from the detector for example) using VOLENERCUT, see chapter 37.

## 22.15 OPTION PHOTON_NEUTRON_RATIO

If the keyword PHOTON_NEUTRON_RATIO is used in a n −γ calculation, the population of photons can be
biased (as soon as they are generated), using splitting or russian roulette. The ratio stands here for the mean
number of photons generated by neutron reactions, over the number of simulated neutrons in a batch. The
user has the choice either to set a global ratio value for all the geometry or to define ratio values for particular
volumes of the geometry. The syntax is as follows:
PHOTON_NEUTRON_RATIO
*
LIST nb(volumes)
volume(1) ratio(1)
volume(2) ratio(2)
...
volume(n) ratio(n)
*
global ratio
where volume(i) is a volume number and ratio(i) its associated ratio. All "ratio" parameters are real numbers.
• By default, the ratio is equal to 1. In this case, the aim is to have a population of photons equal to the
population of neutrons.
• This parameter can be increased (or decreased), which leads to multiplying the splitting and Russian
roulette thresholds by "global ratio" (or (“ratio(i)” for a specific volume i).
• If the choice of ratio per volume is done (with the keyword LIST), the ratio of non listed volumes is kept
to 1.

## 22.16 OPTION ALL_COLLIDED_FLUX_PT_POINTS

This option enables a score contribution of all flux points (FLUX_PT) at each deterministic collision. By
default a flux point is randomly selected. This option is useful if the point flux scores are used to obtain a
picture in imagery or radiography device.

## 22.17 OPTION SUPER_HISTORY

The Super-history method consists of simulating several successive generations in a single batch without
performing any renormalization of the neutron population by ke f f . Such approach has been originally used to
reduce correlations between batches. This method is currently available only for the CRITICALITY simulation
mode.

<!-- page 323 -->
The SUPER_HISTORY keyword may be followed by the LATENT <nb_latent_generations> keyword to specify
the number of additional generations simulated per batch. The default behavior is 10 latent generations.

## 22.18 OPTION WIELANDT_METHOD

The Wielandt method has been originally adapted to Monte Carlo calculations for convergence acceleration
purposes. The method consists in subtracting an extra fission source term on both sides of the transport
equation, which yields
Tψ−Sψ−1
ke
Fψ = ( 1
k0
−1
ke
)Fψ,
(22.22)
where T, S and F denote the usual loss, scattering and fission operators, respectively, k0 is the fundamental
eigenvalue and ke is the Wielandt control parameter, to be chosen as ke > k0. If Eq. (22.22) is to be solved
by power iteration, the fission operator term on the left of the equation is interpreted as additional fission
neutrons that will be tracked in the current cycle. Thus, at every collision, nnext fission neutrons are emitted
for the next cycle, and ncurrent for the current cycle, according to
nnext = νΣf
Σt
1
kn−1
w
+ξ
ncurrent = νΣf
Σt
1
kn−1
e
+ξ,
(22.23)
ξ being a uniform random number. The Wielandt method is basically an eigenvalue-shift approach that
reduces the dominance ratio (thus improving the convergence rate of the power iteration) while preserving
the eigenfunctions. However, it may be difficult to choose a proper value for ke, since the fundamental
eigenvalue k0 is not known in advance: large fluctuations in the neutron population may appear in the early
cycles of the Wielandt method when imposing a fixed value ke. Thus, It was proposed to use ∆= ke −k0
rather than ke as the control parameter, and furthermore introduced an iteration scheme where ∆is allowed
to evolve along cycles in order to mitigate population fluctuations. The average length of the (subcritical)
“fission chains” simulated within each cycle has been shown to be inversely proportional to ∆: L ≃1+k0/∆.
In the TRIPOLI-4® code, three different convergence schemes for ∆, namely a constant ∆, a linear approach to
a target ∆and a user-defined function for the approach to a target ∆. The default method is a linear approach
where ∆start = 1.0 and ∆end = 0.1 with a decrease of 0.05 at each batch leading to a number of steps of 18.
WIELANDT_METHOD
#
DEFAULT
#
CONSTANT ∆
#
LINEAR ∆start∆end nb_steps
#
USER nb_steps ∆1...∆nb_steps
22.19
THE
MULTIPLE
SIMULATION
MODE
(NEUTRONICS-SHIELDING

<!-- page 324 -->
COUPLING)

### 22.19.1 OBJECTIVE

Many applications require a sequence of several separate computations, e.g. in order to obtain in a first step
the neutron productions in the multiplying area and, in a second step, the propagation of neutrons towards
detectors that are more or less distant from the multiplying area, with possible strong attenuations. However,
the drawback of these two-step separate calculation schemes is to leave to the user the proper preparation
of the source for the second calculation. The direct computation of the response of these detectors (i.e. the
neutronics-shielding coupling) aims at providing in a single computation a precise distribution of the fission
neutrons of the core together with their efficient propagation towards the detectors. This feature is devoted
either to fixed-sources sub-criticality or to criticality configurations (with a control of the source convergence).

### 22.19.2 PRINCIPLE

The coupling consists in linking the following two steps within each simulated batch:
• Storing the fission neutrons produced either during a fixed-source criticality batch or during a criticality
batch
• Using them, in the same batch, as source neutrons for the shielding step (this allows using one of the
code’s variance reduction techniques, to propagate the neutrons through large distances with strong
attenuations). The AMS technique (see Chapter 18) was chosen for this coupling because it is specifically
well suited: no normalization of the importance function is needed between the two steps of each batch
since this function is only used for sorting purpose and not for weight management of particles.
The global convergence is achieved by accumulating batches, each one consisting of the two steps.
In the case of criticality computations, the second step is performed only after having discarded the requested
number of batches given by the user (for instance 100 or 200 batches can be discarded).

### 22.19.3 HISTORY OF THE MULTIPLE SIMULATION MODE

The multiple simulation mode was available in previous versions of TRIPOLI-4® and present in the related
user guides, from version 4 to version 9 of the code. The second step of this simulation mode used the
Exponential Transform as variance reduction technique, with the strong limitation of a single energy group
for the importance map (due to normalization constraints in the code), which made this former multiple mode
feature not easy to use and often not very efficient (and with possible variance jump problems). This feature
was then removed from the user guide of versions 10 and 11. Starting from version 12 of the code, the
multiple simulation mode is back, since it has been revisited with the help of the AMS variance reduction
technique (see Chapter 18), which does not need any normalization process and can thus be used as such in
this context.

<!-- page 325 -->
### 22.19.4 SYNTAX

The syntax of the multiple simulation mode is as follows:
SIMULATION
...
MULTIPLE
<number_steps>
*
FIXED_SOURCES_CRITICALITY
*
CRITICALITY DISCARD <nb_discarded>
SCORE
*
NONE
*
<number> <scorename_1>...<scorename_n>
SHIELDING
SCORE
*
NONE
*
<number> <scorename_1>...<scorename_n>
VARIANCE_REDUCTION
*
NONE
*
1 <particle_type> AMS SPATIAL
*
1 <particle_type> AMS <variance_reduction_name>
ENERGY_INF
<particle_type> energy
...
END_SIMULATION
where:
• <number_steps> equals 2 (which is actually linked to a more general syntax of the former multiple
mode of versions 4 to 9 of the code); the same remark applies to the values “1” present in the
VARIANCE_REDUCTION data of the present command block.
• <nb_discarded> is the number of discarded batches in the criticality case (of the first step). This data
is mandatory (and can be 0). During the first discarded batches of the simulation, only the first step is
performed by the code, then the two steps are active and contributions to the scores requested in the
shielding step are taken into account.
• The scores and biasing names must have been defined in the SCORE and VARIANCE_REDUCTION command
blocks (see Chapters 15 and 17) of the input deck.
• The keyword NONE indicates that it is not necessary to choose a score or a biasing.

<!-- page 326 -->
• The AMS can be used either with a spatial importance function (with the keyword SPATIAL) or with
an importance map (in space and energy). In the latter case, it has to be given through an external
importance map, e.g. previously stored with the STORE_IN_FILE option (see Chapter 17) or provided
by another code with the same file format.
• The ENERGY_INF keyword allows for an energy cut-off applying to the second step (shielding calculation
). During the first step (fixed-source criticality or criticality), the lower energy is 10−11 MeV.
Presently, <particle_type> equals NEUTRON.
Remark:
• The multiple mode with AMS needs the presence of an AMS command block (see Chapter 18) in the input
deck.

## 22.20 STORAGE OF PARTICLE EVENTS

The storage of particle events (sources,
collisions and leakage) can be done using the keywords

STORE_SOURCES_IN_FILE,
STORE_COLLISIONS_IN_FILE
and
STORE_LEAKAGE_IN_FILE.
STORE_SOURCES_IN_FILE can be used as a way to restart a simulation from source points (see section
12.6.1). It can also be used to plot particle history events in T4G (see section 38.3.3.3). This feature is
described in the section 31.4.

## 22.21 COUNTING HOLES WITHIN THE SIMULATION OPTIONS

### 22.21.1 OPTIONS HOLE_COUNT, HOLE_MAP, HOLE_VOLU_MAP

Here we present a family of options that allow the user to localize holes and estimate their statistical weight
during the simulation (i.e. the results are bound to the systematic error on the scores of the simulation).
There are several levels of precisions for this counting :
• Hole counting: It counts holes with a precision of Λh, stores and dump the information as a global
output: the Mean hole leakage. It is requested with keyword HOLE_COUNT.
• Hole map: This option allows the user to require the dumping of the position of the different holes
with their respective weight in addition to the Mean hole leakage. It is requested with the keyword
HOLE_MAP.
• Hole map with volumes: Same as above but with the detected nearby volumes. It is requested with the
keyword HOLE_VOLU_MAP.
The method is based on a simple test. As soon as a particle is detected as leaving the geometry, it checks if
there’s a volume at a test point −→
Pt defined as :
−→
Pt = −→
Pp +Λh.−→
Ωp

<!-- page 327 -->
−→
Pp is the position of the particle leaving the geometry and −→
Ωp is its direction.
This test cannot be infinitely precise. It cannot detect holes whose length in the −→
Ωp is superior to Λh and holes
which are closer than Λh from the true boundaries of the geometry.
The Λh value can be set by user with the keyword LAMBDA_HOLE, default value is 10−2. Because of the intrisic
precision of TRIPOLI-4® geometry, εgeo = 10−4, a Λh value inferior to it would be useless and is therefore
not accepted.

### 22.21.2 PROCEDURE FOR TESTING GEOMETRY

This feature can be used as an other form of geometry check (see 7.13). The present alternative is a way of
checking the sanity of complex and extended geometries with the following procedure:
• Do not initialize any useless item for the test: grids (energy, space, angle, time), responses, scores,
boundary conditions, biaising, perturbations, collision bands, verification calculations, outputs, couplings
...
• Place sources in several places inside the geometry. The more sources the more precise hole localisation
will be.
• Replace compositions by vacuum in all volumes thanks to keyword ALL_VOLUMES.
• Add one of the counting options above.
The data set should look like :
GEOMETRY
Geometry to be tested
COMPOSITION 1
POINT_WISE 300 name(compo)
1
name(isotope) 0
END_COMPOSITION
GEOMCOMP
name(compo) ALL_VOLUMES
END_GEOMCOMP

<!-- page 328 -->
SOURCES_LIST nb(sources)
SOURCE
Description of the first source
END_SOURCE
. . .
SOURCE
Description of the last source
END_SOURCE
END_SOURCES_LIST
SIMULATION
BATCH nb(batches)
SIZE size
PARTICLE nb(particles) <PARTICLE_TYPE>
<HOLE_COUNTING_OPTION>
* LAMBDA_HOLE value
END_SIMULATION

<!-- page 329 -->
Defining simulation parameters for the criticality calculation example
SIMULATION
CRITICALITY
BATCH 800
SIZE 500
EDITION 10
PARTICLE
1
NEUTRON
ENERGY_INF
NEUTRON
1.E-11
KEEP_RESULT
END_SIMULATION
