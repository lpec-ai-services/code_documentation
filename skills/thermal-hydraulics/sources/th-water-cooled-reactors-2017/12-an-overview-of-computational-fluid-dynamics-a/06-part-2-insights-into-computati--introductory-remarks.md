# Part 2. Insights into computational fluid dynamics for nuclear power plant applications — CFD applications to nuclear thermal fluids problems — Introductory remarks … CFD models
<!-- source PDF pages 49-56 -->

<!-- page 777 (PDF 49) -->
(6) Breadth vs. Depth: depth of analysis should be preferred to wide range investigations
namely in the domain of NRS; (7) Individual vs. Collective: collective efforts are needed
for a qualified application of CFD; (8) Means vs. Ends: means models and grids and related
hypotheses are more important than results; results in relation to which qualification cannot be
demonstrated are useless; (9) Quantity vs. Quality: quality is more important than quantity, see
also item (6) above; (10) Short-term vs. Long-term: long-term effort and dedication to the
effort (of producing qualified results) are more important than any short-term achievement;
(11) Specific vs General; specific and general topics may have the same importance for the
development of CFD technology; (10) Tradition vs. Change: the best estimate approach
requires the application of the best estimate techniques; therefore change shall be preferred
to tradition always, however, maintaining suitable qualification level; (11) Single-phase vs
Two-phase; single-phase qualification should come first; both single- and two-phase applications
are of interest in nuclear thermal hydraulics; (12) Steady (stable) vs. Unsteady (unstable)
turbulence models: both steady and unsteady turbulence models are needed; however
qualification of steady models should come first; (13) New design evaluation vs. Old design
evaluation: quality and control of results comes (only or primarily) for old design evaluations;
so applicability of CFD codes and methods should be demonstrated for old design; (14)
Understanding physics vs. Safety analysis: understanding physics and understanding safety
analysis constitute independent matters; both of them are essential for a suitable CFD application
; (15) NTF problems vs. General CFD problems: inspiration to solve NTF problems
should come from a profound knowledge of general CFD problems.
l
High-Performance Computing (HPC) and new experiments. Whatever discussed above may
become reality only if a suitable computational power is available as well as powerful
numerical techniques fully integrated with the computer hardware characteristics. So,
(i) higher numerical accuracy constitutes a moving target, (ii) numerical experiments are
welcome and need to be continuously updated, (iii) reference data for lower level models
are welcome even though the level should increase, (iv) new finding in physics should be
expected and new basic experiments must be designed and performed (also in view of
the availability of more powerful measurement techniques), (v) Improving lower level
turbulence closure models by a priori and a posteriori tests is recommended.

## 12.9 CFD applications to nuclear thermal fluids problems

### 12.9.1 Introductory remarks

The status in the application of CFD methods and models to NPP technology including
NRS can be derived from the series of workshop named CFD4NRS listed in the
Foreword to this chapter. Key statements are reported below.
l
CFD is to an increasing extent being adopted in nuclear reactor safety analyses as a tool that
enables specific safety-relevant phenomena occurring in the reactor coolant system to be
better described (Hassan and Smith, 2008).
l
The use of computational methods for performing safety analyses of reactor systems has
been established for nearly 40 years. Very reliable codes have been developed for analyzing
the primary system in particular, and results from these analyses are often used in the safety
assessment of nuclear power systems undertaken by the regulatory authorities. Similarly, but
to a lesser extent, programs have also been written for containment and severe accident

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

<!-- page 780 (PDF 52) -->
which could lead to the release of fission products bypassing the containment):
The complexity and expanse of the geometry to be modeled: at least one hot
leg with the pressurizer surge line, the primary side of the steam generator, including
both plena (inlet and outlet), the SG tubes, and possibly the vessel upper

##### plenum. Difficulties in nuclear thermal fluid problems (Boyd, 2016)

When we apply the CFD methods to nuclear thermal fluids problems, we encounter
several difficulties:
(1) Complex geometry: This makes it difficult to generate computational grids and cause the
computational load. In general, the geometry is simplified; however, to ensure the reliability
of the simplified geometry results, additional efforts are required.
(2) Uncertain and complex flow behaviors
(3) Uncertain boundary and initial conditions
(4) Lack of benchmark data (CFD grade, Full-scale data)
(5) Lack of similar research and references

### 12.9.3 CFD models

#### 12.9.3.1 Single-phase model (OECD/NEA/CSNI/R(2014)3, 2014)

#####  Applications of CFD to single-phase thermal fluids problems

The most important methodological factors in the single-phase CFD are constituted by
the turbulence models and the computational grids, as already discussed in
Section 12.6; see also Table 12.2. The list of NRS single-phase problems is as follows:
l
Boron dilution (DBA)
l
Mixing: stratification/hot-leg heterogeneities (operational) (also multiphase)
l
Heterogeneous flow distribution (e.g., in SG inlet plenum causing vibrations, HDR experiments
, etc.) (operational)
Table 12.2 NRS problems requiring CFD w/without coupling to SYS
TH codes
NRS problem
System
classification
Incident
classification
Single- or
multiphase
Erosion, corrosion,
and deposition
Core, primary,
and secondary
circuits
Operational
Single/Multi
Core instability in BWRs
Core
Operational
Multi
Transition boiling in BWR/
determination of MCPR
Core
Operational
Multi
Recriticality in BWRs
Core
BDBA
Multi
Reflooding
Core
DBA
Multi

<!-- page 781 (PDF 53) -->
l
BWR/ABWR low plenum flow (operational) (also multiphase)
l
PTS (Pressurized thermal shock) (DBA) (also multiphase)
l
Induced break (DBA)
l
Thermal fatigue (e.g., T-junction) (operational)
l
Hydrogen distribution (BDBA) (also multiphase)
Table 12.2 Continued
Lower plenum debris
coolability/melt
distribution
Core
BDBA
Multi
Boron dilution
Primary circuit
DBA
Single
Mixing: stratification/
hot-leg heterogeneities
Primary circuit
Operational
Single/Multi
Heterogeneous flow
distribution (e.g., in SG
inlet plenum causing
vibrations, HDR
experiments, etc.)
Primary circuit
Operational
Single
BWR/ABWR lower
plenum flow
Primary circuit
Operational
Single/Multi
Water-hammer
condensation
Primary circuit
Operational
Multi
PTS (pressurized thermal
shock)
Primary circuit
DBA
Single/Multi
Pipe break—in-vessel
mechanical load
Primary circuit
DBA
Multi
Induced break
Primary circuit
DBA
Single
Thermal fatigue (e.g.,
T-junction)
Primary circuit
Operational
Single
Hydrogen distribution
Containment
BDBA
Single/Multi
Chemical reactions/
combustion/detonation
Containment
BDBA
Single/Multi
Aerosol deposition/
atmospheric transport
(source term)
Containment
BDBA
Multi
Direct-contact
condensation
Containment/
Primary circuit
DBA
Multi
Bubble dynamics in
suppression pools
Containment
DBA
Multi
Behavior of gas/liquid
surfaces
Containment/
Primary circuit
Operational
Multi
Special considerations for
advanced (including
gas-cooled) reactors
Containment/
Primary circuit
DBA/BDBA
Single/Multi
Sump strainer clogging
Containment
DBA
Single/Multi
DBA, design basis accident; BDBA, beyond design basis (or severe) accident; MCPR, critical power ratio.

<!-- page 782 (PDF 54) -->
l
Chemical reactions/combustion/detonation (BDBA) (also multiphase)
l
Special considerations for advanced (including gas-cooled) reactors (DBA/BDBA) (also
multiphase)

#### 12.9.3.2 Two-phase model

CFD can be applied to multiphase thermal fluids problems. The classification of
Eulerian fluid dynamic simulation approaches for two-phase flows can be found in
Table 12.3. The following list is based on OECD/NEA report (OECD/NEA/CSNI/
R(2014)3, 2014).
Table 12.3 Classification of Eulerian fluid dynamic simulation
approaches for two-phase flow (Bestion, 2012)
Treatment of
equations
Pseudo-DNS
Filtered approaches
Multiplied by fluid/
solid
No
No
No
No
Characteristic
functions
O
O
O
O
Open/porous
Multiplication by
phase (field)
No
No
Yes
Yes
Characteristic
functions
2-Fluid
2-Fluid
Nb of phases or fields
n-Field
n-Field
Time or ensemble
averaging
No
No
No
No
Space averaging
No
Yes
Yes
Yes
Space integration
Space integration
ITM or interface
ITM
ITM
IR
No
Recognition/
reconstruction (IR)
Deterministic
Deterministic
Filtered and
statistical
Statistical
Statistical/
deterministic/filtered
interfaces
interfaces
interfaces
interfaces
interfaces
Possible terminology
O.D.D.1
O.F.D.1
O.F.FS.2
O.F.S.2
With acronyms
O.F.FS.n
O.F.S.n
Type of approach
Pseudo-DNS
LES with
deterministic
interfaces
Hybrid LES with
filtered and statistical
interfaces
LES
statistical
interfaces

<!-- page 783 (PDF 55) -->
l
DNB, Dry-out, and CHF (M)
l
Subcooled boiling (M)
l
Two-phase pressurized thermal shock (M)
l
Direct contact condensation: steam discharge in a pool (M)
l
Pool heat exchangers: thermal stratification and mixing problems (H)
l
Containment thermal hydraulics (H)
l
Two-phase flow features in BWR cores (M)
Table 12.3 Continued
Treatment of
equations
RANS
Component codes system codes
Multiplied by
fluid/solid
No
Yes
No
No
No
Characteristic
functions
O
P
Open/porous
Multiplication by
phase (field)
Yes
Yes
Yes
Yes
Yes
Characteristic
functions
2-Fluid
2-Fluid
2-Fluid
2-Fluid
2-Fluid
Nb of phases of
fields
n-Field
n-Field
n-Field
n-Field
n-Field
Time or ensemble
averaging
Yes
Yes
Yes
Yes
Yes
Space averaging
No
Yes
Yes
Yes
Yes
Space integration
Volume
averaging
Volume
Integration
Integration
over 2
Integration
over 1
Space integration
dimensions
dimension
ITM or interface
No (IR)
No
No
No
No
Recognition/
reconstruction
(IR)
Statistical/
deterministic/
filtered interfaces
Statistical
(and filtered
interfaces)
Statistical
interfaces
Statistical
interfaces
Statistical
interfaces
Statistical
interfaces
Possible
terminology
O.R.P.S.2
P.R.S.2
S0.R.S.2
S1.R.S.2
S2.R.S.2
With acronyms
O.R.F.S.n
P.R.S.n
S0.R.S.n
S1.R.S.n
S2.R.S.n
Type of approach
RANS
statistical
and filtered
interfaces
3 Dimensional
porous
medium
approach
0 Dimensional
lumped model
1 Dimensional
2 Dimensional
O, open medium approach; P, porous medium approach; 1, one fluid; 2, two fluid; n, multifield; F, filtered interface;
D, deterministic interface; DNS, direct numerical simulation; S, Statistical interface; R, Reynolds averaged,
V, volume averaged or integrated.

<!-- page 784 (PDF 56) -->
l
Atmospheric transport of aerosols outside containment (M)
l
DBA reflooding (M)
l
Pipe flow with cavitation (M)
l
External reactor pressure vessel cooling (M)
l
Behavior of gas-liquid interfaces (M)
l
Pipe break-in vessel mechanical load (M)
l
Specific features in passive reactors (M)
For each NRS problem, we need to check what is the issue, what is the benefit from the
use of multiphase CFD, and how mature the current CFD level is.
There are numerous approaches in multiphase CFD. To select and apply them in a
right way, we need to understand the details of each method: advantages/disadvantages
, differences from other methods, etc.
For multiphase flows, we need to select and determine not only the governing equations
(e.g., time-averaged, spatial averaged NS) but also the interface treatments (e.g.,
deterministic, statistical, or filtered). Here, we need to know compatibility between
the combinations selected, e.g., in relation to:
–
Interfacial transfer (mass, momentum, energy);
–
Turbulence transfer (based on the selected models);
–
Wall transfer (momentum and energy transfer by wall function)
l
RANS turbulence model is not compatible with deterministic interface capturing method
because the motion and change in the interface are determined by eddies, which cannot
be captured by RANS turbulence models.
l
In principle, the RANS turbulence models can be compatible with all flow regimes if
the multiphase flow is statistically steady or quasisteady; however, in practice, the level
of information loss (inaccuracy) can vary with flow structures (Bestion, 2012): good accuracy
for dispersed bubbly flow or dispersed droplet flow; bad accuracy for separated-phase
flows such as stratified flow and annular flow; Furthermore, for flow regimes with large
bubbles (slug and churn flow) regime,
l
RANS turbulence models with statistical approach are very impirical, thus requiring much
more complex assessment process.
l
RANS cannot simulate strong unsteady flows. LES and quasi-DNS are required.
Turbulence modeling in two-phase conditions seems to be presently limited to extrapolations
of the single phase k-epsilon models by adding interfacial production terms.
The limits of such approaches have already been reached, and multiscale approaches
are necessary to take account of the different nature of the turbulence produced in wall
shear layers, and the turbulence produced in bubble wakes. Certainly, more research
effort is required in this area; see also Fig. 12.5 and related discussion above.
In the area of two phase, the closure laws in 3D, sometime three-fluid, to include a
dispersed phase, are needed and are currently being adopted. These equations require
closure laws representing the exchange of mass, momentum, and energy between the
phases. Namely, except for rather particular flow regimes (separated phases, dispersed
second phase), general purpose expressions for such closure laws require extensive
further development.
