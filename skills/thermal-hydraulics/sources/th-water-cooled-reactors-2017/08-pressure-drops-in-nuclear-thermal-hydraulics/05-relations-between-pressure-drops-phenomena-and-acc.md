# Relations between pressure drops, phenomena, and accident scenarios — Additional relations between pressure drops and phenomena
<!-- source PDF pages 23-37 -->

<!-- page 515 (PDF 23) -->
values for linear heat flux and consequently for core power. What stated above applies
to the nominal operating conditions for the core of water cooled reactors. Cooling
enhancement is also expected in transient conditions: this is the motivation for keeping
this section in a heading section dealing with LB-LOCA.
Pressure drops across spacer grids and CHF enhancement by spacer grids constitute
the topic of many investigations; recent papers by Batta and Class (2016) (related to
spacer grids in metal cooled reactors), Schikorr et al. (2010), Agbodemegbe et al.
(2015), Ikeda (2014), and Jayanti and Reddy (2013) (the last three papers focus on
CHF) are included in the list of references for this chapter and can be considered
by the reader for further details.
All the concerned investigations (with the noticeable exception among the papers
listed above of the work by Schikorr et al., 2010, where the Rehme correlation is at
the center of attention) focus on CFD modeling and applications. Therefore (obvious)
conclusion here is that CFD is the proper technological area within nuclear
thermal-hydraulics for pressure drops and CHF in spacer grids (see, e.g.,
Chapter 12 of the book).

## 8.4.2 Additional relations between pressure drops and phenomena

### 8.4.2.1 Pressure drops and flooding at CCFL location

Counter-current flow (CCF) with upward oriented steam flow and gravity-driven
water down flow in vertical flow sections are expected to occur in many accident
sequences. CCF may also appear in inclined or even horizontal flow sections if there
is a connection with inclined or vertical sections experiencing CCF. At high steam
Increased steam flow through
remaining loop
Refill of single loop seal
(UP
break)
Increased SI flow
RCL full
SG
Status with loops partly cleared
(3 of 4 loops shown)
Cold side SI flow
ACC
RPV
Steam, overheat
Steam, saturation
Coolant, saturation
Coolant, subcooled
PRZ
PRZ riser section
Increased Δp
RPV fill level
RPV downcomer
Higher Δp between upper
plenum and break
Δp
Lower swell level in RPV
riser section
Loop seal
fill level
Fig. 8.8 PKL III increase in Δp across loop due to LS refilling.

<!-- page 516 (PDF 24) -->
flow rates or steam velocities the water flow in the opposite direction may be impeded
or even terminated/diverted in the same direction as the steam flow (cocurrent flow)
due to momentum exchange between the phases. This phenomenon, called CCFL,
may lead to accumulation of water, i.e., flooding or water hold-up at the CCFL location
. CCFL can be considered as one of the key thermal-hydraulic phenomena in reactor
safety analyses because it can prevent or at least deteriorate the backflow of water
to the reactor core. The occurrence of CCFL is generally connected with an increase in
pressure drop at the CCFL location. It therefore does not only lead to a displacement of
water from the core to the CCFL location but it may also cause a certain suppression of
the core level.
CCFL is likely to occur in complex geometries characterized by flow restrictions,
bends or significant reductions of flow areas, such as upper core tie plate, hot Leg
bend, inlet of SG header, or inlet of SG tubes. Additional possible CCFL positions
are the RPV DC, the pressurizer (PRZ) surge line, and the ascending part of the cross
over leg. Specific local modeling is necessary in system codes to obtain reliable
predictions. Flooding correlations are established from experimental data and the
parameters of these correlations are part of the code input deck.
Extensive experimental investigations in SET and integral test facility (ITF) have
been performed during the last decades to address the CCFL issue and to provide an
experimental database for the development and validation of the corresponding
models. Comprehensive experiments in full scale PWR geometry on CCFL in the
hot legs during reflux condenser mode in small break LOCA (SB-LOCA) conditions
have been performed in UPTF. Additional investigations in UPTF addressed CCFL at
the upper core tie plate and in the RPV DC during LB-LOCA. The UPTF test results
and the comparison with results from smaller test facilities clearly demonstrated the
dependency of CCFL occurrence on the geometrical dimensions and the importance
of scaling for the investigated cases. Pronounced heterogeneous 3D flow distributions
with water downflow (breakthrough) and steam upflow paths have been observed and,
for example, nonuniform distribution of vertical differential pressure across the tie
plate has been detected (Mayinger et al., 1993).
CCFL in the SG U-tubes have been mainly addressed by systematic investigations in
integral test facilities (e.g., LSTF, BETHSY, and PKL). As mostly PWR-prototypical
SG tubing with original dimensions of the individual U-tubes is used in the test facilities,
the experimental results are largely representative of the PWR.
CCFL under reflux condenser conditions has been extensively investigated for
instance in the PKL III test facility. Within parametric studies, the influences of
the specific SG load (heat to be removed by the SG) and the primary pressure on
the occurrence of CCFL and on the amount of water accumulated in the U-tubes
due to CCFL was systematically analyzed under quasisteady state and transient conditions
(secondary side cool down). As an example Fig. 8.9 shows typical results from
an experiment on CCFL under reflux condenser conditions performed with a stepwise
increase of the SG load from 4% to 20% of the nominal SG power at a constant primary
pressure of 40 bar (realized by controlling the secondary side pressure). The
measured Δp, between the in- or outlet chamber and the outlet chamber and the
top of the U-tubes for three tubes with different heights as well as the measured

<!-- page 517 (PDF 25) -->
Δp between the SG inlet and outlet chamber are shown in Fig. 8.9. In the PKL test
facility 3 out of 30 U-tubes are equipped with Δp measurements on the inlet and outlet
sides of each of the four SGs.
The test started in “pure” reflux condenser condition, i.e., the mixture level in the
RPV was between the core exit and the lower edge of the RCL and there was no water
accumulation, neither in the hot legs nor in the SG inlet chamber or in the U-tubes.
Under these conditions, the measured Δp on the inlet side (CCF) and outlet side (concurrent
flow) is close to zero. The onset of CCFL in the U-tubes is clearly indicated by
a significant increase in Δp on the SG inlet side and by an increase in Δp between the
SG inlet and outlet chamber at a SG load of 6%. It has to be mentioned that in the SG
inlet chamber liquid hold-up occurred at the same power level, however shortly after
the occurrence of liquid hold up in the U-tubes. Consequently liquid hold up in the
U-tubes was the result of CCFL and not simply a continuous rise of the steam/water
mixture level from the inlet chamber into the U-tubes.
SG in/out
15,000
20,000
25,000
30,000
Time (s)
Outlet side
Intlet side
Inlet side
Inlet side
Outlet side
Outlet side
Tube 1
Tube 19
Tube 29
Tube 29
Tube 19
Tube 1
dp dp
dp
dp
dp
Outlet
CCFL in SG-U-tubes of a PWR
Inlet
dp dp
SG load (%)
0.2
0.4
–0.2
–0.2
0.2
–0.2
0.2
0.4
0.6
0.8
0.4
0.6
0.8
0.2
0.4
Pressure difference (bar)
Pressure difference (bar)
Pressure difference (bar)
Pressure difference (bar)
Fig. 8.9 PKL III—CCFL in SG U-tubes during reflux condenser mode of operation.

<!-- page 518 (PDF 26) -->
Fig. 8.9 also reveals a rather heterogeneous flow behavior among the individual
U-tubes. While the longer tubes experience water hold up, condensate is carried over
to the outlet side in the short U-tube creating a pressure drop (due to high steam/water
velocities) from the top of the U-tubes to the SG outlet chamber (cocurrent water/
steam flow) indicated by the negative value for the pressure difference in the outlet
side of the short tube. Obviously, the steam is not condensed completely in the shorter
tubes, and the remaining steam flows via the SG outlet chamber into the outlet sides of
other tubes experiencing CCFL in their inlet sides. As a result, CCFL may also occur
in the outlet sides of longer tubes if this steam flow rate is large enough. The entire
pressure drops on the inlet side (carry-over of condensate) and the outlet side
(cocurrent flow of steam and condensate) corresponds to the differences in pressure
drops between the inlet and outlet side of the longer tubes which are mainly caused by
the hydrostatic head of the accumulated water, whereas friction pressure drop, local
pressure drop, and possible dynamic effects are also included in the measured Δp.

### 8.4.2.2 Pressure drop and TPCF

When a fluid passes from a high pressure region with a given thermal-hydraulic state
(pressure, temperature, void) via a restriction (e.g., pipe, orifice, valve) to a lower
pressure environment, the mass flow is determined by the pressure difference between
the two regions as far as a certain limit for the pressure difference is not exceeded.
Under these conditions a pressure reduction in the downstream region results in an
increase in mass flow. However, if this pressure falls below a certain value (i.e.,
Δp exceeds a certain value), no further increase in mass flow takes place (Fig. 8.10).
The resulting flow (called critical or chocked flow) is then independent of the conditions
in the downstream region and is for a given geometrical configuration, only a
result of the conditions (e.g., pressure, temperature, void, quality, flow region) in front
of the restriction. Fig. 8.11 shows schematically the pressure profile along the flow
Pressure in the exit cross section p2
Mass flux m
m < mcrit
•
•
•
m = mcrit
mcrit
Critical flow
Subcritical flow
p2
=
□
□
•
•
•
Fig. 8.10 Relation between
mass flow and pressure in
the exit cross section.

<!-- page 519 (PDF 27) -->
path from the inlet to the outlet of a flow duct (restriction). The pressure reduction with
increasing gradient is connected to an acceleration of the two-phase mixture. The reason
for critical flow is the strong expansion of the gaseous phase and can be explained
on the basis of energy conservation (transposition from potential to kinetic energy).
For subcritical flow the pressure in or just upstream of the exit cross section corresponds
to the pressure in the downstream region p2. In case of critical flow a pressure
jump is observed in the exit cross section. The minimum achievable pressure p1 is
called critical pressure pc and cannot be decreased further even if the pressure p2 is
reduced.
As outlined in Chapter 6, the knowledge on the two-phase mass flow under critical
flow conditions is a very important issue in reactor safety analysis concerning a broad
range of accident/events and relevant for different components/structures in reactor
systems, such as:
l
Loss of inventory through breaks/leaks ranging from small cracks to DEGBs,
l
Restrictions inside a system (e.g., surgeline or locked RCP after DEGB),
l
Critical flow though valves, e.g., during
–
Cycling of safety and relief valves to control primary and secondary side pressures, e.g.,
in SBO, LOFW, ATWS, and SB-LOCA transients.
–
Depressurization of primary and/or secondary side by fully opening of corresponding
valves (as AM measures).
Numerous models for critical two-phase flow have been developed for use in
thermal-hydraulic system codes. The detailed description of these models which are
differing among others by their complexity or by the level of assumed disequilibrium
(thermal and mechanical) can be found in the open literature and is not subject to this
x0
x1
x2
p1
p2
p1
p2
p0
x
Fig. 8.11 Pressure along the
flow path as function of the exit
pressure.

<!-- page 520 (PDF 28) -->
chapter. Such critical flow models have been assessed against an extensive set of data
from critical flow experiments mainly conducted in SET. A number of studies based on
existing experimental results have been performed in recent years (e.g., Sokolowski and
Koslowski, 2012; Bartosiewicz et al., 2011), to validate the models in the currently used
codes, to investigate the range of applicability of the individual models and to identify
options for further improvements in the calculation of the critical flow. It is clear that
none of the existing models can cover the entire parameter range expected to occur
under accident situations with respect to the geometrical configuration and with respect
to the thermal-hydraulic conditions in front of the critical flow area.
A large number of SET on critical flow, the first ones already performed in the
seventies of the last century,are known fromthe literature. The OECD/NEA has selected
different experiments as reference tests for critical flow during LOCA transients (see
Chapter 6 of the book). One of the most prominent test campaign often used as source
of experimental data for validation of two-phase critical flow (TPCF) models was
performedwithinaninternationalprojectintheSwedishMarvikenPowerStationfacility
under almost real plant conditions (Ericson and Hall, 1978) in the years 1978–1979.
Typical results of another experimental campaign on two-phase critical BD from a
pressure vessel following a pipe break, performed at the University of Pisa, are shown
in Fig. 8.12. The illustrated curves represent the time trends of the pressures measured
in the pressure vessel and in the exit pipe at two different positions. A method for analyzing
the most important phenomena in the BD transient was applied by D’Auria and
Vigni (1983) to these experimental signals to obtain values for flow rate as well as
spatial and temporal trends of quality and velocity in the exit pipe.
With the spatial profiles of the pressures (input) Fig. 8.13 shows the calculated
velocity and quality profiles along the exit pipe at a certain point in time (t=6 s).
The pressure decrease in the pipe causes, in this case, evaporation of water entering
p0
p1
p2
(Mpa)
p0
p1
p2
t (s)
Fig. 8.12 Pressure evolution at different locations.

<!-- page 521 (PDF 29) -->
the nozzle and then a continuous increase in velocity. In the applied theoretical
method, axially symmetric flow under thermodynamic and mechanic equilibrium
conditions was assumed. The pressure drop due to local discontinuity and wall friction
was considered by corresponding input data (pressure loss coefficient at pipe inlet,
distributed friction factor between pipe wall and fluid and two-phase flow multiplier).
In general, most of the calculation methods for critical mass flow assume in a first
approximation isentropic changes of the conditions from the inlet to the exit of the
flow duct. Under these conditions (typical for ideal nozzle) the pressure drop along
the flow duct only consists of acceleration effects (wall friction is neglected).
Depending on the geometry and the operating conditions, the friction pressure drop
may not be neglected. In constant cross section pipes with chocking occurring at
the pipe exit, the critical flow may be significantly influenced by the entrance losses
and the wall friction in the pipes. The length of the pipe or the L/D ratio is one decisive
factor to quantify the impact of friction pressure drop on the critical flow rate.
In case of narrow wall penetrating cracks in pressurized components, the hydraulic
resistance in the flow path is very important for the determination of the leakage rate.
As an example, Fig. 8.14 shows the pressure distribution through a crack, calculated
with a finite volume program on the basis of geometrical characteristics of the leakage
path (Keim et al., 1999).
The analysis of leak flow rates of through-wall cracks is also relevant in connection
with the qualification of leakage detection and surveillance systems used in NPP and
with respect to break preclusion concepts including leak-before-break.

### 8.4.2.3 The LSC

Depending on the break size and the availability of the emergency core cooling system
a loss of coolant with small or intermediate break may lead to significant reduction in
primary system inventory with interruption of NC and under certain boundary
500 z(mm)
10p/p0
[(p0)t= 6s= 5.7 MPa]
[(x0)t= 6s= 0.0309]
[(h0)t= 6s= 1251 kJ/kg]
x/x0
100w /  2 h0
√
Fig. 8.13 Pressure, quality, and velocity versus distance from the nozzle inlet.

<!-- page 522 (PDF 30) -->
conditions even to core uncovery and cladding temperature increase. The occurrence,
extent, and termination of core uncovery is closely linked with the occurrence of LSC.
In contrast to LB-LOCA where the LSs are completely emptied already during the BD
phase, they remain initially at least partly filled with water in SB-LOCA or intermediate
break LOCA (IB-LOCA) transients.
In case of cold leg break the core level depends on the pressure drop of the steam
flowing from the core to the break. As long as the LSs are filled with water the flow
path via the SG and the cross over legs are blocked and the only available flow paths to
the break are via the upper head—DC bypass (and via the nozzle bypass) leading to a
relative high pressure difference between the UP and the cold leg (break location).
In case of SB-LOCA a certain part of the decay power is transferred to the secondary
side under so called reflux condenser conditions so that the primary pressure is
mainly determined by the secondary pressure. In case of IB-LOCA the primary pressure
typically drops below the secondary pressure due to the larger break size and
there is no heat transfer from the primary to the secondary side for the major part
of the transient. Continues loss of inventory (assuming no or small ECC injection rates
compared to the break flow rate) results in a continuous level reduction in the core.
In parallel a continuous displacement of water in the loops seals from the SG outlet
side to the upward part, i.e., toward the break in the cold leg, occurs. Assuming that the
pressure drop from the core outlet via the SG to the SG outlet is small, the pressure
difference between both sides of the LSs and between core and DC are similar so that
the level reduction on the SG side of the LS proceeds synchronously with the level in
the UP/core region (manometer balance). As soon as the water level in the downward
7E+06
6E+06
5E+06
4E+06
3E+06
p in Pa
2E+06
1E+06
0.005
Static pressure
Total pressure
Δp entrance
Δp outlet
Δp turn
x in m
Δp roughness incl. tums
Fig. 8.14 Pressure within the crack.

<!-- page 523 (PDF 31) -->
vertical part of the LS reaches the upper edge of the horizontal section, steam can flow
through the corresponding loop to the break and can also push the water in the upward
vertical part off the LS toward the cold leg. An additional steam flow path from the
core to the break is generated in this way. This effect is called “LS clearing.”
As a consequence, the differential pressure between the UP and the DC decreases
and the core and DC water levels equalize. A potentially preceding core uncover may
be terminated in this way. This effect can be supported by additional displacement of
water from the LSs to the DC and to the core. The described phenomena could also be
observed in a PKL test simulating a SB-LOCA transient as shown in Fig. 8.15. Core
uncover occurred before LSC (situation 2). Due to the relative high pressure difference
between the UP and the upper DC the core level was “suppressed.” With
LSC and subsequent pressure equalization between UP and DC, water from the
DC and the LS was displaced into the core and the core cooling was reestablished.
Differential pressure (bar)
Fill level (m)
Core collapsed level
Loop seal: RCP-side
Loop seal clearing
–0.1
–0.2
–0.3
260 260
Loop seal: SG side
Δp: RPV in/out
Steam
Water
Two phase mixture
Fig. 8.15 PKL test on loop seal clearing.

<!-- page 524 (PDF 32) -->
Insofar LSC is an issue related to core uncover/recovery in SB- and IB-LOCA transients
. The occurrence of LSC in relation to the occurrence of core uncover is mainly
determined by the difference in elevation between the top of the core and the horizontal
part of the LS. The timing, the dynamic of LSC as well as the number of loops
involved in LSC are depending on additional parameters such as break size, and flow
resistance via UP—DC bypass and by the operation of the SG secondary side (e.g.,
cool-down rate). LSC may also be influenced or even initialed by injection of ECC
water into the cold legs causing condensation at the injection location.
In addition, SETs on LSC were performed in the 1:1 scaled UPTF in a single loop
configuration in order to investigate the residual water level, the flow pattern, and the
pressure drop across the LS during and after its clearance (Liebert and Emmerling,
1998). As an example, Fig. 8.16 shows the pressure drop across the LS for varying
steam flow without droplet entrainment for two pressure levels. The amplitudes of
differential pressure for three different steam flow rates are also illustrated.

### 8.4.2.4 Flow reversal in SG U-tubes

NC plays an essential role in decay heat removal for a number of operational transients
and accidents in PWRs characterized by loss of forced circulation in the primary system
. Loss of forced circulation occurs under loss of off-site power conditions (RCPs
are no more available) or due to automatically or operator initiated shut down of the
RCP, e.g., in case of LOCA. Under NC conditions decay power is transported from the
−1
Pressure drop across loop seal Δp
kPa
0.1
0.2
Steam flow:   3 bar
Steam flow: 15 bar
Wallis paramater J∗
s
0.3
0.4
hi
Ms
Δp
•
0.5
Fig. 8.16 UPTF test on loop seal clearing (Liebert and Emmerling, 1998).

<!-- page 525 (PDF 33) -->
core (heat source) to the SGs (heat sink) at flow rates that are significantly lower than
the flow rates in normal (forced flow) operation (in the order of some percent, e.g.,
core flow rate in NC conditions: about 600 kg/s, for forced flow: about 20,000 kg/s).
The driving forces for NC are the temperature/density differences in the RPV
between the DC and the core region and in the SGs between the inlet and the outlet
side. In steady-state conditions the NC flow mass flow rates in the individual loops are
adjust in a self-regulating way so that the driving forces are equalized by the irreversible
pressure drops due to friction and local flow resistances. The performance of the
SGs in general, and the individual U-tubes in particular, is of great importance for the
overall system behavior under NC. The flow behavior of the individual U-tubes is a
rather complex mechanism, mainly because of the following two aspects:
–
The relatively low driving forces between the inlet and outlet plenum of the SG, typical for
NC conditions.
–
The existence of parallel flow channels between the inlet and outlet plenum of the SG
comprising several thousands of U-tubes with different lengths.
Extensive investigations on the flow behavior in the SG performed in integral test
facilities over the last decades revealed heterogeneous flow distribution among the
U-tubes for many NC situations. In these tests, flow reversal was observed in some
U-tubes leading to a flow from the SG outlet to the SG inlet plenum in such tubes while
at the same time other U-tubes still experienced forward flow from the SG inlet to
the SG outlet plenum. This heterogeneous behavior was observed under single and
two-phase flow conditions and also in the transition phases from two-phase flow
to reflux condensation and from reflux condenser conditions to the restart of
two-phase NC. Fig. 8.17 shows a typical situation with heterogeneous flow behavior
for single-phase NC. In the illustration, the short and medium tubes represent U-tubes
with forward flow and heat transfer from the primary to the secondary side mainly on
the lower part of the inlet side. The long U-tube represents U-tubes with reverse flow.
In such tubes the temperatures over the entire lengths correspond to the secondary side
and there is almost no heat exchange between the primary and secondary sides.
In the experiments the use of temperatures measured inside different U-tubes along
the tubes’ lengths is an appropriate method to detect the flow direction in these tubes.
If a tube is subject to continuous forward flow, it displays a temperature profile that
decreases from the primary side temperature at the tube inlet to the secondary temperature
toward the outlet. In contrast, an equalization of the primary and secondary
temperatures along the active length (no temperature profile) is an indication for flow
stagnation or flow reversal.
As an example, Fig. 8.18 shows the time trends of primary side temperatures on the
inlet sides of two different U-tubes of the same SG observed in a PKL experiment
during a phase with steady-state single-phase NC conditions. While the evolution
of the temperatures in tube 2 reflects continuous stable forward flow, the temperature
drop of the primary side temperatures down to the secondary temperature is a clear
indication for the interruption of forward flow in tube 1. The change in flow distribution
within the SG is also reproduced by a change in differential pressure between the
SG inlet and outlet plenum and a slight reduction in loop mass flow rate.

<!-- page 526 (PDF 34) -->
In NC conditions with heat transfer from the primary to the secondary side the pressure
difference between the inlet and the outlet plenum is normally negative (the outlet
pressure is higher than the inlet pressure). This results from the difference in gravitational
heads between the down flow side (cold) and the up flow side (hot) which generally
exceeds the frictional and local pressure drops along the tube at low flow rates
typical for NC. At higher flow rates the frictional pressure drop exceeds the gravitational
component and the resulting pressure difference over the SG reaches a
positive value.
Assuming that the pressure difference between the inlet and outlet plenum is the
same for all U-tubes, a negative value in NC conditions means that in tubes with
no temperature profile (difference in hydrostatic head is zero) flow reversal is
Hot coolant
(core outlet)
Cold coolant
(secondary side)
Long tube
SG
Medium tube
Short tube
Outlet
ΔpI,o
Δpm,o
Δps,i
Δpm,i
ΔpI,i
Δps,o
ΔpSG i,o
Inlet
Fig. 8.17 Heterogeneous behavior in SG U-tubes (forward and reverse flow).

<!-- page 527 (PDF 35) -->
expected to be established in these tubes. In general, the flow behavior in the individual
U-tubes is the result of the balance of the different pressure drop components
including frictional, local, acceleration, and gravitational pressure drops in different
U-tubes. Because of the composition of the different pressure components and the
interaction between the parallel connected U-tubes the “normal” forward flow in some
tubes may be disturbed, e.g., by a change in the boundary conditions. In the above
mentioned PKL test, a slight change in the secondary pressure was the reason for
the termination of the forward flow at least in one (of 28) U-tube.
Also mathematical models and solutions using the characteristic flow curves (differential
pressure over mass flow rates) for forward and reverse flow in single U-tubes
based on momentum and energy balance equations have been developed by several
researchers (see also Chapter 5 and 11 of the book) with the attempt to interpret/confirm
the observed heterogeneous flow behavior in the U-tubes, to demonstrate the
required conditions for reverse flow and to identify the preferred U-tube positions
for occurrence of reverse flow. More details on the applied methods can be found
in the corresponding literature.
It has to be mentioned that despite the possible occurrence of flow stagnation and
flow reversal in some U-tubes in NC conditions, the overall net forward flow will
always remain stable as long as the corresponding SG is available as heat sink.
The impact on the overall heat transfer is also rather small as the loss of heat transfer
in the tubes with reverse flow is compensated by the increasing heat transfer in the
Temperature
Temperature
Differential pressure “negative value”
Mass flow “positive value, forward flow”
Forward flow
Top of U-tube □ Tsec
Top of U-tube □Tsec
Forward flow
Interruption of forward flow
Bottom of U-tube
Bottom of U-tube
Temperature profile inlet side
Temperature profile inlet side
Reverse flow
Tube 1
Tube 2
Loop flow rate
SG in/out
Time
1 h
d
c
b
a
SG inlet
SG inlet
Fig. 8.18 PKL test on NC.

<!-- page 528 (PDF 36) -->
tubes with continuous forward flow (the SG are designed for much higher load). However
, the total mass flow rate through the SG and therefore also through the core may
be reduced as result of reverse flow in some U-tubes. This again leads to a higher core
outlet temperature. In order to address this aspect in code calculations, the application
of multitube modeling is of importance. It has to be noted that the flow behavior in the
U-tubes may be even more unstable and more heterogeneous under two-phase flow
conditions. Heterogeneous water/steam distribution at the tube sheet with preferred
steam supply to some tubes may promote the heterogeneous flow behavior in the
individual U-tubes.

### 8.4.2.5 Stability in boiling channels

Focus is given in this section to the qualitative role and the importance of pressure
drops in the characterization of stability of fluid systems (single- and two-phase).
Currently, there are more than 80 BWR operating all over the world that provide an
important contribution to the overall electricity supply from the nuclear source. The
water boiled in the core produces steam that is directly used to rotate the turbine(s),
thus constituting the simplest industrial system built so far that is suitable to transform
fission power into electrical power. However, fundamental aspects concerned with the
interaction between SYS TH and neutron kinetics obstructed or delayed (or made less
effective), so far, the exploitation of this type of reactor concept. The BWR stability
issue (D’Auria et al., 1997a,b) caused in the past a number of concerns and requested
specific attention by technologists and researchers.
The classification of instability mechanisms provides an idea of the topic.
Different classifications can be found in the literature. These can be based upon:
(a) fundamental mechanisms, (b) pattern of core oscillations, and (c) system
interactions.
(a) Classification based upon thermal-hydraulic fundamental mechanisms
The static instabilities are:
–
flow excursion (Ledinegg type);
–
boiling crisis;
–
relaxation types, including flow pattern transition, geysering, and chugging.
The dynamic instabilities are:
–
density wave oscillations;
–
pressure drop oscillations;
–
acoustic oscillations;
–
thermal oscillations.
(b) Classification based upon geometrical features of the oscillations
In this case the relationships between phases and amplitudes of the waves at different axial
and azimuthal positions in the core of a reactor or of a reactor simulator are considered.
Coupled neutron physics/thermal-hydraulic and pure thermal-hydraulic oscillations can
be distinguished, respectively. The following classification results:
–
core wide or in phase oscillations;
–
regional or out-of-phase oscillations;
–
single channel or local oscillations;

<!-- page 529 (PDF 37) -->
–
punctual or not propagating oscillations (their existence can only be envisaged from the
performed activity and considered documentation).
Most of the phenomena above can be explained making reference the concept of “harmonic
modes” of the reactor diffusion equations.
(c) Classification based upon system design
This classification is valid primarily for coupled nuclear-thermal-hydraulic systems (BWR
plants), but may occur also in pure thermal-hydraulic systems. The overall system performance
and the origin of oscillations are concerned. The following classification can be
introduced:
–
oscillations involving core-bypass;
–
oscillations involving vessel DC;
–
oscillations involving the entire primary loop (also referred as loop type oscillations);
–
oscillations induced by the Balance of Plant, including the control systems.
The analysis of instability phenomena may constitute a multidisciplinary subject,
involving different technological areas like transient thermal-hydraulics, neutronics,
fuel behavior and fuel cycle management, instrumentation, plant control and monitoring
, and detailed knowledge of plant features and operating conditions.
A wide literature exists in this area, see, e.g., Ishii and Zuber (1970), Yadigaroglu
and Chan (1979), D’Auria et al., 1997a,b, Vijayan (2002), and D’Auria et al. (2016).
Hereafter there is no intention to duplicate the information in reports and papers
devoted to the stability either in BWR and/or in boiling/condensing systems. However
, it seems worth mentioning that the measurement, the modeling, and the prediction
of pressure drops have a key role in this area. Sample reference data for pressure
drops during stability events are given in Figs. 8.19 and 8.20: these constitute typical
diagrams adopted to characterize the stability performance of a system. Change of
sign or passing from positive to negative value for pressure drops (Figs. 8.19 and
8.20) implies occurrence of flow reversal. Amplitudes and frequency of pressure drop
oscillation (Fig. 8.19) correspond to amplitude and frequency for mass flows.
−30
−20
−10
12,800 13,800 14,800 15,800 16,800 17,800 18,800 19,800 20,800
ΔP (Pa)
Time (s)
DR>1
LCO; DR = 1
Fig. 8.19 Characterization of an instability event: pressure drop versus time (Vijayan, 2002).
