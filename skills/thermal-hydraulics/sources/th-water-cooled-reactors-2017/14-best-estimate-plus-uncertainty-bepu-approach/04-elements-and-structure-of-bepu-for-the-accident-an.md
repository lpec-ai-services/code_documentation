# Elements and structure of BEPU for the accident analysis
<!-- source PDF pages 17-27 -->

<!-- page 921 (PDF 17) -->
the principles of civilization including reasons for staying together and, possibly, a
strategy for the sustainability. Once “coordinated individuals” enter the ghost city
rules are created and established. The effort by the “coordinated individuals” may
have a success and the empty town becomes a living town. Under those circumstances,
the wild traveler may become a citizen.
The word civilization may be used to gather all the actions and activities which
transform the ghost city into a living town. In a similar way the BEPU approach
includes all the steps needed for the application of nuclear thermal hydraulics within
nuclear reactor safety. The wild traveler or the thermal hydraulics expert becomes a
citizen or a nuclear reactor safety analyst when he is capable to apply BEPU.
Now, what is BEPU? The BEPU definitely allows a nuclear thermal-hydraulic specialist
to become a maven. A comprehensive explanation of BEPU is equivalent to the
explanation of the process bringing the empty town to become alive and populated by
citizens (not wild travelers). Finally, one may state:
BEPU □ CIVILIZATION
Therefore, even the bases for BEPU may require a deep description, i.e., inconsistent
with the framework and the size of the present document.
14.3
Elements and structure of BEPU for the
accident analysis
In this section the BEPU concept is restricted to the accident analysis part of safety
evaluation for individual NPP and to the current status in its application in technology.
The main objective of the chapter, like the previous one, is to contribute or provide
information suitable for characterizing BEPU avoiding as far as possible duplication
of information from other chapters.

## 14.3.1 Selected key terms

A wide variety of terms, noticeably involving acronyms, which are related to the definition
of BEPU, have already been used in previous sections of this chapter and in
other chapters, namely Chapter 3. Hereafter, a series of terms which are essential
for understanding BEPU are listed together. Added descriptions for each term are provided
to focus on the connection with BEPU.

### 14.3.1.1 DBA & BDBA

The DBA framework fixes the boundary for specific (restrictive) nuclear safety
requirements, thus reflecting on SYS TH code development, related V &
V including scaling, uncertainty evaluation, and application procedures. One key
BEPU basis is constituted by the V & V requirements.

<!-- page 922 (PDF 18) -->
### 14.3.1.2 Deterministic & probabilistic accident analysis

Definitely BEPU approach and related procedures are originated within the Deterministic
Safety Assessment (DSA) technology. The need and the importance to connect
PSA and DSA within BEPU are discussed in different parts of this document (e.g., see
Section 14.3.2).

### 14.3.1.3 Risk informed regulation

The words “risk informed” (regulation) where introduced in the 1990s and reflected in
a key document issued by IAEA, e.g., IAEA (2011). Adopting some oversimplification
one may state that (full) integration of DSA and PSA also includes the consideration
of risk-informed regulation.

### 14.3.1.4 Safety margins

The evaluation of safety margins (SM) is the key goal for safety analyses including
NPP licensing process. The evaluation of SM implies the calculation of related quantities
or Q-SM. A number of additional variables are needed to be computed in order to
calculate the Q-SM. BEPU aims at achieving qualified calculations of SM. BEPU
types of analysis shall be considered also for NPP design and operation, as already
discussed in this document. Then one may state that BEPU is expected to provide
a framework where the calculation of all physically relevant quantities is required
and proper qualification is pursued: i.e., Q-SM values shall have qualification and
qualification is expected for non Q-SM values. Additional discussion can be found
in Section 14.4.3 of this document, see also D’Auria et al. (2015).

### 14.3.1.5 Sensitivity & uncertainty

Sensitivity and uncertainty are key activities to estimate the error expected or characterizing
SYS TH code calculation results. The difference between sensitivity and
uncertainty is shortly outlined hereafter, having in mind the uncertainty methods
based on the propagation of input errors as discussed in Chapter 13 (see also Adu
et al., 2015).
Sensitivity analyses may be worthwhile when carried out in relation to any input
parameter within any range of variation; uncertainty analysis shall be carried out in
relation to those input parameters which are at the origin of the uncertainty in code
calculations and related ranges of variations shall be properly defined to account
for the approximations unavoidable in the overall (calculation) process.
Both sensitivity and uncertainty are of interest within a BEPU approach.

### 14.3.1.6 Accuracy & uncertainty

Accuracy is the known error which characterizes the comparison between measured
and calculated values, e.g., Ambrosini et al. (1987) and Kalli et al. (1995); uncertainty
is the unknown error which characterizes the calculation (or prediction) of NPP transient
performance, e.g., IAEA (2008).

<!-- page 923 (PDF 19) -->
Gathering of accuracy database is necessary to show the qualification of a BEPU
process, and uncertainty is part of the BEPU acronym.

### 14.3.1.7 Reliability & uncertainty

Reliability and reliability analyses constitute key concepts or even established technologies
inside the PSA framework and are not considered. Here the word reliability is
restricted to passive thermal-hydraulic systems and to physical phenomena expected
during their operation.
In this situation, e.g., passive systems and phenomena, reliability can be calculated
with methods similar to those adopted for uncertainty analysis, see e.g., D’Auria and
Galassi (2000), Jafari et al. (2003), and Marques et al. (2005). The comment here is
that reliability analysis related to the design of a system and uncertainty analysis
related to the error of a calculation.
Reliability analysis is important within a BEPU approach where passive systems
are considered.

### 14.3.1.8 Bounding approach

Bounding approach are not frequently used terms to signify one analysis where minimum
conservatism is adopted, see e.g., Zhang et al. (2011). In an oversimplified way
one may state that bounding approach is an intermediate step between conservative
and best-estimate approach. The bounding approach is not expected to have a role
within a BEPU process.

### 14.3.1.9 BE & conservative code

The meaning of BE and conservative code is discussed in other parts of the book, e.g.,
Chapters 1, 2, and 13, see also Table 14.1 in this chapter, where “option 1” and “option
2” deal with conservative analyses. BEPU can be (and must be) used to quantify the
amount of conservatism as already stated (Stanev and D’Auria, 2001; D’Auria et al.,
2001). Only BE codes are of interest within the BEPU framework.

### 14.3.1.10 Conservative & realistic input data

Conservative and realistic input data can be used for BE codes as foreseen by the
“option 2” and the “option 3” in Table 14.1 in this chapter. Only realistic input data,
properly characterized by errors, i.e., input uncertain parameter ranges, are of interest
within the BEPU framework.

### 14.3.1.11 Conservative & realistic assumptions

Realistic assumptions are considered at any step of the application of a BEPU process.
However, conservative assumptions are part of BEPU approaches when related to the
intervention of ECCS, according to the “option 3” in Table 14.1 in this chapter.

<!-- page 924 (PDF 20) -->
## 14.3.2 The elements

Let us define a BEPU element as follows: any software, procedure, or a dataset which
is needed to perform a BEPU application in the area of NPP accident analysis. The key
elements for BEPU shall be derived from the envision provided in Section 14.2.3 and
from selected key terms in Section 14.3.1.
A not exhaustive (minimum) list of BEPU elements is provided hereafter: the
nuclear thermal-hydraulics framework should be considered as element “zero” of
BEPU and is not part of the list; furthermore, items are given not necessarily in the
logical order of application or in any order of importance.
l
Computational tools/SYS TH codes—design and development
l
Computational tools/SYS TH codes—V & V procedures
l
Computational tools/SYS TH codes—procedures for application
l
Computational tools/nodalizations (or input decks)—development
l
Computational tools/nodalizations—V & V procedures
l
Computational tools/code-coupling software—design and development
l
Uncertainty methods/design and development
l
Uncertainty methods/qualification procedures
l
NPP parameters database
l
PIE
l
Phenomena/physical aspects which characterize PIE
l
Databases for code and nodalization qualification
l
Scaling demonstration/procedures and database
l
Users of computational tools/qualification
l
DSA—PSA integration
l
I & C modeling
l
Documentation requirements for each elements
l
Licensing framework—acceptance criteria, SM, procedures, etc.
Additional notes are provided hereafter for some of the elements (e.g., those not considered
in other chapters or in Sections 14.2 and 14.3).
Procedures for SYS TH V & V: In addition to the information in Chapter 13, the
recently completed activity within the framework of IAEA shall be considered in relation
to V & V procedures for SYS TH codes involved within the application of a
BEPU approach, e.g., IAEA (2016).
Procedures for SYS TH code application: The application of SYS TH code to the
BEPU accident analysis is not straightforward: the availability of a code, eventually of
a specific NPP input deck (or nodalization) and of analysts capable of running the
code, does not guarantee the achievement of valid or acceptable results. A variety
of checks are needed (see also below). When an NPP nodalization is available to perform
accident analysis, i.e., ready for the final stage of the code application process,
the Kv-scaled procedures already introduced to support the application of an uncertainty
method are recommended or necessary (D’Auria et al., 1995). The procedure
implies the comparison between calculated NPP transient performance and experimental
data gathered from a suitable Integral Test Facility (ITF) where a
scaled-down experiment has been performed simulating the concerned NPP transient.

<!-- page 925 (PDF 21) -->
Examples of Kv-scaled applications, including substeps and conditions for the analysis
, can be found in the papers by Martinez-Quiroga and Reventos (2014) and
Martinez-Quiroga et al. (2014).
Nodalizations development and qualification: The nodalization or input deck is
tightly connected with the SYS TH code when accident analysis is performed. Importance
for nodalization qualification and related requirements can be found in the paper
by Bonuccelli et al. (1993): criteria are proposed for the acceptance of nodalization
development, for the achievement of steady state and for demonstrating acceptability
of transient results (“on-transient qualification”).
Code coupling software design and development: Coupling among codes derived
for various technologies is essential for performing BEPU analyses; see also Fig. 2.8
in Chapter 2 and related discussion. Creating the interface between different software
aiming at calculating time transients implies new software and related qualification,
e.g., see D’Auria et al. (2004) and D’Auria et al. (2010), both related to coupling in the
areas of thermal hydraulics and neutron physics.
NPP parameters databases: BEPU databases must be created and managed.
A wide variety of databases are needed as discussed by D’Auria (2001), Petruzzi
et al. (2012), Kovtonyuk et al. (2013), Petruzzi and D’Auria (2014), and D’Auria
(2015); see also “BEPU as the exploitation of database” in Section 14.2.3.
PIE: Internal and external PIE need to be properly considered aiming at NPP safety
evaluation. Within the thermal-hydraulics area internal PIE are of interest. These are
discussed in Section 14.3.3, e.g., see IAEA (2002). The BEPU framework and procedures
have the capability to make “robust” and consistent the consideration of
external PIE.
Phenomena and physical aspects: Thermal-hydraulic phenomena expected to be
relevant within the DBA envelope are discussed in Chapter 6 (OECD/NEA/CSNI,
1993, 1996) (see also references listed in Chapter 1). Phenomena and physical aspects
constitute the link between BEPU and the experimental reality.
SYS TH code user training and qualification: The availability of a qualified code
and of a qualified nodalization, as well as of qualified uncertainty procedure, does not
guarantee a qualified BEPU calculation in nuclear thermal hydraulics (NPP accident
analysis). A qualified group of code users and analysts is needed as discussed by
Aksan et al. (1993), D’Auria (1998), Ashley et al. (1998), and Petruzzi et al.
(2011), and in the IAEA (2016), technical guidance document.
I & C modeling: The full modeling of the I & C of the concerned NPP constitutes an
essential requirement for the application of a BEPU approach as discussed by D’Auria
et al. (2012b). Following any PIE, I & C of existing NPP has the task and the capability
to bring the current operating status far from the original one which characterizes the
PIE under concern. This causes a variety of consequences in the analysis of accidents,
as also discussed in IAEA (2015b) (a synthesis of concerned items is provided below):
l
The effectiveness and efficiency of regulatory design reviews are decreased owing to the
extreme difficulty that vendors have in producing a fully standardized and documented design.
l
Uncertainties intervene in the licensing processes and analyses which currently discourage
the adoption (and the consideration) of new systems and technology to analyze I & C.

<!-- page 926 (PDF 22) -->
l
Difficulties emerge with the reuse of previously licensed technical solutions for a large spectrum
of applications and hence affect the validity of actual safety evaluations.
l
Limitations exist in the development of competency on a global basis (i.e., it is difficult to
create an expertise “parallel” to the expertise of the licensee), thus making the resolution of
complex licensing issues more difficult.
Procedures within licensing framework: Procedures shall be derived from the licensing
framework. However specific procedures need to be introduced consistently with
the licensing framework. A sample, and not exhaustive list of procedures, basically
providing an idea of the types of procedures, includes:
-
Harmonizing the regulations in the country where the NPP is built and the country where the
same NPP is designed or where licensing experience exists.
-
Establishing a direct connection between technical specifications for the operation of components
(typically Chapter 16 of FSAR) and the results of safety analysis (i.e., Chapter 15
of FSAR).
-
Establishing the duration of transient calculations, consistently with the need to demonstrate
the licensing requirements.
-
Application of uncertainty methods including cases where wide SM are predicted by BE
calculation.
-
Establishing the list of PIE, based on available or specific PSA (see discussion in
Section 14.3.3).

## 14.3.3 The concerned events

An idea of the PIE can be derived from IAEA (2002); see also USNRC (2005):
Grouping by principal effect leading to potential degradation of fundamental safety
functions leads to the following event categories considered typically in the reactor
design:
l
Increase in heat removal by the secondary side,
l
Decrease in heat removal by the secondary side,
l
Decrease in flow rate in the reactor coolant system (RCS),
l
Increase in flow rate in the RCS,
l
Anomalies in distributions of reactivity and power,
l
Increase in reactor coolant inventory,
l
Decrease in reactor coolant inventory,
l
Radioactive release from a subsystem or component.
Each category of events is typically subdivided into several more specific events.
Events which are expected to occur during the plant lifetime are called AOOs (anticipated
transients). Some of those events are also analyzed under the assumption of a
complete failure of the fast reactor shutdown system and are called ATWS. Additional
variations for each individual event are obtained by considering various plant operational
states (e.g., burn-up or boron concentration when the PIE occurs) at the time of
the accident. “Radioactive releases” include events which do not represent the

<!-- page 927 (PDF 23) -->
consequences of another event given above; i.e., the release is a direct result of the
failure of the component which contains radioactive material.
Grouping by principal cause of the initiating events considered in the reactor design
leads to the following categories:
l
Reactivity anomalies due to control rod malfunctions,
l
Reactivity anomalies due to boron dilution or cold water injection,
l
Coast down of the main circulation pumps,
l
Loss of PS integrity (LOCA),
l
Interfacing systems LOCA,
l
Loss of integrity of secondary system,
l
Loss of power supply,
l
Malfunctions in the PSs,
l
Malfunctions in the secondary systems,
l
ATWS,
l
Accidents in fuel handling,
l
Accidents in auxiliary systems,
l
Accidents due to external events.

## 14.3.4 The needed resources

The following resources typologies are needed to perform a BEPU application
l
Computational tools: codes in various areas, see e.g., Fig. 2.8 in Chapter 2;
l
Computational tools: nodalizations (or input decks) to run the codes;
l
Computational tools: software for coupling the codes;
l
Uncertainty Method;
l
Computers;
l
Group of Analysts and Experts;
l
Databases to demonstrate qualification and applicability of computational tools as well as to
apply uncertainty method.
In order to provide an idea for the amount of resources needed for BEPU application,
the following can be considered, in each case distinguishing between minimum number
of analysts-experts ①(not necessarily working full time all together), rough man-years
effort ②(equivalent effort including availability of computational tools and management
effort), and minimum time needed to complete the activity in years ③:
(A) To perform LBLOCA analysis:
①: 3
②: 10
③: 3
(B) To perform the overall accident analysis
(Chapter 15 of FSAR):
①: 30
②: 150
③: 4
(C) To consider the entire FSAR:
①: 100
②: 500
③: 5
Experience related to activities at items (A) and (B) is available, e.g., Galetti and
D’Auria (2005), and UNIPI-GRNSPG (2008); the framework related to item
(C) can be found in the paper by D’Auria et al. (2015), see also Section 14.4.2.

<!-- page 928 (PDF 24) -->
## 14.3.5 The roadmap

The BEPU roadmap can be considered as the end result of the BEPUplanning, the
origin of the BEPU application, and the consistent assembly of BEPU features. Thus,
a variety of roadmaps can be envisaged. In the case considered below, the BEPU
approach was pursued having access to the original designer delivered information,
but independently from designer.
A sketch of the BEPU roadmap at the basis of the application for Chapter 15 of the
FSAR of the Atucha-2 NPP can be found in Fig. 14.3.
Atucha-2 info: KWU-Siemens-AREVA German design, about 800 MWe, vessel
type, natural uranium, heavy water coolant and moderator, 2 loops with SG for power
production and 4 loops for moderator cooling, full power operation attained in 2015,
final license for operation attained in 2016.
Three parallel paths are possible for each PIE (see Fig. 14.3):
l
CSA (yellow color): Scenarios which are used for assessing the design and demonstrating the
acceptability of ECCS, safeguards, or countermeasures, i.e., evaluation of systems performance
associated with the integrity limits for the safety barriers against radioactive releases.
l
RCA (pink color): Scenarios which are used as bounding (of other scenarios) for estimating
the radiological impacts and demonstrating compliance with regulatory limits set at the
territorial boundaries of the NPP unit.
l
CBA (green color): Scenarios which are used for assessing the structural design of components
or structures for demonstrating stability or integrity, i.e., implying the calculation of
mechanical design loads and stresses.
The diagram shall be entered at item 1 in Fig. 14.3 for a logical interpretation.
A preventive safety study is performed including probabilistic analysis where the
boundary conditions of “enveloping transients” for safety analysis are identified.
The “purposes for the analysis” of those transients shall be introduced according to
the safety needs. Three areas are concerned, corresponding to CSA, RCA, and
CBA, respectively:
(a) “Typical” ECCS design confirmation analysis (CSA in the diagram), e.g., aiming at demonstrating
compliance with criteria in 10 CFR 50.46, USNRC (and German) requirements.
In this case well-established acceptance criteria (e.g., PCT<2200°F) are used and standard
BEPU SYS TH analyses (e.g., see Chapter 15) are performed.
(b) Radiological protection analysis aiming at evaluating the radiological impact of any transient
(RCA in the diagram), ARN (Argentinean Regulatory Body) requirements. In this
case, among others, the maximum dose expected at the assigned territorial boundaries
of the NPP had to be determined. This implies the solution of issues per, each PIE,
like (b1) number of failed fuel rods; (b2) amount of radioactivity in the primary loop;
(b3) amount of radioactivity in the CO; (b4) amount of radioactivity in the reactor building
following assigned CO leakages; (b5) consideration of leakages from reactor building;
(b6) use of meteorological categories including history of measurement on the site;
(b7) passing from radioactivity to doses assuming persons standing at the site boundary;
(b8) consideration of worst impact on the surrounding population also to exclude the need
for evacuation (case of DBA).
(c) Structural mechanical analysis aiming at evaluating the stress and strain status of
safety-relevant components and structures (CBA in the diagram), American Society of

<!-- page 929 (PDF 25) -->
Mechanical Engineering (ASME) requirements. This implied among the other things
calculation of the pressure wave from the break and consequent loads on internals and calculation
of PTS based on realistic accident evolutions.
In relation to each of the above areas acceptance criteria must be identified (item 2 in
the diagram). These are derived from legal requirements in the country (Argentina in
this case).
Phenomena
consideration
Most suited
(BE) code
Nodalization
development
Consideration
of qualification:
- Code
- Nodalization
- User
Scenario
selection
Performing
the analysis
Coupling with the
SYS TH code
Uncertainty and
sensitivity
studies
Criteria
Criteria and acceptability
thresholds
Criteria
U
Quantification?
Acceptability
criteria
Relevant
ph.
Analysis
purposes
Atucha II
safety
margins
CIAU & BF
method
Computational
platform
RCA
CSA
Available codes
Relap5/3D©
ANSYS-CFX-10.0
3D NK - Nestle
XSEC derivation
TransUranus
CBA
RCA
EM/component
stress and results
EM/radiological
consequences
CBA
Assumptions
on BIC
FSAR
Select accept.
criteria
Fig. 14.3 Flow diagram for the BEPU approach pursued for the safety assessment of the
Atucha-2 NPP.

<!-- page 930 (PDF 26) -->
The selection of computational tools, item 3 in the diagram, is based upon the phenomena
which need to be analyzed. This constitutes a key item for the entire process:
complexity of identified phenomena requires suitable level of sophistication which
could not be handled via conservative-simplified codes or approaches. Furthermore,
the need for a variety of computational tools emerged at this level of the process. Actually
, addressing the item 3 brought to the need for a BEPU study: the physical complexity
of the transient following the selected PIE could not be calculated by
conservative methods without having access to the expertise of the original designers
of the NPP. Applications of BE codes and of the latest available technological knowledge
were the only possible alternative to perform assessment independent upon the
original NPP designer.
Items 4, 5, 6, 7, and 8 are the direct consequences of the application of a set of
computational tools. Namely,
l
Selection of the most suited numerical codes was necessary (item 4).
l
Input decks or nodalizations were developed in relation to each code, as needed (item 5).
l
The issues of demonstrating the qualification for the codes, the nodalizations and (not least)
the users or analysts were considered (item 6).
l
Assumptions and acceptability criteria related to the quality and the level of detail for the
values of relevant BIC had to be formulated (item 7). Examples are: (a) the burn-up level
of each fuel assembly; (b) the dimensions of the RPV following thermal dilatation caused
by nominal power operation.
The use of different codes implies the need of coupling (e.g., neutron cross section
generation and three-dimensional neutron kinetics, three-dimensional neutron kinetics
and thermal hydraulics, structural mechanics and thermal–hydraulics, etc.), item 8.
Specific software and related qualification demonstration are needed. Rules are
needed to perform the analyses once computational tools, i.e., codes and nodalizations
including coupling-software, and suitable users are available or ready, item 9. Those
rules refer to unavoidable consideration of conservatism although a BE process is pursued
, including topics like single failure and “worst” failure. Results are expected in
relation to the three areas (a), (b), and (c) defined under item 1.
Uncertainty analysis is performed, item 10, and is part of the results. Compliance
with acceptance criteria shall be demonstrated.
Pursuing the BEPU approach implied a specific consideration of the modalities to
write Chapter 15 of the FSAR (e.g., amount of information provided in each section,
cross-connection among topics, etc.), item 11.
Additional synthesis information related to the diagram in Fig. 14.3 is provided
below. In the first step, as a function of the selected scenario and of the purpose of
the analysis, the complexity of the evaluation model (EM) may range from a simplified
qualitative evaluation (EM/QA) to a complete combination of the three possible
modules (EM/CSA+EM/RCA+EM/CBA). In order to evaluate the plant safety performance
, acceptance criteria are properly selected according to established international
practice.
The two main aspects, which have been considered for developing the EM with the
ability of adequately predict plant response to PIEs, are intrinsic plant features and

<!-- page 931 (PDF 27) -->
event-related phenomena characteristics. “Sets of requirements” connected with the
two aspects are discussed below. The first set of requirements for the EM is imposed
by the design characteristics of the NPP, its systems, and components. Requirements
on the capability of simulating automatic systems are of particular importance for
AOOs, in which control and limitation systems play a key role on the dynamic
response of the plant. It shall be noted that the concerned modeling features are consistent
with the requirements which impose the design of the limitation system
according to the same standard as the reactor protection system. However, this rule
does not apply to control systems. Nevertheless, the best response of the plant cannot
be calculated without the detailed modeling of the control system. This has been considered
in the present framework. The second set of requirements is derived from the
expected evolution of the main plant process variables and the associated physical
phenomena. For the proposed approach, this is performed through the process of identifying
the Phenomenological Windows (Ph.W) and the relevant thermal-hydraulic
aspects (RTA). The relevant timeframe for the event is divided into well-defined intervals
, i.e., the Ph.W, where the behavior of relevant safety parameters, i.e., the RTA, is
representative of the physical phenomena. For the adequate simulation of the identified
phenomena, computational tools were selected from those which have previous
qualification using an appropriate experimental data base. Satisfactory qualification
targets provide basis for acceptability of the postulated application.

## 14.3.6 Selected relevant topics

Different issues, or questionmarks, or “BEPU topics to be addressed” occur when pursuing
the BEPU roadmap (Section 14.3.5). Those are in addition to the terms and the
elements considered in Sections 14.3.1 and 14.3.2, including PIE (discussed in
Section 14.3.3). Again a not exhaustive list of BEPU topics is provided below.
(1) Initial power.
(2) Decay power.
(3) Maximum Linear Heat Generation Rate.
(4) Gap model.
(5) Hydrogen production and clad embrittlement.
(6) Clad burst and FP release, transport and deposition.
(7) Ballooning including coolability after ballooning.
(8) Radiation heat transfer.
(9) Nuclear fuel modeling (pellet crack) including High Burn-up and plutonium-uranium
mixed oxides fuel.
(10) Assumptions on NPP conditions (e.g., single failure).
(11) Mechanical loads.
(12) Long-term cooling including the debris effect.
Some insights into some of the BEPU topics are given with the aim to characterize the
topic rather than providing a suitable answer for applications.
The core power, item (1), is indirectly measured in any NPP and the measurement
is affected by errors. The amount of approximation (or error) can be ·2% or, agreed
