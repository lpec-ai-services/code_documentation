# Chapter foreword — Characterization of thermal-hydraulic phenomena for set — Heat transfer
<!-- source PDF pages 49-53 -->

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
