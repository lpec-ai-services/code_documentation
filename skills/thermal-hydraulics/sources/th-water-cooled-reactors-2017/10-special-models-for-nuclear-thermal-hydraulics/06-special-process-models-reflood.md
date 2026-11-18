# Special process models — Reflood
<!-- source PDF pages 16-18 -->

<!-- page 610 (PDF 16) -->
J*
g = Jg=
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
σgΔρρ=ρ2
g
1=4
r
Nμg = μg= ρgσ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
σ= gΔP
ð
Þ
p
1=2
Important regions of de-entrainment are steam separator and dryer in BWR and separator
in steam generator secondary side. In both cases, the vapor-liquid mixture is
sent through curved channels to create centrifugal forces that separate the liquid from
the steam. Most codes use empirical value of carry over and carry under fractions and
from that, the amount of liquid separated from the two-phase mixture is estimated.
TRACE also has a mechanistic model based on joint development undertaken by
Electrical Power Research Institute (EPRI), United Stated Nuclear Regulatory Commission
(USNRC), and General Electric. It is available in TRACE code and it consists
of conservation of water mass, vapor mass, axial momentum, and angular momentum,
entering and leaving the separating barrel. The model assumes a form of void distribution
and vortex flow. The model does have four parameters that are determined
from the tests.
The scaling issues are the effect of pipe size on entrainment in annular flow, empirical
carry over, and carry under fractions for separators that are empirically obtained.
For developing correlation or for model validation, full-size separate effects tests
are needed.

## 10.2.4 Reflood

Safety of nuclear fuel in light water reactor (LWR) is ensured by keeping fuel covered
with the coolant. In case of LOCAs the reactor loses inventory and may lead to degradation
of cooling due to the uncovered fuel. The uncovered fuel will heat up due to
decay heat. Reactors have safety injection systems such as emergency core coolant,
high pressure injection, and low pressure injection to fill the vessel after the system has
sufficiently depressurized to allow for such injections. Majority of the PWRs have
injection in cold legs, but few designs have injection in downcomer and in hot legs.
The coolant flows down in the downcomer and to lower plenum, and then to core. In
the case of additional injection in the hot leg, the coolant condenses vapor in upper
plenum and eventually some of this coolant flows down in the lower plenum. This
hot leg injection creates an internal recirculating flow of cold coolant flowing down
and two-phase mixture flowing through other part of the core (central part) and it prevents
steam binding by condensing vapor in upper plenum and prevents it going to
steam generator. Effects of radial power distribution and of combined coolant injection
have been reported in a study from Japan (Iguchi, 1998).
These transients have generally three periods—blowdown, refill, and reflood.
Blowdown period lasts about 30 s, refill period about 10 s, and reflood period lasts
about 250 s. The blowdown period ends when ECC injection begins and the refill
period ends when lower plenum is full. During the reflood phase the coolant starts
to fill the core and quench (cool) the fuel.

<!-- page 611 (PDF 17) -->
The physics of quenching the core is complex. If the temperature of the clad is
above the minimum stable film boiling temperature (Tmin), the cooling will be through
film boiling. However due to axial conduction and precursor cooling, the temperature
of the clad can be reduced sufficiently (below Tmin) to allow for transition and subcooled
boiling. The region above subcooled boiling is still film boiling with inverted
annular flow regime and dispersed droplet regime created from the breakup of the core
of the inverted annular regime. The quench front or transition to subcooled boiling
region moves up the core as the steam and droplet cool the core ahead of the front
along with axial conduction. USNRC studies have identified the phenomena and their
impact on heat transfer from the clad (Hochreiter et al., 2010; Odar, 2001).
There are two different regimes during the reflood period, based on inlet subcooling
and coolant velocity, as shown in Fig. 10.7. In the case of saturated or low
subcooling or low velocity core inlet flow, the vapor generation rate is high and flow
regime changes from saturated boiling to dispersed boiling heat transfer. For high subcooling
or higher velocity flows at the core inlet, the quenching occurs sooner and
there is generally an inverse annular flow regime above the quench front. As the vapor
generation increases the central liquid region breaks up, leading to dispersed film boiling
regime. The droplets, in the dispersed phase, cool the vapor by evaporation and
also remove clad heat if they impinge on the clad.
The Hochreiter’s study in support of new Rod Bundle Heat transfer Facility identified
the important processes needed to be investigated in the tests for accurately
modeling reflood period. It identified important processes related to local void fraction
that governs interfacial heat transfer, interfacial area, fuel/clad material, transition
Fig. 10.7 Qualitative reflood flow regimes at different subcooling (high on the right side) and
flow velocity (low on the left side).

<!-- page 612 (PDF 18) -->
boiling heat transfer, inlet fluid temperature and velocity, liquid entrainment, droplet
size, droplet impingement heat transfer, dispersed phase heat transfer, etc. Minimum
stable film boiling temperature is also important to indicate the onset of quenching.
Grid effect was not rated high but the test results showed that grid spacer improves
the heat transfer due to break up of boundary layer and break up of drops.
There have been many tests to study this phenomenon. Most tests are with electrically
heated fuel rod simulators without gas gap. A study (Ihle and Rust, 1987a,b) was
conducted to study the effect of the gap. It concluded that fuel rod simulator without
gap showed delayed quenching and higher temperatures. This is expected as the clad
energy balance with gap has more resistance to heat transfer from the fuel rod leading
to early quench.
The model for reflood phase in the computer codes consists of correlations for Tmin,
film boiling heat transfer, dispersed phase heat transfer, nucleate boiling, transition
boiling, and conduction in the fuel rods including gap and clad. All these phenomena
are based on local conditions and are not subject to any scaling issue. TRACE code has
implemented Stewart and Groeneveld correlation (Stewart and Groeneveld, 1981) for
Tmin as described below. The correlation was validated with independent data. There
are no terms with geometric dimensions or material properties.
Tmin,sat = 557:85 + 44:1*P□3:72 *P2
Tmin = Tmin,sat + hl,sat □hl
ð
Þ
hfg
2:82 + 1:22P
ð
Þ
The convective heat transfer in the inverted annular region is based on estimating the
size of the vapor film on the wall and enhancement due to vapor-liquid interface disturbances
. The correlation was further enhanced to match rod bundle data. There is
also a correction for natural convection in the vapor film. It should be recognized that
the film thickness determines the natural convection fluid dynamics in the vapor
region, and this thickness is directly proportional to the tube hydraulic diameter.
TRACE also has a correction of 30% increase for heat transfer coefficient based on
tube data for application to rod bundles. The transition from inverted annular flow to
dispersed phase is assumed to be void fraction of around 0.6. The heat transfer in dispersed
phase is modeled with correlation by Forslund and Rohsenow (1968). A set of
saturated and subcooled film boiling correlations were provided by Sudo (2012). The
description of TRACE models (or any other system code) shows the need for
well-instrumented tests with heated rod bundles.
There have been many rod bundle tests to study Reflood phenomena (Hochreiter
et al., 2010). These are listed here.
l
FLECHT Cosine Tests (NRC/Westinghouse)
l
FLECHT Skewed Axial Power Shape Tests (NRC/Westinghouse)
l
FLECHT-SEASET 21 Rod Bundle Tests (NRC/Westinghouse)
l
FLECHT-SEASET 161 Unblocked Bundle Tests (NRC/Westinghouse)
l
FEBA Reflood Tests (Germany)
l
THTF Rod Bundle Tests (NRC/Oak Ridge National Lab)
