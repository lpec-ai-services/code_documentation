# Chapter foreword — Characterization of thermal-hydraulic phenomena for set — Heat transfer … Noncondensable gas effect (PWR)
<!-- source PDF pages 49-64 -->

<!-- page 293 (PDF 49) -->
### 6.3.12 Heat transfer

The HT between wall structures and fluid is an essential heat transport mechanism in
LWRs for transporting the heat generated in the core to the turbines. In the first step,
the heat is transferred in the core from fuel to fluid. The SG tubes transmit the heat
between the high pressure primary side and low pressure secondary side. The safety
aspects of the HT are mostly related to the core region.
The fuel cladding temperature is usually near the saturation temperature of
water. During an accidental increase in power, or decrease of flow and pressure,
a deterioration in the HT process is possible. The surface temperature increases
to such a high level that the heated surface can no longer support continuous liquid
contact. This PH is called boiling crisis or dryout depending on the mechanism
leading to the event. The key question is how efficiently the deteriorated HT
mechanism can remove heat generated in the core after the reactor shutdown.
The HT problems are both global in the case of core uncovery and local for high
power rods.
Due to the inadequate understanding of HT mechanisms, an empirical approach is
often necessary. This approach requires the derivation of empirical HT correlations
for each HT configuration, resulting in numerous correlations for each HT mode.
Some correlations are based on the phenomenological basic formulations for
explaining the parametric tendencies, but typically some key parameters are required
for fitting against the experimental data.
At the present time, quite a large selection of HT correlations exists in the world
literature and many correlations are derived from a large database. Most of the HT
correlations are based on tube data, since the simplest test geometry is a heated
tube. Extrapolation of the tube correlations to other geometries (bundles, annuli) is
common practice in reactor safety analysis. In principle no new SETs are needed
for the more accurate calculations of HT in expected incidents. The problem for model
development is inadequate measurements of local parameters needed for developing
models of HT mechanisms for two-fluid codes.

#### 6.3.12.1 Natural or forced convection (FCO) in the core, in the SG, and at structures

Either FCO or natural convection (NCO) can occur when single-phase liquid,
vapor, or two-phase flow is present. During normal operation of a PWR the
FCO to single-phase water is the main HT regime in the primary coolant system.
In the core, subcooled boiling may also occur. During normal operation of a BWR
FCO to single-phase liquid in the core occurs only in the lower entrance region,
while two-phase forced convective HT is the HT regime in the upper part of
the core.
NC of the single-phase water may occur, if the reactor is scrammed and the main
coolant pumps are switched off due to different water densities in the hot part (core,
UP, and hot part of SGs) and the cooler part of the primary system (cold side of SG

<!-- page 294 (PDF 50) -->
U tubes and downcomer). In this situation forced or NCO HT (depending on the Reynolds
number of the flow) can occur at any of the components involved.
Two-phase natural convective HT is important for the HT from the core to the SG
secondary side in the case of small leak scenarios.
Two-phase convective HT is described in Sections 6.3.11.2–6.3.11.4.
Cooling of the core and the primary side fluid inventory via the SG has the highest
priority in nuclear reactor safety. Apart from core and SG HT an additional heat input
may be relevant from hot structure material to the primary side water or steam during
blowdown, for example, and the heat loss from the primary side to the environment
through the vessel and piping structure material may affect the system behavior during
long transients.

#### 6.3.12.2 Subcooled and nucleate boiling HT

The transition from single-phase liquid HT to nucleate boiling takes place, once the
wall temperature exceeds the temperature for onset of nucleate boiling. According to
one hypothesis, the condition for nucleation and thus the onset of subcooled boiling is
the point where the convective heat flux and boiling heat flux are equal. More refined
treatment of nucleation can be derived by considering the temperature profile in the
region adjacent to the wall.
Fully developed subcooled boiling does not exist immediately the surface exceeds
the saturation temperature. A region of partial boiling exists between the subsaturation
zone and fully developed subcooled boiling.
The heat flux/surface temperature relationship in the fully developed region is
independent of velocity and subcooling and may be correlated by the equations of
the type obtained from pool boiling experiments, where the constant coefficients
are mainly functions of the pressure, and the heat flux is a function of the wall superheating
with an exponent n=2, …, 4.
Saturated nucleate boiling starts when the bulk liquid temperature equals saturation
temperature. In saturated boiling the HT consists of two contributions, a nucleate pool
boiling term and a convective term. The Chen correlation (Hsu and Graham, 1986) is
an example of this kind of formulation. The FCO contribution is multiplied by a
two-phase factor F and the nucleate boiling term by the suppression factor S when
the local quality increases.
The nucleation term represents the normal nucleation caused by the nucleation sites
on the wall. The convective term is an effect of the forced vaporization through the
annular liquid layer on the wall.
The nucleate boiling region is an essential part of the HT curve. The onset of
nucleate boiling has an effect on the void profile and thus on the nuclear power profile
in the BWR core. In the PWR core no bulk boiling is expected, but subcooled
nucleate boiling (SNB) can occur in the top third of the core. The possible local
voiding thus generated has the unwanted side effect of disturbing the neutron power
profile.
Nucleate boiling is particularly relevant in special cases such as ATWS in BWRs.

<!-- page 295 (PDF 51) -->
#### 6.3.12.3 Departure from nucleate boiling/dryout

A large number of terms have been used in the literature to denote the occurrence
of CHF: burnout, dryout, boiling crisis, CHF, and DNB. The term DNB is usually
reserved for the occurrence of CHF in the subcooled region caused by microlayer
evaporation under a bubble. Typical mechanisms creating this kind of situation are
the depressurization of the flow channel increasing the wall superheating, decreasing
the liquid subcooling, and perhaps creating a bulk boiling in the liquid together with a
strong nucleate boiling.
Dryout refers to the CHF occurrence caused by evaporation of the wall liquid film
in the annular flow regime. When three fluid fields are considered in an annular flow
pattern, vapor, liquid film, and droplets entrained from the liquid core, the hypothesis
is that the boiling crisis in annular film occurs when the liquid film is depleted by
evaporation and entrainment. A typical situation creating this kind of CHF pattern
is a stationary boiling channel in stationary forced flow conditions, where an annular
flow pattern exists.
The following observed asymptotic trends are valid for the CHF:
–
local subcooling increases CHF,
–
CHF approaches pool boiling CHF at low flows,
–
CHF approaches zero for quality (void fraction) approaching unity,
–
CHF reaches a maximum in the pressure (P) range of 3–4 MPa,
–
CHF approaches zero when P approaches critical pressure,
–
the existence of spacers in the bundle increases CHF rate.
For steady-state operation of the reactor the avoidance of CHF is one of the main
criteria in acceptance of the plant power level. Taking into account the peaking factors
for the maximum power fuel bundle and for the maximum power fuel rod, no CHF is
allowed during steady-state conditions. Rods experiencing CHF may be damaged.
The criterion is also used in anticipated transients, when the plant protection systems
are operating normally.
In accidents including LOCA or in transients with an additional failure of plant
protection systems, CHF at least in the hottest rods may be expected, and as a consequence
the rods may be damaged causing a release of radioactivity to the coolant. During
LOCA the occurrence of CHF initiates the core heat up period.

#### 6.3.12.4 Post-CHF HT

The post-CHF regime means in general the regime where the hot wall temperature or
lack of coolant does not allow liquid to contact the surface. The HT models considered
under this title are the transition boiling, film boiling, HT to the droplet dispersed mixture
, and convection to single-phase steam. Above the dryout type of CHF the coolant
in the flow channel consists of a mixture of droplets and steam when the annular liquid
film has evaporated. After the DNB type of CHF the hot surface temperature prevents
the turbulent mixture of coolant and steam wetting the wall. During quasi-stationary
conditions in the core after core uncovery only steam exists above the swell level. All
these modes are considered as post-CHF HT.

<!-- page 296 (PDF 52) -->
Transition boiling is a special HT mode because the heat flux generally declines
with an increase in surface temperature. The HT area is bounded by the CHF and minimum
heat flux. Transition boiling can be understood as a combination of unstable
film boiling with low HT capability and nucleate boiling with high HT capability
alternating on the heated surface. In high quality region most of the transition boiling
is due to convection to the droplets impinging on the superheated steam layer in the
vicinity of the wall. The increase of mass flux increases the transition boiling rate and
liquid subcooling has a similar effect.
During film boiling, the heated surface is cooled by radiation, by FCO to vapor, and
by interaction of the liquid and the heated surface. The vapor may become highly
superheated and its temperature is controlled by HT from the wall and to the liquid
phase in the chain wall-vapor-liquid. Liquid in the form of a dispersed spray of droplets
is encountered at void fractions in excess of 80% (liquid deficient flow regime)
and in the form of a continuous liquid core (inverted annular film boiling) usually
encountered at void fractions below 30% (inverted annular flow regime). The transition
regime between these two flow regimes takes place usually in the form of a churn
turbulent liquid dispersed flow.
Of the film boiling regimes the liquid dispersed regime with droplets (after
dryout, above liquid swell level) is most commonly encountered and has been well
studied. In a phenomenological model it is assumed that HT takes place in two steps:
from the heated surface to vapor and from the vapor to the droplets. The axial gradients
of the droplet size are evaluated from the heat balance data and the droplet
size is used for the interfacial drag and HT correlations. The wall temperature is
found from the vapor temperature using a superheated steam HT correlation. In
the model a direct droplet-wall interaction can be modeled, as well. The droplet dispersed
HT regime exists during the emergency core cooling above the swell level as
a consequence of droplet entrainment. In BWR HT, the cooling effect of spray droplets
is essential.
Phenomenological models have also been developed for the inverted annular flow
regime. In the basic formulation, the balance equations are written for the vapor film
between the surface and liquid core. The wall-steam friction is calculated for the laminar
or turbulent steam layer and for an average HT coefficient the length is integrated
from the beginning of the film to the start of unstable wave formation in the
liquid-steam interface.
Phenomenological correlations are also developed to predict the degree of thermal
nonequilibrium. The degree of the nonequilibrium is expressed by actual and equivalent
equilibrium qualities.
For steady-state operation, the prediction of the post-CHF HT is not essential,
because the existence of CHF is itself interpreted as a cause of the fuel damage.
For BWR some attempts have been made to allow for local CHF and to demonstrate
safety by using post-CHF HT models. After some fuel rod damage, as a consequence
of CHF in the BWR bundle, the avoidance of CHF has been retained as an acceptance
criterion. In transient analysis the evaluation of the post-CHF HT is needed but also in
this case the existence of CHF in the hot channel/hot rod is interpreted as a cause of the
rod damage.

<!-- page 297 (PDF 53) -->
In accidents with loss of reactor coolant inventory the HT in the post-CHF mode
controls the maximum temperature of the fuel. If the temperature exceeds 800°C, the
heat production by cladding oxidation becomes a significant contributor to the further
core heat up rate. During a quasi-stationary core uncovery the HT capability of steam
depends on the boiling rate below the swell level and in this case the maximum core
temperatures depends on simple energy balance rules.
During the emergency core cooling after a LBLOCA the cooling by the
droplet-steam mixture is essential both for bottom reflooding and UP spray injection.
Quite soon after the reflooding water enters the core, the temperature increase in the
upper part may be stopped due to the steam cooling caused by the droplets. Also, as
soon as spray droplets impinge on the hottest parts of the core, the cladding
temperature starts decreasing. Thus the post-CHF HT is the main contributor to
limiting maximum cladding temperatures in the core and preventing damage by
oxidation.

#### 6.3.12.5 Radiation HT

Thermal radiation will transfer energy both from surface to surface and from surface
to the two-phase flow. Exchange of thermal radiation with the two-phase flow will
mainly consist of absorption in the two-phase flow, mainly in the droplets. Due to
the relatively low temperature the emission of the two-phase mixture is negligible.
The radiation HT becomes important in addition to other HT modes when the structure
temperature locally exceeds the saturation temperature by 200 K. These kind of high
temperatures are possible only in the core with pure steam, with droplet-steam mixture
or with inverted annular flow regime. Typically the net radiative heat flux streams
from the highest temperature regions into colder parts, being partially absorbed in
the fluid.
The radiation flux from the solid surface consists of two contributions: a radiated
flux which is a function of the surface temperature to the fourth power, and a partial
reflection of the incoming radiation.
Steam and liquid emit radiation in principle, but the emission is small compared
to that of surfaces. Both liquid and steam absorb radiation. In practice the absorption
by steam is negligible. The density of liquid water is large enough to absorb all
radiation in the space between fuel rods, for instance if an inverted annular flow
regime with a continuous liquid core fills the flow channel. For droplet dispersed
mixture only a part of the radiation is absorbed and the rest streams to the next
surface.
Before emergency cooling water enters the core during an LOCA during which the
core has become uncovered, the radiation HT between structures is the most significant
HT balancing the local temperature differences. The net heat flux is directed
from the hottest rods to the cooler ones. In the BWR bundle the channel wall finally
absorbs the heat streaming from the central parts of the fuel element. This heat flux
chain between different rod and channel wall creates inside a fuel bundle a temperature
profile, where the central rods are in a higher temperature than the peripheral

<!-- page 298 (PDF 54) -->
ones. Due to its strong dependence on the fuel temperature the radiation may effectively
prevent the temperature rise and prevent cladding oxidation.

#### 6.3.12.6 Condensation in SG tubes and on structures

The condensation of steam on structures whose surfaces are below saturation temperature
can be an efficient means of removing heat from a coolant system. On vertical
and inclined surfaces the condensation of steam produces a thin film of liquid which is
continuously removed by gravity. The rate of HT is dependent on the subcooling of the
surface, and the thickness that the liquid film attains—HT is limited by conduction
through the film. The HT coefficient is also affected by the steam flow rate to some
degree, through its influence on the film thickness and state. The presence of small
amounts of noncondensable gas in the vapor can result in a drastic reduction in condensation
rates under stagnant conditions. This is because the flow of steam toward the
condensing surface produces an increase in the concentration of the noncondensable
gas at the interface, and the presence of the noncondensable lowers the saturation temperature
of the steam.
In parallel channels, condensation can give rise to instabilities with different
tubes going through a refilling and siphoning cycle at different times (D’Auria
et al., 1990).
Condensation within SG tubes is an important mechanism for the removal of
decay heat. Provided that the secondary side of the SG is cooled the primary pressure
will closely follow the saturation pressure of the secondary side when the SG tubes
contain steam. This enables reflux cooling to remove decay heat satisfactorily following
an LOCA, and permits primary depressurization via secondary side cooldown
when the primary circuit is voided above the core. Because of the large
area available within the SG tubes, however, the exact magnitude of the condensation
HT coefficient is not critical at decay heat levels. Only when the secondary side
coolant level was very low or substantial quantities of noncondensable gas were
blocking the SG tubes would the condensation rate be expected to limit the
overall HT.
Condensation on external structures such as pipe walls or within the PRZ steam
space can occur in transients where the pressure rises, with the effect of reducing
the rate of pressure rise.

### 6.3.13 QF propagation/rewet

The reflooding and quenching phenomena are important for LWRs. Indeed, it is
usually postulated that the core is uncovered and overheats due to decay heat from
the fission products and the energy stored prior to LOCA during the so-called blowdown
phase of the LOCA. In PWRs, the core is recovered, that is, the overheated
rods are quenched and adequate HT is reestablished, by reflooding from below.
ECC injection at the top of the core, or combined top and bottom injection are, however
, also practiced in certain types of PWRs. In BWRs, the hot fuel rods may be

<!-- page 299 (PDF 55) -->
quenched by a spray that forms a liquid film flowing down and cooling the rods as
well as the walls of the “channels” containing the rod bundles and also the water
rods in the rod bundles.
Water is forced into the core by the ECCS via bottom flooding (PWRs) or top spray
(BWRs) in order to stop overheating of the fuel rods and reestablish cooling. Otherwise
, cladding oxidation, zircaloy-water chemical reaction or clad melting and the
consequent release of radioactive products can occur.
Reflooding refers to a particular mode of postburnout cooling of a hot channel by
refilling it with coolant. Quenching or rewetting of the hot surface occurs during
reflooding. Quenching refers to the transition from a mode of HT characterized by
total or almost total absence of liquid contacts with the wall to one where the wall
is essentially wetted by the liquid. The HT coefficient increases dramatically following
quenching.
As a result of the high temperatures attained by the clad before the emergency coolant
arrives, water does not initially wet the hot clad surface. Rewetting or quenching of
hot surfaces occurs when the coolant reestablishes contact with the dry surface. The
surface temperature corresponding to the achievement of liquid-solid contact is the
rewetting or quenching temperature. The temperature of the fuel pellets and fuel clad
is reduced by heat conduction and convection to the coolant. As the coolant rises in a
hot channel or in the overheated nuclear fuel rod bundle, complex HT and two-phase
flow phenomena take place and also the succession of regimes moves gradually up the
rod bundle channels. The hot surfaces along the channels experiences in turn free- or
forced-convection cooling by steam, dispersed-flow film boiling, inverted-annular
film boiling, transition boiling, nucleate boiling, and finally single-phase convection
to the liquid. Almost, all the HT modes listed under HT (Section 6.3.12) are encountered
during reflooding and quenching phase.
During reflood multidimensional flow patterns occur in the core and UP due to:
Flow rates and flow regimes are such that gravitational forces are of the same order
as inertial forces; nonuniformities in core power distribution and differences in resistance
to flow through the intact and broken hot legs tend to promote multidimensional
effects; as the flow passes through the UP it must flow around several structural elements
and additionally the flow behavior of a collected pool in the UP may be highly
three-dimensional.
Another important PH, observed in the PWR integral system LBLOCA experiments
, was core wide cooling of the fuel cladding and quench during the blowdown
phase. This PH is important regarding heat up of the core, because it removes a large
part of the stored energy from the fuel during the early phases of the transient. The
blowdown-phase quench was caused by the hydraulic response of the primary system
during the transition from subcooled to saturated choked flow at the break and by the
operational characteristics of the primary system coolant pumps. The rapid cooling of
the cladding is primarily a result of low-quality, high upward core flow at 7 MPa pressure
range. The correlations currently used in the advanced codes cannot handle adequately
such blowdown quench phenomena and also no directly applicable separate
effects type experimental database exists.

<!-- page 300 (PDF 56) -->
QF propagation/rewet on fuel rods and, also channel walls and water rods (BWR)
will be presented below, in some detail.

#### 6.3.13.1 QF propagation/rewet on fuel rods

QF progression has been an interesting physical PH studied intensively over the last
four decades. After a LBLOCA has occurred the core is empty and adiabatic heat
up is possible. Emergency coolant injection by bottom reflooding creates a rising
quenching front, and upper head injection or core spray injection a falling film,
sputtering front. Many experiments in 1970s and 1980s were done for understanding
and visualization of the reflooding front movement. Visual demonstrations with
an overheated, red-colored rod enclosed in a glass tube demonstrated clearly that
quenching to the saturated temperature takes place in a distance of a few
millimeters.
In the boiling curve, QF propagation means a movement from the film boiling HT
mode through transition boiling to the nucleate boiling regime. In a quenching front
the axial temperature gradient of the cladding may be so large that a significant part of
the heat in the unwetted part is removed by the axial conduction in the cladding. For a
fast front movement this gradient may be quite different between the inner and outer
cladding surfaces. But other mechanisms may also support conduction-controlled
quenching or be a main contributor to the cooldown close to the saturation temperature
. These are transition boiling caused by the collapse of the liquid-vapor interface in
the inverted annular film boiling regime and droplet impingement through the steam
layer in the transverse direction toward the wall.
During the LBLOCA the first cladding heat up is caused by the stagnation of flow
going through the core. Soon after this large mass flow rates may exist in the core first
in the negative flow direction and later in the positive direction. This high mass flux
rate may be enough for cooling the cladding along the whole core length without a
specific quenching front (Aksan et al., 1989).
The conduction controlled quenching mechanisms for a rising reflooding front and
a falling film front are quite similar. In the wetted region the heat is transferred, in both
cases, by nucleate boiling and later by convection. In the unwetted part, the heat is
removed by convection to vapor or to droplet-vapor mixture or by inverted annular
flow film boiling during bottom reflooding. Precursory cooling effects support the
QF movement.
The rewetting characteristics of the overheated core after the large LOCA was one
of the most interesting research topics in 1970s and 1980s, and still has a significant
influence on acceptance criteria in licensing and probabilistic safety assessment safety
analyses. The main interest is related to the maximum temperature in the core, but this
turn-over temperature is determined by the liquid dispersed flow well before
quenching. Depending on the amount of water available the cooldown takes place earlier
or later.
The large temperature gradient in the cladding gives rise to a mechanical stress on
the cladding, and it may affect fuel damage and radioactivity leakages. The rapid

<!-- page 301 (PDF 57) -->
temperature drop is also associated with strong steam generation and this may have an
effect on system characteristics including:
–
liquid entrainment rate,
–
CCFL in the UTP,
–
steam binding in the SG,
–
multidimensional flow distribution in the core.

#### 6.3.13.2 QF propagation/rewet on channel walls and water rods (BWR)

Following hypothetical complete emptying of the core in BWR-type reactors (e.g., as
a consequence of a LBLOCA in one circulation line), both rod cladding and fuel box
surfaces attain temperatures well above the saturation temperature of the fluid.
(Usually the system pressure is around a few tenths of an MPa in these conditions.)
At a given time, the reflood process starts, caused usually both by the injection of
cold liquid through the LPCI (low pressure coolant injection) and the LPCS. The former
system injects water into the downcomer or inside the core bypass region; in both
cases the liquid reaches the LP and enters the core from the bottom. In the latter system
, the liquid is sprayed at the top of the core and creates a QF traveling from top to
bottom.
Phenomena like CCFL, entrainment, PDs, etc., are very important for predicting
the transient evolution in these conditions.
The reflood PH inside each fuel bundle follows the same mechanisms described in
Section 6.3.13.1. The fuel box walls play a special role that can be outlined as follows:
(a) Due to the fact that there is essentially no power production and initial temperatures before
reflood are slightly lower than cladding temperatures, reflood occurs earlier along the fuel
box walls than adjacent to the fuel rods (the thickness of fuel boxes, which is far greater than
the rod cladding thickness, does not appear to have a significant role in relation to the different
rewet times between the rods and the fuel box walls).
(b) Because they cool earlier, the walls constitute a heat sink for the rods and make easier the
reflood in the rods themselves; radiation HT plays a role in this regard.
(c) As an additional consequence of the first item, the liquid injected by the LPCI or sprayed by
the LPCS can penetrate to the LP preferentially along the fuel box walls and contribute to
reflooding of the core rods.
The local mechanism of reflood, including the two-dimensional nature of the PH, is
the same as described in Section 6.3.13.1.
The rewetting of fuel box walls gives an important contribution to core reflood. In
this sense the present PH is as relevant as the reflood in the core rods. The same considerations
as in the previous paragraph apply in this case.

### 6.3.14 LP flashing

When a pool containing saturated of subcooled liquid is subjected to depressurization,
the system pressure acting on the liquid itself may reach the saturation pressure
corresponding to the initial liquid temperature. In this case a more or less violent

<!-- page 302 (PDF 58) -->
vaporization (flashing) may occur depending upon the depressurization rate. (High
purity water bounded by a surface with negligible nucleation sites—a very flat
surface—may behave in a different way; in particular, several tens of degrees of liquid
superheating can be expected. This is not of interest in practical reactor situations.)
During flashing (nearly) homogeneous nucleation occurs in the bulk of the liquid,
and the gas bubbles produced may entrain a large mass of liquid toward the upper parts
of the pool (LP in this specific case).
The PH is significantly affected by the geometry of the system, shallow pools giving
rise to more violent flashing than tall ones containing the same volume of liquid.
The liquid entrained in the steam flowing toward the upper part of the vessel both in
BWR and PWR systems, in most of the situations of practical interest, may give a
significant contribution to core cooling. In the case of LBLOCA, the PH may contribute
to early core quench observed in the experiments performed in integral test facilities
. The LP vaporization occurring late in the transient in the case of a large break
may lead to the occurrence of flooding, thus preventing or limiting the flow of injected
liquid into the downcomer. The last PH is more relevant for PWR systems. In the case
of BWR, rapid boiling in the LP may prevent the fall back of liquid from the core
making rod cooling more efficient.

### 6.3.15 Guide tube flashing (BWR)

As indicated in the heading, the PH is typical of a BWR. From a phenomenological
point of view, the substance of Section 6.3.14 is also applicable here. The particular
geometry and the presence of relatively small holes (orifices) at the top of the
guide tubes govern the development of the PH and make it distinct from LP
flashing.
The liquid initially contained in the CRGTs is slightly more subcooled than
the remaining LP liquid. For this reason, flashing during a given transient is delayed
with respect to LP flashing. Level swell is also limited by the abovementioned
orifices.
In view of the above this PH could be considered less important than the previous
one as far as nuclear reactor safety is concerned. Nevertheless, it may affect the core
thermal-hydraulic behavior later in a transient (with respect to LP flooding).

### 6.3.16 One- and two-phase impeller-pump behavior

In single-phase conditions the dimensionless pump characteristics are almost independent
of the fluid (liquid, gas, steam). The small variations are mainly due to viscous
properties connected to recirculation losses, shock losses on the impeller, and fluid
friction (Comolet, 1976).
In two-phase flow the torque and head characteristics are affected by so-called degradation
which is a function of void fraction, pressure, and flow rate. The main causes
of the degradation seem related to phase separation in the impeller due to centrifugal
forces, with liquid phase acceleration and relative deceleration of the gas or steam.
The pre- and postrotations of fluid in the inlet and outlet pipes play a part in this issue.

<!-- page 303 (PDF 59) -->
All these phenomena depend on the type (centrifugal, axial, mixed flow) and geometry
of the pump.
For all LOCAs with running pumps, the pump performance is important. For large
LOCAs the behavior of the intact loop pumps plays a role in determining the position
of the stagnation points in the primary circuit.
For SBLOCAs the pump behavior plays a role in steam-water mixing and core
cooling.

### 6.3.17 One- and two-phase jet-pump behavior

In normal operating conditions the jet pump operates as a single-phase ejector and is
installed in the lower part of the downcomer (BWR-3, 4, 5, and 6). The driving flow
provided by the external recirculation pumps is injected in the upper part of the ejector
(converging section) and creates depressurization in the throat. The downcomer fluid
is accelerated by the pressure difference created and mixes with the driving flow in the
diverging part of the jet pump.
When recirculation pumps stop, as in most transients, the jet pumps behave exactly
as ventures connecting the LP with the downcomer. In the case of main coolant pump
cavitation, steam may flow out of the top nozzles completely preventing the correct
operation of the device.
The component has a critical relevance in terms of nuclear reactor safety in the case
of LOCA involving the break of a recirculation line. Owing to its axial elevation, the
jet pump prevents mass depletion from the core region; so its mechanical integrity is of
vital importance.
In the case of off-normal conditions, the jet pump simply introduces an extra PD in
the flow path from LP to downcomer and vice versa. Consequently, no new phenomena
are expected in this case.
An exception may be the jet pump behavior during pump coast down. Possible
unstable behavior may cause neutron flux instabilities or interact with the neutron
flux. This last aspect may have some safety relevance.

### 6.3.18 Separator behavior

Separators are installed in the vessel of a BWR and in the secondary side of SGs
equipped with U-tubes (PWR). The basic function is to separate the steam from
the two-phase mixture coming either from the core (BWR) or from U-tubes riser
(PWR), allowing (near) pure steam to flow to the turbine.
In all cases, the separation process is based on the larger inertia of the liquid phase
with respect to the steam phase: the upward flowing two-phase mixture is constrained
to rotate. In this way, the steam can continue to flow upward while the liquid droplets
impinge on the walls and are drained downward to the downcomer (of the main vessel
or of the SG in BWR and PWR cases).
The separation efficiency largely depends upon the average velocity of the incoming
mixture. At very low velocity the separator essentially behaves as a simple flow
obstruction.

<!-- page 304 (PDF 60) -->
The component behavior has no direct relevance in terms of nuclear reactor
safety for PWRs and in most cases for BWRs. An exception, in the case of BWR,
is that the PDs introduced in the riser zone can facilitate the occurrence of core
thermohydraulic-neutronic instabilities.

### 6.3.19 Steam dryer behavior

The steam dryer allows the achievement of a vessel exit quality of near to one (0.999).
The working principle is similar to the one adopted for the separator and exploits the
different inertia of the light (steam) and heavy (liquid) phases. The two-phase mixture
exiting from the separator (quality range between 0.98 and 0.99) flows horizontally in
parallel flow paths created between adjacent undulated plates. The steam phase flows
across, while the liquid droplets unavoidably impinge against the wall and are drained
to the bottom of the dryer and toward the downcomer.
Considerations already detailed in Section 6.3.18 are also valid in this case. As in
the case of the separator, the component behavior has no direct relevance in terms of
nuclear reactor safety in PWR. The dryer does, however, contribute to the PD introduced
in the riser zone of a BWR and therefore can facilitate the occurrence of core
thermohydraulic-neutronic instabilities.

### 6.3.20 Accumulator behavior

When, in an LOCA, the primary pressure in a PWR falls below the set point for accumulator
injection, the driving gas within the accumulator can expand, delivering
borated water (boratec) coolant to the primary circuit. The rate of delivery of the flow
depends on the resistance of the accumulator line (important in LBLOCA) and on the
expansion characteristic of the driver gas (dominant effect for SBLOCA). The latter
depends on the HT processes occurring between the gas and the accumulator structure
and the liquid interface. The rate of accumulator delivery may also be influenced by
feedback between the accumulator flow and the system pressure. Condensation on the
injected liquid can lower the circuit pressure, increasing the flow and lowering the
pressure further. On the other hand, accumulator injection can cause an increase in
primary pressure (e.g., by reflooding the core and increasing heat input to the fluid),
reducing the flow rate. The combination of local and system effects can possibly give
rise to instabilities in the accumulator flow rate.
When the liquid within the accumulator is exhausted the cover gas can flow into the
primary circuit. The presence of a noncondensable gas in the primary can then modify
the coolant distribution and the HT processes, particularly condensation. The emptying
of the accumulator could be modified by the formation of a vortex at the
outlet pipe.
Under the near adiabatic conditions occurring in the LBLOCA the cover gas temperature
can fall to subzero (°C) temperatures, leading to the possibility of frost forming
in the accumulator lines.
The accumulators form a key element of the safety injection systems for dealing
with LOCA. In a LBLOCA, they provide the principal means of limiting the peak clad

<!-- page 305 (PDF 61) -->
temperature by refilling the vessel after blowdown and initiating reflood. In SBLOCA
(particularly in beyond DBA scenarios where the HPIS is assumed to fail) the accumulators
also play an important role in preventing or limiting core uncovery. The role
of the accumulators in a range of accident scenarios is discussed in OECD/NEA
(1989).

### 6.3.21 Loop seal filling and clearance

In most current PWR designs, the primary piping from the outlet of the SGs descends
to a level roughly corresponding to half way down the core before rising to enter the
pump inlet from below. During an LOCA when the primary circuit is partially voided,
liquid present in the U bend of this intermediate leg can form a barrier to the flow of
steam around a loop. This liquid plug is said to form a loop seal. A pressure difference
across the loop seal which is greater than the hydrostatic pressure arising from the
height of the pump inlet side of the intermediate leg is necessary before steam can
displace the loop seal.
The manner and extent of the displacement of the liquid from the loop seals depends
on the steam supply characteristics. At reduced steam velocities and low liquid subcoolings
the expulsion of fluid will be incomplete. This aspect of loop seal behavior
is closely connected with the PH of countercurrent flooding limitation (CCFL). However
, the pipe sizes of interest are very much larger than those studied in most SETs.
When the loop seals clear, their liquid contents are displaced into the reactor vessel,
producing a rapid refill. The number of loop seals clearing, which depends for instance
on the size of the break, affects the total amount of water added. How many loops need
to clear is determined by the balance between the frictional PD around the cleared loops
and the hydrostatic pressure difference corresponding to the depth of the loop seal.
It is possible for loop seals to reform, after they have cleared. Back flow of ECCS
from the cold legs through the pump is limited by the height of the impeller and the
diffuser geometry, but can occur if there is a general flow reversal, or if the level in the
cold leg is high enough. Condensate from the down side of the SG tubes also can provide
a contribution to the reforming of the loop seals.
The loop seals have a particularly significant effect on the behavior of a plant in a
small cold-leg break LOCA. Until at least one of the loop seals has cleared steam produced
in the core cannot reach the break, and the pressure in the primary system
remains high, at a level determined by the secondary side pressure. Furthermore,
as the liquid content of the primary side falls, the hydrostatic head of the liquid trapped
in the pump inlet causes the liquid level in the core region to be depressed by an
amount equal to the depth of the loop seal. This can lead to uncovering of the core.
Loop seal reformation could impair long-term cooling after a LBLOCA by causing
periodic depression of the mixture level in the core.

### 6.3.22 ECC bypass/downcomer penetration

The ECC bypass and downcomer penetration PH is a combination of three phenomena
already described (Rohatgi et al., 1990):

<!-- page 306 (PDF 62) -->
l
CCF or CCFL in the downcomer (see Section 6.3.10.5),
l
liquid-vapor mixing with condensation in the downcomer (see Section 6.3.7.2),
l
entrainment/de-entrainment in the downcomer (see Section 6.3.6.3).
These three phenomena contribute to ECC bypass/downcomer penetration. This PH is
listed separately because of its importance to ECC water injection performance. Complete
ECC bypass occurs, if the steam upflow rate is so high that it does not permit any
liquid downflow through the downcomer. All the injected ECC water is carried out
through the broken cold leg by the steam flow. This may be caused by high steam
upflow in the downcomer (as CCFL), increased steam upflow due to pressure decrease
at the condensation location in the cold leg and upper part of the downcomer, as well
as high azimuthal steam velocities from the intact cold legs to the broken cold leg during
LBLOCA blowdown (as entrainment). Downcomer penetration is partial or complete
water downflow of the injected ECC water through the downcomer at lower
steam upflow or lower azimuthal steam flow.
ECC water injected into the cold legs or directly into the downcomer has to flow
downward through the downcomer in order to refill the LP and subsequently reflood
the total core to prevent overheating. This water flow can be limited by upward and/or
azimuthal steam flow. ECC bypass and penetration is ranked to be very important
during LBLOCA refill (OECD/NEA, 1989; Wilson et al., 1990).

### 6.3.23 Parallel channel instabilities

The term “parallel channel instabilities” includes a broad range of instabilities that
may occur in a system owing to the presence of a boiling boundary. Any boiling channel
, even if operated in an open loop mode, may give rise to instabilities that can be
detected as pressure, flow rate, temperature, void fraction, etc., oscillations (OECD/
NEA/CSNI, 1990).
There are several reasons for instabilities including static (e.g., Ledinegg) or
dynamic (e.g., density wave) ones. The most studied instability mode is just called
a density-wave instability: a perturbation in a boiling channel inlet flow rate may
result in a perturbation of the PDs across the channel; this may reflect back to the channel
inlet, strengthening the initial flow rate variation (unstable system) or smoothing it
(stable channel). A special case of “stable oscillations” may also occur.
The cases of interest essentially include a closed loop where the boiling channel is
one of the parts of the system, and a single channel that constitutes the entire system,
bounded by upper and LP with imposed conditions is the other; multiple parallel boiling
channels are of considerable interest in the BWR technology. The core of a BWR
can be considered as a unique channel: in this case parallel channels are constituted by
the bypass and the downcomer. A single core channel can also be considered for instability
purposes: in this case the other channels are the parallel channels that may interact
to some extent with the other external channels (bypass and core).
This very short survey gives an idea of the number of thermal-hydraulic unstable
situations that may occur in a BWR. The complexity increases, if one considers the
neutron flux which may oscillate and interact with thermal-hydraulic instabilities
(neutronic-thermal-hydraulic feedback).

<!-- page 307 (PDF 63) -->
So far, two general kinds of instabilities measured in BWR plants have attracted the
attention of technologists:
(a) core wide oscillations: the neutron flux oscillates with same frequency and amplitude in all
parts of the core;
(b) regional oscillations: at least two parts of the core oscillate with different frequencies.
It seems easy to imagine that a very limited number of channels or even a single channel
can oscillate at its own characteristic frequency and amplitude in a core that may
remain stable.
The PH is relevant in nuclear reactor safety. With reference to the BWR flow map
(power versus core flow rate) a zone has been found, from operational experience,
where the occurrence of instabilities is very probable. This is characterized by power
and core flow rate around 40% and 30% of the nominal value, respectively. Operation
in this zone may be necessary following a pump trip or during plant start-up transients.

### 6.3.24 Boron mixing and transport

Boron is a highly neutron absorbing material and will consequently strongly affect the
core power when inserted or removed from the core. Thus boron mixing and transport
will not directly influence the thermal-hydraulics (if one neglects possibly minor
chemical effects) but will do so indirectly through the core power which is a
thermal-hydraulic
boundary
condition.
In
PWRs,
boron
is
added
to
the
coolant-moderator and its concentration will control the long-term variation of core
reactivity. Because of the high liquid velocity in the RCS, the added boron will be
mixed quite homogeneously with the coolant without steep gradients, and its transport
through the RCS will closely follow the liquid transport.
However, there are low flow conditions, for example, at idle reactor coolant pumps,
when the pump power has temporarily been lost, when inhomogeneous boron concentration
can be attained in the loops with rather steep concentration gradients. In this
case, the diffusion of boron within the liquid can be quite substantial and thus the
boron transport will be different from the liquid flow.
The boron concentration will influence the PWR core power through reactivity
feedback effects. The boron content impacts the moderator temperature reactivity
coefficient and the boron concentration reactivity coefficient. For a fresh normal
PWR core in equilibrium conditions (beginning of life) high boron concentration
(1600–2000 ppm) will cause the former to be slightly positive at low moderator temperatures
(300–400 K) and less positive at higher temperatures. At lower concentrations
it is always negative and more negative at higher temperatures. The boron
concentration coefficient is always negative being more negative at low concentrations
and temperatures.
Boron mixing and transport within the RCS is of crucial importance for core power
control in LWRs. The mixing and transport of boron influences through reactivity
feedback the local core power during normal and off-normal operation of PWRs
and during off-normal operation of BWRs.

<!-- page 308 (PDF 64) -->
During normal operation of a PWR the initial excess reactivity of a fresh core is
compensated by adding boron to the coolant. This added boron is gradually decreased
as the fuel burnup increases in order to keep the core reactivity essentially constant
throughout the core lifetime.
It is also a well-known fact that a PWR cannot be kept in a subcritical cold SHD
condition immediately after refueling without the boron concentration in the coolant
being above some value despite all the control rods being inserted. Thus the boron
concentration and its mixing and transportation with the coolant is also of major concern
at SHD conditions.
During a LBLOCA, the core fission power will almost immediately be terminated
because of global core voiding and associated loss of moderation. However,
during the reflood period it is essential that the injected relatively cold ECCS water
has some level of boration in order to avoid possible local recriticalities of
the core.
During a SBLOCA in a PWR with U-tube SGs it has been found that in the reflux
condensation phase there exists a mechanism which can accumulate boron-free condensate
in the loop seal (Hyvarinen, 1992). Analyses of externally caused boron dilution

transients
suggest
that
the
SBLOCA
in
this
case
could
become
a
reactivity-initiated accident (RIA) initiator.
It has also been found that in some specific cases during SHD conditions in a PWR,
there could be situations where pronounced heterogeneities in the boron concentration
can develop and thus can potentially cause a RIA (Jacobson, 1992).

### 6.3.25 Noncondensable gas effect (PWR)

The presence of a noncondensable gas in the primary circuit plays a role in mechanical
and thermal fluid behavior. Noncondensables are mainly nitrogen from the accumulator
injection or hydrogen from clad oxidation.
In the case of nitrogen injection, the mechanical effects are related to gas expansion
in the cold leg and the upper part of the downcomer. The momentum-transfer between
the gas, steam, and liquid increases the liquid velocity. This has an impact on the
downcomer water penetration and on water bypass to the break.
The thermal effect is related to the change in HT laws, particularly for the condensation
process produced by noncondensables.
Both effects are associated with the end of accumulator injection. When nitrogen
enters the cold leg, the mixing of gas with liquid stops oscillation due to plug formation
. This is due to the compressibility of gas liquid mixture and to the reduction in
condensation rate.
Within the primary circuit the gas migrates from its injection or generation point.
There are several mechanisms for migration: the entrainment of gas by flowing steam,
the gravity forces arising from density differences and diffusion driven by the concentrationgradient
. Inthe SG,due to condensationinthe tubeinlet regionand the flow ofsteam
toward the SG, noncondensable gas stays at the top of the U-tubes and can limit NC.
This PH could have some influence on the general thermal-hydraulics behavior for
LBLOCA but is of most relevance to accidents with NC phases.
