# The space-time-averaged 1-D equations for single-phase flows
<!-- source PDF pages 22-29 -->

<!-- page 188 (PDF 22) -->
A possible set of time-averaged equations for a single-component single-phase flow
equations of Newton-Stokes fluid can be summarized as follows if we use the total
enthalpy equation and if we use the mass-weighted velocity and enthalpy. Note that
the principal variables are here ⟨p, eh, and evj:
Time-averaged equations: 1-Component 1-phase flow equations for
a Newton-Stokes fluid
Principal variables: ⟨p, ev
⃗ , eh
∂ρ
∂t + rρ ev
⃗ = 0
∂ ρev
⃗
∂t
+ ∇ρev
⃗ ev
⃗ + ∇⟨p = + ρ g
⃗ + ∇ · ⟨T + T t
∂
∂t ρ
eh + ev2
(
−⟨p
+ ∇ · ρ ev
⃗
eh + ev2
(
= F
⃗
· ρ ev
⃗
+ ∇ ·
⟨T + T t
· ev
⃗
+ ∇ ·
q
⃗ + q
⃗t
□
□
+ qext
⟨T = −2
3μ∇ · ev
⃗ I + μ
∇ ev
⃗ + t∇ ev
⃗
(
; q
⃗ = −λ ∇⟨T
ρ = ρ ⟨p, eh
□
□
; ⟨T = T ⟨p, eh
□
□
;μ = μ ⟨p, eh
□
□
;λ = λ ⟨p, eh
□
□
+ expressions or equations for T t and q
⃗t
One can notice that time averaging only adds T t and q
⃗t in momentum and energy
equations.
5.5
The space-time-averaged 1-D equations for
single-phase flows
1-D equations are commonly used to describe flows and heat transfers in circuits.
It can result from space averaging over the cross section of the duct and produces
a set of three partial derivative equations function of time and curvilinear abscissa.
It is applicable to ducts with continuous cross-sectional area and is not adapted to
abrupt area changes. Another approach is the use of successive “control volumes”
where equations are integrated over a volume between two sections of the duct. This
produces interconnected zero-D differential equations function of time only rather
than real 1-D equations. This allows abrupt area changes and may be equivalent to
1-D equations when the distance between the sections tends to zero.

<!-- page 189 (PDF 23) -->
## 5.5.1 The 1-D equations for single-phase flow

The derivation of space-time-averaged equations in 1-D is a very common
approach for flows in pipes and ducts. As shown by Delhaye et al. (1981) one can
proceed in two ways: first space averaging then time averaging or time averaging
then space averaging. In the case of single-phase flow, the second approach is
summarized here.
One will use here the set of time-averaged equations given in Section 5.4 where ⟨p,
eh, and evj are the principal variables, which can also be written (with summation on
repeated indices):
∂ρ
∂t + ∂ρ evJ
∂xj
= 0
∂ ρ evJ
∂t
+ ∂ρevι evj
∂xi
+ ∂⟨p
∂xj
= −ρgj + ∂
∂xj
τιJ −Rij
∂ ρ
eh + ev2
(
− ⟨p
∂t
+
∂ ρ evJ
eh + ev2
(
∂xj
−ρgi evι −∂
τιJ −Rij
evι
□
□
∂xj
+
∂ qJ
⃗ + q⃗t
j
□
□
∂xj
= qext
Now one must average these equations on the cross section of a duct using the
following notation
< f>S = 1
A
ð
A
f ds
Fig. 5.2 shows a portion of a duct with the following notations:
z is the curvilinear abscissa of the duct
A(z) is the cross-sectional area
C is the contour of A
n
⃗ is the vector normal to the duct wall directed to the exterior of the duct
nc
⃗ is the vector normal to the contour C directed to the exterior of the duct
gz
⃗ is the gravity acceleration vector projected along z axis
One will use a particular form of the Leibniz rule
d
dt
ð
A
f x, y, z, t
ð
Þda =
ð
A
∂f
∂t da +
ð
C
f v⃗ · n
⃗
dC
n
⃗ : nC
⃗
Since there is no flow through the wall v
⃗ · n
⃗= 0 and:
< ∂f
∂t >S = ∂ < f>S
∂t

<!-- page 190 (PDF 24) -->
Notation: ^f =< ⟨f>S
One will use a particular form of the Gauss theorem applied to a vector B
⃗ or a
tensor T
ð
A
∇ · B
⃗ da = ∂
∂z
ð
A
Bzda +
ð
C
n
⃗ · B
⃗
dC
n
⃗ · nC
⃗
B
⃗=nz
⃗) ∂A
∂z = −
ð
C
n
⃗ · nz
⃗
dC
n
⃗ · nC
⃗
ð
A
∇ · T da = ∂
∂z
ð
A
nz
⃗ · T da +
ð
C
n
⃗ · T
dC
n
⃗ · nC
⃗

### 5.5.1.1 Mass balance equation

∂ρ
∂t + ∇ · ρ ev⃗
□
□
□
□S
= ∂ ρ
h iS
∂t
+ ∇ ρ ev⃗
□
□
D
ES
= ∂ ρ
h iS
∂t
+ 1
A
∂
∂z
ð
A
ρ evzda
= ∂ ρ
h iS
∂t
+ 1
A
∂A ρ evz
h
iS
∂z
= 0
One may define a space-time-averaged velocity
V≜ρ evz
h
iS
ρ
h iS = ρ evz
h
iS
bρ
A∂bρ
∂t + ∂AbρV
∂z
= 0
nc
n
nz
gz
g
z
C
A(z)
Fig. 5.2 Portion of a duct.

<!-- page 191 (PDF 25) -->
### 5.5.1.2 Energy equation

∂ρ
eh + ev2
(
− ⟨p
∂t
+
∂ρ evJ
eh + ev2
(
∂xj
−ρgi evι −∂ τιJ + Rij
evι
∂xj
+
∂ qJ
⃗+ q
⃗t
j
∂xj
= qext
h
∂ρ
eh + ev2
(
− ⟨p
∂t
i
=
∂ ρ eh
D
ES
∂t
+
∂
ρ ev2
□
□S
∂t
−∂ ⟨p
h iS
∂t
Let us define the mass-weighted space-time average enthalpy H and the space-time
average pressure P
H≜
ρ eh
D
ES
ρ
h iS ;
P≜⟨p
h iS = bp
An approximation is necessary for the second term
ρ ev2
□
□
ffiρ
h iS V2
h
∂ρ
eh + ev2
(
− ⟨p
∂t
i
= ∂bρH
∂t +
∂bρV2
∂t
−∂P
∂t
h
∂ρ evJ
eh + ev2
(
∂xj
i
s
= 1
A
∂A ρ evz
eh + ev2
(
□
□S
∂z
= 1
A
∂A ρ evz eh
D
ES
∂z
+ 1
A
∂A ρevz
ev2
□
□S
∂z
Again the averaging of the advection term induces an additional term qz
d:
qd
z ≜ρ evz eh
D
Es
−bρVH
qz
d is called a “dispersion” term and has an axial diffusive effect on H
An approximation is necessary for the second term
ρ evz
ev2
□
□s
ffiρ
h iSVV2

<!-- page 192 (PDF 26) -->
h
∂ρ evJ
eh + ev2
(
∂xj
i
S
= 1
A
∂
∂Z
ð
A
ρ evZ
eh + ev2
(
da = 1
A
∂A ρ evZ
ehev2
(
□
□S
∂z
= 1
A
∂AbρVH
∂z
−∂Aqd
Z
∂z
+
∂AbρVV2
∂z
ρgi evι
h
iS ffibρgzV
∂ τιJ −Rij
evi
∂xj
□
□S
= 1
A
∂
∂z A <
⟨T + T t
· ev
⃗
□
□
nz
⃗>S
h
i
∂qj
⃗+ q⃗t
j
∂xj
*
+S
= 1
A
∂
∂zA ⟨qz + qt
z
□
□S + 1
A
ð
C
n⃗ ·
q⃗ + q⃗t
j
□
□
dC
n⃗ · nC
⃗ = 1
A
∂A bqz + qt
z
□SÞ
∂z
+ 1
ACqw
Cqw is the wall heat transfer term
A ∂
∂t bρ H + V2
(
−P
+ ∂
∂z Abρ V H + V2
(
−Abρgz V =
∂
∂z A <
⟨T + T t
· ev
⃗
□
□
nz
⃗>S −∂Aqeff
z
∂z
+ Cqw + Abρext
qeff
z ≜bρZ + qt
z
□
□S + qd
z = − λ + λt + λd
ð
Þ∂T
∂z
qz
eff is the effective axial diffusion-dispersion term
The axial contribution of the stress tensor ⟨T + T t is usually neglected so that the
equation writes:
A ∂
∂t bρ H + V2
(
−P
+ ∂
∂z AbρV H + V2
(
−Abρgz V = Cqw + Abρext −∂Aqeff
z
∂z
The effective axial diffusion-dispersion term may be neglected when heat sources at
the wall have a much higher impact than axial diffusion.

### 5.5.1.3 Momentum equation

One can apply the particular form of the Leibniz rule and Gauss theorem to the vectorial
equation and then project along z axis or apply the particular form of the Leibniz
rule and Gauss theorem to the equation projected along z axis.

<!-- page 193 (PDF 27) -->
ð
A
∂bρevz
∂t ds = A ∂bρevz
∂t
□
□S
= A∂ bρevz
h
iS
∂t
= A∂bρV
∂t
A r · bρevz ev
⃗
□
□
D
ES
= ∂A bρevzevz
h
iS
∂z
One must define a momentum axial dispersion term Tz
d
Td
z ≜ρevzevz
h
iS −bρVV
A r · ρevz ev
⃗
□
□
D
ES
= ∂A ρevzevz
h
iS
∂z
= ∂AbρVV
∂z
+ ∂ATd
z
∂z
The contribution of pressure term is split into an axial gradient and a contribution Fp
along the duct wall contour C:
A ∂ρ
∂z
□
□S
= A rρ:n
⃗
z
D
ES
= ∂A < ρ>S
∂z
+ A
ð
C
ρ n
⃗ : nz
⃗ dC
n
⃗
c· n
⃗ = ∂AP
∂z + Fp
with:
Fp =
ð
C
ρ n
⃗ · nz
⃗ dC
n
⃗
c· n
⃗
The local time-averaged pressure at wall is split into the space-time-averaged pressure
P and a local-time-averaged pressure difference δ⟨p
ρ = ρ
h iS + δρ = P + δρ
Fp = −PdA
dz +
ð
C
δρ n
⃗ · nz
⃗ dC
n
⃗
c · n
⃗ = −PdA
dz + F0p
with
F0p =
ð
C
δρ n
⃗ · nz
⃗ dC
n
⃗
c · n
⃗
then:
A ∂ρ
∂z
□
□S
= A∂P
∂z + F0p
No difficulty with the external force (gravity) term:
ρgz
h
is =bρgz

<!-- page 194 (PDF 28) -->
Two contributions of the deviator stress tensor:
A r · ⟨T + T t
· n⃗
z
D
ES
= − ∂
∂zA <nz
⃗ · ⟨T + T t
· nz
⃗Þ > +
ð
C
n⃗ · ⟨T + T t
· nz
⃗Þ
dC
n⃗
c · n⃗
The first right-hand side (RHS) term is usually small and neglected. The second RHS
term is the wall friction term.
−Cτw≜
ð
C
n
⃗ · ⟨T + T t
· nz
⃗Þ dC
n
⃗
c· n
⃗
Finally:
A∂bρV
∂t + ∂AbρVV
∂z
+ A∂P
∂z =bρgz −Cτw −F0p−∂ATd
z
∂z
F0p is nonzero when the duct shape or cross section is not constant (n
⃗ · nz
⃗6= 0Þ.
It takes geometrical effects on pressure forces into account and is usually modeled
as a singular pressure loss:
−F0p = A ∂P
∂z
(
sing
= −AKsing
δz ρV2
It can play an important role in singular geometry such as convergent, divergent, bend,
and any other complex geometry which can influence the flow. The form-loss
coefficient Ksing depends on the geometry and may be a function of the Reynolds
number Re = ρVDh
μ
, Dh being the hydraulic diameter Dh = 4A
C
−F0p = + pp − p
h i
□dA
dz
As for the last dispersion term: ∂ATd
z
∂z =
∂A
ρ evzevz
h
iS −bρVV
□
□
∂z
it is zero in established flow (transverse profiles of evz does not depend on z) in a constant
cross-section duct (A = Ct). In nonestablished flow in a constant cross-section duct,
it is most often neglected. In variable cross section or in the presence of complex geometry
, its effect may be modeled together with F0p as a geometrical effect.
These equations must be complemented by equations of state which are necessarily
approximated due to averaging of nonlinear functions such as:
bρ = ρ p, h
ð
Þ
D
ES
ffiρ P, H
ð
Þ = ρ
⟨p
h iS,
ρ eh
D
ES
ρ
h iS
B
@
C
A

<!-- page 195 (PDF 29) -->
These equations must be complemented by closure laws for τw, Ksing, qw, and qz
eff
Usual expressions for τw and Ksing are of the following form:
τw = Cf Re
ð
ÞρV2
2 ; Cf = aRe−b; Ksing = cRe−d
Usual expressions for qw and qz
eff are:
qw = h Tw −T
ð
Þ = λNu Re, Pr
ð
Þ
Dh
Tw −T
ð
Þ; Nu = C Rep Prq
qeff
z = −λeff ∂ ⟨T
∂z
The resulting set of 1-D equation is then:
1-D 1-Phase equations: 1-Component 1-phase flow space-time-averaged
equations
Principal variables: P, V, H
A∂bρ
∂t + ∂AbρV
∂z
= 0
A∂bρV
∂t + ∂AbρVV
∂z
+ A∂P
∂z =bρgz −Cτw −AKsing
δz ρV2
A ∂
∂t bρ H + V2
(
−P
+ ∂
∂z Abρ V
H + V2
(
−Abρgz V = Cqw + Ad
qext −∂Aqeff
z
∂z
τw = Cf Re
ð
ÞρV2
2 ; Ksing = Ksing Re
ð
Þ ; Re =bρVDh
μ
qw = h Tw −T
ð
Þ = λNu Re, Pr
ð
Þ
Dh
Tw −T
ð
Þ; qeff
z = −λeff ∂T
∂z ; Pr = μCp
λ
P = ⟨p
h iS; H =
ρeh
D
ES
ρ
h iS ; bρ = ρ P, H
ð
Þ; μ = μ P, H
ð
Þ; λ = λ P, H
ð
Þ;
T = T P, H
ð
Þ
+ expressions for Cf, Ksing, Nu and λeff

## 5.5.2 Predictive capabilities of the 1-D set of equations

One may note that usual expressions for wall friction and wall heat transfers use the
“principle of locality” of the modeling where the physics of the process to model
depends only on local flow variables (i.e., velocity, pressure, enthalpy) and their time
and space local derivatives. It assumes that the knowledge of the local instantaneous
