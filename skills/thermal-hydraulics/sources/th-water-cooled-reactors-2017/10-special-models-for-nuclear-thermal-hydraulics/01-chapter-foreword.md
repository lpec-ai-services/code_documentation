# Chapter foreword
<!-- source PDF pages 2-2 -->

<!-- page 596 (PDF 2) -->
Chapter foreword
Nuclear thermal hydraulics, as discussed in previous chapters, constitutes among the
other things an ancillary discipline for nuclear reactor safety and design: whatever are
the needs coming from nuclear reactor safety and design a feedback shall be expected
in nuclear thermal hydraulics. In this connection, nuclear thermal hydraulics addresses
the simulation of transient evolutions for two-phase mixtures: this is done through the
balance equations (mass, momentum, and energy), as discussed in Chapter 5, which
are supplemented by constitutive equations (see Chapter 9).
The problem arises owing to the fact that the ensemble of balance and constitutive
equations do not cover all situations of interest in nuclear reactor safety and design.
Therefore, “special models” are needed. Special models are distinguished into two
categories dealing with:
(a) Physical situations, which are not (or cannot be) covered by balance and constitutive equations
such as Counter-Current Flow Limitation (CCFL) and Two-Phase Critical Flow
(TPCF).
(b) Performance of components or regions of the system having geometric complexity, which
is not consistent with the (simple) domain of integration for the balance equations.
Therefore,specialmodelsaredeveloped(anddiscussedinthischapter),whichsupplement
balance and constitutive equations and are part of the system thermal-hydraulic code
described in Chapter 11 and, in some cases, are useful for computational fluid dynamics
(CFD) codes application discussed in Chapter 12.
Thespecialmodelsarevalidatedaspartofthesystemcodeswithproceduresdiscussed
inChapter13and results ofapplication ofthose modelsareembeddedinto the listofphenomena
and Nuclear Power Plant (NPP) transient scenarios are discussed in Chapter 15.
10.1
Introduction
Nuclear reactors are complex systems that generate heat in the fuel. In pressurized
water reactors (PWRs) the heat is convected by the coolant to steam generator where
steam is produced. In boiling water reactor (BWR) the steam is produced in the core.
The steam runs turbine. During abnormal situation, the reactor system depressurizes,
vapor is generated and distributes in the system, and safety injection mixes with
two-phase flows. Two phase flows through various components with different configuration
of the distribution of phases and interfaces.
The nuclear reactor operation and accident scenarios are simulated by thermal
hydraulic codes coupled to neutronics. These codes have two-fluid one-dimensional formulation
, and some have limited three-dimensional capabilities to model the vessel.
However, within the reactor system, under abnormal and accident conditions, there
are processes and components that cannot be modeled by these codes. These processes
and components require empirical or separate analytical models. These special models
have significant impact on the assessment of reactor safety systems.
