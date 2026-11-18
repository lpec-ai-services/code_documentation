# Concepts involved in two-phase flow developments
<!-- source PDF pages 2-15 -->

<!-- page 90 (PDF 2) -->
parameters needed for two-phase flow theory, especially void fraction and quality, are
introduced along with their relationship. Parameters involved in mass, energy, and
momentum balance equations for two-phase flows are also introduced. Phenomena
descriptions complete the notions needed for two-phase flow treatment (among them:
flow regimes, natural circulation, critical flow, blowdown, etc.). Also a brief explanation
on more simple approaches like homogeneous model, separate model, drift-flux
model, or lumped parameter is included in order to illustrate the complexity of the
involved physics. An outline of the so-called two-fluid model concludes the section.
In the second section, devoted to heat transfer, concepts and variables related to
conduction, convection, and radiation are introduced. Such introduction is centered
on characterization comments but it also includes the empirical and theoretical aspects
needed for understanding the expected developments.
The following two sections are devoted to additional concepts to analytical and
experimental thermal hydraulics. Parameters and concepts referred to system codes
and related subjects for the first and referred to test facilities and data management
for the second.
A block of three other sections can be found in the continuation: concepts
connected to design basis (DB), general safety concepts, and concepts related to
deterministic safety analysis (DSA).
The last block includes two sections: concepts related to actual accidents and a
miscellaneous section on concepts related to other uses thermal-hydraulic analysis.
Whenever it has been found interesting, the section includes also a kind of foreword
with the aim of clarifying its context.
3.2
Concepts involved in two-phase flow developments

## 3.2.1 Context

### 3.2.1.1 Importance of two-phase flow

The analysis of water reactors thermal hydraulics needs to consider two-phase flow
and related phenomena. Such phenomena that occur in normal operation in boiling
water reactor (BWR) and also in specific components of pressurized water reactor
(PWR) (mainly in steam generators, SGs) can also take place in accidental scenarios
of both PWR and BWR. Most of the safety scenarios involve depressurization; among
them loss of coolant accidents (LOCAs) and malfunction are related to pressure
control or pressure relief valves. Once a depressurization occurs in a PWR, system
saturation temperature could decrease and two-phase flow could appear. It also
appears in advanced phases of most scenarios in which, due to decay heat and to
the presence of water, vapor is produced in core and any mixture of water and vapor
could flow driven by a break, by an injection, or by natural circulation. The importance
of two-phase flow developments in the field of thermal hydraulics of nuclear
systems has stressed in conferences (OECD/NEA/CSNI, 1992) as well as in internationally
recognized textbooks (Tong, 1965; Wallis, 1969; Collier, 1975).

<!-- page 91 (PDF 3) -->
### 3.2.1.2 Multiscale and multiphysics

Thescientificcurrentapproachtodescribetheinvolvedscenariosincludesmultiscalecalculations
. Thermal-hydraulic analysis devoted to nuclear systems must cover the whole
rangeofmodelingscales.Bynow,itiswidelyacceptedthatsuchscalesarethefollowing:
system scale, subchannel scale, and CFD (computational fluid dynamics) scale.
The aim of the calculations at system scale is to predict the overall behavior of the
plant, including the reactor and other components such as primary circuit, SGs, and
pumps. System codes are the right tool to face the subject. Phenomena described at such
scale are usually called system effects. System codes usually solve the problem using a
1D formulation for most of the modeled system and 3D options for the most relevant
parts as the reactor vessel. System codes are widely used in thermal hydraulics of
nuclear systems (Freixa et al., 2015a,b; IAEA, 2014).
The subchannel scale is also firmly established. It deals with the modeling of the
reactor core or fuel bundles. To be stricter, at the definition level, this scale should
be called component scale, given that, besides the core, different components have more
detailed codes and models. Since the core is the component that more often is studied, it
seems correct to nominate the scale as subchannel scale. At such scale, 3D aspects are
taken into account and fuel bundles are modeled with enough detail in order to predict
local cladding temperatures or DNB expected values. In an analogous way, SG or other
heat exchanger tube bundles are modeled using specific codes at a similar level.
Thethirdgroupistheso-calledCFDscale.CFDproducessimulationsatanextremely
finer scale. The studies at such scale arebased on more advanced physical models, using
nodalizationsofahugenumberofnodesandapplyingmoreupdatednumericalmethods.
Accordingly, the computing power needed is also huge and problem definition is rather
complex (Smith et al., 2008). CFD codes are the tools and by now they are mainly used
to clarify the behavior of local areas or critical components in specific scenarios.
Many initiatives have been carried out devoted to coupling thermal-hydraulic
codes of different scale. In a similar way, there are also many initiatives connecting
thermal-hydraulic codes with codes describing other physical aspects of the simulated
scenario. Among them one can find either neutron physics, (Ivanov and Baratta, 1999;
D’Auria et al., 2004; Pericas et al., 2013, 2016; Pericas, 2015) mechanical or severe
accident codes (e.g., Pla, 2004; Espinosa-Paredes et al., 2012; IAEA, 2008b). Such
activities are by now encouraged by the fact that computers are becoming faster every
day. Multiscale and multiphysics platforms and projects are ongoing activities needed
to be taken into account.
Neither the scale nor the fact of being coupled with other physical formulation affects
the thermal-hydraulic concepts introduced below. Comments will be added if needed.

### 3.2.1.3 Turbulence and two-phase flow

The essential characteristic of turbulent flow is its apparently chaotic property
variation. In a turbulent flow pressure and velocity tend to change in space and time
rapidly due to unsteady vortices that appear on many scales and interact among them.
Reynolds number provides a first approach to limit the question: flows having a large

<!-- page 92 (PDF 4) -->
Reynolds number (more than 5000) are typically turbulent. This is only a first
approach and turbulence, despite the important analytical effort currently devoted
to it, can be considered an unresolved problem.
The analysis of turbulent two-phase flow has some added difficulty. The
above-mentioned chaotic property variations could change or even suppress any
two-phase flow regime. At this point, it seems that to get an accurate picture of
two-phase flow, turbulence has to be mastered previously.
Once again, experimentation is crucial to overcome the problem. Quite an important
amount of tests related to two-phase flow have been performed and the observation of
their results allows some confirmed outcome. Two-phase flow regimes have quite
steadypropertiesandtransitionsamongthemoccuratdefinitevaluesofkeyparameters.
All this has some uncertainty, but it opens a possibility of going ahead with two-phase
flow study. More detail on flow regimes and key parameters is given below.

### 3.2.1.4 Empirical database and instrumentation

An empirical database supports the use of equations, correlations, and codes. This is
an important point since the validation of theories and practices depends on the right
correspondence between what is defined and what is measured. The reliability of the
database is supported by its systematic documentation and by the qualification process
of facility instrumentation.
Ahugedatabasehasbeenproducedformanyyearsandisnowavailableforitsuseatthe
differentlevelwhere it is needed (Addabbo et al.,2002; Pla etal., 2015,2016b).It consists
inseparateeffectandintegralteststhatweredesignedtosupportthedevelopmentsdevoted
to predict the behavior of a reactor system in normal and abnormal or accident conditions.
Bynow,afterfollowinganinitiativeofCSNItheresultsofsuchexperimentsareorganized
in two different matrices (separate effect and integral tests) that establish their suitability
foreach phaseof the validationprocessof bestestimate (BE) thermal-hydraulic computer
codes (Aksan et al., 1987; OECD/NEA/CSNI, 1992, 1993, 1996).
Instruments devoted to produce the measurement of the relevant parameters are
needed for a complete qualification process devoted to certify its reliability. The
design of such instruments has to assure the right correspondence between the signal
produced and the physical parameter that the analyst is following. The complexity of
thermal-hydraulic processes is an additional difficulty related to instrumentation
design and setup. Another difficulty appears in the design and the qualification of
most instruments that are required to be suitable for measuring parameters over wide
ranges. For instance, the validity of thermocouples measuring temperatures in
accidental scenarios is rather complex to certify.

### 3.2.2 3.2.2.1 General aspects

The purpose of this section is to define the most relevant parameters that will be used
in subsequent chapters related to two-phase flow. Again some recognized textbooks
provide interesting details on such parameters and concepts, among them: El-Wakil

<!-- page 93 (PDF 5) -->
(1962), El-Wakil (1971a), El-Wakil (1971b), Tong and Weisman (1970), Fenech
(Ed.) (1981), and Todreas and Kazimi (1990). Parameters, usually known as water
properties, are only mentioned when the added comments are significant enough
for the specific development.
Two different comments are presented in this general section. They are related to
intensive and extensive properties and also to time and volume averaging
techniques.
By definition intensive properties are independent from the extent or the size of the
system while extensive ones are dependent. Temperature is a good example of intensive
property while mass and volume are examples of extensive properties.
Despite the extensive mass and volume, density and specific volume are intensive
and can be easily written down in a table. Water property tables are very useful and
most of the codes have their own versions of them.
Since thermal-hydraulic analysis deals with dynamic behavior of two-phase mixtures
, discretization of time and space is an important issue. To do so, control volumes
or space nodes on the one hand and time steps on the other hand are defined accordingly
. Such definitions may change depending on the problem, and are significant to
distinguish local from volume-average values and instantaneous from time-averaged
values.
Mass and energy conservation usually provide the criterion for averaging quantities
. Such criterion is applied in a slightly different way in case of intensive or extensive
properties. For extensive quantities like mass for example, the application is
straightforward. For intensive properties like liquid water temperature, things are
as follows: the volume-averaged temperature will be that of the liquid water at which
mass and energy of the node are conserved.
Such considerations are usually taken into account when designing measurement
techniques.
A similar rationale can be established in relation to instantaneous and
time-averaged values.

### 3.2.2.2 Void fraction/quality

In a first and most intuitive approach, the void fraction (α) of a two-phase mixture is
the volumetric fraction of a given control volume occupied by vapor.
Since different measurement techniques identify the cross section area (A) of a
given channel and also the areas occupied by the gas (Ag) and the liquid (Al), the void
fraction is written:
α =
Ag
Ag + Al
1□α =
Al
Ag + Al
Void fraction is equal to 1 when all volume is vapor and 0 when it is liquid.

<!-- page 94 (PDF 6) -->
Similarly, quality (x) of a two-phase mixture is the mass fraction of vapor in a given
control volume. If Wg is vapor mass flow and Wl is liquid mass flow then quality is
written:
x =
Wg
Wg + Wl
1□x =
Wl
Wg + Wl
Quality is equal to 1 when all volume is vapor and 0 when it is liquid.

### 3.2.2.3 Interfacial area/interfacial area concentration

Interfacial area, in a given control volume, is the area of contact between the two
phases, liquid and vapor. It is usually described by means of the parameter defined
as interfacial area concentration which is the area of contact between the two phases
per unit of volume (Bestion and Serre, 2013). Such parameter is strongly connected
with flow regimes that will be commented below. Characterizing such connection is
an ongoing research activity that has had interesting results by now.

### 3.2.2.4 Mass velocity

The total mass flow (W) per unit of cross flow area is the so-called mass velocity (G):
W = Wg + Wl
G = W
A
Mass velocity is especially interesting in subchannel analysis since it is directly correlated
with the remaining capability of extracting energy from a fuel bundle.

### 3.2.2.5 Equilibrium/subcooling/super-heating

As a general statement, two substances are in thermal equilibrium when there is no
energy transfer between them; this is when they are at the same temperature. At a
given pressure, there is a temperature, called saturation temperature, at which vapor
and liquid coexist without exchanging any energy. At saturation temperature, vapor
and liquid are in thermal equilibrium. It is useful, for further developments, to use
saturation temperature as a kind of reference.
Thus, liquid with a temperature (T) below saturation is called subcooled and
ΔTSUB=Tsat□T is called subcooling.
And similarly, vapor at a temperature (T) higher than saturation is called
super-heated and ΔTSAT=T□Tsat is called super-heating.

<!-- page 95 (PDF 7) -->
### 3.2.2.6 Hydraulic diameter/Reynolds and Froude numbers

Hydraulic diameter (Dh) is defined as:
Dh = 4A=p
where A is the cross-sectional area and p is the wetted perimeter of the cross section.
It helps handling flow in noncylindrical tubes and channels. Using it, one can
calculate different flow and heat transfer conditions in the same way as for a
cylindrical tube.
The most used dimensionless numbers in two-phase flow are Reynolds number
(Re) and Froude number (Fr).
Reynolds number (Re) is defined as:
Re = ρ· v·Dh=μ
It is the ratio between inertia forces and viscous forces. When viscous forces are dominant
Re has low values and flow becomes laminar, when inertia forces are dominant
Re has higher values and flow becomes turbulent.
Froude number (Fr) is defined as:
Fr = v=√g·L
ð
Þ
It is the ratio between inertia forces and gravity forces. Froude number is crucial when
determining the transition to stratified flows. When gravity forces are dominant flow
becomes stratified.

### 3.2.2.7 Pressure drop

The difference in pressure between two points of a fluid system is known as pressure
drop. Such difference can be due to static head, acceleration, friction, or local
resistance.
Static head is originated between two points having different heights. The acceleration
term, for a given fluid, is due to changes in cross area. Friction is caused
by forces exerted between channel walls and the fluid as a consequence of wall roughness
. Local resistance is due to changes in geometry like those produced by grids and
elbows.
The proper evaluation of pressure drop is crucial in thermal-hydraulic analysis
and becomes more complex when dealing with two-phase flow (Martinelli and
Nelson, 1948; Lockhart and Martinelli, 1949). The start-up of natural circulation
in any dynamic situation depends on the correct evaluation of pressure drops.
Also, in LOCA scenarios, the correct prediction of water mass distribution
depends on the knowledge of pressure drops in the involved system. Once mass
distribution is dynamically established versus time, core dry-out is also properly
predicted.

<!-- page 96 (PDF 8) -->
### 3.2.2.8 Involved in balance equations

Balance equations usually considered in two-phase flow developments are conservation
of mass, conservation of momentum, and conservation of energy.
Mass equation is usually postulated for a definite control volume. The most
relevant parameters and concepts involved are commented.
Each phase has its own volume and velocities and densities are usually considered
in their average value. If ug and ul are velocities of vapor and liquid phase, respectively
, and ρg and ρl are densities of vapor and liquid phase, respectively, then
Wg = Agρgug = Wα
Wl = Alρlul = W 1□α
ð
Þ
The equation of conservation of mass is usually solved for each phase considering the
existing mass of it in a given control volume and adding or subtracting any addition or
removal of mass at the boundaries of the volume.
Vapor generation (due to boiling) and liquid generation (by condensation) are also
terms of such balance. The accumulation of mass in a control volume equals the inlet/
outlet of mass across its boundaries and the mass generated in it. Indeed, boiling and
condensation correspond to this generation term, with the corresponding sign for
each phase.
The equation of conservation of momentum is usually formulated for each phase
considering the forces acting on it in a given control volume and equating it to the
change of momentum of the phase. Under these conditions, the most relevant parameters
and concepts involved are commented.
The forces exerted by each phase against frictional resistance of channel wall in
contact with it have the direction of the fluid and opposite sense.
The forces exerted by each phase against the other phase at the interfacial area have
the direction of the fluid and opposite sense. Its magnitude is proportional to the
relative velocity.
The forces due to static pressure against each phase could be calculated as P·Ag
for vapor and P·Al for liquid.
Since the weight of each phase is vertical, in a pipe having an angle θ with respect
to horizontal direction, the force due to weight (per unit of volume) is computed as ρg g
Ag sin θ for vapor and ρl g Al sin θ for liquid.
A complete momentum equation for two-phase flow should also include a virtual
mass term and the momentum production due to phase change.
Solving the resulting momentum equations has some additional complications
since frictional resistance is difficult to handle. Pressure drop at geometric discontinuities
is usually measured assuming that a fully developed flow is present and
becomes an important source of uncertainty.
The energy balance equation is usually established in a definite control volume.
The most relevant parameters and concepts involved are commented.
General parameters such as flow, velocity, or density are considered for each phase
in a similar way as in the previous equations. Other relevant specific parameters are

<!-- page 97 (PDF 9) -->
the change in enthalpy, the heat absorbed, and the work done. Variations in enthalpy
are not commented since it is a state variable.
The heat absorbed by each phase could be provided by the other phase or by
specific heat sources. Such source could be internal (chemical or nuclear reaction)
or external (hot or cold wall).
The term “work done” (positive or negative) is only relevant in components
producing or converting mechanical energy like turbines and compressors.

## 3.2.3 Phenomena

### 3.2.3.1 Flow-regime definition

Many experiments have been performed with heated and nonheated channels of
different sizes and inclinations (mainly horizontal and vertical). From the observation
of the results of such experiments important conclusions have been extracted.
This observation of results leads to the so-called flow-regime definition which is
crucial in thermal hydraulics of nuclear systems. The development is highly motivated
by the difficulties encountered in detailed calculations. As it has been said in a previous
section, full 3D calculations with advanced physical models and detailed geometries
are still difficult to carry out. Defining and improving the flow-regime definition
methods, using the existing tests database, bring the analyst to something feasible and
this is what induces the thermal-hydraulic community to follow this line. Some example
will help understand the situations that are already tested.
In nonheated channels having at their inlet a two-phase flow, boiling will not be
powered since no energy is added. Some energy exchange could take place depending
on the subcooling of liquid and the super-heating of vapor.
In heated channels having at their inlet a two-phase flow (see e.g., Lahey and
Moody, 1993) additional boiling could occur but this could be higher or lower
depending again on the subcooling of liquid and the super-heating of vapor.
In horizontal channels having at their inlet a two-phase flow, gravity could produce
phase separation depending on void fraction and velocity. Separated phases could easily
get a different velocity for each phase. Friction between phases could appear so that
they exchange momentum and alter again their relative velocities.
In vertical channels having at their inlet a two-phase flow, gravity could only
produce phase separation if velocity is low and boiling is considerable.
The results of experiments fulfill two different purposes: characterizing flow
regimes and establishing flow-regime maps.
A given group of experiments dealing with horizontal channels provides information
useful to characterize the following flow regimes listed at increasing void fraction
: bubbly, slug, annular mist, and dispersed (see Fig. 3.1). All these flow regimes
are considered for this group at high values of mass velocity avoiding horizontal stratification
in this first approach. Combinations of effects will come later along with
comments on other relevant parameters. Characterization produced by this first group
of tests is the following:
l
Bubbly flow (very low void fraction): liquid appears as a continuous phase and vapor is
formed by bubbles usually spherical and small.

<!-- page 98 (PDF 10) -->
l
Slug flow (low void fraction): vapor bubbles are neither spherical nor small. Their diameter
is close to that of the channel.
l
Annular-mist flow (medium void fraction): liquid appears as a thick film in the vicinity of the
wall and vapor is in the central part of the annulus.
l
Dispersed flow (high void fraction): vapor appears as a continuous phase and liquid is
formed by droplets or mist.
The considered group of experiments gives information helpful to derive the transitions
from one regime to the other. Void fraction is the most relevant parameter to
derive such transitions that are specific for horizontal channels. Despite being the most
significant parameter, it is not the only one. This means that Fig. 3.1 is just quite a
good approach that helps understand an approximate transition between different flow
patterns. It is quite a good approach since some system codes are using similar
flow-regime maps. Some authors suggest other more complex maps, and also research
devoted to smooth flow pattern transitions is still an open item.
Other specific aspects of horizontal channels appear at lower values of mass velocity
. The horizontally stratified flow occurs in situations where gravity becomes
significant compared with inertia force, and thus produces phase separation. Once
in a stratified pattern, if vapor velocity is increased, friction between phases will produce
a wavy flow. Such flow does not appear in Fig. 3.1 map, since it appears after
evaluating an additional parameter. Mass velocity and vapor-liquid relative velocity
are the parameters driving specific transitions between flow regimes in horizontal
channels.
Another group of experiments dealing with vertical channels provides the same
information for vertical channels (see Fig. 3.2). At sufficient mean velocity to avoid
vertical stratification and in pre-CHF (critical heat flux) situation, the basic flow
regimes are the same than in horizontal channels.
Combining effects for vertical channels are more complex except for vertically
stratified flow which is observed to appear for sufficiently low-mixture velocity.
Transitions, in this case, depend mainly on one parameter.
The other specific aspect is connected with heat transfer (see Section 3.3) and has to
do with a post-CHF situation. Since after CHF, an important amount of bubbles are
Fig. 3.1 Flow regimes in
horizontal control volumes.
Notes of lecture
“Thermal-hydraulic
Concepts” F. Reventos. UPC
Master of Nuclear
Engineering.

<!-- page 99 (PDF 11) -->
formed and coalesced in the vicinity of the wall, each pattern will move to a new flow
regime accordingly. Bubbly flow will move to inverted annular flow, slug flow to
inverted slug flow, and annular-mist flow to dispersed flow. Transitions, in this case,
depend not only on usual parameters like void fraction but also on the conditions of the
heat transfer mode established at the wall.
At this point an important consistency check can be performed. Let us remind that
ΔT is the difference between wall temperature and that of the bulk of the fluid. In the
next section, it will be shown that once steam bubbles coalesce in the vicinity of the
hot wall, heat transfer coefficient decreases and therefore ΔT increases. Inverted annular
flow appears to be a thick vapor film in the vicinity of the wall and liquid is in the
central part of the annulus, which is consistent with having a high ΔT and a rather low
void fraction.

### 3.2.3.2 Natural circulation

Any closed circuit heated at its lower part and cooled at its upper part could start natural
circulation. The driving force of such natural circulation is due to density difference
between its cold and hot legs. Depending on the magnitude of density difference
and the pressure drop along the circuit, equilibrium can be reached among involved
parameters: power generated, natural circulation mass flow, and power extraction at
the heat sink.
Such well-known phenomenon, which is widely used in heat transfer technology in
conventional heat exchangers and evaporators, appears in NPPs in two different fields.
The first one is related to some safety scenarios analyzed for current water reactors
(D’Auria et al., 1991; IAEA, 2005) and the second one is related to third and fourth generation
reactors (IAEA, 2009). The thermal-hydraulic analyst of nuclear plants needs to
be able to face both. In a nuclear system such as the primary loop of a PWR, the reactor is
supposed to act as thermal power generating device and SGs as heat sink.
Fig. 3.2 Flow regimes in vertical control volumes. Notes of lecture “Thermal-hydraulic
Concepts” F. Reventos. UPC Master of Nuclear Engineering.

<!-- page 100 (PDF 12) -->
### 3.2.3.3 Critical flow and choked flow

Increasing ΔP between upstream and downstream of a valve or junction results in the
increase in the mass flow. Once ΔP becomes higher, a limiting value is observed after
which mass flow rate does not increase anymore. Such value is called critical flow and
the phenomenon occurs when fluid velocity reaches sound’s speed. The phenomenon
is due to a physical reason since mechanical perturbations propagate at sound’s speed.
Theoretical and empirical approaches are available to overcome the difficulty that
appears when trying to solve momentum equation in such situation.
This phenomenon is extremely significant in nuclear safety since water reactors
operate at a quite high pressure and so any break could produce a very high ΔP
between the reactor coolant system (upstream of the break) and the reactor building
space (downstream of the break). The accurate evaluation of mass flow through the
break is crucial to match the right phenomenology of the scenario.
Mass flow rate when ΔP takes values within such critical interval is also called
choked flow (due to the fact that it is limited or choked) and special models are needed
in order to evaluate it (see Section 3.4.6).

### 3.2.3.4 Blowdown/reflood/rewet

Blowdown, reflood, and rewet are the three time phases expected to occur in a
large-break loss-of-coolant accident (LBLOCA) scenario (USNRC, 1987).
Blowdown is the first phase taking place just after the break. In this period a very
high ΔP occurs between the reactor coolant system and the containment. For this
entire time window, the break produces the driving force and an important amount
of coolant mass is lost through the break at a time when pressure and saturation temperature
rapidly decrease and vapor is formed. During the blowdown phase a quick
dry-out is produced and heat transfer decreases a lot. Energy stored in the fuel results
in a high peak of temperature.
Reflood is the second phase of an LOCA scenario. It starts when emergency core
coolant injection brings water to the core. In this period, coolant in the core is vertically
stratified, water level in reactor vessel increases progressively, and heat transfer
comes to a rather complex situation. On the one hand heat transfer phenomena that
appear are very different depending on their location, and on the other hand axial conduction
in fuel becomes rather important due to temperature gradient. Water level in
the core, in this situation is called quench front, increases at a rate that is a function of
injected mass flow. Under the quench front, coolant is dominantly liquid (low void
fraction) and bubbles are formed since cladding is still hot. In this situation flow
regime is probably bubbly and convection mode nucleate boiling either subcooled
or saturated. Above the quench front, coolant is dominantly vapor (high void fraction)
and droplets are dragged by vapor produced under the front. In that other situation
flow regime is probably dispersed or mist and convection mode is post-CHF.
Finally rewet is the last phase of an LOCA scenario. It starts when quench front
reaches the upper part of the core. In this period, coolant is dominantly in liquid phase
and heat transfer does not have any particular situation.

<!-- page 101 (PDF 13) -->
### 3.2.3.5 Reflux condenser mode

Reflux condenser mode is a cooling mechanism that could occur in a PWR usually in
defined phases of small-break LOCA (SBLOCA) (Pretel, 1997). At a reduced inventory
vapor is produced in the core and flows through the hot leg to SG U-tubes where it
can condense, fall back to the vessel, and help cool the core. The secondary side of the
SG has to be active (or at least full of water) to provide the condensing capability.
Also, during such cooling mode counter current flow occurs in hot leg since vapor
flows forward to the SG and liquid flows backward to the vessel.

### 3.2.3.6 Loop seal clearing

In the progression of an SBLOCA scenario, vapor is produced due to depressurization
and heat addition from core decay power (Pretel, 1997). Such vapor could fill the
upper parts of the primary side. More in detail, two different regions comprise such
upper parts: on the one hand upper plenum, hot legs, pressurizer, and SG U-tubes and,
on the other hand cold legs and downcomer upper ring. Liquid water is then cumulated
in the lower parts of primary system especially reactor vessel and intermediate leg or
loop seal. While vapor pressure in the upper head remains smaller than the compensating
water column, loop seal water blocks its path and avoids the merging of water
regions. During this interval, core uncover could occur. In the event of a pressure
increase (due to additional vaporization) loop seal water could be cleared or displaced
to cold leg and from there to the vessel. This phenomenon is known as “loop seal
clearing.”

### 3.2.3.7 Steam binding

In the progression of an LOCA scenario, secondary pressure could become higher than
primary pressure. This can happen after a loop seal clearing when vapor is the dominant
phase of the fluid that fills the upper part of the primary side including SG
U-tubes. In this situation such primary fluid could get heat from the secondary side
and also from hot passive heat structures. As a consequence void fraction and primary
pressure could increase and this could produce difficulties to the existing natural circulation
or to the core level recover. This phenomenon is known as “steam binding.”

### 3.2.3.8 Boron dilution accidents

Boric acid is used as a soluble neutron absorber in the primary coolant of pressurized
water reactors. In normal reactor operation the needed boron concentration is
maintained by the volume control system. The event in which boron concentration
in the core is accidentally reduced and produces the start of a reactivity excursion
is called boron dilution accident (Freixa, 2007; Freixa et al., 2007, 2009a).
The most usual classification of boron dilution transients considers:
l
External boron dilution. In such transients an injection of unborated water from outside the
primary cooling system occurs

<!-- page 102 (PDF 14) -->
l
Inherent boron dilution. In such transients a separation of primary coolant into highly borated
water and almost boron-free water occurs. This process takes place by evaporation and
condensation.
Thermal-hydraulic analysis is highly involved in boron dilution transients. Both the
build-up of a nonborated slug in the primary system and its transport to the core
are connected with thermal-hydraulic phenomena. When the level in the reactor pressure
vessel is low enough and core temperature is such that the coolant in that region
boils, reflux-condensation conditions are established. Under such conditions, the
steam produced condenses in SG tubes and almost boron free water is collected in
a region of the primary system (usually in the loop seal) forming a nonborated slug.
If a later natural circulation is established or a reactor coolant pump is restarted, the
slug can be transported to the core and produce a reactivity excursion.
Experiments related to boron dilution scenarios were carried out in the last decade
in the framework of two OECD projects, OCDE-SETH Project (2001–04) (OECD/
NEA/CSNI, 2004) and OCDE-PKL Project (2004–07) (e.g., Mull et al., 2007;
Umminger et al., 2012). Tests were performed at PKL facility and cover the most
relevant involved scenarios. Analytical activities were also included in the projects
(Freixa et al., 2009b; Revento´s et al., 2008b).

### 3.2.3.9 Boron dilution/deboration

Boron dilution is the process where a local decrease in boron concentration in primary
system occurs. Deboration is the process where a net loss of boron from primary
system occurs, which implies a decrease in average boron concentration. In the same
way, the following definitions are accepted as well: boration (the opposite of
deboration), boron concentration recovery (the opposite of boron dilution), deboration
rate (the rate of deboration), and dilution rate (the rate of boron dilution). These definitions
were proposed by D’Auria et al. (2005), and are nowadays accepted within the
international community.

## 3.2.4 Models and approximations

### 3.2.4.1 Homogeneous model

Solving two-phase flow equations is a complex task; different simplified approximations
are available by now; among them are the homogeneous model, the separated
flow model, and the drift-flux model.
The assumptions of the homogeneous model are the following:
l
Liquid and vapor have equal velocities
l
Liquid and vapor are in thermodynamic equilibrium
l
A single friction factor suitable for the mixture is used
The model could produce suitable results not only when the differences between the
properties of the liquid and vapor are not important (in the vicinity of the critical point)

<!-- page 103 (PDF 15) -->
but also when the mass velocity of the two-phase flow is very high and flow regime is
either bubbly or misty flow.

### 3.2.4.2 Separated flow model

The assumptions of the separated flow model are the following:
l
Liquid and vapor velocities are not necessarily equal
l
Liquid and vapor are in thermodynamic equilibrium
l
An empirically correlated friction factor multiplier is used
The separated flow model has been successfully used for calculating the pressure drop
in flow channels. As a general statement this model fits better at low mass velocity.

### 3.2.4.3 Drift-flux model

The drift-flux model is built on the concepts of drift velocity (which is the relative
velocity between phases) and drift flux (which is the volumetric rate at which
vapor passes forward or backward through the unit of area normal to the traveling
flow).
The drift-flux model is currently used in different codes in thermal hydraulics of
nuclear systems and other industries. It helps in analyzing systems behavior for quite
different transient conditions. Simplicity and robustness are its most significant
advantages.

### 3.2.4.4 Lumped parameter models

As a general statement lumped parameter models are built replacing in a more detailed
model the behavior of a specific parameter by a tested correlation or logic. Its use is
justified when the detailed code run is time consuming. The validity of the approach
relies on that of the correlation or logic involved.

### 3.2.4.5 Two-fluid model

The state-of-the-art knowledge on thermal-hydraulic two-phase flow predictions is
currently in between the approximations depicted above and the detailed simulations
produced by CFD codes.
On the one hand, basic models (like homogeneous, separated flow, drift-flux
model, or even some lumped parameter models) are good tools that help understand
phenomena and calculate some specific scenarios, but they do not bring enough detail
in many other situations. On the other hand, CFD studies, based on more advanced
physical models, nodalizations, and numerical methods, are appropriate for certain
aspects but they have two main drawbacks: a high computing effort is needed, and
their validation process for usual nuclear safety scenarios is still not fully completed.
Nowadays, the most commonly used option is the so-called two-fluid model, which
other authors may refer as the “flow pattern model” or even the UVUT model (where
U=unequal; V=velocity; U=unequal; T=temperature). This approach allows the
