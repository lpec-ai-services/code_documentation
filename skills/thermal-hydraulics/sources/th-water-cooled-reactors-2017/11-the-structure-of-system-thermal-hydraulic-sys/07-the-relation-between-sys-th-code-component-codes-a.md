# The relation between SYS-TH code, component codes, and subchannel codes
<!-- source PDF pages 29-32 -->

<!-- page 667 (PDF 29) -->
BC. Then during the long-term cooling, there may be some coupling between the reactor
and the containment.
However, in a PWR LBLOCA, the pressures in primary circuit and containment
are rapidly equalized and both systems are coupled. There may be a strong impact
of containment pressure on the core reflooding, the reflooding being more difficult
at lower pressure. Therefore, using the single failure criterion leads to minimize
the availability of containment spray system (one out of two independent trains of
spray may be supposed out of service) to demonstrate that containment pressure
remains below the safety limit and, on the contrary, the single failure criterion leads
to maximize the availability of containment spray system, since it will induce lower
pressure during the core reflooding. In PWR LBLOCAs, at the end of the refill phase,
there may be some reverse gas flow from containment to primary circuit due to a
strong depressurization induced by condensation on cold ECCS water from accumulators
. This gas is then a mixture of air and steam and this is also a coupling between
the reactor and the containment.
In any type of LOCA, the long-term cooling with possible recirculation of the water
pumped from the containment, reactor, and containment are also coupled by the pressure
and possible effects of sump clogging.
Some reactors, particularly generation III reactors have many systems which
induce a stronger coupling between reactor and containment, such as automatic
depressurization systems (ADS) which blow steam in a pool in the containment, or
passive RHR systems using water pools in containment. Therefore, the coupling of
system codes with containment codes became more useful and two strategies are
possible:
l
develop coupling between system and containment codes;
l
extend system code capabilities to make them capable of simulating some containment
phenomena.
The first approach is rather common and does not raise very big difficulties. The second
approach is limited to the use of 0-D or a multi-0-D modeling of the containment.
It is limited to the modeling of phenomena which control containment pressure and it
cannot predict hydrogen explosion. It requires some specific capabilities including the
following:
l
Treatment of steam-air mixtures.
l
Specific treatment of wall condensation in the presence of noncondensable gases.
l
Models for spray cooling.
l
Vaporization at a free surface in the case of a pool which may be heated by an ADS or a HX.
11.7
The relation between SYS-TH code, component
codes, and subchannel codes
System codes, component codes, and subchannel analysis codes have been developed
in parallel since the 1980s in different contexts. They have different features but also

<!-- page 668 (PDF 30) -->
overlapping domains of simulation. These legacy codes are first presented to show
their characteristics and domains of simulation before drawing perspective for future
of the reactor thermal-hydraulic codes.

## 11.7.1 System codes

The system scale is dedicated to the overall description of the circuits of the reactor for
the simulation of all transients required by safety analysis. The primary and secondary
circuits of a reactor are modeled by coupling 0-D, 1-D, and 3-D modules together with
submodules for pumps, valves, breaks, safety systems, HX, and control systems. Pipes
are treated by a 1-D model, pipe connections with Tees, large volumes with 0-D modules
, and the pressure vessel may be modeled with a 3-D module using CFD for porous
medium. The whole reactor is modeled using a few hundred 0-D and 1-D meshes,
whereas a 3-D pressure vessel modeling currently uses about 103 coarse meshes. This
method allows simulations of all accident scenarios, including LBLOCAs and
small-break LOCAs (SBLOCAs), with a reasonable CPU time (less than 12 h of a
single-processor computer).

## 11.7.2 Component codes

The component scale also uses CFD in porous medium. This scale is dedicated to the
design, safety, and operation studies of reactor cores and tubular HX (SGs, condensers
, auxiliary exchangers). Rod or tube bundles are homogenized into the control
volumes using the “porosity” concept. The minimum spatial resolution is fixed by the
subchannel size (of the order of 1 cm), which gives the subchannel analysis. Some
component codes can either do subchannel analysis or model a core with larger
radial meshes corresponding to a few rods or one assembly or several assemblies.
Examples of component codes used for LWR core are COBRA-TF (Thurgood
et al., 1981; Avramova, 2006, 2007), FLICA (Toumi et al., 2000), and SUB-
CHANFLOW (Imke et al., 2010). Example of a component code used for SG is
GENEPI (Obry et al., 1990; Belliard and Grandotto, 2000). All component codes
are 3-D codes in porous medium. The two-phase models in component codes may
be a three-equation model with drift flux (GENEPI), a four-equation with drift flux
allowing
one
phase
being
out
of
thermodynamic
equilibrium
(FLICA),
a
six-equation model or even a three-field model with eight or nine equations to describe
separately the liquid films and the droplets (COBRA-TF). The domain of simulation
of component codes used for the core includes the following applications:
l
Core instabilities in BWR with possible coupling to 3-D neutron kinetics
l
Some ATWS in BWR or PWR
l
SLB transients in PWR with possible coupling to 3-D neutron kinetics
l
Boron dilution transients in PWR with possible coupling to 3-D neutron kinetics
l
Rod ejection reactivity transient with coupling to 3-D neutron kinetics
l
PWR core reflooding

<!-- page 669 (PDF 31) -->
The whole core is usually modeled. A usual modeling is a row of mesh for each assembly
. In many applications, the component code is coupled to a system code and may
also be coupled to a CFD code (SLB, boron dilution) and to a 3-D neutron kinetics.
Fig. 11.10 shows a COBRA-TF core moderator density distribution in a coupled
ATHLET/COBRA-TF calculation simulating the Oskarshamn-2 NPP ATWS event.
The domain of simulation of component codes used for the SGs and the HX
includes the following applications:
l
Heat transfer efficiency of the exchanger depending on the design
l
Mass inventory and recirculation ratio in a SG
l
Fouling in SG and in any HX
l
Tube vibrations
The component codes may include some capabilities to have local mesh refinements
using domain decomposition and local zoom methods (Belliard and Grandotto, 2000).

## 11.7.3 Subchannel analysis codes

Subchannel analysis codes model fuel assemblies with one raw of meshes per subchannel
. Most of the time such capabilities are included in component codes which
can also use coarser meshing. Subchannel analysis is more an application of component
codes rather than a type of code. The domain of application includes the
following:
600.00
779.51
Moderator_density
400.00
200.00
51.12
X
Z
Y
Fig. 11.10 COBRA-TF core moderator density distribution in a coupled ATHLET/COBRA-TF
calculation of the Oskarshamn-2 NPP ATWS event (Jimenez and Sanchez, 2015).
From Jimenez, J., Sanchez, V., 2015. Final report on BWR thermal-hydraulics at system scale
and sub-channel scale. NURESAFE, D33.12.5, EC Project, Brussels, Belgium.

<!-- page 670 (PDF 32) -->
l
Analysis of CHF tests and modeling of flows in rod bundles to predict CHF occurrence. Usually
, such subchannel analysis models the various transfers between subchannels including
mass transfers by crossflows, turbulent diffusion, and dispersion of mass momentum and
energy. After a validation of the various radial transfers on dedicated experiments, they interpret
CHF tests performed in small rod bundle tests (e.g., 5·5 bundles) and establish a correlation
of CHF as function of the local average values of P, G, and X. Then they can be used
to simulate a reactor core and to predict when and where CHF may occur.
l
Subchannel analysis may be used in a part of a core to predict with a high resolution the
highest power assembly(ies) in some transients whereas the rest of the core is simulated with
a coarser meshing (e.g., one row meshes per assembly).

## 11.7.4 Common features and differences between codes

Component codes, subchannel codes, and 3-D modules of system codes use the porous
body approach where local instantaneous equations are multiplied by a fluid characteristic
function then by a phase or field characteristic function before being averaged
over time and over a spatial domain. This is clearly different from CFD in open
medium where equations are written only in the fluid domain possibly with a multiplication
by a phase or field characteristic function before being time averaged (see
Chapter 5).
Component codes, subchannel codes, and 3-D modules of system codes must
model radial transfers by diffusion, dispersion, and due to crossflows (Chandesris
et al., 2013). However, since they have different applications, the role of diffusion
and dispersion may be either important (in CHF investigations) or negligible
compared to crossflows and to wall and interfacial heat transfers (in LOCAs).
Component codes, subchannel codes, and 3-D modules of system codes differ by
the size of the meshes or control volumes. Fig. 11.11 illustrates these differences and
compare also to the CFD in open medium approach.
Differences may exist in the type of model and number of equations.
Differences may exist in the treatment of the momentum balance equations in the
radial direction. They can be written in the same way as in the axial direction, or they
may be simplified by a simple relation between pressure difference and flow rate,
which is sometimes called a cross-flow junction.
Differences may exist in the numerical scheme and in the flexibility of the
meshing: Cartesian grid, cylindrical grid, prismatic grid, and body fitted meshing.

## 11.7.5 Current trends

The CPU cost of system codes is becoming very low due to the continuous progress of
computer efficiency. This allows using the 3-D modules of system codes with a finer
grid. Such modules were compared to component and subchannel codes in PSBT and
BFBT benchmarks (see NUPEC documents available from public literature), to predict
flow in experimental tests relative to PWR and BWR rod bundles. Although this
was an exercise typically devoted to component and subchannel codes, system codes
have shown relatively good performance. They could be used with a meshing at the
subchannel scale and one may imagine that these modules will progressively be used
