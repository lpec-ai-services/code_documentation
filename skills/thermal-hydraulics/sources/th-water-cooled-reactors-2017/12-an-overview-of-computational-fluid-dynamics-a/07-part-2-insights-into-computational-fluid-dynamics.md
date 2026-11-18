# Part 2. Insights into computational fluid dynamics for nuclear power plant applications — CFD applications to nuclear thermal fluids problems — Applications of CFD
<!-- source PDF pages 50-51 -->

<!-- page 778 (PDF 50) -->
analyses. Such codes are based on networks of 1D or even 0D cells. However, the flow in
many reactor primary components is essentially 3D in nature, as is natural circulation,
mixing, and stratification in containments. CFD has the potential to treat flows of this type,
and to handle geometries of almost arbitrary complexity. Already, CFD has been successfully
applied to such flows, and to a limited extent has made up for a lack of applicable test
data in better quantifying safety margins. Consequently, CFD is expected to feature more
prominently in reactor safety analyses in the future.
l
Computational methods have been used in the safety analysis of reactor systems for nearly
40 years. During this time, very reliable numerical programs have been developed for
analyzing the primary system, and similar programs have also been written for modeling
containments and severe accident scenarios. Such codes model the reactor components as
networks of 1D or even 0D cells. It is evident, however, that the flows in many reactor
primary components are essentially 3D in character, as is natural circulation, mixing, and
stratification in containments. CFD has the potential to numerically simulate flows of this
type and to handle geometries of almost arbitrary complexity. Consequently, CFD is
expected to feature more prominently in reactor thermal-hydraulics analyses in the future
(OECD/NEA/CSNI/R(2014)3, 2014).
l
Traditional approaches to NRS analysis, using system codes for example, have been successful
because of the very large database of mass, momentum, and energy exchange correlations
that have been built into them. The correlations have been formulated from essentially 1D
special-effects tests, and their specific ranges of validity have been very well scrutinized.
Analogous data relating to 3D flow situations are very sparse by comparison. Consequently,
the issue of the validity range of CFD codes for 3D NRS applications is first to be addressed
before the use of CFD may be considered as routine and trustworthy, as it is, for example, in
the turbo-machinery, automobile, and aerospace industries. Assessment of the reliability of
CFD methodology in NRS applications represented the primary focus of the WG2 group
(OECD/NEA/CSNI/R(2014)3, 2014).
l
The application of CFD to nuclear thermal fluids problems is a broad topic that is hard to deal
with in a chapter. There are numerous CFD-related problems (OECD/NEA/CSNI/R(2014)3,
2014) that involve a broad spectrum of the CFD method. Hence, only addressing basic concepts
of respective CFD methods can make a series of books.
l
What we expect from the CFD analysis is to approach more realistic phenomena. In some
cases, it is expected that more detailed 3D phenomena obtained from CFD analysis can
improve previous 1D models. The CFD plays a certain role like an experiment in the 1D
model development. If the CFD is more time and cost-effective for a certain phenomenon
or problem than experiment, it has a clear advantage over experiment in that it can provide all
detailed information within the computational domain. Another prerequisite for this application
is the accuracy and reliability of the CFD methods and results. In other cases where it
is almost impossible to include 3D effect in 1D frame, CFD can be a part or even a main tool
in the entire analysis process for a given problem. The former case is needed when only using
CFD in the entire analysis process is neither time nor cost-effective.

### 12.9.2 Applications of CFD

#### 12.9.2.1 Usage of CFD: OECD/NEA/CSNI report

Selected nuclear reactor safety issues supposed to be addressed by CFD codes with or
without the coupling with system thermal-hydraulics (SYS TH) codes are listed in
Table 12.2 (OECD/NEA/CSNI/R(2014)3, 2014).

<!-- page 779 (PDF 51) -->
#### 12.9.2.2 CFD application procedures for nuclear thermal fluids problems

A general procedure for the CFD applications to the nuclear thermal fluids problems
can be summarized as follows: First, the key phenomena should be clarified because
this step critically affects the selection of the CFD models. Especially for an emerging
issue, this step is very important. Second, the selected CFD methods or models
become a CFD methodology for the problem. Third, a thorough assessment effort
for the selected CFD methodologies should be performed. The verification and validation
(V&V) and uncertainty quantification are key parts in the assessment step.
Feedback by trial and error and the multitude of V&V can establish best practice
guideline specific for the problem.

#### 12.9.2.3 Issues and notes

Selected issues and notes (or topics) are reported below which have already been implicit
or explicit part of discussion in other parts of the chapter. The issues and notes are:
l
Boundary and initial conditions are also important.
l
The simpler method requires more thought and multiple assessment procedures because
more impirical models are involved.
l
Application scope should be clear.

##### Examples of CFD application scopes

l
Understanding of 3D phenomena (Qualitative) evaluation of lower level code models
−
In-vessel mixing phenomenon: help identify the mixing laws used in the actual schemes
(systems codes, coupled system, 3D core thermal-hydraulic and neutronics codes) in use
l
For the part that needs 3D information
−
In-vessel mixing phenomenon: one could imagine integration of a CFD code into the
coupled chain: i.e., system, CFD, core 3D thermal-hydraulic and neutronics codes operating
together
l
Main:
−
In-vessel mixing phenomenon: if the capability of CFD codes is assessed for core
thermal-hydraulic simulation, one could imagine the use of CFD for lower plenum
and the core, coupled to 3D neutronics codes.

##### Variety of problems

l
Single-phase/multiphase
l
Chemical reaction
l
Conditions ranging from supersonic flow with shock waves to low-Froude-number buoyant
jets or mixed convection are possible
l
Natural convection
l
Fluid-structure interaction (FSI)—Steam generator tube vibration; fuel rod wear due to
grid-to-rod fretting (GTRF).

##### Necessity of geometry simplification

Induced break (This scenario is of direct safety relevance because it involves the
potential for a steam generator tube rupture during a severe accident scenario,
