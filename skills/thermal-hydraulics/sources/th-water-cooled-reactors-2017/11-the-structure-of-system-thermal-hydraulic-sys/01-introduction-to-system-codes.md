# Introduction to system codes
<!-- source PDF pages 3-4 -->

<!-- page 641 (PDF 3) -->
This chapter is the pivot chapter in the book: it connects the basic information in
thermal hydraulics (e.g., Chapter 3, see also Chapters 1 and 2), the modeling capabilities
(e.g., Chapters 5, 7–10), the needs in nuclear technology (e.g., Chapter 4 of the
book) and, noticeably, the phenomena expected in transient conditions for
water-cooled reactors (e.g., Chapter 6) with the applications (see, e.g., Chapter 15),
and the procedures for the application in nuclear reactor safety (see, e.g.,
Chapter 14). Key elements ensuring proper connection between development
and application are verification, validation, and uncertainty as discussed in
Chapter 13.
The SYS-TH code (or codes) have a birth time which can be localized in the
early 1970s (see Chapter 2) and an expected lifetime which will cover some decades
during the current century, that is, till the time when computational fluid dynamics
(CFD) codes (Chapter 12) will become adequately mature and sufficiently powerful
. Possibly, integration of capabilities for SYS-TH and CFD codes can be
expected.
11.1
Introduction to system codes
The nuclear reactor safety technology is based on deterministic safety analysis (DSA)
and probabilistic safety analysis (PSA). In order to perform DSA, fully qualified computational
tools are needed. Among the computational tools, the SYS-TH codes play
the major role since it is able to model the whole reactor with all interactions between
circuits and between components. To some extent the SYS-TH codes are multiphysics
simulation tools since they include:
l
Thermal-hydraulic (or fluid) modules to model flows and heat transfers in circuits
l
Conduction heat transfer in solid domain
l
Fuel thermomechanics
l
Neutron kinetics diffusion equations
l
Pump and turbine models including simple equations for predicting rotation speed of
the shaft
l
Regulations, control, and protection systems including actuation of safety systems, SCRAM,
opening of valves, or safety injections (SIs)
l
Auxiliary circuits such as residual heat removal (RHR), volumetric and chemical control,
and emergency core cooling system (ECCS) may be modeled or treated as boundary
conditions (BCs)
Many types of incidents or accidents can be modeled (breaks in primary, secondary
, and auxiliary circuits, station black-out, loss of RHR, loss of feedwater
(LOFW), loss of heat sink, stop of pumps, inadvertent closure or opening of valves
, etc.).
Point kinetics (0-D modeling) for the neutron flux in the core is usually embedded
in the codes, including time constancy for the axial power profile in any region
of the core. However, coupling with more detailed 3-D neutron kinetics may be
available.

<!-- page 642 (PDF 4) -->
SYS-TH codes have the capability to cover design basis accident (DBA) and
some beyond DBA (BDBA) scenario up to the condition of loss of core geometric
integrity; at that point severe core damage and wide melting occur that need additional
modeling capabilities usually part of severe accident codes. Coupling of system
codes with severe accident codes or severe accident modules may be available.
The code characteristics that are necessary and that are covered here are the
following:
l
Although many system codes have the capability to model light water reactor (LWR),
heavy-water reactors, gas-cooled reactors, liquid metal reactors, only the steam-water flows
are considered here as encountered in LWRs. However, there may be some noncondensable
gases, boron, radioactive, and chemical products transported in circuits.
l
Modeling capabilities are available for all water-cooled reactors, including primary circuit,
secondary circuit, balance of plant (BoP), and pool in the case of research reactors.
l
The physical domain of simulation of SYS-TH codes should cover the single- and
two-phase flows in the pressure range from 0.001 to 22 MPa, steam and clad temperatures
up to 1200°C, velocity from zero to supersonic velocities. All single- and two-phase flow
regimes may be encountered, and each phase can be saturated, subcooled, or superheated.
Metastable states (subcooled steam and superheated liquid) are encountered in rapid
depressurization.
l
All heat transfer regimes between a heating or cooling wall and a single- or two-phase flow
have to be modeled, including the characteristic points of the “boiling curve,” the critical
heat flux (CHF), and the minimum film boiling (MFB) temperature. Furthermore, a specific
reflood model is often needed.
l
Modeling of two-phase critical flow (TPCF) rate and countercurrent flow limitation (CCFL)
is necessary.
l
Codes should be able to cover steady states and transients. Tools are necessary to obtain a
reference state of a plant or of an integral test known by a few measured data temperatures,
power, pressures, and to guaranty that it is a stationary state.
l
Zero-dimensional or point kinetics model should be part of the code with the capability of
dealing with feedbacks, for example, void fraction, temperature, control rods, etc. The availability
of coupling with a 3-D neutron kinetics model is desirable.
l
Fuel modeling is available, including capabilities to calculate fuel elastic deformation and
creep (ballooning) and failure, as well as the effect of ballooning upon the thermal-hydraulic
performance of the concerned core region. The oxidation with hydrogen production and
transport model should also be available.
l
SYS-TH codes have the capability of modeling logics (so-called I&C) installed in the
nuclear power plant (NPP) independently of their relevance from the safety or licensing
point of view (logics are needed to calculate the “realistic” system performance).
The main known system codes for which information is available are in alphabetic
order: APROS (Ylijoki et al., 2008), ATHLET (Teschendorff et al., 1996), CATH-
ARE (Bestion, 1990a; Antoni et al., 2009), CATHENA (Luxat et al., 1996), KORSAR
(Gudoshnikov and Migrov Yu, 2008), MARS (Jeong et al., 1999), RELAP5
(RELAP5/MOD3, 1995; RELAP5-3-D, 2001), SPACE (Kim et al., 2009), TRAC
(Boyack, 1996), TRACE (TRACE, 2007a,b,c).
Fig. 11.1 illustrates the modeling of a three-loop pressurized water reactor (PWR)
modeling of a system code by the display of code results in a plant simulator based on
the CATHARE code.
