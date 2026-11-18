# Introduction
<!-- source PDF pages 4-17 -->

<!-- page 834 (PDF 4) -->
analysis is already mentioned. The validation procedures described in this chapter are
based on phenomena described in Chapter 6 of the book.
Finally, validation, scaling, and uncertainty constitute very basic and important
elements for the best estimate plus uncertainty (BEPU) approach described in
Chapter 14 and should be considered when interpreting results of calculations
presented in Chapter 15 of the book.
The reader may recognize that validation, scaling, and uncertainty are linked
among each other and needs suitable understanding prior to the application of
thermal-hydraulic models and code to the evaluation of safety of nuclear
installations.
13.1
Introduction
This chapter deals with important steps before performing safety analyses using
thermal-hydraulic
computer
codes
calculating
the
physical
behavior
of
a
steam-supply system of a NPP. Verification and validation are means to prove the
quality of a computer code. Since many experiments, which are used to validate a
code, are in small scale compared with a nuclear reactor, the scaling effects have
to be considered. Since initial and boundary conditions, geometry, reactor plant operating
parameters, fuel parameters, and scale effects may not be exactly known, and the
SYS TH computer codes approximate the physical behavior, the code predictions are
not exact but uncertain. Agreement of calculated results with experimental data is
often obtained by choosing specific code input options or changing parameter values
in the model equations. These selected parameter values usually have to be changed
again for different experiments in the same facility or a similar experiment in a
different facility in order to obtain agreement with data. To make calculation results
useful, for example to be compared with limits of acceptance, the uncertainty in the
predictions has to be calculated separately. Therefore, uncertainty analysis methods
were developed to estimate safety margins if best estimate codes are used to justify
reactor operation. These uncertainty analyses are used more and more instead of
the former conservative analysis methods using conservative computer models
and/or conservative initial and boundary conditions with the intention to cover all
existing uncertainties.
This chapter describes the verification, validation, scaling, and uncertainty evaluation
to perform safety analyses because of their strong interrelation.
13.2
Verification and validation of thermal-hydraulic
system computer codes
Evaluation of nuclear reactor safety is based on deterministic safety analysis (DSA)
and probabilistic safety analysis (PSA). In order to perform DSA, properly qualified
computational tools are needed. Verification deals with the question “are the correct

<!-- page 835 (PDF 5) -->
equations implemented and solved correctly?” while validation deals with the question
“are the calculated results in agreement with experimental results?” Among
the computational tools, the current emphasis is on the SYS TH codes. These codes
consist of three major modules: the input/output (I/O) module, the governing equation
solver, and closure models. The governing equation solver consists of the following
three key modules:
l
Thermal-hydraulics (or fluid) balance equations solved in the fluid domains
l
Fourier equations for conduction of heat transfer in solid material
l
Neutron diffusion equations
Parts of the system code are the “special models” which supplement the capabilities of
the various sets of equations. Deviations in the prediction of the same scenario by the
same code used by different users may come from different options and selections of
input parameters by these users.
This book focuses on water-cooled nuclear reactors, including research reactors,
heavy water-cooled/moderated reactors, and graphite-moderated boiling reactors
designed and operated in Russia. Any calculation method or tool, including computer
codes, applied within the nuclear reactor safety issue shall undergo proper verification
and validation (V&V).
The quality of a calculation depends upon: (a) the quality of the code, (b) the
quality of the nodalization, (c) the adequacy of the adopted computer-compiler installation
, (d) the quality of the input data, and (e) the qualification level of the code-user.
Furthermore, any calculation by a best estimate SYS TH code should be supported by
uncertainty evaluation, specifically when results are relevant to safety or licensing.
Attention should also be exercised that scaling-related qualification is performed to
be part of the validation. Qualitative and quantitative accuracy evaluation, including
identification and ranking of thermal-hydraulic phenomena, is also considered for
performing verification and validation.

## 13.2.1 Verification of computer codes

Verification of computer codes is performed within a code development process to
show that the code behaves as intended, i.e.,
l
that it is a proper mathematical representation of the conceptual model or the design
l
that the equations are correctly encoded and solved
l
corresponds to the description in the documentation
The verification is performed to demonstrate that the design of the code numerical
algorithms conforms to the design requirements, that its logic is consistent with the
design specification, and that the source code conforms to programming standards
and language standards. Physical phenomena and processes to be simulated are
represented by a set of equations and closure relations.
Verification of computer codes consists of:
(1) the verification of the code design or concept and
(2) the verification of the source code (ANS, 1987; IAEA, 2009, 2015).

<!-- page 836 (PDF 6) -->
In general, the verification of the code design is performed to ensure that the numerical
methods, the transformation of the numerical equations into a numerical scheme to
provide solutions, and user options and their restrictions are appropriately
implemented in accordance with the design requirements. The verification of the code
design includes a review of the design concept, basic logic, flow diagrams, numerical
methods, algorithms, and computational environment. If the code is run on a hardware
or software platform other than that on which the verification process was carried
out, the continued validity of the code verification should be assessed (portability).
When the code design contains the integration or coupling of codes, then the verification
of the code design should ensure that the links and/or interfaces between the
codes are correctly designed and implemented to meet the design requirements.
Verification of the source code is performed to demonstrate that it conforms to
programming standards and language standards, and that its logic is consistent with
the design specification. The comparison with measured values is not part of the
verification; such a process is included in the validation process.
Practical instruments to verify the source code are review, inspection, and audit.
Checklists may be provided for review and inspection. Examples for checklists for
reviews and inspections of verification of the code design as well as the source code
are given in ANS (1987) and IAEA (2015).
Comparisons with independent calculations are carried out where practicable to
verify that the mathematical operations are performed correctly. Audits will be
performed on selected items to ensure quality. A review and inspection of the entire
code may not be practicable for verification purposes due to its large size. In such
cases, verification of individual modules or parts of the code can be conducted,
and this should include a careful inspection of all interfaces between the modules.
Any noncompliance of the code or its documentation with the design requirements
should be reported to and should be corrected by the code developer. The impact of
such noncompliances on results of analyses that have been completed before the
correction and used as part of the safety assessment for a plant should be assessed.

## 13.2.2 Validation of computer codes

Validation is the process carried out by comparing code calculation results with
experimental measurements or measurements in a reactor plant if available. A code
or code model is considered validated when sufficient testing has been performed
to ensure an acceptable level of predictive accuracy over the range of conditions over
which the code may be applied. Accuracy is a measure of the difference between measured
and calculated quantities taking into account uncertainties and biases in both.
Bias is a measure, usually expressed statistically, of the systematic difference between
a true mean value and a predicted or measured mean. Uncertainty is a measure of the
scatter in experimental or predicted data. The acceptable level of accuracy is judgmental
and will vary depending on the specific problem or question to be addressed
by the code. The procedure for specifying, qualitatively or quantitatively, the accuracy
of code predictions is also called code qualification or code assessment.

<!-- page 837 (PDF 7) -->
### 13.2.2.1 Validation process

Validation is mandatory to be performed on all computer codes that are used for
the DSA of NPPs. The purpose of validation is to provide confidence in the ability
of a code to predict, realistically or conservatively, the values of the safety parameter
or parameters of interest. Analysis methods that are used for safety demonstration
of the fulfillment of the regulatory acceptance criteria must be validated for
their respective scope of application. If calculation methods are used for analyzing
the effectiveness of preventive or mitigative accident management measures, these
shall also be validated for their respective scope of application.
The major sources of information that should be used to assess the quality of
computer code predictions are analytical solutions, experimental data, NPP transients,
and benchmark calculations, i.e., code-to-code comparisons. Those code-to-code
comparisons can be used for validation purposes provided that, at least, one of the
codes has been validated.
It is recommended for complex analysis, to perform the validation process in
two steps: the development phase, in which the assessment is performed by the
code developer, and the independent validation phase, in which the validation is
done by someone who is independent of the developer of the code. Both phases
are necessary for an adequate validation procedure. If possible, it is recommended
that the data used for the independent validation of the code and the data that are
used for the validation by the code developers should be selected from different
experiments. Where possible, users should do validation exercises without having
any prior knowledge of the experimental results to preclude any deliberate tuning
of code calculations to yield better agreement with experimental results. Validation
exercises are a very good means for users of a code to get experience in applying
the code.
The validation process should ideally include four different types of test
calculation:
(1) Basic tests. Basic tests are simple test cases that may not be directly related to a NPP. These
tests may have analytical solutions or may use correlations or data derived from
experiments.
(2) Separate effects tests (SET). Separate effects tests address specific phenomena that
may occur at a NPP but do not address other phenomena that may occur at the same
time. SETs should ideally be performed at full scale. In the absence of analytical
solutions or experimental data, other codes that are known to model accurately the
limited physics represented in the test case may be used to determine the accurate
solution.
(3) Integral tests (ITs). Integral tests are test cases that are directly related to the behavior of the
system of a NPP. All or most of the relevant physical processes as well as their interactions
are represented. However, these tests are usually carried out at a reduced scale, the tests may
use substitute materials or may be performed at low pressure.
(4) NPP level tests and operational transients. Nuclear power plant level tests are performed
on an actual NPP. Validation through operational transients together with NPP tests are
important means of quantifying the plant model.

<!-- page 838 (PDF 8) -->
The validation tests should ideally cover the entire range of values of parameters,
conditions, and physical phenomena that the code is intended to cover. The scope
of the independent validation exercise performed by the code user should be consistent
with the intended purpose of the code and the range of experimental data available.
The scope of validation should also be in accordance with the complexity of the code
and the complexity of the physical processes that it represents. The code user should
also evaluate qualitatively or quantitatively the accuracy of the results of the calculations
. For complex applications, a validation matrix should be available for code
validation because a code may predict one set of test data with a high degree of accuracy
but may be extremely inaccurate for other data sets. The validation matrix should
include test data from different experimental facilities at different scale and different
sets of conditions in the same facility. It should ideally include basic tests, SETs, ITs,
and NPP level tests. If sufficient data from full-scale experiments are not available,
data from reduced scale experiments will be used, with appropriate consideration
of scaling (see Section 13.3).
Internationally agreed integral test facility (ITF) matrices for validation of realistic
thermal hydraulic system computer codes were established in the OECD/NEA/CSNI
validation matrix (CSNI, 1996) containing a total number of 177 PWR and BWR
specific ITs selected as potential source for thermal hydraulic code validation. ITF
development is mainly for pressurized water reactors (PWRs) and boiling water reactors
(BWRs). A separate activity was for Russian pressurized water-cooled and
water-moderated energy reactors (WWER) (CSNI, 2001). First, the main physical
phenomena that occur during considered accidents are identified, test types are
specified, and test facilities suitable for reproducing these aspects are selected.
Second, a list of selected experiments carried out in these facilities has been set down.
The criteria to achieve the objectives are outlined.
The SET are designed to validate specific phenomena of the whole physical model
independently from the others. SETs may address:
–
A specific basic flow process (flashing, critical flow, direct contact condensation,
counter-current flow limitation (CCFL), lower plenum voiding, etc.)
–
A specific closure term for a given flow or for a given range of flow parameters
–
The specific behavior of a specific reactor component (separator, break, valve, loop seal,
etc.). This is called a component test
–
A specific flow process occurring in a specific reactor component during a selected time
span of an accidental transient identified as a phenomenological phase
Due to the variety of models, the variety of flow regimes and the variety of geometrical
configurations, a SET validation matrix has a large number of tests. The OECD/
NEA/CSNI SET matrix (CSNI, 1994) contains 67 thermal-hydraulic phenomena and
1094 tests from 185 test facilities as potential source for thermal hydraulic code
validation. Subsequent experiments have been performed in the meantime to investigate
different reactor designs.
The number and the selection of tests in the test matrix used for validating specific
computer codes do not need to use all these experiments contained in the international
validation matrices. The number of tests used should be justified as being sufficient for

<!-- page 839 (PDF 9) -->
the intended application of the code. The range of validity and the limitations of a
computer code, which are established as a result of validation, should be documented
in a validation report which should be referenced in licensing documentation.
However, code users may perform additional validation to demonstrate that the code
satisfies the objectives for their specific application. This, however, necessitates the
availability of experimental data as well as experimental documentation or the results
of NPP data, like start-up tests.
When experiments are used for validation of the computer codes, care should
be exercised when planning an experiment to ensure that the measured data are
as suitable as possible for the purpose of code validation. The safety parameters
that will be calculated using the code should be considered when the experiment
and its instrumentation are planned. To ensure that the code is validated for
conditions that are as close as possible to those in a NPP, it should be ensured that
the boundary conditions and initial conditions of the test are appropriate. Consideration
should be given to scaling laws. A scaled experimental facility cannot
be used to represent all the phenomena that are relevant for a full size facility
(see Section 13.3). Thus, for each scaled facility that is used in the assessment
process, the phenomena that are correctly represented and those that are not
correctly represented should be identified. The effects of phenomena that are
not correctly represented should be addressed in other ways. The uncertainty in
the experimental data should be reported in the documentation of the experiment.
When performing a validation against experimental data, allowance for errors in
the measurements should be included in the determination of the uncertainty of
the computer code.

### 13.2.2.2 Qualification of input data

The input data for a computer code include a representation of all or parts of the
NPP. There is usually a degree of flexibility in how the plant is modeled or
nodalized. The intention is to be flexible in calculating different reactor types
and different scenarios. The input data that are used to perform safety assessment
calculations should conform to the best practice guidelines for using the computer
code as described in the user manual and should be independently checked. The
input data should be a compilation of actual information found in as-built and valid
technical drawings, operating manuals, procedures, set point lists, pump performance
charts, process diagrams and instrumentation diagrams, control diagrams,
etc. Users who prepare input data to model validation tests should be suitably
qualified and should make use of all available guides. These include the specific
code user guide, generic best practice guides for the type of code, and guidance
from experienced users. The validation process itself often enables the determination
of best practices. This may include nodalization schemes, model options, solution
methods, and mesh size. Those who generate input data sets for safety analysis
calculations should use the best practice guidelines established during the validation
process.

<!-- page 840 (PDF 10) -->
### 13.2.2.3 Qualitative and quantitative assessment of validation calculations

A realistic or “best estimate” computer code or analysis method may be deemed
validated if the applicability and sufficient accuracy of the code applied has been
demonstrated for the respective application within the framework of the validation
scope performed and documented.
Qualitative judgment of agreement between the code calculation and the data is
generally divided into four categories:
Excellent agreement: The calculation lies within or near the data uncertainty band at all
times during the phase of interest.
Reasonable agreement: The calculation sometimes lies within the data uncertainty band and
shows the same trends as the data. Code deficiencies are minor.
Minimal agreement: Significant code deficiencies exist. Some major trends and phenomena
are not predicted. Incorrect conclusions may be drawn based on the calculation when data are
not available.
Unacceptable agreement: A comparison is unacceptable when a significant difference
between calculation and the data is present, and the difference is not understood. Such a
difference could follow from errors in either the calculation or the presentation of the data,
or an inadequate code model of the phenomenon.
A code is considered to be of adequate applicability when it shows either excellent
or reasonable agreement with the highly ranked phenomena, sometimes identified
as the dominant phenomena, for a transient of interest. If the code gives minimal
or unacceptable agreement, additional work must be performed, ranging from additional
code development to additional analysis to understand the phenomena.
Quantitative judgment of agreement between code results and data can be performed
in different ways. The Japan Atomic Energy Research Institute comparing the
submissions of International Standard Problem No. 26 (ISP-26), calculating an experiment
on the LSTF facility, a 5% cold leg break experiment LSTF-SB-CL-18,
performed one accuracy quantification study. Seventeen time-averaged deviations
between selected, calculated, and measured results were performed for the different
participants:
Xcal□Xexp
j
j=Xexp < limit
The limit chosen for ISP-26 (LSTF-SB-CL-18) was, for example:
good agreement: limit=0.1
acceptable agreement: limit=0.2
poor agreement: limit>0.2
Such an accuracy quantification method has not generally been used because of the
dependence of results on the number and type of included variables, the dependence
on the chosen time span, error compensation may not be detected, erroneous initial
and boundary conditions may not be taken into account, and a lack of information
about qualitatively correct trends in the calculation.

<!-- page 841 (PDF 11) -->
University Pisa, using the fast Fourier transform-based method (FFTBM) with
imposed acceptability limits (Ambrosini et al., 1990) has proposed another accuracy
quantification method. The FFTBM has been developed to perform quantitative accuracy
evaluation of the results of SYS TH codes. The idea is to perform the comparison
between the measured and the calculated results from the time domain toward the
frequency domain in order to get a figure of merit independent of the time duration
of the scenario. The main FFTBM output is the average accuracy related to an
individual or the total accuracy related to a set of variables. Kunz et al. (2002) discuss
the comparison of the FFTBM with other methods suitable for quantifying accuracy,
and Prosek et al. (2005) present application results.
For conservative safety analysis methods used in licensing applications of NPPs,
experimental results should be bounded in the direction of regulatory acceptance
criteria, like the peak cladding temperature (PCT) of 1200°C for loss of coolant
accidents (LOCAs). Conservative is understood here in the unfavorable direction
to acceptance criteria of safety parameters. That means the result of a conservative
code should always be closer to the acceptance criterion than the realistic value.

### 13.2.2.4 International Standard Problems

A special and challenging case of validation activities is occurring during an International
Standard Problem (ISP), where comparison exercises are performed between
different participants. Two kinds of comparison exercises can be organized between
participants for code calculations, following the definition made generally in the
CSNI, benchmarks, and ISPs. The benchmark exercise corresponds to calculations
of a physical case defined theoretically for which no experimental reference exists.
The comparisons are performed between each participant calculations, but there is
no way to decide which one is really the best. In an ISP the calculations are centered
on experimental results. Comparisons between each participant are still part of the
exercise, but the final quality of the predictions is judged on the basis of the experimental
results themselves which play consequently a key role. As a consequence, the
specifications relative to the experimental results should follow detailed requirements
in the ISP process. The mode for distribution of experimental data becomes also very
important. A specific CSNI Report 17 (CSNI, 2004) discusses all these points and
provides recommendations on each of them. 26 out of the 52 ISPs performed within
the CSNI between the years 1973 and 2012 were from primary and secondary SYS
THs and six from containment thermal-hydraulics. The others were from fuel behavior
during LOCA (2) and severe accidents (19); 1 proposal was cancelled. Brief
descriptions of all CSNI Standard Problems up to ISP 43 can be found in report
CSNI (2000); further reports about CSNI Standard Problems are available on the
CSNI web site www.oecd-nea.org/nsd/docs.
The recommendations on the ISP specifications emphasized particular important
features. Here are some of them:
–
The experimental facility description provided to the ISP participants should be sufficiently
detailed including layout, drawings, component characteristics that are necessary. Before
proposing an ISP one must be sure that no proprietary interdiction is on the required data.

<!-- page 842 (PDF 12) -->
–
The instrumentation should be detailed. Location, type, accuracy, data acquisition system,
sampling, response time should be supplied to the participants.
–
The test conditions should be well known; initial and boundary conditions should be provided
with sufficient detail for running the prediction calculations in a meaningful way.
One can observe that those recommendations are still topical and that partial nonobservance
is, even now, sometimes the source of shortcomings in the results. The
governing idea has been to put the ISP participant in the same situation as when
the user of a code is proceeding to a plant calculation for solving a safety issue. Therefore
, in the last ISPs, results like those from characterization tests giving, for example,
pressure drops, pump characteristics, heat losses and their distributions, etc., have
been added in the specifications to the test conditions. Furthermore, for ISPs in relation
to actual plant transients, additional specifications were supplied such as the
timing and degree of interventions from operators as well as plant auxiliary system
conditions with their uncertainty bands.
The distribution of test results is also a key point in the ISP performance. Different
options have been used which change the nature and the outcome of the ISP.
Depending of those options, ISPs are classified in open, blind, semiblind, or
double-blind ISPs. These categories are explained in more details:
–
Open ISP: This is an ISP where the participant gets all the experimental data from the very
beginning. All information is open. The calculations are performed, while the experimental
results are known.
–
Blind ISP: on the contrary to open ISP, the participants in the blind ISP have no access to the
test results except the test boundary and initial conditions in the general meaning discussed
above. Actual test results remain locked until the calculations are finished and sent to the
ISP organizer. The participants are doing their calculation in a blind situation in the same
way they are doing the calculations of plant accidents where no experimental data is available
. Blind ISPs are consequently recommended because they reflect better the real conditions
in which an analyst will find himself for plant analysis. Furthermore, this is
reinforced by the very frequent observation that calculations are generally better when
experimental results are available at the time of the calculation. This is due to adjusting
of the computer model and/or of the input data to account for the specific test results.
Calculations in blind situation may avoid most of this kind of “tuning effect.”
In reality, even in blind situations, some tuning of the code may be obtained by using
tests which have been already performed on the same experimental facility and which
may be more or less similar to the one proposed for the ISP. For this reason, distinction
was made in ISPs between real blind participants and participants who in fact
had opportunities to perform extensive analysis of other tests and who could therefore
not be considered as completely blind. This is also why the concept of double-blind
ISP was created.
–
A double-blind ISP is an ISP for which the participant has not access to the results of the
ISP test or to the results of any other tests performed on the experimental facility (except
the characterization tests considered as normal additions to tests conditions). This situation
represents in fact the exact real situation of the analyst performing plant calculations.
Consequently, double-blind ISPs are especially challenging to both the codes and the code
users, and correspondingly more valuable in assessing code performance. However, such
ISP can only be performed in the very rare situations where no test results have been already

<!-- page 843 (PDF 13) -->
published, i.e., when starting a new facility. In this situation, meeting the high quality of
standard requested for ISP is considerably difficult for the organization running the
facility as it requires a perfect control of the experimental procedure, which is in fact in
contradiction with the learning phase generally experienced on a brand new experiment.
Consequently, very few double-blind ISPs have been practically organized.
From the preceding discussion, it appears clearly that the “more” blind an ISP is, the
more significant the conclusions may be. However, there are cases where the generalization
of this statement is in fact an oversimplification.
–
A semi blind ISP concept has been introduced, for example, when the prediction of the tests
involves two types of interacting phenomena and when the uncertainties on one of these
phenomena will preclude the conclusions, which can be drawn on the other one. In these
specific cases, it has often been decided, for preserving the ISP efficiency that the results
concerning the first phenomena will be opened, and the results of the second will be blind.
This semiblind procedure has been for instance used for fuel behavior ISPs where
thermal-hydraulic conditions were often open and fuel results were blind so that uncertainties
on thermal-hydraulics will not prevent to draw conclusions on fuel.
As another example where blind ISPs are not providing necessarily the most significant
conclusions, we can mention ISPs dealing with physical areas where the knowledge
is at an early stage or dealing with areas where phenomena are particularly
complex. In such cases, blind calculations would give unusable results and valuable
ISPs could only be open ones. In those specific areas, even if the ISPs results look
encouraging, it should be kept in mind that for such ISP, an open exercise has been
chosen because of the difficulties expected in blind calculations and that consequently
, one could also expect similar difficulties in similar plant calculations, which
will be performed by the analysts in a necessarily blind-like situation.
The comparisons between the calculations and the experiment and between the
calculations themselves are the constitutive part of the ISPs. It provides the basis
for drawing conclusions on the capabilities and the deficiencies of existing calculation
tools in an international framework. It is also during the analysis that the most detailed
discussions can take place between experts.

### 13.2.2.5 User effects

The user of state-of-the-art SYS TH computer codes must make many choices in
setting up an input deck and running a calculation. Such a flexibility is by purpose
to be able to apply such a code for different events and purposes. One experience from
International Standard Problems is, however, that large differences of code results
from different code users applying the same code version and the same specifications
(e.g., initial and boundary conditions, geometry) have been observed. These differences
are considered as code user effects (CSNI, 1995). In other arenas, e.g., plant
calculations, some of these elements may better be classified as code, scale, plant
state, etc., uncertainties. Uncertainty analyses are supposed to quantify some of these
user effects. The focus is here on quantifying user effects of experienced code users
and qualified input decks but not exactly known values for several input parameters.
Mistakes in the input deck and code deficiencies in calculating important phenomena

<!-- page 844 (PDF 14) -->
should not be included in these uncertainty quantifications. The main source of quantifying
code model uncertainties is therefore the experience of experts during the validation
process.
The development of thermal-hydraulic advanced codes was expected to decrease
this effect of code users, but the last thermal-hydraulic ISPs have shown that there was
still a significant “user effect” in applying these advanced codes. Detailed studies of
this effect have been made on different ISPs. In addition to the identification of the
user effect, ISPs have contributed largely to its understanding. ISPs are really providing
data that are absolutely unique on this crucial subject. In recent comparisons of
international applications of uncertainty evaluations, we have seen significant user
effects, too.
Ways to reduce user effects have been proposed within the CSNI working groups
(CSNI, 1995, 1998; Shotkin, 1997; D’Auria, 1998). User training by performing validation
, mentoring, and instruction are the most effective and easiest ways to improve
the quality of code predictions. Users need a good knowledge of the physical modeling
and limitations of the codes, the facility to be described, and an understanding of major
phenomena expected to occur during the transient. User Guidelines that are based on
the results of a systematic code validation program are also a way to reduce the user
effect. They prevent an inadequate use of a code and avoid mistakes. However, these
guidelines cannot give detailed recipes for all existing conditions. They cannot
substitute for a trained and experienced code user.
Another way to reduce code user effects is quality assurance. Preparation and testing
of an input deck requires at least 6 months for an experienced code user. Clear
quality assurance strategy is necessary. Often, incomplete or error-ridden input decks
are used. It is common practice to use existing input decks. However, a warning should
be issued to share existing decks between different users to save time who then introduce
only minor modifications without complete checking of the major part and without
understanding for what purpose the available input decks have been developed.
Even though some suggested ways to reduce the user effect have been proposed, it
remains that we are quite far from controlling it completely. The user effect has also
appeared as a generic question and not only in the thermal-hydraulics area where it has
been discovered. In particular, the several ISPs that have been recently performed in
the severe accident area have shown the same importance for this effect.

### 13.2.2.6 Counterpart and similar tests

The development and the assessment of system codes used in the safety analysis of
water-cooled reactors have to rely mainly on experimental data from scaled, separate
effects, or integral system test facilities. Data from full size plants are not usually
available for code validation except for mild operational transients. The typicality
of the experimental data acquired in scaled test facilities is however often questioned
due to inherent scaling distortions stemming from design and simulation constraints.
In order to assure the adequacy of system codes in predicting a realistic system
response, the code assessment process is thus diversified over a wide range of test data
from test facilities having different scaling ratios and/or design concepts.

<!-- page 845 (PDF 15) -->
In addition, it is considered beneficial to verify the code scalability aspects against
a set of data from tests performed in different facilities but under “similar” initial and
boundary conditions. This would partially separate the code assessment process from
physical assumptions emphasizing instead the influence of configurational and
geometric scaling aspects.
The word “similar” has been however the subject of many discussions in the past,
and some authors tried to indicate which of the minimum set of initial and boundary
conditions have to be preserved between the various test facilities in order to classify
that series of tests as “Counterpart Tests.” Counterpart tests are tests specified from the
beginning as counterpart tests to be performed in different test facilities with scaled
initial and boundary conditions. It should be noted then that some tests are more
suitable than others to be the subject of a counterpart test: in particular tests where
the influence of facility distortions (e.g., heat losses) are less important.
The difficulty in the specification of a counterpart test connected with generally
strict and fixed test programs makes it difficult to have a large number of these test
series. Nevertheless, looking at the integral facilities test programs it is possible to
identify some tests which although they do not meet exactly the conditions for a
counterpart test do maintain a great similarity in the initial and boundary conditions.
These tests here referred to as “Similar Tests” can reveal important scaling influences
that would otherwise been lost.
The most relevant counterpart test activity was performed during a time frame of
about 20 years. Selecting small break (SB) counterpart tests, for example, five IT
facilities and seven experiments, are involved. The ITFs are
l
LOBI (simulator of a German four loops PWR by two unequal loops)
l
SPES (simulator of a US three loops PWR by three equal loops)
l
BETHSY (simulator of a French three loops PWR by three equal loops)
l
LSTF (simulator of a US four loops PWR by two equal loops)
l
PSB (simulator of Russian four loops VVER-1000 by four equal loops)
Four of the involved ITF are equipped with vertical U-tubes steam generators, and the
fifth one, PSB, is equipped with horizontal tube steam generators. The concerned
experiment is a SB-LOCA simulating a break in one cold leg, without activation of
the high-pressure injection system.
A few remarkable results taken from the SB-LOCA counterpart test database
(e.g., see D’Auria et al., 1994; Blinkov et al., 2005; D’Auria and Galassi, 2010) are
reported in Figs. 13.1–13.3 for the system pressure, water mass inventory, and rod
surface temperature. These figures were produced by University of Pisa. The objective
is to give an impression of the counterpart test database. Each of the three diagrams
shows the comparison between seven experiments out of five test facilities and seven
calculated trends. This gives an impression of the capabilities of computational tools
to calculate phenomena at different scale with a comparable level of accuracy.
Some selected interesting aspects of these counterpart tests are:
l
Occurrence of three dry-out conditions due to:
(a) pump seal blockage, consequential drop of water level in the core region, and clearance
of the pump seal and consequently recovery of water level in the core region

<!-- page 846 (PDF 16) -->
500.
1000.
1500.
2000.
2500.
3000.
Time (s)
2.0
4.0
6.0
8.0
10.0
12.0
14.0
16.0
18.0
Pressure (MPa)
XXX
BETHSY_EXP
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
YYY
BETHSY_CALC
Y
Y
Y
Y
Y
Y Y Y Y Y Y Y Y Y
Y
Y
Y
Y
Y
ZZZ
LOBI_EXP
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
VVV
LOBI_CALC
VV
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
JJJ
LOBI_EXP_H
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
HHH
LOBI_CALC_H
H H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
###
LSTF_EXP
OOO LSTF_CALC
OO
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
AAA
PSB-VVER_EXP
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
BBB
PSB-WWER_CALC
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
CCC
SPES_EXP
C
C
C
C
C C C C C C C C C C C C C C C
DDD
SPES_CALC
D
D
D
D D D D D D D D D D D D D D D D
EEE
SPES_EXP_H
E
E
E
E
E
E E E E E E E E E E E E E E
FFF
SPES_CALC_H
F
F
F
F
F F F F F F F F F F F F F F F
WinGraf 4.1 - 02-06-2010
Fig. 13.1 Upper plenum pressure of SB-LOCA counterpart test database and calculations.
Courtesy of D’Auria, F., Galassi, G.M., 2010. Scaling in nuclear reactor system
thermal-hydraulics. Nucl. Eng. Des. 240, 3267–3293.
500.
1000.
1500.
2000.
2500.
3000.
Time (s)
.20
.40
.60
.80
1.00
1.20
Normalized residual mass (-)
WinGraf 4.1 - 02-06-2010
XXX
BETHSY_EXP
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
YYY
BETHSY_CALC
Y
Y
Y
Y
Y Y Y Y Y Y Y Y Y Y
Y
Y
Y
Y
Y
ZZZ
LOBI_EXP
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
VVV
LOBI_CALC
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
JJJ
LOBI_EXP_H
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
HHH
LOBI_CALC_H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
###
LSTF_EXP
OOO LSTF_CALC
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
AAA
PSB-VVER_EXP
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
BBB
PSB-WWER_CALC
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
CCC
SPES_EXP
C CCC C
C
C
CC
C
C
CC C
DDD
SPES_CALC
D
D
D D D D D D D D D D D D D D
D
D
D
EEE
SPES_EXP_H
E
E
E
E E E E E E E E E E E E E E E
E
FFF
SPES_CALC_H
F
F
F F F F F F F F F F F F F
F
F F F
Fig. 13.2 Normalized residual water mass of SB-LOCA counterpart test database and
calculations.
Courtesy of D’Auria, F., Galassi, G.M., 2010. Scaling in nuclear reactor system
thermal-hydraulics. Nucl. Eng. Des. 240, 3267–3293.

<!-- page 847 (PDF 17) -->
(b) water inventory loss via the SB and water inventory recovery by accumulator injection
(c) water inventory recovery by Low Pressure Injection System (LPIS)
l
For all these ITF experiments, the scaled initial power condition was considered in the
design. However, only LOBI and SPES were able to simulate scaled full initial power,
the others had reduced scaled initial power (10%–14%). Seven experiments in five ITF
are part of the SB counterpart test program.
l
Measured data from the seven experiments fulfilled the objectives of the tests, are consistent,
and discrepancies among the corresponding time trends could be explained. However, in principle
, all thermal-hydraulic phenomena are scale dependent with regard to geometry. For
instance, two-phase pressure drop depends on diameter because flow regimes depend on diameter
. Then, a number of phenomena depending on volume to surface ratio are scale dependent.
Noticeable examples are found for liquid penetration (i.e., downflow) in the downcomer, or
across the upper core plate in the case of hot leg injection. It strongly depends upon the geometric
dimensions of the components for counter-current flow, see also Sections 13.3.2 and
13.3.3 of this chapter as well as Glaeser and Karwat (1993). In case of small-scale experiments,
liquid penetration is interfered by more intense steam-water interaction compared with large
scale where more separate steam-water flow passages are possible. Consequently, higher ECC
water penetration to the core region is possible for cooling the core.
l
Accuracyinthepredictionsbyusingmorethanonecodewasindependentuponscalingusingan
appropriate ratio of experimental and calculated value Yexp/Ycalc. “Y” is a generic parameter
value representing a thermal-hydraulic phenomenon under investigation (D’Auria et al., 1988).
Analyses of counterpart tests in PWR for scenarios different from SB-LOCA and
performed in ITF, scaled according to time-preserving laws, can also be found in
the literature (e.g., Bazin et al., 1992) dealing with natural circulation.
500.
1000.
1500.
2000.
2500.
3000.
Time (s)
Temperature (K)
WinGraf 4.1 - 02-06-2010
XXX
BETHSY_EXP
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
X
YYY
BETHSY_CALC
Y
Y Y Y Y
Y Y Y Y Y Y Y Y Y
Y
Y
Y
Y
Y
ZZZ
LOBI_EXP
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
Z
VVV
LOBI_CALC
VV
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
V
JJJ
LOBI_EXP_H
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
J
HHH
LOBI_CALC_H
H H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
H
###
LSTF_EXP
OOO LSTF_CALC
OOOO
O
O
O
O
O
O
O
O
O
O
O
O
O
O
O
AAA
PSB-VVER_EXP
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
BBB
PSB-WWER_CALC
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
CCC
SPES_EXP
C C C
C
C C C C C C C C
C
C
C
C C C C
DDD
SPES_CALC
D D
D
D D D D D D D D D D D
D
D D D D
EEE
SPES_EXP_H
E E E E
E E E E E E E E E E E
E
E
E
E
FFF
SPES_CALC_H
F
F F
F F F F F F F F F F F
F
F F F F
Fig. 13.3 Heater rod surface temperature of SB-LOCA counterpart test database and
calculations.
Courtesy of D’Auria, F., Galassi, G.M., 2010. Scaling in nuclear reactor system
thermal-hydraulics. Nucl. Eng. Des. 240, 3267–3293.
