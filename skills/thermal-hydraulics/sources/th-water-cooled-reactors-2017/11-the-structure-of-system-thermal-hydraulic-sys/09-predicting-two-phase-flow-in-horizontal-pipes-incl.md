# Predicting two-phase flow in horizontal pipes including stratification
<!-- source PDF pages 48-59 -->

<!-- page 686 (PDF 48) -->
l
Nucleation delay is difficult to model in a general way for all conditions.
l
2-D or 3-D effects (such as vena contracta) in abrupt area change are not well described in a
1-D model.
l
In the worst cases the uncertainty in predicting flow rate may be about 15 %.
A state-of-the-art report on “Critical flow modelling in nuclear safety” published by
OECD-NEA-CSNI (1982) recommended to develop 1-D modeling to obtain more
accurate predictions than 0-D models. After the efforts spent in the 1980s, the 1-D
models actually obtained some progress but not as expected.
More recently, Bartosiewicz and Seynhaeve (2014) have proposed the delayed
equilibrium model (DEM) implemented in a 1-D three-field model with saturated
steam, saturated liquid, and metastable liquid which performs better in low subcooling
conditions than any other model. A mechanical equilibrium is assumed
between the three fields and a relaxation equation controls the mass fraction of metastable
liquid. The relaxation time constant was somewhat empirically correlated.
However, one may interpret the success of this model by a better capability to treat
transient conduction in a model which keeps the memory of the upstream fluid temperature
. This flashing model was implemented in both a 1-D model and in a 3-D
CFD code (Duponcheel et al., 2015). This opens the way to a better prediction of
geometrical effects.
The accurate prediction of critical flow rate at a break on a reactor circuit in a
nuclear reactor may not be considered as mandatory since safety analysis of reactors
should cover any kind of break sizes. However, the very limited accuracy of critical
flow rate prediction by system codes may be an issue when analyzing IETs by
preventing from precise validation of other code models. Moreover a precise prediction
of choked flow in well-know reactor component geometry (valve, flow limiter,
etc.) may be necessary for a precise analysis of some reactor transients. The continuous
increase of computer power will allow in near future a 2-D or 3-D treatment of a
break flow at a reasonable CPU cost which may be associated with a modern flashing
modeling such as the DEM model and may predict choked flow with a significantly
better accuracy than current models.
11.9
Predicting two-phase flow in horizontal pipes
including stratification

## 11.9.1 Phenomena of interest in HL and CL of a PWR

HLs, CLs, and ILs of PWRs play an important role in accident sequences, particularly
when two-phase steam water flow occurs in the loops (see Fig. 11.16). When the primary
mass inventory is degraded in the case of a loss of coolant accident (LOCA) the
phase coupling or decoupling controls the amount of water which is kept out of the
pressure vessel and influences the occurrence of a core uncovery with fuel clad
temperature excursion. The formation of a liquid slug in IL after the end of natural

<!-- page 687 (PDF 49) -->
circulation and the loop seal clearing may also induce a core uncovery. Many auxiliary
circuits are connected to HL and CL such as SIs, RHR circuit, and the pressurizer
surge line. All these connections may also be considered as potential breaks when analyzing
the safety of the reactor.
The knowledge of the flow regime in horizontal pipes may play an important
role in PWR accident scenarios. For example, during many LOCA transients,
the flow regime in HLs or CLs influences the amount of liquid and steam lost
at a break or entrained in the pressurizer surge line in the case of pressure relief
valve opening. Both the primary mass inventory and the primary pressure are very
sensitive to the steam quality of the break or valve flow. As an example, the quality
of the flow rate at a break or steam relief valve in the pressurizer will strongly
depend on the flow regime at the T junction between HL and surge line as illustrated
in Fig. 11.17.
Fig. 11.16 Examples of flow situations encountered in hot legs and cold legs in accidental
transients of a PWR.

<!-- page 688 (PDF 50) -->
The main phenomenon in hot and CLs is phase stratification, which dramatically
decreases the mechanical coupling between phases. The interfacial friction in stratified
flow is several orders of magnitude lower than in dispersed bubbly flow. Therefore
, the entrainment of liquid water in the loop by steam coming from the core is
minimized in stratified flow. This is a favorable feature since it keeps more water
in the core without affecting the heat release to the SGs which may continue even after
the stop of two-phase natural circulation, by the reflux condensation mode. In the
stratified flow regime in a horizontal pipe, there may be a nonhorizontal free surface
due to interfacial friction and/or due to some interfacial waves propagating at the free
surface. In many SBLOCAs there is a liquid slug formed in the IL after the end of the
two-phase natural circulation. This liquid slug is then removed by the so-called loop
seal clearing process and some quantity of water is kept at the bottom of the IL, which
depends on the interfacial friction at the free surface and on the predicted free surface
slope which determines the minimum cross-section for steam flow and then the maximum
steam velocity. The slope of the free surface is the result of the interfacial friction
and the slope influences the interfacial friction and the possible entrainment of
water by determining the maximum steam velocity.
In the two-phase natural circulation mode, the flow at the entrance of the HL may
be bubbly or stratified-bubbly—with a continuous vapor flow at the top and a bubbly
flow below the free surface—when the swell level in UP decreases to the elevation of
the HL. In most cases velocities are low and the flow regime changes progressively to
pure stratified flow without any more bubbles.
In the case of stratified flow, waves are created at the free surface, which increase
the surface roughness and the interfacial friction. Both fluvial and torrential flows may
occur and a hydraulic jump may be created when there is a transition from torrential to
fluvial regime.
In the case of reflux condenser mode, CCFL may occur in the HL in the zone of the
bend and the SG entrance nozzle. Large amplitude waves reflecting on the bend were
observed in some conditions in the MHYRESA tests (Geffraye et al., 1995). CCFL
may result from liquid entrainment at the crest of large amplitude waves.
The MHYRESA hot-leg entrainment tests (Geffraye and Laroche, 1999; Ratel and
Geffraye, 2000; Geffraye et al., 2000) have also shown that for a given liquid level in
the UP, a hydraulic jump could be created and moved downstream when the gas flow
rate is increased.
Fig. 11.17 Two different flow regimes at the pressurizer T junction or at two different break
orientations.

<!-- page 689 (PDF 51) -->
During the reflooding of a LBLOCA a mist flow enters the HL and some deposition
of droplets occurs. Liquid films are created along HL walls and a continuous
liquid field is collected at the bottom of the pipe. Due to the large vapor
velocity, droplets may be also entrained from the crest of waves. The mist flow
which enters the SG tubes is the result of this deposition and entrainment of droplets
occurring first in the UP and in the HL. Prediction of the resulting droplet
flow rate entering SG tubes is of prime importance for modeling the so-called
steam-binding effect (Valette et al., 2011). The vaporization of droplets in the
hot SG tubes creates addition pressure losses in the loops which decreases the
flooding rate in the core.
In postulated accident sequences where pumps are supposed to operate in
two-phase flow conditions, the phases may be well mixed at the outlet of the pump
and may tend to stratification when flowing to the pressure vessel.
Postulated small and medium size breaks in HL, IL, and CL may be oriented at the
top, on the side or at the bottom of the pipe (see Fig. 11.17). The quality and mass flow
rate at the break depends a lot on the position of the break and on the flow regime. In a
stratified flow there may be a very large difference between a bottom break, which
entrains a large flow rate but a low quality, and a top break, which entrains a high
steam flow rate and a low mass flow rate. Losing a high coolant mass flow rate
may induce a core uncovery with fuel clad temperature excursion. Having a high
steam quality at the break induces a slower loss of primary mass and decreases primary
pressure (Bestion, 1989) so that actuation of SI will occur earlier. Therefore,
core uncovery is less likely to occur and will be shorter than in the bottom break case.
This shows the importance of predicting the flow regime and more generally the
vertical repartition of steam and water in horizontal pipes.
Postulated loss of RHR accidental transients at very low pressure (close to atmospheric
pressure) may create high velocity steam flow in the HL. Such situations may
occur during mid-loop operation with vent valves possibly open or even with an open
manhole in the pressurizer or the SG header. The loss of mass inventory is controlled
by water entrainment either in the pressurizer or to the SG, which depends a lot on the
flow regime in the HL. Transitions from stratified to slug flow by Kelvin-Helmholtz
instability or to stratified-mist flow by droplet entrainment at wave crests may occur
and influence the water entrainment out of the circuit.
SI in CL, or in both CL and HL, induce direct contact condensation since subcooled
water is injected into a saturated steam or steam-water mixture. Analysis of SI COSI
experiments (see Janicot and Bestion, 1993) has shown that a stratified flow is created
in most cases. However, the high turbulence created by SI jets induces an efficient
mixing which enhances the local condensation. In the case of a very high condensation
rate (when the SI flow rate is very high) in a CL there may be a condensation-induced
Kelvin-Helmholtz instability with a liquid slug which may go back to the pump at high
velocity. UPTF refill tests have also shown that condensation may be sensitive to the
presence of small amounts of degassed nitrogen at the accumulator injection, which
limits the condensation and prevents large instabilities.
In summary the main phenomena that must be predicted with sufficient accuracy in
horizontal legs are:

<!-- page 690 (PDF 52) -->
l
Transition from bubbly to stratified flow
l
Transition from stratified flow to slug flow by Kelvin-Helmholtz instability
l
Transition from stratified flow to stratified-mist flow by droplet entrainment
l
Transition from mist flow to stratified-mist flow by droplet deposition
l
Presence of free surface waves which increase the interfacial friction
l
Occurrence of fluvial and torrential flow regimes with a possible hydraulic jump
l
Effects of the cross-section area changes and of orientation changes (in the bends of HL and
IL) on the free surface position
l
All phenomena which affect a possible free surface inclination, such as interfacial friction or
wave propagation
l
Remaining water mass in IL after a loop seal clearing
l
Interfacial heat and mass transfers associated with DCC at SIs, which depend a lot on
turbulence created by ECCS jets
Other phenomena exist in horizontal legs which are less sensitive in accidental transients
. Wall friction in large diameter pipes is rather small compared to friction in
other components such as the core and SGs so that they do not influence the loop flow
rate a lot. Therefore, the modeling of wall friction does not require a high accuracy. In
bubbly or slug flows in horizontal legs there is practically no slip between gas and
liquid due to the absence of buoyancy forces, so the transition from bubbly to slug
flow and the interfacial friction in these flow regimes do not require very accurate
modeling.

## 11.9.2 Horizontal flow modeling with the two-fluid model

As already discussed in Section 5.8.3, the 1-D two-fluid one-pressure six-equation
model is able to describe many important features of two-phase flow in horizontal
or inclined pipes including stratification where a significant pressure difference
may exist between phases due to gravity.
The case of a stratified flow in a horizontal or inclined duct is particular since the
interface has a simple shape and the pressure field in a cross-section may be reasonably
approximated. The CATHARE code two-fluid six-equation model able to
describe stratified flows was derived by de Crecy (1986), see also Bestion and
Serre (2012) using the following assumptions:
l
A hydrostatic transverse pressure gradient
l
Vapor and liquid densities uniform over the cross-section
l
Continuity of pressure across the interface (no surface tension effect and no pressure jump
induced by mass transfer)
In such conditions the derived momentum equations are:
∂
∂tAαkρkVk + ∂
∂zAαkρkV2
k + Aαk
∂P
∂z = Aαkρkgz + AεkГWi ≡εkSiτi ≡Skτwk
≡ Api
∂αk
∂z + 1≡αk
pi
∂A
∂z + A
3)
2εkα 1≡α
ð
Þρm
∂gcosθ
∂z
with

<!-- page 691 (PDF 53) -->
pi = α 1≡α
ð
Þ ρL ≡ρV
ð
ÞgcosθA
1)
ρm = αρV + 1≡α
ð
ÞρL
The pi
∂αk
∂z term plays a very important role in stratified flow. It represents the force
which tends to homogenize the free surface elevation in horizontal pipe. It controls the
characteristic velocity corresponding to void fraction waves which are shallow water
waves at the free surface of the stratified flow.
The “cross-momentum equation” obtained by eliminating the pressure gradient
between gas momentum and liquid momentum controls the slip ratio, whereas the
total mixture momentum equation (addition of the gas and liquid momentum equation
) controls relations between flow rate and axial pressure gradient.
In the case of horizontal steady established flow (∂
∂t = 0 and zero axial gradient of
velocities and void fraction) and for a constant cross-section horizontal pipe without
interfacial mass transfer, one can write a simple force balance representing the
equilibrium:
Siτi ffiαSLτwL ≡ 1≡α
ð
ÞSVτwV
However, this equilibrium is practically never reached in HL, IL, and CL.
In many stratified situations in HL, IL, and CL, wall friction terms are negligible
but there is a level slope such that the force balance may be described by the following
approximation equation:
Siτi ffi≡Api
∂αk
∂z
In the case of a stationary steep level slope such as a hydraulic jump, the inertial forces
may not be negligible and the situation may be described by the following approximation
equation:
∂
∂zAαvαl ρvV2
v ≡ρlV2
l
+ Siτi ffi≡Api
∂αk
∂z

## 11.9.3 Properties of the system of equations for stratified flow

As shown by de Crecy (1986), the characteristic equation may be written from mass
and momentum equations for gas and liquid. It is here assumed that both phases are
incompressible and sound speed is infinite in order to simplify the calculation of the
void wave propagation velocities. It results in the following equation:
λ2 ≡2λ f
ρV + f
ρV2 ≡pi = 0

<!-- page 692 (PDF 54) -->
The hyperbolicity condition is:
pi > f
ρV2 ≡
f
ρV
□2
ρm
With
eX = αXL + 1≡α
ð
ÞXV
or
pi > α 1≡α
ð
Þρvρl Vv ≡Vl
ð
Þ2
ρm
The characteristic velocities are W+Cα and W≡Cα where:
C2
α = ρmpi ≡α 1≡α
ð
Þρvρl Vv ≡Vl
ð
Þ2
ρ2
m
W = αρlVl + 1≡α
ð
ÞρvVv
αρl + 1≡α
ð
Þρv
The limit between fluvial (subcritical with respect to void waves) and torrential
(supercritical with respect to void waves) occurs when W=Cα, or when:
pi = f
ρV2
Then depending on the value of pi, one may find nonhyperbolic flow, torrential flow,
or fluvial flow as shown in Fig. 11.18.
An example of two flows obtained in the MHYRESA test facility (representing a
PWR HL) is shown in Fig. 11.19. The water level H increases progressively in the case
of the flow rate Q4, whereas it increases suddenly with the flow rate Q6. Condition Q4
is fluvial from entrance to exit whereas condition Q6 is torrential then fluvial after a
hydraulic jump.
Momentum equations with the pi∂α=∂z term presented above have the capability of
the Saint-Venant equations to distinguish the two flow conditions and to predict a
Nonhyperbolic
Torrential
–
∼
rV2
pi
∼
rV2
Fluvial
rm
∼
(rV)2
Fig. 11.18 The torrential and fluvial stratified flow regimes depending on the pi value.

<!-- page 693 (PDF 55) -->
hydraulic jump. This is not possible when using a simple mixture momentum equation
with drift flux.

## 11.9.4 Predicting stratification

All models for the transition from stratified flow to slug flow or intermittent flow are
based on an analysis of the Kelvin-Helmholtz instability in one or two dimensions.
The CATHARE model assumed that a 1-D analysis is sufficient and that the model
equations contain enough information to study these instabilities.
Two kinds of linear stability analysis have been investigated (Bestion and Micaelli,
1986) a high frequency linear stability and a marginal stability analysis. They consist
in determining the conditions when a void fraction wave has a positive growth rate.
High frequency analysis considers only differential terms of the equation and
neglects the viscous and algebraic source terms. It corresponds to the hyperbolicity
limit of the system of equations. It can be demonstrated that when the hyperbolicity
is not satisfied, high frequency waves are unstable and all wave lengths are unstable.
The limit overestimates the stability domain.
It corresponds to a limiting Froude number defined as:
Fr =
ρvρl Vv ≡Vl
ð
Þ2
gcosθ ρl ≡ρv
ð
Þρm
= 1
The marginal stability analysis takes into account all terms of the equation and determines
the limit at which at least one wavelength becomes unstable. There is no explicit
expression for this limit and it must be solved numerically.
0.5
1.5
z (m)
Hydraulic jump
H (cm)
2.5
Q 4
Q 6
Fig. 11.19 Examples of water level evolution in the MHYRESA hot leg.

<!-- page 694 (PDF 56) -->
The two limits are illustrated in the plane Jv versus Jl by adding the mechanical
equilibrium equation for established flow as in Fig. 11.20. It was observed that the
limit value of 0.25 for the Froude number is close to other stratification criteria
(Taitel and Dukler, 1976) and not far from the marginal stability limit.
Therefore, it was considered that:
1<Fr
Nonstratified flow
(R1=0)
0.25<Fr<1
Transition
(0<R1<1)
Fr<0.25
Stable stratification
(R1=1)
A rate of stratification R1 in the range 0–1 may be defined based on the K-H
instability.
However, this only considers the stability of a stratified flow; it is not sufficient to
determine the flow regime. The stability of a bubbly flow regime must also be
analyzed.

### 11.9.4.1 Stability of bubbly flow regime

A horizontal bubbly flow can remain dispersed bubbly or change to another flow
regime depending on the forces acting on the bubbles in the vertical direction:
l
The buoyancy force may induce bubble rising and accumulation at the upper part of the pipe,
where they can coalesce. If the coalescence dominates, the bubbles will merge leading to
large gas pockets that eventually lead to stratified flow, slug flow, or plug flow.
l
Turbulence of the liquid tends to mix the bubbles and homogenizes the bubble concentration,
preventing their accumulation at the upper part of the pipe and thus their coalescence. Bubbles
are dispersed by being entrained by the liquid eddies due to the drag force and added
mass force associated with the fluctuating velocity field.
l
Average drag force in the mean flow slows the movement of the bubbles whatever the
direction.
Hyperbolicity limit
Fr=1
Fr=1/4
Nonstratified
All waves unstable
Stratified
All waves stable
Transition
At least 1 unstable wave
JI
JV
Marginal stability
Fig. 11.20 Qualitative view of stability domains with respect to Kelvin-Helmholtz.

<!-- page 695 (PDF 57) -->
Therefore, the persistence of the dispersed flow will strongly depend on the liquid turbulence
intensity since it can first prevent the bubbles rising, then prevent their coalescence
and it may also break the largest ones. It also depends on the bubble size:
small bubbles are more likely to be entrained by eddies since the drag coefficient
is higher than for large bubbles. In addition, the buoyancy force is proportional the
bubble size to the cube when drag and turbulent dispersion forces are proportional
to the squared bubble size.
The modeling of the transition from bubbly to stratified flow or slug flow may consist
in comparing two velocity scales: Vb is the bubble rising velocity and Vt is the
liquid turbulent velocity scale. One will consider that the flow will remain bubbly
if the turbulent velocity is significantly larger than the rising velocity and transition
to stratification may occur in the opposite situation.
For example, the bubble rise velocity was taken in CATHARE 2 as:
Vb = 4σgΔρ
ρ2
l
□
(1)
and the turbulent liquid velocity was taken proportional to the wall friction velocity:
Vt =
ffiffiffiffiffiffi
τwl
ρl
r
=
ffiffiffiffiffi
Cf
r
Vl
With Cf = 0:003 one obtains Vt = 0:039Vl.
Experimental data sources have been used to calibrate the transition criterion. The
stratification is possible almost when Vt < Vb and impossible almost for Vt > 3Vb with
a transition in between. Similar criteria were adopted by other system codes.
Looking at the stability criteria for Kelvin-Helmholtz instability and for the stability
of bubbly flow four cases are possible:
1. Stable stratified flow possible and stable bubbly flow impossible: in this case one can easily
decide that the flow is stratified.
2. Stable stratified flow impossible and stable bubbly flow possible: in this case one can easily
decide that the flow is bubbly.
3. Stable stratified flow impossible and stable bubbly flow impossible: in this case one can easily
decide that the flow is intermittent (slug or plug flow).
4. Stable stratified flow possible and stable bubbly flow possible: in this case one cannot easily
decide what the flow regime is.
This last case corresponds to flow conditions with rather high liquid velocity and
rather low velocity difference between phases; this may occur in bubbly, slug, and
stratified flows. One should know the history of the flow to determine which regime
is possible and this is not possible with only the six local variables of the two-fluid
model. More advanced models may provide useful additional information. If a transport
equation for the interfacial area was added it could clearly allow distinguishing
stratified flow from bubbly flow. A multifield model with two gas fields (continuous
gas and dispersed bubbles) could also easily distinguish stratified flow from bubbly

<!-- page 696 (PDF 58) -->
flow. In the absence of knowledge of the history, the CATHARE six-equation model
preferred to select bubbly flow when both bubbly and stratified flow could be stable.
This allows stratification only when stratified flow is stable and bubbly flow unstable.
In PWR horizontal legs, high liquid velocities are mainly encountered when pumps
are still on. Therefore, the flow at the inlet of the CL cannot be stratified due to strong
perturbations in the pump. At the exit of the UP there may be either a bubbly flow or a
stratified flow with bubbles below the free surface depending on the position of a possible
swell level in the UP. In the latter case the CATHARE code may be partly wrong
by predicting pure bubbly flow. However, this situation does not happen very often
and no big discrepancy in IET prediction was observed which could be attributed
to this weakness of the flow regime identification.

### 11.9.4.2 Interfacial friction

In horizontal bubbly flow in large diameter pipes, there is a low axial pressure gradient
and consequently the mean velocity of the bubbles and of the liquid are very close. It is
not difficult to predict the right slip between phases which is nearly zero. A simple
extrapolation of the interfacial friction from vertical bubbly flow would be convenient
. For the same reasons extrapolating the interfacial friction from vertical slug
flow would be convenient in horizontal flow.
For stratified flow the interfacial friction is much lower and there can be large
velocity differences between phases. The interfacial friction coefficient depends a
lot on the presence of waves. The TRACE code (TRACE, 2007a) adopted only
a friction coefficient for stratified smooth regime. The RELAP5 code also uses
an interfacial friction coefficient for stratified flow which is similar to the wall friction
(Blasius model). Several academic works may be found in the literature which
correlated the interfacial friction based on experiments including wavy stratified
flow. The friction coefficient depends on some gas Reynolds number or on a Froude
number to take into account the roughness due to waves. However, there may be a
difficulty since the roughness due to waves may depend on the axial location along
the pipe since waves are created and increase progressively in amplitude as shown
in Fig. 11.21.
The average liquid level H may be constant or quasi-constant while the amplitude
of waves increases. This should produce an increasing interfacial friction coefficient
but there is nothing in the principal variables of the two-fluid model which can tell
what the local amplitude of waves is. The time-averaged values of the void fraction
and of the phase velocities are constant. Therefore, it is impossible to predict the axial
increase of the interfacial friction when the wave amplitude increases. One can only
adopt a homogeneous average friction coefficient which takes into account the presence
of waves. However, for the same conditions, the average wave amplitude is
smaller for a short pipe than for a longer pipe. It was considered that the models of
the literature were not well adapted to the reactor HL, IL, and CL since they were
obtained for established flow conditions in very long pipes. Therefore, the interfacial
friction coefficient of the CATHARE code was derived from experiments which
represented an IL and a HL. This was supposed to be the best compromise.

<!-- page 697 (PDF 59) -->
One must notice that only the roughness of the waves which are not predicted by
the code has to be taken into account in the averaged friction coefficient. As shown
above “shallow water waves” may be predicted by the two-fluid model due to the
pi∂α=∂z term which gives to the two-fluid equations the capabilities of the
Saint-Venant equations. Such waves have a wave length longer than twice the water
depth. Shorter wavelength waves may be created at the free surface of the stratified
flow which cannot be predicted by the two-fluid model—they are “deep water
waves”—even if the time averaging was made on a very short time interval. At least
all these deep water waves should be taken into account by interfacial friction
coefficients.

## 11.9.5 Conclusion on predictive capabilities of two-fluid model in horizontal pipes

In the classical two-fluid six-equation one-pressure model, the axial effects of gravity
forces may be correctly taken into account even in the case of change of the
cross-section area or of the pipe orientation (see Section 5.8.3 in Chapter 5). It can
predict both fluvial and torrential flow with a possible hydraulic jump. The shallow
water waves may be predicted but the presence of small wavelength “deep water
waves” should be treated as a free surface roughness in the interfacial friction coefficient
for a stratified flow regime.
Since phase stratification plays a dominant role, the Kelvin-Helmholtz instability
and the stability of bubbly flow regime must be considered. A transition criterion
based on a Kelvin-Helmholtz instability and a criterion for the transition from bubbly
to stratified flow regime can be established from local flow variables. The prediction
of the actual flow regime may be obtained from these two criteria except when both
stratified flow and bubbly may be found stable. For this situation the two-fluid model
cannot decide what the flow regime is whereas a multifield could easily determine the
flow regime.
The use of a transition domain between bubbly and stratified flow or between stratified
and slug flows provides a progressive change of flow regime. Then the predicted
qualitative behavior is consistent with the physics but there is no quantitative control
of the transition time period. Here again a multifield model could model the transition
and the time period and space extension of the transition may be physically controlled.
Fig. 11.21 Typical formation
of a wavy stratified flow.
