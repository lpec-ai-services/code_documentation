# Part 2. Insights into computational fluid dynamics for nuclear power plant applications — CFD-related elements and definitions
<!-- source PDF pages 14-21 -->

<!-- page 742 (PDF 14) -->
Part 2. Insights into computational fluid
dynamics for nuclear power plant applications

## 12.6 CFD-related elements and definitions

This section aims at substantiating the statement in the Sword to Chapter 12 describing
the CFD technology as a building site with work in progress. Namely, the pieces, or
the equivalent of bricks, compounds, components, and subcomponents of different
nature (electrical, chemical, metal, and plastic industrial products in the building site)
for the CFD technology are defined or just mentioned below; this includes acronyms
which are considered in other parts of the chapter and are defined at the end of the
chapter. The current technological status is that various pieces are not integrated at
the time of writing of the book. In the subsequent sections (i.e., starting from
Section 12.7) snapshot type of details and insights are given.
The list of CFD topics (including open issues and question marks) to be considered
for a comprehensive presentation of its role in nuclear thermal hydraulics is as
follows:
−
“CFD.” Definition: Collection of solvers of physical models in a user interface. Physical
models.
Governing
equations:
Porous
medium
&
Open
medium.
Averaging:
volume-averaging, time-averaging, filtered Navier-Stokes equations. Interface models. Statistical
model (two-fluid model) and ITM (VOF, level set). Multicomponent models.
Lagrangian-Eulerian method.
−
“Application-1.” (i) Contents—(i-1) local, detailed results: providing data for other analyses
(e.g., thermal fatigue, vibration, CILC analysis); (i-2) 3D phenomena, e.g., asymmetric distribution
of flows in the reactor pressure vessel; improvement of 1D-based model (in system
code); (ii) Format/method: coupling with system code.
−
“Application-2.” (i) A part of multiphysics and multiscale analysis, i.e., needing coupling
with separate analyses and codes in different areas or related calculation results; (ii) As a
fully integrated and self-standing multiphysics and multiscale analysis.
−
“Application-3.” What system codes (and experiments) cannot do (well).
−
“Nuclear Thermal Fluids Problems.” Design evaluation and optimization; experimental
design evaluation; safety and performance analyses; methodology evaluation in regulatory
process (e.g., Boyd, 2016).
l
Introduction to CFD discussion – Background. Many uses of CFD computational
tools are possible. A broad spectrum of applications can be derived from the analysis
of the literature. Various aspects having different origin and implication are relevant:
some of these are discussed in Foreword, Abstract, and in the Introduction to Part 1 of this
chapter.
l
CFD code. A code can be seen as the collection of multiple numerical solvers for fluid
dynamics, heat transfer, and the interface in the case of two-phase flows. Coupling among
different solvers may be needed, as well as coupling between CFD codes and codes in other
areas, like structural analysis, chemical reaction, and radiation heat transfer (see
Section 12.10, below).
−
Solver: A solver is a generic term indicating a piece of mathematical software, possibly in
the form of a stand-alone computer program or as a software library that “solves” a

<!-- page 743 (PDF 15) -->
mathematical problem. A solver takes problem descriptions in some sort of generic form
and calculates their solution. In a solver, the emphasis is on creating a program or library
that can easily be applied to other problems of similar type (e.g., see also
Wikipedia-related definitions).
−
Assessment of “CFD code.” Assessment is used here as synonymous of the second “V” in
the acronym V&V (i.e., validation). Open question is: Is assessment right? Namely,
assessment of “System code” makes sense (Chapter 13), but assessment of “CFD code”
isveryambiguousbecauseinmanycasesweusepartialCFDcodes,e.g.,becausetheword
CFD is sometimes associated with codes like GOTHIC, GASFLOW, and COBRA, e.g.,
see Westinghouse (2014), Thurgood et al. (1983), and Xiao et al. (2016), respectively.
l
Introduction – Motivation. Open question is: Is the right image of CFD available to decision
makers and end users? Streamlines for addressing the questions are:
–
Possibly, more focus is provided on multiphysics than on CFD itself;
–
The image of CFD is biased by the idea of system codes;
–
There is the misunderstanding that the products are dependent on purpose;
–
The application targets may reveal either too ambitious or too loose;
–
There can be overconfidence in the results or the temptation to neglect the related
implications;
–
A broad spectrum of CFD codes and methods is available for application and the selection
of the best code or the best method may reveal difficulty;
–
In all cases difficulties may arise in demonstrating the validation of the process of code
application or the quality level of results.
l
Differences of CFD codes from system (SYS TH) codes. The following differences are
emphasized
(1) Governing equations are very important in CFD code applications, while the governing
equations are fixed in SYS TH codes and modeling effects connected with constitutive
equations (see Chapter 9) are dominant;
(2) Meshing has infinite degree of freedom and a key factor affecting the results in
CFD codes;
(3) Typically, solutions of balance equations in SYS TH codes are obtained in control
volumes bounded by solid walls; this is not the case for CFD codes;
(4) Averaging is needed in control volumes in the case of SYS TH codes;
(5) LimitationofCPUresourcesisanimportantfactorfortheselectionofmethodsinthecase
of CFD code; the same limitation may not apply in the case of modern SYS TH codes;
(6) Application range should be selected carefully in the case of CFD codes; application
ranges for SYS TH codes may be broader and properly fixed by the validation process;
(7) The spectrum of application models in CFD codes may reveal wider (i.e., overpassing
the boundary of interest for nuclear thermal hydraulics);
(8) The validation process for CFD codes may reveal more complex than for SYS TH codes
(9) the computational domain and boundary condition effects are critical to accuracy in
both CFD and SYS TH codes; however the criticalities and the impact upon accuracy
of results may be different;
(10) CFD codes are in principle able to provide new phenomenological results; this capability
is not expected from the application of SYS TH codes.
l
What system (SYS TH) codes cannot do:
–
full prediction of three-dimensional phenomena;
–
prediction of local (transient) phenomena;
–
detailed consideration (modeling) of geometrical effects.

<!-- page 744 (PDF 16) -->
l
The Ideal and the real in CFD NTF.
−
The ideal: we assume that the results are accurate and reliable; we trust in
three-dimensional and local calculated data; we assume that all information in the computational
domain are available to the (CFD) analysts; we accept all transient data, i.e.,
whatever characteristics of fluctuation intensity and frequency values; we obtain positive
results from sensitivity study performed by adopting the method that showed good
agreement with benchmark data;
−
The real: We need to calibrate models to match the results of experiments if available
(e.g., for the validation process); we note that even calibration cannot produce good
results in most cases; we realize that broad methodology comparisons (e.g., through
round robin benchmark) are needed but are not available; we realize that higher level
calculations (HPC, High Performance Computing) are required and not available:
namely, HPC results are needed for the systematic calibration for the lower level
calculations;
l
What CFD codes can do. In general, CFD can do what system code and/or experiments
cannot do (3D effect, local phenomenon) or cannot do well, i.e., in a satisfactory way.
Specific additional examples are given below.
−
Finding new problems/issues: this includes phenomena-finding like fluid velocity reversal
in rod bundle with split-type mixing vane grids;
−
Reducing conservatism: specifically in relation to local phenomena like occurrence of
CHF or DNB conditions and formation of crud layer over fuel pins (so-called CILC
occurrence);
−
Developing/Improving models: examples are constituted by “weak” models used by
SYS TH codes like those used for two-phase critical flow (TPCF) (e.g., Guyot et al.,
2016) or for heat transfer in highly time-dependent transient conditions (RIA) (see
e.g., Baudin et al., 2016).
−
Explaining the reason/causes: one example is to analyze and measure the void fraction at
the inlet of an electric submersible pump (ESP) and the effect of the gas in the head
delivered by the first stage of this pump (Pineda et al., 2016).
−
Providing data that would be used in other analyses: examples are the coupling with
other codes (Section 12.10 below), like thermal fatigue, formation of crud. In this connection
a right balance should be achieved between detail level requested and level of
detail (complexity, cost, and qualification) available from CFD analysis.
−
Evaluating CFD: this means to evaluate other CFD results with higher level turbulence
simulations, e.g., achieved by HPC or by the application of LES level turbulence models;
within the same framework, for a specific problem this implies evaluating the results
from lower level turbulence models (such as steady RANS) or enabling the improvement
of them by a priori and a posteriori tests.
l
Variety of problems: The variety of problems which can be addressed by CFD analysis
includes the following (only representative examples are given) analyses of:
−
Single-phase/multiphase;
−
Chemical reaction;
−
Conditions ranging from supersonic flow with shock waves to low-Froude-number
buoyant jets or mixed convection are possible
−
Natural convection;
−
Fluid-structure interaction (FSI);
−
Steam generator tube vibration;
−
Fuel rod wear due to grid-to-rod fretting (GTRF).

<!-- page 745 (PDF 17) -->
l
List of NRS single-phase problems. A list of nuclear reactor safety issues of interest for CFD
applications is derived by a recent document published by OECD/NEA/CSNI (OECD/NEA/
CSNI/R(2014)3, 2014). The list includes:
−
Boron dilution (DBA conditions);
−
Mixing: stratification/hot-leg heterogeneities (NPP normal operation conditions), also
multiphase conditions;
−
Heterogeneous flow distribution (e.g., NPP normal operation conditions in SG inlet
plenum causing vibrations, the analysis of HDR experimental data, etc.);
−
BWR/ABWR low plenum flow (NPP normal operation conditions), also multiphase
conditions;
−
Pressurized thermal shock, PTS, (DBA), also multiphase conditions;
−
Induced break, e.g., by pipe whip or missile generated by the break of components like
main coolant pump (DBA);
−
Thermal fatigue, e.g., caused at any T-junction (NPP normal operation conditions);
−
Hydrogen distribution (BDBA), also multiphase conditions;
−
Chemical reactions/combustion/detonation (BDBA), also multiphase conditions;
−
Special considerations for advanced (including gas-cooled) reactors (DBA/BDBA), also
multiphase conditions.
l
Difficulties in nuclear thermal fluid problems. When we apply the CFD methods to nuclear
thermal fluids problems, we encounter several difficulties, as discussed by Boyd (2016):
−
Complex geometry: This makes it difficult to generate computational grids and cause the
computational load. In general, the geometry is simplified; however, to ensure the
reliability of the simplified geometry results, additional efforts are required.
−
Uncertain and complex flow behaviors.
−
Uncertain boundary and initial conditions.
−
Lack of benchmark data (CFD grade, full-scale data).
−
Lack of similar research and references.
l
Reactor core performance-related challenging problems. A nonexhaustive list includes
pellet-clad interaction (PCI), grid-to-rod fretting, crud formation (CILC), cladding integrity
in case of reactivity insertion accident (RIA), cladding integrity in case of loss of coolant
accident (LOCA), namely when challenged by the occurrence of ballooning, occurrence
of departure from nucleate boiling, (DNB) phenomenon. Reference literature related to listed
topics is given by, see e.g., Kothe et al. (2010), Kothe (2011), and Kothe (2015).
l
Various aspects—Safety, Operation, Design. Detailed information can be found in the
CASL (the Consortium for Advanced Simulation of Light Water Reactors) website, see
e.g., Kothe et al. (2010), Kothe (2011), and Kothe (2015). A summary list of safety aspects
in nuclear thermal hydraulics, part of CASL, is given in Fig. 12.1.
Various Standpoints. Stakeholders in the area of CFD can be listed as follows: CFD User
Community (Utility Owner-Operators, Reactor Vendors, Fuel suppliers, Engineering
providers, and National Laboratories), Regulatory Authority, Universities and Research
Laboratories, and Public.
l
Operational and Safety Issues limiting reactor performance. Recent orientations for NRS
applications can be found in the CASL DOE project in United States, as given in
Fig. 12.2, Kothe et al. (2010), Kothe (2011), and Kothe (2015). Phenomena expected within
the DBA in water-cooled reactor are proposed by OECD/NEA/CSNI and listed in
Table 12.1, see Aksan et al., 1993; the same phenomena are updated and discussed in detail
in Chapter 6. Making reference to Table 12.1, phenomena in row 10 are of special interest for
CFD applications.

<!-- page 746 (PDF 18) -->
l
Deficiencies that CFD code validation for NRS applications frequently encounters.
Deficiencies in CFD code validation have been the target of recent activities performed
within the CSNI-WGAMA framework, see e.g., OECD/NEA/CSNI/R(2014)3, (2014),
Smith et al. (2015), and Bestion et al. (2016). A summary list of deficiencies is summarized
as follows in those reports (not an exhaustive list and including some modifications introduced
by the present author):
−
PIRT for the intended application is not available in a systematic way.
−
Quantified estimates of experimental (measurement error) and numerical uncertainties
(approximations introduced by numerical methods) are not provided.
Safety
Operating
Design
•  DNB safety limit
•  DNB operating limit
•  LHGR limit
•  PCI
•  Coolant activity
•  Gap activity
•  Source term
•  Control rod drop time
•  RIA fuel failure limit
•  Crud deposition
•  Stress/strain/fatigue
•  Oxidation
•  Hydride concentration
•  Transport loads
•  Fretting wear
•  Clad diameter increase
•  Cladding elongation
•  Radial peaking factor
•  3D peaking factor
•  Cladding stability
•  Reactivity coefficients
•  Shutdown margin
•  Enrichment
•  Internal gas pressure
•  PCMI
•  RIA fragmentation
•  Non-LOCA runaway oxidation
•  LOCA: PCT, oxidation,
   H release, long-term cooling
•  Seismic loads
•  Holddown force
•  Criticality
Fig. 12.1 CASL: list of safety, design, and operational aspects in nuclear technology relevant to
CFD (Kothe, 2015).
Courtesy of Oak Ridge National Laboratory, U.S. Dept. of Energy.
¥
¥
¥
¥
¥
¥
¥
¥
¥
¥
¥
¥
¥
¥
¥
¥
¥
¥
Power uprate
High burnup
Life extension
Operational
CRUD-induced power shift (CIPS)
CRUD-induced localized corrosion (CILC)
Grid-to-rod fretting failure (GTRF)
Pellet-clad interaction (PCI)
Fuel assembly distortion (FAD)
Safety
Departure from nucleate boiling (DNB)
Cladding integrity during loss of coolant accidents (LOCA)
Cladding integrity during reactivity insertion accidents (RIA)
Reactor vessel integrity
Reactor internals integrity
Fig. 12.2 CASL: list of key phenomena challenging CFD applications in nuclear technology
(Kothe, 2015).
Courtesy of Oak Ridge National Laboratory, U.S. Dept. of Energy.

<!-- page 747 (PDF 19) -->
Table 12.1 List of phenomena for separate-effect tests derived from
accident analysis of water-cooled reactors (Aksan et al., 1993)
0. Basic phenomena
1. Evaporation due to
depressurization
2. Evaporation due to heat input
3. Condensation due to
pressurization
4. Condensation due to heat removal
5. Interfacial friction in vertical flow
6. Interfacial friction in
horizontal flow
7. Wall to fluid friction
8. Pressure drops at geometric
discontinuities
9. Pressure wave propagation
1. Critical flow
1. Breaks
2. Valves
3. Pipes
2. Phase separation/vertical flow with and
without mixture level
1. Pipes/plena
2. Core
3. Downcomer
3. Stratification in horizontal flow
1. Pipes
4. Phase separation at branches
1. Branches
5. Entrainment/deentrainment
1. Core
2. Upper plenum
3. Downcomer
4. Steam generator tube
5. Steam generator mixing
chamber (PWR)
6. Hot leg with ECCI (PWR)
6. Liquid-vapour mixing with condensation
1. Core
2. Downcomer
3. Upper plenum
4. Lower plenum
5. Steam generator mixing
chamber (PWR)
6. ECCI in hot and cold leg (PWR)
7. Condensation in stratified conditions
1. Pressurizer (PWR)
2. Steam generator primary
side (PWR)
3. Steam generator secondary
side (PWR)
4. Horizontal pipes
Continued

<!-- page 748 (PDF 20) -->
−
Validation metrics, figures of merit, or target values for the error for the intended application
are not defined.
−
Experiments, selected for validation at some of the tiers, do not meet all intended requirements
one would like to have on validation experiments. Since validation experiments are
very expensive, experiments intended for other purpose (e.g., for the study of physical
phenomena or for the development of physical models), or very old experiments
Table 12.1 Continued
8. Spray effects
1. Core (BWR)
2. Pressurizer (PWR)
3. Once-through steam generator
secondary side (PWR)
9. Countercurrent flow/countercurrent flow
limitation
1. Upper tie plate
2. Channel inlet orifices (BWR)
3. Hot and cold leg
4. Steam generator tube (PWR)
5. Downcomer
6. Surge line (PWR)
10. Global multidimensional fluid temperature,
void and flow distribution
1. Upper plenum
2. Core
3. Downcomer
4. Steam generator secondary side
11. Heat transfer:
Natural or forced convection
Subcooled/nucleate boiling
DNB/dryout
Postcritical heat flux
Radiation
Condensation
1. Core, steam generator, structures
2. Core, steam generator, structures
3. Core, steam generator, structures
4. Core, steam generator, structures
5. Core
6. Steam generator, structures
12. Quench front propagation/rewet
1. Fuel rods
2. Channel walls and water rods
(BWR)
13. Lower plenum flashing
14. Guide tube flashing (BWR)
15. One and two phase impeller-pump behaviour
16. One and two phase jet-pump behaviour
(BWR)
17. Separator behavior
18. Steam dryer behavior
19. Accumulator behavior
20. Loop seal filling and clearance (PWR)
21. ECC bypass/downcomer penetration
22. Parallel channel instabilities (BWR)
23. Boron mixing and transport
24. Noncondensable gas effect (PWR)
25. Lower plenum entrainment

<!-- page 749 (PDF 21) -->
performed in (today) dismantled facilities are sometimes used. The last deficiency also
prevents feedback between CFD simulations and experiments.
−
For some physical phenomena identified in the PIRT (when this is available) the
experiments at the basis of the PIRT evaluation are not identified: in those cases,
new experiments must be proposed.
−
Validation simulations cannot provide information on boundaries of regions of acceptability
of the conceptual model from regions where the model cannot be applied or
where its application is questionable. In other terms boundary of validity for the applicability
of the codes is not available.
l
Main questions and issues.
Selected key questions and (unresolved) issues that should be considered by the CFD community
of code and model developers as well as by users and (possibly) by end users are
summarized in the following:
−
Main Question 1: From where do we start (e.g., for developing a new CFD model)? What
we (e.g., CFD code-user or model developer) can do and what do we need (goal-directed
activity to be performed)? Triggering statements and recommendations to address the
questions in nuclear thermal hydraulics are as follows: There is no single starting point,
and a wide basis of competences, information, and data is needed to start. Concerned
knowledge elements must be connected among each other and should constitute a system
at the end. The assimilation of information available from recognized technical literature
is essential. For instance, system code-based V&V, UQ, and general CFD
methodologies discussed in international agreed CSNI reports (Mahaffy et al., 2007a,b;
OECD/NEA/CSNI/R(2014)3, 2014; Smith et al., 2015; Bestion et al., 2016) must be
considered. Proper importance must be given to review the activity by senior experts
and taking into account previous research and data. In some cases the target of activities
should be limited by the statement “change unknown knowns into known unknowns.”
−
Main question 2: What are the differences in methodological approaches between
CFD and other areas? E.g., CFD model development vs. experiments design, planning,
and execution; CFD vs. SYS TH codes; CFD code “A” vs. CFD code “B.” A hint for
addressing this question may be taken from considering the topics listed below:
(1) CFD-level experiments must be defined and planned. Experiments used to develop and
to validate SYS TH codes must be considered. Phenomena (relevant to nuclear thermal
hydraulics) should be targeted, possibly defining a series of intermediate targets.
(2) Specific set of experiments must be planned for CFD code validation: those experiments
must be independent from experiments used or considered to develop the
CFD models.
(3) System codes V&V and UQ must be considered.
(4) An attempt should be made to define the meaning of CFD scaling. Possibly, the
scaling activities performed in relation to SYS TH codes (see e.g., ongoing efforts
by CSNI and ASME) should be considered.
(5) etc.
−
Main Question 3: What do we need to do in the future? Some recommended directions
are listed below:
(1) Right goal setting: this includes distinguishing short-term and long-term targets;
different (simultaneous) directions for research could reveal necessary.
(2) Goal set 1: qualitative and quantitative targets should be distinguished; this
includes different acceptance methods and thresholds for results.
(3) Accumulation of experience in the application of specific methodologies, like
BPG: Develop problem-specific BPG as many as possible and consider knowledge
management techniques.
