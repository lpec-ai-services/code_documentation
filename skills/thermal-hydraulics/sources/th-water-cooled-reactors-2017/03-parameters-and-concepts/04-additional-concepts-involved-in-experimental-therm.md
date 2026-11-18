# Additional concepts involved in experimental thermal hydraulics
<!-- source PDF pages 25-29 -->

<!-- page 113 (PDF 25) -->
## 3.4.8 Nodalization/nodalization diagram

Spatial discretization of the two-phase flow field, in which equations are solved, is
organized in control volumes connected by junctions and it is called nodalization.
Sometimes the meaning of the word nodalization is extended to the whole set of
parameters and information supplied by the user.
Nodalization diagram is a drawing or illustration showing control volumes with
theirconnectingjunctions.Suchdiagrams,whentheyhaveenoughdetailandareproperly
set, become very useful to understand, at first glance, the involved calculation.

## 3.4.9 User effect/good practices

An initial characterization of user effect was given in 1993 by Aksan et al. (1993).
Later on, in 1998, it had been defined by OECD/NEA as it follows: “User effects
are any differences in calculations that use the same code version and the same specifications
for a given plant or facility.” The document giving such definition (Ashley
et al., 1998) analyzed also the main reasons explaining the appeared difference and
established also a series of “good practices” devoted to avoid or minimize the user
effect. Good practices are based on user training (D’Auria, 1998; Petruzzi et al.,
2008), user discipline, and quality assurance, and in a wider context with organization
requirements and safety culture.

## 3.4.10 International standard problems

International standard problems (ISPs) are comparative exercises in which predictions
or recalculations of a given physical problem with different best-estimate computer
code are compared with each other and above all with the results of a carefully specified
experimental study. Such exercises are organized within OECD/NEA framework
since 1975 to increase confidence in the validity and the use of the different tools that
are used in assessing the safety of nuclear installations. Extensive information is available
. It includes reports on particular exercises (Kimber et al., 1998), compendium of
groups of exercises (OECD/NEA/CSNI, 1997), or even articles on the results of revisiting
any exercise with updated codes and models (Freixa et al., 2015a).
3.5
Additional concepts involved in experimental
thermal hydraulics

## 3.5.1 Separate effect tests

Each separate effect test (SET) facility has been designed to investigate the local
occurrence of a particular phenomenon. Usually, such facilities represent physically
either some relevant zones of the NPP or some geometry in which the studied phenomenon
can be identified and studied. The results of the experiments performed are used
to validate the models created to describe the studied phenomenon. The final goal of
the whole thing is to include the model in a system code.

<!-- page 114 (PDF 26) -->
The SET Validation Matrix is a document (OECD/NEA/CSNI, 1993), established
under the auspices of OECD, devoted to identify the phenomena covered by the matrix
and to give an outline of existing facilities and test types. The document manages to
show a cross-reference matrix considering relationship between phenomena, test type,
and facility.

## 3.5.2 Integral effects tests/integral test facilities

Each integral effects test (IET) performed in an integral test facility (ITF) has been
designed to investigate the behavior of its reference plant under accidental conditions.
All the significant components and systems of the involved NPP are reproduced usually
at lower scale. For such reason scaling considerations have to be considered in
order to assure the suitability of the results. The expected results are the response
of the plant to the simulated initiating events. The results are also used to improve
models or to check code capabilities.
The IET Validation Matrix is a document, established under the auspices of OECD,
devoted to identify the scenarios covered by the matrix and give an outline of existing
facilities and test types.
PKL facility in Erlangen (Germany), LSTF in Tokaimura (Japan), and ATLAS in
Daejeon (Korea) are three relevant ITFs currently in operation.
LOBI facility in Ispra (Italy), LOFT in Idaho Falls (Idaho, USA), and BETHSY in
Grenoble (France) were ITFs operating in the past and currently dismantled.

## 3.5.3 Analytical support to experimental thermal hydraulics

The analytical support to experimental thermal hydraulics (Ummimger et al., 2012) is
based on calculations simulating the tests. Pretest calculations are usually performed
before running the test and are devoted to complete test preparation or to clarify uncertain
aspects of what is expected. Posttest calculations are performed after the test
(e.g., Revento´s et al., 2012). The results obtained are compared with experimental data
and the comparison is useful in code and nodalization validation. Posttest can be open
or blind. Both are helpful for validation and blind calculations have an additional
outcome since they show the actual capabilities of predictive analysis.

## 3.5.4 Databases of experimental thermal hydraulics

The importance of experimental data production for code validation is clearly accepted.
The databases of test results must be preserved and properly organized. Data need to be
accessed and retrieved easily by analysts involved in their use (Addabbo et al., 2002).
The information stored in such databases includes basically files containing experimental
data at different time frames (ASCII or binary formats) in order to facilitate
the comparison between prediction and test results. Also typical documents related to
experiments, among them the well-known Quick-Look Report (QLR) and Experimental
Data Report (EDR), complete the information associated to each test.
The STRESA (Storage of Thermal Reactor Safety Analysis Data) web-based informatics
platform is a good example of how such database can be implemented (Pla
et al. 2015, 2016b). In its current version STRESA is forming a network of nodes
and storing data of an important amount of relevant thermal-hydraulic tests.

<!-- page 115 (PDF 27) -->
## 3.5.5 Scaling/scaling issue/addressing the scaling issue

Scaling in nuclear-thermal hydraulics constitutes the topic of an important document,
completed in 2016 by a Specialist Scaling Group (SSG) formed in 2013 by the
WGAMA (OECD/NEA/CSNI, 2016c). The document testifies not only the importance
of scaling in nuclear technology, but also the controversial evaluations of
scaling-related findings by the scientific community.
“Scaling,” “scaling issue,” and “addressing the scaling issue” indicate actions,
methods, and techniques aimed at connecting the parameter values related to
experiments with NPP conditions. Scaling is the process of demonstrating the
applicability of any parameter value to the reactor conditions. Addressing the scaling
issue refers to the process of demonstrating the applicability of data from
models to prototype.
A general guideline for addressing the scaling issue can be found in USNRC code
scaling, applicability, and uncertainty method (CSAU) (USNRC, 1989). It is an extensive
work aimed at providing a suitable framework for uncertainty and accuracy
analyses by the use of best-estimate codes. This methodology was presented as a
response to the revision of the 10CFRpart 50 ECCS rule (USNRC, 2015), for which
the evaluation of the acceptance criteria could be done using realistic codes under
certain conditions, literally:
l
Uncertainties in the analysis method and inputs must be identified and assessed so that uncertainty
in the calculated results can be estimated
l
There is a high level of probability that the criteria would not be exceeded
The document faces the scaling issue emphasizing the need of considering two main
aspects:
l
To evaluate the capability of BE codes to scale-up processes from reduced scale test facilities
to full-scale NPPs
l
To quantify the effects of scale distortion and/or a limited data base, on code uncertainty to
calculate a safety parameter of interest, for example, peak clad temperature
Related to these concepts, several scaling criteria and scaling analysis methodologies
can be found in the technical literature. Regarding scaling criteria and design of experimental
facilities, one can find terms like linear scaling, power-to-volume scaling, and
modified time preserving scaling. Regarding scaling analysis and experimental data
extrapolation, hierarchical two-tiered scaling, Ishii three-level scaling, and fractional
scaling analysis are the most common methodologies. Some of these techniques are
depicted below.

## 3.5.6 Power-to-volume scaling

Power-to-volume scaling (or volume scaling) method conserves the time, length (or
height), velocity, and heat flux equivalently to those of the prototype. A test facility
designed following power-to-volume scaling has a full-height scale, while area and
volume of the facility are reduced with the same scale. Experiments involved conserve
also pressure, temperature, and time.

<!-- page 116 (PDF 28) -->
## 3.5.7 Hierarchical two-tiered scaling

Hierarchical two-tiered scaling (H2TS) is a comprehensive, systematic yet practical,
auditable, and traceable methodology for evaluating the applicability of the experimental
data from scaled-down facilities to NPP conditions, and hence, implicitly,
the capability of the system codes and their special models (because they are qualified
just at facility level) to scale-up TH data to full-scale plant conditions. It is based on
the premise that each TH process that occurs in a system can be characterized by three
parameters, volumetric concentrations, transfer areas, and time scales; and that all of
them can be included just in the timescale parameter dependencies; hence, that is possible
to determine TH process relevance with just one parameter. H2TS is divided into
two levels of analysis: the “top-down system scaling analysis” and the “bottom-up
process scaling analysis.”

## 3.5.8 Ishii three-level scaling

Ishii three-level scaling approach is a systematic methodology for designing IET facilities
as well as analyzing their generated experimental data relative to prototype conditions
. The bases of the methodology are the conservation principles and the
constitutive laws. This approach is divided into three levels of analysis, integral system
scaling, control volume scaling, and local phenomena scaling. The first two levels
correspond to the top-down scaling and the third level represents the bottom-up
scaling.

## 3.5.9 Fractional scaling analysis

Fractional scaling analysis (FSA) is a quantitative methodology based on the H2TS
approach that has been developed to facilitate two aspects:
l
scaling up of time-dependent evolution processes involving an aggregate of interacting modules
and processes (such as a NPP)
l
integration and organization of the information and data of interest to NPP design and safety
analyses.

## 3.5.10 Scaling distortion

Scaling distortion refers to any discrepancy between the scaled and the referenced
plant parameters. In a perfectly scaled experiment all the scaled parameters are
equally reproduced at the intended scaled time. Only in very limited cases, like very
specific SETs, perfect scaling is perfectly feasible. Usually, tests are rather complex
and they involve phenomena that need diverse scaling criteria for the design of the
scaled-down facility.
Following what is established in Buckingham π theorem, equations and laws can be
written in nondimensional form. A long list of nondimensional groups can be generated
to define similarity conditions. Nevertheless, all of them cannot be matched
simultaneously in the design of scaled-down facilities, and distortions will appear

<!-- page 117 (PDF 29) -->
once the analyst or the designer decides which are the most relevant to be preserved.
Analysis and justification of such distortions is one of the most significant purposes of
current scaling developments.

## 3.5.11 Counterpart tests/similar/special CP

Counterpart (CP) tests are tests performed in IET facilities of different scale with the
same initial and boundary conditions. Their purpose is to study effect of scale in the
behavior of the plant. If tests are properly designed and facilities have close configurations
, similarities in the time trends of important parameters have to appear and
the source of distortions have to be identified and explained. Such distortions have
to be mainly due to differences in configuration (Martı´nez-Quiroga, 2014;
Martinez-Quiroga et al., 2014; Martinez-Quiroga and Reventos, 2014).
Similar tests refer to some tests which, although they do not meet exactly the conditions
of a CP test, have a great similarity in the initial and boundary conditions. Similar
tests are at least useful to corroborate similarities expected in time trends of main
parameters.
A special CP test is a kind of scaled-down SET designed using full-scale test data as
reference and having the goal of clarifying the same phenomena and processes. In special
CP test, significant phenomena may be recorded at a higher level of detail.

## 3.5.12 Using system codes in scaling analysis

The use of system codes can help at every step of the analysis of complex transients.
As said in OECD/NEA/CSNI (2016c): “System codes can reduce the cost of manpower
by quickly doing evaluations that are done ‘by hand’ in H2TS and FSA. System
codes are not an alternative to scaling analysis, but they are a tool for assisting scaling
analysis and solving problems. For example, the identification of the phases of a transient
may be easier after some preliminary simulations of the transient using system
code, even before having simulated the transient with an appropriate IET.”
System codes also can identify (or help identify) the dominant processes and predict
how the relative importance of each process may change all along the transient.
They open the possibility of investigating phenomena that may be of second order
importance, but might require some attention.

## 3.5.13 Kv-scaled calculations

A Kv-scaled calculation is a system code simulation in which defined IET conditions
are scaled up to an NPP nodalization in order to reproduce the same scenario. It allows
the behavior of the NPP and ITF nodalizations to be compared under the same conditions
. Then it may be used to check the validity of the NPP nodalization and to
improve it when needed.
In the framework of qualifying the NPP nodalization and meeting its quality assurance
procedures, Kv-scaled calculations, introduced by D’Auria et al. (1995), are of
great value because they allow testing their capabilities and the plant’s response under
