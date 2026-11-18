# The numerical solution methods
<!-- source PDF pages 21-27 -->

<!-- page 659 (PDF 21) -->
would be treated by subchannel analysis model, that is, with one raw of meshes for
each subchannel.

## 11.4.16 Importance of the nodalization

A reactor nodalization includes several thousands of figures and errors are very likely
to be introduced in the input deck. Therefore, smart systems were developed in preprocessors
and man-machine interface with graphical user interface (GUI), with many
consistency checks to help users and to minimize the possible errors. However, the
various possible choices in the nodalization process are the origin of the “user effect”
which is visible in blind benchmarks, when several independent users simulate the
same transient with the same code and obtain significantly different results. In order
to minimize this “user effect,” more and more precise User Guidelines were
established by code developers which give recommendations for many of these
choices.
The process of nodalization includes a space averaging of a complex physics which
affects the prediction quality in two ways:
l
The space resolution is rather coarse (a few hundred to a few thousand meshes are usually
modeling reactors) which gives only macroscopic information on the physical parameters.
l
The average equations are no more exact equations but are simplified equations with many
closure laws which introduce many approximations and simplifications resulting in a limited
accuracy of predictions.
From these two points, the former represents a limitation of the amount of information
produced by the code whereas the latter is the main source of difficulties for solving
reactor safety issues and represents the main source of code uncertainty.
11.5
The numerical solution methods
The successive steps to establish the model equations and to solve them are shown in
Fig. 11.8. The space discretization of space and time-averaged equations for all modules
(0-D, 1-D, 2-D, and 3-D) results in a set of ODEs and further time discretization
leads to a set of linear algebraic equations.
The numerical scheme is the set of mathematical algorithms which is used to solve
the set of nonlinear PDEs. It includes the space and time discretization of equations
which is used in finite-volume or finite-difference methods. Then the set of nonlinear
PDEs is finally converted to a set of coupled linear equations. The converged solutions
in one time step are calculated using iteration techniques in most cases.
From the physical reality to the simulated reality, both the physical modeling and
the numerical scheme induce some degradation which should be kept within acceptable
and estimated limits.
The numerical method in the SYS-TH codes uses variants of finite-volume and
finite-difference methods based on the ICE method of Harlow and Amsden (1968,
1971, 1975). Although all codes are rather similar in the space discretization, they

<!-- page 660 (PDF 22) -->
differ by the time discretization which may be from semiimplicit up to fully implicit.
The space discretization uses a staggered mesh and the donor cell principle in
first-order scheme. Velocities are defined at vector nodes Xj and scalar quantities
are defined at scalar nodes Oj (see Fig. 11.9). Mass and energy equations may be written
using a conservative form and can be discretized in order to preserve a very good
mass and energy conservation.
These methods are known for their robustness in a wide range of two-phase flow
configurations. The material Courant condition (or CFL condition) on the time step
SIMULATED REALITY
NUMERICAL
SOLUTION
PHYSICAL MODELING
PHYSICAL
REALITY
Set of linear algebraic equations
Time dependent ODE
3-D
(e.g., PV)
S
V
Space
averaging
Space
discretization
Time
discretization
Time
averaging
Multiplied by
phase/field
characteristic f °
Multiplied by
fluid/solid
characteristic f °
Basic local
instantaneous PDE
Averaged PDE
Continuity eq
Navier-Stokes
Energy conservation
(e.g., downcomer)
(e.g., pipe)
Lumped model
2-D
1-D
0-D
}
}
}
}
}
}
cf
ck
ck
ck
ck
Δr
df
□dt
□dr
□dS
□dV
□dt
□dt
□dt
□□□ dxdydz
Fig. 11.8 The successive steps for establishing and solving thermal-hydraulic equations.
Scalar mesh
Mass and energy
equations
Vector mesh
Momentum
equations
Xj – 1
Oj – 1
Xj
Oj
Xj –1
Oj+1
Vector
node
Scalar
node
Fig. 11.9 Illustration of the space discretization for 1-D models.

<!-- page 661 (PDF 23) -->
has to be respected in semiimplicit schemes to ensure the stability. On the contrary,
implicit methods may use very large steps without any limitation which is very convenient
for stationary initial state of a reactor, or even for very slow transients. The
CATHARE code has selected this fully implicit scheme for 0-D and 1-D modules
since it allows prediction of critical flow at a break with very high velocities in very
small meshes required by the strong pressure gradient. This would lead to extremely
small time steps with a semiimplicit scheme due to CFL limit, which prefer to model
break flow by a 0-D sink modeling. In a 1-D module, the CFL limits prescribe that in a
mesh with a length dX with a fluid velocity V, the time step dt should respect the
condition:
dt < dX=V
The heat conduction in solid structures is usually implicit to avoid time step limitations
. It also uses an implicit coupling to hydraulic equations.
Semiimplicit and implicit methods require an iterative solution of every time step
with calculation of a Jacobian matrix. A linear system of equations is solved at each
iteration. Semiimplicit methods allow the elimination of all variable increments as
function of only pressure increments, which reduces the CPU time.
The semiimplicit schemes were extended to numerical schemes without CFL time step
limitations: nearly implicit method in RELAP (Trapp and Riemke, 1986) and
stability-enhancingtwo-step(SETS)methodinTRACtheTRACEcodes(Mahaffy,1982).
The space and time discretization of balance equations result in a nonlinear system
of equations which is often solved by a Newton-Raphson iterative method following
several steps. For example, in the CATHARE code at each iteration:
l
Increments of variables of heat structures and other submodules are eliminated as function of
increments of fluid variables
l
Increments of internal fluid variables of each element are eliminated as function of
increments of junction fluid variables
l
Increments of all junction variables are calculated
l
All variable increments are regenerated and convergence tests are performed
The numerical scheme of a SYS-TH code should meet many requirements. Examples
of common requirements are given below.
Some requirements for the numerical algorithm are mandatory such as the consistency
, the convergence, and the stability.
l
Consistency: ability of a system of discretized equations to tend toward the system of PDEs
when the discretization steps tend to zero.
l
Convergence: ability of a numerical scheme to converge to the solution when the
discretization steps tend to zero.
l
Stability: ability of a numerical scheme not to generate nonphysical instabilities.
Some other requirements are very important for system codes:
l
Robustness: capability to converge to a solution in all physical situations of the domain of
simulation without code failure. If the system code is used to design NPPs or to assess the
safety of them, this requirement is very important.

<!-- page 662 (PDF 24) -->
l
Mass and energy conservation: It is not only a requirement for being accurate on mass and
energy, but also to be able to predict system pressure correctly since any numerical source or
sink of mass or energy will affect the pressure. The system pressure has a strong impact on
reactor transient scenarios since it controls actuations of SCRAM signal, SIs, safety valve
opening, accumulator discharge, and so on. Mass conservation in thermal hydraulics, and
energy conservation in both thermal hydraulics and solid heat structures are then very
important.
Some requirements are also important for system codes:
l
Numerical efficiency criterion: The CPU time must remain compatible with the intended use
of the code.
l
Accuracy:
−
Accuracy on mass and energy conservation is mandatory (see above).
−
Accuracy of transport processes has to be sufficient with respect to some acceptance
criteria, or at least requirements on space and time increments (dx and dt) may be defined
to obtain a given accuracy. This may be important for transport of a temperature front
(e.g., positive reactivity feedback due to flowing cold water into the reactor core by overcooling
in the SG in the case of a steam line break, SLB) or for the transport of a boron
concentration (e.g., positive reactivity feedback due to flowing unborated water into the
reactor core in the case of SBLOCA).
−
Accuracy of propagation processes has to be sufficient with respect to some acceptance
criteria, or at least requirements on space and time increments (dx and dt) may be defined
to obtain a given accuracy. This may be important for pressure wave propagation in
water hammer situation or in condensation-induced water hammer (CIWH) where strong
pressure peaks may propagate in the fluid. This may also be important for void fraction
wave propagation in particular in the case of stratified flow where free surface waves
may propagate either downstream or upstream depending on the conditions. In subcritical
conditions, the prediction of void fraction requires the capability to predict the
upstream propagation velocity correctly.
−
Accuracy and numerical efficiency are tightly coupled since any numerical scheme may
improve its accuracy by reducing space and time increments (dt and dx), which also
increases the resolution time.
l
The numerical algorithm has to be able to deal with water level, swollen levels, and water
packing. When a liquid level or swell level passes a mesh there should not be numerically
induced pressure peaks that affect the transient behavior.
At last, there are several requirements related to operability (i.e., the capability to deal
with different flow conditions) of the numerical algorithm to treat the physical
situations of interest:
l
The numerical algorithm has to be able to deal with incompressible and compressible flows
with nonsimplified equations of state.
l
The numerical algorithm has to be able to deal with flows with strong interfacial mass transfers
(strong pressure-void fraction coupling).
l
The numerical algorithm has to be able to deal with strong hydraulic-wall conduction
couplings (passing DNB, rewetting).
l
The numerical algorithm has to be able to deal with flows in an extended range of velocities
including subsonic and supersonic velocities.

<!-- page 663 (PDF 25) -->
l
The numerical algorithm used for thermal-hydraulic equations has to be able to deal with all
the two-phase flow regimes in the whole range of void fraction and to respect some positivity
constraint to keep the void fraction in the range [0, 1] while preserving mass and energy
conservation.
l
The numerical algorithm has to be able to work in a wide range of pressures and temperatures
: 0<Tl<350°C; 0<Tv<2000°C; 0.001 MPa<P<22 MPa.
l
When used with additional equations for noncondensable gases, the numerical algorithm
must respect some positivity constraint to keep all gas mass fractions (or molar fractions)
of each component of the gas mixture (e.g., steam-air, steam-H2, steam-N2) in the range
[0, 1] while preserving mass and energy conservation.

## 11.5.1 State-of-the-art on numerical schemes in current system codes

The numerical schemes used in current system codes meet the mandatory requirements
and differ by the robustness, accuracy, and efficiency criteria. None of them
fulfill all the criteria fully satisfactorily. The schemes implemented in the current
codes are robust and fairly efficient but not very accurate. The main capabilities
are the following ones:
Robustness: The schemes implemented in the current system codes solve the system
of equations in a very wide range of flow configurations without code failure or
with very few failures.
Accuracy: In many situations of interest, the accuracy of numerical scheme is
limited by the use of nonconverged mesh size and/or time step.
Accuracy and mesh size: The advection terms being discretized at first order, this induces
some numerical diffusion which is increasing with the mesh size. In particular temperature
of each phase and other scalar quantities (boron concentration) are artificially diffused particularly
with an implicit time discretization. In addition, most of the time, the nonspace convergence
of the calculation of wall and interfacial transfer terms induce even more
inaccuracy than the numerical diffusion. However, these wall and interfacial transfer terms
are modeled by empirical correlations which have a rather high uncertainty. At the end, the
numerical error is often acceptable since it is one order of magnitude smaller than the uncertainty
due to the imperfect physical modeling.
Higher order schemes: Other more accurate schemes exist which are operational in a smaller
range of flow configurations and still did not prove their robustness when the scope of application
is broadened. Higher order models may be used on option in some particular cases
when a temperature front or boron concentration front is transported and should not be
smoothed artificially by numerical diffusion.
Accuracy and time step. It may occur that the physics of the flow creates phenomena with
very small time scale. This is often due either to instabilities, to oscillations, or to pressure
wave propagation. Instabilities may be generated in boiling flow such as density wave oscillation
(DWO) or Ledinegg instability, or in the case of CIWH. Oscillations may be generated
between loops, or gravity oscillations between the core and the downcomer. A valve opening
or closure and a break opening induce pressure wave propagation with possible reflections
and water hammer. Such phenomena can only be captured when a sufficiently small time
step is used. It is possible that a code does not predict some of these phenomena when

<!-- page 664 (PDF 26) -->
the time step is too large. For two-phase pressure wave propagation, the time step should be
limited by the sonic velocity Cs (dt<dx/Cs) but time scales associated with flashing and condensation
may be even smaller than this, and require even smaller time steps. Boiling instabilities
at low pressure may be predicted during core reflooding when using small time step
(e.g., dt<0.005 s) and are not seen with a larger time step. Gravity oscillations may be artificially
damped if the time step is not small enough. This is particularly true for implicit time
discretization which is dissipative.
Phase appearing and disappearing. The phase appearing and disappearing when the
void fraction is close to zero or one may lead to numerical difficulties with void fractions
values out of the bounds [0, 1] at least during iterations. Special techniques are
used in system codes to guaranty that void fractions stays within bounds without having
violated mass and energy conservation. However, small time steps are often necessary
to approach the bounds with sufficiently small increments. Interfacial heat and
mass transfer models have to be conditioned in such a way that they cannot produce
vaporization when there is no more liquid and they cannot produce condensation when
there is no more steam. This looks trivial but is not so straightforward when steam is
mixed with noncondensable gases.
Time step control. The time step control includes usually both a user control and a
code time step management. When a physical situation requires a particular attention
to small time scale processes, the user must impose a maximum time step. The numerical
algorithm may not be able to obtain a convergence with this maximum time step
and codes implemented procedures to decrease the time step until convergence is
obtained. Then this time step may increase again if the numerics allows.
Water packing problem. Generic problem in two-phase flow modeled by the
two-fluid model is the possible discontinuity of void fraction when there is a free
surface level or a swell level in a vertical component or a swell level. It is found in
the former case that moving the level from one mesh to the next mesh may create
artificial pressure peaks, particularly when the water is subcooled and creates a
countercurrent flow with steam due to condensation. This is the “water packing”
problem and it is due to both an inadequate physical modeling and inadequate
space discretization in such situation. Codes have developed some interface tracking
methods which recognize the situation and apply modified physics and discretization
. A remarkable study by Aktas (2003) provides very good behavior
in TRACE.
Stability and hyperbolicity. Many instabilities exist in two-phase flow. Taylor
instability and Kelvin-Helmholtz instability are very frequent and induce bubble or
droplet break up, droplet entrainment from a free surface or a film surface. They govern
mainly the interface structure of each flow regime and some transitions between
flow regimes. Oscillations between loops, Ledinegg instabilities in parallel heated
channels, DWOs may appear and have an important effect on the global behavior
of a reactor transient. Kelvin-Helmholtz instability in a stratified flow is probably
the most abrupt change in the mechanical behavior. This instability is responsible
for the transition from a stratified flow—which is a separate-phase flow regime with
a very low coupling between phases—to a slug flow characterized by a much stronger
coupling between phases. In large diameter pipes, this transition may increase the

<!-- page 665 (PDF 27) -->
interfacial friction coefficient by several orders of magnitude in a very short time.
Such instability is even more violent when associated with condensation in the case
of CIWH.
A choice has to be made in SYS-TH codes to simulate or not the instabilities.
The answer depends on the instability:
l
Since the code intends to filter in time and space the physics, many local instabilities responsible
for the flow regime transitions may be simply taken into account by using flow regime
maps.
−
The passage from one regime to the other may be very progressive (bubbly to slug, bubbly
to churn, bubbly to stratified flow). In such case there is no difficulty to represent the
smooth physical behavior.
−
The onset of droplet entrainment is somewhat abrupt but induces a progressive change of
phase coupling since the rate of entrainment increases also progressively.
−
The transition from stratified to slug flow is more abrupt but may be smoothed in the
space-time-averaged model. The objective is to be able to predict the change of flow
regime without simulating the local instability with a free surface wave having a very
high rate of increase up to liquid bridging.
l
Large-scale instabilities which affect the system behavior should be simulated by the code.
This requires that the physical processes responsible for the instability are correctly
modeled. The two-fluid model has shown its capability to predict many of these instabilities
(Ledinegg instability, density wave instability, coupled neutronic-thermal-hydraulic
instabilities in BWR, instabilities between loops during natural circulation) provided that
time step and mesh size are sufficiently small. Such large-scale instabilities do not create
very steep gradients nor very sudden changes of flow parameters and do not challenge the
code numerics.
Current numerical schemes can then simulate the most important instabilities and can
smooth the most steep Kelvin-Helmholtz instability.
A slightly different question also associated with the stability in system codes is the
hyperbolicity of the system of equations. Since axial diffusion terms in 1-D equations
are neglected, all codes use a first-order set of PDE. A necessary and sufficient condition
for a first-order set of PDE function of time and space to be well posed is the
hyperbolicity of the system of equations. The well posedness in the sense of Hadamard
states that:
l
a solution exists,
l
the solution is unique,
l
the solution depends continuously on initial conditions.
If a problem is ill-posed, it needs to be reformulated for numerical treatment. In order
to include some smoothness in the solution. This process is known as regularization.
This question is treated in Section 5.12 (Chapter 5) and the various SYS-TH codes
adopted two main different approaches.
l
In TRAC, RELAP5, TRACE, MARS, and SPACE codes, a very pragmatic point of view has
been developed. The second-order diffusive terms that have been neglected in six-equation
model are small compared to numerical diffusion and the cell size used is such that there is no
need to add this second-order terms. Diffusion stabilize the high frequency void waves and
