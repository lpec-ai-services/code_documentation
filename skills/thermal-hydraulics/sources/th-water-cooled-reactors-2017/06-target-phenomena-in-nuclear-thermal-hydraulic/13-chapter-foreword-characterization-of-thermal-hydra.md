# Chapter foreword — Characterization of thermal-hydraulic phenomena for set — Global multidimensional fluid temperature, void, and flow distribution
<!-- source PDF pages 44-48 -->

<!-- page 288 (PDF 44) -->
### 6.3.11 Global multidimensional fluid temperature, void, and flow distribution

Phenomena in this section address mainly the three-dimensional flow behavior in
selected components compared with phenomena described in Section 6.3.3. Global distribution
means large-scale behavior of the fluid temperature, void, and flow distribution
within special components such as the UP, core, downcomer, or SG secondary side.
Nearly all two-phase flow phenomena are inherently three-dimensional and unsteady
on a fluid-element scale, for example, in a droplet and in the gas field around a droplet.
Also turbulent fluctuations are ignored in all practical problems, and space-time averaging
of the conservation equations filters them out. Only the average three-dimensional,
time-varying characteristics of the flow over the size of the numerical mesh cells can be
retained. Within this average framework, the terms for the production and convection of
fluxes of mass, momentum, and energy are all specified in a mathematically rigorous
form(Yadigarogluetal.,1990;OECD/NEA,1989).However,theaveragingprocessgenerates
unknown distribution coefficients for the convective terms and several unknown
coefficients for the wall and interface transport terms. Distribution coefficients are usuallytakentobeunity
.Transportorconstitutiverelationshipsareoftenassumedtobealgebraic
relationships involving parameters such as friction factors, drag coefficients,
and HT coefficients, derived from the fully developed situation and related to
one-dimensional variables such as the cross-sectional average velocity—all these have
to be established empirically.
On the other hand, three-dimensional phenomena are sometimes very evident, even
dominating the local thermal-hydraulics, in large size flow passages of the primary
system, such as the UP in the reactor vessel, the core and the downcomer in a
PWR. Mixing, condensation, and CCF of liquid and vapor during ECC injection
are typical examples which give rise to three-dimensional velocity, temperature,
and
void
distributions
in
these
regions.
One-dimensional
mixture
and
one-dimensional two-fluid models can only average these three-dimensional effects
into their one-dimensional framework, which may penalize the scaling and generality
of their prediction capabilities. Thus, uncertainties introduced by the one-dimensional
approximation have to be assessed from near full-scale experiments.
UPTF results indicate that the larger the size of a flow passage (such as the reactor
vessel downcomer, or the UP and core), combined with nonuniform geometric distribution
of water inlet and flow outlet, the more multidimensional the flow distribution
becomes (Glaeser, 1992). Fluids of different density and different direction of flow
find it much easier to establish their own preferred flow paths in which the flow is
predominantly cocurrent rather than countercurrent.
The two-fluid code TRAC allows a three-dimensional representation of the pressure
vessel. However, interface transfer like shear stress, heat and mass transfer
between the fluid in neighboring fluid is included only where there is bulk flow
exchange between the cells (Glaeser, 1990a,b). The averaging process within the cells
is described above.
One of the major sources of uncertainty in current thermal-hydraulic computer
code simulation is the fact that it is not adequately known for all flow situations,

<!-- page 289 (PDF 45) -->
how to describe the local interfacial area density and the momentum, mass, and energy
transfer rates at those interfaces, irrespective of the computational cell size.
All the above considerations specifically address the geometric configuration of
the primary circuit of PWRs. Nevertheless, these are essentially valid for BWRs,
for which case the following aspects can be added:
–
The multidimensional behavior in the Iower plenum occurs as in the case of PWRs with the
additional complexity arising from the presence of the control rod guide tubes (CRGTs)
with related CCFL and delayed flashing phenomena.
–
The multidimensional behavior in the core originates from the interaction of single channels
, where the flow can be locally two-dimensional, from channel to channel and involve
multidimensional interchange with the upper and lower plena. Additional detail can be
found in Section 6.3.11.2.
–
The multidimensional behavior in the UP is less complex than in the PWR case because of the
geometricalconfigurationthatallowsonlyverticalflowsfromcoretoseparators;infactnohorizontal
connections corresponding to PWR hot legs are present. The injection of spray systems
inside this zone creates thermodynamic situations that are similar tothose created in the caseof
hot-leg injection in a PWR (see also Section 6.3.9.1). Multidimensional phenomena may take
place in the steam dome in the case of a main steam line break (MSLB) or during the period of
actuation of the fast depressurization system (ADS, automatic depressurization system), also
causing eccentric loading of the internal structures. These are not further considered here
because of their low relevance in terms of safety and to the global behavior of the system.
–
The geometric dimensions of the vessel downcomer (thickness and flow area) are much
greater in a BWR compared with a PWR. This makes the 3-D behavior of the BWR vessel
downcomer less important compared to the PWR. The relatively small ratio between the
feedwater flow area and the downcomer cross-section area (in comparison with the ratio
of
cold
leg
area
to
downcomer
cross-section
area
in
a
PWR)
also
reduces
three-dimensionality. Three-dimensional effects can occur in the case of the break of
one recirculation line (for additional details, see Section 6.3.11.3) while limited or no (in
the majority of BWRs) 3-D effects are expected following the injection of emergency
cooling system water.
Phenomena in this section also incorporate the PH of temperature stratification. Temperature
stratification in the water in the LP and in the U tubes of the SGs are not specifically
addressed in this section, but may have an influence on the system behavior,
if this water is pushed to other locations (e.g., into the core). Its relevance to nuclear
safety is considered to be low.
6.3.11.1
Global multidimensional fluid temperature, void,
and flow distribution–UP
The flow in the UP is three-dimensional. During the blowdown period of a LBLOCA,
for example, water is delivered from the PRZ and the SG primary side into the UP via
the hot legs.
In the case of hot-leg ECC water injection, water is injected toward the UP via a
special nozzle at the bottom of each hot leg. The water jet is directed out of the hot legs
horizontally into the UP. The ECC water impinges on the columns (guide tubes) in the
UP and is directed downward.

<!-- page 290 (PDF 46) -->
The water downflow location in the UP determines the downflow location through
the upper end box, including the UTP, into the core region. This observation has been
made in UPTF and other large-scale test facilities like SCTF and CCTF (Damerell
et al., 1993a,b; MPR Associates, 1990). The magnitude of the cross-section of the
ECC water downflow in the UP and in the core is important for partially cooling
the core during the end of blowdown and refill period of a postulated LOCA. Multidimensional
effects are also of prime importance in estimating fuel rod damage during
the heat-up period. The UP multidimensional flow is one of the most important phenomena
during refill and reflood with hot leg or UP ECC injection.
The liquid inventory in the UP is relevant for steam binding, if no subcooled ECC is
injected into the UP (only cold leg or downcomer injection). The UP liquid inventory
for all injection designs may be important for washout of fission products released
from defect fuel rods. (Fission product transport and distribution themselves are
not considered in this chapter.)

#### 6.3.11.2 Global multidimensional fluid temperature, void, and flow distribution—core

During normal operation of a PWR the core is completely covered with water whereas
in a BWR the steam is produced in the core. Even when the core is liquid covered, flow
patterns, which are essentially three-dimensional rather than 1-D, can be set up. In the
case of an accident the water level may drop and the cooling of the core has to be
reestablished by means of the ECC system.
Cold-leg injection leads to a core refill from the bottom upwards. The combined coldandhot
-legECCinjectionorthehotlegonlyinjectionleadstoalocaltop-downcoolingof
the core in addition to refilling from the bottom. The hot-leg ECC injection water flows
down within preferred flow paths. The precursory cooling in these water downflow locations
is higher than in the steam dominated core regions. The precursory cooling may
reduce the possible fuel rod damage during the heat-up period.
A three-dimensional distribution of water downflow and steam upflow establishes
itself above the swell level in the core. After the start of bottom reflood the void fraction
and flow distribution determines the further core cooling.
There is also some local top down water flow in the core from the PRZ and the SGs
during blowdown.
In the case of BWRs the different parallel channels bounded by the fuel boxes may
cause different flow regimes (Dix, 1983): three of these may occur at the same time
during a typical LOCA transient. In the peripheral region of the core, where the coolant
is sprayed, and in the bypass region, where there is almost no power production, the
subcooled liquid may flow downward from UP to LP (CCFL breakdown condition),
thus condensing almost all the steam eventually produced. In other zones of the core,
a few fuel channels vent the flashing vapor from the LP which results in cocurrent
upflow condition of steam and entrained droplets in those channels. At the same time
the remaining parts of the fuel channels may experience typical CCFL conditions at the
bottom, with level formation inside the fuel bundles (see Section 6.3.10.2).

<!-- page 291 (PDF 47) -->
Looking at the overall scenario, a typical horizontal “sandwich” situation is
expected with level formation in the LP (the steam is produced due to boil-off caused
by the depressurization), core (the steam is produced by the evaporation of the coolant
and by depressurization), and UP (the liquid is produced by the de-entrainment of
droplets from core and by the injection of the spray systems).
The cooling of the core by means of available remaining water or by injected subcooled
ECC water is the most essential safety aspect. The increase of water inventory
by means of ECC injection determines the HT from the fuel rods.
Three-dimensional flow is important for combined injection (into hot and cold legs
during refill), and is ranked important for cold-leg injection only during reflood in
LBLOCA (OECD/NEA, 1989; Wilson et al., 1990).
The 3-D flow behavior is important in the case of BWRs considering that the flow
patterns discussed above constitute a typical configuration for the core.

#### 6.3.11.3 Global multidimensional fluid temperature, void, and flow distribution—downcomer

During the blowdown and LP refill of an LOCA, the ECC water injected into the cold
legs flows down the downcomer below the injection cold legs, if the steam upflow is
sufficiently low. With increasing steam upflow the water downflow may be limited
(see Section 6.3.10.5).
If the collapsed water level is higher than the bottom of the downcomer (above the
lower edge of the downcomer skirt) the steam upflow from the core is stopped.
During core reflood, the water level in the downcomer approaches the bottom of
the cold-leg height. An azimuthal steam flow is directed from the intact cold legs to the
broken cold leg within the downcomer, which may entrain water from the downcomer
through the broken cold leg. Consequently, the downcomer liquid head, which is the
driving force for core reflood, is reduced.
The distribution of the down flowing ECC water in the downcomer has an influence
on the water delivery to the LP which may be limited by steam upflow. Multidimensional
effects are ranked as being important during LBLOCA refill (OECD/
NEA, 1989; Wilson et al., 1990).
A reduction of the downcomer liquid head may reduce the driving force for
core reflood.
During subcooled ECC water injection into hot water the temperature distribution
in the downcomer may be of interest for evaluating the PTS stress on the reactor
vessel wall.

#### 6.3.11.4 Global multidimensional fluid temperature, void, and flow distribution—SG secondary side

In the SG secondary side there are several areas where multidimensional effects are of
high importance and will influence the overall behavior of the primary to secondary
side HT. The flow rate on the secondary side is determined by NC, and small changes
to void and temperature distributions can have a substantial impact on the flow

<!-- page 292 (PDF 48) -->
conditions and hence on the local HT. This has been demonstrated, for example, at
feed and bleed operation of the auxiliary feedwater flow in the case of loss of main
feedwater, where subcooled auxiliary feedwater is mixed with the vapor in the SG
downcomer (D’Auria et al., 1993).
At the top of the downcomer subcooled feedwater is mixed with saturated liquid
which is returning from the separators and dryers. Some vapor will be present in this
separated liquid flow (carryunder) which will be condensed on contact with the
feedwater. The feedwater is provided fairly uniformly around the top of the downcomer
resulting in rather uniform downcomer flow conditions.
At the bottom of the downcomer the flow enters the riser where the liquid is heated
to saturation and boiling starts. Baffle plates will force the flow to pass the tube bundle
in a transverse direction along with its main axial direction. This increases the HT
coefficient on the tubes outer surface.
The two-phase flow enters the steam separators located at the top of the riser. The
number of separators can vary from only a few to a vast number in parallel. They all
rely on separation due to centrifugal forces. The two-phase mixture is set into rotation
by means of swirl vanes at the separator inlets. The liquid will then be “spilled” over
the separator top edge and will fall back to downcomer.
The vapor with some liquid droplets (carryover) then enters the dryers in the
steam-generator dome. In the dryers the remaining liquid is separated from the vapor
and is feedback to the downcomer. The vapor passes through the SG outlet nozzle and
enters the steam line.
Multidimensional effects prevail at almost every location in the flow path due to
the system geometry, and the mixing of liquid and vapor. However, the most important
parts are the riser and the steam separators.
In the riser the baffle plates force the two-phase flow into a zigzag flow path.
Behind the plates and tubes eddies will be created, which will strongly influence
the two-phase flow pattern and the interfacial area distribution. It is likely that a dispersed
regime will be promoted even under conditions where other flow regimes normally
would prevail. As mentioned above also the HT on the outer surface of the tubes
will be augmented compared to ordinary pipe flow because of the crossflow nature of
the flow.
In the separators, three-dimensional effects will be introduced through the circulation
of the flow. These effects will govern the actual separation of the two-phase
mixture and will determine the carryunder and carryover fractions in the separated
flow. The interfacial area and the slip are of essential importance for the separation
behavior. The presence of a preheater in some SG designs produces additional multidimensional
effects.
During the course of intermediate and SBLOCAs it is essential to keep the heat
sinks as intact as possible to mitigate the consequences of the transients. However,
the detailed conditions of the SG secondary side are not of crucial importance in this
respect, and neither are the two-phase multidimensional characteristics of the secondary
flow in many cases. It has been found, though, that the conditions in the downcomer
in some cases have influenced the overall SG behavior.
