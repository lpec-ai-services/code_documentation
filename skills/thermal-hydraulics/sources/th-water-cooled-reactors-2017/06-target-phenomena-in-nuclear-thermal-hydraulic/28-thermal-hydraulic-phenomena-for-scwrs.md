# Thermal-hydraulic phenomena for SCWRs
<!-- source PDF pages 100-106 -->

<!-- page 344 (PDF 100) -->
6.6
Thermal-hydraulic phenomena for SCWRs
SCWR has been currently chosen by Generation IV International Forum as one of the
reactor designs to be investigated. It is the only water-cooled NPP studied under the
Generation IV framework. In Europe, investigations on the SCWR concept have been
integrated into a joint research project, called high performance light water reactor
(HPLWR), which is a LWR operating at supercritical pressure (25 MPa). HPLWR
is cofunded by the European Commission and has been worked out by a consortium
of 10 partners from 8 European countries as their contribution to the Generation IV
International Forum. The concept is based on a RPV similar to a PWR, but designed
for a higher pressure of around 25 MPa. Other plant characteristics of the HPLWR
include also a coolant heat up from 280°C to more than 500°C (Squarer et al.,
2003). At these conditions, water changes its phase continuously from liquid to steam
without boiling, so that a boiling crisis in the core can be physically excluded. As in a
BWR, the high temperature steam is fed directly to the high pressure turbine, so that a
closed primary cycle like in a PWR can be omitted. Steam separators or primary
pumps, which are needed in BWRs, are not required either.
The high steam enthalpy increases the power density of the steam cycle by more
than 40%. The envisaged net efficiency of 44% exceeds by far those of conventional
LWR (Bittermann et al., 2004). It is expected that the HPLWR will be more economical
than conventional LWRs (Bittermann et al., 2003), it will have a higher
efficiency and thus a better fuel utilization, which also produces less waste per
kWh, but it still fulfills the high safety standards of third generation nuclear plants,
for example, EPR, SWR1000 (Aksan et al., 2003). Key advantages of this concept
shall be a significant reduction of equipment, resulting in a smaller building volume
and consequently of plant erection costs, compared with conventional PWR design,
and lower fuel costs thanks to the higher thermal efficiency, keeping the safety features
at least as advanced as with third generation LWRs.
During the safety analysis studies for the HPLWR, one of the initial phase activities
was to identify the new additional thermal-hydraulic phenomena which needs to be
considered for the thermal-hydraulic safety analysis. As a result of these investigations
, a list of thermal-hydraulic phenomena for HPLWR conditions has been identified
and selected in addition to the phenomena included in earlier studies mentioned in
Sections 6.3 and 6.4. These are:
–
thermal-physical properties near and at supercritical conditions,
–
critical flow during depressurization from supercritical conditions,
–
pressure loss characteristics of supercritical water (SCW),
–
HT characteristics of SCW,
–
reflooding for tight lattice geometry at low pressure,
–
boil-off for tight lattice geometry at low pressure,
–
instability and NC in supercritical pressure systems.
Above six identified thermal-hydraulic phenomena for HPLWR have also been confirmed
for other SCWR designs (eight different concepts including SCWR using
heavy water) during investigations and studies carried out (2007–12) by a group of

<!-- page 345 (PDF 101) -->
scientists in the Cooperated Research Program (CRP) of IAEA on “HT Behaviour
and Thermohydraulics Code Testing for Super Critical Water Cooled Reactors
(SCWRs)” (IAEA and Aksan, 2014)

## 6.6.1 Thermal-physical properties near and at supercritical conditions

HT at supercritical pressure is mainly characterized by the thermal physical properties
which vary strongly, especially near the pseudocritical line. Fig. 6.1 shows the specific
heat as a function of pressure and temperature.
It is seen that at each pressure there is a local maximum of the specific heat capacity
. In the subcritical pressure range the maximum specific heat locates on the saturation
line. At the critical point (P=22.1 MPa, T=374°C) specific heat has its
maximum value. In supercritical pressure range, the line connecting the maximum
values of the specific heat is called pseudocritical line (PCL), as shown in Fig. 6.2.
Fig. 6.1 Specific heat of water (Wagner and Kruse, 1997).
Temperature (°C)
Pressure (MPa)
Pseudocritical line
Fig. 6.2 Pseudocritical line
PCL in a P-T diagram.

<!-- page 346 (PDF 102) -->
It is seen that the pseudocritical temperature increases with increasing pressure.
At a pressure of 25 MPa the pseudocritical temperature is 384°C. The specific heat
at the critical point is as high as 5600 kJ/kg K, which is more than 1000 times higher
than that at room temperature. Near the pseudocritical line the density decreases
dramatically. There exists a large peak of the thermal expansion coefficient, which
behaves very similar to the specific heat. Thermal conductivity decreases with
increasing temperature. It shows, however, a local maximum near the pseudocritical
point. Beyond the pseudocritical temperature thermal conductivity decreases sharply.
Similar behavior shows also the dynamic viscosity. Due to the sharp increase in
specific heat capacity, there exists a large peak of the Prandtl number at the
pseudocritical point.
It has been found that near the critical point, thermal-physical properties obtained
from different sources might deviate strongly from each other, especially as related to
specific heat and thermal conductivity. This is due to the steep variation of the fluid
properties, leading to a less accurate interpolation and a lower measurement accuracy.
A comparison between two water-steam tables in use at EDF has shown a deviation of
up to 35% for thermal conductivity and up to 10% for heat capacity at a condition
close to the critical point. If the physical properties are showing these types of deviations
, the physical parameters, which describe certain PH, for example, HT coefficient
will also show some calculated differences. Consequently, it is important to use
the same or at least similar steam tables for the application and use of different computer
codes within a design or safety-related project, when analysis work is performed.
Based on the experience gained and the critical review performed during the
HPLWR project, it was recommended that the steam tables of IAPWS-97 and
IAPWS-95, whichever relevant was well accepted by international institutions and,
therefore, should be taken as reference. Due to the large expenditure needed for the
implementation of such a steam table into the existing codes, it is not required to
use unique steam table for each of the code, but the deviation (compared to
IAPWS-97, respectively to IAPWS-95) of the steam tables used should be clearly indicated
. The International Association for the Properties of Water and Steam (IAPWS) is
an international, nonprofit association of national organizations concerned with the
thermo-physical properties of water and steam, particularly those properties of high
temperature steam, water, and aqueous systems that are relevant to thermal power
cycles and other industrial applications. The IAPWS released its formulation for general
and scientific use in 1995. IAPWS-95 is a state-of-the-art accurate representation
and covers the entire range of light water properties (Wagner and Kruse, 1997). At the
limit boundaries, ideal gas behavior is satisfied and at the other “residual” behavior.

## 6.6.2 Critical flow during depressurization from supercritical conditions

Critical flow is defined as the maximum flow that can pass through an opening for a
given thermodynamic condition. Under this definition, numerous different configurations
are possible: orifices or long tubes, single-phase flow or two-phase flow, rough

<!-- page 347 (PDF 103) -->
or smooth tubes, sharp or round entrances, etc. All of these configurations affect the
flow in their own manner and thus have to be characterized upon the specific application
, in this case, an LOCA of a SCWR.
When a fluid discharges from a high pressure and high temperature system, a
“choking” or critical condition occurs, and the flow rate no longer increases as the
downstream pressure is further decreased. During a postulated LOCA of a PWR
the break flow will be subject to this condition (see Section 6.3.2 for details).
An accurate amount of the critical flow rate is important for the evaluation of the reactor
safety, because this flow rate controls the loss of coolant inventory and energy
from the system, and thus has a significant effect on the accident consequence.
A depressurization event or LOCA is particularly of a concern for the SCW reactor
safety due to the lower coolant inventory compared to a typical PWR for the same
power output. This lower coolant inventory would result in a faster transient response
of the reactor dominated by the discharge flow rate. Critical flow is coupled with
drastic depressurization and vaporization, and the flow rate is heavily dominated
by the vapor content or quality of the vapor, which is closely related with the onset
of vaporization and the interfacial interaction between phases. This presents a major
challenge for the estimation of the flow rate due to the lack of the knowledge on those
processes, especially under the conditions of interest for the SCWR. High pressure
depressurization leading to critical flow has been investigated extensively, in both
experimental and theoretical ways. These studies have mostly been conducted with
subcritical pressure or ideal gases well above the vapor dome, as presented in number
of comprehensive reviews. Selected examples of these reviews can be given as in
Levy et al. (1982) and Lee and Swinnerton (1983), and Saha (1978), but little work
has been done near or above the thermodynamic critical point. To the author’s knowledge
, the available experimental data for SCW are those obtained by Lee and
Swinnerton (1983) at a maximum temperature of 402°C and by Chen with a maximum
temperature of 474°C (Chen et al., 2009). Based on the limited data of supercritical
fluids, the critical flows at conditions above the pseudocritical point seem to
be fairly stable and consistent with the subcritical HEM predictions. Further, in this
regime the flows tend to be lower than those in the two-phase region. Thus the major
difficulty in the prediction of the depressurization flow rate remains in the region
where two phases coexist, that is, within the two-phase portion of the vapor dome.
In this region, the flow rate is strongly affected by the nozzle geometry and tends
to be unstable. Various models for this region have been developed with different
assumptions, for example, the HEM and Moody model (Moody, 1965), and the
Henry-Fauske nonequilibrium model (Henry and Fauske, 1971) are currently used
in subcritical pressure reactor safety design (Ardron and Furness, 1976). It appears
that some of these models could be reasonably extended to above the thermodynamic
pseudocritical point. The more stable and smaller flow observed in conditions above
the pseudocritical point suggests that even though SCWR designs have a smaller
coolant inventory, the safety implications of an LOCA and the subsequent depressurization
from supercritical conditions may not be as severe as expected and the limiting
accident scenario may be driven by the critical flow within the subcritical
pressure region.

<!-- page 348 (PDF 104) -->
## 6.6.3 Pressure loss characteristics of SCW

Pressure losses in the heat transport system have a direct impact on the pump
capacity and the power output, affecting the capital and operating costs. In addition
, these losses affect the local flow conditions along the fuel assembly impacting
the HT characteristics. Depending on the design, the pressure loss components consist
of frictional loss, form losses (such as valves and elbows), head loss due to
gravity, and loss due to acceleration. A significant portion of the overall pressure
loss occurs in the core region (particularly over the bundle assembly). Therefore, it
is important to evaluate the core pressure loss accurately (see also Sections 6.3.1.7
and 6.3.1.8).

## 6.6.4 HT characteristics of SCW

In supercritical fluids, the properties change rapidly with the temperature, especially
in the pseudocritical region. Here, the local HT coefficient varies significantly, depending
on flow conditions and the value of the heat flux. Effect of heat flux, together with
the thermo-physical properties variations needs to be understood, based on experimental
, numerical, and theoretical data available in order to be able to predict the onset
of heat transfer deterioration (HTD).
As already indicated in Section 6.6.1, a large variation of thermal physical properties
occurs near the pseudocritical line. This would lead to a strong variation in
HT coefficient. Just considering simply for single-phase steam flow near and at supercritical
conditions, the Dittus-Boelter equation gives at the pseudocritical point
(T=384°C) a HT coefficient of about 40 kW/m2K, more than twice of that at low temperature
(e.g., 300°C) and five times of that at high temperature (e.g., 500°C). This
shows clearly that due to the variation in thermal physical properties, HT coefficient
varies strongly near the pseudocritical line. The closer the pressure to the critical point
is, the higher is the peak of the HT coefficient.
As indicated and agreed in the open literature, the actual HT coefficient deviates
from the Dittus-Boelter equation, especially near the pseudocritical line. At low
heat fluxes, HT coefficient is higher than the values predicted by Dittus-Boelter.
This PH is called HT enhancement. At high heat fluxes the HT coefficient is lower
than that computed by the Dittus-Boelter equation. At a low heat flux the wall temperature
behaves smoothly and increases with increasing bulk temperature. The
difference between the wall and the bulk temperature remains small. At a high heat
flux a similar behavior of the wall temperature is expected, except for the bulk temperature
approaching the pseudocritical value. In this case a sharp increase in the
wall temperature can occur. The wall temperature decreases again, when the bulk
temperature exceeds the pseudocritical value. This large increase in the wall temperature
is referred to heat transfer deterioration. In the literature there is still no
unique definition for the onset of HTD, because the reduction in HT coefficient, or
the increase in the wall temperature behaves rather smoothly, compared to the
behavior of the boiling crisis at which a much sharper increase in the wall temperature
takes place.

<!-- page 349 (PDF 105) -->
## 6.6.5 Reflooding for tight lattice geometry at low pressure

The concept and also the geometric arrangement of HPLWR core, as example of
SCWRs, differs drastically from conventional LWR concepts by the use of SCW to achieve
higher core outlet temperatures. The fuel assembly design examples are based on
tight lattice geometry and also have different configurations (Hofmeister et al.,
2005). Considering these types of fuel assembly arrangements, tight lattice geometry
and special arrangements of fuel rods is considered to be a solution. In general, quenching
and rewetting phenomena process defined and described in Sections 6.3.13.1 and
6.3.13.2 for SET is valid also for tight lattice geometries. But it has to be considered that
specific reflooding modeling and experiments are needed for selected geometrical
consideration.

## 6.6.6 Boil-off for tight lattice geometry at low pressure

As already mentioned and considered in Section 6.6.6, CHF and post-CHF HT phenomena
defined for SET in Sections 6.3.12.3–6.3.12.5 are valid also for tight-lattice
geometries. But it has to be considered that specific CHF and post-CHF HT models
and experiments are needed for selected geometrical consideration.

## 6.6.7 Instability and NC in supercritical pressure systems

The design of SCW-cooled reactors poses new challenges in relation to the prediction
of some basic phenomena, whose characteristics are relatively well known at subcritical
pressure. In particular, stability and NC phenomena observed in single-phase conditions
at subcritical pressures become more complex at supercritical pressures
because of the strong variability of thermodynamic and thermophysical properties.
Moreover, categories adopted for dealing with two-phase flow phenomena must be
updated to deal with supercritical pressure flow regimes, having in principle a simpler
structure than the corresponding two-phase flow ones, though they anyway involve
uneven distributions of lighter and heavier fluids within the channel cross-section.
Flow instabilities and NC, being dealt with in this section, have been the subject of
major experimental and modeling efforts at subcritical pressures. Some of these studies
belong to both aspects, since a quite populated intersection of the two categories is
represented by the interesting domain of NC instabilities. In single-phase flow, in particular
, apart from turbulence and acoustic effects, which are beyond the scope of this
section, instabilities mainly occur in NC systems, being driven by a mechanism
explained with effective elementary arguments by Welander in 1967 (Welander,
1967). In that work, it was suggested that pockets of fluid with perturbed temperature
may emerge from the heat source and/or the sink, affecting the fluid residence time
along the loop and being damped or amplified as a consequence of the subsequent
passages through the heater and the cooler. This mechanism was proposed on the basis
of numerical computations and was confirmed later on by further experimental and
computational studies, focusing on different interesting aspects affecting the PH
(see, e.g., Creveling et al., 1975). A remarkable feature of the observed behavior is

<!-- page 350 (PDF 106) -->
its chaotic character, mainly caused by the fact that the growth of flow perturbations
frequently leads to flow reversal; as a consequence, the system is seen to continuously
switch from clockwise to counterclockwise flow directions and vice versa, showing a
high sensitivity to initial conditions. Two-phase flow instabilities are mainly connected
with the behavior of boiling channels that are recognized to be susceptible
to different instability mechanisms, having a “static” or a “dynamic” nature (see,
e.g., Lahey and Moody, 1993). The discrimination among the two categories of instabilities
is introduced considering whether their occurrence can be explained on the
basis of the static internal PD versus flow characteristic of the system. The Ledinegg
“excursive” instability mechanism (Ledinegg, 1938) is representative of the category
of static instabilities, while density wave, PD oscillations and thermal oscillations are
mechanisms which belong to the second category. Of these instabilities, density waves
represent the most relevant instability mechanism for nuclear reactor applications
since, in combination with neutronic feedback, it is responsible for observed space
and time oscillations of BWR core power. These instabilities have been the subject
of extensive studies, summarized in review papers and SOARs (March-Leuba and
Rey, 1993). Basic experimental investigations (see, e.g., D’Auria et al., 1997) allowed
grasping the main features of involved phenomena, gaining the basic understanding
necessary for analytical developments. An interesting body of information about reactor
plant events is also available (see D’Auria et al., 1997). Models for predicting the
unstable behavior of boiling systems have been set up and qualified by applications
ranging from the scale of experimental facilities to the full reactor scale (see, e.g.,
D’Auria et al., 1997). Both time-domain (i.e., transient) and frequency-domain
(i.e., linearized) models are available to estimate the stability thresholds of even very
complex systems. NC phenomena have also been thoroughly studied at subcritical
pressures, both in single- and two-phase flow conditions. The relevance of this PH
for nuclear reactors is well known, since NC involves several regimes of reactor operation
. As previously mentioned, NC and stability phenomena have an extensive intersection
in single- and two-phase flows. A limited list of relevant aspects relating NC at
subcritical pressures is reported hereafter:
l
Different single- and two-phase NC modes appear during start-up, under normal operating
conditions and postulated LWR accidents, as observed in experiments and code predictions
(see, e.g., D’Auria and Frogheri, 2002).
l
NC is relied upon for decay heat removal from the nuclear reactor core and/or the containment
system; in particular, passive decay heat removal by NC represents one of the most
important features in advanced (Gen III) and innovative (Gen IV) reactors.
l
Different modes of flow instabilities are recognized in NC boiling systems, adding additional
phenomena to be addressed to those already observed in boiling channels (see, e.g., D’Auria
and Frogheri, 2002).
l
The vast body of information from experimental and theoretical researches on stability and
NC performed at subcritical pressures constitutes a useful background also for SCW reactor
applications, at least in view of two main aspects.
l
The knowledge acquired on fundamental phenomena can be helpful in supporting the new
developments required for supercritical pressure conditions, provided that analogies and differences
between the two operating regions (subcritical and supercritical) are properly
identified.
