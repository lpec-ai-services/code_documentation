# Current uncertainty methods — Introduction … Common methods
<!-- source PDF pages 34-42 -->

<!-- page 864 (PDF 34) -->
perform safety analysis for power reactors. Strong connections are therefore between
scaling, code validation, setting up the nodalization and uncertainty evaluation,
as well as code user qualification and expertise.
Power and volume scaling is the dominant approach. The concept of scaling hierarchy
byZuber may be applied.Fullheightisoften used fortestfacilities. Thealternative
Ishii scaling allows to reduce the cost of an experimental facility, and to reduce the
influence of heat release from structures or the distortion due to different surface
to volume ratio on the course of a transient. However, the Ishii scaling may need
confirmation by a scaling preserving the time in order to provide confidence in the simulation
of important phenomena and the timing of sequences of an accident scenario.
The examples presented show very clearly that the thermal-hydraulic behavior of a
down-scaled ITF cannot be extrapolated directly to obtain nuclear plant behavior.
Although the ITFs have been designed in different volume scaling, ranging from
1:2070 to 1:48, the experimental results of these facilities are not solving the scaling
problem. A combination of integral system tests with separate effect tests in full reactor
scale is indispensable. The computer codes shall be validated to calculate integral
and separate effects experiments over the whole available scaling range in good agreement
with the data. Therefore, the SYS TH computer code is an important scaling tool
to perform safety analysis for power reactors.
The refinement of the thermal-hydraulic system codes, the completion of the validation
and the quantification of the uncertainties in the simulation of full size plant
accidents are tasks for the next years.
Another important effort in the analytical work will be focused on the development
of two-phase flow computational fluid dynamics (CFD) codes. Due to the high resolution
in space and the possibility for three-dimensional description of the single- and
two-phase flow phenomena the scaling issue will become less important. Parallel to
the progress in the development of the computer hardware with regard to reducing
calculation time the application area of these codes will be extended.
The development of the two-phase flow CFD codes is a great challenge for the
analytical teams in the next decades and may contribute to the motivation of young
scientists working in the field of nuclear technology.
13.4
Current uncertainty methods

## 13.4.1 Introduction

The safety analysis used to justify the design and construction of water-cooled NPPs
demonstrates that the plants are designed to respond safely to various postulated accidents
in a deterministic thermal-hydraulic safety evaluation. These postulated accidents
include LOCAs in which the pressure boundary containing the water, which
takes heat away from the reactor core, is breaking and a range of other transients
in which conditions deviate from those in normal operation.
The equations of state and heat transfer properties of water including relevant
two-phase phenomena vary very substantially over the conditions that will occur in
such accidents. These events can therefore only be simulated by computer codes.

<!-- page 865 (PDF 35) -->
Initial and boundary conditions, geometry, reactor plant operating parameters, fuel
parameters, and scale effects may not be exactly known. The models of the
thermal-hydraulic computer codes approximate the physical behavior, and the solution
methods in the codes are approximate. Therefore, the code predictions are not
exact but uncertain. Agreement of calculated results with experimental data is often
obtained by choosing specific code input options or changing parameter values in the
model equations. These selected parameter values usually have to be changed again
for different experiments in the same facility or a similar experiment in a different
facility in order to obtain agreement with data. A single “best estimate” calculation
with an advanced realistic code would give results of one code run of unknown accuracy
. To make such results useful, for example, if they are to be compared with limits
of acceptance, the uncertainty in the predictions then has to be calculated separately.
Uncertainty analysis methods therefore were developed to estimate safety margins if
best estimate codes are used to justify reactor operation. A particular stimulus was the
USNRC’s revision of its regulations in 1989 to permit the use of realistic models with
quantification of uncertainty in licensing submissions for ECCS (CFR, 1989).
In addition, uncertainty analysis can be used to assist research prioritization. It can
help to identify models that need improvement and areas where more data would be
needed. It can make code development and validation more cost-effective.
The alternative is to use conservative computer codes and/or conservative initial
and boundary conditions to introduce unquantified conservatisms to bound uncertainties
. This may lead to unrealistic results. A list of ECCS evaluation models is provided
in Appendix C of CFR (1989) to follow the conservative approach in the United
States. That approach is not part of this section dealing with uncertainty evaluation
rather than trying to bound computational results of safety parameters conservatively
toward the direction of regulatory acceptance criteria (CFR, 1989). An uncertainty
analysis quantifies the uncertainty of a result of a safety parameter, and the range
toward the acceptance criterion determines the margin. Such a procedure is not nonconservative
. It is quantifying the conservatism of a calculation result.

## 13.4.2 Common methods

Within the uncertainty methods considered, uncertainties are evaluated using either
(1) Propagation of input uncertainties: code scaling, applicability, and uncertainty (CSAU)
method and GRS (Gesellschaft f€ur Anlagen- und Reaktorsicherheit) method or
(2) Extrapolation of output uncertainties: uncertainty methodology based on accuracy extrapolation
and code with the capability of internal assessment of uncertainty (UMAE/
CIAU).
For the “propagation of input uncertainties,” uncertainty is obtained following the
identification of uncertain input parameters with specified ranges and/or probability
distributions of these parameters, and performing calculations varying these parameters
. The propagation of input uncertainties can be performed by either deterministic
or statistical methods. For the “extrapolation of output uncertainty” approach,

<!-- page 866 (PDF 36) -->
uncertainty is obtained from the output uncertainty based on comparison between calculation
results and relevant experimental data.
A short description of these methods is provided in the following sections. These
methods have been described in several publications. Detailed comprised information
on the different methods and their applications can be obtained from the IAEA Safety
Series No. 52 (IAEA, 2008).

### 13.4.2.1 CSAU method

The CSAU methodology was proposed to investigate the uncertainty of safety-related
output parameters. It supplies a complete framework to go through the whole process
of an uncertainty analysis. The output parameters in the demonstration cases of this
method were only single-valued parameters, such as PCT or minimum water inventory
, no time dependent values were provided. Prior to this, a procedure is used to
evaluate the code applicability to a selected plant scenario. Experts identify all the
relevant phenomena. Following this step, the most important phenomena are identified
and are listed, based on an examination of experimental data and code predictions
of the scenario under investigation, ranking them as highly important. In the resulting
PIRT, ranking is accomplished by expert judgment. The PIRT and code documentation
are evaluated, and it is decided whether the code is applicable to the plant scenario
. The CSAU methodology is described in detail by Boyack et al. (1990).
Demonstration applications have been performed for a LB-LOCA and a SB-LOCA
for a PWR (Boyack et al., 1990; Ortiz and Ghan, 1992).
An optimized nodalization to capture the important physical phenomena should be
used for all calculations. This nodalization represents a compromise between accuracy
and cost, based on experience obtained by analyzing SETs and integral experiments.
No particular method or criteria are prescribed for this task.
Only parameters important for the highly ranked phenomena are selected for
consideration as uncertain input parameters. The selection is based on a judgment
of their influence on the output parameters. Additional output biases are introduced
to consider the uncertainty of other parameters not included in the variation
calculations.
Information from the vendor of NPP components as well as from experiments and
previous calculations was used to define the mean value and probability distribution or
standard deviation of uncertain input parameters, for both the LB- and the SB-LOCA
analyses. Additional biases can be introduced in the output uncertainties.
Distributions values of uncertain input parameters are uniform and normal which
were used in the two applications performed for demonstration. Output uncertainty is
the result of the propagation of input uncertainties through a number of code
calculations.
A statistical method for uncertainty evaluation has not been proposed in the CSAU
but has been widely used in the past. A response surface approach was used in the
demonstration applications. The response surface fits the code predictions obtained
for selected parameters and is further used instead of the original computer code
for performing the variation calculations. Such an approach then entails the use of

<!-- page 867 (PDF 37) -->
a limited number of uncertain parameters in order to reduce the number of code runs
and the cost of analysis but was limited to results of point values, like PCT in the
demonstrations. However, within the CSAU framework the response surface
approach is not prescribed and other methods can be applied.
Scaling is considered by the CSAU, identifying several issues based on test facilities
and code assessment. The effect of scale distortions on main processes, the applicability
of the existing database to the given NPP, the scale-up capability of closure
relationships, and their applicability to the NPP range is evaluated at a qualitative
level. Biases are introduced if the scaling capability is not provided.

### 13.4.2.2 Statistical (GRS) method

The statistical method again propagates potential uncertain input parameters to uncertain
output parameters by code calculations. The main advantage to use these tools is
that the number of calculations is independent of the number of uncertain parameters
to be investigated. The number of calculations depends only on the chosen tolerance
limits or intervals of the uncertainty statements of the results. Not using these statistical
tools necessitates a drastic increase of code calculations with the number of
uncertain parameters when uncertain values of the selected input parameters have
to be combined.
Choosing combinations of parameter values at will by the expert and performing
the respective code runs does not allow to make quantitative tolerance/confidence
statements about the combined influence of the identified uncertainties. Such statements
could not be made without the tools from statistics, not even after a very large
number of code runs. It simply is a matter of efficiency to exploit what is known from
statistics in order to reach the target uncertainty coverage and confidence at minimum
cost or to extract the most of information from the expended number of runs. The features
of the statistical method are:
(1) The uncertainty space of input parameters like computer code models, initial and boundary
conditions, geometry, reactor plant operating parameters, fuel parameters, scale effects, and
solution algorithms are defined by their uncertainty ranges and probability distributions.
These are sampled at random according to the probability distributions of the uncertain
parameters. Code calculations are performed by sampled sets of parameters.
(2) The number of code calculations is determined by the requirement to estimate a tolerance
and confidence interval for the quantity of interest, such as PCT or cladding temperature
versus time. Following a proposal by GRS, Wilks’ formula (Wilks, 1941, 1942) is used
to determine the number of calculations to obtain the uncertainty bands.
(3) Statistical evaluations are performed to determine the sensitivities or importance of input
parameter uncertainties on the uncertainties of key results, i.e., parameter importance
analysis.
The smallest number n of code runs to be performed is according to Wilks’ formula
(Wilks, 1941, 1942):
1□an □ b

<!-- page 868 (PDF 38) -->
which is the size of a random sample (number of calculations) such that the maximum
calculated value in the sample is an upper statistical tolerance limit. The required number
n of code runs for the a=upper 95% fractile is 59 at the b=95% confidence level.
For two-sided statistical tolerance intervals (investigating the output parameter
distribution within an interval) the formula is:
1□an □n 1□a
ð
Þan□1 □ b
The minimum number for a 95%/95% two-sided tolerance interval is 93. The minimum
number of calculations can be found in Table 13.4.
Upper statistical tolerance limits are the upper b confidence for the chosen a fractile
. The fractile indicates the probability content of the probability distributions of the
code results (e.g., a 95% means that PCT is below the tolerance limit with at least
a=95% probability). One can be b% confident that at least a% of the combined influence
of all the characterized uncertainties is below the tolerance limit. The confidence
level is specified because the probability is not analytically determined. It accounts for
the possible influence of the sampling error due to the fact that the statements are
obtained from a random sample of limited size. The 95% probability for the uncertainty
evaluation comes from US NRC Regulatory Guide 1.157 “Best Estimate Calculations
of Emergency Core Cooling System Performance” that an acceptance
criterion has not to be exceeded with a probability of 95% or more. The same value
is stated in the IAEA Specific Safety Guide No. SSG-2 “Deterministic Safety Analysis
for Nuclear Power Plants” (IAEA, 2009). In addition it says: “Techniques may be
applied that use additional confidence levels, for example, 95% confidence levels.”
For regulatory purposes, where the margin to licensing criteria is of primary interest
, the one-sided tolerance limit may be applied, that is, for a 95th/95th percentile, a
minimum of 59 calculations should be performed.
As a consequence, the number n of code runs is independent of the number of
selected input uncertain parameters, only depending on the percentage of the fractile
and the desired confidence level percentage. The number of code runs for obtaining
sensitivity measures is also independent of the number of uncertain input parameters.
As an example, 100 runs were carried out in the analysis of a reference reactor, using
Table13.4 Minimum number of calculations n for one- and two-sided
statistical tolerance limits
One-sided statistical tolerance limit
Two-sided statistical tolerance limit
a=0.5
0.90
0.95
0.99
a=0.5
0.90
0.95
0.99
b=0.50
b=0.90
b50.95
b=0.99

<!-- page 869 (PDF 39) -->
50 parameters. More description can be found in references of Hofer (1993) and
Glaeser (2008).
The total number of (n) code runs is performed varying simultaneously the values
of all uncertain input parameters, according to their distribution. For each instant of
time the n values of the considered output parameters are ordered from the lowest to
the highest values:
Y 1
ð Þ < Y 2
ð Þ⋯< Y n□1
ð
Þ < Y n
ð Þ
That “order statistics” is used when Wilks’ formula is applied. On the basis of ordering
of the output values, the tolerance limits are obtained at a confidence level of 95% by
selecting the output values in Table 13.5.
For the selected plant transient, the method can be applied to an integral effects test
simulating the same scenario prior to the plant analysis. If experimental data are not
bounded, the set of uncertain input parameters has to be modified or ranges and distributions
changed.
Experts identify significant uncertainties to be considered in the analysis, including
the modeling uncertainties and the related parameters, and identify and quantify
dependencies between uncertain parameters if present. Probability density functions
(PDFs) are used to quantify the state of knowledge of uncertain parameters for the
specific scenario. Uncertainties of code model parameters are derived based on
validation experience. Therefore, experts performing the validation should determine
the probability distributions of model uncertainties.
The scaling effect is quantified as a model uncertainty. Additional uncertain model
parameters can be included or PDFs can be modified, accounting for results from
differently scaled SET analysis.
Input parameter values are simultaneously varied by random sampling according to
the PDFs and according to dependencies between them, if dependencies are relevant.
A set of parameters is provided to perform the required number n of code runs. For
example, the 95% fractile and 95% confidence limit of the resulting distribution of
Table 13.5 Selection of tolerance limits at the 95% confidence level
depending on number of code runs performed
Number of
code runs
(samples)
One-sided 95th
percentile
tolerance limit
One-sided 5th
percentile
tolerance limit
Two-sided 95th
percentile
tolerance interval
Y(n)
Y(1)
–
Y(n□1)
Y(2)
Y(1) and Y(n)
Y(n□2)
Y(3)
Y(1) and Y(n)
Y(n□3)
Y(4)
Y(2) and Y(n□1)
Y(n□4)
Y(5)
Y(3) and Y(n□2)

<!-- page 870 (PDF 40) -->
the selected output quantities are directly obtained from the n code results, without
assuming any specific distribution. No response surface is used.
Statistical uncertainty and sensitivity analysis provides statements on:
l
Uncertainty range of code results that enables to determine the margin between the bound of
uncertainty range closest to an acceptance criterion and the acceptance criterion. The 95%
fractile, 95% confidence limit for output parameters versus time are provided.
l
Sensitivity measures about the influence of input parameters on calculation results, i.e., a
ranking of importance versus time is provided which
□
allows a ranking of input parameters on output uncertainty as result of the analysis
instead of setting up a prior PIRT
□
guides further code development
□
prioritizes experimental investigations to obtain more detailed information
The sensitivity or importance measures give useful information about those input
parameters influencing the uncertainty of computer code results most. That information
can be used to find out which ranges and distributions of input uncertainties
should potentially be determined more accurately. These sensitivity measures, using
regression or correlation techniques from the sets of input parameters and the
corresponding output values, allow ranking of the uncertain input parameters in relation
to their contribution to output uncertainty. The ranking of parameters is therefore
a result of the analysis, not of prior expert judgment, like a PIRT. Nevertheless, a PIRT
may be performed to define uncertainty ranges and distributions for a limited number
of input parameters, which are considered to be important or to identify important
code models to be validated.
The same ordered statistical method using Wilks’ formula for setting up the number of
codecalculationsfollowedlatertheAREVAMethod(MartinandDunn,2004),ASTRUM
(AutomaticStatisticalTReatmentofUncertainty)—MethodofWestinghouse(Muftuoglu
etal., 2004), KREM in Korea, ESM-3D in France and several more. TheAREVA method
has been licensed by USNRC in the year 2003 and the ASTRUM Method in 2004.

#### Number of calculations for statistical methods to meet more than one regulatory acceptance limit

A controversial international discussion took place about the number of calculations to
be performed using ordered statistical methods during the years 2003–2005. That
issue was mainly brought up when more than one regulatory acceptance criterion
or limit has to be met, like PCT, local oxidation of fuel rods, and core average
zirconium-water reaction for LOCAs. Wald (1943) extended Wilks’ formula for multidimensional
joint/simultaneous tolerance limits or intervals. However, it seems that
a direct and satisfactory extension of the concept of tolerance limits for safety-relevant
applications in nuclear safety is not necessary. A slightly modified concept has therefore
been proposed by Krzykacz-Hausmann from GRS, introducing a lower
confidence limit (Glaeser et al., 2008). The lower confidence limit according to
Clopper-Pearson (Brown et al., 2001) for the binomial parameter is now the unknown
probability that a result is lower than a regulatory acceptance limit. Instead of direct
joint tolerance limits for the outputs of interest, one considers the lower confidence
limit for the probability of “complying with the safety limits for all outputs,”

<!-- page 871 (PDF 41) -->
i.e., “meeting the regulatory acceptance criteria.” Basis is that both of the following
statements are equivalent:
1. The Wilks’ (probability a=95% and confidence b=95%) limit for the results is below the
regulatory acceptance limit
2. The lower b=95% confidence limit for the probability that the value of the result stays
below the regulatory acceptance limit is greater or equal a=95%
The regulatory acceptance limits are incorporated into the probabilistic statements.
It turns out that
(1) in the one-dimensional case, i.e., for a single output parameter, this concept is equivalent to
the one-sided upper tolerance limit concept.
(2) the necessary number of model runs is also the same in the general case, i.e., independent of
the number of outputs or criteria involved and of the type of interrelationships between
these outputs or criteria. Therefore, the number of necessary model runs is the same as
in the one-dimensional tolerance limit case, even if several output parameters are involved.
In the one-dimensional case the lower 95%-confidence interval for the probability of
“complying with the regulatory limit” corresponds to the two step procedure: (1) compute
the tolerance limit as usual and (2) compare this tolerance limit with the given regulatory
limit. In other words: The statement “there is a 95% confidence that the probability of
complying with the regulatory limit xreg exceeds 95%” is equivalent to the statement
“the computed 95%/95% tolerance limit xTL lies below the regulatory limit xreg.” In the
multidimensional case there is no such direct correspondence or equivalence.
The principal advantage of the confidence interval or limit (or “sign-test”) approach
seems to be that it can directly be used in the multidimensional case, i.e., multiple
output or several output variables, too. The multidimensional extensions of the tolerance
limit approach suffer from
(1) not being unique because the runs with the highest value for checking the first limit has to be
eliminated for comparison with the next limit, and so on
(2) require substantially increased calculation runs and
(3) are in most cases not necessary since functions of several variables can be reduced to the
one-dimensional case
Much more influence on the uncertainty range of computational results has the specified
input uncertainty ranges. Less important is the distribution of these input uncertainties
. Therefore, high requirements are on the specification and the justification for
these ranges. Investigations are underway to transform data measured in experiments
and posttest calculations into thermal-hydraulic model parameters with uncertainties.
Care must be taken to select suitable experimental and analytical information to specify
uncertainty distributions. The selection of suitable experiments is important for
the UMAE/CIAU method as well.

### 13.4.2.3 UMAE/CIAU method

The CIAU method is based on the principle that it is reasonable to extrapolate code
output deviations of relevant experimental tests to real plants, as discussed by D’Auria
et al. (1995) and D’Auria and Giannotti (2000). The development of the method
implies the availability of qualified experimental data. A first step is to check the

<!-- page 872 (PDF 42) -->
quality of code results with respect to experimental data by using a procedure based on
fast Fourier transform method. Then a method (UMAE) is applied to determine both
quantity accuracy matrix (QAM) and time accuracy matrix (TAM).
Considering ITFs of a reference light water reactor (LWR) and qualified computer
codes based on advanced models, the method relies on code capability qualified by
application to facilities of increasing scale. Direct data extrapolation from
small-scale experiments to the reactor scale is difficult due to the imperfect scaling
criteria adopted in the design of each scaled-down facility. Only the accuracy
(i.e., the difference between measured and calculated quantities) is therefore extrapolated
. Experimental and calculated data in differently scaled facilities are used to
demonstrate that physical phenomena and code predictive capabilities of important
phenomena do not change when increasing the dimensions of the facilities. However,
available IT facility scales are far from reactor scale.
One basic assumption is that phenomena and transient scenarios in larger-scale
facilities are close enough to plant conditions. The influence of the user and the
nodalization upon the output uncertainty is minimized in the methodology. However,
user and nodalization inadequacies affect the comparison between measured and
calculated trends; that deviation is considered in the extrapolation process and contributes
to the overall uncertainty.
Calculations of both ITs and plant transients are used to obtain uncertainty from
accuracy. Nodalizations are set-up and qualified against experimental data by an iterative
procedure, requiring that a reasonable level of accuracy be satisfied. Similar
criteria are adopted in developing plant nodalization and performing plant transient
calculations. The demonstration of the similarity of the phenomena exhibited in test
facilities and plant calculations, taking scaling laws into consideration, leads to a
qualified nodalization of the plant.
It is not possible to establish a correspondence between each input and each output
parameter without performing additional specific calculations. That is, however,
beyond the scope of the UMAE. The process starts with the experimental and calculated
database. Following the identification (e.g., from the CSNI validation matrix) of
the physical phenomena involved in the selected transient scenario, relevant
thermal-hydraulic aspects are used to evaluate the acceptability of code calculations,
the similarity among experimental data, and the similarity between plant calculation
results and available data. Statistical treatment is pursued in order to process accuracy
values calculated for the various test facilities and to obtain uncertainty ranges with a
95% probability level. These are superimposed as uncertainty bands bracketing the
qualified base calculation using the above mentioned qualified nodalization.
The scaling of both experimental and calculated data is claimed to be explicitly
assessed within the framework of the analysis. In fact, the demonstration of phenomena
scalability is necessary for the application of the method and the evaluation of the
uncertainty associated with the prediction of the NPP scenario.
Comparison of thermal-hydraulic data from experimental facilities of a different
scale constitutes the basis of the UMAE checking whether the nodalization and code
calculation results are acceptable. An adequate experimental database including the
same phenomena as in the selected test scenario of the NPP is needed for the
