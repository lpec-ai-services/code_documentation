# Some simplified two-phase models: HEM drift-flux model
<!-- source PDF pages 57-64 -->

<!-- page 223 (PDF 57) -->
Axial diffusion and dispersion terms of energy are not included in standard models
but some options may exist and may be actuated for some specific transients. Axial
diffusion and dispersion terms of mass concentrations of transported species like
boron or radio-active components, which are treated as passive scalars, may also
be added on option.
Energy equation may be written as a total enthalpy equation (CATHARE) or as
internal energy equation (RELAP-5) or as total energy equation (TRACE):
A∂αkϱkUk
∂t
+ ∂AαkϱkVkUk
∂z
= −AP∂αk
∂t −P∂AαkVk
∂z
+ Ckqwk + Aqik + AΓikHK + Aqkext + Dk
Dk is a viscous dissipation in phase k
A
∂αkϱk Uk + Vk2
(
∂t
+
∂AαkϱkVk Uk + Vk2
(
∂z
+ ∂AαkVkP
∂z
= AαkϱkgzVk
+ Ckqwk + Aqik + AΓikHki + AτikVk + AτwkVk + Aqkext
5.11
Some simplified two-phase models: HEM
drift-flux model

## 5.11.1 From one- to two-fluid models

Historically, two-phase steam-water flows were first described as a one-fluid forming
a homogeneous mixture following approximately the single-phase set of equations
with some minor modifications. A 1-D one-fluid 3-equation two-phase flow model
was the first set of equations used to describe steam-water flow in a reactor. It can
use both mechanical and thermodynamic equilibrium in the HEM or it may accept
some velocity difference (slip between phases) expressed by an algebraic relation.
Before going to the 1-D 6-equation two-fluid model, some 4-equation or 5-equation
models were used in some codes for steam-water flow to describe thermodynamic
nonequilibrium of one phase or both phases.
In two-phase steam-water flow, the interface between phases is at saturation temperature
. A phase can be at thermodynamic equilibrium in a two-phase system when it
is at saturation temperature (Tk = Tsat P
ð ÞÞ. A phase can be out of thermodynamic
equilibrium in a two-phase system when it is either subcooled (Tk < Tsat P
ð ÞÞ or superheated
(Tk > Tsat P
ð ÞÞ.
Phases may have different velocities when different forces are applied to them.
For example the gravity force being proportional to the phase density creates some
differences between phases. Also the same friction force along walls is not applied to
both phases, which may affect the two velocities. Mechanical interactions between

<!-- page 224 (PDF 58) -->
phases (drag force, added mass force) tend to couple phases and to reduce the slip
between phases. As a result of all forces there may be an equilibrium slip between
phases. Due to different inertia of phases—corresponding to different densities—
there may be some acceleration of phases before reaching an equilibrium slip which
may be expressed as an algebraic relation between gravity, drag, and wall friction
forces. The simplest assumption considers an equilibrium slip with no velocity difference
. This corresponds to an infinite drag coefficient. A more realistic assumption
considers that phases are always at equilibrium slip: only an algebraic relation
between phase velocities is sufficient. The most realistic treatment is to consider
the different inertia of phases, which requires separate momentum equations for each
phase. Table 5.6 summarizes the existing models from one-fluid to two-fluid system
of equations.
Let us define some quantities:
ϱk≜c
ρk
k≜χkρk
h
iS
αk
space-time phase average density
ϱm≜αvϱv + αlϱl
space-time mixture average density
Pk≜c
pk
k≜χkpk
h
iS
αk
space-time phase average pressure
P≜αvPv + αlPl
space-time mixture average pressure
Vk≜vzk⟩k≜χkρkvzk
h
iS
χkρk
h
iS = χkρkvzk
h
iS
αkc
ρk
k
mass-weighted space-time phase average velocity
Gk≜αkϱkVk = χkρkvzk
h
iS
phase mass flux
G≜Gv + Gl
mixture mass flux
Hk≜Hk⟩k≜χkρkhk
□
□S
χkρk
h
iS =
d
ρkhk
k
c
ρk
k
mass-weighted space-time phase average enthalpy
Pk≜c
pk
k≜χkpk
h
iS
αk
space-time phase average pressure
P≜αvPv + αlPl
mixture space-time average pressure
Hm≜αvϱvHv + αlϱlHl
ϱm
mass-weighted space-time mixture average enthalpy
H
z}|{
k≜χkρkvzkhk
□
□S
χkρkvzk
h
iS = αk ρkvzkhk
□
□S
Gk
mass flux weighted space-time phase average enthalpy
H
z}|{
m≜GvH
z}|{
v + GlH
z}|{
l
G
mass flux weighted space-time mixture average enthalpy
x≜αvϱv
ϱm
static quality
X≜Gv
G
dynamic quality
Xth≜H
z}|{
m −hlsat
hvl
thermodynamic quality (or equilibrium quality)

<!-- page 225 (PDF 59) -->
Table 5.6 The various steam water models from 1-fluid to 2-fluid system of equations
Mass balance
Momentum
balance
Energy balance
Thermodynamic
equilibrium assumptions
Mechanical equilibrium
assumptions
3-Equation HEM
1 Mixture equation
1 Mixture equation
1 Mixture equation
Both phases at saturation
No slip between phases
3-Equation +
drift flux
1 Mixture equation
1 Mixture equation
1 Mixture equation
Both phases at saturation
Algebraic equilibrium-slip
between phases
4-Equation +
drift flux
2 Equations
1 Mixture equation
1 Mixture equation
1 Phase at saturation
1 Phase out of equilibrium
Algebraic equilibrium-slip
between phases
5-Equation +
drift flux
2 Equations
1 Mixture equation
2 Equations
Both phases out of
equilibrium
Algebraic equilibrium-slip
between phases
6-Equation
2 Equations
2 Equations
2 Equations
Both phases out of
equilibrium
No mechanical equilibrium
between phases

<!-- page 226 (PDF 60) -->
## 5.11.2 The homogeneous equilibrium model (HEM)

The HEM is the simplest model to describe a steam-water flow. It assumes that both
phases are tightly mechanically and thermally coupled so that they have the same
mean velocity Vv = Vl
ð
Þ and the same temperature. Since the two-phase mixture is
supposed to be at thermodynamic equilibrium, it results that both phases are at saturation
temperature when they coexist.
The 1-D HEM model is here reestablished starting from the 1-D two-fluid
formulation.
Adding the two phasic mass balance equations provides the mixture mass balance
equation. Adding the two phasic momentum balance equations provides the mixture
momentum balance equation. Adding the two phasic total enthalpy balance equations
provides the mixture total enthalpy balance equation. The variations of kinetic energy
and the work of gravity are neglected. The axial diffusion and dispersion terms are also
neglected.

### 5.11.2.1 A single set of equations from single-phase liquid to single-phase steam

The one-fluid HEM model is able to treat continuously a flow of subcooled water
which receives heat, vaporizes progressively up to a full superheated vapor flow
which can then be cooled and condensate to come back to a pure liquid flow.
Depending on the value of the mean mixture enthalpy one can consider three cases,
giving the following set of equations with P, G, and H being the three principal
variables:
1-D HEM equations
Main variables: P, G, H
z}|{
m
A∂ρm
∂t + ∂AG
∂z = 0
A∂G
∂t +
∂AG2.
ρm
∂z
+ A∂P
∂z = Aρmgz −Cτw − A
δzδpsing
Aρm
∂Hm
∂t + AG∂ H
z}|{
m
∂z −A∂P
∂t = Cqw
H
z}|{
m < hlsat ; Xth ≜Hl −hlsat
hlv
< 0; αv = x = X = 0
Hm = H
z}|{
m = Hl;ρm = ρl P, Hl
ð
Þ; T = Tl P, Hl
ð
Þ

<!-- page 227 (PDF 61) -->
H
z}|{
m > hvsat ;Xth ≜Hv −hlsat
hlv
> 1;αv = x = X = 1
Hm = H
z}|{
m = Hv; ρm = ρv P, Hv
ð
Þ; T = Tv P, Hv
ð
Þ
hlsat 	 H
z}|{
m 	 hvsat ; 0 < Xth < 1; Xth = X = x = H
z}|{
m −hlsat
hlv
Hm = H
z}|{
m = xhvsat + 1−x
ð
Þhlsat
αv =
H
z}|{
m −hlsat
□
□
ρlsat
hvsat − H
z}|{
m
□
□
ρvsat +
H
z}|{
m −hlsat
□
□
ρlsat
ρm =
ρlsatρvsathlv
hvsat − H
z}|{
m
□
□
ρvsat +
H
z}|{
m −hlsat
□
□
ρlsat
+ expressions for τw,δpsing,qw

### 5.11.2.2 Predictive capabilities of the 1-D HEM set of equations

Although the 1-D HEM set of equations looks very close to the single-phase 1-D set of
equation the predictive capabilities are much worse and can be very poor depending
on the two-phase flow situation. Main limitations are:
l
The no-slip assumption is almost always far from the reality and is the main source of error. It
may be a reasonable approximation only in the case of a bubbly flow with very small bubbles
. It is totally wrong in separate-flow, such as annular flow and stratified flow and is also a
bad approximation for droplet flow.
l
The thermodynamic equilibrium of both phases does not allow good prediction of condensing
flow and in post-CHF conditions with inverse-annular, inverse-slug, and dispersed flow.
l
Closure laws for τw and qw are available but are much more complex and must take into
account a large number of flow regimes and heat transfer regimes. There are generally much
less accurate than closure laws of single phase flow.

## 5.11.3 The drift flux model

The drift flux model was the first approach which could better model the mechanical
interactions between phases and describe the slip between phases.
It can easily be obtained from simplification of the two-fluid model only if phase
density variations within the time-space averaging domain are neglected.

<!-- page 228 (PDF 62) -->
Let us define some quantities:
local phase time averaged velocity:
⟨vk
zk≜χkvzk
εk
Phase k local superficial velocity:
jk≜χkvzk = εk⟨vk
zk
Local mixture superficial velocity:
j≜jv + jl
Phase k superficial velocity:
Jk≜jk
h iS = εk⟨vk
zk
□
□S
Mixture superficial velocity:
Jm≜Jv + Jl
Space-time phase averaged velocity:
Vk≜Jk
αk
= χkvzk
h
iS
χk
h
iS
Distribution parameter
Co≜
εvj
h
iS
εv
h
iS jh iS = εvj
h
iS
αvJ
Drift velocity
Vgj≜εv ⟨vv
zv −j
□
□S
αv
From the identity:
jv = εv⟨vv
zv = εvj + εv ⟨vv
zv −j
one can write:
jv
h iS = εvj
h
iS + εv ⟨vv
zv −j
□
□S
and dividing by αv obtain the drift flux identity:
Vv = CoJ + Vgj
where the difference between the average gas velocity Vv and the mixture superficial
velocity J is due to two effects:
l
void and velocity profiles effects when Co 6= 1
l
average local slip between phases through Vgj 6= 0
An approximation neglecting the density variations within the time-space averaging
domain simplifies expressions of accumulation and advection terms of the equations.
On can then consider that:
Vk≜χkρkvzk
h
iS
χkρk
h
iS ffiVk = χkvzk
h
iS
χk
h
iS
Hk≜hk⟩k≜χkρkhk
□
□S
χkρk
h
iS ffihk
ck = χkhk
□
□S
χk
h
iS
Provided that good models are available to express Co and Vgj, the simple algebraic
relation between the phase velocities and the void fraction can eliminate one partial
differential equation (PDE) of the 1-D 6-equation 2-fluid model:
Vv 1−Coαv
ð
Þ = Co 1−αv
ð
ÞVl + Vgj

<!-- page 229 (PDF 63) -->
It can also be used together with a 1-D 3-equation model (using thermodynamic equilibrium
) to remove the main drawback of the HEM model.

## 5.11.3 Drift-flux model versus two-fluid model

Let us consider momentum equations of the two-fluid model and in the drift flux
approach. In the two-fluid model one writes two-phase momentum equations:
A∂αkϱkVk
∂t
+ ∂AαkϱkVkVk
∂z
+ Aαk
∂P
∂z + Afi
∂αk
∂z + gk
∂A
∂z
= Aαkϱkgz −Aτik −Ckτwk −Aαk
δPksing
δz
+ AFAM
k
+ AΓikVi
One can write the mixture momentum equation by adding them:
A∂αvϱvVv + αlϱlVl
∂t
+ ∂A αvϱvVvVv + αlϱlVlVl
½
□
∂z
+ A∂P
∂z + gv + gl
ð
Þ∂A
∂z
= Aϱmgz −Cvτwv −Clτwl −A αvδPvsing + αlδPlsing
δz
(
and one can obtain a “cross-momentum equation” by elimination the pressure gradient
term between the two-phase equations:
A αl
∂αvϱvVv
∂t
−αv
∂αlϱlVl
∂t
+ αl
∂AαvϱvVvVv
∂z
−αv
∂AαlρϱlVlVl
∂z
= − Afi
∂αv
∂z − gvαl −αvgl
½
□∂A
∂z −A αvαl ϱl −ϱv
½
□gz
−Aτiv −Cvαlτwv + Clαvτwl −Aαvαl
δPvsing −δPlsing
δz
(
+ AFAM
v
+ AΓivVi
Let us consider a quasi-steady flow
∂
∂t ffi0
(
and quasi-established flow
∂αv
∂z ffi0; ∂Vk
∂z ffi0 without strong geometrical complexity (gv ffi0;δPksing ffi0Þ and
without big interfacial mass transfer (ΓivVi term is negligible) this cross momentum
equation is simplified:
A τiv ffi−A αvαl ϱl −ϱv
½
□gz −Cvαlτwv + Clαvτwl
In such conditions, the force balance between phases is reduced to equilibrium
between drag force gravity, and wall friction forces. Considering a dispersed gas phase
and a continuous liquid as encountered in bubbly, slug and churn flow, in a vertical

<!-- page 230 (PDF 64) -->
channel at moderate velocity, wall friction terms may be significantly smaller than
interfacial friction due to a much higher interfacial area than wall friction area. Then
a rough approximation in vertical upward oriented flow leads to:
τiv ffiαvαl ϱl −ϱv
½
□g
This simple balance between buoyancy and drag forces has a clear similarity with the
drift flux models where the drift velocity models are of the following form:
Vgj = C
ffiffiffiffiffiffiffiffiffiffi
gΔρδ
ρl
s
where δ is a length scale characteristic of the bubble size. This expression can be
obtained from a balance between buoyancy B and drag force D applied to a bubble
of size:
B ≡ gΔρδ3;D ≡ Cdρlδ2V2
gj
If the drag coefficient is assumed constant and if δ is proportional to the Laplace scale,
one obtains the form of Zuber and Findlay (1965), model for churn-turbulent bubbly
flow:
Vgj ≡ gΔρσ
ρ2
l
)0:25
If the drag coefficient is assumed constant and if δ is bounded by the duct diameter,
one obtains the form of Zuber and Findlay model for slug flow:
Vgj ≡
ffiffiffiffiffiffiffiffiffiffiffiffi
gΔρD
ρl
s
From the drift flux equation, Vgj general expression, and simplified cross-momentum
equation, one can obtain an expression of the interfacial friction which is consistent
with a drift flux model:
τiv = αvαlϱl
V2
gj
C2δ = αvαlϱl 1−Coαv
ð
Þ2 Vv −CαVl
ð
Þ2
C2δ
Cα = Co 1−αv
ð
Þ
1−Coαv
ð
Þ
This simply shows that a drift flux approach can be equivalent to a full two-fluid
6-equation model when the approximations made in the simplified cross-momentum
