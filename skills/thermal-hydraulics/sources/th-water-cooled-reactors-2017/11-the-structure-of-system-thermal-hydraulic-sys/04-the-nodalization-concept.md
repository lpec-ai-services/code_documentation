# The ``nodalization´´ concept
<!-- source PDF pages 11-20 -->

<!-- page 649 (PDF 11) -->
In addition to the basic 1-D pipe component, more simplified lumped parameter
models are used for tees, branches, and capacities which are needed to build complex
thermal-hydraulic networks. The code is based on a two-fluid six-equation model. In
the version CATHARE 2 V2.5 (Antoni et al., 2009), a validated 3-D pressure vessel
modeling is available. The code is able to model any kind of experimental facility or
PWR (Western type and WWER), and is usable for other reactors (fusion reactor,
RBMK reactors, BWRs, research reactors).

### 11.3.4.4 The ATHLET code

The thermal-hydraulic computer code ATHLET (Analysis of THermal hydraulics of
LEaks and Transients) is being developed by the Gesellschaft f€ur Anlagen- und
Reaktorsicherheit (GRS) for the safety analysis of LWRs (Teschendorff et al.,
1996). The code can model the whole spectrum of design basis and BDBAs (without
core degradation) like anticipated and abnormal plant transients and small to
large-break loss of coolant accidents (LBLOCAs) in PWRs and BWRs. For the fluid
dynamics the code user can choose between three options having different degrees of
sophistication:
l
The basic option is a five-equation drift flux model with separate balance equations for mass
and energy and one mixture momentum equation; mechanical nonequilibrium is calculated
by a full-range of drift flux correlations for horizontal and vertical flow conditions.
l
A two-fluid model with separate balance equations for mass, momentum, and energy with
corresponding algebraic source terms for the description of interfacial transport processes.
l
A four-equation homogeneous thermal nonequilibrium model including separate mass
balance equations and mixture equations for momentum and energy.
11.4
The “nodalization” concept
SYS-TH codes model the thermal-hydraulic physical system and other related
coupled systems. The thermal-hydraulic system can be either the cooling circuits
of a nuclear reactor, or the circuits of a test facility, to be simulated by solving systems
of equations. The thermal hydraulics of the cooling circuits is generally treated by a
generic method used for all components. However, some specific components having
a particular geometry require some specific thermal-hydraulic models. Thermal
hydraulics is also coupled to nonthermal-hydraulic systems which are also modeled
in SYS-TH codes.
Since the system of interest in nuclear thermalhydraulics, that is, the reactor, is
extremely complex by the geometry and by the very various physical processes, a simplified
model of the reactor is established in SYS-TH codes. The fluid domain is split
into a number of meshes or “control volumes” where balance equations derived from
first principles are written. This results in a discretized set of equations where physical
parameters such as pressures, temperatures, and velocities are calculated in a set of
nodes. Mathematically speaking, the simplification reduces the state space of the system
to a finite dimension, and the partial differential equations (PDEs) of the

<!-- page 650 (PDF 12) -->
continuous (infinite-dimensional) time and space model of the physical system into
ordinary differential equations (ODEs) with a finite number of parameters. This
process is often called the nodalization and includes many choices which have an
important influence on the quality of predictions:
l
Choice to model some component of the reactor fluid domain by either 0-D, 1-D, 2-D, or 3-D
models
l
Choice of the number and type of meshes (or control volumes) in each component
l
Choice to model heat transfers in solid structures by either 1-D, 2-D, or 3-D models and
choice of the size of meshes for heat conduction
l
Choice between several options for modeling pumps, turbines, valves, safety valves,
check valves, flow limiters, neutron kinetics (from point kinetics to coupling with 3-D
neutron
kinetics),
breaks,
and
ECCS
systems
(accumulators,
injection
systems
with pumps)
l
Modeling of some systems such as separators and dryers in BWRs and in SG of PWRs
l
Modeling of I&C with possible regulations
l
Choice of pressure loss coefficients in all component of the circuits
l
Choice to activate some CCFL option in some specific component of the circuit
l
Choice of heat losses modeling
l
Choice of a break flow model with possible multipliers
l
Modeling of HX and choice of mesh sizes for fluid and solid walls
l
Modeling of fuel either by a simple multilayer wall or by a more complex thermomechanical
model which can predict fuel deformation, creeping, clad rupture, clad oxidation, etc.
l
Use of additional transport equations for noncondensable gases such as nitrogen which may
be injected through accumulators, hydrogen which is produced by clad oxidation, air which
may enter the system through breaks or when the system is open to containment in cold
shutdown state
l
Use of additional transport equations for boron concentration
l
Use of additional transport equations for radioactive elements
l
The coupling to containment calculation
l
The coupling to possible passive systems
Such choices are necessary for building the input deck of a SYS-TH calculation. In
addition to the nodalization, information is necessary to define the process to obtain
an initial state—which is often a stationary and reference state—and the scenario of
the transient with all necessary BCs all along the transient (break opening, automatic
safety system actuations, operator actions, etc.). The time step management is also
part of an input deck and it is an important choice of the user which may affect the
calculation accuracy (see subsection on numerics).
The 0-D and 1-D versions of the two-fluid six-equation model are the basic models
in most SYS-TH codes.

## 11.4.1 The 1-D modules in system codes

It is clearly the basic module of system codes since it is able to model complex
two-phase flow in most components of the reactors including all pipes and also flow
in core assemblies. As soon as there is a privileged direction of the flow, a 1-D model
can describe the flow. There may be different closure laws depending on the duct

<!-- page 651 (PDF 13) -->
shape. For example the CATHARE code distinguishes the pipe (used for circulation
loop, surge line, SG tubes, any pipe connected to primary and secondary circuits), the
annuli (for modeling annular downcomer in pressure vessel and in SGs), and the rod
bundles and tube bundle (for core and riser of SGs). The 1-D system of equations is
described in Chapter 5. This module was able to catch most phenomena of interest in
many accidental transients of LWRs. However, a few limitations were encountered in
low velocity situations when natural circulation effects induce 3-D velocity field with
possible recirculation cells or when it is used in components which have a very complex
3-D geometry.

## 11.4.2 The Tee junctions

Many connections between two pipes exist in reactors and it required specific models
where specific momentum balance equations have to be written. Attention was paid to
phase separation phenomena when a side branch takes some fluid from a main pipe
(Fig. 11.2). Due to complex pressure field and different inertia of steam and water, the
quality of the side branch may be very different from the quality in the main pipe. Also
in the case of stratified flow in the main pipe, the branch may be below the free surface
or above and vapor pull-through below the level or water suction above the level have
to be taken into account.
Tee
Fig. 11.2 A modeled Tee junction with
illustration of the phase separation
phenomena.

<!-- page 652 (PDF 14) -->
## 11.4.3 0-D modules in system codes

OD modules exist in some system codes when some specific flow behavior cannot be
treated as a current mesh or control volume of the 1-D module. For example when
large capacities are connected to various pipes or ducts at various elevations and with
various orientations, the CATHARE code may use a two-node volume module. It is
assumed that velocities within the module are small compared to velocities at the junctions
so that gravity effects play a major role in the phase repartition and the pressure
field is assumed hydrostatic. The module may describe phase stratification by splitting
the total volume into two subvolumes separated by a free surface, with water and bubbles
below the free surface and steam with possible droplets above the free surface.
This explains that scalar quantities are calculated at two nodes. Similarly to the Tee,
such module may represent phase separation phenomena at the junctions (see
Fig. 11.3).
Thermal hydraulics of coolant fluid in reactor circuits may be influenced by a local
specific geometry, which requires some specific models. Some of them are classified
as special component models or special process models. Examples of special process
models are briefly described below.

## 11.4.4 Critical flow

Choked flow or critical flow conditions may occur in reactor transients either at a
break or in internal flow at flow restrictions or pumps. When sonic velocities are
reached at a section (often at the smallest flow cross-section area) the flow becomes
ai
gi
Fig. 11.3 Illustration of a
0-D two-node module for
representing large capacities
with phase stratification
(from the CATHARE code).

<!-- page 653 (PDF 15) -->
independent from downstream conditions. Predicting critical flow is then of prime
importance for all LOCA transients since the break flow rate controls the coolant mass
inventory, and consequently the core cooling capability. System codes developed
either 0-D or 1-D models for break flow or choked flow. They are presented in more
detail in Section 11.8.1.

## 11.4.5 Singular pressure losses

Complex geometries, such as bends, flow limiters, valves, sudden area change,
nozzles, perforated plates, spacer grids, and support plates, induce irreversible
pressure losses which are called “form losses” or “singular pressure losses.” System
codes do not predict these losses and the user has to enter loss coefficients in the
input deck.

## 11.4.6 Countercurrent flow limitation

The flooding limit and the CCFL play an important role in many accident sequences
since it may control the quantity of cooling water which is kept out of the core (UP, hot
leg (HL), SG tubes) and which is no more available for the core cooling. The basic
phenomenon is the limitation of a liquid downward flow rate by a given upward
gas flow rate. The CCFL is likely to occur in complex geometry such as upper core
tie plate, HL bend, inlet of SG header, inlet of SG tube, and a specific local modeling is
necessary in system codes to obtain reliable predictions. Flooding correlations are
established from experimental data and the parameters of these correlations are
entered in the code input deck.

## 11.4.7 Separators

Separators are used to separate steam and liquid water at core exit of BWRs or at the
top of PWR SGs. A two-phase mixture enters the separator barrel, passing through a
set of stationary swirl vanes. These vanes produce a high rotational velocity component
in the fluid flowing through the separator barrel. The resultant centrifugal force
separates the steam-water mixture into a water vortex on the inner wall of the separator
barrel and a steam vortex core. Because this process cannot be simulated by using the
1-D two-fluid model, special models are used for separators. The separator model
determines the void fraction in the (bottom) liquid fall back junction and the liquid
fraction in the (top) outlet junction. In general, two options might be available:
(i) a simple separator model in which a steam-water inflowing mixture is separated
by defining the quality of the outflow streams using empirical functions, and (ii) a
mechanistic separator model, which is intended to model the centrifugal separators
by solving phasic continuity equation, angular momentum equation, and axial
momentum equation with some simplifying assumptions.

<!-- page 654 (PDF 16) -->
## 11.4.8 Dryers

The steam dryer uses Chevron vanes to remove the moisture which is discharged from
the steam separators. The vanes provide a curved path which the liquid droplets must
follow if they are to flow through the dryer. The liquid droplets, flowing along the
curved path, hit the vanes due to their inertia and are deentrained. The resultant liquid
film flows down the vanes under the force of gravity and then back to the liquid pool
surrounding the separators. The dryer efficiency depends on the steam velocity and the
moisture content of the steam flow entering the dryer. Since this process cannot be
simulated by using a 1-D two-fluid model, special models which are either simple
or mechanistic are used for dryers.

## 11.4.9 Pumps

Pumps are generally modeled as a point (or 0-D) module. A pump is located in a node
or a mesh and it adds source and/or sink terms to the momentum and energy balance
equations. The angular momentum equation is added and controls the rotation speed
of the pump. The hydraulic torque is generally modeled through user defined characteristic
functions of fluid velocities and rotation speed. The hydraulic torque is a sink
term for the angular momentum equation and is multiplied by the rotation speed in a
source term for the fluid energy equations. The pump head is also modeled through
user defined characteristic functions of fluid velocities and rotation speed. The pump
head appears as source terms in the fluid momentum equations. The head and torque
characteristic functions have to be known in the four quadrants.
Usually pump vendors give only single-phase characteristic functions in the first
quadrant. It may be necessary to do experimental tests to get the pump characteristic
functions in the other quadrants. Moreover two-phase characteristic functions have
also to be given as user defined functions since pump performance (head and torque)
are degraded in two-phase flow conditions. Usually two-phase characteristic functions
are also function of inlet void fraction.

## 11.4.10 Turbines

Turbines, like the pumps (see above), are generally modeled as a point (or 0-D) module
. Turbine also adds source and/or sink terms to the momentum and energy balance
equations. The sink and source terms are also modeled as user defined functions.

## 11.4.11 ECC injections

ECC injection is often simply modeled as a source term (of mass, momentum, and
energy) in a node or mesh. A very simple model may be used when the flow rate
is a function of the pressure at injection location. The ECC injection (special) model
takes care of the mixing, including interfacial transfer, between different fluids in the
delivery line and in the primary system (typically).

<!-- page 655 (PDF 17) -->
## 11.4.12 Accumulators

Accumulators may be modeled either using standard modules (0-D, 1-D, valve, Tee,
walls) of the codes or by a specific accumulator model. The specific module must
predict:
l
Accumulator pressure as function of remaining mass and of heat released from accumulator
walls (from isentropic depressurization for rapid discharge to quasi-isothermal for slow
discharge).
l
Flow rate delivered to the circuit as function of valve opening, accumulator pressure,
primary circuit pressure, pressure losses, etc.
l
Mass momentum and energy source terms in both phases in the injection mesh.
If some specific options are actuated, the accumulator specific module should also
predict the amount of dissolved nitrogen in liquid water and the source term of nitrogen
in gas mixture in the case of transport of noncondensable gas.

## 11.4.13 Valves, safety valves, control valves, check valves, and flow limiters

Many valves, safety valves, control valves, and check valves exist in a reactor. They
may be “internal” to the modeled circuit or “external” when they connect the modeled
circuit with the external space (e.g., containment or pressure suppression pool). They
are characterized by functions giving either the pressure loss as a function of flow rate
and the degree of opening, or flow rate as function of upstream pressure and temperature
for choked flow conditions. Most of the time, only single-phase valve characteristics
are known. The valve model also must predict the behavior in abnormal
two-phase conditions.

## 11.4.14 Breaks

The break may occur anywhere in a pressurized system and may put in communication
a high pressure (typically high temperature) environment with a low pressure
(typically ambient temperature and pressure) environment. Conditions for the
occurrence of “critical flow” (i.e., TPCF) develop at the break. Although a number
of breaks and break configurations are excluded for technological reasons (e.g.,
catastrophic vessel break, application of the leak before break concept in selected
piping), a wide variety of break configurations may appear. This reflects in a wide
variety of break shapes that cannot be controlled by thermal-hydraulic parameters
and, at the same time, affects the prediction of relevant thermal-hydraulic quantities
like critical flow rates. Furthermore, the capabilities to predict TPCF are not
necessarily embedded into the balance equations (with the noticeable exception of
the CATHARE code, where a specific experimental database was created and
used) even due to the specific ranges of validity of relevant equations: for example
, friction pressure drop at very high fluid speed, or vaporization rate when steep
pressure gradient occur along the flow direction and as a function of time. Owing

<!-- page 656 (PDF 18) -->
to this, special critical flow models are needed and are provided by code developers
as well as by several researchers in the open literature.

## 11.4.15 Spray cooling

The spray of subcooled liquid into a steam environment constitutes an efficient way to
cool a space region of the NPP. Spray cooling is adopted in nominal operating conditions
(e.g., cooling of the vapor region of the pressurizer in PWR in order to control
the pressure) or in accident conditions (e.g., cooling of the upper core region of BWR
to facilitate the liquid entering into the upper part of the core following the occurrence
of accidents). Thermodynamic nonequilibrium phenomena occurring in direct contact
condensation conditions are involved that are not within the domain of validity of closure
equations. Furthermore, the phenomenon is controlled by aspects like the droplet
size, the droplet speed distribution, and the formation of droplets clouds and the interaction
of droplets with solid walls. Those aspects are not part of the balance equations;
rather they are dependent upon the design and the operation of the spray nozzles.
Owing to this, special models are needed and are provided by code developers.
One of the first RELAP5 nodalization schemes for LBLOCA test of LOFT facility
is shown in Fig. 11.4. In the early times of system codes, the CPU cost was an issue and
code users had to minimize the cost by reducing the number of control volumes. Here
an SG tube was represented with only 4 upward meshes and 4 downward meshes, a HL
by only 5 meshes and the core by only 13 meshes.
Fig. 11.4 RELAP5 nodalization scheme for large-break LOCA test at LOFT facility.

<!-- page 657 (PDF 19) -->
Fig. 11.5 illustrates a more recent nodalization of a PWR with CATHARE. One can
identify a few 1-D “pipe” modules for modeling HLs, intermediate legs (ILs), cold
legs (CLs), SG tubes in the broken loop (on the left) and on the intact loops (on
the right), the surge line, the steam lines, a break pipe, and the core bypass. One
can also identify a 1-D “annulus” module for the downcomer, a 1-D “rod bundle”
module for the core, and a few 0-D components for the pressurizer, the UH, the
UP, the LP, the top of the downcomer, the steam domes of SGs, the steam header collecting
steam lines. Tee junctions are used for connecting the surge line to a HL, the
break pipe to a CL, the steam line to a safety valve. Pumps are present in each loop.
BCs are here required for the break, the exit of steam header, the inlet of SG valve.
Source submodules are used for modeling SG feedwater and SIs. An accumulator submodule
is also represented. HX are used in SGs. This is a rather simple nodalization of
a reactor.
Fig. 11.6 shows a nodalization of a PWR pressure vessel using a 3-D module. One
can see a cylindrical system of coordinates with from bottom to top, 4 levels in the LP,
about 40 levels in the core, 4 levels in the UP, and 2 levels in the UH. In the radial
direction, there is a radial mesh in the downcomer, a radial mesh for the core baffle,
and three radial meshes within the core. This nodalization is rather coarse and the continuous
progress of computer power will allow in near future mesh refinements as
illustrated in Fig. 11.7. The core nodalization might include one vertical row of
meshes for each fuel assembly in a Cartesian frame of reference, and various subcomponents
might use either cylindrical or elliptical frames of reference depending on the
local geometry. The nodalization on the right-hand side of Fig. 11.6 uses Cartesian and
cylindrical meshes. This requires nonconformed junctions between subcomponents.
One may also imagine local mesh refinements in one or a few fuel assemblies which
BREAK1
Tee
Volume
Pipe
Pipe rodbundle
Pipe annular
BC
Source
Accumulator
Heat exchanger
Pump
PIPBRK
VOLDOWN
UPPLEN
UPHEAD
DOWNCO
BYPASS
LWPLEN
MIDCORE
ACC1
SSS1
SFEEDSGI
STMDOMI
PIPTEI
VALVEI
EXCHI
DOWNCOMI
STMGENI
EXTHEAD
STMHEAD
TEVALVEI
STMGENB
PRESSU
SURGEL
TEBREAK
TEPRESSU
o
Fig. 11.5 Illustration of a PWR nodalization for SBLOCA simulation by the CATHARE code.

<!-- page 658 (PDF 20) -->
Fig. 11.6 Illustration of the nodalization of a PWR pressure vessel using a 3-D module. Left: a
very coarse nodalization. Right: a finer nodalization particularly in the core.
Fig. 11.7 Illustration of advanced pressure vessel modeling for system codes.
