# Part 2. Insights into computational fluid dynamics for nuclear power plant applications — CFD applications to nuclear thermal fluids problems — CFD models
<!-- source PDF pages 52-56 -->

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
