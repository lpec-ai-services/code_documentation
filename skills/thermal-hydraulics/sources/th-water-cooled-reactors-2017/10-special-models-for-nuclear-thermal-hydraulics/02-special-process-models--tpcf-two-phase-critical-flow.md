# Special process models — TPCF-Two-phase critical flow … Reflood
<!-- source PDF pages 3-18 -->

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

<!-- page 601 (PDF 7) -->
There are few documents (Saha, 1978; Elias and Lellouche, 1994; Levy, 1999;
Sokolowski et al., 2012; Brittain and Karwat, 1982; Miller, 2010; OECD/NEA/
CSNI, 1980) that describe various models and tests available for critical flows.
Elias and Lellouche (1994) listed 66 tests with different lengths, diameters, and pressures
. However, only 42 data sets were usable. The diameter of broken pipe varied
from very small at 4 mm to large at 76 mm. The length varied from no pipe to
1700 mm pipe. Marviken provided a data set that was much closer to reactor system.
The diameter of the pipe varied from 200 to 500 mm and length varied from 166 to
1800 mm. Elias and Lellouche’s study indicated that none of the model did well with
the data. The scatter plots indicated that most of the data were outside of ·10% of
mean line.
Saha (1978) had earlier reviewed various models and concluded the following:
1. The HEM underpredicts the critical flow rates for short pipes and near liquid saturation or
subcooled upstream conditions.
2. The equilibrium slip models of Fauske, Moody, and others, although successful for long
tubes, underpredicted the critical flow rates for short pipes. This is particularly true if the
upstream condition is subcooled or near saturation.
3. Effects of thermal nonequilibrium must be taken into account for short pipes. However, it is
not clear whether the pipe length, L, or the pipe length-to-diameter ratio, L/D, or both are
important in determining the effects of thermal nonequilibrium.
4. At present, there is no general model or correlation for critical flow, which is valid for a
broad range of pipe lengths, pipe diameters, and upstream conditions including subcooled
liquid. The more sophisticated the model used for a more precise design, the more prudent
it is to consider some data benchmarking under similar conditions.
There has not been any systematic scaling study for critical flow phenomenon. The
subphenomena that affect the critical mass flux have been identified but the data
have not been compiled with dimensionless groups representing subcooling, flow
rate, slip, wall friction, nucleation sites, geometry of break, and two-dimensional
effects. Deych and Filipov (1969, Chapter 3) have provided nondimensional analyses
and identified groups that control the flow conditions and critical flow. Their
approach was to nondimensionalize basic two-fluid balance equations with
two-phase transfer terms. They identified Strouhal (transient case), Euler, Reynolds
Froude numbers, Weber, Peclet, Prandtl, Mach, and Nusselt (at interface) numbers
for assessing similarity.

## 10.2.1.1 Models in system codes

The system codes calculate conditions at the break plane based on code models for
wall and interfacial transfer terms that include wall friction. However, flow is
restricted based on correlation for critical two-phase flow. These system codes include
constitutive relationships based on steady-state data and flow near the choke point is
rapidly changing conditions. Therefore, imposed critical flow model on break flow or
possible location of choking will be sufficient.
System codes developed either 0-D or 1-D models for break flow or chocked flow
but in the worst conditions the accuracy of prediction cannot be better than 20% due to
complex geometrical effects and to unpredictable nucleation conditions. Assessment

<!-- page 602 (PDF 8) -->
of TRAC code with Marviken as part of code scaling applicability and uncertainty
(CSAU) uncertainty estimate showed that critical flow uncertainty (or error in
comparison with experimental data) was in excess of 20% (USNRC, 1989b).
These models predict area average flow rates through the break based on the conditions
just upstream of the break. As these critical flow models are based on fluid
properties and thermal-hydraulic conditions (pressure, temperature, void fraction),
they are expected to predict break area average mass flux as independent of scale
for application with same fluid. However, nonfully developed flow conditions occur
upstream of the break and flow development depends, almost unavoidably, upon
scale. Lack of fully developed flow will also have an impact on critical flow. In
the case of power to volume scaling, the break size is scaled to volume to preserve
the timescale. Ishii et al. (1998) also stated that critical velocity or mass flux is dependent
on the property and thermal hydraulic conditions and the scaling should be
applied to the design of the break size.
An assessment of RELAP5 and TRACE critical flow models was undertaken, e.g.,
by Sokolowski et al. (2012). The conclusion from this study was that code predictive
accuracy was independent of the length of the pipe before the break. Another conclusion
implied that same correlation worked better with one code than the other. These
results indicated that the effect of length alone is not conclusive. This also means that
the other two-phase flow models that estimate void vapor generation may have more
important influence on the critical flow. Also the diameter effect has not been
established. However, unless cross-section flow variation is significant, the diameter
effect will diminish with the size of the pipe. The fact that length affects the level of
thermal nonequilibrium at the break and thus affects the flow has been accepted.

## 10.2.2 Counter-current flow limitation (CCFL)

Counter-current flow of gas and liquid appears in many places in the reactor system,
such as steam generators, core upper tie plate, hot and cold legs, and downcomer during
phases of various transients (OECD/NEA/CSNI, 1993). In most cases the liquid
flows down and gas flows up, and they interact at the interface. The shear at the interface
that increases with gas flow rate opposes the liquid down flow. This limits the
liquid down flow. CCFL is the limit of this liquid flow due to opposing gas flow.
It has safety implication in getting coolant to the core and preventing heat up.
The upper plenum tie plate is a plate with holes. Similar plates exist in BWR and
PWR. In both cases liquid may accumulate on the top and flow down on the top of the
core. However, steam up-flow may impede or prevent this liquid down flow. The
upper support plate flow is multidimensional as the steam up-flow is not uniform;
the correlations are generally for average of flows over whole plate. There are data
available at almost full scale from UPTF.
One of the most important phenomena for large break loss of coolant accident
(LBLOCA) safety is the emergency core coolant bypass, where some of the coolant
injected in the cold legs during LOCA is bypassed to broken cold leg instead of going
down in the downcomer and filling the lower plenum, and flooding the core. This
bypass is caused, in part, by the steam flow from the core to the broken cold leg

<!-- page 603 (PDF 9) -->
through downcomer. This steam up-flow in the downcomer impedes and in some
cases reverses the down flow of the coolant from the intact cold legs. The downcomer
has counter-current flow where steam flow transfers momentum at the interface and
also creates waves and entrainment at the interface. The combination of these phenomena
lead to limitation of down flow of coolant for given steam up-flow, coolant
subcooling, and downcomer geometry. It has also been observed that in the downcomer
type geometry, the liquid coming from cold legs spreads azimuthally in the
downcomer. This spreading phenomenon is much different from counter-current flow
in pipes. This counter-current flow phenomenon is shown in Fig. 10.2.
There have been many experimental studies at different scales to address CCFL
(Levy, 1999). They are in pipes and in annuli. Tests in pipes of different sizes and
liquid injection methods were used to develop CCFL correlations by Wallis and
Kutateladze. Wallis correlation is based on pipe diameter as length scale. Nondimensional
volumetric fluxes for gas and liquid are correlated well. However, this
correlation diverges from data for larger diameter pipes.
j*
g = jg
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
ρg
gD ρl □ρg
v
u
u
t
j*1=2
g
+ mj*1=2
l
= C
Core
Rapid condensation
Legend:
Steam flow
Water flow
Cold leg
Boiling on vessel wall
ECC delivery down
the downcomer
ECC
injection
Upper
plenum
Broken
cold leg
Steam/water flow
up downcomer
Downward steam
flow in core
Fig. 10.2 Flow field in downcomer during refill phase.

<!-- page 604 (PDF 10) -->
For pipes with diameter greater than 5 cm, the CCFL can be represented by
Kutateladze correlation. It has length scale based on surface tension. Kutateladze
correlation is for large pipes where waves at the interface are smaller than the pipe
diameters. This is given as
Ku*1=2
g
+ C1Ku*1=2
l
= C2
Ku*
g = jg
ρ2
g
gΔρσ
!
1)
4:
Traditionally Wallis model is used in smaller pipe component. However recent experiences
from UPTF (Wolfert, 2008; Mayinger et al., 1993) show that it can be
extended to larger pipe as well, like the hot leg of PWRs.
Wallis’ model predicted the reflux condensation return flow back to hot leg well in
both high and low pressure range. There have been correlations similar to Wallis
correlation for annular flow but were not widely used. A systematic scaling study
has been done for annular geometry (Yun et al., 2004).
Different tests with annular geometry were reviewed in CSAU (Rohatgi et al.,
1990) as given in Table 10.1 and Fig. 10.3. These tests were UPTF (1/1), CREARE
(1/5), BCL (2/15), BCL (1/15), CREARE (1/15), and CREARE (1/30). These facilities
were designed with linear scaling. A comparison of TRAC-PF1 prediction with
the data (e.g., Fig. 10.4, Martinson et al., 1989, or Rohatgi et al., 1990) indicated that
TRAC-PF1 overpredicted lower plenum filling rate (underpredicted emergency core
cooling system (ECC) bypass) for smaller facilities. For UPTF tests, TRAC-PFI
underpredicted lower plenum filling rates.
Analyses of UPTF data indicated that most of the injected ECC was unaffected by
steam flow as shown in Fig. 10.5. The cold water injection in the intact cold leg falls
under the cold leg junction and is not impeded by steam up-flow.
Yun et al. (2004) have shown that linear scaling method is not appropriate and
provided a modified linear scale method. The facilities for studying CCFL phenomena
are of annular shape. The flow is multidimensional as the spread and thickness of
the film are important. The annular gap has effect on flow regime expected in the
downcomer; therefore the size should be such that the flow regime expected is preserved
. The film thickness as it spreads under the cold leg in the downcomer is same
fraction of the downcomer gap as expected in the plant. As it implies that the interfacial
shear is same, the downcomer aspect ratio, that is gap and circumference ratio,
should be preserved as it affects the film spreading. Yun et al. (2004) showed that data
plotted in Wallis form of superficial gas velocities show that data at different
sizes match.
It is recommended that UPTF or any other full-scale data can be used for code
validation and for uncertainty analyses as they are available.

<!-- page 605 (PDF 11) -->
Table 10.1 Geometrical parameters for the CREARE, BCL and UPTF (Rohatgi et al., 1990)
PWR
UPTF
CREARE (1/5)
BCL (2/15)
CREARE (1/15)
CREARE (l/30)
Actual
Scalea
Actual
Scale
Actual
Scale
Actual
Scale
Actual
Scale
Vessel diam
4.4 m
4.87
1.1
0.89 m
0.2
0.618 m
0.14
0.292 m
0.066
0.152 m
0.034
DC, gapb
0.26 m
0.25 m
0.96
0.038 m
0.146
0.031 m
0.119
0.0126 m
0.048
0.0064 m
0.025
DC, height
5.33 m
6.64 m
1.25
1.37 m
0.257
0.82 m
0.153
0.46 m
0.086
0.229 m
0.043
LP, depthb
1.94 m
2.48 m
1.28
1.52 m
0.783
1.022 m
0.526
0.86 m
0.443
0.528 m
0.272
LP vol, M3
29.6
24.9
0.84
0.94
0.032
0.302
0.010
0.058
0.0019
0.0096
3□10□4
Cold leg diam
0.74 m
0.75 m
1.01
0.152 m
0.21
0.21
0.102 m
0.0476 m
0.064
0.076 m
0.1
DCL/D
0.168
0.154
–
0.168
–
–
0.165
0.163
–
0.5
aScale is the ratio of actual dimension to PWR dimension.
bLower plena are deeper and gaps are narrower in subscaled facilities.

<!-- page 606 (PDF 12) -->
The pioneering investigation of this phenomenon was performed in the Semiscale
facility at Idaho National Laboratory near the end of 1960s (Batt and
Berta, 1978). During the simulated LOCA conditions the flashing of lower plenum
liquid prevented the penetration of ECCS injected water. The coolant injected by
accumulators during the blowdown period was experimentally found to be almost
completely diverted toward the break, causing the bypass of the core. The resulting
phenomenon was called “ECCS-core-bypass.” The ECCS core bypass is affected by
UPTF
Recommended
Recommended: Beckner and Reyes, RIL-128.
CREARE 1/5
CREARE 1/30
CREARE 1/15
BCL 1/15
BCL 2/15
0.05
0.1
0.15
0.2
0.25
0.3
0.005
0.01
0.015
0.02
0.025
0.03
0.035
0.04
0.045
0.05
Jg
*
Jf
*
Fig. 10.3 CCFL experiments in CREARE, BCL, and UPTF (Rohatgi et al., 1990).
Scale
0.5
1.5
0.2
0.4
0.6
0.8
1.2
R MLP
CREARE (3/15)
6 RUNS
CREARE (1/15)
8 RUNS
UPTF (1/1)
4 RUNS
BCL(2/15)
12 RUNS
C1/15
B2/15
1.13
0.7
0.50
S
0.38
1.19
0.36
0.1
0.20
C1/5
Nonconservative
Conservative
U1/1
< R MLP>
R MLP -(MLP)pred/(MLP)exp
Fig. 10.4 TRAC-PF1 prediction of ECC bypass flow (Rohatgi et al., 1990).

<!-- page 607 (PDF 13) -->
many phenomena including the depressurization rate, the TPCF at the break, the
pressure drops inside the vessel and the heat transfer from the reactor pressure vessel
(RPV) walls. The last phenomenon is also known as the “hot wall delay.” The
design of ECCS and its capability to cool the core became of concern in reference
to the inability to cool the core during the LBLOCA fast depressurization observed
in the experiment. Subsequent deep analyses with continuous experimental support
continued until the availability of the full-scale UPTF experiments in Germany
(Damerell and Simons, 1992).

## 10.2.3 Entrainment and de-entrainment

Nuclear reactor system has entrainment and de-entrainment phenomena taking place
in different components such as core, steam generators, steam separator in BWR, and
suppression pool. There are three scenarios—one in which the gas bubbles out from
the interface, second, where the gas flows parallel to the interface and third, where
water is separated by centrifugal forces such as in BWR separator/dryer and steam
generator secondary side.
The phenomena of entrainment and de-entrainment are important as they affect the
distribution of liquid in gas phase, and affect the interfacial energy, mass, and momentum
transfer through the shape and size of the interface. These phenomena occur at the
interface between gas and liquid phases. The mechanism for entrainment and
de-entrainment is different. The entrainment occurs due to relative velocity between
gas and liquid leading to instabilities at the interface. The peaks in the waves are broken
by the gas phase and results in liquid entrainment. This captured liquid may break
up further until stable drop size is achieved.
–6500
–6000
–5500
–5000
–4500
–4000
–3500
–3000
–2500
–2000
–1500
–1000
–500
90°
360°
Height (mm)
BR
270°
180°
Fig. 10.5 Flow in downcomer detected in UPTF.

<!-- page 608 (PDF 14) -->
There are many mechanisms of de-entrainment. In the case of horizontal flow of
gas and droplet over an interface, any decrease in air velocity will decrease the shear
between the gas and droplets, leading the droplets to be deposited on the interface. In
the case of vertical flows, there is continuous impingement of droplets on the interface
along with creation of entrainment from wavy interface. As gas slows down,
the waviness will decrease, the entrainment will decrease, with a net effect of
de-entrainment exceeding entrainment. In addition, if there are many steps or barriers
in flow direction, the droplet will impinge and separate from the gas-droplet
mixture. While gas can change direction, the droplets due to larger momentum cannot
easily change the direction and impinge on the barriers. Grid spacers in the core
act as a separator for droplets. These droplets impinge on solid surfaces of heated
rods during accidents, providing precursor cooling prior to full-scale reflood. The
phenomena of entrainment are at localized process level and generally not modeled
by first principle in the system codes. Instead, the codes use correlations for net
entrainment.
The system codes such as TRACE and RELAP5 have correlation for entrainment
fraction, E∞based on Ishii and Mishima correlation (Ishii and Mishima, 1989):
E∞= tanh 7:25*10□7We1:25
g
Re0:25
f
h
i
where
Weg =
ρgj2
gDh
σ
Δρ
ρg
!1=3
Ref = 1□α
ð
ÞρlVlDh
μl
As can be seen the entrainment is based on local Weber number and Reynolds
number, and depends on the diameter of the tube. The interface instabilities generally
depend on the thickness of the film. Film thickness will be larger for larger
diameter pipes for same void fraction and is more likely to have instability at the
interface.
The other mechanism of entrainment is when gas bubbles emerge from the interface
and as they leave the interface, a liquid filament is created that breaks and leads to
drops. The drops have some momentum from the gas phase. However, some of the
drops can fall back to the interface. A good review of this type of entrainment was
provided by Bagul et al. (2013) and Ishii and Kataoka (1984). As in this situation,
the liquid phase is stagnant except for activity at the interface, the entrainment ratio,
Efg (h, Jg), is defined differently (see Fig. 10.6). It is the ratio of gas phase supplied and
liquid entrained above the interface. The ratio of liquid entrainment and gas flow is
shown here as function of gas space height, h. Droplets can fall back for large gas
space above interface.

<!-- page 609 (PDF 15) -->
Near interface,
Efg h, Jg
□
□
= 4:84*10□3
ρg
Δρ
□
□□1
Deposition controlled region
Efg h, Jg
□
□
= 7:13*10□4J*3
g N0:5
μg
ρg
Δρ
□
□□0:31
exp □0:205 h
Dh
□
□
For intermediate region, the entrainment depends on momentum exchange and the
rate is given for three different gas flow rates. For high gas flows the correlation near
the interface applies.
For low flows the correlation is as follows.
Efg h, Jg
□
□
= 2:21N1:5
μg *D*1:25
h
ρg
Δρ
□
□□0:31
J*
gh*□1
Forintermediateflows,J*
gh*□1 > 6:39*10□4,adifferentcorrelationwasrecommended:
Efg h, Jg
□
□
= 5:42*106J*3
g N0:5
μg
ρg
Δρ
□
□□0:31
D*1:25
h
Deposition controlled region
Near surface region
(without deposition)
h ⇒
Efg (h, Jg) ⇑
Momentum controlled region
(with deposition)
Fig. 10.6 Regions of entrainment above the separation interface.
Taken from Ishii, M., Kataoka, I., 1984. Mechanistic modeling of pool entrainment
phenomenon. Int. J. Heat Mass Transf. 27 (11), 1999–2014.

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
