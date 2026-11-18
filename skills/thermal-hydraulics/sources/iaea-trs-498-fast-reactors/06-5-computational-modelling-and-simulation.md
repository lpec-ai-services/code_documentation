# 5. COMPUTATIONAL MODELLING AND SIMULATION
<!-- source PDF pages 36-46 -->

<!-- page 24 (PDF 36) -->
in the case of IGCAR, since the mock-up is very large compared with the size of
the probe, its influence seems to be negligible.
At CEA, PIV allows for the acquisition of large 2-D or 3-D velocity fields.
It is based on the measurement of particle displacement during two short laser
pulses separated by a brief delay. The double frames are recorded using a camera
located perpendicular to the laser sheet. Spatial calibrations, which allow for the
conversion of pixels to millimetres, are carried out prior to measurement using
a target. This technique provides accurate results when the flow is isothermal
but encounters some limitations when a thermal gradient occurs. In this case,
because of the change in the refractive index as a function of temperature, the
images of the particle are blurred.
Ultrasonic velocity profiling is a measurement technique based on
ultrasound Doppler and used to acquire velocity profiles of liquid flows. Each
connected transducer measures a 1-D velocity profile along its own axis, and a
combination of several transducers provides 2-D or 3-D maps of the studied flow.
This non-intrusive measurement is highly resolved in both time and space. It can
be used in opaque fluid, which is an advantage compared with PIV. However, it
seems less accurate than PIV.

### 4. 4. 3. Particles

At IGCAR, in the MINA facility, particles produced from sodium
combustion are analysed using a range of techniques [62]. They are collected
through sampling ports to analyse the aerosol in a spatiotemporal manner on a
filter paper sampler for the mass concentration measurement (off-line), using
a low-pressure impactor (off-line) and an aerosol spectrometer (on-line) to
determine the size distribution.

# 5. COMPUTATIONAL MODELLING AND SIMULATION

## 5.1. INTRODUCTION TO REACTOR MODELLING

Within nuclear thermal hydraulics, simulation techniques are used for
design and safety analyses of reactor concepts. Over the years, various simulation
techniques have been developed for different purposes. Figure 3 introduces these

<!-- page 25 (PDF 37) -->
techniques and classifies them with respect to the required computational efforts
and modelling level.
In general, fluid and heat transport are described by the Navier–Stokes
equations, which can be found in textbooks on fluid mechanics and heat transfer.
These equations, in principle, contain terms for turbulent momentum and heat
transport that require extremely fine spatial and temporal discretization to be
solved directly. Such simulations are called DNS. When the large turbulent
eddies are being solved in the simulation and only the smallest eddies, which are
assumed to behave isotropically, are modelled, the simulations are referred to as
large eddy simulations (LES). However, such simulations still demand a large
amount of computational power. LES and DNS are often referred to as ‘high
resolution (or fidelity) simulation techniques’. High resolution techniques are in
general too costly for industrial purposes. To resolve this issue, one approach
is to average the turbulent eddies. This is the so called RANS approach. DNS,
LES and RANS cover the CFD domain of solving the Navier–Stokes equations.
Recently, hybrid simulation techniques, which combine the strengths of LES and
RANS, have also been developed. Hybrid and RANS techniques are sometimes
referred to as ‘engineering CFD’. Engineering CFD is increasingly finding
applications in nuclear thermal hydraulics for design purposes.
Within nuclear engineering, dedicated simulation tools have been developed
to analyse the fluid and heat transport in nuclear cores. These tools are referred to
as subchannel codes, since they resolve the flow at a subchannel level (i.e. within
the space between three or four fuel pins in a fuel element, depending on the
arrangement of the pins). Such simulations require less computational effort than
FIG. 3.  Pyramid of computational methods used in nuclear thermal hydraulics (courtesy of
F. Roelofs, NRG, Kingdom of the Netherlands).

<!-- page 26 (PDF 38) -->
engineering CFD approaches, but, on the other hand, rely more on empirical
correlations for the transport of fluid and heat between subchannels.
However, even subchannel analysis codes are computationally too
expensive to analyse a complete reactor cooling system, including the primary
circuit as well as the secondary and tertiary cooling systems. More central
processing unit execution time is needed for transient analyses, especially when
reactivity feedback is included in typical nuclear reactor safety analysis. This is
traditionally the solution domain of STH codes or lumped parameter codes, in
which the Navier–Stokes equations are solved by averaging the fluid flow and
heat transfer variables over large computational volumes, subchannels between
the fuel pins. These codes rely largely on empirical correlations for fluid and
heat transport, using friction or pressure drop correlations and heat transport or
Nusselt number correlations. They need relatively less computational power and
provide reasonably accurate results.
Code coupling is being investigated by many researchers as a possible
solution to overcome the modelling limitations of computationally cheaper
numerical codes on the one hand and the computational costs of more detailed
analyses on the other hand. Section 7 of this publication is dedicated to this
approach to numerical simulation in multiscale and multiphysics analyses.
The following subsections will briefly describe the state of the art in
simulation approaches and will finally discuss how thermal hydraulics simulation
tools are being used during the safety review in the licensing process.

## 5.2. SYSTEM THERMAL HYDRAULICS

System thermal hydraulics codes have been used for reactor analysis for
decades. They form the backbone of safety analysis: they are well validated
for water applications and are therefore widely accepted by safety authorities.
However, for application to liquid metal cooled reactors, most codes require both
adaptation and new verification and validation (V&V) efforts.
Lorusso et al. [63] and Roelofs et al. [64] explain the changes that need
to be made to existing codes for the simulation of LMFRs. The following code
capabilities are especially helpful:
— Properties
Fluid and material properties might be hard coded in the code itself; however,
it is preferable to allow flexible input of properties by the user. This will
ensure that the latest values can be implemented easily or, conversely, that
different values can be implemented for sensitivity analysis or in case these
are agreed upon in a benchmark.

<!-- page 27 (PDF 39) -->
— Friction and heat transfer correlations
Correlations can also be either hard coded or provided by flexible user
input.
— 3-D modelling capability
Since fast reactor designs often employ pool designs and/or include large
volumes in which the coolant flow is essentially three dimensional, 3-D
modelling capabilities provide added value.
— Using different fluids in the various cooling systems
Fast reactors typically employ different coolants in the primary system and
the energy conversion system. Therefore, the code having the capability to
model multiple fluids at the same time is helpful.
Nowadays, a variety of STH codes are available and reported in the
literature. These include RELAP5-Mod3.3, RELAP5-3D, SPECTRA, SAM,
TRACE, SAS4A/SASSYS1, MARS, CATHARE, ATHLET, APROS and
ASTEC-Na. Short descriptions of most of these codes can be found in the
benchmark publications by Narcisi et al. [65] and Lorusso et al. [32].
Benchmarks, as described in these papers, play an important role in
increasing the performance and acceptance level of the codes. Nevertheless,
it is important to understand that the level of V&V of fast reactor STH codes
will, for the foreseeable future, require significant effort to approach the level
that has been achieved for water cooled reactors. However, it is necessary to be
cautious when judging the safety level of a fast reactor based on the ‘general’
validation level of the STH codes. From a safety assessment point of view, it is
important that all relevant phenomena are identified and that codes are validated
for each specific analysis on the basis of experimental data and international
benchmark exercises.

## 5.3. SUBCHANNEL CODES

Like STH codes, subchannel codes have been developed and validated
mostly for light water reactor (LWR) applications. For sodium cooled reactors,
development activities were most intense in the 1980s. Recently, there has
been a renewed interest in subchannel code development for fast reactor
applications (e.g. the ANTEO+ code as described by Lodi and Caruso [66]).
Ciurluini  et al. [67] take another route by trying to adapt the STH code RELAP5-
3D to perform at the level of a subchannel code.

<!-- page 28 (PDF 40) -->
Specific aspects that play a role in fast reactor thermal hydraulics and need
attention are the following:
— The mixing between subchannels, especially in the case of new fuel pin
configurations, fuel element designs and coolants for fast reactors.
— The influence of the inter-wrapper flow, which can significantly contribute
to the cooling, especially in decay heat removal scenarios, and which
especially plays a role in fast reactor core designs with closed fuel elements.
This aspect is specifically treated in the TIFONE code, which is under
development in Italy by Nallo et al. [68].
— The influence of (irradiation) deformation of fast reactor fuel pins and fuel
elements.
— The influence and occurrence of blockages at the inlet and internally in fast
reactor fuel assemblies.

## 5.4. ENGINEERING COMPUTATIONAL FLUID DYNAMICS

Engineering CFD aims to solve thermal hydraulics challenges primarily at
the component level. The workhorse in engineering CFD is RANS. However,
unsteady RANS (URANS) and hybrid (LES-URANS) methods are also
being pursued. Since all RANS approaches include turbulence modelling, the
development and use of a suitable turbulence model for momentum and heat
transport is an important backbone of engineering CFD. More information on
turbulence model development is provided in Section 3 on fundamental thermal
hydraulics and is not repeated here.
Sergeenko et al. [69] recently demonstrated that, in liquid metal cooled
reactors, chemistry control also needs attention and can be modelled using
CFD. They present a study of CFD modelling of oxygen transport in a German
experimental lead bismuth cooled facility. This is a relatively new field of
expertise in which pioneering work has been done by Marino et al. [70, 71] for
application to the lead bismuth cooled MYRRHA reactor design. They investigate
the transport of corrosion products in the pool as well as the oxygen mass transfer
in the fuel bundle.
Figure 4 shows a graphical overview of CFD application areas in LMFRs,
ranging from basic turbulent heat transfer model development, through core
thermal hydraulics at the fuel element level and in the inter-wrapper flow, to
pool thermal hydraulics at the component level (e.g. upper pool, lower pool,
heat exchangers, pump, fuel storage, fuel handling machines, etc.) and finally
to complete pool or primary STH. The state of the art of core and pool CFD
applications and their modelling gaps are briefly discussed below.

<!-- page 29 (PDF 41) -->
### 5. 4. 1. Core thermal hydraulics

With respect to core thermal hydraulics and with a particular emphasis
on LMFRs, significant attention has been paid in recent years to enhancing
the validation level and estimating the accuracy achievable in modelling fluid
flow and heat transport within a fast reactor fuel assembly. In those studies,
the focus is on normal operational conditions, without considering changes in
geometry compared with the design drawings. An international group of experts
from Europe and the USA reported the consensus that the expected accuracy of
engineering CFD is on the order of 5–15% with respect to the experimental or
high fidelity numerical reference data for wire wrapped fuel assemblies [72].
However, it is important to understand that the accuracies reported in Ref. [72]
were taken from the original publications, and definitions of accuracy may
vary among different authors. There is a clear need for an agreement on a
common methodology to assess the accuracy of the fuel assembly simulations.
Furthermore, a similar exercise needs to be performed for grid spaced fuel
assemblies. Moreover, it is important to note that even under normal operation
conditions, fuel pins are deformed because of prestress, variations in thermal
expansion coefficients and irradiation effects. The impact of these deformations
on the hot spot factors — and, vice versa, their deformations due to temperature
gradients — is now starting to be studied with CFD and will attract more
attention in the coming years. Similarly, the effect of potential flow blockages
FIG. 4.  Typical engineering CFD application domains in an LMFR (courtesy of F. Roelofs,
NRG, Kingdom of the Netherlands).

<!-- page 30 (PDF 42) -->
and their formation, either at the inlet of the assembly or internally, needs to be
studied in more detail. Detailed CFD modelling is being applied to gain insights,
but validation is needed and is not always easy to achieve. This is because of the
uncertainties and limitations of the experimental investigations as well as of the
numerical studies.
Another aspect that is gaining attention is the influence of the inter-wrapper
flow on the cooling of the core, especially in transient accident situations.
Experiments for the validation of CFD approaches are reported in Pacio
et al. [73]. These experiments were conducted in the inter-wrapper flow gapat the
cross-section of three assemblies, as shown in Fig. 4. Mathur et al. [74] compare
their CFD results with the experiments and show good agreement. Data from
larger domains spanning more fuel assemblies are scarce. The most well known
are the experiments at the PLANDTL facility in Japan [75].
Finally, vibrations in fuel assemblies also need to be analysed. For the
wire wrapped MYRRHA fuel assembly design, Kennedy et al. [76] show that
no excessive vibrations were found experimentally. Since not all fast reactor
designs employ wire wraps, and since grid spaced fuel assemblies might be more
susceptible to vibrations, a new experimental campaign is now being designed
for the Italian lead loop HELENA, as outlined by Roelofs et al. [77].

### 5. 4. 2. Pool thermal hydraulics

Roelofs et al. [78] provide a short review of pool thermal hydraulics CFD
simulations performed up until 2013. They show that initial attempts were made
in the early 1990s to model a 45° or 90° sector of the pool using an isotropic
standard turbulence model and computational grids with a total number of
computational cells in the range of 104 to 105. During the 2010s, the computation
was expanded to full reactor pool simulations using 106 to 107 computational
cells. More recently, pool thermal hydraulic simulations have been reported
that typically use 107 to 108 cells (e.g. the MICAS [79], MYRRHABELLE and
E-SCAPE [80] experimental facilities and the MYRRHA [81, 82], SEALER [83]
and ALFRED reactor designs [84]).
Challenges that remain are related to the user’s decisions on the modelling
approaches for large and complex components, like the core, the pumps and
the heat exchangers. Most analysts use porous medium approaches that require
specific attention with respect to the correct representation of pressure losses,
heat transfer and thermal inertia. Heat exchangers pose an additional challenge,
since their secondary side is typically not explicitly considered, meaning that
correct boundary conditions need to be set. Although this may be relatively
straightforward in a (quasi) steady state situation, it is difficult for transients,
especially when the secondary side flow conditions are changing. The challenges

<!-- page 31 (PDF 43) -->
associated with modelling transients in facilities that include cover gas and
potential changes in plenum levels also need to be taken into account.
Another challenge lies in the validation of the modelling approaches: the
CFD models need to exhibit the ability to deal with the separate effects that may
occur in a reactor pool. However, integral validation is also essential, underlining
the need for well instrumented experimental facilities (both with water as a
simulant and with the real coolant) and for typical reactor data. International
exchange of such data in well organized and documented benchmarks
(e.g. coordinated by the OECD or the IAEA) is of unparalleled value.

## 5.5. HIGH RESOLUTION COMPUTATIONAL FLUID DYNAMICS

High resolution CFD is computationally very expensive and is in practice
mostly applied to small, geometrically simple domains. This is especially true
for DNS. On the other hand, LES simulations are beginning to be used for more
complex geometries and larger domains. However, since this still demands
considerable computational effort, LES simulations often necessitate the use of
supercomputers.
Applications to liquid metals, with their low Prandtl numbers and new
developments in turbulent heat transfer, open new doors in simulation approaches:
when the spatial discretization is sufficiently fine for the momentum transport to
be treated using LES, it allows the energy field, in some cases, to be treated using
DNS. This leads to a sort of hybrid approach.
DNS, and often also LES, is mostly used to create reference data for the
development and validation of engineering CFD approaches, supplementing
experimental data. Experimental data help to provide the final confirmation.
However, it is important to understand that experimental instrumentation has
its limitations, primarily because of the harsh environment involved when
working with liquid metals, as well as the fact that instrumentation cannot be
applied everywhere in the domain. High resolution CFD provides access to
flow quantities wherever the nuclear engineer is interested in values of turbulent
transport terms that would require the simultaneous measurement of turbulent
velocities and temperatures at a single point. Recently, Komen et al. [85]
discussed in more detail what high resolution simulation approaches bring to the
field of nuclear thermal hydraulics.
Within the application area of fast reactors, a lot of attention is being paid
to liquid metal thermal hydraulics. As explained in Section 3 on fundamental
thermal hydraulics, this requires special attention in terms of engineering CFD
approaches. Table 5 provides a non-exhaustive overview of publications on high
resolution CFD simulations that support the development and validation of such

<!-- page 32 (PDF 44) -->
novel but also existing approaches. One conclusion that can be drawn from this
list is that, for natural circulation, data for development and validation are not
widely available and need to be elaborated in the future.
TABLE 5. NON-EXHAUSTIVE LIST OF HIGH RESOLUTION CFD
SIMULATIONS IN THE FIELD OF LMFRs
Reference
Type
Channel flow
Flow separation
Shear layers/jets
Natural convection
Mixed convection
Rod bundles
Kozuka et al. [86]
DNS
X
Kawamura et al. [87]
DNS
X
Tiselj and Cizelj [88]
DNS
X
Duponcheel et al. [24]
LES/DNS
X
Errico and Stalio [89]
DNS
X
X
Niemann and Fröhlich [90]
DNS
X
Buckingham et al. [91]
LES
X
Zhao et al. [92]
qDNS
X
Oder et al. [93]
DNS
X
Duponcheel and
Bartosiewicz [94]
DNS
X
Otić and Class [95]
LES/DNS
X
Angeli [96]
LES
X
Fregni et al. [97]
DNS
X
Merzari et al. [98]
LES
X

<!-- page 33 (PDF 45) -->
TABLE 5. NON-EXHAUSTIVE LIST OF HIGH RESOLUTION CFD
SIMULATIONS IN THE FIELD OF LMFRs (cont.)
Reference
Type
Channel flow
Flow separation
Shear layers/jets
Natural convection
Mixed convection
Rod bundles
Yu et al. [99]
LES
X
Cascioli et al. [100]
LES/DNS
X
Duponcheel and
Bartosiewicz [101]
DNS
X
Angeli et al. [102]
DNS
X
Otić et al. [103]
DNS
X
Martínez et al. [104]
DNS
X
Guo and Prasser [105]
DNS
X
Marocco [106]
DNS/LES
X
Marocco et al. [107]
LES
X
Bhushan et al. [108]
DNS
X
De Santis et al. [109]
DNS
X
Zhao et al. [110]
DNS
X
Obabko et al. [111]
LES
X
Shams et al. [112]
LES
X
Saxena [113]
LES
X
Merzari et al. [114]
LES
X

<!-- page 34 (PDF 46) -->
TABLE 5. NON-EXHAUSTIVE LIST OF HIGH RESOLUTION CFD
SIMULATIONS IN THE FIELD OF LMFRs (cont.)
Reference
Type
Channel flow
Flow separation
Shear layers/jets
Natural convection
Mixed convection
Rod bundles
Goth et al. [115]
LES
X
Shams et al. [116]
qDNS
X
Bovati and Hassan [117]
LES
X
Bovati et al. [118]
LES and RANS
X
Note:
CFD: computational fluid dynamics; LMFRs: liquid metal cooled fast reactors

## 5.6. APPLICATION TO SAFETY REVIEW

Thermal hydraulics phenomena occurring in fast reactors, such as thermal
striping, thermal fatigue, thermal stratification, free surface level fluctuations,
cellular convection and inter-wrapper flow, play an important role in the safety
review of fast reactors. Mohanty et al. [119] bring up some of these challenges
within the framework of a safety review for a sodium fast reactor application.
They explain that the fatigue loading imposed by thermal striping and gas
entrainment, as well as decay heat removal by inter-wrapper flow, is important
for the safety evaluation of reactor components. They show that design specific
thermal hydraulics limits are established for various parameters based on safety
analyses using large scale water experiments, liquid metal experiments, literature
reviews and the various thermal hydraulics simulation tools discussed previously.
Once these limits have been established, a detailed safety review of the analytical
and experimental predictions related to the mentioned issues can be performed.
This comprehensive assessment, guided by standard codes and protocols, will
ultimately lead to final acceptance.
