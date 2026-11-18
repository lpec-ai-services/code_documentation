# The requirements and the domain of simulation
<!-- source PDF pages 5-6 -->

<!-- page 643 (PDF 5) -->
11.2
The requirements and the domain of simulation
In order to simulate all DBAs of interest, a SYS-TH code is expected to be a multiscale
, multiphysics computational tool.
Thus, the domain of simulation can be formally defined as “the set of multiphysics
phenomena expected in the NPP in the case of operational and DBA
conditions.”
The lists of the disciplines needed to meet the requirements are:
l
Thermal hydraulics (TH) for all parts where there is fluid which may exchange mass,
momentum, and energy at the boundaries. The fluid is water, steam, or steam-water mixture
with possible addition of:
Fig. 11.1 A three-loop PWR modeled by a system code (from the plant simulator
based on the CATHARE French system code). This corresponds to a situation
encountered during a SBLOCA with a partial core uncovery and with liquid slugs in
intermediate legs.

<!-- page 644 (PDF 6) -->
l
Gases (i.e., N2, H2, air, and fission products), which may be transported by steam or dissolved
in liquid water.
l
Boron and nonvolatile fission products (B & NVFP) transport.
l
Heat conduction within solid structures with exchanges with fluids.
l
Neutron physics (NP).
l
Chemistry, (CH) restricted to the zirconium-water reaction.
l
Fuel performance (FP).
l
Mechanics (ME), for example, dealing with the inertial behavior of rotors or the flapper
movement in check valves.
l
The I&C including the logics used to control the overall system, the subsystems, and the
individual components of an NPP.
Depending on the reactor component and on the situation of interest, phenomena may
be treated with more or less space resolution. Then SYS-TH codes have usually the
following capabilities:
l
0-D models or lumped parameter models which may model components where velocities are
low: pressurizer, upper head (UH), lower plenum (LP), upper plenum (UP), steam generator
(SG) dome, inlet and outlet headers of SGs, etc.
l
1-D models for flow in components which have a privileged flow direction such as pipes,
core assemblies, and annuli.
l
2-D and 3-D models for components with a 3-D velocity field as may be found in the
pressure vessel (PV). An annular downcomer is usually modeled as a 2-D component
and LP, core, UP, and UH are modeled as 3-D components with a relatively coarse
nodalization.
Additional disciplines are involved in the DBA that are not usually treated by system
codes. They are often modeled in other tools that may be coupled to SYS-TH codes:
l
Mechanical loads on structures from pressure wave propagation or from pressurized thermal
shock (PTS) are usually treated by other simulation tools.
l
A 3-D neutron kinetics tools may substitute the “zero-dimensional” modeling capability of
the system code.
l
CFD codes may allow zooming in some regions of the reactor when a fine space resolution is
needed for turbulent mixing (e.g., temperature mixing, boron mixing, etc.).
l
The subchannel modeling of core assemblies was traditionally treated by specific
component codes although some modern system code versions have included this
capability.
l
Containment thermalhydraulics must also be simulated either as a simple 0-D or multi 0-D
model or as a full 3-D model. The former may be treated by SYS-TH codes but the latter
requires usually coupling to a specific CFD model.
SYS-TH codes are designed to be able to simulate with sufficient confidence all reactor
components and all involved phenomena in the DBA domain. Identifying all dominant
phenomena in each component for all reactor design and all considered DBA
transients required a huge work that took decades. Such lists of phenomena and
components were established for code validation matrices in OECD/NEA/CSNI
documents (OECD/NEA/CSNI, 1987, 1993, 1996, 2001). A state-of-the-art report
on Thermo-hydraulics of Emergency Core Cooling in Light Water Reactors was
published by OECD/NEA/CSNI (1989).
