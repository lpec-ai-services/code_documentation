# Time-averaged two-fluid equations
<!-- source PDF pages 37-41 -->

<!-- page 203 (PDF 37) -->
### 5.6.2.6 Locality and universality of the modeling

The “principle of locality of the modeling” is used in two-phase CFD as it is used
in single-phase CFD since closure laws are expressed only as functions of local
flow variables (i.e., velocity, density, internal energy) and their time and space
derivatives. Here the exceptions to this principle of locality are the so-called wall
functions where some closure terms depend on the distance to a wall and the equivalent
for large interfaces which may be called “interfacial functions.” This allows
using rather coarse nodalization in high shear regions close to a wall or close to a large
interface.
It was stressed that the principle of locality is more relevant when the processes to
model at point P(x,t) depend on flow conditions close to the point P. In single-phase
CFD the principle of locality is better satisfied in LES type method than in a RANS
approach since the subfilter local turbulent viscosity in a LES approach models only
effects of small eddies which are close to point P. In two-phase, there are small interfaces
(small bubbles and droplets) and also large-scale interfaces such as the large
distorted bubbles in churn flow, the free surface in stratified flow, and the film surface
in annular flow. Therefore in the flow regimes with large interfaces like slug and churn
flow, the principle of locality may only be reasonably applied in LES with deterministic
or filtered interfaces

### 5.6.2.7 Applicability and degree of maturity of the various CMFD approaches

Table 5.4 summarizes the applicability and degree of maturity of the various
two-phase CFD approaches to every flow regime. It may be seen that only two modeling
approaches can be applied to simulate physical situations where all two-phase flow
regimes may occur: the RANS (or URANS) and the LES with filtered and statistical
interfaces. However the former is more mature than the latter. The pseudo-DNS and
the LES with deterministic interfaces can address all flow regimes but are practically
limited by the required CPU time which is prohibitive in the most complex flows. The
LES with statistical interfaces cannot treat “large interfaces” and is intrinsically
limited to dispersed flows.
5.7
Time-averaged two-fluid equations
Phase time averaging or field time averaging is the most natural approach to extend
CFD RANS models to two-phase flow, Fig. 5.4. It consists in multiplying basic
equations by the phase indicator function χk of phase k.
The derivation of equations is presented in detail by Ishii and Hibiki (2011), and
various methods are also presented for dispersed flow by Morel (2015).
Following Ishii and Hibiki (2011), a general form of transport equation for a
specific quantity integrated over time period Δt is (see Fig. 5.3):

<!-- page 204 (PDF 38) -->
Table 5.4 Applicability and degree of maturity of the various two-phase CFD approaches to every flow regime
including CPU cost
Pseudo-DNS
LES simulated
interfaces
LES-VLES statistical
and filtered interfaces
LES-VLES statistical
interfaces
RANS-URANS statistical
and filtered interfaces
Bubbly
Applied
Applied
Applied
Applied
Applied
Slug-Churn
Possible
Too expensive
Possible
Too expensive
Possible
Not possible
Possible
Annular
Possible
Expensive
Possible
Expensive
Possible
Not possible
Applied
Annular-mist
Possible
Too expensive
Possible
Too expensive
Possible
Not possible
possible
Mist flow
Applied
Applied
Applied
Applied
Applied
Stratified
Applied
Applied
Applied
Not possible
Applied
Stratified-mist
Possible
Too expensive
Possible
Too expensive
Possible
Not possible
Possible
All flow
regimes
Too expensive
Too expensive
Possible
Not possible
Possible
Degree of
maturity
Average in some
flow regimes
Zero for “all
flow regimes”
Average in some
flow regimes
Zero for “all
flow regimes”
Average in some flow
regimes
Very low for “all flow
regimes”
Average in dispersed
flow
Average in some flow
regimes
Low for “all flow regimes”
Applied, is applicable and has been applied; not possible, cannot be applied due to intrinsic limitations; possible, can be applied but not very mature; expensive, requires a very high CPU time; too
expensive, unaffordable with current computer power.

<!-- page 205 (PDF 39) -->
∂εkρk
kf
ψk
k
∂t
+ r ·
εkρk
kf
vk
⃗
k
f
ψk
k
!
+ r · εk
⟨J k
k + Jt
k
□
□
h
i
= εkρk
kf
ϕk
k + 1
Δt
X
j
vni
n
⃗
k · ρk vk
⃗− vi
⃗
□
□
ψk
h
i
+ n
⃗
k · Jk
□
□
ϕk is the volumetric source of ψk in phase k
Jk is the diffusive flux of ψk in phase k
Mass momentum and total energy balance equations can be written considering the
respective ψk, ϕk, and Jk, as given in Table 5.5.
Fk
⃗
isthespecificexternalforceonphasek(N/kgorm/s2)usuallylimitedtogravityforce(F
⃗=g
⃗)
Tk is the stress tensor in phase k (Pa or N/m2)
q
⃗
k is the heat flux vector in phase k (W/m2)
qext is the external volumetric source of energy (usually radiation)
n
⃗
k is the unit vector normal to the interface oriented outside of phase k
v
⃗
ni is the component of velocity of interface normal to the interface
v
⃗
ti is the component of velocity of interface tangential to the interface
Jk
t is the turbulent flux of ψk
Jt
k≜χkρk vk
⃗ψk
εk
−ρk
kf
vk
⃗
k
f
ψk
k
This term results from averaging of a product for convection terms.
The second RHS term takes account of convective and diffusive fluxes through all
interfaces which passed at point x during the period of time Δt.
One obtains the following set of phase mass, momentum, and energy equations:
∂εkρk
k
∂t
+ r ·
εkρk
kf
vk
⃗
k
!
= 1
Δt
X
j
vni
n
⃗
kρk vk
⃗− vi⃗
□
□
h
i
□
□
≜γik
γik is the time averaged interfacial mass transfer per unit volume (kg/m3/s)
Table 5.5 Volumetric source and surface source
in mass momentum and total energy equations
ψk
ϕk
Jk
Mass
Momentum
vk⃗
Fk
⃗
−Tk
Energy
uk + vk⃗2
qkext + Fk
⃗
· vk⃗
qk
⃗−Tk· vk⃗

<!-- page 206 (PDF 40) -->
∂εkρk
kf
vk
⃗
k
∂t
+ r ·
εkρk
kf
vk
⃗
kf
vk
⃗
k
!
+ εkrpk
k
= εkρk
k g
⃗ + r · εk T k + T t
k
□
□
+ M
⃗
ik
M
⃗
ik = 1
Δt
X
j
vni
n
⃗
k ·ρk vk
⃗− vi⃗
□
□
vk
⃗
h
i
− n⃗
k ·Tk
□
□
A very common approximation is to consider a unique pressure for both phases:
pf
f = pg
g = ⟨p
Mik is the time-averaged interfacial momentum transfer per unit volume (N/m3)
The first term is usually modeled as:
Δt
X
j
vni
n
⃗
kρk vk
⃗− vi⃗
□
□
vk
⃗
h
i
□
□
ffiγik
f
vk
⃗
k
The second term is the most complex contribution since it contains pressure and viscous
forces applied to a moving deformable interface which may have very diverse
forms depending on the flow regime.
A very common approximation is to consider a part equal to ⟨prεk and model the
rest as several forces.
M
⃗
ik = ⟨p rεk + M
⃗D
ik + M
⃗L
ik + M
⃗AM
ik + M
⃗TD
ik
The drag force M
⃗D
ik is a coupling between average phase velocities. For a bubble this is
written as:
M
⃗D
ig = −M
⃗D
if = −aiCd
8 ρf
f
vg
⃗
g
− f
vf⃗
f
□□□□□
□□□□□
f
vg
⃗
g
− f
vf⃗
f
!
The lift force M
⃗L
ik is a force applied to a particule (bubble or drop) of a dispersed phase
d. It is perpendicular to the velocity difference between phases and is proportional to
the rotational of the continuous phase c.
M
⃗L
id = −M
⃗L
ic = −CLεdρc
f
vd
⃗
d
− f
vc
⃗
c
!
^
r^ f
vc
⃗
c
(
The added mass force M
⃗AM
ik is a coupling between phase accelerations. A particle (bubble
or drop) which accelerates has to accelerate the fluid around it and this increases its
inertia. It was established first for a sphere accelerating in an infinite medium by

<!-- page 207 (PDF 41) -->
solving inviscid flow equations. This force is particularly important for dispersed gas
since the fluid around the bubble has a high density, and it may be neglected for drops
since the gas around the drop has a low density. It is also not considered in
separate-phase flows such as annular flow or stratified flow.
A possible expression for a bubbly flow is:
M
⃗AM
ig = −M
⃗AM
if
= CAM 1 + 2εg
1−εg
εgρf
∂f
vg
⃗
d
∂t
+ f
vg
⃗
g
·rf
vg
⃗
g
B
@
C
A−
∂f
vf⃗
f
∂t
+ f
vf⃗
f
·rf
vf⃗
f
B
@
C
A
The turbulent dispersion force M
⃗TD
ik is associated to the fluctuating part of all forces
which has been identified as an important contribution in dispersed flow (see
Morel, 2015). It includes the mixing effect of dispersed particles by turbulent eddies.
One of the simplest models has the following form which uses the turbulent kinetic
energy kc of the continuous phase.
M
⃗TD
id = −M
⃗TD
ic = CTDρckcrεd
The total energy equation writes:
∂
∂t εkρk
k
euk
k +
f
vk
⃗
k2
B
@
C
A
75 + r ·
εkρk
kf
vk
⃗
k
euk
k +
f
vk
⃗
k2
B
@
C
A
= εkρk
k g
⃗ ·f
vk
⃗
k
−r· εk
q
⃗
k
k
+ q
⃗t
k
(
+ qrk + Eik + r· εk ⟨T k + T t
k
· f
vk
⃗
k
"
Eik = − 1
Δt
X
j
vni
n
⃗
kρk · vk
⃗− vi
⃗
□
□
uk + vk2
(
− n
⃗
k ·Tk· vk
⃗ + n
⃗
kq
⃗
k
□
□
Eik is the time-averaged interfacial energy transfer per unit volume (W/m3)
The contribution of the stress tensor is often neglected and Eik is usually modeled as
function of interfacial mass transfer γik and interfacial heat transfers qik:
Eik ffiqik + γik
ehk
k +
f
vk
⃗
k2
B
@
C
A
A RANS two-fluid model as it was used for adiabatic bubbly flow by Krepper et al.
(2011), and for boiling bubbly flow by Koncar et al. (2011), is summarized hereafter:
RANS two-fluid equations for CMFD: 3-D 2-phase flow equations
Principal variables: ⟨p, εg, f
vg
⃗
g
, f
vf
⃗
f
, ehg
g, ehf
f
∂εkρk
k
∂t
+ r ·
εkρk
kf
vk
⃗
k
!
= γik
