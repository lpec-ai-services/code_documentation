# The space averaged 1-D equations for two-phase flow
<!-- source PDF pages 42-54 -->

<!-- page 208 (PDF 42) -->
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
+ εkr⟨p
= εkρk
k g
⃗ −Mik + γik
f
vk
⃗
k
+ r · εk T k + T t
k
□
□
∂
∂t
εkρk
k
hkek +
f
vk
⃗
k2
B
B
@
C
C
A
775 + r ·
εkρk
kf
vk
⃗
k
hkek +
f
vk
⃗
k2
B
B
@
C
C
A
775−εk
∂ρ
∂t
= εkρk
k g
⃗ · f
vk
⃗
k
+ r · εk q
⃗
k + q
⃗t
k
□
□
h
i
+ qik + γik
hkek +
f
vk
⃗
k2
B
B
@
C
C
A + qrk
X
k
εk = 1;
X
k
γik = 0;
X
k
Mik = 0;
X
k
qik + γik
hkek +
f
vk
⃗
k2
B
@
C
A
75 = 0;
Mik = MD
ik + ML
ik + MAM
ik + MTD
ik
T k = −2
3μkr· f
vk
⃗
k
I + μk
rf
vk
⃗
k
+ trf
vk
⃗
k
!
; q
⃗
k = −λk rTk
ρk
k = ρk ⟨p, hkek
□
□
; ⟨Tk = Tk ⟨p, hkek
□
□
; μk = μk ⟨p, hkek
□
□
; λk = λk ⟨p, hkek
□
□
+ expressions or equations for T k
t, q
⃗t
k, Mik
D, Mik
L, Mik
AM, Mik
TD

## 5.7.1 Predictive capabilities of the time-averaged two-fluid model

A lot of information is lost when averaging a two-phase flow due to the complex and
moving geometry of interfaces. The main source of difficulty is associated to the contributions
of pressure and viscous forces on the interfaces which required the main
modeling efforts. Another difficulty comes from turbulence in two-phase flow which
by far not so well understood as in single phase. Modeling efforts so far provided reasonable
predictions of dispersed flow for bubbles and droplets, but the accuracy
remains significantly degraded compared to single-phase turbulent flow.
Time average two-fluid model were also used with some success to separate-phase
flow with large interfaces (Lucas et al., 2011). A specific effort was spent to the identification
of large interfaces using IRT or ITM and to mass momentum and energy
transfers at the large interfaces.
5.8
The space averaged 1-D equations for two-phase flow
The 1-D two-fluid 6-equation model of two-phase flow is the most currently used for
describing two-phase flow with heat transfers in circuits. It results from space-time
phase averaging (Delhaye et al., 1981; Ishii and Hibiki, 2011; Morel, 2015). Phase

<!-- page 209 (PDF 43) -->
averaging means that a multiplication of local instantaneous equations by a phase indication
function is made before a time or a space averaging.
One can obtain the 1-D two-fluid 6-equation model of two-phase flow in two ways:
l
multiplying local instantaneous equations by χ k, then time averaging, then space averaging
l
multiplying local instantaneous equations by χ k, then space averaging, then time averaging
It is chosen here to show some steps of the second method since it allows identifying
and justifying some of the most important simplifications and approximations which
are necessary.

## 5.8.1 The space-phase averaging

Let us define some useful quantities and operators (see also Fig. 5.5).
Space averaging:
fh iS≜1
A
ð
A
f ds
Time averaging:
⟨f≜1
T
ð
T
f dt
Time fraction of phase k:
εk≜χk = 1
T
ð
T
χk dt = Tk
T
Space fraction of phase k:
Rk≜χk
h
iS = 1
A
ð
A
χk ds
Phase space (surface) averaging:
bfk
k≜
ð
A
χkfkds
ARk
Phase mass-weighted area averaging
⟩
f k
k≜χkρkfk
h
iS
χkρk
h
iS
Al
Av
•
Fig. 5.5 Definition of space fractions for phase k.

<!-- page 210 (PDF 44) -->
One can notice:
Rk bfk
k = χkfk
h
iS
Phase time averaging:
⟨f
k≜
ð
T
χkfkdt
ð
T
χkdt
One can notice:
εk ⟨f k = χkfk
Considering commutativity of space and time integration:
ð
A
ð
T
χkfkdtds =
ð
T
ð
A
χkfkdsdt
Rk bfk
k
= εk ⟨f k
k
D
E
A space time average phase fraction αk is defined, i.e., according to Fig. 5.6:
Ci
A2
A1
C1
C2
nc
n
A
nkc
nk
Ai
nz
Fig. 5.6 Portion of a duct with a two-phase flow.

<!-- page 211 (PDF 45) -->
αk≜Rk = εk
h
i
A is the cross section of the duct
Ck is the contour of A occupied by phase k
Ai is the interfacial surface
Ci is the contour of phase k in A (intersection of A and Ai)
n
⃗ is the vector normal to the duct wall directed to the exterior of the duct
nc
⃗ is the vector normal to the contour C directed to the exterior of the duct
−⃗
nkc is the vector normal to the contour Ci directed to the exterior of phase k
nk
⃗ is the vector normal to the interface Ai directed to the exterior of phase k
nz
⃗ is the unit vector along the duct axis

## 5.8.2 The space-phase averaged equations

### 5.8.2.1 Mass balance of phase k

∂ARk ρk
h
iS
k
∂t
+
∂ARk ρk
−⃗
vkz
D
ES
k
∂Z
= −
ð
Ci
ρk vk
⃗− vι
⃗
□
□
· nk
⃗
dCi
nk
⃗ · −⃗
nkC
≜AΓik
The interface has no volume and no mass so that: Γiv = −Γil

### 5.8.2.2 Momentum balance of phase k

Time derivative term
ð
Ak
∂ρvz
∂t
(
dA = ∂ARk ρkvkz
h
iS
k
∂t
= A∂Rkc
ρk kV
^
k
k
∂t
Advection term
ð
Ak
∂y
∂zρvz vz
(
dA = ∂ARk ρkvkzvkz
h
iS
k
∂z
+ Mvik
Mvik =
ð
Ci
ρkvkz vk
⃗− vi⃗
□
□
· nk
⃗
dCi
nk
⃗·−⃗
nkC
Mvik is the volumetric axial momentum transfer through interface. Considering that
both phases have the same axial velocity Vi at the interface: Mvik=A ΓikVi
Vi must be modeled as function of Rk,Vl,
^ Vg
^ depending on the flow regime
One must define a phase momentum axial dispersion term Tkz
d
Td
kz≜ρkvkzvkz
h
iS
k −c
ρk kVk
^ k
Vk
^ k

<!-- page 212 (PDF 46) -->
ð
Ak
∂y
∂zρvz vz
(
dA = ∂ARkc
ρk kVk
^ k
Vk
^ k
∂z
+ ∂ARkTd
kz
∂z
+ Mvik
Stress tensor term (deviator part)
ð
Ak
−r · T · n
⃗
z dA = −
∂ARk n
⃗
z · T ; · n
⃗
z
D
ES
k
∂z
−Ffrik −Ffrwk
The first RHS term is usually small and neglected.
Ffrik is the axial component of the friction of phase k along interface
Ffrwk is the axial component of friction term of phase k along wall
Ffrik≜
ð
Ci
n
⃗
z · T k · n
⃗
k
dCi
n
⃗
kc · n
⃗
k
Ffrk≜
ð
Ck
nz
⃗ · T k · nk
⃗ dCk
n
⃗
c· n
⃗
External force (gravity) term
ð
Ak
ρgz dA = ARkc
ρk kgz
Pressure term
ð
Ak
∂p
∂z dA =
ð
Ak
rp · n
⃗
z dA = ∂ARkpk⟩k
∂z
−Fpwk −Fpik
Fpwk ≜
ð
Ck
nk
⃗· p nz
⃗ dC
n
⃗
c· n
⃗
Fpik ≜
ð
Ci
n
⃗
kp· nz
⃗
dC
n
⃗
kc · n
⃗
k
Fpwk is the axial contribution of pressure force on the part of duct wall occupied by phase k
Fpik is the axial contribution of pressure force along the interface
Let us define an average mixture pressure P and a local pressure difference p 0 k in
phase k
P≜Rvpv
cv + Rl bpll
p0
k≜pk −P

<!-- page 213 (PDF 47) -->
Fpwk + Fpik = −P∂Ak
∂z + F0
pwk + F0
pik = −P∂ARk
∂z
+ F0
pwk + F0
pik
F0
pwk =
ð
Ck
n
⃗
k ·p0
k nz
⃗ dC
n
⃗
cn
⃗
k
; F0
pik =
ð
Ci
n
⃗
kp0
k · nz
⃗
dC
n
⃗
kc · n
⃗
k
Note that:
pvc v = P−Rl bpll −pv
c v
≜P−δpv
bpll = P−Rv pvc v − bpll
≜P−δpl
Then: δpvl = Rvδpv = −Rlδpl
∂ARvpv
c v
∂z
= ∂ARvP
∂z
−∂ARvδpv
∂z
= ∂ARvP
∂z
−∂Aδpvl
∂z
∂ARl bpll
∂z
= ∂ARlP
∂z
−∂ARlδpl
∂z
= ∂ARlP
∂z
+ ∂Aδpvl
∂z
In the frame of a one-pressure model, one can eliminate phase pressures pk⟩k from the
momentum equation to keep only the mixture pressure P:
ð
Ak
∂p
∂z dA = ∂ARkc
pk k
∂z
−Fpwk −Fpik = ∂ARkc
pk k
∂z
−P∂ARk
∂z
+ F0
pwk + F0
pik
= ∂ARkP
∂z
−P∂ARk
∂z
+ F0
pwk + F0
pik −∂ARkδpk
∂z
= ARk
∂P
∂z + F0
pwk + F0
pik −∂ARkδpk
∂z
Let us define Fiv* and Fil*:
Fiv*≜F0
piv + Ffriv + ∂Aδpvl
∂z
Fil*≜F0
pil + Ffril −∂Aδpvl
∂z
One must model the three components of Fiv* and Fil* which depend on the phase
repartition in each flow regime.
A∂Rkc
ρk kVk
^ k
∂t
+ ∂ARkc
ρk kVk
^ k
Vk
^ k
∂z
+ ARk
∂P
∂z
= A Rkc
ρk kgz + F0pwk + Ffrwk + F0pik + Ffrik + AΓikVi □∂Aδpvl
∂z
+ ∂ARkTd
kz
∂z

<!-- page 214 (PDF 48) -->
The law of action and reaction writes:
X
k F0
pik + Ffrik + Mvik
□
□
= 0
It is extremely difficult to model F0pwk,Ffrwk,F0pik,Ffrik,δpvl, and Tkz
d due to the complexity
and diversity of the interface shape. In particular, pressure force integration on
complex and moving boundaries is a real challenge.
Simplifications and approximations are necessary.
One common simplification is used in dispersed flow (bubbly flow and droplet
flow) which considers that δpvl = 0 so that pvc v = bpll = P
However it may be found that the average pressure at the interface is usually lower
than the average mixture pressure. From F 0 pik one may identify a part which is
corresponding to an average interface pressure and a part which is due to differences
or interface pressure along the interface.
Considering the interface pressure shown in Fig. 5.7, it is higher than the average
pressure at the stagnation point at the leading edge, then it decreases due to curvature
of the streamlines, and it never recovers the stagnation pressure at trailing edge due to
flow detachment in the wake. The average interface pressure is lower than the average
pressure. The part of F 0 pik due to the average interface pressure may be modeled as a
term of the form: Afi
∂Rk
∂z with fi ≡ ρ Vg −Vl
□2 (see Stuhmiller, 1977).
Fig. 5.7 Interface pressure along a spherical particle.

<!-- page 215 (PDF 49) -->
The other part of F 0 pik corresponds to the difference between the local and the average
interface pressure and is responsible for a part of the drag on the particle (higher
pressure on leading edge than on the trailing edge). It is then combined to a part of Ffrik
in the drag force Aτik which couples the velocities of the phases.
In accelerating flow, another part of F 0 pik and Ffrik is known as the added mass
force which couples the acceleration of the phases.
A possible expression is:
A FAM
v
= A βRk 1−Rk
ð
Þρm
∂V
^v
v
∂t + V
^v
v
∂V
^v
v
∂z −∂V
^l
l
∂t + V
^l
l
∂V
^l
l
∂z
5; FAM
l
= −FAM
v
ρm is a mixture density and β is an added mass coefficient
In the same way, in a duct of varying cross section, one may model F 0pwk as a term
of the form gk
∂A
∂z
It may also be integrated into a singular pressure loss term as in single-phase flow:
−ARk
δpsing,k
δz
= A Rk
Ksing,k
δz
ρk
Vk
^ 2
Ffrwk is usually modeled as a wall friction term
Ffrwk = −Ckτwk
The momentum equation can then be written:
A∂Rkc
ρk kVk
^ k
∂t
+ ∂ARkc
ρk kVk
^ k
Vk
^ k
∂z
+ ARk
∂P
∂z + Afi
∂Rk
∂z + gk
∂A
∂z
= ARkc
ρk kgz −∂ARkTd
kz
∂z
−Aτik −Ckτwk −A Rk
δpsing,k
δz
+ A FAM
k
+ AΓikVi
The terms gk
∂A
∂z and ∂ARkTd
kz
∂z
being influenced by geometrical effects may be modeled
together with the singular pressure loss δpsing,k depending on the flow regime

### 5.8.2.3 Energy balance of phase k

Time derivative term
Let us define the mass-weighted phase space average enthalpy: Hk
^ k
= ρkhk
h
iS
k
c
ρk k

<!-- page 216 (PDF 50) -->
ð
Ak
∂ρ h + v2
(
∂t
dA =
∂Ak < ρk hk + vk2
(
>k
∂t
=
∂A Rkc
ρk k
Hk
^ k
+ Vk
^ k2
@
A
∂t
An approximation was necessary for the kinetic energy term:
< ρk
vk2
2 >k ffic
ρk k Vk
^ k2
Advection term
ð
Ak
r·ρ v⃗
h + v2
(
dA = ∂ARk ρkvkzhk
h
iS
k
∂z
+
∂ARk
ρkvkz
vk2
□
□S
k
∂z
+ MHik + ECik
ffi
∂A Rkc
ρk kVk
^ k
Hk
^ k
+ Vk
^ k2
@
A
∂z
+ ∂ARkqd
kz
∂z
+ MHik + ECik
MHik and ECik are the volumetric energy transfer through interface
MHik = −
ð
Ci
ρk vk
⃗−vi
⃗
□
□
hk ·nk
⃗
dCi
nk
⃗·−⃗
nkC
ECik = −
ð
Ci
ρk vk
⃗−vi
⃗
□
□vk2
2 ·nk
⃗
dCi
nk
⃗·−⃗
nkC
MHik and ECik are usually modeled as:
MHik = AΓikHk
^ k
ECik = Γik
Vi2
Again the averaging of the advection term induced an additional dispersion term qkz
d:
qd
kz≜ρkvkzhk
h
iS
k −c
ρk kVk
^ k
Hk
^ k

<!-- page 217 (PDF 51) -->
qkz
d can be modeled as:
qd
kz = λd
kz
∂Tk
^ k
∂z
Pressure term:
ð
Ak
∂p
∂t dA = A∂Rk pk
h
iS
k
∂z
= A∂Rkc
ρk k
∂t
Contribution of the deviator stress tensor
ð
Ak
r· T · v⃗ dA = ∂
∂zAkvk
⃗·
T k ·nz
⃗
□
□S
k + EFik + EPik
This first term is often neglected.
The second term EFik is a work of interfacial friction and can be modeled as:
EFik = τik Vi
The third term EPik is a work of interfacial pressure and can modeled as:
EPik = EP0
ik −P∂Rk
∂t ffi−P∂Rk
∂t
Gravity term
ð
Ak
ρg
⃗
z · v⃗ dA = Ak ρkgzukz
h
iS
k = ARkc
ρk kVk
^ k
gz
Heat flux term:
−
ð
Ak
r · q
⃗ dA = − ∂
∂zAk qk
⃗ · nz
⃗
□
□S
k −
ð
Ci
n
⃗
kqk
dC
n
⃗
kc · n
⃗
k
−
ð
Ck
n
⃗ · q
⃗
k
dC
n
⃗ · nC
⃗
= −∂ARkqkz
∂z
+ Ckqwk + Aqik
with:
Ckqwk≜−
ð
Ck
nk
⃗ · q
⃗
k
dC
nk
⃗ · −⃗
nCk
;Aqik ≜−
ð
Ci
n
⃗
kqk
dC
n
⃗
kc · n
⃗
k
X
k
qik + ΓikHk
^ k
= 0

<!-- page 218 (PDF 52) -->
A
∂ Rkc
ρk k
H
^
k
k
+ V
^
k
k2
@
A
∂t
+
∂ARkc
ρk kV
^
k
H
^
k
k
+ V
^
k
k2
@
A
∂z
−ARk
∂P
∂t + ∂A Rk qkz + qd
kz
∂z
= + ARkc
ρk kVk
^ k
gz
+ Ckqwk + Aqik + AΓik Hk
^ k
+ Vi2
(
+ AτikVi + A d
qkext
Considering orders of magnitudes, it is found that the diffusion-dispersion term and
the term τikVi are often small compared to others and are neglected.

## 5.8.3 The space-phase averaged equations for stratified flow

The case of a stratified flow in a horizontal or inclined duct is particular since the interface
has a simple shape, and the pressure field in a cross section may be reasonably
approximated. Therefore, the integration of pressure forces is easier than in more complex
flow regimes.
Having in mind that the main difficulty in horizontal legs is to correctly predict the
stratification occurrence and the characteristics of stratified flow, attention was paid in
the CATHARE code development to derive the best possible system of equations.
The CATHARE code two-fluid 6-equation model able to describe stratified flows
was derived by de Crecy (1986), who also analyzed its properties, Fig. 5.8. Assuming:
l
A hydrostatic transverse pressure gradient
l
Vapor and liquid densities uniform over the cross section
l
Continuity of pressure across the interface (no surface tension effect and no pressure jump
induced by mass transfer)
Vapor
Liquid
Av
AL
nL
nLS
gz
z
GV
SV
SL
X
X
Sl
GL
g
g cos q
q
Fig. 5.8 Stratified flow.

<!-- page 219 (PDF 53) -->
In such conditions pressure terms can be calculated and momentum equations are written
as:
A∂Rkc
ρk kV
^k
k
∂t
+ ∂ARkc
ρk kV
^k
kV
^k
k
∂z
+ ARk
∂P
∂z + Afi
∂Rk
∂z Δk∂A
∂z + AεkGz −Dk
= ARkc
ρk kgz −Aτik −Ckτwk + AΓικVi
with:
gz = −gsinθ
Δk = −ρkgsinθ Xk −Xi
ð
Þ
Δk is the pressure difference between the average pressure pk in phase k and pressure
at the interface pi
fi = RgΔl − 1−Rg
Δv + Rg 1−Rg
□∂ Δv −Δl
ð
Þ
∂α
Gz = Rg 1−Rg
□∂ Δv −Δl
ð
Þ
∂z
Dk =
ð
Sk
nz
⃗ · nk
⃗ pk x, y, z
ð
Þ−pi
½
□
ds
nk
⃗ · nks
⃗
Ev = 1; El = −1
For each phase k, Dk takes into account the pressure difference due to gravity between
the interface and the wall perimeter in contact with phase k.
Dk and Δk are terms dependent on the pipe shape. In the particular case of a square
duct, the following expressions are found:
Gz = A
3□
2εkα 1−α
ð
Þρm
∂gcosθ
∂z
fi = Rg 1−Rg
ρL −ρV
ð
ÞgcosθA
1□
Δk = 1−αk
fi
ρm = RgρV + 1−Rg
ρL

<!-- page 220 (PDF 54) -->
The momentum equation is:
A∂Rkc
ρk kVk
^ k
∂t
+ ∂ARkc
ρk kVk
^ k
Vk
^ k
∂z
+ ARk
∂P
∂z
+ Δk
∂A
∂z + AEkGz −Dk = ARkc
ρk kgz −Aτik −Ckτwk + AΓikVi
−Afi
∂Rk
∂z + 1−Rk
fi
∂A
∂z + A
3□
2εkRk 1−Rk
ð
Þρm
∂gcosθ
∂z
The expression for fi in a circular pipe should include a shape function of void fraction
which is often forgotten and replaced with 1.
In the CATHARE code 1-D module (de Crecy, 1986; Bestion and Serre, 2012), fi is
written:
fi = Rg 1−Rg
ρL −ρV
ð
ÞgcosθD
The fi
∂Rk
∂z term controls the characteristic velocity corresponding to void fraction
waves which are shallow water waves at the free surface of the stratified flow (see
Bestion and Serre, 2012).
The properties of the momentum equations in stratified flow are illustrated in
Fig. 5.9 where water is injected very slowly at the entrance of a pipe with area restriction
and enlargement followed by a bend. Gas velocity is zero at the entrance and pressure
is imposed at the outlet. It is shown that the water level plotted from the predicted
void fraction respect a horizontal free surface even in varying diameter zones and in
the bend. This is the result of the last three terms of the momentum equations.
Fig. 5.9 Liquid level at rest in a pipe with varying diameter and inclination.
