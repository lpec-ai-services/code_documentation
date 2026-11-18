# Chapter foreword — Characterization of thermal-hydraulic phenomena for set — Basic phenomena … Entrainment/de-entrainment
<!-- source PDF pages 14-30 -->

<!-- page 258 (PDF 14) -->
## 6.3 Characterization of thermal-hydraulic phenomena for set

A brief description of each of the 67 phenomena listed in Table 6.1 is provided in this
section.
This indicates the interpretation that has been put on the PH for the purposes of
assessing suitable SET data. Thus, for example, it will be seen that the term horizontal
stratified flow has been used to include the PH of thermal stratification as well as
aspects of two-phase stratified flow associated with the presence of a surface. The
description also indicates where in a reactor system, and under what circumstances,
the PH is likely to occur. The discussion of the PH should indicate features such as the
degree of scale or geometry dependence, which affect the range of data likely to be
necessary for code model validation.
Some groups of phenomena are linked. In this case an introductory description
prefaces the group to avoid repetition of material. For instance, CCFL can occur
at a variety of locations in an LWR. CCFL is very geometry dependent and encompasses
a wide range of situations, requiring data from different types of SET facilities.
Nevertheless, some aspects of CCFL are common to all these circumstances.
In some cases, there is an apparent overlap of the phenomena description, since the
same PH occurs in combination with other phenomena. The details and specifics of
overlaps and clarifications are provided in detail for each specific PH.

### 6.3.1 Basic phenomena

Basic phenomena are the transfer processes at the interface between different fluids
(liquid and steam or a noncondensable gas) and solid surfaces facing the fluid. They
comprise momentum, heat, and mass transfer which have been divided into evaporation
due to depressurization (Section 6.3.1.1), evaporation due to heat input
(Section 6.3.1.2), condensation due to pressurization (Section 6.3.1.3), condensation
due to heat removal (Section 6.3.1.4), interfacial friction in vertical flow
(Section 6.3.1.5), interfacial friction in horizontal flow (Section 6.3.1.6), and wall
to fluid friction (Section 6.3.1.7), PDs at geometry discontinuities (Section 6.3.1.8),
and pressure wave propagation (Section 6.3.1.9).
In the six equation models used in some thermal-hydraulic safety computer codes,
the constitutive laws are intended to model these basic transfers between phases. The
method of discretization for the fluid dynamics, and the numerical solution, significantly
affect the calculation of pressure wave propagation.
Basic phenomena govern all the fluid behavior during an accident sequence, so
they are inevitably important for nuclear safety.
In most cases of practical interest there is no direct measurement of basic phenomena
for two-phase flow. They can be only evaluated on the basis of global measurements
(e.g., DP, P, T).
Models are necessary to evaluate the basic transfers from the global measurements.
From these models correlations are set up. But it is important to realize that the use of

<!-- page 259 (PDF 15) -->
these correlations is not independent of the chosen model. Normally the correlations
should be used in a way which is consistent with their derivation. Usually the basic
phenomena (Sections 6.3.1.1–6.3.1.7) are treated as independent of modeling.
With the present state of knowledge, models employed in codes give a large range of
differences on evaluation of basic phenomena, Forge et al. (1988). But the global
thermal-hydraulic behavior is nevertheless predicted quite similarly by different
approaches, Ambrosini et al. (1988).

#### 6.3.1.1 Evaporation due to depressurization

A good illustration of the PH is the case of water and saturated steam in an adiabatic
cylinder with a piston. By increasing the volume with the piston, one can observe a
sudden pressure decrease followed by a pressure increase due to vaporization of the
liquid. The common understanding is that there is a delay before vaporization begins
and then a gradual return to thermodynamic equilibrium. The delay depends on water
purity which means that the presence and the number of microscopic nucleation sites
play a roll.
In a closed cylinder of fixed dimensions, the pressure variation can be obtained by
extracting a certain amount of liquid at the bottom or steam at the top.
Another way to depressurize the two-phase fluid is to use a steady-state flow in a
Venturi nozzle. In this case the fluid acceleration is the main source of depressurization
and induces steam evaporation. A strong gradient of pressure can be obtained in a
steady state with this process.
In the real experiments, the perfect adiabatic situation is not reached. There is
always heat exchange with walls, and heat losses.
In blowdown experiments the flow can enhance transfer phenomena between
phases.
This PH gives a major contribution to the general behavior during the course of an
accident, for example, pressure evolution, upstream flow conditions at the breach,
stagnation point for LBLOCAs.
This PH is easily predicted under the thermal and mechanical equilibrium conditions
that occur in slow transients (in which mass and energy conservation are important
but the kinematics are not). It is the prediction of departures from the equilibrium
behavior that is of particular interest in the safety context.

#### 6.3.1.2 Evaporation due to heat input

Evaporation of liquid due to heat input is one of the most essential phenomena occurring
both in normal and off-normal operation of LWRs. The evaporation or boiling
process on a heated surface is a very effective HT mode with more than one order
of magnitude higher HT coefficient than for single-phase convection. On the other
hand, at high heat flux on the heated surface, or when a high vapor content has accumulated
under forced flow conditions, a sudden deterioration of the effective boiling
HT mode can occur which can be hazardous to the heated surface.

<!-- page 260 (PDF 16) -->
Because of its contribution to determining boiling HT and dry-out phenomena, a
relatively detailed description of the nucleation process is given below. HT from a
heated surface is described in Section 6.3.12.
The evaporation process implies that vapor bubbles can be created and then are able
to grow within the liquid. This requires that bubble nuclei are present and that the surrounding
liquid is somewhat superheated. The nucleation process is described in terms
of the difference of free energy between existing small vapor clusters in a liquid and
the surrounding liquid (Hsu and Graham, 1986).
The free energy will reach a maximum as a function of increasing vapor cluster
radius and then decrease. When the cluster radius is less than this critical radius,
the natural tendency is for the vapor cluster to collapse since this will reduce free
energy. On the other hand, if the cluster radius is greater than the critical value, an
increase in the cluster size will also reduce free energy and thus a spontaneous growth
of the cluster will occur. The vapor clusters with sizes greater than the critical value
will serve as nuclei for vapor bubbles.
In the case when a solid heated surface is immersed into a liquid, the free energy
difference required for nucleation is usually smaller than for the case of a homogeneous
liquid. The reason is that on the solid surface small cavities exist which will
act as nucleation sites. The liquid temperature gradient across the thermal boundary
layer adjacent to the heated surface will determine the bubble growth.
When a bubble leaves the heated surface (or collapses) relatively cold liquid will
replace the space earlier occupied by the bubble. This liquid is gradually heated by
transient conduction until the temperature is high enough to allow for a new bubble
to grow. The period until the appearance of the second bubble is called the waiting
period. Following the appearance of the bubble, the growth period starts. During this
period the bubble will grow because of evaporation taking place at the vapor-liquid
interface and also to some extent from the microlayer of liquid at the bubble base.
The adjacent liquid is subjected to enhanced convection because of bubble agitation.
The growth period terminates with bubble departure or collapse. Then the process
repeats itself and a new bubble is created.
When the thermal boundary layer temperature is increased, more nucleation sites
are activated. The bubble frequency at each site is increased, while the waiting period
is decreased. A multibubble region will be established in which the creation of one
bubble is strongly influenced by existing adjacent bubbles. Also coalescence of bubbles
in the thermal boundary layer will occur, and this will be increased with heat flux.
As a result liquid access to the heated surface will be restricted and momentary dry
patches will begin to form. When this situation is reached the heat flux is approaching
the critical heat flux (CHF).
The evaporation process due to heat input is a basic PH that contributes substantially
to determining the overall course of an accident or transient event. The evaporation
and coalescence of bubbles occurring at small scales give rise to different
macroscopic two-phase flow regimes. The associated HT in the different regimes
determines the maximum fuel temperature encountered during subsequent phases
of a transient and, for example, the quenching velocity of the fuel during the reflood
phase of an LOCA. The evaporation is also a basic process when a three-dimensional

<!-- page 261 (PDF 17) -->
distribution of vapor and liquid is developed in pressure vessel plena after an accident
and in a steam generator (SG) secondary side.

#### 6.3.1.3 Condensation due to pressurization

In the case of the experiment described in Section 6.3.1.1, by reducing the volume
with the piston, one can observe a sudden increase of pressure followed by a small
decrease due to condensation of steam. In a closed cylinder of fixed geometry, the
pressure increase can be obtained by injection of saturated water at the bottom or saturated
steam at the top. This effect is also very sensitive to the film condensation process
which occurs as walls become subcooled when pressure increases. It is possible
that this condensation process is more important than the condensation at the interface.
In real experiments the same remarks as in Section 6.3.1.1 apply. The pressurization
is, generally, due to injected subcooled water (e.g., safety injection).
The PH contributes to the general behavior of the pressurizer (PRZ) which governs
the pressure evolution of transients such as anticipated transients without scram
(ATWS), and feed and bleed procedures for transients such as a loss of feedwater
(LOFW). Pressure recovery in the upper head at the end of some transients and SG
secondary side behavior in the case of tube rupture are related to this PH, and void
collapse in the upper head during refill and reflood of the core at high pressure
may delay core recovery.

#### 6.3.1.4 Condensation due to heat removal

Condensation of vapor due to heat removal is an essential PH occurring in certain
phases of normal and off-normal operation of LWRs and in various types of condenser
equipment. The mode of condensation can be classified as dropwise or film-wise condensation
on a solid surface, or as direct contact condensation on the surface of a
subcooled liquid.
Dropwise and film-wise condensations are obtained on surfaces with temperatures
below the saturation temperature in a superheated or saturated vapor environment.
The exact mechanism of initiation of condensation is not yet fully understood. However
, the consensus view is that the initiation of condensation starts in small surface
cavities which contain liquid with enough subcooling. The magnitude of the subcooling
depends on the curvature of the liquid surface that faces the vapor.
If the condensed liquid does not wet the surface the condensate will form droplets
that run off the surface depending on the surrounding flow velocity, surface conditions
, and surface inclination. This is known as dropwise condensation.
If the liquid wets the surface, or the dropwise condensation is intense enough, a
continuous liquid film will be created and will cover the surface. This mode of condensation
has a much lower HT coefficient than the dropwise mode. However,
film-wise condensation is the predominant mode and is usually assumed when specifying
correlations for condensation HT coefficients on a surface. These correlations
are almost entirely based on Nusselt’s theory.

<!-- page 262 (PDF 18) -->
Direct contact condensation is obtained when existing subcooled liquid droplets
are passing through a saturated or superheated vapor environment. An example of this
kind of condensation will be the spraying in a PWR PRZ. Relatively cold liquid will be
provided as spray by means of spray nozzles in the PRZ top. The condensation will
take place at the surface of the droplets and the temperature of the droplets will gradually
increase as the droplets pass through the vapor phase. The spray flow rate is normally
rather high compared with the amount of vapor being condensed and hence the
droplet radius will increase only by a small amount.
The amount of condensed vapor will depend on the temperature difference between
the vapor and liquid droplets, the droplet size, the droplet transit time in the vapor
phase, and on vapor and liquid properties.
The condensation processes due to heat removal are important during some parts of
the course of evolution of an accident in LWRs and generally in condensers.
In condensers the condensation of vapor takes place on the shell side while the
cooling liquid passes on the tube side in the usually horizontal tubes. The tubes are
often arranged in a triangular pattern in such a way that the condensate can drain
as freely as possible due to gravity and at the same time allow for high vapor velocities
at low PDs within the condenser.
During the course of a small-break loss of coolant accident (SBLOCA) in a PWR, a
situation can occur where vapor from the more or less uncovered core flows through
the hot leg and condenses on the hot-leg side of the SG tubes. The condensed liquid
flows back due to gravity along the tube wall and back through the hot leg to the core.
This mode of cooling the core is quite effective and is characterized as the reflux condensation
mode. The condensation in the SG tubes will basically be of the
film-wise type.
The spray process is important in PRZ control and for the effectiveness of emergency
core cooling in BWRs.

#### 6.3.1.5 Interfacial friction in vertical flow

The momentum transfer between phases is principally a function of relative velocity
between steam and water, of fluid densities and of a so-called interfacial friction coefficient
which is highly dependent on flow regime. For vertical flow the basic flow
regimes are bubbly flow, slug flow, chum flow, annular flow, and inverted annular
flow (Govier and Aziz, 1976). The interfacial friction in general is highest in those
flow regimes which result in high interfacial areas. In relating the interphase friction
to the difference in average phase velocities, the effect of nonuniform velocity (velocity
profile) needs to be considered, as does the effect of averaging flow structures (e.g.,
use of a single droplet diameter). Although interfacial friction is a basic PH, it is still a
highly complex one, in which much simplification must be done to reduce it to a
one-dimensional two-fluid description.
The interfacial friction has a direct influence on carryover and carryunder: entrainment
and de-entrainment of water by steam. During core uncover, the swell level is
related to interfacial drag. If the friction is high, the swell level is higher. This PH,
coupled with wall friction, also influences CCFL.

<!-- page 263 (PDF 19) -->
To study the fundamentals of this PH air-water flow is useful (no heat and mass
transfer).
Interphase friction is a key PH affecting the overall fluid behavior in a system under
two-phase conditions, and its correct modeling is crucial for the adequate prediction of
a number of other phenomena. This PH, together with wall-to-fluid friction (see
Section 6.3.1.7), contributes to determining PD for two-phase flow in vertical situations
. It governs phase separation and swell level particularly in the core, and so it is of
high relevance for reactor safety.

#### 6.3.1.6 Interfacial friction in horizontal flow

On the same physical basis as described in Section 6.3.1.5, the interfacial friction in
horizontal flow is highly influenced by flow regime. Possible flow regimes are bubbly
flow, plug flow, stratified flow, wavy flow, slug flow, and annular flow (Delhaye
et al., 1981). It also influences countercurrent flow (CCF) in stratified conditions,
and CCFL (Hewitt, 1989). At high flow rates horizontal and vertical flows behave
similarly. There are major differences, resulting from the effects of phase separation,
at low flows.
This PH, together with wall-to-fluid friction (see Section 6.3.1.7), contributes to
PD for two-phase flow in horizontal conditions. It plays a role in the reflux condenser
heat removal mode and also in the rate at which water can drain from the upper parts of
the circuit to the core.

#### 6.3.1.7 Wall-to-fluid friction

Wall-to-fluid friction causes, as is well known, a force opposite to the direction of the
motion of the fluid. In single-phase fluid dynamics, the force is known to be dependent
upon the cross-section average squared velocity and fluid density and upon external
parameters. These parameters are the roughness of the walls and the equivalent diameter
of the flow duct. The fluid viscosity also plays a role in the determination of the
friction coefficient.
In two-phase flows, the wall-to-fluid interaction may depend greatly upon flow
regime and local void fraction.
The PH gives a significant contribution to the overall PDs in a plant during normal
and off-normal conditions. Essentially, three kinds of geometric situations can be distinguished
in a nuclear reactor system concerning the wall-to-fluid friction:
(a) large plena,
(b) piping,
(c) core and SGs.
The last item (c) is characterized by small values of equivalent diameter.

#### 6.3.1.8 PDs at geometric discontinuities

Important pressure variations occur due to abrupt changes of geometry in any
thermal-hydraulic
system
including
variations
of
curvature.
Void
fractions,
cross-section profile of the fluid velocities and geometric peculiarities of the system

<!-- page 264 (PDF 20) -->
(e.g., shape of the edges that constitute the discontinuity) are among the main parameters
that affect the PH.
Strong three-dimensional flow paths may occur in the proximity of abrupt geometry
variations making difficult analytical modeling and a complete experimental
characterization of the PH.
The prediction of this PH is essential to evaluate scenarios in the plant. The following
main zones are relevant as far as local PDs are concerned:
(a) inlet and outlet of the core;
(b) inlet and outlet of the vessel;
(c) inlet and outlet of the U-tube bundle in primary and secondary sides of PWR SGs;
(d) bypass flow paths, mostly inside the vessel;
(e) special components like pumps, steam separators, and valves.

#### 6.3.1.9 Pressure wave propagation

Because the primary system’s coolant is subcooled everywhere except in the PRZ,
extremely rapid decompression occurs following an almost instantaneous rupture
of the primary system piping. The pressure can fall well below the hot-leg saturation
pressure (12 MPa), to around 5 MPa. The subsequent motion of decompression waves
through the piping and vessels induces severe dynamic loads on their internal structures
. The larger the breach, the larger are the instantaneous differences of pressure
applied to structures. The decompression waves have a smaller effect for smaller
breaches. On the secondary side in the case of a steam line break, pressure waves
can propagate and induce dynamic loads on elbows.
Later in the transient in the case of a large amount of steam in the primary or secondary
side, the injection of the cold water can cause a condensation shock and a
related water hammer, for example, on dead ends or bends.
The BWR vessel has the same features as the secondary side of SGs in PWRs as far
as the propagation of pressure waves is concerned. Sudden condensation and evaporation
are a consequence of the transit of pressure waves attenuation of the amplitude
is strongly affected by the geometry and by the average value of void fraction (including
the degree of subcooling) in a given volume.
Core internals have to be designed to withstand these dynamic loads without severe
deformation in order to ensure that a coolable geometry is retained during a large
breach LOCA. Severe deformation could also prevent the control rods from entering
the core. For most plants the control rods are not essential during a LBLOCA in a
PWR, because coolant voids and the boron injected with the ECC water will make
the reactor subcritical anyway. It is nevertheless good engineering practice and essential
for small breaches to ensure that the reactor is scrammed.
Condensation shock and related water hammer can damage pipes and some problems
have been experienced on the secondary side for some plants.
Positive pressure propagation causes void collapse in the BWR core and may be the
origin of a significant neutron flux excursion. The interaction between neutronics and
thermal-hydraulics in the case of instability may also be affected by the propagation of
small pressure waves (e.g., initial perturbation).

<!-- page 265 (PDF 21) -->
Furthermore, especially in the case of LBLOCA (steam line or recirculation line
break), pressure wave propagation from the break toward the vessel may cause significant
loads on internal structures and damage to the systems relevant to safety.

### 6.3.2 Critical flow

When a flow discharges from a reservoir at higher pressure to a reservoir at lower pressure
through a joining pipe, providing the pressure difference is not too large, the rate
of flow will be determined by the size of the pressure difference and (inter alia) the
wall frictional losses at the pipe walls, entrance, and exit. If the ratio of the upstream to
downstream pressure is large enough, however, the flow is found to be independent of
the downstream reservoir conditions, and the flow is said to be critical, or choked. In
single-phase flow this condition is simply interpreted: the speed of the flow at some
point along the flow path, the choke plane, is then equal to the maximum speed at
which pressure disturbances can propagate within the flow. Such a situation is conceptually
simpler in the case of flow through a pipe, where the flow is essentially
one-dimensional, than for flow through a short constriction such as a break in the side
of a pipe, or a valve, where multidimensional effects can be more important (Brittain
et al., 1982).
The three cases of breaks, valves, and pipes are treated separately below. For the
purposes of discussion the term “pipe” is taken to apply to a constant cross-section
duct with a length to diameter ratio (L/D) greater than 5. In practice there will be a
gradual change in behavior as the length of a duct with critical flow at exit is increased
from L/D<1 to L/D≫1, and the choice of 5 is rather arbitrary. Length of the flow path
affects velocity profile development, the degree of thermal disequilibrium between
phases, and the importance of wall friction. Two possible sites for choking in a
LBLOCA, in addition to the break itself, are the PRZ surge line and the pump. No
specific SETs relating to either of these two cases have been found. The PRZ surge
line should in principle be covered by the database for critical flow in pipes. The pump
rotor and diffuser have a more complex geometry, and present problems akin to those
encountered in valves. In addition the rotor may be spinning or locked.
The CSNI published a State of the Art Report on critical flow modeling in OECD/
NEA/CSNI (1982) which covered both critical flow models and experimental data. An
extended review of the models is reported in the technical addendum to this report
(D’Auria and Vigni, 1980).

#### 6.3.2.1 Critical flow in breaks

When a break occurs in a separating wall structure between a high and low pressure
system the flow through the break will be dependent on conditions upstream the break
and on the break area and shape. Critical flow through a break is similar to critical flow
through a nozzle, but because the geometry of the break can encompass any shape,
location, and size from a small crack to a complete 200% guillotine break in a flow
pipe, multidimensional effects and losses are important but also difficult to account for
accurately.

<!-- page 266 (PDF 22) -->
For a guillotine break in a large pipe the flow will pass across the entire break area
cross-section in a rather homogeneous way but for a small break the geometry of the
break and the upstream flow pattern close to the break is of great importance. At low
flow rates stratification effects upstream of the break are crucial to the flow rate.
Under such conditions, the orientation of the break relative to the liquid-vapor interface
governs the actual flow rate and this is also likely to change during the course of
drainage through the break. Two-phase flow processes influencing the flow rate
through a break in a horizontal pipe include upstream flow regime transitions, liquid
entrainment in the break flow, and vapor pull-through.
The critical flow through breaks is a very important element in analyzing plant
behavior during the course of the complete spectrum of LOCAs. The break flow determines
the depressurization rate of the system and the time to core uncovery which in
turn are of major concern for when and how different mitigation auxiliary systems will
be initiated and function. Because of the empirical nature of critical flow models as
well as the arbitrariness in location, orientation, shape, and size of a break, the licensing
requirements of a plant include that a spectrum of postulated breaks is analyzed. It
is important that in such analyses that the envelope of the influences from the break
conditions can be found.

#### 6.3.2.2 Critical flow in valves

Critical flow through a valve is essentially no different from critical flow through a
nozzle, but because the geometry of the flow path through a valve is variable, and
usually more complicated than a nozzle, multidimensional effects and losses are likely
to be more important and more difficult to account for. Several studies have shown
that the choking position and the effective minimum area in a valve are not always
easy to determine. They may even vary with downstream conditions. There are many
different types of valves, and because of the uncertainties inherent in using 1-D
models, data from at least a scaled version of the relevant geometry is highly desirable
if reasonably accurate critical flow predictions are required.
Critical flow through valves is an important element in many analyses of plant
behavior. In safety assessments it is central to the stuck open PRZ valve LOCA,
ATWS, LOFW, and accident recovery procedures based on dumping primary side
coolant.

#### 6.3.2.3 Critical flow in pipe

In a constant cross-section pipe choking is expected to occur at the pipe exit. In this
case the flow rate is still influenced by the entrance losses and wall friction in the pipe
since these produce a fall in pressure before the choke point is reached. Thus L/D is an
important parameter in determining critical flow from pipes. Pipe length is also important
in determining the degree of thermal and mechanical disequilibrium in the critical
flow. The experimental evidence suggests that unless the pipe is very short, even in the
absence of significant wall friction the phases will approach thermal equilibrium at the
choke plane. The relative importance of length, and length to diameter ratio are

<!-- page 267 (PDF 23) -->
discussed in Holmes and Allen (1990). It is also assumed that for critical flow in pipes
slip ratios are close to unity.
The subject of critical flow through cracks is closely related to that occurring in
pipes, being dominated by friction and the attainment of thermal equilibrium.
A pipe break is a prime mechanism for initiating an LOCA. The pipe involved
could be a main coolant pipe, in which case complete severance leads to a LBLOCA,
or a pipe connected to the main coolant loop (e.g., an emergency core cooling system
(ECCS) line) which could lead to an intermediate or SBLOCA. The flow rate from the
pipe is an important factor in determining the course of the resulting transient. The
way in which the flow evolves as a function of time can be different for the case
of a small broken pipe from that corresponding to a small hole in a large pipe even
when the initial break flow is the same in both cases. In many licensing applications
the actual flow rate through a break of a given size is not required because what is of
interest is the behavior of a plant for a range of break sizes. Exceptions are the determination
of the maximum flow from particular types of break (for instance from an
instrument penetration in the pressure vessel), and the likely flow from a broken
SG tube.

### 6.3.3 Phase separation/vertical flow with and without mixture level

Flow regimes in two-phase conditions are included under the title “phase separation/
vertical flow with and without mixture level”; this comprises the limit case of stagnant
or nearly stagnant two-phase mixture when all the liquid is collapsed in the bottom of
the vertical component. The consideration of the so-called mixture level is also part of
this section.
Three subsections have been distinguished owing to their relevance in nuclear reactor
thermal-hydraulics and to the differences in the flow regimes that are a consequence
of the geometry and of the boundary conditions (essentially, heat input in
the case of the core)
–
pipes and plena,
–
core,
–
downcomer of the vessel.
The first item essentially includes the SG tubes, both primary and secondary sides, and
the vertical parts of the PRZ surge line and of the hot and cold legs of PWR main loops.
The subitem plena include all the zones of the primary and secondary sides where the
fluid velocities are substantially lower than the neighboring zones. Examples of this
are the lower and UP of the vessel (in both BWR and PWR), the steam dome of the
SGs, the inlet and outlet chamber of the SG primary side, and the PRZ. Stratified conditions
are typical of plena, particularly the lower plenum (LP) of both PWR and
BWR, while several slow regimes may occur and are important in vertical pipes
and in other types of plena (e.g., SG chambers, see also Section 6.3.7.5).
All flow and HT regimes occur in the core region of BWR under nominal conditions
and are expected for PWR during off-normal conditions (second item). The

<!-- page 268 (PDF 24) -->
difference between the two kinds of reactor is the possibility of cross slow in PWR that
is inhibited in BWR owing to the presence of the fuel boxes.
The third item has been introduced mainly to take account of the complex
three-dimensional situations occurring in a PWR vessel downcomer during several
kinds of accidents: the ECC bypass/downcomer penetration, specifically considered
as item 21 in Table 6.1, is an example of this.
6.3.3.1
Phase separation/vertical flow with and without mixture
level—pipes and plena
Steam and liquid phases remaining at rest or flowing cocurrently in vertical channels
tend to separate owing to either the gravity force or the inertia forces, both essentially
driven by the different density of the two phases. With the phases at rest or moving at
very low velocity, gravity dominates and the PH is very simple with the lighter phase
stratifying in the upper part of the available volume. Essentially, the only physical
aspect to be considered in modeling this situation is the time required to reach a stable
condition starting from mechanical nonequilibrium (e.g., liquid in the upper part of a
voided system).
The situation is much more complex in a flowing system: various flow configurations
may occur as a function of system parameters (e.g., equivalent diameter, flow
area, geometric flow path, wall HT, etc.), of the fluid thermodynamic parameters
(e.g., pressure, liquid and steam velocities, void fraction, etc.) and of the fluid properties
. The well-known flow regime zones are the result of the interaction of the
parameters mentioned. The formation of a mixture level is also a consequence of
the interaction between the phases in flowing and/or wall-heated two-phase fluid systems
. Finally, special flow regimes may occur in the case of strong mechanical and/or
thermodynamic nonequilibrium such as in the case of abrupt area change or reflood.
The PH is relevant to nuclear reactor safety because of the significant dependence
of the values of PDs and HT upon the flow regimes. The prediction of flow regime
may be important in the case of BWR (nominal conditions) or BWR and PWR (conditions
of accidents without scram) in the evaluation of local void fraction, and as a
consequence, in predicting neutron flux.

#### 6.3.3.2 Phase separation vertical flow with and without mixture level—core

Phase separation in the core will develop during some phases of an LOCA in PWRs
and under normal and off-normal conditions in BWRs. The separation effect is caused
by gravity, inertia, or drag dominated forces acting on the phases along with the density
difference between the phases.
At low flow velocities and accelerations, gravity will cause the phases to stratify
. If the transient is slow enough there may also be time for thermal nonequilibrium
to develop. Vapor and droplets can be driven out of the mixture
creating a mixture level. This type of separation can be found, for example, toward
the end of the blowdown phase of an LOCA. The rate of phase separation will

<!-- page 269 (PDF 25) -->
depend on parameters controlling the velocity of rising bubbles in the liquid and
the stability of the separated flow interface, such as bubble size, geometry, and
different types of drag (form, interfacial, and wall) and pressure gradient. The
HT from the fuel cladding to the fluid is highly dependent on the location of
the mixture level. Below the level, the HT coefficient can be quite high, resulting
in moderate fuel temperatures, whereas the conditions above the level can be the
opposite.
At higher flow velocities the vapor-liquid interface will be distributed in
the flow creating complex two-phase flow patterns which are dependent on different
parameters. Governing system parameters are, for example, core flow area and
geometry, possibly spacer vanes characteristics, etc., while fluid thermodynamic
parameters are pressure, phase velocities, void fraction, etc. This flow behavior
is typical in BWRs at normal and off-normal conditions and in PWRs at LOCA
conditions.
Another form of phase separation that can occur in the core is droplet entrainment
and de-entrainment. In this case liquid droplets can be entrained from for instance a
mixture surface by means of the vapor flow. The liquid droplets carried along in the
vapor flow will enhance the downstream cooling of the core.
The phase separation in the core is crucial for the fuel-coolant HT during some
phases in LOCAs in both PWRs and BWRs and during normal operation in a
BWR. This process determines for instance the quenching of the core during an LOCA
and consequently has great impact on the fuel maximum temperature.

#### 6.3.3.3 Phase separation vertical flow with and without mixture level—downcomer

Phase separation with and without mixture level in vertical flow is mainly determined
by gravity or inertia forces, both essentially influenced by density of the gas and liquid
phases. If the phases are at rest or moving at very low velocity the gravity force dominates
and the lighter phase separates in the upper part of the downcomer. One aspect
is the time required to obtain a stable condition starting from well-mixed two-phase
distribution situations.
In a flowing system the flow regimes are dependent on void fraction and mass
fluxes of steam and water and dimensions of the downcomer flow path. The formation
of the mixture level is also dependent on the evaporation of water at the hot downcomer
walls, if the walls are still at higher temperatures compared with the water during
or after blowdown. If the flow is directed from the downcomer to the cold leg(s)
the flow conditions in the cold leg are affected (e.g., cold-leg break flow rate, pressure
decrease in the system, etc.).
The downcomer collapsed water level is the driving force for core reflood and
consequently core cooling conditions. The phase separation in the downcomer influences
the water inventory loss during blowdown via a cold-leg break due to its influence
on the pressure loss mainly in the broken loop and on the critical flow rate at
the break.

<!-- page 270 (PDF 26) -->
### 6.3.4 Stratified flow in horizontal pipes

At high velocities the flow of a two-phase mixture in a horizontal pipe can be fairly
homogeneous. As the velocity falls the gravitational forces tending to cause phase separation
across the direction of flow become more important compared with the inertial
forces. The ratio of these forces is expressed by the Froude number, a key number in
describing stratified flows. The occurrence of stratified flow has a significant effect on
a number of two-phase flow processes. Interfacial friction and the interfacial area for
HT are much reduced compared to other flow regimes, and in branching flows the
occurrence of stratified flow can significantly alter the flow quality within a branch.
Stratified flow conditions are a prerequisite for CCF in a horizontal pipe.
Adjacent flow regimes range from bubbly (at low gas flow velocity and low void
fraction) through plug flow and slug flow to wavy-annular flow (at high gas velocity
and high void fraction). The transition between stratified and nonstratified flow is
often not a sharp one. For instance the boundary between stratified and slug flow
can be difficult to define. When the slug frequency is low the flow retains many of
the characteristics of purely stratified flow.
The prediction of behavior within the stratified regime requires knowledge of
appropriate wall friction, interphase friction, and HT relationships. These are less difficult
to determine than for other more complex flow regimes, although these relationships
depend on whether the stratified surface is smooth or wavy. However,
inhomogeneous effects within the liquid phase, such as thermal stratification, are more
noticeable in this low flow regime. The extent to which inlet effects influence the flow
regime (when the flow is not fully developed) is still not fully understood.
It should be noted that stratified flow is not confined to horizontal pipes, but can
occur in quite steeply inclined pipes.
The main sites for stratified pipe flow are the hot legs, the cold legs, and the loop
seals of a PWR. Stratified flow can also occur in auxiliary piping such as feedwater
lines. The development of stratified conditions in the hot legs is closely bound up with
the transition from NC to refluxing, and the draining of the SG tubes in an LOCA. Its
occurrence in the cold legs affects the condensation rates of steam on the ECCS liquid
in SBLOCA. Where a break in the primary circuit occurs in a horizontal pipe, the
break flow is much more strongly dependent on the orientation of the break once
the flow in that pipe has become stratified, when the break flow quality becomes very
level dependent. Similar considerations apply to a stuck open PRZ valve during
LOCA. Flow stratification was found to occur in LOFT at reduced primary inventory
even while the primary pumps were still running.
Thermal stratification within the liquid phase is an important consideration in the
determination of thermal stresses associated with ECC injection.

### 6.3.5 Phase separation at branches

At low velocities, where the flow tends to stratify, phase separation at branches is
dominated by gravity effects. In this case the flow through the branch will be liquid
rich, if the branch is at the bottom of the pipe and, gas rich, if it is at the top. In general

<!-- page 271 (PDF 27) -->
the branch flow quality will be greatly dependent on the liquid level in the main pipe.
Liquid entrainment and vapor pull through, which are primarily inertial effects, both
exert a powerful influence on this relationship.
At high velocities the effect of inertial forces on branching flow becomes dominant
: the heavier phase (liquid) tends to flow in the straight direction, while the lighter
one (steam) is more easily diverted by the low pressure in the side junction of the
branch. This causes in most cases a larger void fraction in the side pipe with respect
to the value at the branch inlet. The mechanism is multidimensional and is significantly
affected by all the geometric peculiarities of the system.
The flow regime also plays an important role in this connection; as an example, in
bubbly or slug flow the steam phase can prefer to flow in the side branch as mentioned
above, but in annular flow, the liquid on the walls may be diverted more easily to the
side branch.
Branching situations can occur in LOCA scenarios at break locations. The prediction
of the phase separation at branches is important for evaluating the energy and
mass lost from the system. Vapor pull-through and liquid entrainment are examples
of phenomena expected.
Other typical branching configurations include the connections of the main piping
with the vessel and of the surge line with the hot leg in the PWR.

### 6.3.6 Entrainment/de-entrainment

Dropletentrainmentandde-entrainmentarealsoformsofphaseseparationandarerelated
to interface friction dependent on the flow regime. Water can, for example, be entrained
by sufficiently high steam velocities from the bottom of the reactor vessel and be carried
out of the vessel. This water can be lost from the liquid inventory in the pressure vessel.
Compared to phase separation in vertical flow with and without mixture level
(Section 6.3.3), entrainment and de-entrainment processes are more related to high
void fraction flows including void fraction discontinuities.
The main source of entrainment, in the case of core uncovery, is the core, where
steam is produced. Another place closely connected to the core is the UP where both
entrainment and de-entrainment can occur. These phenomena also take place in the
downcomer, mainly in the case of reverse steam flow for LBLOCAs. SG mixing
chambers, SG tubes, and the hot legs, in the case of ECCS injection, are also affected
by these phenomena.
For a given mass inventory, entrainment and de-entrainment influence the mass distribution
in the primary circuit and as a consequence the available mass inventory in the
core. So they have consequences on core cooling and are relevant for nuclear safety.
The important parameters related to entrainment and de-entrainment to be measured
are the droplet sizes and distribution, the interfacial area, the field of velocities.
Only limited global measurements are available based mainly on DP measurements.
Catch tanks are also used, and carryover tanks are available.
The present state of knowledge is limited to allow a detailed description of these
phenomena. Only global correlations are available. The geometry of internals and

<!-- page 272 (PDF 28) -->
geometric discontinuities also play an important role in relation to this PH. This limits
the degree of extrapolation of particular models.

#### 6.3.6.1 Entrainment/de-entrainment in the core

Droplet entrainment and de-entrainment are forms of phase separation. Water can, for
example, be entrained by sufficiently high steam velocities from the bottom of the
reactor vessel and be carried out of the vessel. Thus water can be lost from the liquid
inventory in the vessel. Droplets carried out of the reactor core by rising steam during
reflooding can be de-entrained by impinging on the various structures situated in the
UP and, consequently, may fall back into the core.
Entrainment of liquid droplets by the flow of steam has considerable influence on the
effectiveness of emergency core cooling. The importance of the entrainment has been
especially recognized associated with heat and mass transfer processes during LOCAs,
inparticular, duringtherecoveryphaseofthese accidents throughrefloodingofa core. In
thiscaseentrainmentimprovesHT,sincedropletsactasaheatsinkthroughdropletevaporation
.Thiswillleadtolowervaporsuperheatandimprovedcoolingoffuelrods.Indeed,
the hot portion of the fuel rods in the core is cooled by the mixture of steam and entrained
droplets. Liquid entrainment affects the liquid core inventory and is also important in the
determination of the CHF location. Another indirect effect of the entrainment is that the
vaporizationofthe droplets carried to SGs pressurizesthe UPand prevents thecorewater
level from rising (i.e., steam binding effect). Liquid de-entrainment occurs when water
entrainedinthesteamgeneratedinthecoreisremovedfromthesteamflowatotherplaces
inthecore,UP,orbeyond.De-entrainmentoccursfromgravitationalandinertialforces.It
is enhanced when flow slows down because of a flow area increase or when it changes
direction to pass around flow obstructions or structures or to turn out through a nozzle.
De-entrainment removes entrained
water from the
two-phase
flow mixture.
De-entrained water that accumulates in the core and UP provides a source of water for
core cooling supplementing the cooling by bottom reflood. This enhances core cooling
near fuel assembly grid spacers and is also important for the upper regions of the core.
Clearly, such entrainment and de-entrainment phenomena are controlled by interfacial
shear.Correctmodelingoftheinterfacialshearforceiscrucialfortheadequateprediction
of a number of phenomena and interfacial shear models also vary according to the flow
regimes.
The importance of the entrainment and de-entrainment in a core has been recognized
associated with heat and mass transfer processes during LOCAs, in particular,
during the recovery phase of these accidents through reflooding of a core and also
under boil-off situations. Since these phenomena will lead to improved cooling of
the fuel rods, the knowledge of the extent of entrainment and de-entrainment is necessary
to predict the hydrodynamic and thermal response in the core.

#### 6.3.6.2 Entrainment/de-entrainment in the UP

These phenomena are very much related to the entrainment and de-entrainment in the
core (Section 6.3.6.1). Some of the carryover out of the core will be captured in the
water pool, which may form on the upper core support plate, and by UP structures.

<!-- page 273 (PDF 29) -->
Pool formation refers to the collection of water in the UP during reflood. The source of
this water is entrained water carried up from the core which is then de-entrained in the
UP. The UP contains a great deal of internal structures that act as a steam separator to
de-entrain liquid in the two-phase flow. In addition, the drop in flow velocities from
the core to the UP allows gravitational separation of liquid from steam. The flow
behavior of a collected pool may be highly three-dimensional because of the tendency
of the water pool to collect in low flow areas and in regions near walls and structures.
UP pool formation is important to ECCS performance during an LOCA. The reasons
can be summarized as: the pool, particularly due to its multidimensional nature, provides
a source of additional cooling water for the core; de-entrainment and pool formation
reduce carryover to the SG; the pool can reduce the flooding rate by creating a
static head PD in the UP.
The extent of liquid carryover to the UP is expressed by the liquid carryover rate
fraction, that is, the ratio of total liquid mass flow rate out of the core to the liquid mass
entering the core. Liquid carryover reduces the rate of accumulation of water within
the core and provides a source of water for de-entrainment in the UP or beyond.
Carryover has a major effect, because the rate of advance of the quench front (QF)
is tied directly to the increase in core mass inventory, and is therefore highly relevant
to reactor safety.

#### 6.3.6.3 Entrainment/de-entrainment in the downcomer

In a large cold-leg break LOCA, the beginning of the “reflood” phase occurs when
the reactor vessel water level reaches the bottom of the core. This creates a seal
between the core and the downcomer, and further ECC water injection tends to fill
the downcomer to near the cold-leg elevation. The difference in water level between
the downcomer and the core provides the driving head for core flooding. This driving
head also creates a pressure difference from the top of the core to the top of the downcomer
which tends to cause core steam generation to flow out of the core and through
the loops to the downcomer. In combined injection PWRs, essentially all of the steam
flow is condensed by hot-leg and/or cold-leg ECC water and there is no steam flow
into the downcomer. In cold-leg injection or downcomer injection PWRs, steam
flows to the downcomer via intact loops or vent valves. Some of the steam is condensed
by ECC injected in the cold legs or in the downcomer. Any steam not condensed
, along with steam generated in the downcomer due to superheated walls,
flows circumferentially around the downcomer and out of the broken cold
leg, potentially entraining and carrying away a portion of the ECC water (Damerell
and Simons, 1993b). Some de-entrainment may occur due to higher inertia of the
water droplets compared with the steam phase where the flow changes its direction
from the downcomer to the broken leg.
The PH is mainly important if a large cold-leg break occurs and the ECC water is
injected only at the cold side of the reactor (into the cold legs or into the downcomer).
The circumferential flow of steam around the downcomer and the generation of steam
on superheated downcomer walls tend to entrain ECC in the downcomer region. The
interaction of steam flow, wall boiling, and ECC entrainment is important since it

<!-- page 274 (PDF 30) -->
affects the water level in the downcomer. Reduction of the downcomer liquid level
below the level (which is at the bottom of the cold-leg nozzles) reduces the available
driving head and tends to reduce the core flooding rate. This prolongs quench times
and potentially allows higher clad temperatures in the core.
The PH is not important if subcooled ECC water is injected at the hot side of the
reactor vessel and condenses a considerable steam flow from the core to the hot legs.
The PH is not important for intermediate and small breaks (rupture area less than 25%
of maximum pipe area connected with the pressure vessel) since the circumferential
steam flow in the downcomer is not high enough to cause a significant entrainment.

#### 6.3.6.4 Entrainment/de-entrainment in SG tubes

In the case of high steam flow rate droplets can be entrained into the SG tubes, from
the mixing chambers. In the case where the SG is a heat source (such as a large break
accident) the droplets may vaporize creating additional steam binding. This entrainment
process is strongly connected with the behavior of fluid in the mixing chambers.
This PH contributes to the so-called steam binding for LBLOCAs.
For a smaller break size, entrainment contributes to reducing the two-phase NC, to
producing reverse flow in some SG tubes and to reducing mass inventory in the core.

#### 6.3.6.5 Entrainment/de-entrainment in SG mixing chambers

Mixing chambers, by reducing the steam velocity, have a large impact on the phase
separation process and can reduce droplet entrainment in SG tubes. But when a mixture
level appears within a mixing chamber a sufficiently high steam flow can also
generate droplets with consequences for fluid behavior in the SG tubes (see
Section 6.3.6.4).
As in Section 6.3.6.4, this PH contributes to steam binding for large break and to
flow distribution in U-tubes (3-D effects) for smaller sizes of break and NC conditions.
It also influences the mass distribution in the primary circuit.

#### 6.3.6.6 Entrainment/de-entrainment in the hot leg with ECC injection (PWR)

A pressure difference exists from the UP to the downcomer through the loops, if a
large break occurs at the cold-leg side of one of the primary coolant loops, or if condensation
occurs in the SG primary side in a small-break scenario. The pressure difference
causes a steam flow from the UP to the SGs. ECC water injected into the hot
legs via a special nozzle (H€utze in KWU PWR) at the bottom of the hot legs, for
instance, may be entrained toward the SG by sufficiently high steam velocities.
The entrained water may reach the SG tubes where it may evaporate in the large break
case. The evaporated water is no longer available for core cooling. On the other hand,
the pressure in the SG primary side increases due to the evaporation, reducing the
steam velocity toward the SG, or even causing a steam flow from the SG to the
UP. Consequently, the total ECC water injected into the hot legs will be delivered into
the UP for a certain time span, causing an oscillatory flow in the hot legs.
