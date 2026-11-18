# Scaling of thermal-hydraulic phenomena and relation to system code validation
<!-- source PDF pages 18-33 -->

<!-- page 848 (PDF 18) -->
## 13.2.3 Conclusions

Verification and validation of a computer code are important activities to assure its
quality. On the other hand, performing validation calculations is a very good exercise
for the users of a code to improve the understanding and handling of the code to set-up
the input data.
The results of a systematic code validation are an important basis to determine the
uncertainty of the results obtained by a code calculation. In assessing the uncertainty
of a code, user effects should be minimized. Different methods are appropriate for
assessing the uncertainty of the results from the validation by comparing calculation
results with experimental data. Dependent on the methods used for evaluating the
uncertainty, differences between calculation and experimental results are used
directly, or uncertainty ranges and distributions of relevant model parameters are
derived (see Section 13.4).
13.3
Scaling of thermal-hydraulic phenomena and
relation to system code validation
In the last five decades, large efforts have been undertaken to provide reliable
thermal-hydraulic system codes for the analyses of transients and accidents in NPPs.
Many SETs and integral system tests were carried out to establish a database for code
development and code validation. In this context, the question has to be answered, to
what extent the results of downscaled test facilities represent the thermal-hydraulic
behavior expected in a full-scale nuclear reactor under accident conditions. Scaling
principles, developed by many scientists and engineers, present a scientific-technical
basis and give a valuable orientation for the design of test facilities. However, it is
impossible for a downscaled facility to reproduce all physical phenomena in the
correct temporal sequence and the kind and strength of their occurrence. The designer
needs to optimize a downscaled facility for the processes of primary interest. This leads
compulsorily to scaling distortions of other processes with less importance. Due to
distortions, phenomena may dominate small-scale facility behavior, but these may
be less important for large-scale tests. For example, due to different surface to volume
ratio the heat losses and wall effects are higher in small-scale facilities. Therefore, the
computer code to be applied for safety analyses is the necessary and important tool to
scale physical phenomena. Consequently, a goal-oriented code validation strategy is
required, based on the analyses of SETs and integral system tests as well as transients
occurred in full-scale nuclear reactors. The CSNI validation matrices and international
experimental programs are an excellent basis for fulfilling this task. SETs in full scale,
like on the upper plenum test facility (UPTF) test facility, have here an important role.
Because a full-scale IT including physical interactions over the whole coolant
system of a NPP is usually impossible, the scaling of the test facilities becomes a
fundamental issue. The question of scaling has to be considered not only in the design
of the test facilities;ithas alsoto be taken into account in thecode development process.

<!-- page 849 (PDF 19) -->
The codes must describe the results from SETs and integral system tests of different
scale (for example, volume scaling of integral system tests range from 1:48 to 1:2070).
Whenacodemodeldescribing,forexample,thecounter-currentflowinthedowncomer
of a PWR, was development mainly on the basis of results of the 1:1 scaled UPTF
separate effects experiments must also describe this phenomenon in down-scaled integral
system tests (scale-down capability). For the full range of transients and accidents,
the interactions of the code models can be checked only on the results of down-scaled
integral system test facilities. On the other hand, code models developed mainly based
on the results of down-scaled experiments, must describe the thermal-hydraulic
processes expected in the full-scale reactor plant (scale-up capability).

## 13.3.1 Scaling concepts

Thetransferofexperimentalresults—obtainedinascaled-downtestfacility—toreality
in a large-scale industrial plant is a common challenge of engineering. A sufficient
similarity of parameters is needed controlling the processes in the test rig and the
real plant. This similarity can be geometric, mechanic, thermal-hydraulic, static,
or dynamic.
Several methods have been proposed to develop scaling laws. One of the most
known methods is based on the nondimensional form of the governing differential
equations describing the thermal-hydraulic processes. In this method the differential
equations are made nondimensional by choosing proper reference values for various
physical quantities in the equations. From these equations nondimensional numbers,
respectively, similarity groups can be obtained. For example, the derivation of the
nondimensional Reynolds and Grashof numbers is the simplest case, namely for
the steady-state single-phase flow (Glaeser and Wolfert, 2012).
Compared with this simple example for a single-phase flow the development of
scaling laws for two-phase processes is much more complicated. Not only the number
of differential equations but also the high number of constitutive equations describing
the interfacial interactions and the interactions of the two phases with the channel wall
hamper enormously the derivation of scaling laws. Some examples of scaling laws
used for the design of integral system tests facilities and SETs facilities can be found
in Glaeser and Wolfert (2012).
To obtain information about the overall system behavior and about the interaction
of the different system components of a nuclear steam-supply system, integral
system tests have been performed for more than four decades. However, because
a full-scale ITF is usually not feasible, the facility scaling becomes a
fundamental issue.
The Nahavandi scaling principle is most popular for LOCA test facilities
(Nahavandi et al., 1979, see Table 13.1). Ishii and Kataoka (1983) have presented
similarity groups for two-phase flow, which can be obtained from the set of balance
equations directly or the perturbation analyses. Similarity between test facility and
prototype is assumed if these dimensionless numbers are identical for facility and
prototype. Two typical similarity groups are shown below for illustration, where g

<!-- page 850 (PDF 20) -->
is gravitational acceleration, H is enthalpy, ρ is density, u is flow velocity, and l is
characteristic length.
Subcooling number (subcooling/latent heat)
Nsub = ΔHsub
ΔHfg
Δρ
ρg
Froude number (inertia/gravity force)
NFr = u2
gl
ρ
Δρ
Similarity criteria, such as given above, cannot be fulfilled in total. Nevertheless, they
present a scientific-technical basis and give a valuable orientation for the design of
test facilities. Ishii and Kataoka (1983) presented scaling criteria specifically for
the coolant loops of PWRs under single- and two-phase natural circulation
conditions. Ishii et al. (1998) presented the Ishii scaling for the test facility PUMA,
simulating the simplified BWR by introducing scaling of geometric length.
The hierarchical two-tiered scaling (H2TS) (Zuber, 1991) creates a hierarchy
among scaling factors and scaling design. The “first tier” or top-down scaling analysis
examines synergistic effects on the system by interactions between the constituents.
A phenomena identification and ranking table (PIRT) process is applied, involving
expert judgment. The “second tier,” or bottom-up scaling analysis, provides similarity
criteria for specific processes, such as flow pattern transitions and flow-dependent
heat transfer. The focus is on developing similarity criteria to scale individual
processes of importance to system behavior as identified in the first tier. Closure
equations addressing local phenomena are considered to obtain similarity criteria.
The fractional scaling analysis (FSA) proposed by Zuber et al. (2007) considers
fractional rate of change (FRC) and fractional change metric (FCM). The first quantifies
the intensity of each transfer process (agent of change), which changes a state
variable by a fraction of its total change during a selected transient, and allows the
ranking of the agents of change. The second is representative for scaling the fractional
Table 13.1 Scaling ratios proposed by
Nahavandi et al. (1979)
Length
Time
Area
S
Volume
S
Velocity
Acceleration
Material property
Heat generation rate/volume
Power
S
S, area-model/area-prototype.

<!-- page 851 (PDF 21) -->
change of a state variable. The FCM is used for scaling the fractional change of a system
state variable, like pressure. These scaled state variable trajectories representative
for different transients show similarities that do not show up when the same variables
are represented versus time. FRC and FCM are similar to the “specific frequency” and
“time ratio” in the H2TS, respectively.
It is claimed that FSA can replace complex computer codes and to establish a
different framework for the analysis of complex scenarios. However, that obviously
overburdens this method. FSA is a scaling analysis, not a prediction tool (Wulff et al.,
2005). As stated in Wulff et al. (2005), FSA provides the quantitative hierarchy that
may supersede the widely used, but subjectively generated PIRT. FSA can be used to
compare computer code simulations by an independent analytical infrastructure
(D’Auria and Galassi, 2010).
Reyes (2015) and Reyes et al. (2015) to address the time dependency of scaling
distortion, propose a dynamical system scaling (DSS). The strategy is to convert
the transport equations to a process space through a coordinate transform and exploit
the principle of covariance to derive similarity relationships between the prototype
and model. After the transformation, the target process can be expressed in the
process-time space as a three-dimensional phase curve called geodesics. If a similarity
is established between model and prototype, these two-phase curves will overlap at
any moment of the transient. Any deviation of the process curves represents the deviation
of the scaling as a function of time. By specifying the ratios of the conserved
quantity and the process (called 2-parameter transform), the generalized framework
can be converted to a specific scaling method such as the power-to-volume scaling.
But this generalized approach provides the benefit of identifying the distortion
objectively and quantitatively at any moment of the transient.
DSS computes scaling distortion as a function of dimensionless process time via
the (flat-space) geodesic separation between the prototype and test facility geodesic
process curves. The same normalizing factor, the process action, is applied to all quantities
when computing dimensionless process time. This allows comparing the prototype
and test facility process curve trajectories throughout the entire transient which
reveals that distortion is a dynamic quantity. It may increase and/or decrease as the
responses evolve. The geodesic separation can then be integrated to yield a single
measure which accounts for all distortion present between the two facilities or
between a code calculation and experimental results. DSS can make use of a simplified
transient analysis model for optimization of an experiment over the entire duration
of a transient process (Yurko et al., 2015).
An overview about different scaling approaches for the design of thermal-hydraulic
integral test facilities (ITFs) is given in a published article of D’Auria and Galassi
(2010). The importance of system computer codes for the scaling issue is emphasized
there, too. A state-of-the art report on scaling collected extensive information on the
topic (CSNI, 2016b).
It is impossible for a down-scaled facility to reproduce all the physical phenomena
during a transient process in a real scale plant. The designer needs to optimize a
down-scaled facility for the processes of greatest interest. However, this leads compulsorily
to distortions of other processes with less importance.

<!-- page 852 (PDF 22) -->
The H2TS, FSA, and DSS aim to the design of an experimental facility. A different
objective is the scaling application of SYS TH computer codes to the process of
determining the safety of NPPs.

## 13.3.2 Integral system tests

The LOBI Programme (Riebold et al., 1984) has demonstrated the impact of test facility
scaling very impressively. The LOBI facility was volume scaled 1:712. The tests
were performed with two different gap widths of the annular-shaped downcomer.
In the first test series, a downcomer gap width of 50 mm was used what resulted in
6.3 times too large downcomer volume and therefore in a strong distortion of the mass
distribution in the scaled system. The intention was to preserve as far as possible
counter-current flow as well as hot wall-related phenomena during the refill period.
In the second test series, a downcomer of 12 mm gap width was installed. The
12 mm was chosen as a compromise between the volume-scaled downcomer
(7 mm gap width) and a downcomer which would yield the same pressure drop
due to wall friction as in the reference reactor (25 mm gap width for the scaled facility
). The influence of downcomer gap width and downcomer volume was shown by
comparing the results. Both tests simulated a double-ended cold leg break with cold
leg accumulator injection. Overall initial and boundary conditions were generally
equal or directly comparable for the two tests.
No significant influence of downcomer gap width on the SYS TH behavior
occurred during the very first blowdown period when subcooled fluid conditions
persisted in the downcomer region. However, the course of the transient was strongly
affected during the subsequent saturated blowdown and refill periods. Water evaporation
had also started in the cold regions of the system due to the depressurization
rate. The relatively higher-density fluid persisting near the core entrance and the
reestablishment of positive mass flow through the core were much more pronounced
in the case of the large downcomer where the initial liquid inventory in the downcomer
is about 3.6 times larger than in the case of the small downcomer. This in turn ensured
enhanced cooling of the heater rod bundle during the late blowdown. Therefore,
completely different conditions existed in the primary system at the time when
ECC injection from the accumulator started. Conversely, a smaller downcomer width
tended to inhibit ECC water penetration and lower plenum refill, which led to nearly
stagnation conditions in the core and relatively poor core cooling.
Extremely poor core cooling was observed in the smaller 1:1600 scale SEMI-
SCALE facility. In contrast to the results of the UPTF test facility with a geometrical
scaling of 1:1, the SEMISCALE test results have shown that penetration of ECC water
into the downcomer during cold leg ECC injection was completely prevented by
CCFL. The multidimensional flow in the annulus downcomer of a large PWR could
not be reproduced by the small tubular downcomer of the SEMISCALE facility.
No effect of cold leg ECC injection on core cooling has been observed, what was
misleading with respect to large-scale behavior.
These examples show very clearly that the thermal-hydraulic behavior of a
down-scaled ITF cannot be extrapolated directly to obtain nuclear plant behavior.

<!-- page 853 (PDF 23) -->
Although the facilities have been designed in different volume scaling, ranging from
1:2070 to 1:48 (Table 13.2), the experimental results of these facilities are not solving
the scaling problem. A combination of integral system tests with SETs in full reactor
scale is indispensable. The computer codes shall be validated to calculate integral and
separate effects experiments over the whole available scaling range in good agreement
with the data. Therefore, the SYS TH computer code is an important scaling tool to
perform safety analysis for power reactors.
Another effect of scaling of geodetic height of a test facility for passive emergency
core cooling systems (ECCS) relying on gravity was observed from the APEX test facility
. The design of the AP1000 reactor uses gravity-driven passive safety systems to provide
emergency core cooling (ECC) and containment cooling in case of an accident for
an extended period of time. The APEX test facility at Oregon State University in USA
simulates accident behavior of an AP1000 reactor plant. Height scaling of APEX is 1:4
(see Table 13.2). That is the reason for a drawback. The incontainment refuelling water
Table 13.2 PWR integral system test facilities and main
characteristics
Test facility
Country
Volume
scaling
Max. power
(MWth)
Pressure
(MPa)
LSTF
Japan
1:48
10.0a
16.0
LOFT
The United
States
1:50
50.0
15.5
BETHSY
France
1:100
3.0a
17.2
PKL
Germany
1:145
2.5a
4.5
APEX (AP1000)
The United
States
1:192
(1/4 height)
1.0a
2.76
ATLAS
(APR1400)
South Korea
1:288
(1/2 height)
1.96a
15.7
PSB-VVER
(VVER-1000)
Russia
1:300
1.5a
PACTEL
(VVER-440)
Finland
1:305
1.0a
8.0
PACTEL (EPR)
Finland
1:400
1.0a
8.0
SPES
Italy
1:430
9.0
20.0
UMCP (2 hot,
4 cold legs)
The United
States
1:500
0.2a
2.1
LOBI
EU/Italy
1:712
5.4
15.5
MIST (2 hot,
4 cold legs)
The United
States
1:840
0.34a
15.5
SEMISCALE
The United
States
1:1600
2.0
15.0
PMK-2
(VVER-440/213)
Hungary
1:2070
0.664
16.0
aFull power scaling not possible.

<!-- page 854 (PDF 24) -->
storage tank (IRWST) injection to the AP1000 reactor coolant system starts when the
pressure in the primary system is lower than the pressure in the IRWST due to its water
head. The scaling of APEX delays the IRWST injection start. NUREG-1826 report
“APEX-AP1000 Confirmatory Testing To Support AP1000 Design Certification” (nonproprietary
) (NRC, 2005a) states that the IRWST injection start occurs for:
l
AP1000 at reactor pressure 0.198 MPa (28.7 psia)=10.0 m height of liquid level in
the IRWST
l
APEX at reactor pressure 0.125 MPa (18.2 psia)=2.5 m (=¼) height of liquid level in
the IRWST
Such a delayed IRWST injection may have a negative effect on core cooling on the
APEX tests. Core-uncovery was observed in tests investigating failure of two ADS4
valves to open on the nonpressurizer side (beyond design basis accident in the United
States) in combination with either a double-ended direct vessel injection (DVI) break
or a 2 in. break at the bottom of a cold leg, for example. The explanation for the behavior
on the APEX test facility is the height scaling of the test facility: APEX has a
reduced IRWST head due to ¼-scaled height. Timing of IRWST injection would
be earlier with 1:1 height scaling.

## 13.3.3 Separate effects tests

In addition to the integral system tests, SETs are being performed for investigating
particular phenomena. There are several reasons for the importance and high value
of this test type.
First, it has been recognized that the development of individual code models often
requires some iteration, and that a model, despite well-conceived, may need refinement
as the range of applications is widened. To establish a firm need for the modification
or further development of a model it is usually necessary to compare
predictions with SETs data rather than to rely on inferences from IT comparisons.
Second, a key issue concerning the application of best estimate codes to LOCA and
transient calculations is the quantification of the uncertainties in predicting
safety-relevant parameters. Most methods for determining these uncertainties rely on
assigning uncertainties to the modeling of individual phenomena. This concept has
placed a new emphasis on SETs above that originally envisaged for model development.
The advantages of SETs are:
l
Clear boundary conditions
l
Measurement instrumentation can be focused on a particular phenomenon
l
Reduced possibility of compensating modeling errors during validation
l
More systematic evaluation of the accuracy of a code model across a wide range of conditions
up to full reactor plant scale
l
Steady state and transient observations possible
A further incentive to conduct SETs in addition to experiments carried out on integral
system test facilities is the difficulty encountered in the upscaling of predictions of
phenomena from down-scaled ITs to real plant applications. Where a phenomenon
is known to be highly scale dependent and difficult to model mechanistically, there
is a strong need for conducting SETs at full scale.

<!-- page 855 (PDF 25) -->
Only a few selected results from experiments on the 1:1 scaled UPTF can be
presented here in the following sections to show some scaling effects and differences
to observations from small-scale experiments.

### 13.3.3.1 UPTF tests

UPTF (Weiss et al., 1986, 1990; GRS, 1992, 1993) in Germany was a full-scale (1:1)
representation of the primary system of a 1300 MWe PWR with four-loop system.
It was a fluid-dynamic facility especially designed for studying multidimensional
two-phase flow effects in components of large volume like downcomer, upper
plenum, entrance region of the steam generator, and main coolant pipes. The steam
generation in the core and the entrained water flow during emergency cooling were
simulated by feeding steam and water via nozzles in the so-called core simulator.
The behavior of the steam generators was simulated by a controlled removal or feed
of steam and water from or to the steam generator simulator from outside. The
required steam was provided by a fossil fired power station.

### 13.3.3.2 Vertical heterogeneous counter-current steam-water flow in the downcomer

In order to illustrate the scaling dependence of thermal-hydraulic phenomena in the
downcomer for heterogeneous vertical steam-water counter-current flow, some results
are presented. That phenomenon is considered to be important for efficient
core cooling by the ECC systems during a LOCA when a break of a pipe of the main
coolant system occurs. The previous insight of downcomer phenomena during cold leg
ECC injection had been developed particularly based on the USNRC ECC Bypass
Programme. It contained steam-water tests which were performed at 1/30, 1/15,
2/15, and 1/5 length scale at the Battelle Columbus Laboratories and CREARE.
Steady-state CCFL tests with steam upflow and ECC water downflow as well as
transient tests involving lower plenum flashing and two-phase upflow were carried out.
Empirical flooding correlations based on experimental data of these down-scaled
test facilities have been developed, using two dimensionless phase velocities: a modified
Wallis parameter
J _X =
_MX
ρXADC
ρX
gW ρW □ρs
ð
Þ
½
·
containing W as average downcomer annulus circumference and the Kutateladze
number
K _X =
_MX
ρXADC
ρX
gσ ρW □ρs
ð
Þ
½
·
In spite of the variation of scale of the test facilities between 1/30 and 1/5, the extrapolation
to full-scale downcomer geometry was still not clear.
To provide CCFL and ECC bypass data for full reactor geometry, tests on UPTF
were carried out. The result of a UPTF experiment, simulating the downcomer

<!-- page 856 (PDF 26) -->
behavior during the end-of-blowdown and the refill phases for a large cold leg break,
is shown in Fig. 13.4.
The test was carried out at a reactor typical steam upflow of 320 kg/s and ECC
water injection (subcooling 115 K) into the three intact loops. The contour plot shows
isotherms of fluid temperatures (subcooling) in the downcomer projected in a plane.
The two-dimensional presentation shows strongly heterogeneous steam-water flow
conditions which were not observed in small-scale experiments. The ECC water delivered
from the cold legs 2 and 3, which are located opposite the broken loop connection
, penetrates the downcomer without being strongly affected by the upflowing
steam. Most of the ECC water delivered from cold leg 1, which is located close to
the broken loop, however, flows directly to the break bypassing the core.
To demonstrate the effect of the facility scaling on downcomer CCFL, the data
obtained from UPTF and CREARE with 1/5 scaling are compared in reference
(GRS, 1992; Glaeser and Wolfert, 2012). Slightly subcooled ECC water was used
in this UPTF test and saturated ECC water on CREARE. Due to the strongly heterogeneous
flow conditions in the full-scale downcomer of UPTF the water delivery
curve of UPTF is significantly higher than for CREARE.
The
main
findings
with
respect
to
downcomer
behavior
during
the
end-of-blowdown and refill phases of a large cold leg break with cold leg or downcomer
ECC injection can be summarized as follows:
–
A significant scale effect on downcomer behavior can be observed
–
Steam-water flow conditions in the downcomer are highly heterogeneous at full scale
Fluid subcooling distribution in downcomer
–6500
–6000
–5500
–5000
–4500
–4000
–3500
–3000
Height (mm)
–2500
–2000
–1500
–1000
90°
360°
270°
180°
UPTF TEST RUN 131
–2
–2
–2
–2
–2
–1
–2
–6
–6
BR
SET DOWNCOMER CCFL PROCEDURE A1 ECC=120C
Offset from DAS start: 61.40 sec
Data averaged over 0.04 sec
–500
Fig. 13.4 Counter-current flow conditions in full-scale downcomer for strongly subcooled ECC
water, distribution of subcooled temperatures.

<!-- page 857 (PDF 27) -->
–
Heterogeneous or multidimensional behavior increases water delivery rates at full-scale
relative to previous tests on down-scaled facilities
–
CCFL correlations developed from the down-scaled tests are not applicable to full-scale
downcomers
–
Downcomer CCFL correlations for cold leg ECC injection based on down-scaled test results
underpredict the water penetration to the lower plenum at full scale
–
Due to strong heterogeneous flows in a real downcomer, a CCFL correlation has to account
for the location of the ECC injection relative to the broken cold leg
In order to describe the vertical asymmetric heterogeneous gas/liquid counter-current
flow in the full-scale downcomer, the Kutateladze-type flooding equation was
extended by Glaeser (1992) correlating the local steam velocities of the multidimensional
flow field with the superficial steam velocity. A geometrical lateral
distance between the legs with ECC injection and the broken loop is introduced in
the gas upflow momentum term. This term relates the local upward gas velocity at
the water downflow locations to the superficial gas velocities. The superficial gas
velocity can be calculated from the steam mass flow rate.
K1=2
g
v2=3
g
g1=3L
!1=2
+ 0:011K1=2
l
= 0:0245
g1=3L
v2=3
g
□ 5400 L = 0:5πdoutersin2 0:5ΘECC□BCL
ð
Þ
If there is more than one ECC injection location, the arithmetic mean value of all
distances L between the ECC injection legs and the broken leg has to be used in
the correlation. However, only those injection locations can be considered where
water can flow downward. This means that the modified dimensionless gas velocity
obtained by using the value of L for the individual injection location has to be below
the onset of penetration point. Otherwise, the respective ECC injection leg cannot
be included in the arithmetic mean value L. More details of the derivation and application
of the Glaeser-correlation can be found in Glaeser (1992) and Glaeser and
Karwat (1993).
The resulting lowest gas velocity for zero water penetration (onset of penetration)
is shown in Fig. 13.5 (legend provided in Table 13.3) compared with the downcomer
circumference scale. Water downflow is impossible for gas velocities above the
curve. Three different flooding correlations are applicable for three different scaling
regions. These are the classical Wallis- and Kutateladze-type as well as the
Glaeser-correlation. The range of applicability is dependent on the dimensionless
annulus circumference, which governs the different flooding correlations. It can be
seen that it is impossible to extrapolate counter-current flow correlations from
small-scale data below one-ninth downcomer circumference scale (equivalent to
1/81 flow cross-section scale) to reactor scale. The full-scale UPTF data were needed
to clarify the influence of scaling on the ECC flooding phenomenon.

<!-- page 858 (PDF 28) -->
13.3.3.3
Calculated results for importance of downcomer
counter-current flow on maximum cladding
temperature and quench time
The downflow of ECC water injected into the cold legs or at the top of the downcomer
counter-current to steam flowing upward was considered as highly important in the
PIRTs, especially for a large break (LB) in one cold leg scenario. As described before,
3.5
10.5
Dimensionless gas velocity Kg
Downcomer circumference scale
DOWNCOMER (ONSET OF PENETRATION)
ng
2/3
g1/3L
ng
2/3
J' Correlation
K Correlation
Own Correlation
CREARE
1/30
CREARE
1/15
CREARE
1/5
Kg = 0.16 Bo1/2
Kg = 3.2
Kg = (0.0245)2
g1/3L
Bo = 400
= 5400
L =
pdouter
(q = 180°)
Bo = pdav
g(rl.rg)
s
1/15
p = 400 kPa : 0
1/9
=
Reg
2/3
Frg
1/3
g1/3L
ng
2/3
Fig. 13.5 Downcomer flooding correlation for zero penetration of liquid (total bypass).
Table 13.3 Legend for Fig. 13.5
ADC
Flow cross section of downcomer
Bo
Bond number
dav
Downcomer average diameter
douter
Downcomer outer diameter
Fr
Froude number
g
Gravity
L
Characteristic geometrical length
M
Mass flow rate
≡ECC-BCL
Angle between ECC injection leg and broken loop
ν
Kinematic viscosity
ρ
Density
σ
Surface tension
Subscripts
g
Vapor
l
Liquid

<!-- page 859 (PDF 29) -->
that phenomenon had a significant effect on the cooling of the heater rod bundles
representing the core of a reactor in small-scale experimental facilities, like SEMI-
SCALE and LOBI.
A statistical uncertainty and sensitivity analysis for a 2%□100% cold leg break on
the Zion NPP was performed using the ATHLET computer code (Glaeser et al., 2008).
Of interest here was to get information on the importance of counter-current flow in
the downcomer on the maximum cladding temperature. Such information can be
obtained
from
the
statistical
GRS-uncertainty
and
sensitivity
method,
see
Section 13.4. Validation of differently scaled experiments up to 1:1 UPTF separate
counter-current flow experiments in the downcomer was performed. The interfacial
shear multiplier was adjusted to calculate the counter-current flow in good agreement.
Interfacial shear had to be reduced significantly for UPTF experiments during nondispersed
flow in the downcomer and the core compared with small-scale experiments
in order to calculate the downflow water mass flow in agreement with the data. The
interfacial shear in the upper plenum and core region was adjusted in order to calculate
water flow coming locally via the hot legs from the steam generators and the pressurizer
. These extended ranges for interfacial shear were used for the Zion calculations.
The upper bound of the uncertainty ranges from small-scale experiments remained.
The multipliers for the downcomer derived from 1:1 scale UPTF calculations are
in the range of 0.05–3.0 for the reactor instead of 0.33–3.0 used for the 1:50 scale
LOFT experiments. The ranges for the core, tie plate, and upper plenum are
0.01–2.5 instead of 0.2–2.5 for LOFT.
Different to earlier PIRTs, it turned out, that no significant effect of downcomer
counter-current flow on the cladding temperature is to be seen in the reactor
calculation.
Fig. 13.6 shows the uncertainty band (tolerance interval) of calculated maximum
cladding temperature versus time and the time span of accumulator injection.
Maximum clad temperature (°C)
Time (s)
Two-sided lower limit
Two-sided upper limit
Reference
Accumulator injection time : from approx 12 s through 50-80 s (ref. calc. 60 s)
Fig. 13.6 Calculated uncertainty band of maximum cladding temperature of Zion reactor,
2%□100% cold leg break.

<!-- page 860 (PDF 30) -->
The importance measures are shown in Fig. 13.7 during the blowdown phase and
Fig. 13.8 during the reflood phase. The length of the bars indicate the importance,
positive sign tends to increase cladding temperature with increasing input parameter
values, and vice versa. More effect on the cladding temperature comes from the
core and tie plate counter-current flow, even more on the quench time (Fig. 13.9).
A reason may be that the time of limitation of water downflow through the
–0.3
–0.2
–0.1
0.1
0.2
0.3
0.4
0.5
Rank correlation coefficient
Index of parameter
Interfacial shear in
vertical bundle
Interfacial shear in
downcomer
Power factor hot rod
Fig. 13.7 Importance measures of 55 uncertain input parameters for maximum cladding
temperature during blowdown phase.
–0.4
–0.3
–0.2
–0.1
0.1
0.2
0.3
0.4
0.5
Rank correlation coefficient
Index of parameter
Model for
one-phase
convection
to steam
Model for
film boiling
Film boiling
Number of droplets
Interfacial shear in
vertical bundle non
dispersed flow
Interfacial shear in
downcomer
Power factor hot rod
Decay heat
Fig. 13.8 Importance measures of 55 uncertain input parameters for maximum cladding
temperature during reflood phase.

<!-- page 861 (PDF 31) -->
downcomer counter-current to significant steam upflow is relatively short during such
a LB transient in reactor scale.
13.3.3.4
Vertical counter-current flow of saturated steam and
water for homogeneous flow conditions at the upper
core tie plate and in the upper plenum
To study the counter-current flow at the upper core tie plate and the liquid hold up
above the tie plate in case of saturated steam/water upflow a series of UPTF tests
were carried out. The core simulator with controlled injection of steam and water
adjusted reactor typical steam/water upflow. Steam and entrained water upflow is
of higher relevance for counter-current flow in the reactor than steam upflow only.
This effect has not been investigated in vertical counter-current SETs prior
to UPTF.
The test results indicate that:
l
Steam/water upflow, two-phase pool above the tie plate, and water fall back through the tie
plate is uniform across the core area
l
Flooding curves for both full-scale and subscale test facilities are similar
l
Water downflow to each fuel assembly is scale-invariant
l
For homogeneous flow conditions at the tie plate the flooding curve can be defined by
applying the Kutateladze number as scaling parameter
Consequently, the effects of scaling on vertical counter-current steam-water flow
is dependent on the two-phase flow distribution, either heterogeneous or homogeneous
. Heterogeneous flows are highly scaling dependent but homogeneous
flows not.
–0.6
–0.4
–0.2
0.2
0.4
0.6
Rank correlation coefficient
Index of parameter
Model for
one-phase
convection
to steam
Rewet heat
transfer upper
quenchfront
Rewet heat
transfer lower
quenchfront
Direct
condensation
Interfacial shear in
vertical bundle
nondispersed flow
Interfacial shear in
downcomer
nondispersed
flow
Critical velocity
nondispersed to
dispersed in
vertical bundle
Initial core fluid
temperature
Decay heat
Fig. 13.9 Importance measures of 55 uncertain input parameters for quench time.

<!-- page 862 (PDF 32) -->
### 13.3.3.5 Flow conditions in the hot leg during reflux condenser mode

Heat is transferred from the core to the secondary side of the steam generators by
evaporation of water in the core and subsequent condensation of the steam in the
U-tubes of the steam generators in the reflux condenser mode. A portion of the condensate
flows back from the steam generator to the upper plenum counter-currently to
the steam through the hot leg. That condensate serves cooling the core. Due to momentum
exchange between the steam-flow and the water-flow in the hot legs flooding may
occur, which could prevent or at least deteriorate the water flow back to the core.
The Kutateladze-type equation considering instabilities of the gas-liquid interface
in horizontal counter-current flow conditions can be transferred into the Wallis-type
equation (Glaeser, 1992). This is possible for horizontal or inclined flow since the
gravity force of unstable waves and droplets act perpendicular to the main flow directions
of steam and water and counter the pressure difference between the bottom of
such a wave and the crest due to different steam velocities at the wave crest and bottom
(Glaeser and Karwat, 1993). Hence, the Wallis correlation is applicable to horizontal
counter-current flow over the whole scaling region what is different to vertical
heterogeneous counter-current flow.
The UPTF test has demonstrated that a substantial margin exists between the
flooding limit and the typical conditions expected in a PWR during reflux condenser
mode of a SB-LOCA. This is the case in a full-reactor scale hot leg (Glaeser and
Karwat, 1993; see Fig. 13.10). This steam mass flow results from a 2% core decay
power scaled from 8 to 0.3 MPa pressure of UPTF.
GRS used these full-scale UPTF test series data of counter-current flow in the hot
leg for the code development and validation of their ATHLET computer code when
they became available in the year 1984. Prior to that, the code was developed and
validated using small-scale LOBI and LOFT experiments. A new correlation for
the geometry of the horizontal tube including the inclined tube section at the steam
generator inlet was developed and validated against a variety of UPTF experiments.
For example, saturated water was supplied from the steam-generator side and, simultaneously
, saturated steam from the vessel side, i.e., from the upper plenum was supplied
in UPTF Test 11. The steam mass flow rate was increased gradually until
occurrence of the CCFL. Good correspondence for a horizontal tube with original
diameter demonstrated that the velocities of the two phases including the CCFL
are determined realistically by the new correlation.
With the new correlation, further experiments were analyzed successfully, e.g., the
depletion of the steam generator U-pipes during a small-break experiment in the LOBI
test facility. After completion of the model validation calculations, the new correlation
wasincludedintheATHLETcode.Basedonthesamefindingsthevendormadesimilar
improvements in his version of SRELAP5. Some licensing calculations were repeated
in order to find out the effect of the changed correlation in ATHLET. A medium break
size of 160 cm2 (3.6%) in the cold leg of the KONVOI plants was selected for demonstration
. It turned out that no heat-up was calculated compared with the old model due
to improved back-flow of condensate from the steam generator toward the upper
plenum to fill the core region and serve better cooling of the core (see Fig. 13.11).

<!-- page 863 (PDF 33) -->
## 13.3.4 Conclusions and future trends

Some information about scaling in nuclear reactor SYS THs is presented. Some phenomena
strongly depend on geometrical scale, like heterogeneous vertical
steam-water CCFL. The SYS TH computer code is an important scaling tool to
Steam mass flow rate for D=0.75 (kg/s)
Condensed mass flux
Ohnuki
Scaling Dfacility/Dreactor
Steam mass flux (kg/s m2)
(1 active SG)
Water delivery
Richter
UPTF Test 11
1:10
1:3
:1
Fig. 13.10 Counter-current flow limitation compared with reactor steam mass flow in the
hot leg.
Time (s)
Cladding temperature (°C)
Recent
analysis
Previous
analysis
Fig. 13.11 Application of counter-current flow results of UPTF on ATHLET calculations for
small break LOCA (160 cm2 break in cold leg of PWR 1300 MW electric) with respect to
maximum cladding temperature in the core.
