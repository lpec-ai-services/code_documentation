# The time-averaged single-phase equations
<!-- source PDF pages 18-21 -->

<!-- page 184 (PDF 18) -->
5.4
The time-averaged single-phase equations
5.4.1
Reynolds averaging—time averaging
Time averaged single-phase equations are used in single-phase RANS CFD models.
CFD is presented in more detail in Chapter 12. So these equations are just rapidly presented
here in view of using them for double-space time-averaging of 0-D, 1-D, 2-D,
and 3-D models for porous body.
When boundary conditions of a flow are steady—not considering turbulent
fluctuations—time-averaged equations are used. The Reynolds averaging was applied
to steady of quasi-steady flows where time scales of mean flow variations are significantly
larger than time scales of turbulent fluctuations. Time averaging over a time
period T is:
f = 1
T
ð
T
f dt
f ≜f + f 0
If variations of f over a time scale T is negligible, then
f 0 = 0
The properties of the Reynolds averaging are such that:
cf = cf if c = cte
⟨f = f
fg = f g
∂f
∂x = ∂⟨f
∂x
∂f
∂t = ∂⟨f
∂t
One can consider three level of compressibility of the fluid:
1. Incompressible flow for low Mach flow without dilatation:
ρ = ρ0 = cte
2. Dilatable flow for low Mach flow with dilatation:
ρ = ρ0 1−β T −T0
ð
Þ
½
□

<!-- page 185 (PDF 19) -->
3. Compressible flow:
ρ = P, T
ð
Þ
In the most general case one may average local instantaneous equations and obtain the
following mass, momentum, and total enthalpy equations:
∂ρ
∂x + ∂ ρvJ
∂xj
= 0
∂ ρvJ
∂t
+ ∂ρvIvJ
∂xi
+ ∂⟨p
∂xj
= −ρgi + μ ∂2⟨vJ
∂xi2 + 1
∂2⟨vi
∂xj∂xi
∂
∂t ρu + ρv2
"
+ ∇ · ρuv⃗ + ρv⃗v2
"
− F
⃗ · ρv⃗ −∇ ·
T · v⃗
□
□
+ ∇ · q
⃗ = qext
∂
∂t ρh + ρv2
2 − ⟨p
"
+ ∇ · ρhv⃗ + ρv⃗v2
"
− F
⃗ · ρv⃗ −∇ ·
T · v⃗
□
□
+ ∇ · q
⃗ = qext
It is usual to define mass-weighted average quantities of velocity, internal energy, or
enthalpy
evj = ρvj=ρ
eu = ρu=ρ
eh = ρh=ρ
Mass balance equation is thus simplified
∂ρ
∂t + ∂ρevj
∂xj
= 0
But the averaging of the nonlinear momentum balance advection term induces an
additional tensor T t of components Rij
T t ≜ρ v
⃗v
⃗ −ρev
⃗ ev
⃗ ; Rij ≜ρvivj −ρevievj
Rij is called the Reynolds stress tensor
The averaging of the nonlinear enthalpy balance advection term induces also an
additional vector term q
⃗t which is a turbulent heat transfer: or
q
⃗t≜ρh v
⃗ − ρehev
⃗ ; qt
j ≜ρhvj − ρehevj

<!-- page 186 (PDF 20) -->
## 5.4.2 Incompressible flow

In the case of an incompressible flow:
∂⟨vj
∂xj
= 0
ρvivj ≜ρ⟨vi⟨vj + ρv0
iv0j; Rij = ρv0
iv0j
ρhvj ≜ρ⟨h⟨vj + ρh0v0j ; qt
j = ρh0v0j
∂⟨vj
∂t + ∂vivj
∂xi
+ 1
ρ
∂⟨p
∂xj
= −gj −∂Rij
∂xi
+ ν ∂2⟨vj
∂xi2
∂
∂t ρ
⟨h + ⟨v2
2 + k
(
− ⟨p
+ r· ρ
⟨hv
⃗ + v
⃗v2
!
"
−ρ F
⃗ · v
⃗−r· T · v
⃗
□
□
+ r·
q
⃗ + q
⃗t
□
□
= qext
k = 1
2v0
iv0i is the turbulent kinetic energy
when Cp = ct
ρhvj ≜ρ⟨h⟨vj + ρCpT0v0j ;qt
j = ρCpT0v0j
This shows that Rij and qt
j are representing, respectively, a transport of momentum and
energy by velocity fluctuations. By analogy with transport by molecular agitation,
they were first modeled as diffusive terms.
A usual modeling consists in using a turbulent viscosity and turbulent
conductivity:
T t ≜Rij = −ρv0
iv0
j = ρ −2
3 kδij + νt
∂⟨vi
∂xj
+ ∂⟨vj
∂xi
(
qt
j = ρCpu0
jT0 = −λt
∂ ⟨T
∂xj
λt = Cpμt
Prt
u0jYk0 = −DYk t
∂ ⟨Yk
∂xj
DYk t = νt
Sct
Considering an isotropic turbulent viscosity one can model it as a product of a turbulent
length scale l with a turbulent velocity scale v0
νt ≡ lv0

<!-- page 187 (PDF 21) -->
Following Kolmogorov, in high Reynolds number flows the dissipation ε is controled
by inertial processes and does not depend on viscosity. Then from dimensional
analysis one can write:
ε ≡ v03
l
Using the turbulent kinetic energy k as the square of the velocity scale:
νt ≡ v04
ε = Cμ
k2
ε
This relation opens the way to the very popular k−ε turbulence model which requires
transport equations for k and ε. It belongs to the first-order RANS models.
Many other turbulence model exist for Rij and qt
j. More advanced second-order
RANS models write separate equations for each component of the Rij tensor
and q
⃗t vector which may be complemented by equations for ε, temperature variance
kθ = T
02, and its associated dissipation εθ.

## 5.4.3 Closure of the time-averaged equations

In order to close the system of time-averaged equations, some simplifications and
models are necessary:
l
A choice is first made of using only time averaging of all variables or using mass-weighted
averaging of velocity and enthalpy
l
Expression for Rij: models developed first for incompressible flows were extrapolated to
compressible flow with some adaptation
l
Expression for qj
t : models developed first for incompressible flows were extrapolated to
compressible flow with some adaptation
l
Expression for: ρv2
2 :
□
it may be approximated by ρv2
2 ffiρ⟨v2
2 + ρk and k may be neglected considering that:
⟨v2
2 ≫k
□
it may be also approximated by ρv2
2 ffiρev2
2 + ρk and k may be neglected considering that:
ev2
2 ≫k
l
Expression for r· T : v
⃗
□
□
may require simplification of average of products:
□
r· T · v
⃗
□
□
ffir·
⟨T · v
⃗
□
□
□
or r· T · v
⃗
□
□
ffir·
eT ·ev
□
□
