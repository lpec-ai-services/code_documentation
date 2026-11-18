# The perspectives for SYS TH
<!-- source PDF pages 22-40 -->

<!-- page 62 (PDF 22) -->
2.3
The perspectives for SYS TH
This chapter aims at providing an outline of the current perspectives for the development
of nuclear thermal-hydraulics, i.e., the second objective for this chapter of the book.
The historic outline in the previous section as well as the expectable incomplete list
of key actors and stakeholders provides another picture of the “thermal-hydraulics
universe” and of its complexity (Section 2.2.2 and Table 2.1). A broad set of activities
is already ongoing (Section 2.2.3) in the same framework. Thus, the destiny of any
individual or personal position for development may reveal impractical and unusable,
as also discussed in the “Chapter foreword” of this chapter.
However, a list of envisaged ideas for the future is prepared looking from an optimistic
viewpoint and in the attempt to invite the reader to a (further) reflection. The
concerned domains for investigation include modeling features of computational
tools, validation and application of those tools, and planning of experiments. The list
unavoidably reflects the personal experience and shall not be seen as in competition
with any ongoing international projects or with any similar list supported by proper
contexts.
The envisaged needs in SYS TH, or better, elements for reflection may need elaborations
and details beyond what is possible in one chapter of an edited book. Furthermore
, what are called here envisaged needs or, better, elements for reflection shall be
seen as complementary (or in addition) to the needs discussed in Chapter 4 of the book.
No attempt has been made to provide an order-of-importance for the issues concerned
below and priority classification is left to the reader if deemed necessary.1
Sixteen elements for reflection (or categories/targets for improvement) are considered
. Interactions in virtual activities related to the elements are unavoidable although
an attempt is made to select independent research topics. A description of each
“element” is provided and rough proposals are formulated dealing with ideas to
address the concerned open issues.
2.3.1
The “local form loss” coefficients (also reported as
“K-factors” hereafter)
The K-factor is the multiplicative term to the product ρw2 (where “ρ” is the
“reference” density and “w” is the “reference” velocity of the concerned fluid) to
calculate pressure drops at geometric discontinuities.
The origin of the issue lays in the derivation of the balance equations at the hearth
of SYS TH codes: the balance equations are derived making reference to a geometric
space without discontinuities (some advancement is proposed for the integration
1Commonly, this has been done in the past by adopting PIRT or related techniques. Then, the occasion is
taken to state a view point in relation to PIRT. The present author expressed his doubts in relation to the use
of the “ranking” process in SYS TH, since its presentation in 1989. Recently, the sentences by the
key-proponent of the PIRT process, “… the PIRT process as presently implemented produces absolutely
useless documents … ranking is based purely on subjective opinions …” (Zuber, 2010), put those doubts in
the right perspective.

<!-- page 63 (PDF 23) -->
domain by TRACE code, but this is insufficient for practical applications). Therefore,
the missing information about form loss coefficients at geometric discontinuities,
either in the forward fluid motion direction, typically nominal conditions for the
steady-state operation of NPP and ITF, or in the reverse direction (expected during
a transient), must be fixed by the analyst or code-user. In a few situations tabulated
(precalculated) or experimental data exist. In the largest majority of conditions the
user must consider analogies with those data and/or “invent” a value based on his
expertise.
The user has almost no possibility to estimate the effect of the not-fully developed
flow upon the value of the “K-factor.” Additional origins of misunderstandings and
consequently of errors in the values of “K-factors,” derives from inherent difficulties
in gathering qualified experimental data: (a) irreversible pressure drops shall be distinguished
from reversible pressure drops; (b) practical difficulties arise when measuring
the pressure in narrow spaces and in complex geometries; (c) the influence
of local velocities and of void fraction, other than the non-fully developed flow condition
and the transient situation upon the adopted values of the coefficients, can be
large and may require a broad range of experimental conditions. All of this is confirmed
in a recent activity, Benhamadouce (2015), where making reference to spacer
grids and high Re numbers, errors in the comparison between experimental and CFD
calculated data in the range of 15%–30% have been found.
The impact of the issue in NRS can be derived from the following: (1) many of the
discrepancies among results of application of SYS TH codes to target cases (either of
the same code or of different codes) is originated from the process of “fixing” the
“K-factors”; (2) in some cases, based on the comparison between experimental data
and calculated results involving unacceptable discrepancies, code models other than
the formulas for pressure drops are modified to minimize those discrepancies without
accounting for the effect of the arbitrarily fixed “K-factors”: this brings to never ending
efforts for SYS TH code improvement.
The proposals to address the issue are:
l
an effort shall be made to develop traceable procedures for calculating local form loss coefficients
in cases of interest to the nuclear technology and/or supporting those procedures with
a comprehensive data bank. Experiments and experimental conditions all over the world
should be collected and archived. Examples for this could be the libraries for look-up tables
for CHF and the microscopic XS (cross section) for neutrons.
l
CFD computational tools, primarily in single-phase conditions, should be systematically
used to generate proper values of K-factors in the situations of interest for NPP. Related
results shall constitute a traceable support to the application of SYS TH codes. Specific
attention shall be devoted to rounded or sharp edges.

## 2.3.2 The multi-D heat transfer coefficient surface

The convection heat transfer, i.e., one of the mechanisms for the transfer of thermal
power between fluid and wall, is modeled by the well-established empirical relationships
between the heat transfer coefficient (HTC) and the heat flux. This gives rise to
the current need to use around two dozen correlations to cover the range of interest in

<!-- page 64 (PDF 24) -->
NPP design and NRS, noticeably including the consideration of phenomena like CHF,
reflood (also characterized by the acronym RNB and the MFB temperature), and condensation
(also in the presence of noncondensable gases).
At least three fundamental issues of concern shall be identified in relation to the
current status in predicting HTC:
(a) The continuity among HTC values calculated from the various correlations, namely at the
boundaries of the respective validity ranges.
(b) The repartition of heat flux from the wall to the fluid, distinguishing contributions to the gas
and to the liquid phases and even directly (from wall) to the interface liquid-steam.
(c) Heat flux by radiation heat transfer adds to total heat flux and in some experimental situations
(noticeably film boiling in the presence of fluid droplets) separation between convection
and radiation becomes difficult to be quantified.
The proposal here, related to the issue (a), is to construct an as far as possible continuous
multidimensional (multi-D) surface covering all the heat transfer regimes (examples
of HT (heat transfer) regimes are nucleate boiling, saturated boiling, film boiling)
and all the flow regimes (example of flow regimes are bubbly, slug, and annular flow).
Reflood and condensation should be included in this picture. No proposal is formulated
in relation to the issues (b) and (c) which also deserve proper consideration.
It should also be noted that the problem (i.e., of constructing a multi-D HTC
surface) is quite well known in nuclear thermal-hydraulics and also applicable to
other (nonnuclear) technologies (e.g., Divo et al., 2000, see also Tanaka and
Dulikravich, 2000).

## 2.3.3 Energy and entropy balance following RCS blowdown and containment pressurization

Thesystemofinterestisapressurevesselsurroundedbyfull-pressurecontainment.The
vessel is filled by high-pressure high temperature (two-phase fluid), and the containment
is ideally isolated from the environment and filled by air at atmospheric conditions
. The opening of a break in the pressure vessel triggers the “irreversible
phenomenon” called blowdown or pressurized two-phase mixture discharge into the
containment. The containment pressure increases, and energy exchanges with environment
are (ideally) prevented. In this situation the entropy of the isolated system constituted
by the vessel and the containment is expected to increase following the start of
blowdown, i.e., an irreversible thermodynamic process for an isolated system. Results
of code calculations are not consistent with what expected. This constitutes the issue.
In the case of SYS TH codes the difficulty may come in estimation the energy
flowing out of the break (TPCF model results can be qualified against experimental
data, and the same is more complex in relation to the energy flow out of the break).
Additional issues (or subissues) connected with the above include:
(a) Supersonic conditions. Supersonic conditions may occur in discharge pipes (e.g., the line
connecting the PORV with the sump or the ADS 1–3 to the IRWST in the case of AP1000
design). Pressure drops in the discharge lines and mechanical loads upon constraints are
affected by the occurrence of supersonic conditions.

<!-- page 65 (PDF 25) -->
(b) TPCF on-off. This is the situation which occurs when pressure difference between upstream
(reactor pressure vessel side) and downstream (containment side) is not enough to provoke
critical flow at the assigned throat and cycles of TPCF and “Bernoulli-flow” occur.
(c) TPCF location jumps. It is known since different decades that TPCF conditions in a nozzle
may migrate (or jump) from one section to another. The same situation can be more complex
inside a valve. TPCF location jumps may be originated by sharp edge cavitation: steam
generated at any geometric discontinuity upstream an assigned critical section may cause
the shift of the critical section at the upstream geometric discontinuity.
The capability to predict the discussed phenomena is not demonstrated. Recommendation
here is to perform specific experiments and eventually to modify SYS TH
codes. Again, as in the previous case, the problem is well known in nuclear
thermal-hydraulics (e.g., D’Auria et al., 2003; IAEA, 2014; Qiu et al., 2015): the
importance given to the problem constitutes the issue.

## 2.3.4 Precision targets

The word precision is not commonly used in SYS TH area. Common words, other than
“error,” are “accuracy” and “uncertainty,” the former being the known error resulting
from the comparison between measured and calculated data, and the latter being the
unknown error in NPP predictions. The word precision may be used to encompass
both the words and the concepts of accuracy and uncertainty. No values for precision
or precision targets are fixed by any institution (or by stakeholders identified in
Table 2.1). So the common practice is to produce new codes or improved code versions
without knowing the target for acceptability.
The recommendation is to solicit the issuance of precision targets in SYS TH which
also should be moving targets associated with the advancements in the technology
and the understanding. In this case, the reluctance from all actors in nuclear
thermal-hydraulics to fix the precision target constitutes the issue. An attempt to fix
precision target for a narrow range of conditions can be found in D’Auria et al. (2004).

## 2.3.5 The application of CFD-like approaches to NPP design and NRS technologies

CFD has already been mentioned in Chapter 1 of the book (under the heading and in
Section 1.1.1) and, more important, constitutes the topic for Chapter 12 of the book.
CFD applications in NRS are the subject of many publications (e.g., see Bestion, 2014;
Smith et al., 2008). Some notes consistent with those key documents are discussed
hereafter to make self-standing this chapter of the book.
CFD technology impacted the area of NPP technology and NRS since the 1990, as
already mentioned. The CFD code design targeting steady-state conditions, the lack of
traceability of embedded equations (due to commercial reasons), the common
assumption to neglect the pressure influence upon density changes, and the difficulty
to model an entire NPP loop in two-phase conditions may represent obstacles for the
application of CFD in accident analysis or may delay its full exploitation. Otherwise,
the quality assurance and the needs from the DiD (see Fig. 2.1) impose the use of the

<!-- page 66 (PDF 26) -->
best techniques (i.e., the least restrictive assumptions) and the possibility of
“independent” checks.
CFD codes for single-phase flows may be seen as part of a mature technology ready
for applications even for NPP design and NRS situations. The issue for full application
to NPP design and mainly to NRS is the qualification:
(a) Best Practice Guidelines (BPG) are available and may need enforcement and improvement
(b) the convergence of results when the mesh sizes are decreased shall be demonstrated in any
application
(c) the demonstration of independence of results from mesh generation might be required
A further issue is related to the coupling between CFD and SYS TH codes. The coupled
computational tool may generate inconsistent results (e.g., in a closed NC loop partly
modeled by SYS TH and CFD codes): in fact CFD code results are (strongly) affected
by boundary and initial condition values at the boundaries of the CFD domain of
integration which are necessarily approximate (otherwise, CFD modeling of the entire
loop is needed).
A recommendation is to use CFD for the evaluation of local pressure drops
including derivation of direct and reverse K-factors (Section 2.3.1 above): properly
qualified CFD codes and approaches may be exploited to generate a databank for
K-factors suitable for qualified SYS TH code applications.
Finally, CFD codes for two-phase flows are going to be developed. The full exploitation
(the useful application) of the capabilities for those codes in NPP design and
NRS may need decades or even never happen. Thus, two-phase CFD codes may
not be strictly considered (within the present context) as part of the needs in SYS TH.

## 2.3.6 The thermal-hydraulics of passive systems

Passive systems and related thermal-hydraulics are part of the history for NPP design
and NRS (e.g., IAEA, 2005, 2009b): the configuration of the RCS for both BWR and
PWR (for instance) is determined considering the possibility to cool the core via NC,
at least removing decay heat (e.g., D’Auria et al., 1991, 1997). Passive ECC systems
and components like accumulators are installed in most of the NPP. The Chernobyl
event in 1986 triggered new attention toward passive systems: new (i.e., other than
accumulators) passive ECCS are part of NPP design, e.g., AP1000 and passive phenomena
are at the basis of the RCS operation, e.g., ESBWR. Passive systems are also
used in the category of “small” NPP, the so-called SMR (small and medium reactors or
small modular reactors).
A not-comprehensive list of issues connected with the design and the operation of
passive systems (again not in the order of importance) is given below:
(a) Stabilityofflow oftwo-phasemixtureinadozenmeter high,largediameterriserofESBWR.
(b) Triggering of NC flow-rate, in some cases consequence of opening of a valve: high values
of flow-rate may cause too fast cooling and large dynamic loads on the structures.
(c) Stability issue: all NC systems are characterized by “small” driving forces (i.e., small
related to a possible similar system equipped by a centrifugal pump). “Small” perturbations
may challenge the stability. The stability issue is even more complicated for the category of
NC systems where boiling and condensation occur.

<!-- page 67 (PDF 27) -->
(d) The stability issue for “composite” systems: Either different NC systems are connected
among each other by a heat exchanger (series connection, e.g., passive cooling of SG when
PS is working in NC) or they are hydraulically connected (parallel connection, e.g., PRHR
(pressurized residual heat removal), CMT (core makeup tank), and IRWST loops in
AP1000). The issue here is that instability of one loop may propagate to connected loops:
the stability issue must be addressed for the entire system.
(e) The local pressure drop coefficients. The issue here, see also item (1) in the present list, is
the precision needed for the “K-factor” values: owing to the impact on stability (e.g., a
“cliff-edge” type of thermal-hydraulic phenomenon) and to the “small” driving forces
available, a higher precision is needed for the “K-factor” values than needed for system
equipped with energized pumps. Then, qualification results of calculations, without having
access to suitable values for “K-factors,” may reveal questionable.
(f ) The reliability of passive systems constitutes a thermal-hydraulic issue not well established
among designers of passive systems (e.g., Jafari et al., 2003).

## 2.3.7 The scaling issue and the experiments

Notwithstanding the large number of papers and reports related to scaling, the
“scaling” still constitutes a controversy in SYS TH and applications, e.g., see the paper
by D’Auria and Galassi (2010). The scaling issue in licensing is considered by
D’Auria and Galassi (2010), who introduced the scaling pyramid to explain the current
situation (Fig. 2.4) and proposed a roadmap for addressing the issue (Fig. 2.5).
ADDRESSING THE SCALING ISSUE
Operational
Transients
LOFT
UPTF
NPP
TMI-2
CT-n
CT-2
Conduction HT
Similar Tests
HTC rod-to-fluid
Sub channel-mixing
CT-1
Full
Scale
Full
Scale
Established Similitude
Code-Nodalization Qualification and Uncertainty Evaluation
Mihama SGTR
Experimental Simulation
Bases for
Application
Fig. 2.4 The scaling pyramid proposed by D’Auria and Galassi (2010).

<!-- page 68 (PDF 28) -->
Even though there is no common acceptance for the proposed roadmap, the reader can
refer to the last mentioned paper for details. The scaling issue for designing experiments
is considered hereafter.
SETF and ITF shall be distinguished when addressing the scaling issue for
experiments.
OBJECTIVE AND SCOPE
Reference Npp
CSNI List
Use of RTA
Component-Zone-
Phenomena
Selection of:
- ITF/SETF
- Code
- Nodalizations
Qualitative & Quantitative
Accuracy (Use of FFTBM)
Development of NPP
nodalization
Accident Scenarios
I
II
IV
III
V
VI
VII
VIII
IX
X
XI
Macro scale
Micro scale
(HOT) ROD SURFACE TEMPERATURE
ITF & SETF DESIGN
End of process
if conditions
are not fulfilled
SCALE EMBEDDED INTO CODE MODELS
SCALING SIMILARITY OF EXPERIMENTAL DATA
CODE ACCURACY INDEPENDENT OF SCALING
PERFORMING Kv SCALED ANALYSIS
REFERENCE NPP CALCULATED SCENARIO
Finalizing the Scaling Analysis
Exploitation of Experimental Data
Use of Scaling Parameters
Achieving Scaling Parameters
TEST DESIGN
(including Counterpart Test)
POWER-TO-VOLUME, FULL-HEIGHT,
FULL-PRESSURE, TIME-PRESERVING
APPROACH
Fig. 2.5 The scaling road-map proposed by D’Auria and Galassi (2010).

<!-- page 69 (PDF 29) -->
The SETF design as well as the design of SETF experiments may or may not be
connected with scaling: rather, the need to characterize a TH phenomenon, coming
from the process of code validation, shall be at the basis of the SETF design. So,
the connection between scaling and SETF may be weak and not further discussed here.
In the case of ITF a suitable design process shall include, namely, when the planned
experiments are relevant for NRS, the consideration of principles like ALARA or the
framework like DiD. ALARA imposes that the design effort shall be consistent with
the safety relevance: in other terms inadequacy of budget may not justify the construction
of a “very” (too) small facility or of a “short” (reduced height) facility. The framework
of DiD imposes providing proper consideration to (in this case “the simulation
of”) parameters affecting the safety functions and the integrity of safety barriers.
Then, “the simulation of” PCT shall be considered a key target when designing
ITF. This requirement may become more stringent when NC phenomena (or passive
systems, see the item above) are involved in the simulation. The scaling-freedom in
relation to the (design of a possible reduced) height for ITF offered by the so-called
Ishii-scaling may reveal inconsistent with the DiD framework and the ALARA principle
. Thus, basic limitations of the Ishii-scaling (actually reduced height is an interpretation
of the Ishii papers) are:
l
There is no criteria to determine an acceptable “shorter” length: i.e., to simulate 4 m of active
length for the reference core (prototype) height one can choice 3.9 m or even 0.5 m in
the model
l
The rod surface temperature cannot be simulated to the best when shorter length is adopted
because of the unknown relationship (this typically constitutes the objective of any experimental
campaign) between linear power, HTC, and fluid dynamic conditions like local
velocities and void fraction
Scaling is closely connected with experiments. The issue here is the preservation of
Experimental Data Base (EDB). Preservation of EDB implies the characterization of
what must be preserved and the gathering of the data: indications for the process can
be found in the paper by Petruzzi et al. (2012).
Related to scaling issue and namely to the scaling in NRS, a comprehensive report
is in preparation at the time of the writing of this chapter, within the framework of
OECD/NEA/CSNI, called Scaling State of Art Report (S-SOAR) (see OECD/NEA/
CSNI, 2016).

## 2.3.8 The V&V for SYS TH codes

As in the case of CFD (Section 2.3.5 above) the V&V subject has already been mentioned
in Chapter 1 of the book (under the headings and in Section 1.1.1) and, more
important, is the topic of Chapter 13 of the book. Furthermore, a recent IAEA report
deals with a comprehensive vision for V&V (IAEA, 2015). A synthesis picture on the
V&V for a SYS TH code derived from that report can be found in Fig. 2.6. Hereafter
some notes supporting those key documents are discussed to make self-standing this
chapter of the book.
The V&V applies to SYS TH codes and, as such, shall be considered a technological
branch established since the beginning of 1980. The precision targets, item

<!-- page 70 (PDF 30) -->
(4) above, should be considered as a prerequisite for V&V and part of the present
V&V issue. Additional aspects deal with the procedures for V&V and with the comparison
between calculated and experimental data.
An attempt to synthesize current V&V understanding might be too long for the present
chapter. So, the issues, or the element for reflections, are:
(a) Matrices for V&V should be available as a complement to code development (i.e., developmental
assessment matrices) and should be endorsed by the scientific community based
on fulfillment of acceptability conditions (e.g., see OECD/NEA/CSNI, 1993, 1996).
(b) Independent assessment matrices (i.e., matrices at the basis of code application), mostly
dealing with Validation and not with verification, should also be available based on requirements
: the exploitation of those matrices should be the basis and the prerequisite for any
code application to NRS problems.
Nomenclature associated with Fig. 6
NEEDS
Bases for
Application
NPP
OPERATION
I
DBA
MULTI-
PHYSICS
SPECIFIC  PLANT  DESIGN
TH*
NP
CH
FP
GT
B&NVFP
ME
I&C
*definitions
in the text
II
THE VALIDATION PROCESS
PHENOMENA
SUB SYSTEMS
AND
MODULES
Example:
TH
-natural circulation
-pump performance
B&NVFP
-boron dilution
III
RELEVANT
ASPECTS
Example:
TH
-pressurizer
 emptyting
GT
-accumulation
 in upper head
IV
RANGE
OF
PARAMETERS
V
CODE FEATURES & CAPABILITIES
B        = born including mixing and separation
CH      = chemistry restricted to the zirconium-water reaction
FP      = fuel performance
GT      = gas transport (N2, H2 and fission products) including mixing and separation
I&C    = instrumentation and control including the logics
ME     = mechanics, e.g., dealing with the inertial behaviour of rotors
NP      = neutron physics
NVFP = non volatile fission products transport including mixing and separation
TH      = thermal-hydraulics including conduction and radiation heat transfer
Fig. 2.6 A snapshot of the V&V for SYS TH codes (IAEA, 2015).

<!-- page 71 (PDF 31) -->
The recommendation here is to pursue the development and the application of those
matrices and introduce acceptability requirements in connection with either the
coverage-range of phenomena (see also Section 2.3.12 in this chapter), and the evaluation
of comparison results coming from the use of the experiments part of the matrices
(see also Section 2.3.4 in this chapter).

## 2.3.9 Uncertainty analysis

The uncertainty needs come from the V&V process. Evaluation of uncertainty must be
connected with the application of BE SYS TH codes and must be supported by suitable
UM. In other terms, one may state that the application of SYS TH code to the
analysis of experimental data (e.g., obtained in ITF or SETF within the framework
of [code-developers independent] validation activities) shows unavoidable errors, typically
referred as accuracy; thus, errors shall be expected in the prediction of NPP transient
scenario and are referred as uncertainty of code calculations. A recent IAEA
report deals with current status of UM (IAEA (2008a). Uncertainty is the topic of
Chapter 13 and also considered in Chapter 14 of the book. A synthesis picture providing
an idea of UM can be found in Fig. 2.7. Hereafter some notes supporting those key
documents are discussed to make self-standing this chapter of the book.
International projects like UMS, BEMUSE, and PREMIUM are worthwhile
to spread the expertise and shall be pursued. However looking from the exterior,
Fig. 2.7 A snapshot on the motivation and the processes to estimate the uncertainty of SYS TH
code predictions.

<!-- page 72 (PDF 32) -->
e.g., from the side of scientists not part of the working teams, it definitely may appear
that those initiatives bring more questions than answers, or more doubts than solutions.
Bifurcation analysis, or identification of cliff edges, is possible with current UM
(e.g., see D’Auria et al., 2000).
The elements for reflection, or the issues for possible development, are:
(a) The correct interpretation of results from international projects
(b) The set-up and the acceptability procedure and criteria for V&V of UM
(c) The integration of CIAU and GRS UM is desirable
The elements (a) and (b) are applicable to different areas of nuclear thermalhydraulics
and to other disciplines.
International projects like those mentioned above are important to achieve common
understanding and even to open the way for further development in the concerned
areas. However, in the general case because of (lack of ) proper resources,
(presence of ) proprietary information and (need of ) consensus among several
participants from different Countries, written conclusions from the activities
are smooth and may not reflect the current status. Therefore, item (a), expertparticipant
evaluation may be needed to supplement the information from the final
report of the activities.
Any method or set of equations in nuclear thermal-hydraulics should be supported
by a validation framework, item (b). In other words, because of lack of knowledge,
e.g., associated with turbulence modeling or to the evaluation of convection heat transfer
, suitable proofs of validation and related documentation are strictly necessary for
any method including UM.
An idea was launched to combine GRS and CIAU methods (Kovtonyuk et al.,
2008) item (c). The completion of the activity, actually never started, may provide
an additional proof of validation for both the methods.

## 2.3.10 Coupling with SYS TH

Starting from the 1960 the fundamental disciplines for NPP design and NRS followed
separate paths for developments and related expertise was built in “separate
compartments” as already discussed in Chapter 1 of the book. To some extent this
was also true in relation to SYS TH if one consider computational tools in the analysis
sectors of transient RCS performance, core design (primarily aimed at nominal conditions
), subchannel analysis, and CO.
During the decade 1990–2000 the increase in computer power allowed the numerical
coupling among codes in different areas like structural mechanics, neutron physics
, CFD, and nuclear fuel, other than different branches in SYS TH. The SYS TH
codes played a pivot role in this connection.
The coupling among codes implies addressing “numerical and informatics” interfaces
between the codes and the computer-compilers. Those interfaces are not necessarily
homogeneous at the design level for different codes and generate issues
connected with the transfer of information among codes and with the selection of time
step in transient calculations.

<!-- page 73 (PDF 33) -->
The elements for reflection and the recommendations are:
(a) To merge in one SYS TH code the capabilities of modeling RCS, core, subchannel, and CO:
this brings the advantage of avoiding troublesome code coupling in some situations.
(b) To propose systematic V&V procedures for coupling, also involving acceptance criteria for
the coupled results (e.g., see D’Auria et al., 2004, in relation to the coupling between SYS
TH and 3D NK codes).
An example of cross correlation between codes, technological areas in NRS,
and modeling of physical barriers, materials, and NPP components/systems can be
seen in Fig. 2.8 (D’Auria et al., 2012a) (see also CFD coupling in Section 2.3.5 in this
chapter).

## 2.3.11 Modeling and structure for computational tools

The structure and the modeling of existing TH SYS codes (or computational tools) are
based on the application of the “six-partial-derivative-balance-equations” to simulate
the transient performance of the two-phase mixtures. Those equations shall be seen
as the result of the application of the principles of thermodynamics and mechanics.
However, approximations or even inadequacies (so far unavoidable) are part of the
structure and the modeling, like (more details can be found in the paper by
D’Auria et al., 1998):
–
Two-phase flow regimes are not directly accounted.
–
Averaging is needed at the levels of cross-sectional flow area, integration volume, and time;
all of this is associated with the concept of control volume.
–
Consideration of two (or three) fluid fields as solution domain (this may be seen as a consequence
of the two items above).
–
Need for a variety of constitutive and(/or) closure equations which are unavoidably used
outside their range of applicability; this also implies the need of “virtual correlations”
(or numerical terms) to get solutions within the real domain.
The concept of control volume implies the need to reconstruct the continuous reality
(i.e., the NPP configuration) by more or less large pieces, thus introducing undue discontinuities
at the connection faces. The well-known issue of “water-packing” is a
consequence.
The V&V with main reference to the validation shall be seen as the only way to
qualify and, eventually, to make acceptable those inadequacies.
Nevertheless, the SYS TH codes shall be seen as the basket for the expertise gathered
in the areas of modeling and experiments. Validation has been, and actually is,
the key to overcome the modeling approximations. From pursuing the validation
process one shall recognize that errors exist in the results from code application
and shall be capable to quantify those errors: this imposes, among the other things,
the need for estimating the uncertainty (see also item (9)).
The recommendation here is a systematic effort to characterize the listed deficiencies
, also including a detailed evaluation of their impact upon the results. This also
constitutes the target of the international network for code developers, FONESYS,
recently established (e.g., see Ahn et al., 2015).

<!-- page 74 (PDF 34) -->
FP
BARRIERS
FUEL MATRIX
UO2 PELLETS
GAS FUEL GAP
FUEL ASSEMBLY
Zircalloy-4 CLAD
D2O COOLANT
Zircalloy-4 PRESSURE TUBE
D2O MODERATOR
SPHERICAL STEEL
CONTAINMENT
CONCRETE CONTAINMENT
BUILDING
ID OF SOURCE TERM
ESTIMATE ON DISPERSION AND
DOSE
MODERATOR TANK
REACTOR PRESSURE VESSEL
MAIN CIRCULATION LOOPS
CLAD
ENVIRONMENT
CONTAINMENT
PRESSURE
BOUNDARY
Materials & Components
Technological Areas
System Thermal-Hydraulics
CONTAINMENT
CFD
STRUCTURAL
MECHANICS
& FUEL
NEUTRONICS
X-SEC
GENERATION
DEPLETION
FP RELEASE &
TRANSPORT,
DOSE
CALCULATION
TRANS
URANUS
TRANS
URANUS
ANSYS
MECHANICAL
ANSYS-CFX
RELAP 5 -3D ©
HELIOS
ORIGEN
NESTLE
MCNP5
NEWT
RELAP 5
3D ©
RELAP 5 -DYNETZ
ASSUMPTIONS/ PEN AND PAPER BASED ON
USNRC REGULATORY GUIDE 1.183
REACTOR COOLING
SYSTEM
MELCOR
MELCOR
(CHOICE ON CONTAINMENT RELEASE PATH)
(CHOICE ON CONTAINMENT RELEASE PATH)
... coupling
... qualification
MACCS
Fig. 2.8 Coupling between codes: cross correlation with technological areas in NRS and modeling of physical barriers, materials, and NPP
components/systems (D’Auria et al., 2012a).

<!-- page 75 (PDF 35) -->
## 2.3.12 Licensing needs

Licensing can be seen as the legal part of NRS and also as the exit edge for NRS findings
and requirements. A picture for the licensing framework in the area of accident
analysis (or Chapter 15 of the FSAR) can be derived from Fig. 2.9. An example of
hierarchy of documents applicable for licensing analysis can be found in Fig. 2.10.
THE LICENSING CONTEXT
PSA Level 1
Normal
Operating
Conditions
AOOs
>10–2/y
DBAs
10–2–10–5/y
DSA: Conservative
Control Systems
(mainly)
Accident Management
(special features,
emergency planning)
Defence in depth
Probabilistic Safety Criteria
Safety Systems
(only)
Defence in depth
Radiological Limits
BEPU
BDBAs
(10–4–10–5/y) (10–5–10–6/y)
Severe
Accidents
(CD)
Severe
Accidents
(LR)
PSA Levels 2 & 3
DSA: BE
External PIEs
(∼10–4/y)
Internal PIEs
PIEs
Fig. 2.9 A picture of the licensing framework, based on a proposal by J. Misak, later on
modified by M. Dusic and F. D’Auria.
IAEA HIERARCHIC SET OF DOCUMENTS
Principles 5
and 8
Comprehensive &
detailed analysis required
Development
&
Application
of
Level 1 PSA
for NPPs
SSG-3
Development
&
Application
of
Level 2 PSA
for NPPs
SSG-4
New SGs provide guidance on
performing DSA and PSA and their
application
SAFETY
REQUIREMENTS:
Safety
Assessment
for
Facilities
and Activities
GS-R-4
2008/09
SAFETY
FUNDAMENTALS
SAFETY
REQUIREMENTS
SAFETY
GUIDES
Deterministic
Safety
Analysis
for NPPs
SSG-2
Fig. 2.10 An example of hierarchy of documents from IAEA, applicable for licensing analysis.

<!-- page 76 (PDF 36) -->
Accident analysis constitutes an important part of the licensing. DBA, anticipated
operational occurrence (AOO), beyond DBA (BDBA) as well as emergency operating
procedure (EOP), and Accident Management Guidelines (AMG) constitute established
concepts in accident analysis. Moreover, following the start of any accident (e.g., a PIE
(postulated initiating event) part of the DBA envelope) I&C have the potential to bring
the NPP far from the initial condition (e.g., D’Auria et al., 2012a).
The first element for reflection for accident analysis deals with the use of conservatism
. The conservatism in input data, also known as “Option 2” in IAEA documents
(e.g., see IAEA, 2008a, 2010a) does not ensure conservatism in the output (or code
calculation results). Conservatism in the output can only be demonstrated when BEPU
analyses are performed; otherwise adequacy of conservatism on the output can only be
inferred by deep expertise. Thus, the IAEA “Option 2” should be considered as an
“interim” option in the history of application of SYS YH codes to licensing.
ThekeyissueinthecaseofaccidentanalysisandlicensingistheapplicationoftheBEPU
approach also identified as “Option 3” in the IAEA documents (e.g., see IAEA, 2008a,
2010a).Pioneeringeffortshavebeencompletedinthisdirectionasdiscussedunderthehistoric
outline above. However, developments are needed to make traceable and robust the
regulatoryprocess,byaddressingsubissueslike(notacomprehensivenotasystematiclist):
–
use of 3D NK to determine the maximum linear power of individual fuel rods
–
use of 3D NK to perform the transient analysis of events where nonhomogeneous core
behavior is expected
–
consideration of single failure
–
consideration of the availability of systems and components part of the NPP (noticeably
including engineered safety features, ESF)
–
BEPU analysis of transients or situations identified as ATWS, SBO, and PTS (pressurized
thermal shock)
–
establish procedures for determining the worst break position and, at a higher level of detail,
the break opening time which affect the calculation of mechanical load on internal and
external components and structures
–
establish procedures to account for the impact of burn-up upon the transient analysis
–
establish procedure to calculate the quantities affecting the acceptance criteria other than the
PCT and the H2 production, i.e., the demonstration of core remaining intact (mostly
mechanical loads at the transient start in case of LBLOCA) and the long-term core cooling
involving the specific subissues of sump-recirculation, debris-effect, and, where applicable,
containment leakages and long-term condensation.
Further elements for reflections are:
(a) A procedure shall be established connecting the accident analysis with the design and the
applicability domain of system codes: DBA envelope⃗TH phenomena⃗significant
physical quantities (e.g., pressure, heat flux, flow-rate)⃗range of variations for those
quantities and related combinations⃗design domain and V&V domain for SYS TH codes
(e.g., see Fig. 2.6).
(b) I&C simulation shall be part of the analysis of accidents (e.g., see D’Auria et al., 2012b).
The first recommendation also applies in relation to V&V for SYS TH codes
(Section 2.3.8 in this chapter). The second recommendation also applies in relation
to PSA and SYS TH (Section 2.3.13 in this chapter).

<!-- page 77 (PDF 37) -->
## 2.3.13 PSA and SYS TH

PSA process at any of the Levels 1, 2, or 3 requires deterministic calculations to establish
the success of any sequence, decide about the failure modes of systems structures
and components, and estimate the “source term.” Historically, approaches and computational
tools have been adopted for deterministic calculations which are simplified
in relation to the methods and the numerical codes available within the SYS TH
domain (the reason for this being the huge number of requested calculations). Current
controversial issue is constituted by the quality or the qualification level of the deterministic
calculations which are used for PSA (e.g., see IRSN, 2013).
The role of I&C in PSA constitutes an additional concern. I&C systems and components
are designed with the target of being uninfluential or providing benefits after
any PIE. However, the complexity of the entire NPP system and the interaction among
various logics and components following any PIE has the potential to bring the NPP
conditions far from the configuration associated with the originating PIE.
The issues or the elements for reflection are:
(a) The design of complex EOP and SAMG on the one hand and the availability of UM on the
other hand, together with the advent of more powerful computers, impose reconsidering the
use of simplified approaches when estimating the success of any sequence or when calculating
radiological releases. This may imply the need for huge computational resources.
(b) The role of “deterministic” uncertainty shall be included in probabilistic results.
(c) I&C simulation shall be considered for PSA and DSA.

## 2.3.14 Severe accident and SYS TH

Making reference to the predicted evolution of any accident the intact (or nearly
intact) core geometry is normally taken as the boundary between SYS TH and SA
analyses. Furthermore, Severe Accidents are outside the domain of interest for this
book as stated in Chapter 1.
The quality of DBA analyses (or of analyses performed within the DBA envelope)
shall be distinguished from the quality of SA analyses or analyses involving core degradation
. Enormous progresses have been made during the last two decades in the
understanding of SA phenomena; however, the qualification level of results from
SA analyses shall be considered far lower than the qualification level expected or
achieved in the area of SYS TH analyses. A picture of the SA area can be obtained
from documents (USNRC, 1995; OECD/NEA/CSNI, 2007, 2009; IAEA, 2008b).
The design impact from SA analyses shall be avoided or minimized, rather SA analyses
shall be used to ensure thorough bases for nuclear technology understanding and
supporting the decision of NPP staff in the unluckily SA situation. New systems to
mitigate SA conditions may reveal improper and not in the direction of facilitating
the operator actions and, even worse, can be the origin of new accident sequences
(e.g., the undue flooding of reactor cavity during nominal operation).
Recommendations or elements for reflection are:
(a) The analysis until the prediction of important core degradation shall be performed by the
BE SYS TH code. This is specifically true in relation to the calculation of the time of

<!-- page 78 (PDF 38) -->
occurrence of degraded core conditions: in other terms, the use of simplified approaches
might produce misleading results far from what can be reliably obtained by BEPU
approach.
(b) SA codes results properly supported by SYS TH code results can be relevant for planning
operator actions: optimized SAMG and connected procedures can be designed.
(c) Impact on the NPP hardware design from SA code results, even supported by SYS TH codes,
should be avoided owing to the low qualification level, as already mentioned. Furthermore
design changes caused by SA analyses should implychanges inthelicensing approach which
currentlydistinguishesbetweenDBAandBDBA:DBAenvelopeshallbechangedaccording
to the design, and proper quality level should be ensured for SA computational tools.

## 2.3.15 User effect and training

The current user effect in the application of SYS TH codes and coupled codes undermines
the applicability of those codes, the confidence toward the derived calculation
results, and the possible benefits from code applications (e.g., see Aksan et al., 1993;
Ashley et al., 1998; D’Auria, 1998; Petruzzi et al., 2005).
The effect of code-users upon “poor” code calculation results shall be seen similar
to the effect of unexperienced drivers bringing top-quality bus or truck against a wall
or out-of-the-road. In these cases (truck or bus off-road), little or no blame is put to the
truck makers or designers, and discipline and training is invoked for drivers. In the
case of SYS TH code, poor code calculation results are preferably attributed to poor
code capabilities: codes appear unreliable and code development processes become
repetitive and never-ending.
Elements for reflections are discussed later.
More focus should be on the qualification of researchers in SYS TH area, and additional
emphasis should be given to the requested (mainly from the side of regulators)
qualification level of code users. International programs are ongoing in this direction
(e.g., Petruzzi et al., 2005), but they appear still weak and not properly supported by
regulatory authorities. Targets and accomplishments for code users shall be connected
with the number of year of experience and the modalities of performing the analysis
(e.g., see IAEA, 2015). The role of input deck, or the interface between the NPP reality
and the code, should receive proper attention. Specific recommendations are:
–
The input deck or the nodalization developed by group 1 of code-users should be
“independently checked” by group 2 of code users.
–
Proper acceptance criteria shall be used to endorse the quality of any input deck.
–
The results of any safetyor design relevant calculation should be “independently checked” and
approvedby a “supervisor”having atleast 10 yearsdocumentedexpertise inSYS THanalyses.
–
In addition to uncertainty analysis needed in conjunction with any BE code calculation,
properly planned sensitivity analyses are necessary to minimize the risk of neglecting possible
bifurcation or cliff-edge effects.

## 2.3.16 The BEPU approach

Only the definition of BEPU (approach), and key elements part of the approach are
given here in order to complete the list of perspectives for the future in nuclear

<!-- page 79 (PDF 39) -->
thermal-hydraulics. BEPU is discussed in the papers by D’Auria et al. (2012a) and
D’Auria et al. (2012b). Details related to BEPU can be found in Chapter 14 of
the book.
The following statements may help in providing an idea about BEPU:
(a) BEPU is composed by the words best estimate (=the best one can do, within current technology
—i.e., a moving target—in predicting/calculating an assigned, typically complex,
transient scenario) and Uncertainty (=expected, or unavoidable, error associated to the calculation
process).
(b) The process of combined application of a SYS TH code and an UM, to the analysis of accident
in NPP, is called BEPU.
(c) BEPU can be seen as the connection between nuclear thermal-hydraulics and licensing
(needs) (see also Fig. 2.11).
(d) A metaphor has been used to describe BEPU (D’Auria, 2013). The knowledge acquired in
nuclear thermal-hydraulics resembles a city suddenly abandoned by inhabitants: everything
is there at rest, and no information is available to trigger the life in the city.
A wild-experienced traveler arriving there feels lost and unable to use his competence
and the existing and visible knowledge. In the allegory, the wild experienced traveler is
the (expert) thermal-hydraulic specialist, the city and its components and systems is the
nuclear thermal-hydraulic knowledge, and BEPU constitutes the civilization needed to
make alive the city.
(e) BEPU constitutes a process which implies the widest exploitation of data and information in
nuclear thermal-hydraulics: this can be derived from Fig. 2.11 (D’Auria, 2015).
The element for reflection is as follows: the application of BEPU is strongly
recommended; benefits from the application can be listed and partly quantified
(see also D’Auria et al. 2015); however, given those circumstances, neither Regulatory
Authorities nor Nuclear Industry (more reasonable) is pushing for the application
of BEPU.
DATA
BASIC
SETF
ITF
NPP
SYS TH CODE DEVELOPMENT
V & V (SCALING)
UNCERTAINTY
ACCIDENT ANALYSIS/FSAR—CHAPTER 15
LICENSING
BEPU
Other Disciplines + PSA
UNCERTAINTY
ACCIDENT ANALYSIS/FSAR—CHAPTER 15
LICENSING
BEPU
Other Disciplines + PSA
SYS TH CODE DEVELOPMENT
Fig. 2.11 The BEPU
process focusing on
accident analysis and
Chapter 15 of FSAR
(D’Auria, 2015).

<!-- page 80 (PDF 40) -->
## 2.3.17 Summary remarks

A synthesis of the items above is provided in Table 2.2. The following modalities or
areas are proposed to plan possible improvements (third column in Table 2.2):
l
The SYS TH code: this implies that improvements are expected for the codes and includes
the (fundamental) modeling.
l
Modeling: this implies that fundamental processes, or basic research, or experimental data
are needed.
l
Application: this deals with modalities and requirements for the processes and the procedures
which foresee the application of computational tools and data to the NPP design,
safety, or licensing. The word Application is adopted here to signify “exploitation of
achieved knowledge and understanding in the technological practice.”
l
Design:thisimpliesthatimprovementsareexpectedinthedesignofthermal-hydraulicsystems.
l
ITF design: this implies that improvements (or acceptable strategies) are expected in the
design of new ITF.
l
EDB: this should be taken as a synonymous of “EDB preservation” and implies that investments
are expected in the area of preserving and storing experimental data.
It shall be noted how SYS TH code is both a target for improvement and a way to
pursue envisaged improvements.
Table 2.2 Synthesis of (personal) views for perspectives in system
thermal-hydraulics
Topic
no.
Category/target
for improvement
Modality for
improvement
Proposals/notes
Local “form loss”
coefficients—
K-factors
Modeling
Libraries shall be created with similar
complexity as the ones for neutron
microscopic XS
Multi-D HTC
surface
Modeling
Either a new approach for calculating
wall-to-fluid HT, or a suitable
multi-D surface for HTC
RCS
depressurization
and CO
pressurization
SYS TH code
New experiments may be needed
Precision targets
Application
Precision targets shall be established
(also part of V&V)
CFD role for NPP
design and NRS
Application
Specific V&V needed, including
improved BPG
Passive systems
Design and
SYS TH code
Specific experiments needed,
addressing the stability issue
Scaling and
experiments
ITF design
and EDB
Scaling issue in licensing is addressed
in OECD/NEA/CSNI (2016), see also
D’Auria and Galassi (2010). Scaling
for experiments is discussed here.
“Full” height ITF may be needed.
EDB to be properly stored
