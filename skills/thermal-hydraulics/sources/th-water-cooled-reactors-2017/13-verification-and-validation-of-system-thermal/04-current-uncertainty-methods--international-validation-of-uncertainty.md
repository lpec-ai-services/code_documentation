# Current uncertainty methods — International validation of uncertainty methods — International validation of uncertainty methods … Uncertainty method study
<!-- source PDF pages 43-51 -->

<!-- page 873 (PDF 43) -->
application of this method. For a successful application it is necessary that the accuracy
of the calculations does not dramatically decrease with increasing scale of the
experimental facilities. The demonstration that accuracy improves when the dimensions
of the facility in question are increases would need a sufficiently large database
which is not fully available now.
The extension of the method to internal assessment of uncertainty CIAU can be
summarized in two parts (D’Auria and Giannotti, 2000):
(1) Consideration of plant state: Each state is characterized by the value of six relevant quantities
(i.e., a hypercube) and the value of the time since the transient start
(2) Association of an uncertainty to each plant state
In the case of a PWR the six quantities are: (a) upper plenum pressure; (b) primary
loop mass inventory (including the pressurizer); (c) steam generator secondary side
pressure; (d) cladding surface temperature at 2/3 of core active height (measured from
the bottom of the active fuel), where the maximum cladding temperature in one horizontal
core cross section is expected; (e) core power; and (f ) steam generator downcomer
collapsed liquid level. If levels are different in the various steam generators, the
largest value is considered.
A hypercube and a time interval characterize a unique plant state for the purpose of
uncertainty evaluation. All plant states are characterized by a matrix of hypercubes
and a vector of time intervals. Y defines as a generic thermal-hydraulic code output
plotted versus time. Each point of the curve is affected by a quantity uncertainty and
a time uncertainty. Owing to the uncertainty, each point may take any value within the
rectangle identified by the quantity and time uncertainties. The value of uncertainty—
corresponding to each edge of the rectangle—can be defined in probabilistic terms.
This shall satisfy the requirement of a 95% probability level acceptable to NRC staff
for comparing best estimate predictions of postulated transients with the licensing
limits in 10 CFR 50.
The basic assumption of the CIAU is that the uncertainty in code prediction is the
same for each plant state. A quantity uncertainty matrix (QUM) and a time uncertainty
vector (TUV) can be set-up by means of an uncertainty methodology, like UMAE.
Possible compensating errors of the used computer code are not taken into account
by UMAE and CIAU, and error propagation from input uncertainties through output
uncertainties is not performed and is not the purpose of that method. A high effort is
needed to provide the database for deviations between experiment and calculation
results in CIAU. That time and resource consuming process has been performed only
by University of Pisa for the codes CATHARE and RELAP5 up to now. The database
is available only there. That is the reason why this method is only used by University
of Pisa up to now.

## 13.4.3 International validation of uncertainty methods

Several international programs have been performed within OECD/CSNI in order to
apply uncertainty methods, to compare their applications by different participants and
derive conclusions and recommendations.

<!-- page 874 (PDF 44) -->
### 13.4.3.1 Uncertainty method study

International validation and comparison exercises in applying uncertainty methods
have been performed. The first was the uncertainty method study (UMS) with the
objectives:
1. To gain insights into differences between features of the methods by:
l
comparing the different methods, step by step, when applied to the same problem
l
comparing the uncertainties predicted for specified output quantities of interest
l
comparing the uncertainties predicted with measured values
l
allowing conclusions to be drawn about the suitability of methods
2. To inform those who will take decisions on conducting uncertainty analyses, for example, in
the light of licensing requirements.
The United Kingdom was given the task of leading the study. The study was performed
from May 1995 to June 1997.

#### Methods compared

The methods compared in the UMS are summarized in Table 13.6. The methods may
be divided into three groups according to their basic principles (Wickett et al., 1998):
l
The University of Pisa method, the uncertainty method based on accuracy extrapolation
(UMAE), extrapolates the accuracy of predictions from a set of integral experiments to
the reactor case or experiment being assessed, see previous Section 13.4.2.
The other methods rely on identifying uncertain models and data and quantifying and
combining the uncertainties in them. They fall into two kinds:
l
The AEA Technology method that characterizes the uncertainties by “reasonable uncertainty
ranges” and attempts to combine these ranges with a bounding analysis.
l
Methods which assign probability distributions to uncertainty ranges for uncertain input
parameters and sample the resulting probability density at random in the space defined
by the uncertainty ranges (see Section 13.4.2.2). In the UMS, the GRS, IPSN, and ENUSA
methods are of this kind. The probability used here is due to imprecise knowledge and is not
probability due to stochastic or random variability.
Chosen experiment The International Standard Problem (ISP) 26 experiment,
LSTF-SB-CL-18, was used. LSTF-SB-CL-18 is a 5% cold leg SB-LOCA experiment
conducted in the ROSA-IV Large-Scale Test Facility (LSTF). The LSTF is located at
the Tokai Research Establishment of JAERI and is a 1/48 volumetrically scaled, full
height, full pressure simulator of a Westinghouse type 3423 MWth PWR. The experiment
simulates a loss of off-site power, no high-pressure injection (HPIS), the accumulator
system initiates coolant injection into the cold legs at a pressure of 4.51 MPa,
the low pressure injection system initiates at 1.29 MPa. Thus, the experiment considers
a beyond design basis accident. Because of the ISP the experiment was already
well documented.
Although ISP 26 was an open ISP participants in the UMS have not used experimental
measurements from the test, for example, the break flow or the secondary pressure
. In the same way other experiments performed in the LSTF were not used. This

<!-- page 875 (PDF 45) -->
means not allowing the related measurements to influence the choice of input uncertainty
ranges and probability distributions of the input uncertainties. Submissions
included a written statement of the justification used for input uncertainty ranges
and distributions used and were reviewed at workshops. All other assumptions made
were listed and reviewed.
Comparison of calculated uncertainty ranges The participants were asked to
make uncertainty statements, based on their calculation results, for:
(1) Functions of time
l
Pressurizer pressure
l
Primary circuit mass inventory
l
Rod surface temperature for B18 rod (4, 4) position 8 (TW359 TWE-B18448)
(2) Point quantities
l
First peak clad temperature
l
Second peak clad temperature
l
Time of overall peak clad temperature (the higher of the two)
l
Minimum core pressure difference at DP 50 DPE300-PV
As a result of the short time scale of UMS and limited funding some of the uncertainty
ranges derived from experimental data for the calculations have been less well refined
and, as a consequence, wider than would have been the case, for example, if the
calculations were for a plant safety analysis. This affected the AEAT and ENUSA
CCFL ranges, for example.
Table 13.6 Summary of methods compared in the UMS study
Institution
Code version
Method name and type
AEA Technology, UK
RELAP5/
MOD3.2
AEAT Method. Phenomena
uncertainties selected, quantified by
ranges and combined
University of Pisa, Italy
RELAP5/MOD2
cycle 36.04,
IBM version
CATHARE 2
version 1.3U
rev 5
Uncertainty method based on
accuracy extrapolation (UMAE).
Accuracy in calculating similar
integral tests is extrapolated to plant
Gesellschaft f€ur Anlagenund
Reaktorsicherheit
(GRS), Germany
ATHLET Mod
1.1 Cycle A
GRS Method. Phenomena
uncertainties quantified by ranges
and probability distributions (PDs)
and combined
Institut de Protection et de
Suˆret⟨e Nucl⟨eaire (IPSN),
France
CATHARE 2
version 1.3U
rev 5
IPSN Method. Phenomena
uncertainties quantified by ranges
and PDs and combined
Empresa Nacional del
Uranio, SA (ENUSA),
Spain
RELAP5/MOD
3.2
ENUSA Method. Phenomena
uncertainties quantified by ranges
and PDs and combined

<!-- page 876 (PDF 46) -->
#### Functions of time

The uncertainty ranges calculated for pressurizer pressure, primary inventory, and hot
rod surface temperature for LSTF B18 rod (4, 4) at position 8 are shown in
Figs. 13.12–13.14.

#### Clad temperature ranges

The AEAT and ENUSA predictions are remarkably similar. The same code
(RELAP5), the same base input deck, and mostly the same input uncertainties were
used. However, they applied different methods, i.e., bounding (AEAT) versus statistical
treatment (ENUSA) of the uncertainties, and the numbers of the input uncertainties
are different (7 by AEAT and 25 by ENUSA).
The two applications of the Pisa (UMAE) method using different computer codes
(RELAP and CATHARE) are broadly similar. The clad temperature ranges for the
second dry-out are similar. Those ranges for the first dry-out calculated by CATHARE
gave a narrower range because the base case calculation did not predict the dry-out.
However, the UMAE still generated a successful uncertainty range for this quantity
because of the first dry-out measured on those experiments considered for accuracy
extrapolation to the LSTF experiment.
Of the probabilistic methods, IPSN gave the narrowest ranges. This is attributed to
the choice of parameters made and the parameter ranges used. An actuation of the
CCFL option in the CATHARE code (at the upper core plate and the inlet plena of
the steam generators) was needed to predict the first dry-out.
The large uncertainty ranges for clad temperature calculated by AEAT, ENUSA,
and GRS prompted discussion among the participants about the reasons for them.
InthecaseofAEATandENUSAthismaybeinpartduetounrealisticallylargeuncertainty
ranges for CCFL parameters, agreed upon in order to complete the study on time.
When AEAT discounted CCFL uncertainty completely the calculated uncertainty
range for peak clad temperature changed from 584-1142 K to 584-967 K. Another contribution
may come from the used RELAP5 version MOD 3.2, calculating higher peak
clad temperatures than MOD 2 and MOD 3.2.2, see under “follow-on activity.”
The measured maximum clad temperature during the second heat-up is well below
that of the first. In the GRS calculations, many of the 99 calculated time histories
exhibit the contrary, namely a maximum during the second heat-up. The uncertainty
of the maximum temperature during the second heat-up is about double of that during
the first. In some code runs a partial dry-out occurs due to fluid stagnation in the rod
bundle which causes an earlier second heat-up, and as a consequence, a larger increase
of the clad temperature.
The large uncertainty is striking, and the sensitivity measures indicate which
of the uncertainties are predominantly important. These sensitivities are presented
in Volume 2 of reference Wickett et al. (1998). Main contributions to uncertainty
come from the critical discharge model and the drift in the heater rod bundle.
Other contributions that are worth mentioning come from the bypass cross section
upper downcomer-upper plenum. As a consequence, improved state of knowledge
about the respective parameters would reduce the striking uncertainty of the

<!-- page 877 (PDF 47) -->
Pressure (MPa)
–100
Time (s)
AEAT
Exp
LB
UB
–100
Pressure (MPa)
Time (s)
Pisa (RELAP)
Exp
LB
UB
–100
Pressure (MPa)
Time (s)
Pisa (CATHARE)
Exp
LB
UB
Pressure (MPa)
–100
Time (s)
GRS
Exp
LB
UB
–100
Pressure (MPa)
Time (s)
IPSN
Exp
LB
UB
–100
Pressure (MPa)
Time (s)
ENUSA
Exp
LB
UB
Fig. 13.12 Uncertainty ranges and data for pressurizer pressure.
From Wickett, T., Sweet, D., Neill, A., D’Auria, F., Galassi, G., Belsito, S., Ingegneri, M., Gatta, P., Glaeser, H., Skorek, T., Hofer, E., Kloos, M.,
Chojnacki, E., Ounsy, M., Lage Perez, C., Sa´nchez Sanchis, J.I., 1998. Report of the uncertainty methods study for advanced best estimate thermal
hydraulic code applications, Volume 1 (Comparison) and Volume 2 (Report by the participating institutions). NEA/CSNI/R(97)35, Paris, France.

<!-- page 878 (PDF 48) -->
–100
Mass (kg)
Time (s)
AEAT
Exp
LB
UB
–100
Mass (kg)
Time (s)
Pisa (RELAP)
Exp
LB
UB
–100
Mass (kg)
Time (s)
Pisa (CATHARE)
Exp
LB
UB
–100
Mass (kg)
Time (s)
GRS
Exp
LB
UB
–100
Mass (kg)
Time (s)
IPSN
Exp
LB
UB
–100
Mass (kg)
Time (s)
ENUSA
Exp
LB
UB
Fig. 13.13 Uncertainty ranges and data for primary mass.
From Wickett, T., Sweet, D., Neill, A., D’Auria, F., Galassi, G., Belsito, S., Ingegneri, M., Gatta, P., Glaeser, H., Skorek, T., Hofer, E., Kloos, M.,
Chojnacki, E., Ounsy, M., Lage Perez, C., Sa´nchez Sanchis, J.I., 1998. Report of the uncertainty methods study for advanced best estimate thermal
hydraulic code applications, Volume 1 (Comparison) and Volume 2 (Report by the participating institutions). NEA/CSNI/R(97)35, Paris, France.

<!-- page 879 (PDF 49) -->
–100
Temperature (K)
Time (s)
AEAT
Exp
LB
UB
–100
Temperature (K)
Time (s)
Pisa (RELAP)
Exp
LB
UB
–100
Temperature (K)
Time (s)
Pisa (CATHARE)
Exp
LB
UB
–100
Temperature (K)
Time (s)
GRS
Exp
LB
UB
–100
Temperature (K)
Time (s)
IPSN
Exp
LB
UB
–100
Temperature (K)
Time (s)
ENUSA
Exp
LB
UB
Fig. 13.14 Uncertainty ranges and data for hot rod temperature.
From Wickett, T., Sweet, D., Neill, A., D’Auria, F., Galassi, G., Belsito, S., Ingegneri, M., Gatta, P., Glaeser, H., Skorek, T., Hofer, E., Kloos, M.,
Chojnacki, E., Ounsy, M., Lage Perez, C., Sa´nchez Sanchis, J.I., 1998. Report of the uncertainty methods study for advanced best estimate thermal
hydraulic code applications, Volume 1 (Comparison) and Volume 2 (Report by the participating institutions). NEA/CSNI/R(97)35, Paris, France.

<!-- page 880 (PDF 50) -->
computed rod surface temperature in the range of the second core heat-up most

#### effectively. UMS follow-on activity

After the closure of the UMS and after the report by Wickett et al. (1998) was issued
University of Pisa performed comparison calculations of experiment LSTF-SB-CL-18
using different versions of the RELAP 5 code, i.e., MOD 2, MOD 3.2, and MOD 3.2.2.
Mod2 was used by the University of Pisa, and MOD 3.2 by AEA Technology as well
as ENUSA in this study. It turned out that MOD 3.2 calculated a 170 K higher peak
clad temperature compared with MOD 2 and MOD 3.2.2 using the same input deck.
This may contribute to the relative high upper limit of the uncertainty ranges calculated
by AEAT and ENUSA. That explanation is also in agreement with the AEAT
peak clad temperature of 787 K at 300 s for their reference calculation using nominal
values for the input parameters, without calculating the first heat-up. The measured
second peak is 610 K at 500 s.
A new application was performed by GRS using revised probability distributions
for the most important uncertain parameters, which were identified by importance
measures in the UMS analysis, contraction coefficient of critical discharge flow
and drift in the heater rod bundle. A newer ATHLET version Mod 1.2, cycle
A was used instead of Mod 1.1, Cycle A. The result was a shorter duration of the second
heat-up and lower peak clad temperatures during the second heat-up (Fig. 13.15).
Due to these findings lower differences of uncertainty ranges by different participants
are expected.
Two-sided lower limit
–200
Cladding temperature, Level 8 (K)
Time (s)
Two-sided upper limit
Exp. min.
Exp. max.
Reference
Fig. 13.15 Revised calculated uncertainty range compared with measured minimum and
maximum values of rod clad temperature by GRS.

<!-- page 881 (PDF 51) -->
#### Conclusions and recommendations of UMS Study

Five uncertainty methods for advanced best estimate thermal hydraulic codes have
been compared. Most of the methods identify and combine input uncertainties.
Three of these, the GRS, IPSN, and ENUSA methods, use probability distributions,
and one, the AEAT method, performs a bounding analysis. One of the methods,
the University of Pisa method, is based on accuracy extrapolation from integral
experiments. To use this method, stringent criteria on the code and experimental
database must be met.
Where the predictions of the methods differ, the differences have been accounted
for in terms of the assumptions of the methods and the input data used. The calculated
ranges bound the experimental results with some exceptions. The possible causes of
these discrepancies have been identified.
Comparison between the calculations The differences between the predictions
from the methods will come from a combination of:
l
the method used
l
the underlying accuracy of the reference calculation and the modeling used
l
the completeness of the identification and selection of uncertainties
l
the conservatism of the input (e.g., uncertainty ranges, probability distributions) used
l
in the Pisa method optimization of the nodalization and possibly from the different
number of experiments investigated (5 experiments with CATHARE, 10 experiments
with RELAP)
Of these, differing degrees of conservatism of the input, particularly where data are
sparse, probably account for the major differences between the specified uncertainty
ranges. For example, critical two-phase flow data from LSTF were not used, and data
for the geometry of the LSTF orifice were not available.
The ideal is for a specified uncertainty range that fully reflects the accuracy of the
underlying modeling. The input uncertainties mainly responsible for the differences
are probably those identified as important by the sensitivity studies of the methods.
These are: choked flow and CCFL (AEAT and ENUSA) and choked flow and drift
in the heater rod bundle (GRS). Further work to refine input uncertainty ranges for
these will affect the calculated uncertainty ranges. An example performed by GRS
is presented here. It follows that it is very important how the methods are applied.
Due to these findings lower differences of uncertainty ranges by different participants
are expected in the future. In all cases appropriate knowledge, skill, experience, and
quality standards must be applied.

#### Other Conclusions of UMS

For some of the methods described here the present study was the first full application.
For all of them it constituted a pilot study that allowed a better understanding of the
basic assumptions of the method.
The information gained in the UMS about the methods described and how they can
be applied can be used to inform decisions on the conduct of uncertainty analyses, for
example, in the light of licensing requirements.
