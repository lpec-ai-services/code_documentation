# Flow regime map
<!-- source PDF pages 6-15 -->

<!-- page 554 (PDF 6) -->
9.3
Flow regime map
Extensive studies of gas-liquid two-phase flow have their origins in the petrochemical
and chemical process industries. These were further investigated in the nuclear power
industry for their own purposes. One of the complicated features in a two-phase flow
is its liquid-gas interface structure. A particular type of geometric distribution of the
liquid and gas phases in a two-phase flow is called a flow pattern or flow regime
(Collier and Thome, 1994). It has an important effect on the prediction of void fraction
, wall and interfacial heat transfer, interfacial drag, and pressure drop.
In most system TH codes, flow regimes are divided into pre- and post-CHF flow,
depending on wall temperature. The post-CHF flow regime is used when the temperature
of a wall surface is above the minimum stable film boiling temperature and, thus,
the liquid phase cannot contact the hot surface. Otherwise the pre-CHF flow regime
is used.
Pre-CHF flows are typically subcategorized into vertical flows, horizontal flows,
and inclined flows. Fig. 9.2 shows the schematic representation of vertical flow
regimes in pipes (Collier and Thome, 1994).
In a bubbly flow, small bubbles are dispersed as discrete bubbles in a continuous
liquid phase. With increasing void fraction, the small bubbles coalesce into larger
slugs, whose diameters approximately reach the pipe diameter, resulting in a slug flow.
The nose of the slug bubble has a spherical cap. The length of the main gas bubble can
vary considerably. The flow structure becomes unstable with increasing flow velocity.
The net flow remains upward, but components of the flow travel in both directions.
Bubble
Slug
Taylor cap
bubble
Annular mist
Mist
Increasing void fraction and/or vapor velocity
Fig. 9.2 Schematic of vertical flow regimes.

<!-- page 555 (PDF 7) -->
The instability comes from the balance of the gravity and shear forces acting in opposing
directions on the thin liquid film of the Taylor bubbles. Slug bubbles are more likely
in smaller pipes, while Taylor cap bubbles are more common in larger pipes. Churn
flow may be formed by the breakdown of the large bubbles in slug flow.
The annular-mist regime follows with increased gas flow rate. The interfacial shear
of the high-velocity gas on the liquid film dominates over gravity in the annular flow
regime. When the heat transfer from the wall increases further, the liquid film disappears
or dries out, finally reaching a mist flow.
Fig. 9.3shows horizontal flow regimes. They have different characteristics dueto the
asymmetryofthephasesresultingfromtheeffectsofgravity(CollierandThome,1994).
The bubble flow pattern is similar to that of vertical flow—at low liquid velocities the
gas bubbles tend to travel in the upper half of the pipe, whereas at high liquid velocities
the bubbles are dispersed. By increasing the vapor flow, plug flow is formed. This is
similar to slug flow in a vertical pipe. The stratified or stratified wavy flow only occurs
at low liquid and gas velocities, where the two phases flow separately with a relatively
smooth interface. As the gas velocity is increased, the interface becomes disturbed by
waves traveling in the direction of the flow. A further increase in the gas velocity causes
the waves at the interface to bridge the channel and form a frothy slug that is propagated
with a high velocity. A still higher gas velocity results in the formation of a gas core with
a liquid film around the periphery of the pipe. This annular regime is usually accompanied
by the presence of entrained droplets due to the high gas velocity.
In the post-CHF flows, the liquid phase cannot contact the hot surface. This leads to
inverted flow regimes, with the gas phase in contact with the wall, as illustrated schematically
in Fig. 9.4.
In inverted annular flows, there is a core of liquid in the center of the pipe surrounded
by an annulus of vapor. In inverted slug flow, large slugs of liquid surrounded
by vapor are present. In dispersed flows, droplets are present in a vapor flow with no
liquid in contact with the wall. These flow regimes may exist in the reflood phase of an
LOCA in a PWR.
The flow regime map and transition criteria have been developed to identify the
flow regimes for local flow conditions. Some old flow regime maps, which are still
Slug
Plug
Annular
Bubble
Stratified/
stratified wavy
Increasing void fraction and/or velocity
Fig. 9.3 Schematic of horizontal flow regimes.

<!-- page 556 (PDF 8) -->
used, are summarized in Table 9.1. The complexity and deficiencies in the understanding
of various flow regimes can be seen indirectly from the various flow variables
which are used for flow regime identification. This complexity results from the difficulty
of observation and measurement—the flow regimes are very sensitive to flow
geometry, and the transition mechanisms are not clearly known.
Traditional two-phase flow-regime criteria based on gas and liquid superficial
velocities may not be suitable for the analyses of rapid transient or entrance flows
by the two-fluid model. Ishii and Mishima (1984) assumed that direct geometrical
parameters, such as the void fraction, were conceptually simpler, and therefore more
reliable parameters could be used in flow regime criteria than the traditional parameters
. They developed new flow-regime criteria for upward gas-liquid flow in vertical
tubes considering the mechanisms of flow regime transitions. These became the basis
for the RELAP5 and TRAC-PF1 flow regime maps.
In the remainder of this section, the vertical and horizontal flow regime maps of
RELAP5 are briefly introduced first, and those of other system TH codes are also
discussed. The RELAP5 flow regime maps are similar to those of the RELAP5-
3D, TRACE, and SPACE codes. It is noted that, in RELAP5, the volume and junction
flow regime maps are provided separately. The volume flow regime map is based on
volume quantities, which is used for interfacial heat and mass transfer, wall friction,
and wall heat transfer. The junction flow regime map is based on both junction and
volume quantities. It is used for the interphase drag and shear, as well as the
Top
quench front
Bottom
quench front
Pre-CHF regime:
annular/mist
Dispersed flow
Inverted slug
Pre-CHF regime:
bubbly/slug
Inverted annular
Hot wall
Fig. 9.4 Schematic of inverted
flow regimes in post-CHF
conditions (USNRC, 2013).

<!-- page 557 (PDF 9) -->
coefficient of virtual mass. Conceptually the volume and junction flow regime maps
are the same.

## 9.3.1 Vertical flow regime map

Fig. 9.5 shows the schematic of the RELAP5 vertical flow regime map (USNRC,
1998a). This map for both up and down flow is for volumes whose elevation angle
ϕ is such that 45<jϕj<90 degrees. It is noted that, in RELAP5-3D (Idaho
National Lab., 2012a), nearly the same vertical flow regime map is used for
60□jϕj<90 degrees and the horizontal flow regime map for 0<jϕj<30 degrees.
An interpolation region between vertical and horizontal flow regimes is used for volumes
whose absolute value of vertical inclination angle is between 30 and 60 degrees.
Kim et al. (2007, 2010) showed that the flow regime is very sensitive to flow geometry
and angle. It is clear that the approaches in the two codes may have great uncertainties.
The vertical flow regime map in Fig. 9.5 is modeled as nine regimes: four for
pre-CHF heat transfer, four for post-CHF heat transfer, and one for vertical stratification
. For pre-CHF heat transfer, the regimes modeled are the bubbly, slug,
annular-mist, and mist-pre-CHF regimes. The mist-pre-CHF regime was added for
smoothness. For post-CHF heat transfer, the bubbly, slug, and annular-mist regimes
are transformed to the inverted annular, inverted slug, and mist regimes, respectively,
as suggested by Ishii and Jarlais (1982). The mist-post-CHF regime was added for
symmetry with the mist-pre-CHF regime.
Table 9.1 Old flow regime maps
Authors
Geometry
Flow regimes
Flow variables
Baker (1953)
Horizontal pipe
Bubble, forth,
plug, slug,
stratified, wavy,
annular
Superficial mass velocities
of the vapor and liquid
phases
Taitel and
Dukler (1976)
Horizontal pipe
Bubble,
bubble-slug, slug,
churn, wispyannular
, annular
Four dimensionless
numbers: T, F, K, X
Fair (1960)
Vertical tubes
Bubble, slug,
annular, mist
Mass flux and a
dimensionless parameter,
x
1·1
□
□0:9
ρl
ρg
!0:5
μl
μg
!0:5
Hewitt and
Roberts (1969)
Vertical tubes
(small diameter
1–3 cm)
Bubble, plug/
slug, annular,
wavy, stratified
Superficial momentum
fluxes of the liquid and
vapor phases
Taitel et al.
(1980)
Vertical tube
(5 cm diameter)
Bubble, slug,
churn, finelydispersed
bubble
Superficial velocities of the
vapor and liquid phases

<!-- page 558 (PDF 10) -->
The schematic in Fig. 9.5 is three-dimensional, to illustrate flow regime transitions
as functions of void fraction (αg), average mixture velocity (vm), and boiling regime
(pre-CHF, transition, and postdryout), where
vm = Gm
ρm
,
(9.6)
Gm = αgρg Vg
 + αf ρf Vf
:
(9.7)
When the mixture velocity is sufficiently low (≡50%) in comparison with the Taylor
bubble velocity (vTb), the flow is assumed to be vertically stratified. vTb is given by the
correlation:
vTb = 0:35
gD ρf ·ρg
□
□
ρf
1=2
:
(9.8)
In the pre-CHF regimes, the void fraction of bubbly-to-slug transition (αBS) is given by
αBS =
αL
for Gm □ 2000 kg=m2s,
αL + 0:001 0:5·αL
ð
Þ Gm ·2000
ð
Þ
for 2000 □ Gm □ 3000 kg=m2s,
0:5
for Gm □ 0,
>
>
<
>
>
:
(9.9)
Vertically stratified (VST)
Transition
Unstratified
Bubbly
(BBY)
BBY/IAN
Slug
(SLG)
SLG/
ANM
Annular
mist (ANM)
Inverted annular
(IAN)
IAN/
ISL
IAN/
ISL-SLG
ISL/
SLG-ANM
Mist
(MST)
Inverted slug
(ISL)
SLG/
ISL
0.0
1.0
Increasing void fraction
Increasing
mixture
velocity
0.0
1.0
Post-dryout
Transition
Pre-CHF
vTb
2vTb
ANM/MST
Fig. 9.5 Schematic of the RELAP5 vertical flow regime map (USNRC, 1998a).

<!-- page 559 (PDF 11) -->
where
αL = 0:25 min 1:0,
D*
22:22
□
□8
"
,
D* = D
g ρf ·ρg
□
□
σ
1=2
,
D is the pipe diameter.
The slug-to-annular transition void fraction (αSA) is given by
αSA = 0:25min α f
crit, αe
crit
□
□
,
(9.10)
where
α f
crit =
Vg
gD ρf ·ρg
□
□
ρg
1=2
for upflow,
0:75
for downflow and countercurrent flow,
>
>
>
<
>
>
>
:
αe
crit = 3:2
Vg
gσ ρf ·ρg
□
□
ρ2
g
1=4
:
The transition region between the slug flow and annular-mist flow regimes is defined
by αDE and αSA where
αDE = max αBS,αSA ·0:05
ð
Þ:
(9.11)
The minimum void fraction for annular-mist flow, αSA, is constrained to lie between
0.5 and 0.9. For the transition between annular mist and mist pre-CHF, the value of
αAM is
αAM = 0:9999:
(9.12)
If the hydrodynamic volume has heat flux from a surrounding wall to the vapor, or the
reflood model is turned on for that wall, and the vapor temperature is more than 1 K
superheated, then the flow regime is a post-CHF regime, in which the previous αBS and
αSA are still effective. The transition region between inverted slug flow and inverted
annular flow regimes is defined by αBS and αCD, where
αCD = αBS + 0:2:
(9.13)

## 9.3.2 Horizontal flow regime map

The horizontal flow regime map is for volumes whose elevation angle ϕ is such that
0<jϕj<45 degrees. This map is similar to the vertical flow regime map except that

<!-- page 560 (PDF 12) -->
the post-CHF regimes are not included, and a horizontally stratified regime replaces
the vertically stratified regime. The horizontal flow regime map therefore consists of
horizontally stratified, bubbly, slug, annular-mist, and mist-pre-CHF regimes.
A schematic for the horizontal flow regime map is shown in Fig. 9.6 (USNRC,
1998a). The transition criteria for the bubbly to slug and the slug to annular-mist
regimes are similar to those for the vertical map.
The bubbly-slug transition criterion is
αBS =
0:25
for Gm □ 2000kg=m2s,
0:25 + 0:00025 Gm ·2000
ð
Þ
for 2000 < Gm < 3000 kg=m2s,
0:5
for Gm □ 3000 kg=m2s:
>
<
>
:
(9.14)
The minimum void fraction for annular-mist flow, αSA, is a constant
αSA = 0:8,
(9.15)
and the transition region between slug flow and annular-mist flow regimes is defined
by αDE and αSA, where
αDE = 0:75:
(9.16)
The annular-mist to mist-pre-CHF transition criterion is
αAM = 0:9999:
(9.17)
The flow is horizontally stratified if the phasic velocity difference satisfies the
condition
Vg ·Vf
 < Vcrit
BBY-HST
SLG-HST
SLG/
ANM-HST
ANM-HST
MPR-HST
Increasing void fraction
Horizontally stratified (HST)
Bubbly
(BBY)
Slug
(SLG)
SLG/ANM
Mist
Pre-CHF
(MPR)
Annular
mist
(ANM)
vcrit and
2500 kg/m2s
vcrit and
3000 kg/m2s
Increasing
relative
velocity
and mass flux
0.0
1.0
Fig. 9.6 Schematic of the RELAP5 horizontal flow regime map (USNRC, 1998a).

<!-- page 561 (PDF 13) -->
and the mass flux satisfies the condition
Gm < 3000kg=m2s,
where Vcrit = 1
ρf ·ρg
□
□
gαgA
ρg sin θ
1=2
1· cos θ
ð
Þ and the angle θ is defined in Fig. 9.7.
If the above two conditions are not met, then the flow field undergoes a transition to
the bubbly, slug, annular-mist, or mist-pre-CHF flow regime.
In addition to the vertical and horizontal flow regime maps, RELAP5 provides the
high mixing flow regime map, which is used in pumps, and the ECC mixer volume
flow regime map.

## 9.3.3 CATHARE 2 and TRACE flow regime maps

In the CATHARE 2 code, only two flow regime transition criteria are explicitly written
, and they are used in several closure terms (Bestion, 1990; Serre et al., 2011;
Bassenghi, 2013).
The first transition is between stratified and no stratified flow, which is associated
with the parameter R in Fig. 9.8. This transition depends on two criteria: the first criterion
is based on the Kelvin-Helmholtz instability threshold, and the second depends
on the relative effects of bubble sedimentation and of bubble turbulent mixing. The
second transition is between annular and droplet flows, which is associated with
the parameter E in Fig. 9.8.
The parameters R and E are used for interpolation to establish smooth transitions of
the flow regimes. The post-CHF flow regimes in CATHARE 2 are inverted annular
and dispersed flow (liquid slugs and/or droplets).
The TRACE code considers three distinct classes of flow regimes (USNRC, 2013):
(i) the pre-CHF flow regime consist of the bubbly/slug and the annular/mist regimes,
(ii) the horizontal stratified flow regime is available for 1-D components that are either
horizontal or inclined, and (iii) the post-CHF flow regime encompasses the inverted
Vapor
Liquid
Fig. 9.7 Horizontally stratified flow.

<!-- page 562 (PDF 14) -->
flow regimes that occur when the wall is too hot for liquid-wall contact. The TRACE
pre-CHF flow regime map, which is used for interfacial heat transfer, is that of
TRAC-PF1/MOD2 (Spore et al., 1993). As shown in Fig. 9.9, the flow regime is based
on void fraction and mass flux, with the mass flux range limited for the Taylor cap or
slug bubble flow regime. The map is similar to that of RELAP5 except that there is no
vertically stratified flow regime.
Pipe
Annulus
Rod bundle
Dispersed
(bubbly,
churn, slug)
Transition
Stratified
Annular
Annular mist
E = 0
R = 0
R = 1
0<E < 1
Rate of
stratification
0<R < 1
Fig. 9.8 Schematic of the CATHARE 2 pre-CHF flow regime map.
Dispersed
bubble
Cap/slug
bubble
Interpolation
region
Annular mist
Void fraction
0.3
0.5
0.75
Mass flux (kg/m2s)
Fig. 9.9 Schematic of the TRACE pre-CHF flow regime map (USNRC, 2013).

<!-- page 563 (PDF 15) -->
## 9.3.4 Limitations of the flow regime map approach and recent improvements

The flow regime map is very important because it determines the flow regime for a given
localflowconditionand,basedontheflowregime,theinterfacialtransfermodelandinterfacial
area per unit volume (or called interfacial area concentration, IAC) are determined.
The shortcomings caused by the traditional two-phase flow regimes and regime
transition criteria were pointed out by Ishii (1975) and coworkers (Ishii and
Mishima, 1980; Hibiki and Ishii, 2002; Ishii et al., 1998; Uhle et al., 1998), which
can be summarized as follows:
l
The flow regime transition criteria are algebraic correlations, which have been usually developed
from steady-state, fully developed flows. Hence, the effects of the entrance and developing
flow cannot be taken into account correctly, nor can the gradual transitions between
regimes.
l
The transition criteria and flow-regime-dependent IAC correlations are valid in limited
parameter ranges for certain operational conditions and geometries. Most of them are
obtained from simple experiments and phenomenological models. Often the scale effects
of geometry and fluid properties are not correctly taken into account.
l
The method based on the flow regime transition criteria is a two-step method, which requires
flow configuration transition criteria and IAC correlations for each flow configuration. The
compound errors from the transition criteria and IAC correlations can be very significant.
To solve such problems, the interfacial area transport equation (IATE) was introduced
(Ishii, 1975; Ishii and Kojasoy, 1993; Kocamustafaogullari and Ishii, 1995). The
IATE can be obtained by considering the fluid particle number density transport equation
analogous to Boltzmann’s transport equation (Wu et al., 1998; Morel et al., 1999).
The one-group formulation was suggested first, where the dispersed bubbles are
assumed to be spherical in shape (Ishii et al., 2000; Hibiki and Ishii, 2002). The
one-dimensional form of the one-group IATE in a bubbly flow is given by:
∂ai
∂t + r □ aiV
⃗
g
□
□
= ΦB ·ΦC + ΦP + ΦE:
(9.18)
The four terms in the right-hand side of Eq. (9.18) indicate the rates of change of IAC
due to bubble breakup, bubble coalescence, phase change, and bubble expansion,
respectively.
To realistically describe the interfacial area transport in various two-phase flow
regimes, the two-group transport equation was suggested (Ishii et al., 2005; Ishii and
Hibiki, 2006). This is because the differences in bubble sizes or shapes cause substantial
differences in their transport mechanisms and interaction phenomena. Therefore, two
transport equations for two characteristic groups of bubbles were suggested: group 1
for small dispersed and distorted bubbles, and group 2 for cap/slug/churn-turbulent
bubbles. The maximum bubble diameter of the group 1 bubble is given by
Dd,max = 4
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
σ= gΔρ
ð
Þ
p
:
(9.19)
The two-group IATEs have more complicated source and sink terms, including additional
intergroup transfer terms.
