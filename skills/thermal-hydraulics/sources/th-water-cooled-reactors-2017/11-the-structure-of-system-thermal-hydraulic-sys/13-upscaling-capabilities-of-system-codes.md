# Upscaling capabilities of system codes
<!-- source PDF pages 66-69 -->

<!-- page 704 (PDF 66) -->
The coarse nodalization and the use of 1-D models makes it impossible for system
codes to predict CCFL and flooding limits which depend on small-scale 3-D geometrical
effects. CCFL is for interfacial friction what form losses are for wall friction
. System codes are not predictive for form losses and for CCFL since the user
must know the solution which depends on the actual geometry and representative
experiments are necessary to establish the adequate flooding correlations. Data are
plotted as in Fig. 11.24 to determine the values of C and M and the flooding correlation
is determined. Then it is translated into a drift flux model or an interfacial
friction correlation. Using such drift flux or interfacial friction correlations in
system codes make them capable to predict the correct flooding limit. Many experimental
programs were devoted to the determination of the flooding limits in
various reactor components to determine the flooding correlation as illustrated in
Fig. 11.24.
11.13
Upscaling capabilities of system codes
The reactor safety demonstration requires the analysis of complex problems related to
accident scenarios. Experiments cannot reproduce at a reasonable cost the physical
situation without any simplification or distortion and the numerical tools cannot simulate
the problem by solving the exact equations. Only reduced scale experiments are
feasible to investigate the phenomena and only approximate system of equations
may be solved to predict time and/or space averaged parameters with errors due to
imperfections of the closure laws and to numerical errors. Therefore, complex
M
C
JG
*1/2
(KG
*1/2)
JL
*1/2
(KL
*1/2)
Fig. 11.24 Determination of
CCFL and flooding curve
from experimental data.

<!-- page 705 (PDF 67) -->
methodologies are necessary to solve a problem including a PIRT analysis, a scaling
analysis, the selection of scaled IETs or combined effect tests (CET) and SETs, the
selection of a numerical simulation tool, the verification and validation of the tool,
the code application to the safety issue of interest, and the use of an uncertainty
method to determine the uncertainty of code prediction. This global approach is
illustrated in Fig. 11.25.

## 11.13.1 PIRT

Phenomena identification is the process of analyzing and subdividing a complex
SYS-TH scenario into several dominant processes or phenomena. Usually, there is
a parameter of interest in the thermal-hydraulic scenario which may be a safety criterion
(e.g., a PCT, a reactivity insertion, a thermal or mechanical load, etc.). Ranking
means here the process of establishing a hierarchy between identified processes with
regards to its influence on the parameter of interest. PIRT is a formal method
described by Wilson and Boyack (1998). When PIRT-identified dominant processes
of a reactor transient, the code should take care to model these processes with
sufficient fidelity.
PIRT
Process identification
& ranking table
Integral effect tests
Combined effect tests
Upscaling from data +UQ
Or code upscaling + UQ
Separate effect
tests
development
Code Validation & Verification
+ Uncertainty Quantification
Analysis
SCALING IET or CET
Reactor Issue Resolution
Model & code
SCALING
SCALING SET
Fig. 11.25 General methodology for solving a complex reactor thermal-hydraulic issue using
experiments, codes, and UQ methods.

<!-- page 706 (PDF 68) -->
## 11.13.2 Scaling

When dominant phenomena are identified and ranked, experiments are designed to
simulate at reduced scale and power the reactor transient in IET facilities and in
SET facilities. Scaling of an experiment is the process of selecting the nondimensional
numbers to be respected for having a good similarity with the reactor behavior at least
for the dominant processes. For application in nuclear reactor safety, a first comprehensive
scaling methodology named H2TS (“Hierarchical Two-Tiered Scaling”) was
developed by a Technical Program Group of the USNRC under the chairman Zuber
(1991).
Simulation tools are most often used to extrapolate from experiments to reactor
situation—this is the upscaling process—and the degree of confidence on this extrapolation
is part of the scaling issue. When dominant phenomena are affecting the whole
behavior of the system, a system code is necessary. This is the case of many transients
like LOCAs, SLB, LOFW, loss of electrical power, loss of residual heat removal
(LORHR), etc. When local complex 3-D phenomena are playing a dominant role,
CFD codes may be required or even a coupling of system and CFD codes.

## 11.13.3 Distortion in IET

Although IETs are designed to represent correctly dominant phenomena, distortions
exist of phenomena which may play a nonnegligible role in the transient of interest.
Let us consider an example. A classical scaling of IET used the Kv-scaling or
power-to-volume scaling where the same reduction factor λ is applied to power, volume
, and flow rate. If vertical scale is preserved, channels are thin and tall. This is not
a problem in core and SGs since one may just reduce the number of rods (resp. tubes)
and respect the hydraulic diameter, this preserves all nondimensional numbers that are
important for friction losses, heat transfers, flow regime, and interfacial transfers.
Namely,
λ = W
Wr
= V
Vr
=
_M
_Mr
Horizontal legs of a PWR should respect a Froude similarity in order to respect the
stratification criterion. This induces some distortions of Reynolds and Kutateladze
numbers:
D = λ
5Dr; L = λ
5Lr; v = λ
5vr; Re = λ
5Rer; Ku = λ
5Kur
One may expect that droplet entrainment occurrence will not be respected which plays
a significant role in a LBLOCA reflooding. Also the aspect ratio or shape of the bend
and inlet header of SG is not respected and one may expect distortions in the CCFL in
such components and this may induce a wrong liquid mass repartition in some
small-break or intermediate-break LOCAs.

<!-- page 707 (PDF 69) -->
This CCFL distortion problem can be solved by using system codes provided that
they are able to predict with the same reliability the CCFL in reactor geometry and in
IET geometry. Fig. 11.26 shows a set of experiments which were used for CATHARE
code validation. It includes CCFL tests in the same geometry as the BETHSY IET but
also reduced scale and scale 1 data in reactor geometry. This is a typical case where the
system code can solve the distortion in an IET by validation on SETs.

## 11.13.4 Code upscaling capability

Distortion may be encountered in thermal-hydraulic codes due to some simplifying
assumptions which are not satisfied in all conditions of interest. The two-fluid model
is used in most system codes and it has extended capabilities to model correctly. However
, some situations have countercurrent of droplets and liquid films which may not
be predicted with only one liquid velocity. Many other limitations of the current
models were mentioned here above and they may induce various small distortions
to a simulated transient. In reactor safety analysis, these distortions should be taken
into account at least in the UQ. Measuring the accuracy of code predictions in many
SETs is a good way of identifying the impact of all these small distortions.
Codes which are validated on some scaled SETs and IETs may have the capability
to predict the phenomena of interest at reactor scale provided that some conditions are
satisfied. This is called the upscaling or scaling-up capabilities. Among the main
conditions to satisfy one may find:
l
The code has modeled the dominant phenomena of a transients of interest.
l
The model has been validated on scaled IETs which represent the dominant phenomena, and
the code predicts well qualitatively and quantitatively the main phenomena.
l
In the favorable case where several scaled IETs at different scales have simulated the transients
of interest, the code must predicts the scale effect or the absence of scale effect.
PWR D= 750 mm
UPTF D= 750 mm
Richter D = 203mm
D =
Saturated
BETHSY D= 118 mm
MHYRESA D= 118 & D= 75
ECTHOR D =250
MHYRESA D =350 & D=75
Fig. 11.26 SETs used in the CATHARE code validation to solve the BETHSY IET distortion
problem for CCFL and flooding limit in hot leg and SG inlet header.
