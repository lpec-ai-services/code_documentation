# Key features of system codes
<!-- source PDF pages 7-10 -->

<!-- page 645 (PDF 7) -->
11.3
Key features of system codes
SYS-TH codes considered here have three main attributes:
l
SYS-TH codes are best-estimate codes
l
SYS-TH codes are safety codes
l
SYS-TH codes are industrial codes

## 11.3.1 Best-estimate code

A best-estimate (BE) code aims at modeling with sufficient reliability all dominant
processes that take place in the domain of simulation. The modeling intends to be
as close as possible to the physical reality. This is totally different from
“conservative codes” which do not predict the figure of merits (FoM) but an upper
bound or a lower bound of the FoM on the unfavorable side with respect to safety.
For example, BE codes intend to predict the peak clad temperature (PCT) during
LOCAs with the best possible accuracy when conservative codes just predict an upper
limit of PCT.
The first generation of system codes was used for licensing of the first PWR and
BWR (boiling water reactor) in many countries. They are being replaced by second
generation BE codes for licensing.
The four first BE codes of the second generation (TRAC, RELAP5, ATHLET, and
CATHARE) started to be developed in late 1970s and the 1980s and reached full
maturity in the 1990s. The main objective of developing these codes was to replace
evaluation models which used many conservative assumptions by the best-estimate
approach for more realistic predictions of PWR or BWR accidental transients.
This constituted a very big scientific challenge since they have much higher level
requirements than previous codes:
l
All phenomena of all transients had to be first identified and modeled at a sufficient level of
fidelity. This required a very large database and progresses in experimentation and measurement
techniques were necessary.
l
The selected thermal-hydraulic model had to be more sophisticated that previous models to
describe the very complex physics of two-phase flows, but should remain accessible to
experimental validation. A difficult compromise was made which selected the two-fluid
six-equation model as the basic model for two-phase flow. This was due to the need to model
both mechanical and thermal nonequilibrium with possible low mechanical coupling in stratified
flow, with highly superheated steam in post-CHF conditions, with subcooled water at
ECCS injection and superheated flashing water in break flow.
l
0-D and 1-D models were found able to describe most flows but a few large-scale 3-D effects
were identified which required 3-D pressure vessel models and specific 2-D-3-D experimental
programs.
l
Closure laws for mass momentum and energy transfers at the walls and at steam-water interfaces
had to be established in a huge domain of parameters, in a very large variety of complex
component geometry, and for all two-phase flow regimes. This may need 150 to about 200
closure laws, which are often identified as “correlations” or “constitutive laws.” A very
extensive separate effect database was necessary to develop and validate each closure law.

<!-- page 646 (PDF 8) -->
## 11.3.2 Safety code

Codes which are applied to safety demonstration for licensing must have some
necessary attributes:
l
The code should be developed with clearly specified quality assurance (QA) procedures
l
The code must be fully documented
l
The code should be verified
l
The code should be validated and should prove its scalability
l
The code should be complemented by uncertainty quantification (UQ) methods
l
The code should have precise User Guidelines to reduce the user effect
Verification is a process for accessing the software correctness and the numerical
accuracy of the solution to a given physical model defined by a set of equations.
The verification is performed to demonstrate that the code numerical algorithms
conform to the design requirements, that the source code conforms to programming
standards and language standards, and that its logic is consistent with the
design specification. This includes tracking of code errors, evaluation of numerical
errors as function of node size and time step, checking of mass error and
energy errors, control of code portability on different platforms and different
compilers, etc.
Validation is a process for accessing the accuracy of a physical model based on
comparisons between computational simulations and experimental data. The validation
is performed to provide confidence in the ability of a code to predict the values of
the safety parameter or parameters of interest realistically or conservatively. The validation
results may be used to determine the uncertainty of some constitutive laws of
the code. The validation can be conducted by the code developers and/or by the code
users. The former is called developmental assessment and the latter is called independent
assessment.
User Guidelines are provided to code users to give them the necessary recommendations
for building an adequate nodalization and input deck, in order to perform an
appropriate simulation of a thermal-hydraulic problem. User Guidelines of a system
code address mainly:
l
the choice of modules (0-D, 1-D, 3-D) and submodules (pumps, sources, sinks, valves,
breaks, heat exchanger (HX), neutron kinetics models, etc.) to model the components of
a system (test facility or reactor),
l
the space resolution by giving recommendations on the mesh size for hydraulic meshes and
for heat conduction in solids,
l
the time resolution by giving recommendations on the time step and time step control.
User Guidelines are necessary to eliminate or at least to reduce as far as possible
the user effect. The “user effect” is what makes the difference between two
sets of calculation results obtained by two code users (or two groups of code
users)
who
use
the
same
code
to
simulate
the
same
problem
(here
a
thermal-hydraulic system with initial and BCs), and have access to the same
information for setting up the nodalization and for determining the needed input
and BC values.

<!-- page 647 (PDF 9) -->
The code scalability or scale-up capability is the capacity to simulate a reactor transient
with the same fidelity and accuracy as observed in SET and integral effect test
(IET) simulations relative to the same situation.
UQ of a SYS-TH code is necessary when a BE code is used for safety demonstration
in a BEPU methodology. The UQ methodology may use propagation of uncertainty

or
accuracy
extrapolation
methods.
The
propagation
methods
being
extensively used, they require a quantification of the model uncertainties at the level
of each of the closure laws.

## 11.3.3 Industrial code

An industrial code is a code which can be used in standardized industrial processes in a
routine way. The main requirements of an industrial code are:
l
The code should be highly robust and perform all simulations without code failure or with a
very low rate of failures.
l
The code should be developed and maintained following precise QA procedures. Successive
versions should be tested and the impact of error corrections or of new capabilities should be
measured and justified.
l
The CPU time and response time should remain reasonable and allow many calculations
with sensitivity tests to closure laws.
l
When SYS-TH codes are implemented in plant simulators for operator training, real time
calculations of transients which require operator actions should be obtained.

## 11.3.4 Some features of the first BE codes

Such system codes have a wide range of applications from research to safety and
design purposes. Examples of applications are:
l
Safety analysis
l
Quantification of the conservative analyses margin
l
Investigation of plant operating procedures and accident management
l
Definition and verification of emergency operating procedures
l
Investigations for new types of fuel management
l
Preparation and interpretation of experimental programs
l
Licensing when used together with a methodology to evaluate uncertainties of the code
predictions
l
Design of new reactors and systems including passive features for the third and fourth
generations of NPP
System code application has been often extended to the field of severe accidents. For
this purpose they are coupled with other codes, which model core degradation and
fission product release.
Implementation in full scope plant simulator: simplified versions were first used to
obtain real time simulations and later, thanks to the increasing computer performance,
the standard versions were used.
Some features of the first second generation codes are given below.

<!-- page 648 (PDF 10) -->
### 11.3.4.1 The RELAP5 code

RELAP5 is the advanced version of the RELAP (Reactor Excursion and Leak Analysis
Program) code developed at the Idaho National Engineering Laboratory. The
version, RELAP5/Mod3 (see RELAP5/Mod3, 1995), includes some contributions
and improvements from the member countries of the joint International Code Assessment
Programme (ICAP) and its successor, the Code Application and Maintenance
Programme (CAMP).
The description of the thermal hydraulics is based on a two-fluid model for
two-phase flow with a flow-regime-based modeling of interfacial transport processes
for mass, momentum, and energy. In the US-NRC version, only a 1-D model is available
with possible cross-flow junctions to allow some description of multi-D flows in
porous bodies (core, horizontal SG, etc.). A DOE version included a 3-D pressure
vessel model.

### 11.3.4.2 TRAC and TRACE codes

The Transient Reactor Analysis Code (TRAC), developed at the Los Alamos National
Laboratory is an advanced, best-estimate computer program for the numerical simulation
of postulated accident and related transient behavior in PWRs. A first preliminary
version (TRAC-P1) was publicly released in 1977. Since then the code has been
continuously improved (TRAC-PF1, TRAC-PF1/MOD1, and TRAC-PF1/Mod2) in
order to extend the code robustness and range of applicability. A BWR version of
the code was developed as a side branch at the Idaho National Engineering Laboratory
following the same modeling and numerical approach as its PWR counterpart.
TRACE code (TRACE, 2007a,b,c) is written in FORTRAN 90 and combines both
PWR and BWR predictive capabilities. It is supposed to replace RELAP and TRAC
codes for all LWRs at the US-NRC. The first validated version TRACE V5.0 (see
TRACE, 2007a) was released in 2007.
The basic modeling approach for transient two-phase flow is a two-fluid model
with flow regime dependent correlations for the interfacial heat, momentum, and
energy transfer processes. TRAC and TRACE have a 3-D pressure vessel model.

### 11.3.4.3 The CATHARE code

The Code for Analysis of THermal hydraulics during Accident of Reactor and Safety
Evaluation is the French counterpart to the RELAP5 or TRAC code. The code has
been developed by three partners, the French Atomic Energy Commission with the
safety institute CEA & IPSN (now IRSN), the French utility EDF, and the vendor
FRAMATOME (now AREVA-NP) for the BE analysis of postulated accidents
in PWRs.
As in most best-estimate codes, the description of thermal nonequilibrium inhomogeneous
two-phase flow is based on a two-fluid approach using mainly algebraic constitutive
relations for the modeling of interfacial coupling, wall friction, and wall heat
transfer processes (Bestion, 1990a). An interfacial pressure difference term has been
introduced, which results in an unconditionally hyperbolic system of equations.
