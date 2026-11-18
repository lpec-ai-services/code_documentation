# Special process models — Counter-current flow limitation (CCFL)
<!-- source PDF pages 8-12 -->

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
