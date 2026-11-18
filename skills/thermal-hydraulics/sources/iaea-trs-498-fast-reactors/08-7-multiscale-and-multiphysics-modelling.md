# 7. MULTISCALE AND MULTIPHYSICS MODELLING
<!-- source PDF pages 52-59 -->

<!-- page 40 (PDF 52) -->
# 7. MULTISCALE AND MULTIPHYSICS MODELLING

## 7.1. ADVANCING REACTOR SIMULATION: MULTISCALE AND

MULTIPHYSICS CHALLENGES
In the safety analysis of nuclear reactors, STH simulation tools offer a
strong basis. Such tools are very useful, since they make it possible to consider
the whole plant, including the interactions among various subsystems and
components, while allowing relatively fast computations. However, when three
dimensional (3-D) flow and heat transfer play a role, the traditional STH tools
lack accuracy. Therefore, there is a need for the development of more advanced
simulation tools, especially for application to large pool type reactors, like many
of the fast reactor designs.
 FIG. 5. Illustration of functional containment in an LMFR (courtesy of J. Liao, WEC, USA).

<!-- page 41 (PDF 53) -->
## 7.2. MULTISCALE THERMAL HYDRAULICS MODELLING

The 3-D flow and heat transfer effects in nuclear reactors can be taken into
account by extending existing STH tools with 3-D modules, as is done in the
SAM [127] and RELAP5-3D [128] codes. Such tools can be beneficial because all
the transition from the system scale to the more detailed scale takes place within
the same tool and can be dealt with by the same user. However, the 3-D modules
in these codes are typically simplified and not as accurate as CFD tools [129]. On
the other hand, CFD codes, although suited to analysing the details of the flow,
demand large computational efforts and may lack some of the models needed
to simulate a complete nuclear reactor system. A simple straight pipe element
that requires one or two elements in STH will demand, even if coarsely meshed,
at least a couple of hundred computational volumes in CFD. A compromise
among the alternatives mentioned above is to couple STH and CFD tools. This
can be done in a monolithic way (e.g. as in Ref. [130]), in which the coupling
takes place within a single numerical tool. Another option is to couple separate
STH and CFD tools through a dedicated coupling routine and/or tool. Such
examples can be found in the pressurized thermal shock analysis presented by
Papukchiev and Yang [131], in the analysis of the main steam line break and
anticipated transient without scram presented by Grunloh and Manera [132], in
the analysis of a loss of flow accident of a liquid metal cooled reactor presented
by Toti et al. [133], and in the liquid metal reactor models [134, 135]. These
selected coupled simulations show a variety of tools and approaches being used,
as explained in the following section.

## 7.3. CODE COUPLING ASPECTS

Zhang [136] presents a classification system for multiscale coupling
approaches. Coupling approaches are classified according to five main strategies:
field mapping, operation mode, domain coupling, coupling architecture and
temporal coupling. These five strategies have subcategories to cover all possible
coupling approaches. Operation mode distinguishes between serial and parallel
solvers. In principle, this is supposed to lead to the same result. Normally,
parallel solvers are to be preferred because of their efficiency. However, the
implementation of such methods may be more complex. Field mapping refers to
the way the data are transferred from one code’s specific spatial discretization to
another. The other three strategies are briefly discussed below.

<!-- page 42 (PDF 54) -->
### 7. 3. 1. Domain coupling: Domain decomposition versus domain overlap

In the domain overlap method, both codes simulate the same spatial
domain. The spatial discretization may be different (see Fig. 6, top). A choice has
to be made regarding which code is leading in solving the coupled parameters
and which code is adopting these. In the case of a coupling between CFD and
STH codes, often the STH simulates a complete system, whereas the CFD only
simulates a specific part. Nevertheless, the coupled parameter values of the CFD
can often be adopted by the STH code to simulate the complete system. Typically,
the domain overlap method is more robust than the domain decomposition
method, in which each code works on its own part of the spatial domain, with
data exchange happening at the boundaries (see Fig. 6, bottom). On the other
hand, the domain decomposition method profits from a straightforward intuitive
topology, though it may need more advanced temporal coupling.

### 7. 3. 2. Coupling architecture: Internal versus external coupling

The coupling architecture will determine both the efficiency and the
complexity of the coupling. The choice may depend on the access rights of a
coupling developer to the source of the two solvers (codes). In an internally
coupled system, one code is compiled as a library that is fully integrated inside
the other code, resulting in a single executable. In an externally coupled system,
the two codes communicate with each other either through input and output
files, through a server (supervisor) or in a serverless way [136]. Although
communication with a server or a serverless method may be more efficient, it
also assumes in depth knowledge of both codes. Alternatively, communication
through input and output files may be chosen.
 FIG. 6.  Domain overlap (top) and domain decomposition (bottom) coupling methods.

<!-- page 43 (PDF 55) -->
### 7. 3. 3. Temporal coupling: Explicit versus implicit coupling

For temporal coupling, explicit or implicit numerical schemes may be
adopted, or variants of these, like semi-implicit schemes. It is explained in
Refs [136, 137] that an explicit coupling is the most straightforward temporal
coupling method. In this coupling method, data transfer is performed at the
beginning or end of a time step. Usually, the solution accuracy is first order
and may experience instability (above some critical time step value) or slow
convergence. Explicit coupling is most often used when a domain overlap
method is applied. For domain decomposition, semi-implicit or fully implicit
schemes are normally applied. A semi-implicit scheme ensures the consistency
of the coupled codes within the time steps. Data transfer can be done many
times before advancement to the next time step. The performance of the coupled
system can be further improved by spreading the data transfer across the set of
equations. This is called implicit coupling. Implicit coupling may be the most
efficient and robust coupling approach. However, it is also the most complex and
challenging to implement.

### 7. 3. 4. Verification and validation

The V&V of multiscale and, especially, multiphysics methods is not
easy. Normally, combinations of separate and integral tests are used to validate
simulation methods. Since the phenomena in a multiscale problem occur at
different levels (scales), some simple SETs may not be sufficient. On the other
hand, existing data may not be useful if the measurements were not detailed
enough for the more detailed level of modelling. However, Gerschenfeld [138]
notes that validating multiphysics effects is an especially challenging endeavour.
In order to reproduce neutronics phenomena, validation cases need to be
performed in a nuclear environment, where other measurements may be
complicated. Ideally, validation needs to consist of small tests performed in an
experimental reactor facility, supplemented by integral tests at the reactor scale.

## 7.4. MULTIPHYSICS MODELLING

Instead of coupling the same type of physics (mostly thermal hydraulics) at
various scales, the safety analysis of a nuclear reactor also requires the coupling
of various types of physics. Most STH codes employ some kind of multiphysics
module(s) (e.g. by integrating a point kinetics model) to deal with reactor
physics. Nevertheless, new tools are under development to increase accuracy.

<!-- page 44 (PDF 56) -->
Most of these tools aim for a monolithic approach, although coupled tools are
also being considered.

## 7.5. CODE PLATFORMS UNDER DEVELOPMENT

With respect to the use of coupled simulations in a licensing process,
Gerschenfeld [138] explained that integrated generic coupling tools will be
preferred over ad hoc, problem specific coupling approaches. This allows for
improvements in quality and the reduction of user effects, which makes them
easier to use in a licensing process. Such integrated generic coupling tools are
now under development worldwide, such as the MATHYS tool [139], the C3PO
platform [140] and the ALICES environment [141] in France, the MOOSE
tool [142] and the ARMI tool [143] in the USA, the ARKADIA platform [144] in
Japan, the preCICE coupling library [145] in Germany, the CERES platform [146]
in Belgium, the SEALION platform [147] in Denmark, and the myMUSCLE
tool [148] in the Kingdom of the Netherlands.
Examples of multiphysics tools include the integrated generic multiscale
tools mentioned above. However, dedicated tools are also under development, like
the multiphysics code [149] in Italy, the finite element tool [150] in the Kingdom
of the Netherlands, the GeN-Foam tool [151] in Switzerland and MUSCLE-Foam
[152, 153] in the Kingdom of the Netherlands. These code platforms typically
include thermal hydraulics solvers, reactor physics (or neutronics) solvers and/or
thermal mechanics solvers.
Table 6 presents an overview of the tools mentioned above that can be used
for multiphysics simulations and/or have an integrated generic coupling capability.
Since the development of advanced (beyond STH) multiscale and
multiphysics tools is relatively new, there are still many challenges that need to
be addressed. Table 7 summarizes the challenges and future directions identified
by various authors in open literature. Although the number of times a certain
direction is mentioned is by no means related to its importance, it is striking to
note that all authors mention validation as a means of using the code platform
for licensing.

<!-- page 45 (PDF 57) -->
TABLE 6. NON-EXHAUSTIVE OVERVIEW OF NUMERICAL TOOLS
AND PLATFORMS FOR MULTIPHYSICS AND CODE COUPLING
Tool
Thermal
hydraulics
Thermal
mechanics
Reactor physics
Integrated
generic coupling
Country
Reference
ALICES
X
X
X
X
France
Koren [141]
ARKADIA
X
X
X
X
Japan
Uchibori et al.
[144]
ARMI
X
X
X
X
USA
Touran et al.
[143]
CERES
X
X
X
X
Belgium
De Laet and
Verdebout [146]
CORPUS/C3PO
X
X
France
Greiner et al.
[140]
GeN-Foam
X
X
X
Switzerland
Fiorina et al.
[151]
MATHYS
X
X
France
Gerschenfeld
[139]
MOOSE
X
X
X
X
USA
Martineau et al.
[142]
MUSCLE-Foam
X
X
X
Netherlands,
Kingdom of the
Roelofs et al.
[153]
myMUSCLE
X
Netherlands,
Kingdom of the
Uitslag-
Doolaard et al.
[148]
POLIMI
Multiphysics
X
X
X
Italy
Cervi et al.
[149]
PreCICE
X
Germany
preCICE [145]

<!-- page 46 (PDF 58) -->
TABLE 6. NON-EXHAUSTIVE OVERVIEW OF NUMERICAL TOOLS
AND PLATFORMS FOR MULTIPHYSICS AND CODE COUPLING
(cont.)
Tool
Thermal
hydraulics
Thermal
mechanics
Reactor physics
Integrated
generic coupling
Country
Reference
SEALION
X
X
Denmark
Groth-Jensen
et al. [147]
TU Delft
Multiphysics
X
X
Netherlands,
Kingdom of the
Tiberga et al.
[150]
TABLE 7. CHALLENGES AND FUTURE DIRECTIONS FOR
MULTISCALE AND MULTIPHYSICS SIMULATION PLATFORMS
IDENTIFIED IN OPEN LITERATURE
Future directions
Reference
Innovations for acceleration and
robustness
Tiberga [154]
Novak et al. [155]
Roelofs et al. [153]
Phase change models (solidification)
Tiberga [154]
Multiphase flow
Fiorina et al. [151]
Cervi et al. [149]
Gerschenfeld [141])
Roelofs et al. [153]
Full fast reactor core simulation
including bypass
Takasugi et al. [156]
Expansion to severe accident
conditions
Uchibori et al. [144]
Improved thermomechanical solvers
Fiorina et al. [151]
Cervi et al. [149]
Uncertainty quantification methods
Roelofs [137]
Novak et al. [155]

<!-- page 47 (PDF 59) -->
TABLE 7. CHALLENGES AND FUTURE DIRECTIONS FOR
MULTISCALE AND MULTIPHYSICS SIMULATION PLATFORMS
IDENTIFIED IN OPEN LITERATURE (cont.)
Future directions
Reference
Fuel performance
Fiorina et al. [151]
Novak et al. [155]
High resolution (fidelity) experiments
and tools to create additional
complementary reference data
Aufiero et al. [157]
Novak et al. [155]
Validation (for licensing)
Fiorina et al. [151]
Cammi et al. [158]
Roelofs [137]
Zhang [136]
Gerschenfeld [141]
Pucciarelli et al. [159]
Novak et al. [155]
Roelofs et al. [153]
Zwijsen et al. [152]
Integrated pre- and postprocessing
tools
Roelofs et al. [153]
One of the most recent publications is by Novak et al. [155]. They
specifically focus on the challenges developers face in various aspects, such
as software design, data transfer, coupling solvers and the V&V of methods
and tools. Although most of this was based on experience in the USA with the
MOOSE platform, the lessons learned and future directions are likely the same
for developers worldwide.
It is evident that all code platforms will need V&V. For multiscale
developments, a combination of separate and integral effect tests is typically
used. Often, the cases show that single scale simulations are either not sufficiently
accurate or not sufficiently efficient. For multiphysics platforms, validation of the
combination of thermal hydraulics and neutronics poses a particular challenge.
There are limited test cases available, and not all data are of sufficient quality
when more detailed methods (e.g. CFD) are considered.
