# Chapter foreword — Introduction
<!-- source PDF pages 2-4 -->

<!-- page 144 (PDF 2) -->
R & D
research and development
SAR
safety analysis report
SET
separate effect test (facility)
VHTR
very high temperature reactor
V&V
verification and validation
Chapter foreword
Following the definitions in nuclear thermal-hydraulics (Chapter 3 of the book), an
attempt is made in the present chapter to establish the needs for the (nuclear
thermal-hydraulics) discipline. The needs come from the design/operation of the
nuclear power plants (NPPs), namely the water cooled nuclear reactors and from
the safety evaluations. Focus is given in the chapter to the needs coming from safety,
namely from the licensing process.
The needs shall translate into features of the computational tools as well as for the
procedures needed to prove their validity including the scaling capabilities. So, ideally
the reader may jump from Chapter 1 of the book (general overview of nuclear
thermal-hydraulics) to Chapter 4 (present chapter), to Chapter 11 (the features of computational
tools are discussed), to Chapter 13 (the validation procedures and methods
are described), and finally to Chapter 15 (selected application results from computational
tools are discussed).
Some information in the chapter is specifically related to gas-cooled reactors: that
information is also applicable to the technology of water cooled reactors.

## 4.1 Introduction

Thermal-hydraulics is the physics of fluid flow, energy (e.g., heat) transfer, as well as
the interactions between fluid flow, energy, and the surrounding structures. In nuclear
systems, material interactions with nuclear radiation are also sometimes an important
consideration. Therefore thermal-hydraulics in nuclear reactors is a very wide-ranging
subject and includes such diverse topics as gravity-dominated stratified flow in pipes
with a free surface—including hydraulic jumps, momentum-driven critical flow
through passages and restrictions, fluid-structure interactions such as fluid jet
impingement on structures, flow boiling and condensation, flow and heat transfer
regimes for flow in various geometries at various orientations, energy generation
and transfer to fluids and structures from nuclear sources, and a multitude of other
phenomena. The study of these topics may range from one-dimensional to
three-dimensional flow fields that interact with structures that may be represented
as point to three-dimensional bodies with heat sources and/or sinks. For many of
the scenarios which must be considered in nuclear reactors important variables and
phenomena change as a function of time.
Thermal-hydraulic analyses are governed not only by their boundary and initial
conditions, but also by limiting values of important figures-of-merit which define

<!-- page 145 (PDF 3) -->
maximum or minimum acceptable limits stemming from design/operational or safety
requirements. Therefore the thermal-hydraulic analysis objectives may often be
separated into two broad categories:
l
Design: limits defined to ensure the plant design is robust and thus can operate economically
with minimal shutdowns and operational costs and
l
Safety: limits defined by law or regulatory rules which are specified to protect public health
or living standards.

### 4.1.1 Design

Thermal-hydraulic design analyses focus on creating nuclear systems and components
which are robust and reliable, have a long and trouble-free lifetime, are efficient and
economical to operate, do not tend to stray into unwanted transient scenarios leading
to shutdowns that challenge equipment design limits, and are easy to inspect and maintain
. A well-designed and operated nuclear system should be able to consistently
achieve capacity factors in excess of 90% and have an operational lifetime which
easily exceeds 30 years.
Because design analyses generally deal with normal operational conditions and the
transition from one normal operational condition to another including power-up and
shutdown, such analyses are generally centered on nonsafety grade equipment performance
and phenomena that are known to affect plant efficiency, reliability, and
long-term operations. Examples are:
1. Efficiency: steam separator and dryer performance for Rankine cycle plants; core power distributions
(axial and radial) that match specifications; and uniform core inlet conditions.
Optimization of such parameters enhances power output by enabling the plant to function
at or near technical specification limits.
2. Reliability and long-term operations: unwanted fluid-structure interactions throughout the
system, but particularly in the core at spacers and the steam generator (case of PWR)
U-tubes—such as fretting; and factors which are known to cause crud formation in the core.
By minimizing phenomena known to be adverse in the long-term plant reliability is
enhanced and long-term operations assured.
Thermal-hydraulic analyses centered on the system design include numerical analysis
tools which include those usually used for safety analyses such as (a) system analysis
codes, fuel behavior codes, and containment performance evaluation tools, but also
some not generally used for safety analyses such as (b) operational core power distribution
analysis tools, computational fluid dynamics (CFD) and heat transfer numerical
models, and many specialized thermal-hydraulic tools tuned for analysis of
specialized operational conditions.

### 4.1.2 Safety

Thermal-hydraulic safety analyses focus on ensuring the nuclear systems and components
always operate with operational margins consistent with the “defense-in-depth”
approach required by the regulatory agencies. In essence, the principle of

<!-- page 146 (PDF 4) -->
defense-in-depth requires four levels of protection of public health and safety to be
present, as follows (Sorensen et al., 1999):
1. NPPs are designed to not fail for the range of normal and abnormal conditions they might
reasonably experience during their operating life, including extreme natural phenomena and
man-made hazards;
2. Redundant and diverse support systems are provided to detect initiating events or incipient
failures and shut the reactor down before fuel damage can occur following events within the
design basis;
3. Redundant and diverse emergency systems, including emergency core cooling and containment
systems, are provided to limit the release of radioactivity to the environment and
thereby mitigate accident consequences if the first two levels of defense fail; and
4. Reactors are sited remotely and emergency plans are prepared and practiced in advance with
local and regional authorities to limit the public consequences of a catastrophic accident
involving a large release of radioactivity.
Thermal-hydraulic analyses are important ingredients in all four of the defense-indepth
protection levels. Adherence to the defense-in-depth principle has resulted in
less than 0.1 safety significant event annually per plant with no discernible radiological
health effects from operations and incidents.
Because thermal-hydraulic safety analysis tools generally are used to assess the
margin between calculated key figures-of-merit and limits for those figures-of-merit
imposed on plant operations by national law, the analysis tools are assessed1 using a
very rigorous protocol which has been closely examined and is monitored by the
licensing authorities. Thermal-hydraulic tools used for safety analyses are usually system
analysis tools, containment analysis tools, core performance tools, and fuel performance
tools all created to study the behavior of the nuclear system under very
adverse transient conditions which may lead to fission product release.

### 4.1.3 The role of thermal-hydraulics

Whether for the purposes of designing a nuclear system or demonstrating the safety of
a nuclear system by meeting the necessary licensing requirements, these objectives are
achieved by:
1. Identifying the nuclear reactor operational and accident envelopes,
2. Isolating the key phenomena in each of the plant scenarios that comprise the operational and
accident envelopes,
3. Developing numerical models that accurately calculate the behavior of the key phenomena
for the scenarios of interest,
4. Assessing the numeric models to demonstrate their adequacy for calculating the scenarios
and thus calculate the nuclear reactor behavior for these scenarios in a manner which can be
trusted by the plant designers and regulatory authorities, and
5. Performing the necessary calculations showing the subject nuclear reactor meets the necessary
design and licensing requirements.
1The term “assessed” includes verification and validation of the numerical models using a top-down and
bottom-up protocol which has been rigorously examined and is approved by the licensing authorities.
