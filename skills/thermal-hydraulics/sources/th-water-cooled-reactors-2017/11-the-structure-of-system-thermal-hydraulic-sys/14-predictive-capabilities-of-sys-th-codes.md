# Predictive capabilities of SYS-TH codes
<!-- source PDF pages 70-75 -->

<!-- page 708 (PDF 70) -->
l
The code has proved that closure laws have a good upscaling capability by validation of all
important phenomena at local or component scale against several SETs at different scales.
l
The code closure laws validation domain covers the entire prototypical thermal hydraulic
range of interest. This includes the pressure and temperature domain, the flow quality,
and the flow geometry. When the reactor domain is not fully covered, physical arguments
should be given to justify that the code extrapolation to reactor domain of parameters is
reliable. For example, when scale 1 data are not available, validation should at least cover
several scales.
l
Since scaled IETs have necessarily some scale distortions, the code should be able to predict
correctly the distorted and nondistorted phenomena. This may require a validation of the
distorted (in IETs) phenomena in nondistorted SETs.
l
The uncertainty of code prediction should take into account the uncertainty due to IC and
BC, material properties, physical models, numerical errors, and should also estimate the
uncertainty due to nonmodeled phenomena or code distortions due to limitations of the
physical model.
11.14
Predictive capabilities of SYS-TH codes

## 11.14.1 Status of current system codes

The current generation of best-estimate system codes fully met the difficult challenge
of replacing the previous conservative evaluation models to provide more accurate
and reliable safety analyses of most accidental transients of interest for LWRs.
A huge effort was spent to provide sufficient experimental data to develop and
validate the 150-to-200 closure laws of the system of equations. This experimental
program considerably improved the knowledge of the two-phase flow phenomenology
at system, component and local levels. The SETs covered all local and component
physical situations. The various IET facilities were necessary to validate the global
consistency of the models and to identify remaining weaknesses. For example, phenomena
such as phase separation in separating Tee junction, or geometry-dependent
CCFL required additional SET investigations to better simulate IET tests.
Today the industrial versions of first system codes which have been developed
since the late 1970s such as RELAP5, CATHARE, TRAC then TRACE, ATHLET
and a few other more recent codes are fully mature and are able to predict qualitatively
and quantitatively well all dominant processes of all accidental transients of interest.
Best-estimate plus uncertainty methodologies can be used for licensing provided that
the code version is qualified, fully verified, and validated and that uncertainty evaluation
method is applied.
Uncertainties methods demonstrated also a good maturity in the BEMUSE international
benchmark (De Cr⟨ecy et al., 2007). Fig. 11.27 shows the PCT in the LOFT
L2.5 LBLOCA test. Data are compared to CATHARE prediction with the base case
calculation, an upper bound and a lower bound calculation. This was obtained with an
uncertainty propagation method using 100 calculations with all input uncertain parameters
(IC, BC, material properties, and closure laws) being randomly sampled. The

<!-- page 709 (PDF 71) -->
Wilks theorem was used to determine the 95th percentile PCT with 95% level confidence
. Today CPU time is no more an issue for system codes and 1000 calculations
were performed of the first peak giving the pdf of the PCT shown in Fig. 11.28.
This example is characteristic of the common uncertainty band of system codes for
the PCT in LOCAs which is often of the order of □150 or even □200 K. This limited
accuracy is due to significant uncertainty of boundary and initial conditions and of
material properties (such as UO2 conductivity) and also for an important part to the
limitations of the physical modeling.
The main sources of the physical modeling uncertainty are due to four main
reasons:
1. The extreme complexity of two-phase flow with so many flow regimes and heat transfer
regimes, with a very large diversity of interface geometry, with many possible bifurcations
(CHF, quenching, flow regime transitions, etc.). In regard to this measurement techniques
are limited to characterize all these processes and experimental uncertainty may be
rather large.
2. The extreme complexity and diversity of flow geometries in the various components of
LWRs. The physics being highly nonlinear, small geometrical details may have a very
significant effect on macroscopic processes (CHF dependent on spacer grid design details,
CCFL dependent on small-scale details of the geometry).
Fig. 11.27 Peak clad temperature in the LOFT L2.5 LBLOCA test. Data are compared to
CATHARE prediction with the base case calculation, an upper bound and a lower bound
calculation obtained by uncertainty propagation (BEMUSE exercise).

<!-- page 710 (PDF 72) -->
3. The two-fluid six-equation model used in 0-D, 1-D, and 3-D modules has inherent limitations
. Some phenomena cannot be described (effects of flow nonestablishment, history
effects on the flow regime, countercurrent flow of liquid films and droplets, combined
effects of coalescence break up nucleation, and collapse on interfacial area) which are partly
responsible for the final uncertainty of the physical model. Further progress would require
additional equations, such as a multifield modeling and transport equations for interfacial
area or for turbulent scales.
4. The macroscopic description of flows in system codes may not describe all small-scale
geometrical effects in a general way with a high accuracy.
Other limitations are listed below.
l
The accuracy of the various models is not uniform since more attention was paid to the most
sensitive models in accidental transients. Looking at heat transfers from fuel rods to the fluid
in a core, some heat transfer regimes such as liquid forced convection or nucleate boiling
have good heat transfer coefficients and can easily remove and transfer the rod power. Then
no specific effort to accurately model these transfers with all possible effects were made.
l
A rather high degree of empiricism was necessary for some models reflecting a lack of
understanding of all governing physical processes.
<760
>1360
Number
Temperature range (K)
Histogram of the first PCT (1000 computations)
1000 Computations
Normal law
Fig. 11.28 Probability density function of the peak clad temperature in the LOFT L2.5
LBLOCA test obtained by 1000 uncertainty propagation CATHARE calculations (BEMUSE
exercise).

<!-- page 711 (PDF 73) -->
These two reasons make system code application to new transient situations or new
geometry somewhat hazardous. New experimental programs with industrial configuration
are still required for any new reactor design.

## 11.14.2 Capabilities of system codes seen from the validation

An optimistic view of the code capabilities results from the assessment calculations
including both SETs and IETs. SETs have well-specified BCs and many measured
flow parameters provided enough data for a good validation of closure laws. Then,
IETs are necessary to check the general consistency of all models, to verify that all
important phenomena are modeled, to validate the nodalization in conditions close
to reactor application.
SETs are generally well calculated since they were extensively used for the development
or the improvement of the closure relations. SET with well-specified BCs are
the only way to determine the validity and accuracy of each closure relation.
Many IETs are also well calculated. One can consider three main cases:
l
All the important phenomena are well predicted with a good timing and a good accuracy.
l
The most important phenomena are predicted. The timing and the accuracy are not perfect
but it does not prevent from clear conclusions on safety issues.
l
Some important phenomena are not predicted or are predicted with a very bad accuracy.
The first type of calculation is still exceptional but the second type became more and
more frequent and the third type was progressively eliminated.
Calculations of many integral tests with system codes allowed to point out and to
solve some problems:
l
Problems in modeling a component: Problem may come from an inadequate choice of module
to model a component. All codes have several types of modules with specific capabilities.
The user must select a module depending on the transient to calculate. For example, a common
modeling of a pressurizer with the CATHARE code uses a simple two-node volume
module which is sufficient for all LOCA transients where the pressurizer is rapidly empty.
For transients such as a LOFW with PORV opening or a multiple SGTR with pressurizer
regulations, a more sophisticated modeling is available and must be selected. Such errors
were minimized after having developed precise User Guidelines.
l
Physical process not predicted by the code: physical mechanisms can be encountered which
cannot be quantitatively predicted by system codes. For example, when CCFL occurs in a
zone with a complex geometry the corresponding flooding correlation must be established
first from experimental tests having the exact geometry before it is implemented in the code.
A specific CCFL model is implemented in system codes where the equations are forced to
find a prescribed flooding limit correlation given by the user on option for a particular node.
This requires that the possible occurrence of CCFL was suspected in a particular region of a
circuit and that representative experiments were performed to measure the flooding curve.
When CCFL is not suspected or when no data exist, prediction errors are possible. Experimental
data now exist for most important reactor components where CCFL is expected to
occur and User Guidelines may recommend adequate flooding correlations.
l
Transients highly sensitive to a certain physical process: The loop seal clearing in some PWR
CL small-break transients is an example of possibly sensitive process. The formation of a

<!-- page 712 (PDF 74) -->
liquid slug in the IL of a PWR is a common feature of many SBLOCA transients. This occurs
in particular after the rupture of the natural circulation when the reflux condenser mode
starts. The primary circuit steam is divided into two parts separated by two liquid slugs
in loop seals and in the vessel bottom. These two subsystems are practically uncoupled from
the energetic point of view. They follow a thermal equilibrium defined by a saturation temperature
resulting from local energy exchanges. In the hot subsystem—core, HLs, SG
tubes—the temperature level is generally stabilized just above the secondary pressure. In
the cold subsystem the energy balance generally depends on the presence of a CL break
and of SIs, both of them giving a trend to a temperature and pressure decrease. Such a depression
of the cold part moves water from core to downcomer and induces a core uncovery with
a clad temperature excursion. This dangerous situation stops when the liquid level in the
descending part of the IL reaches the horizontal part. The loop seal clearing occurs either
simultaneously or at different times in the different loops. After loop seal clearing the pressure
in hot and CLs are nearly equal again. When the process is slow it is very sensitive to
small asymmetries between the loops. Once it happens in one loop a stable state may be
reached preventing from its occurrence in the other loops. Codes have many difficulties
to predict these nonsymmetrical behavior correctly. It is a typical problem of predictability
with small causes having big effects. Such situations were identified by the extensive application
of system codes to integral tests. It should be accounted for in an UQ methodology.

## 11.14.3 Was the two-fluid model the right choice?

The present generation of system codes is based on the two-fluid model. This choice
was made after having identified unacceptable drawbacks of previous models. In the
domain of simulation of system codes for reactor accidental transients, all kinds of
thermal and mechanical nonequilibrium may exist.
Subcooled liquid with direct contact condensation after ECCS injection have to be
modeled. Superheated vapor has to be modeled mainly when post-CHF heat transfer
occurs in the core. Meta-stable superheated liquid and subcooled vapor exist in flashing
flows with a small relaxation time constant (of the order of 10≡3 s). Only models
with two mass balance equations plus two energy balance equations can model all
these situations.
Mechanical nonequilibrium is also encountered in most situations with possible
weak coupling between phases. Using only one momentum equation with a drift flux
models is sufficient for many situations, particularly when the coupling between phases
is rather strong. Two-momentum equations are necessary in other cases particularly
when inertial forces play a role in the slip ratio. Droplets created in a core during a
reflooding are entrained by steam but do not reach the equilibrium slip velocity before
leaving the core due to high inertia. Better capabilities—than with the drift flux model—
are also found for stratified flows by writing two-momentum equations, which allow to
represent wave propagation phenomena, fluvial and torrential regimes and.
The choice of the two-fluid model promoted a very extensive experimental program
required for validating all closure relations. Due to this effort, the choice of
the two-fluid model was a success.
Multifield models are expected to have better capabilities for annular-dispersed
flows or stratified-dispersed flow. The main reason of not having chosen a

<!-- page 713 (PDF 75) -->
three-field model in the 1970s and 1980s was probably the high CPU cost at that time.
Today a three-field model does not penalize the CPU time too much so that most
recent system codes such as SPACE developed by KAERI in Korea (No et al.,
2013) or COSINE developed by SNPSDC in China (Liu et al., 2013) are based on
three-field models.

## 11.14.4 The evolution of 3-D modeling in system codes

System codes like RELAP and ATHLET codes first developed “cross-flow junctions”
between 1-D modules to represent some multidimensional flow features. 1-D equations
are written in the main direction of the flow and simplified momentum equations
are used in the transverse direction to allow mass exchanges between several parallel
channels. This simplified approach of 3-D flows may be sufficient in some cases particularly
for porous body like a reactor core when only small crossflows exist due to
high resistance to transverse velocity.
Explicit 3-D modules exist as an option in the codes TRACE, RELAP5, CATH-
ARE, and SPACE for the reactor pressure vessel. They represent a straightforward
extension of the 1-D modules for cylindrical or Cartesian coordinates. The main
objective of such 3-D modules is the modeling of large-scale 3-D effects in a pressure
vessel during LBLOCA such as downcomer penetration of ECCS water and
reflooding of the core with transverse power profile effects.
Due to the heavy computational effort needed, the 3-D modules are being used
mainly for fast (short) transients like LBLOCA but with the increasing computer
power CATHARE 3-D Module is now also used for SBLOCA and many other transients
. In most applications, rather coarse nodalization schemes (about 1000 nodes for
a CATHARE Pressure Vessel 3-D nodalization) are applied and consequently the
advantage of a 3-D modeling of the flow processes might be offset to a certain extent.
However, large-scale 3-D effects can be better modeled than with 1-D models.
Using such coarse nodalization is far from being converged in space. Then these
3-D modules must validate together the physical model, the numerical scheme, and
the reference vessel nodalization using scale 1 experiments such as UPTF tests. This
does not prevent from compensating errors but such 3-D modules are a progress
compared to parallel channel representation with cross-junction connections.
The computer power continuous increase now allows much finer nodalizations
with a core nodalization which may be one mesh/assembly and 40 axial meshes, that
is, 6000–10,000 meshes for the core. Forty axial meshes were found to provide a reasonably
good convergence of PCT (a few degrees) during LOCA simulations whereas
ten axial meshes could result in numerical errors of about 30 K. One considers that the
industrial use of a system code allows transient simulations within hours (say <12 h)
of common engineer computers so that many sensitivity tests can be performed or
uncertainty propagation using a Monte-Carlo type method (a 100 runs are usually
performed) can be performed.
Previous validation was limited to some UPTF tests for LBLOCA refill and
PERICLES, SCTF, or CCTF tests for reflooding. They provided sufficient validation
for LBLOCA. If the use of 3-D modeling is extended in such a way to cover
