# Chapter foreword — Classification of thermal-hydraulic phenomena for set
<!-- source PDF pages 7-13 -->

<!-- page 251 (PDF 7) -->
the group of experts. As basis for the phenomenon (PH) identification for AWCRs,
earlier works performed within the OECD/NEA framework during 1983 to 1997 were
in detail considered (OECD/NEA, 1987; Lewis et al., 1989; Aksan et al., 1994;
Annunziato et al., 1996; Aksan and D’Auria, 1996). The list of relevant phenomena
established in Aksan and D’Auria (1996) has been taken as basis for the AWCRs work
and been modified according to the reactor types and passive safety systems considered
. It is to be also noted that in identifying the relevant thermal-hydraulic phenomena
in the list which is provided in Section 6.5, expert judgment is the main
contributor.
IAEA-TECDOC-626 provides definitions for safety-related terms as applied to
advanced reactors (IAEA, 1991). In that document, the concepts of passive and active
safety systems are defined and discussed. The definition of a passive safety system is
as follows: Either a system which is composed entirely of passive components and
structures or a system which uses active components in a very limited way to initiate
subsequent passive operation. Four categories were established to distinguish the different
degrees of passivity.
This chapter
will provide some details on the important
and relevant
thermal-hydraulic phenomena for current generation LWRs (e.g., PWRs, BWRs,
and VVERs) including separate effect and integral effect phenomena, AWCRs
(AP1000, ESBWR, EPR, VVER-1200, etc.), and SCWRs (super critical water reactors
). These identified phenomena are the backbone of subject area of the nuclear reactor
thermal-hydraulics and helps to define the research and development activities in
the experimental and analytical field.

## 6.2 Classification of thermal-hydraulic phenomena for set

The basic conservation equations used in thermal-hydraulic two-phase flow models
for analyzing LWR systems under normal and off-normal operating conditions
describe the transport of mass, momentum, and energy of the steam and water.
These local instantaneous partial differential equations are generally integrated
over a control volume of the fluid to result in a set of finite difference equations
(algebraic equations) which can be solved numerically by known algorithms. When
making the integration some kind of averaging procedure is applied which implies
that the resulting equations will loose the capability to resolve phenomena in a
microscale sense. Thus phenomena such as turbulent fluctuations will either be
ignored or integrated into correlations. Only the average three-dimensional,
time-varying characteristics of the flow over a scale dictated by the size of the mesh
cells can be retained. The most commonly used averaging procedure includes
double averages, in time and space. The procedure generates distribution
coefficients for different transport phenomena. These coefficients appear as the
ratio of the averages of products divided by the products of the averages. Due to
lack of information on these coefficients they are usually taken to be unity
(Yadigaroglu et al., 1990).

<!-- page 252 (PDF 8) -->
In earlier two-phase models the fluid was treated as a homogeneous mixture of liquid
and vapor and consequently only three conservation equations were needed to
describe the two-phase flow. In the HEM the phases are assumed to move with the
same velocity and also exist at the same temperature. An extension to the mixture
model is the drift flux model in which the relation between the phasic velocities is
described through an algebraic equation, thus allowing for slip between the phases
(Sonnenburg, 1990). In further developed models, the conservation equations are
set up for each phase separately, and six equations are used (two-fluid two-phase flow
models). Additional equations can be incorporated in the models to account for liquid
solutes and noncondensable gases. The significant property of the two-fluid model is
that it allows the two phases to have different velocities and temperatures. Consequently
, this type of model has the potential to calculate the effects of phase separation
and thermal nonequilibrium.
The two-phase flow model is in most cases simplified to be a one-dimensional
model whether it is a mixture or two-fluid model. Then possible three-dimensional
effects cannot be taken into account, but have to be included by means of special process
models (e.g., special models for simulating the phenomena associated with subcooled
ECC injection into a voided pipe) and by simulating the actual flow path by the
appropriate connections of a number of one-dimensional flow paths.
There are two-phase models that retain some three-dimensional characteristics,
although simplifications in the equations are usually introduced in order to make system
calculations practical. Despite the simplifications, these models have the potential
to simulate three-dimensional effects which can be most important, for example, in
some time windows of a LBLOCA, where flow redistributions are supposed to occur
in the reactor vessel.
In order to solve the set of finite difference equations, closure or constitutive equations
are required, along with relations describing the steam-water properties under
different conditions. In this context the steam-water properties are assumed to be well
known for most of the application ranges and associated tables and functions are supposed
to be adequately programmed in any of the used codes. The same is also
assumed to be true for needed derivatives of the properties.
The constitutive equations describe the HT between wall structures and the
two-phase fluid, the interphase mass, momentum, and HT, and the wall to fluid drag.
The wall HT and the wall drag to each phase are dependent on the extent of the wall
contact of the phase and the associated transfer process, whereas the interphase
exchange of mass, momentum, and energy depends on the interfacial area along with
associated interphase transport processes. In view of the averaged nature of the conservation
equations as mentioned above, the wall contact of the phases and the interfacial
area has to be expressed as volume based or averaged quantities. The adequate
description of the interfacial area density, and thus the prevailing flow regimes, and
the wall to fluid and interphase transport processes is one of the most important
requirements for accurate modeling of the two-phase flow behavior.
Most of the constitutive equations are based on correlations with different levels of
empiricism, from pure empirical models to models based on physical principles and
with possibly only a few constants that have to be evaluated from experimental data.

<!-- page 253 (PDF 9) -->
Pump degradation curves at two-phase conditions are examples of the former while
models for frictional PDs can be examples of the latter. In some cases, the inherent
capabilities of the two-fluid model are not fully exploited and a separate special process
model or correlation is utilized. An example is the modeling of critical flow
(Yadigaroglu et al., 1990). The integration of the two-fluid conservation equations
is able to predict a choked condition. Choking calculations in a component with a
smooth area change could be done by using a sufficiently fine axial mesh and noting
the occurrence of the critical conditions. However, this requires a very fine mesh to
adequately predict the critical conditions.
The interactions of different correlations along with the conservation equations
will constitute a code’s capability to simulate important phenomena during the course
of an LOCA or transient. lt is essential to identify each relevant PH and to ascertain
that the specific PH is adequately simulated by the code. This is usually done by comparing
the code’s results from simulations of well-defined tests carried out in properly
designed test facilities with the test data. In this context a distinction is made between
integral tests and SETs.
Integral tests are carried out in scaled test facilities and provide data on the overall
behavior of a simulated reactor system during an LOCA or transient. These tests are
being used for code assessment purposes relating to overall reactor behavior.
A definition of sets of such tests (matrices) has been provided in OECD/NEA
(1987). These facilities have a complicated configuration and are expensive to operate
. Compromises, for instance with respect to scaling to real plants, are inevitable.
Also the instrumentation for measurements of parameters governing different
two-phase flow phenomena is limited. This makes the integral tests less suitable
for detailed investigations of specific two-phase flow phenomena. As a consequence,
this also requires in assessment analyses that the code user is very confident of which
phenomena prevail during the course of a transient in order to avoid “good results but
for the wrong reasons” (compensating errors).
SETs are employed not only to develop correlations of specific processes but also
to investigate individual or localized two-phase phenomena which in most cases are
dependent on several specific processes. These kinds of tests are also used to characterize
the behavior of single components such as pumps or steam separators.
The interactions with other phenomena or components as in a full-scale LWR are
either imposed by external boundary conditions on the test, or are purposely eliminated
. In fact, an important consideration in the design of SETs is to have
well-defined boundary conditions. In some cases, the test section in a SET is locally
in full scale or very near to full scale. This minimizes the concern about scale effects.
On the other hand, in all SETs it is important to evaluate the influence of the chosen
boundary conditions on measured parameters.
In SETs the instrumentation for measurements of two-phase flow parameters can
be quite extensive. Thus data for assessment of details of the models used in the codes
to simulate localized phenomena can be provided, and this can help in understanding
the interactions of different processes that combine to produce the overall phenomena
of interest. The data have also proved to be valuable when evaluating prediction
uncertainties of specific phenomena at or near full scale.

<!-- page 254 (PDF 10) -->
As part of the definition of integral test matrices in OECD/NEA (1987), different
phenomena were identified. In particular, phenomenological windows were distinguished
in the case of:
–
LBLOCAs in PWRs,
–
small- and intermediate-break LOCAs and transients in PWRs,
–
LOCAs in BWRs,
–
transients in BWRs.
TypicaI scenarios simulated in the integral test facilities constituted the basis for this
analysis. The consideration of presumed evolution paths of accidents in the reference
plants (PWRs and BWRs) also played a role in this connection. The phenomena
were identified essentially on the basis of the experience of the individual members
of the Writing Group that was formed to investigate the simulated scenarios. Those
identified phenomena formed a first basis for a more detailed list of relevant
phenomena.
An expansion of that list covering different important LOCA phenomena was presented
for both BWRs and PWRs in Lewis et al. (1989). A weighting and appraisal of
each PH were also included. The main support for these phenomena was provided by a
number of integral and SETs. That list of phenomena is the basis for the one given in
Table 6.1. Only minor modifications were introduced in the list. Apart from some
rearrangement a new group named “Basic Phenomena” has been added. Each PH
in this group can be characterized as independent of other phenomena and is of a constitutive
nature for the two-phase flow.
In this section, the identification of the relevant two-phase flow phenomena is
made and a short description of each PH is provided. A total of 67 phenomena is
identified and the resulting phenomena list is given in Table 6.1. As stated above
the identification is based on the phenomena list in OECD/NEA (1987). All representative
phenomena occurring during an LOCA or transient is included, although
several phenomena are combined under a general heading in some cases such as various
instances of countercurrent flow limitation (CCFL), and of critical flow. lt
should also be realized that some phenomena are dependent on each other, for
instance spray effects and condensation. lt will be seen that there are several different
types of phenomena, varying from those such as interphase friction which is a very
basic attribute of a two-phase flow, to those such as loop seal clearing, which is
essentially a system PH, localized in its occurrence but very dependent on events
and conditions elsewhere in the loop. In such cases the influences from the loop have
to be provided as boundary conditions.
Some groups of phenomena are linked. In this case an introductory description
prefaces the group to avoid repetition of material. For instance, CCFL can occur
at a variety of locations in an LWR. CCFL is very geometry dependent and encompasses
a wide range of situations, requiring data from different types of SET facilities.
Nevertheless, some aspects of CCFL are common to all these circumstances.
In some cases, there is an apparent overlap of the phenomena description, since the
same PH occurs in combination with other phenomena. The intention has been,
though, to provide the information without repetition, as far as possible.

<!-- page 255 (PDF 11) -->
Table 6.1 List of thermal-hydraulic phenomena
Basic phenomena
Evaporation due to depressurization
Evaporation due to heat input
Condensation due to pressurization
Condensation due to heat removal
Interfacial friction in vertical flow
Interfacial friction in horizontal flow
Wall to fluid friction
Pressure drops at geometric discontinuities
Pressure wave propagation
Critical flow
Breaks
Valves
Pipes
Phase separation/vertical flow with and without
mixture level
Pipes/plena
Core
Downcomer
Stratification in horizontal flow
Pipes
Phase separation at branches
Branches
Entrainment/de-entrainment
Core
Upper plenum
Downcomer
Steam generator tube
Steam generator mixing chamber (PWR)
Hot leg with ECCI (PWR)
Liquid-vapor mixing with condensation
Core
Downcomer
Upper plenum
Lower plenum
Steam generator mixing chamber (PWR)
ECCI in hot and cold leg (PWR)
Continued

<!-- page 256 (PDF 12) -->
Table 6.1 Continued
Condensation in stratified conditions
Pressurizer (PWR)
Steam generator primary side (PWR)
Steam generator secondary side (PWR)
Horizontal pipes
Spray effects
Core (BWR)
Pressurizer (PWR)
Once-through steam generator secondary
side (PWR)
Countercurrent flow/countercurrent flow limitation
Upper tie plate
Channel inlet orifices (BWR)
Hot and cold leg
Steam generator tube (PWR)
Downcomer
Surge line (PWR)
Global multidimensional fluid temperature, void,
and flow distribution
Upper plenum
Core
Downcomer
Steam generator secondary side
Heat transfer:
Natural or forced convection
Core, steam generator, structures
Subcooled/nucleate boiling
Core, steam generator, structures
DNB/dryout
Core, steam generator, structures
Post-critical heat flux
Core, steam generator, structures
Radiation
Core
Condensation
Steam generator, structures
Quench front propagation/rewet
Fuel rods
Channel walls and water rods (BWR)

<!-- page 257 (PDF 13) -->
Lower plenum flashing
Guide tube flashing (BWR)
One and two phase impeller-pump behavior
One and two phase jet-pump behavior (BWR)
Separator behavior
Steam dryer behavior
Accumulator behavior
Loop seal filling and clearance (PWR)
ECC bypass/downcomer penetration
Parallel channel instabilities (BWR)
Boron mixing and transport
Noncondensable gas effect (PWR)
Lower plenum entrainment
