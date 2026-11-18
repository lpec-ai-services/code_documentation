# Chapter foreword — Characterization of thermal-hydraulic phenomena for set — Basic phenomena
<!-- source PDF pages 14-20 -->

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
