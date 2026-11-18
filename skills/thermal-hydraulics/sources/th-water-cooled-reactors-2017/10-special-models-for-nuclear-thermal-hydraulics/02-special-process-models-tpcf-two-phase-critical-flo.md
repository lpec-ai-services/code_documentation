# Special process models — TPCF-Two-phase critical flow
<!-- source PDF pages 3-6 -->

<!-- page 597 (PDF 3) -->
Special process and component models are described in this chapter. Section 10.2
addresses process models and Section 10.3 describes special component models.
10.2
Special process models
These are the process or phenomena that are not amenable to modeling by current
system formulation and require either empirical correlations or separate analytical
models. In this section, some of the processes such as critical flow, Counter-Current
Flow Limitation (CCFL), entrainment and de-entrainment, reflood, break flow through
branch, area change losses, and grid spaces are described.
10.2.1
TPCF—Two-phase critical flow
Choked flow or critical flow conditions may occur in reactor transients either at a
break or in internal flow at flow restrictions or pumps. When sonic velocities are
reached at a section (often at the smallest flow cross section area) the flow becomes
independent from downstream conditions. Estimation of critical flow is then of prime
importance for all loss of coolant accident (LOCA) transients since the break flow rate
controls the system pressure and coolant mass inventory and distribution, and consequently
, the core cooling capability (see e.g., Sozzi and Sutherland, 1975).
Largeclassesofdesignbasisaccidentscenariosinvolvesometypeofoutflowfromthe
reactor system,eitherthroughpipebreak orstuck-openvalves.Theflowcouldbechoked
at high pressure. The choking could be subcooled choking, where flashing occurs at the
break,or saturated choking, where flow at the break could be two-phase mixture or could
be single-phase vapor flow choking. The computer codes for reactor simulations have
generally separate correlations for subcooled and saturated choking.
The single-phase vapor flow choking is governed by gas dynamics with choked
velocity based on velocity of sound at choking plane that is either at the exit of a
straight pipe or lowest area in a channel. This will not be discussed here.
c2 =
∂p
∂ρ
□
□
s
In the case of two-phase choking the critical flow will depend on the rate of vapor
generation at choke point. The compressibility of the mixture will depend on the rate
of vapor generation as fluid particles move toward the break. The rate of change of
density with pressure is an inverse of sonic velocity and in case of two-phase flow,
there is large change in mixture density with change in pressure, even more than in
the gas phase. The sonic velocity in two-phase flow is lower than in the
single-phase gas flow (Fig. 4.13 of Deych and Filipov, 1969). The measured values
of the ratio of two-phase sonic velocity to vapor sonic velocity, as function of quality
is shown in Fig. 10.1. There are other curves that are from different analytical models
for different frequency and bubble/droplet size in this report. Similar behavior was
mentioned in other studies (Kieffer, 1977). The conclusion was that the sound velocity

<!-- page 598 (PDF 4) -->
is lower for single-component two-phase flow compared to two-component mixture
and can vary with frequency.
This vapor generation will depend on flow regime, interfacial area, interfacial
momentum transfer or slip, and liquid superheat or degree of nonequilibrium. The
vapor generation leads to increase in mixture velocity. It was stated by Kestin
(1991) and Rohatgi and Reshotko (1975) that in case on converging-diverging nozzles
the choke point could be in the diverging section contrary to single-phase flow. The
vapor generation can compensate for increase in area and still accelerate the flow.
However, there are no tests that measure local details of two-phase flow in critical
flow tests.
The idealized situation is homogenous equilibrium model (HEM) where both
phases have same velocity and same temperature. The formulation is similar to
single-phase gas flow and provides the lowest sonic or choking velocity. However,
this type of condition could exist in long pipe where two phases have time to get close
to equilibrium conditions. HEM formulation predicts the lowest sound velocity.
G2
c,hem =
1□xc
ð
Þ
∂ 1
ρl
∂p
B
B
@
C
C
A
s
+ xc
∂ 1
ρg
∂p
B
B
@
C
C
A
s
+
ρg
□ 1
ρl
!
∂xc
∂p
□
□
□1
The homogeneous thermal nonequilibrium phenomenon was addressed by two mechanistic
approaches. In one case nucleation and bubble growth combination was used
and in another approach critical plane pressure undershoot was estimated from experiments
. The conditions at the break plane control the critical flows. It is observed that
during depressurization of subcooled liquid at the break plane, there is a delay in vapor
generation due to the finite rate of nucleation and bubble growth leading to fluid pressure
undershooting the vapor pressure. This phenomenon was studied by Alamgir and
Fig. 10.1 Ratio of sound velocity in two phase to vapor sound velocity as function quality.

<!-- page 599 (PDF 5) -->
Lienhard (1981) and Jones (1980), and expression for pressure at which vaporization
will begin, as documented in TRACE, is as follows:
Pl = Psat □Max 00,0:258
σ1:5
Tl
Tcrit
□
□13:76
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 + 13:25 □
1:01325*1011
DP
Dt
□
□0:8
s
kTcrit
ð
Þ0:5 1□ρg
ρl
□
□
□27 0:072
ð
Þ2
At
Aup
□
□2 ρlv2
t
vt = max aHEM,
v2
up + 2 Pup □Pl
□
□
ρl
□
□0:5
"
Here subscripts l, g, crit, t, up, and HEM are liquid, vapor, critical, throat, upstream,
and homogeneous equilibrium, respectively. As is seen in the expression there is an
effect of rate of change of pressure of the fluid particle as it moves from upstream to
the throat and of surface tension. Bernoulli equation is used to estimate flow at this
pressure, which is below the saturation pressure.
There have been few studies that account for nucleation and bubble growth models
to estimate vapor generation and its effect on critical flows (Rohatgi and Reshotko,
1975; Richter, 1983). While these studies provide a framework of modeling, they
require a free parameter such as nucleation site density and it is not a measured quantity
. It may vary by many order of magnitude values from 109 m□3 to 1011 m□3. These
analyses have used friction loss at the wall. In the case of gas flow with wall friction,
the critical flow is estimated from the model and it is called Fanno equations. The reason
for decrease in critical flow for gas flow is that stagnation pressure decreases and
with that critical flow decreases.
There are correlations that deal with relaxation of one or other equilibrium criterion
such as homogenous nonequilibrium or nonhomogenous equilibrium models. Most
widely used correlations are by Moody (1966) and Henry and Fauske (1971) and
HEM model is described earlier.
Moody (1965) relaxed the criterion of equal velocity but kept thermal equilibrium.
His correlation is given here.
x = s0 □sl
sg □sl
G2
c =
2 H0 □Hl □x Hg □Hl
□
□
□
(
ug
ulρl
1□x
ð
Þ + x 1
ρl
□
□2
x + 1□x
ð
Þ
ul
ug
□
□2
!

<!-- page 600 (PDF 6) -->
where H0 is stagnation enthalpy, x is equilibrium quality, s is entropy, ul and ug are
phasic velocities.
ug
ul
=
ffiffiffiffiρl
ρg
r
Fauske (1962) has suggested a slightly different slip correlation.
ug
ul
=
ffiffiffiffiρl
ρg
r
The other widely used correlation is from Henry et al. (1970) for local conditions.
They relaxed the thermal equilibrium criterion by decreasing the quality at break from
equilibrium value.
x = Nkxe
where k is slip ratio. It is stated that the slip would be close to 1.0 at choke location.
The critical mass flux expression was empirically obtained for low quality and valid
for long pipes, and is given as
N = 20xeq for 0 < xeq < 0:05
N = 1 for xeq > 0:05
Gcr = Gcr,HEM
ffiffiffiffiffiffiffiffi
Nexit
p
:
Henry (1970) also developed correlations including pipe length. The exit quality was
given as
xexit = xLT
1□exp □B
L
D□12
□
□
□
□
□
□
Here xLT is quality for long tube and defines as
xLT = Nxeq
Henry (1970) assumed incompressible liquid and isothermal expansion of vapor
phase. The critical mass flux is given as
G2
cr =
x
pρg
□
ρg
□ 1
ρl
!
Ndxeq
dp
"
exit
:
The decay constant B was obtained from fitting with the data and a value of 0.0523
was recommended.
