# Introduction to balance equations
<!-- source PDF pages 8-13 -->

<!-- page 174 (PDF 8) -->
5.1
Introduction to balance equations
The objective of this chapter is to give minimum information to engineers on most
current systems of equations used to describe and predict single- and two-phase flow
in nuclear reactor thermal-hydraulic studies. Various modeling approaches are possible
, and a few reference books exist on the mathematical derivation of the systems of
equations (Delhaye et al., 1981; Lahey and Moody, 1993; Ishii and Hibiki, 2011;
Morel, 2015). Fundamental research in the area was also done by Boure (see, e.g.,
Boure, 1975). Details of all existing approaches will not be repeated here, and the following
sections are focused on some important aspects of the most common set of
equations used in system codes and some computational fluid dynamics (CFD) codes.
Attention will be drawn on the physical assumptions and simplifications used to derive
the equations and on the resulting limitations of the predictive capabilities.
After having recalled the basic principles of thermodynamics and fluid mechanics,
the local instantaneous mass, momentum, and energy equations are given. Then, the
various approaches to single- and two-phase flow modeling are presented and classified.
The time-averaged, single-phase equations are derived to introduce the CFD approach
and the turbulence modeling. The space averaged 1-D equations for single-phase
flow are derived as they may be a very reasonable approximation in many situations.
Then two-phase modeling is considered in the frame of the two-fluid approach.
Time-averaged, two-fluid equations are given, and the derivation of space averaged
1-D equation is summarized in view of identifying the most important simplifications,
before presenting the time-space averaged 1-D two-fluid system of equation as it is used
in current system codes. Some simple two-phase models, such as the homogeneous
equilibrium model (HEM), and the drift flux model are here presented as simplifications
of the two-fluid model although they were previously developed, in order to better identify
the degree of approximation as function of the flow regime. Some recent advances
on two-phase flow modeling include transport of interfacial area (TIA) and the
three-filed model. Equations used in these new approaches are also given.
5.2
The principles of thermodynamics and mechanics
All
fluids
considered
in
reactor
thermal-hydraulics
are
here
considered
as
Newton-Stokes fluids. They may be present as a single-component (species) fluid or
multicomponent fluid. They may be present as a single-phase liquid, a single-phase
gas, or even as a two-phase gas-liquid. It may happen that a dominant species (e.g.,
water) is present in both liquid and vapor phases with some other species present as
noncondensable gas in a gas mixture or diluted in liquid (boron, nitrogen,…).

## 5.2.1 The local instantaneous equations

The three basic equations result from the basic principles:
−
mass conservation
−
Newton’s second law of motion applied to fluid flow
−
energy conservation (first principle of thermodynamics)

<!-- page 175 (PDF 9) -->
Let us consider a fluid volume V(t) limited by a surface A(t) as in Fig. 5.1. One may consider
the variation of some specific quantity ψ using the general conservation equation:
d
dt
ð
V tð Þ
ρ ψ dv =
ð
V tð Þ
ρϕdv−
ð
A tð Þ
ρψ v⃗ − vA
⃗
□
□
· n
⃗ da−
ð
A tð Þ
J· n
⃗
□
□
da
(5.1)
where −
ð
A tð Þ
ρψ v⃗ − vA
⃗
□
□
· n
⃗ da is the flowrate of ψ entering through A(t) and:
n
⃗ is the unit vector directed outside V(t)
ρ is the fluid density (kg/m3)
v
⃗ is the velocity vector (m/s)
vA
⃗ is the surface velocity vector (m/s)
ϕ is the volumetric source of ψ within V(t)
J is the diffusive flux of ψ through A
Mass momentum and total energy balance equations can be written considering the
respective ψ, ϕ, and J
⃗ given in Table 5.1.
F
⃗ is the specific external force (J/kg or m/s2) usually limited to gravity force (F
⃗=g
⃗)
T is the stress tensor (Pa or N/m2)
q
⃗ is heat flux vector (W/m2)
qext is the external volumetric source of energy (usually radiation)
The Leibniz rule applied to a sufficiently regular function f(x, y, z, t) writes:
d
dt
ð
V tð Þ
f dv =
ð
V tð Þ
∂f
∂t dv +
ð
A tð Þ
f vA
⃗ · n
⃗ da
Fig. 5.1 Volume V(t) limited by a surface A(t).
Table 5.1 Volumetric source and surface source in mass momentum
and total energy equations
ψ
ϕ
J
Mass
Momentum
v
⃗
F
⃗
−T
Energy
u + v2
qext + F
⃗ · v
⃗
q
⃗ −T· v
⃗

<!-- page 176 (PDF 10) -->
Applied to f=1 it shows that:
ð
A tð Þ
vA
⃗ · n
⃗ da = dV tð Þ
dt
The Gauss theorem applied to a vector a
⃗ and a tensor B writes:
ð
V tð Þ
∇ · a
⃗ dv =
ð
A tð Þ
a
⃗ · n
⃗ da
ð
V tð Þ
∇ · Bdv =
ð
A tð Þ
B · n
⃗ da
Using Leibniz rule and Gauss theorem, one can write all terms of the balance Eq. (5.1)
using only volume-averaged terms. Applied to an elementary volume of fluid, it
results in local instantaneous mass, momentum, and energy equations (see Delhaye
et al., 1981).
The mass balance equation or continuity equation is:
∂ρ
∂t + ∇ · ρ v⃗
□
□
= 0
The momentum balance equation is:
∂ρ v⃗
∂t
+ ∇ · ρ v⃗ v⃗
□
□
−ρ F
⃗ −∇ · T = 0
The total specific energy (internal energy+kinetic energy) balance equation is:
∂
∂t ρ u + v2
(
+ ∇ · ρ v⃗
u + v2
(
−ρ F
⃗ · v⃗ −∇ · T · v⃗
□
□
+ ∇ · q
⃗= qext
u is the specific internal energy
v2 =v⃗ · v
⃗ is the specific kinetic energy (m2/s2)
T is split into a pressure tensor and deviator stress tensor T
T ≜T + p I
τij are the components of tensor T
p is the pressure (Pa)
I is the identity tensor

<!-- page 177 (PDF 11) -->
Separating the contributions of pressure and T :
∂
∂t ρ u + v2
(
+ ∇ · ρ v⃗
u + v2
(
−ρ F
⃗ · v⃗ + ∇ · p v⃗
□
□
−∇ · T · v⃗
□
□
+ ∇ · q⃗= qext
A total specific enthalpy equation can be written as:
∂
∂t ρ h + v2
(
−p
+ ∇ · ρ v⃗
h + v2
(
−ρ F
⃗ · v⃗ −∇ · T · v⃗
□
□
+ ∇ · q
⃗= qext
h is the specific enthalpy
h = u + p
ρ
The momentum equation can then be written as
∂ρ v⃗
∂t
+ ∇ · ρ v⃗ v⃗
□
□
+ ∇p−ρ F
⃗ −∇ · T = 0
and can be projected along each coordinate in a Cartesian frame, using summation on
repeated indices:
∂ρvj
∂t + ∂ρvivj
∂xi
+ ∂p
∂xj
−ρFj −∂τij
∂xi
= 0
One can also write an equation for the specific kinetic energy v2
2 by multiplying
the momentum energy by the velocity vector v
⃗
∂ρv2.
∂t
+ ∇ ·
ρ v⃗ v2
(
−ρ F ·
⃗
v⃗ + v⃗ · ∇p− v⃗ · ∇ · T = 0
which can be subtracted from total energy or total enthalpy equations to obtain internal
energy and enthalpy equations:
∂ρu
∂t + ∇ · ρ v⃗ u
□
□
+ p∇ · v⃗ −T : ∇ v⃗ + ∇ · q
⃗= qext
∂ρh
∂t + ∇ · ρ v⃗ h
□
□
−∂p
∂t − v⃗ · ∇p−T : ∇ v⃗ + ∇ · q
⃗= qext
The flow can be solved by using a system of equations with the mass balance, the
momentum balance, and one of the various forms of energy or entropy equations
complemented with equations of state and expressions of q
⃗ and T .

<!-- page 178 (PDF 12) -->
The Fourier law is used for q
⃗:
q
⃗= −λ ∇T
λ is the heat conductivity (W/m/K)
In Newton-Stokes fluid, T writes:
T = −2
3μ∇ · v⃗ I + μ ∇ v⃗ + t∇ v⃗
□
□
μ is the dynamic viscosity (kg/m/s)
The thermodynamic state of a single-phase single-component fluid is characterized
by the knowledge of two independent state variables such as pressure and temperature
(p, T) or (p, h), (p, u).
Let us consider that (p, h) are chosen as independent variables, the necessary equations
of state are:
ρ p, h
ð
Þ;T p, h
ð
Þ;μ p, h
ð
Þ;λ p, h
ð
Þ
Combining above equations can then result in three equations with three independent
unknowns p, h, and v
⃗ such as:
∂ρ
∂t + ∇ · ρ v⃗
□
□
= 0
∂ρ v⃗
∂t
+ ∇ · ρ v⃗ v⃗
□
□
+ ∇p−ρ F
⃗ −∇ · −2
3μ∇ · v⃗ I + μ ∇ v⃗ + t∇ v⃗
□
□
= 0
μ is often considered as nearly homogeneous so that:
∂ρ v⃗
∂t
+ ∇ · ρ v⃗ v⃗
□
□
+ ∇p−ρ F
⃗ −μ
3∇ ∇ · v⃗ + ∇ 2 v⃗
(
= 0
∂
∂t ρ h + v2
(
−p
+ ∇ · ρ v⃗
h + v2
(
−ρ F
⃗ · v⃗ −∇ · T · v⃗
□
□
−∇ · λ ∇T
ð
Þ = qext
Momentum equation for each component is:
∂ρvj
∂t + ∂ρvivj
∂xi
+ ∂p
∂xj
= −ρgj + μ ∂2vj
∂xi2 + 1
∂2vi
∂xj∂xi
The entropy equation writes:
ρ ds
dt = qext
T −∇ ·
q
⃗
T
 !
+ T : T
2μT + λ ∇T
ð
Þ2
T2

<!-- page 179 (PDF 13) -->
The two last terms of the entropy equation are the irreversible entropy sources associated
to viscous dissipation and heat conduction.
The second principle of thermodynamics just indicates that μ > 0 and λ > 0.
The single-component single-phase flow equations of Newton-Stokes fluid can be
summarized as in the following if we use the total enthalpy equation. Note that the
principal variables are here p, h, and v
⃗:
Basic equations: 1-Component 1-phase flow equations for a
Newton-Stokes fluid
Principal variables: p, v
⃗, h
∂ρ
∂t + ∇ · ρ v
⃗
□
□
= 0
∂ρ v
⃗
∂t
+ ∇ · ρ v
⃗ v
⃗
□
□
+ ∇p−ρ F
⃗
−μ
3∇ ∇ · v
⃗ + ∇ 2 v
⃗
(
= 0
∂
∂t ρ h + v2
(
−p
+ ∇ · ρ v⃗
h + v2
(
−ρ F
⃗
· v⃗ −∇ ·
T · v⃗
□
□
−∇ · λ ∇T = qext
T = −2
3μ∇ · v⃗ I + μ ∇ v⃗ + t∇ v⃗
□
□
;
ρ = ρ p, h
ð
Þ;T = T p, h
ð
Þ;μ = μ p, h
ð
Þ;λ = λ p, h
ð
Þ
In a multicomponent fluid flow with n species, n−1 equations are added to predict
mass concentration of each species.
∂ρYk
∂t
+ ∇ · ρYk v⃗
□
□
= ∇ ·
−⃗
_mYk
□
□
+ SYk
−⃗
_mYk = DYk∇Yk
which can be written as:
∂ρYk
∂t
+ ∂ρvjYk
∂xj
= ∂
∂xj
DYk
∂Yk
∂xj
(
+ SYk
Yk is the mass concentration of species k
ρ is the density of the mixture
X
k=1,nYk = 1
where −⃗
_mYk is the diffusion mass flux vector of component k within the mixture
(kg/m2/s)
