# Current uncertainty methods — International validation of uncertainty methods — Best estimate methods-uncertainty and sensitivity evaluation (BEMUSE) programme
<!-- source PDF pages 52-63 -->

<!-- page 882 (PDF 52) -->
13.4.3.2
Best estimate methods—uncertainty and sensitivity
evaluation (BEMUSE) programme

#### Objectives of BEMUSE

The high level objectives of the work are:
–
To evaluate the practicability, quality, and reliability of best-estimate (BE) methods including
uncertainty and sensitivity evaluation in applications relevant to nuclear reactor safety
–
To develop common understanding from the use of those methods
–
To promote and facilitate their use by the regulatory bodies and the industry
Operational objectives include an assessment of the applicability of best estimate and
uncertainty and sensitivity methods to ITs and their use in reactor applications. The
justification for such an activity is that some uncertainty methods applied to BE codes
exist and are used in research organizations, by vendors, technical safety organizations
, and regulatory authorities. Over the last years, the increased use of BE codes
and uncertainty and sensitivity evaluation for design basis accident (DBA), by itself,
shows the safety significance of the proposed activity. Uncertainty methods are used
worldwide in licensing of LOCAs for power uprates of existing plants, new reactors,
and new reactor developments. End users for the results are expected to be industry,
safety authorities, and technical safety organizations.

#### Main steps of BEMUSE

The programme was divided into two main steps, each one consisting of three phases.
The first step is to perform an uncertainty and sensitivity analysis related to the LOFT
L2-5 test, and the second step is to perform the same analysis for a NPP LB-LOCA.
The program started in January 2004 and was finished in September 2010.
–
Phase 1: Presentation “a priori” of the uncertainty evaluation methodology to be used by the
participants; lead organization: IRSN, France
–
Phase 2: Reanalysis of the International Standard Problem ISP-13 exercise, posttest analysis
of the LOFT L2-5 large cold leg break test calculation; lead organization: University of Pisa,
Italy (CSNI, 2006)
–
Phase 3: Uncertainty evaluation of the L2-5 test calculations, first conclusions on the
methods and suggestions for improvement; lead organization: CEA, France (CSNI, 2007)
–
Phase 4: Best-estimate analysis of a NPP-LBLOCA; lead organization: UPC Barcelona,
Spain (CSNI, 2008)
–
Phase 5: Sensitivity analysis and uncertainty evaluation for the NPP LB-LOCA, with or
without methodology improvements resulting from phase 3; lead organization: UPC
Barcelona, Spain (CSNI, 2009)
–
Phase 6: Status report on the area, classification of the methods, conclusions and recommendations
; lead organization: GRS, Germany (CSNI, 2011)
The participants of the different phases of the programme and the used computer
codes are given in Table 13.7.

#### Used methods

Two classes of uncertainty methods were applied. One propagates “input
uncertainties,” and the other one extrapolates “output uncertainties.”

<!-- page 883 (PDF 53) -->
The main characteristics of the statistical methods based upon the propagation of
input uncertainties is to assign probability distributions for these input uncertainties,
and sample out of these distributions values for each code calculation to be performed.
The number of code calculations is independent of the number of input uncertainties
but is only dependent on the defined probability content (percentile) and confidence
level. The number of calculations is given by Wilks’ formula (see Section 13.4.2.2).
By performing code calculations using variations of the values of the uncertain input
parameters, and consequently calculating results dependent on these variations, the
uncertainties are propagated in the calculations up to the results. Uncertainties are
due to imprecise knowledge and the approximations of the computer codes simulating
thermal-hydraulic physical behavior.
The methods based upon extrapolation of output uncertainties need available
relevant experimental data and extrapolate the differences between code calculations
and experimental data at different reactor scales (see Section 13.4.2.3). The main
difference of this method compared with statistical methods is that there is no need
Table 13.7 BEMUSE participants and used codes
No.
Organization
Country
Code
Participation in
phases
AEKI
Hungary
ATHLET 2.0A
1, 2, 4, 5
CEA
France
CATHARE2
V2.5_1
1, 2, 3, 4, 5
EDO
“Gidropress”
Russia
TECH-M-97
2, 4, 5
GRS
Germany
ATHLET
1.2C/2.1B
1, 2, 3, 4, 5
IRSN
France
CATHARE2
V2.5_1
1, 2, 3, 4, 5
JNES
Japan
TRACE ver4.05
1, 2, 3, 4, 5
KAERI
South Korea
MARS 2.3/3.1
2, 3, 4, 5
KINS
South Korea
RELAP5 mod3.3
1, 2, 3, 4, 5
NRI-1
Czech
Republic
RELAP5 mod3.3
2, 3, 4, 5
NRI-2
Czech
Republic
ATHLET
2.0A/2.1A
1, 2, 3, 5
PSI
Switzerland
TRACE v4.05
5rc3
1, 2, 3, 4, 5
UNIPI-1
Italy
RELAP5 mod3.2
1, 2, 3, 4, 5
UNIPI-2
Italy
CATHARE2
V2.5_1
4, 5
UPC
Spain
RELAP5 mod3.3
2, 3, 4, 5
From CSNI, 2011. BEMUSE phase VI report, status report on the area, classification of the methods, conclusions and
recommendations. NEA/CSNI/R(2011)4, Paris, France.

<!-- page 884 (PDF 54) -->
to select a reasonable number of uncertain input parameters and provide uncertainty
ranges (or distribution functions) for each of these variables. The determination
of uncertainty is only on the level of calculation results due to the extrapolation of
deviations between measured data and calculation results.
The two principles have advantages and drawbacks. The first method propagating
input uncertainties is associated with order statistics. The method needs to select a
reasonable number of variables and associated range of variations and possibly
distribution functions for each one. Selection of parameters and their distribution must
be justified. Uncertainty propagation occurs through calculations of the code under
investigation. The “extrapolation on the outputs” method needs to have “relevant
experimental data” available to derive uncertainties. The sources of deviation between
calculation and data cannot be derived by this method. The method seeks to avoid
engineering judgment as much as possible.
In BEMUSE, the majority of participants used the statistical approach, associated
with Wilks’ formula. Only University of Pisa used its method extrapolating output
uncertainties. This method is called the CIAU method, Code with (the capability
of ) Internal Assessment of Uncertainty. The reason why other participants do not
use this method is the high effort needed to get the database for deviations between
experiment and calculation results in CIAU. That time and resource consuming
process has been performed only by University Pisa for the codes CATHARE and
RELAP5 for the time being. The database is available only there.

#### Selected results

Application to LOFT L2-5 experiment Based on procedures developed at University
of Pisa, a systematic qualitative and quantitative accuracy evaluation of
the code results have been applied to the calculations performed by the participants
for LOFT test L2-5 in BEMUSE phase 2. The test simulated a 2%□100% cold leg
break. LOFT was an experimental facility with nuclear core. A FFTBM was performed
to quantify the deviations between code predictions and measured experimental
data (CSNI, 2006). Participants carefully pursued the proposed criteria for
qualitative and quantitative evaluation at different steps in the process of code
assessment during the development of the nodalization, the evaluation of the
steady-state results, and the measured and calculated time trends. All participants
fulfilled the criteria with regard to agreement of geometry data and calculated
steady-state values.
The results of uncertainty bands for the four single-valued output parameters first
PCT, second PCT, time of accumulator injection, and time of complete quenching for
the calculations of the LOFT L2-5 test are presented in Fig. 13.16 (CSNI, 2007). It was
agreed to submit the 5/95 and 95/95 estimations of the one-sided tolerance limits, that
is, to determine both tolerance limits with a 95% confidence level each. They are
ranked by increasing band width. It was up to the participants to select their uncertain
input parameters.

<!-- page 885 (PDF 55) -->
1st PCT: uncertainty bounds ranked by increasing band width
GRS
PSI
UPC UNIPI NRI-2 NRI-1 CEA IRSN KAERI KINS
Organisation name
Temperature (K)
Lower uncertainty bound
Reference
Upper uncertainty bound
Experiment
2nd PCT: uncertainty bounds ranked by increasing band width
PSI
GRS UPC NRI-1 IRSN UNIPI NRI-2 KINS CEA KAERI
Organisation name
Temperature (K)
Lower uncertainty bound
Reference
Upper uncertainty bound
Experiment
Time of accumulator injection: uncertainty bounds ranked
by increasing band width
KINS
PSI
IRSN CEA GRS KAERI NRI-1 UPC NRI-2 UNIPI
Organisation name
Time (s)
Lower uncertainty bound
Reference
Upper uncertainty bound
Experiment
Time of complete quenching: uncertainty bounds ranked
by increasing band width
UPC
PSI NRI-2 NRI-1 UNIPI GRS KAERI CEA KINS IRSN
Organisation name
Time (s)
Lower uncertainty bound
Reference
Upper uncertainty bound
Experiment
Fig. 13.16 Uncertainty analysis results of LOFT L2-5 test calculations for four single-valued output parameters, first PCT, second PCT, time of
accumulator injection and time of complete quenching compared with experimental data.
From CSNI, 2007. BEMUSE phase III report, uncertainty and sensitivity analysis of the LOFT L2-5 test. NEA/CSNI/R(2007)4, Paris, France; CSNI,
2011. BEMUSE phase VI report, status report on the area, classification of the methods, conclusions and recommendations. NEA/CSNI/R(2011)4,
Paris, France.

<!-- page 886 (PDF 56) -->
The following observations can be made:
l
First PCT: The spread of the uncertainty bands is within 138-471 K. The difference among
the upper 95%/95% uncertainty bounds, which is important to compare with the regulatory
acceptance criterion, is up to 150 K and all but one participant cover the experimental value.
One participant (UPC) does not envelop the experimental PCT due to a too high lower
bound. Two reasons can explain this result: Among all the participants, on the one hand,
UPC has the highest reference value; on the other hand, its band width is among the
narrowest ones. KINS attribute their low lower uncertainty bound to a too high value of
maximum gap conductance of the fuel rod.
l
Second PCT: In this case, one participant (PSI) does not envelop the experimental PCT,
due to a too low upper bound. The reasons are roughly similar to those given for the first
PCT: PSI, as several participants, calculates a too low reference value but has also the
specificity to consider an extremely narrow upper uncertainty band. The spread of the
uncertainty bands is within 127–599 K. The difference among the upper 95%/95% uncertainty
bounds, which is important to compare with the regulatory acceptance criterion, is up
to 200 K.
l
Time of accumulator injection: Four participants among 10 calculate too low upper bounds
(KINS, PSI, KAERI, and UPC), whereas CEA finds an upper bound just equal to the experimental
value. These results are in relationship with the prediction of the cold leg pressure
reaching the accumulator pressure 4.29 MPa. The band widths vary within the range
0.7–5.1 s for all the participants except for UNIPI which finds a much larger band, equal
to 15.5 s. This is mainly due to the consideration of time error for the pressure transient
calculated by UNIPI.
l
Time of complete quenching: All the uncertainty bands envelop the experimental value,
even if the upper bound is close to the experimental value for one participant. The width
of the uncertainty range varies from 10 s to more than 78 s. If the core is not yet quenched
at the end of the calculation as it is the case for two participants (KAERI, KINS), or if there
are several code failures before the complete quenching (IRSN), the upper bound is plotted at
120 s in Fig. 13.16.
First suggestions for improvement of the methods have not been proposed as result of
the exercise; however, recommendations for proper application of the statistical
method were given, see under “Conclusions and recommendations of BEMUSE
programme.”
Application to Zion NPP The scope of phase 4 was the simulation of a LB-LOCA
in a NPP using experience gained in phase 2. Reference calculation results were
the basis for uncertainty evaluation, to be performed in the next phase. The
objectives of the activity are (1) to simulate a LB-LOCA reproducing the phenomena
associated to the scenario and (2) to have a common, well-known basis for the future
comparison of uncertainty evaluation results among different methodologies and
codes (CSNI, 2008).
The activity for the Zion NPP was similar to the previous phase 2 for the LOFT
experiment. The UPC team together with UNIPI provided the database for the plant,
including RELAP5 and TRACE input decks. Geometrical data, material properties,
pump information, steady-state values, initial and boundary conditions, as well as
sequence of events were provided. The nodalization comprised generally more
hydraulic nodes and axial nodes in the core compared with the LOFT applications.

<!-- page 887 (PDF 57) -->
Results of reference calculations The base case or reference calculations are the
basis for the uncertainty evaluation. The calculated maximum cladding temperatures
versus time shows Fig. 13.17. The highest difference in calculated maximum PCTs
between the participants is 167 K (EDO “Gidropress”: 1326 K, KAERI: 1159 K),
what is lower than the difference of BEMUSE phase 2 calculations of the LOFT test.
Single parameter sensitivity A list of sensitivity calculations was proposed by
UPC and performed by the participants to study the influence of different parameters,
such as material properties, initial and boundary conditions upon the influence of
relevant output parameters in the scenario under investigation, i.e., a LB-LOCA of
a cold leg (CSNI, 2008).
Fig. 13.18 contains values for difference in PCT as well as calculated difference
in reflood time ΔtReflood, what is meant as difference in total quench time, for the
minimum and maximum values of the input parameter range. This shows the highest
difference in calculated cladding temperature using the same variation in maximum
linear power of □7.6% of the nominal value. The differences are up to 100 K, mainly
between different codes with the exception of UPC using RELAP5 mod 3.3.

#### Results of uncertainty analysis

Phase 5 dealt with a power plant (CSNI, 2009) like phase 4. There was no available
documentation concerning the uncertainties of the state of the plant, initial and boundary
conditions, fuel properties, etc. To solve this situation, it was agreed to provide
–25
100 125 150 175 200 225 250 275 300 325 350 375 400 425 450 475 500 525 550 575 600
Temperature (K)
Time (s)
CEA (CATHARE V2.5_1 mod6.1
EDO (Tech-M-97)
GRS (ATHLET 2.1A)
IRSN (CATHARE V2.5_1 mod6.1)
JNES (TRACE ver4.05)
KAERI (MARS)
KINS (RELAP5/MOD3.3)
NRI-1 (RELAP5/MOD3.3)
PSI (TRACEv5.0rc3)
UNIPI-1 (RELAP5/MOD3.3)
UNIPI-2 (CATHARE V2.5_1)
UPC (RELAP5/MOD3.3)
AEKI (ATHLET 2.0A)
Fig. 13.17 Calculated maximum cladding temperature versus time for the Zion NPP.
From CSNI, 2008. BEMUSE phase IV report, simulation of a LB-LOCA in Zion nuclear power
plant. NEA/CSNI/R(2008)6, Paris, France; CSNI, 2011. BEMUSE phase VI report, status
report on the area, classification of the methods, conclusions and recommendations. NEA/
CSNI/R(2011)4, Paris, France.

<!-- page 888 (PDF 58) -->
common information about geometry, core power distribution, and modeling. In addition
, a list of common input parameters with its uncertainty was prepared. This was
done due to the results of phase 3, calculating the LOFT experiment, showing quite a
significant dispersion of the uncertainty ranges by the different participants. The CEA,
GRS, and UPC teams prepared this list of common uncertain input parameters
with their distribution type and range for the NPP. These parameters were strongly
recommended to be used in the uncertainty analysis when a statistical approach
was followed. Not all participants used all proposed parameters. On the other hand,
some considered only these given parameters without any model uncertainty. The list
is shown in Table 13.8.
Themainresultsofthecalculateduncertaintybandscanbeseenforthesingle-valued
code results maximum PCT in Fig. 13.19. This temperature is defined as the maximum
fuel cladding temperature value, independently of the axial or radial location in the
active core during the whole transient. It is the main parameter to be compared with
its regulatory acceptance limit in LOCA licensing analyses. For comparison purposes
it was agreed to submit the 5%/95% and 95%/95% estimations of the one-sided tolerance
limits, that is, to determine both tolerance limits with a 95% confidence level each.
Comparing results for the maximum PCT, there is an overlap region of 17 K
(i.e., between 1221 and 1238 K). This region is very small. EDO, JNES, and PSI
considered only the proposed common input parameters from Table 13.8 without
model uncertainties.
ΔPCT (K) and ΔtReflood (s)
ΔPCT (Ir)
ΔPCT (ur)
ΔtReflood (Ir)
ΔtReflood (ur)
ΔPCT = 60 K
ΔPCT = 103K
–50
–100
–150
CEA
EDO
GRS
IRSN
JNES
KAERI
KINS
NRI-1
PSI
UNIPI-1
UNIPI-2
UPC
Fig. 13.18 Largest effect of same variation of maximum linear power by □7.6% on differences
of participant’s calculated PCT and ΔtReflood for NPP Zion.
From CSNI, 2011. BEMUSE phase VI report, status report on the area, classification of the
methods, conclusions and recommendations. NEA/CSNI/R(2011)4, Paris, France.

<!-- page 889 (PDF 59) -->
Table 13.8 Common input parameters associated with a specific
uncertainty, range of variation, and type of probability density
function
Phenomenon
Parameter
Imposed range
of variation
Type of pdf
Comments
Flow rate at
the break
Containment
pressure
[0.85, 1.15]
Uniform
Multiplier
Fuel thermal
behavior
Initial core
power
[0.98; 1.02]
Normal
Multiplier
affecting both
nominal power
and the power
after scram
Peaking factor
(power of the
hot rod)
[0.95; 1.05]
Normal
Multiplier
Hot gap size
(whole core
except hot
rod)
[0.8; 1.2]
Normal
Multiplier.
Includes
uncertainty on
gap and
cladding
conductivities
Hot gap size
(hot rod)
[0.8; 1.2]
Normal
Multiplier.
Includes
uncertainty on
gap and
cladding
conductivities
Power after
scram
[0.92; 1.08]
Normal
Multiplier
UO2
conductivity
[0.9, 1.1]
(Tfuel <2000 K)
[0.8,1.2]
(Tfuel >2000 K)
Normal
Multiplier.
Uncertainty
depends on
temperature
UO2 specific
heat
[0.98, 1.02]
(Tfuel <1800 K)
[0.87,1.13]
(Tfuel >1800 K)
Normal
Multiplier.
Uncertainty
depends on
temperature
Pump
behavior
Rotation speed
after break for
intact loops
[0.98; 1.02]
Normal
Multiplier
Rotation speed
after break for
broken loop
[0.9; 1.1]
Normal
Multiplier
Continued

<!-- page 890 (PDF 60) -->
Table 13.8 Continued
Phenomenon
Parameter
Imposed range
of variation
Type of pdf
Comments
Data related
to injections
Initial
accumulator
pressure
[□0.2;
+0.2] MPa
Normal
Friction form
loss in the
accumulator
line
[0.5; 2.0]
Log-normal
Multiplier
Accumulators
initial liquid
temperature
[□10; +10] °C
Normal
Flow
characteristic
of LPIS
[0.95; 1.05]
Normal
Multiplier
Pressurizer
Initial level
[□10; +10] cm
Normal
Initial pressure
[□0.1; +0.1] MPa
Normal
Friction form
loss in the
surge line
[0.5; 2]
Log-normal
Multiplier
Initial
conditions:
primary
system
Initial intact
loop mass
flow rate
[0.96; 1.04]
Normal
Multiplier. This
parameter can
be changed
through the
pump speed or
through pressure
losses in the
system
Initial intact
loop cold leg
temperature
[□2; +2] K
Normal
This parameter
can be changed
through the
secondary
pressure, heat
transfer
coefficient, or
area in the
U-tubes
Initial
upper-head
mean
temperature
[Tcold;
Tcold+10 K]
Uniform
This parameter
refers to the
“mean
temperature” of
the volumes of
the upper
plenum
From CSNI, 2009. BEMUSE phase V report, uncertainty and sensitivity analysis of a LB-LOCA in Zion nuclear power
plant. NEA/CSNI/R(2009)13, Paris, France; CSNI, 2011. BEMUSE phase VI report, status report on the area,
classification of the methods, conclusions and recommendations. NEA/CSNI/R(2011)4, Paris, France.

<!-- page 891 (PDF 61) -->
#### Results of sensitivity analysis

Sensitivity analysis is here a statistical procedure to determine the influence of uncertain
input parameters on the uncertainty of the output parameter (result of code
calculations). Each participant using the statistical approach provided a table of the
most relevant parameters for four single-valued output parameters and two time trends
(maximum cladding temperature and upper-plenum pressure), based on their influence
measures. To synthesize and compare the results of these influences, they are
grouped in two main “macro” responses. The macro response for core cladding
temperature comprise first, second, and maximum PCT, maximum cladding temperature
as function of time before quenching and time of complete core quenching. The
summary of the total ranking by participants is shown in Fig. 13.20. Such information
is useful for further uncertainty analysis of a LB-LOCA. High ranked parameters are
fuel pellet heat conductivity, containment pressure, power after scram, critical heat
flux, and film boiling heat transfer.

#### Conclusions and recommendations of BEMUSE programme

The methods used in this activity are considered to be mature for application, including
licensing processes. Differences are observed in the application of the methods,
consequently results of uncertainty analysis of the same task lead to different results.
These differences raise concerns about the validity of the results obtained when applying
uncertainty methods to system analysis codes. The differences may stem from the
application of different codes and uncertainty methods. In addition, differences
between applications of statistical methods may mainly be due to different input
JNES
NRI1 KAERI
PSI
GRS
EDO UNIPI2 CEA
KINS
UPC
IRSN UNIPI1 AEKI
NRI2
Participant
Temperature (K)
Lower limit 5/95
Reference case
Upper limit 95/95
Fig. 13.19 Calculated uncertainty bands of the maximum PCT of Zion NPP LB-LOCA.
From CSNI, 2009. BEMUSE phase V report, uncertainty and sensitivity analysis of a
LB-LOCA in Zion nuclear power plant. NEA/CSNI/R(2009)13, Paris, France; CSNI, 2011.
BEMUSE phase VI report, status report on the area, classification of the methods, conclusions
and recommendations. NEA/CSNI/R(2011)4, Paris, France.

<!-- page 892 (PDF 62) -->
Form loss coef. (BCL)
Two-Phase multiplier of pressure drop in
Liquid-wall friction
Heat transfer flashing
Break discharge coefficient
Initial core power
Peaking factor
Hot gap size (whole core except rod #5)
Hot gap size (hot rod #5)
Power after scram
UO2 conductivity
UO2 specific heat
Containment pressure
Pump rotational speed (IL)
Pump rotational speed (BL)
Complex of heat transfer models: heat
Forced convection to liquid
Nucleate boiling
Forced convection to vapour
Film boiling
Transition boiling
Critical heat flux
*Blowdown: interfacial friction (ILHL, UP and
*Refill and reflood: Interfacial friction in
*Refill and reflood: Steen-Wallis velocity for
Interfacial friction downstream QF
Interfacial shear in non-dispersed vertical
Interfacial shear in non-dispersed vertical
Velocity of transition from non-dispersed to
Critical velocity of transition from non-
Interfacial friction for annular flows
Alternative models – two-Phase flow
Alternative models: liquid entrainment model
Interfacial friction in bubbly-slug flow (DWR)
Interfacial shear in stratified and wavy
Interfacial shear in dispersed horizontal
CCFL in the upper core plate: c of Wallis
Direct condensation
Liquid-interface heat transfer: turbulences
Number of droplets per unit volume
Accumulator:pressure
Accumulator line form loss coefficient
Accumulator: liquid temperature
LPIS: Flow characteristic of liquid injection
Pressurizer initial pressure
Bubbles rise velocity
Fluid-wall heat transfer (2D conduction near
Rewetted side HTC: lower QF
Interfacial friction (core, upstream from the
Global HTC (core, downstream from the
Initial intact loop mass flow rate
Initial intact loop cold leg temperature
Initial upper header mean temperature
Parameter
Total ranking
Fig. 13.20 Total ranking of the influence of input uncertainties on cladding temperature per uncertain input parameter for Zion NPP LB-LOCA.
From CSNI, 2009. BEMUSE phase V report, uncertainty and sensitivity analysis of a LB-LOCA in Zion nuclear power plant. NEA/CSNI/R(2009)13,
Paris, France; CSNI, 2011. BEMUSE phase VI report, status report on the area, classification of the methods, conclusions and recommendations. NEA/
CSNI/R(2011)4, Paris, France.

<!-- page 893 (PDF 63) -->
uncertainties, their ranges, and distributions. Differences between CIAU applications
may stem from different data bases used for the analysis. However, as it was shown by
all BEMUSE phases from 2 to 5, significant differences were observed between the
base or reference calculation results. Furthermore, differences were seen in the results
using the same values of single input parameter variations (e.g., in BEMUSE phase 4,
see Fig. 13.18).
When a conservative safety analysis method is used, it is claimed that all uncertainties
are bounded by conservative assumptions. Differences in calculation results
of conservative codes would also be seen, due to the user effect, such as different
nodalization and code options, like for best estimate codes used in the BEMUSE
programme. Difference of code calculation results have been observed for a long time
and have been experienced in all International Standard Problems where different participants
calculated the same experiment or a reactor event. The main reason is that the
user of a computer code has a big influence on how a code is used. The objective of an
uncertainty analysis is to quantify the uncertainties of a code result. An uncertainty
analysis may not compensate for code deficiencies. Necessary precondition is that
the code is suitable to calculate the scenario under investigation.
Consequently, before performing uncertainty analysis, one should concentrate
first of all on the reference calculation. Its quality is decisive for the quality of
the uncertainty analysis. More lessons were learnt from the BEMUSE results.
These are:
–
The number of code runs, which may be increased to 150–200 instead of the 59 code runs
needed when using Wilks’ formula at the first order for the estimation of a one-sided
95%/95% limit tolerance. More precise results are obtained, what is especially advisable
if the upper tolerance limit approaches regulatory acceptance criteria (e.g., 1200°C PCT).
–
For a proper use of Wilks’ formula, the sampling of the input parameters should be of type
simple random sampling (SRS). Other types of parameter selection procedures like
“Latin-Hypercube-Sampling” or “Importance-Sampling” may therefore not be appropriate
for tolerance limits.
–
Another important point is that all the code runs should be successful. At a pinch, if a number
of code runs fail, the number of code runs should be increased so that applying Wilks’
formula is still possible. That is the case supposing that the failed code runs correspond to
the highest values of the output (e.g., PCT).
In addition to the above recommendations, the most outstanding outcome of the
BEMUSE programme is that a user effect can also be seen in applications of uncertainty
methods, like in the application of computer codes. In uncertainty analysis, the
emphasis is on the quantification of a lack of precise knowledge by defining appropriate
uncertainty ranges of input parameters, which could not be achieved in all cases
in BEMUSE. For example, some participants specified too narrow uncertainty ranges
for important input uncertainties based on expert judgment, and not on sufficient code
validation experience. Therefore, skill, experience, and knowledge of the users about
the applied suitable computer code as well as the used uncertainty method are important
for the quality of the results.
Using a statistical method, it is very important to include influential parameters
and provide distributions of uncertain input parameters, mainly their ranges. These
