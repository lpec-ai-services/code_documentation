# General: — Heat conduction
<!-- source PDF pages 5-22 -->

<!-- page 361 (PDF 5) -->
development in the area and as a whole is designed for professionals as well as for
students who perform their course work and degree program. The contexts that follow
in this Part 1 focus on the heat conduction, condensation, radiation, and complex heat
transfer problems represented by heat transfer process inside a nuclear fuel rod, prior
to delving into boiling heat transfer in Part 2.

## 7.1 Heat conduction

### 7.1.1 Basic principles and definitions

#### 7.1.1.1 Temperature field and heat flux

Temperature field is described by a function T in space (x,y,z) and time τ and is
written as (Berman, 1976; Carslaw and Jaeger, 1959; Schneider, 1973):
Т = Т x, y, z, τ
ð
Þ,
or on general coordinate systems in general.
A set of points of the same temperature forms a curved isothermal surface, which
we call an isotherm. We call the amount of heat transferred per unit time through an
isothermal surface area A, heat flow Q. The heat flow per unit area is the heat flux,
q = dQ=dA W=m2
□
□
,
which is written by the Fourier’s law, in proportion to the temperature gradient
(Fig. 7.1):
q
⃗= −λgrad T = −λ · n
⃗
0 · ∂T
∂n ,
(7.1)
n
q
T1
T2<T1
T3< T2
Fig. 7.1 Temperature field and heat flux lines.

<!-- page 362 (PDF 6) -->
where λ is the thermal conductivity (W/(m K)).
The Fourier’s law assumes infinite speed of the heat propagation. In most cases
of technical importance, this assumption is accepted. In the case of a high thermal
conductivity, the heat flux is as follows:
q = −λ∂T
∂n +
λ
cρ · w2
q
∂q
∂τ ,
(7.2)
where c and ρ are the heat capacity and density of the medium; wq is the heat propagation
speed; τ is the time; λ= ρcw2
q
□
□
= τr is the relaxation time. λ= ρc
ð
Þ = a (m2/s) is
called the thermal diffusivity. If τr≪1, we arrive at Eq. (7.1).
In many text books and reference books (e.g., Todreas and Kazimi, 2012), it is a
common agreement to express heat flux with a double dot “i.e., q” in W/(m2 K). In the
context that follows, however, we use q for the heat flux since there will be no mixed
up with the expressions for the quantity per unit length or per unit volume. The heat
generation per unit length (cylinder or tube) is the linear heat rate q0 in W/m. The
density of the heat generation in power plants and nuclear reactors is often expressed
by q000 or qV in W/m3, the amount of heat generated per unit time (s) per unit of volume
(m3)—volumetric heat generation rate (see Table 7.1).

#### 7.1.1.2 Heat conduction mechanisms

Heat transfer medium is always a set of discrete particles, and heat propagation is a
reflection of the mechanisms of interaction of the particles. Ratio of the average kinetic
energy Ek of a particle to the binding energy U between particles is the major criterion to
determine the state of the substance, i.e., gas, liquid, and solid (see Fig. 7.2).
The energy transfer in gases is carried out by particle collisions and translational
motion. From the molecular kinetics theory of molecular dynamics, the thermal
conductivity is known to be written for the monatomic gas at normal temperatures
and pressures as:
Table 7.1 Typical q000 in various power units
Unit
Average power density q000 (MW/m3)
Steam boilers
RBMK
2–4
BWR, BК
30–50
PWR, VVER
80–150
SFR, BN
500–600
BOR-60
Rocket combustion chambers
20,000
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 363 (PDF 7) -->
λ = 1
3ρcvl⟨w,
where ρ is the density; cv is the specific heat at constant volume; l the mean free path of
the molecules; ⟨w =
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
3RT=M
p
the average velocity of the molecules with R the universal
gas constant and M the molecular weight. The mean free path of molecules
is in inverse-proportion to the pressure (l∝1/p), and the density in proportion to
the pressure (ρ∝p). Hence ρ · l □ const: and the gas thermal conductivity is weakly
dependent on pressure. Thermal conductivity of gas is in the range 0.005–0.4 W/
(m K). It is noted that the highest thermal conductivity of pure gases is attained by
hydrogen and helium, which are 0.15 and 0.125 W/(m K), respectively. Thermal conductivity
of air is of the order of □0.03 W/(m K). The thermal conductivity of gases
increases with increasing temperature.
In liquids, the energy is transferred in the process of elastic collisions of oscillating
particles. Exceptions are liquid metals in which the thermal conductivity close to that
of solid metals in which heat is transferred not only by vibrations from one particle to
another, but also with the free electrons (Kokorev and Farafonov, 1990). The thermal
conductivity of the water is of the order of 0.6 W/(m K) at 20°C, and liquid sodium
75 W/(m K) at 300°C.
In solids, the energy transfer mechanism is associated with vibrations of the atoms
that constitute the solid. The vibrations of atoms are independent of each other and can
be transmitted at the speed of sound from one atom to another. The solid body can be
regarded as a vessel containing a cloud of electrons and fictitious particles, i.e., phonons.
The highest thermal conductivity of metal is for silver □430 W/(m K) and copper
□400 W/(m K) (Fig. 7.3). Impurities reduce the thermal conductivity of pure metals.

#### 7.1.1.3 Heat transfer and heat exchange

The term heat transfer refers to the process of transferring heat from the heated surface
to the coolant (liquid or gas) or from the hot coolant to the cold surface (Fig. 7.4A).
In engineering practice, finding the temperature gradient
∂T=∂n
ð
Þ according
to Eq. (7.1) in its various points is very difficult and this formula is replaced by
Newton’s law:
Gas
Molecular
collision
Bounded
moleculars
(clusters)
Free electron
Free
electron
Valence
electron
Valence
electron
Lattice
vibrations
Lattice
vibrations
Free electron
(ionized gas)
Free
molecule
Ek>> U: Free motion of atoms
(molecules) and electron
Ek≅U: Atoms (molecules), electrons
and phonons are interacting each other
Ek<<U: Vibration of atoms in the
crystalline lattice structure, and energy
transfers by free electrons and phonon
vibration
Liquid
Solid
Fig. 7.2 Heat conduction mechanisms.

<!-- page 364 (PDF 8) -->
q = Q=A = α · ΔT
W=m2
□
□
, where Q = αΔT · A in W:
(7.3)
Here ΔТ = Т w −Tf is the difference between the wall surface temperature and the
average liquid temperature (bulk temperature); A is the heat transfer surface area;
and α is the heat transfer coefficient in W/(m2 K).
The term referring to heat exchange is the heat transfer from one (hot) heat transfer
medium to another (cold) through a solid wall (Fig. 7.4B). The amount of heat transferred
to the coolant from one another if they are separated by a solid wall, is from
expression:
Q = k · ΔТ · A:
(7.4)
where ΔТ = Т1 −Т2; k is the overall heat transfer coefficient (W/(m2 K)). The heat
flux is:
Thermal insulation
Methane
Water vapor
Air
10−3
10−2
10−1
Liquid
water
Solid
water
Diamond
Silver
Superconductors
λ, W/mK∞
Iron
Mercury
Hydrogen
(3500 K)
Perfect conductor
Vacuum
Fig. 7.3 Typical values of thermal conductivity from thermal insulators to superconductors.
T
T
y
y
q
q
Tw
ΔTw
Tf
ΔTa
ΔT2
ΔT1
Tf1
Tf2
Tf2
Tw1
i
R
R1
ΔU
ΔU
R2
Rc
i
(A)
(B)
Fig. 7.4 (A) Heat transfer; (B) heat exchange; and electrical analogy with Ohm’s law: ΔT=qR;
ΔT=ΔT1+ΔT2+ΔT3; ΔU=iR; ΔU=i(R1+R2+R3).
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 365 (PDF 9) -->
q = k · ΔТ:
(7.5)
Eqs. (7.3), (7.4) can be rewritten as: q = Тw −Tf
1=α
; q = T 1 −T 2
1=k
. It is an obvious analogy
with Ohm’s law in electrical engineering: I = U1 −U2
R
, where R is the electrical
resistance. By analogy, 1/a is called the thermal resistance of the heat transfer, and
value 1/k is the overall heat transfer resistance.

### 7.1.2 Basic equations of thermal conduction: Conditions of uniqueness

#### 7.1.2.1 Differential equation

The differential heat conduction equation is a mathematical expression of the law of conservation
of energy. The most common expression of the time-dependent conduction
equation for a fixed isotropic medium, which takes into account the dependence of λ,
cp,ρonthetemperatureandthedistributionofthevolumetricheatsourcesqV,isasfollows:
cpρ∂Т
∂τ = div λ · grad T
ð
Þ + qV:
(7.6)
For moving medium with the velocity components (vx, vy, vz) in the Cartesian
coordinate system, we have the total time derivative:
dT
dτ ≡∂T
∂τ + vx
∂T
∂x + vy
∂T
∂y + vz
∂T
∂z ,
which is equal to the substantial time derivative DT/Dτ. At constant material properties
of the substance, i.e., λ,cp,andρ are constant, Eq. (7.6) takes the form:
∂Т
∂τ = ar2Т + qV
ρcp
,
(7.7)
where a=λ/cp is the thermal diffusivity, the quantity which is proportional to the
propagation velocity of the isothermal surface and 1/a characterizes the inertial
properties of the body for the distribution of temperature field.
For stationary process, obviously:
r2Т + qV
λ = 0:
(7.8)
In the absence of internal heat sources (qV=0) at a steady temperature regime, the
following Laplace equation governs the temperature field:
r2Т = 0:
(7.9)

<!-- page 366 (PDF 10) -->
Thus, the shape of the steady-state temperature distribution without heat sources at
constant material properties does not depend on its properties.
The Laplace operator r2 in different coordinate systems is as follows:
–
In Cartesian coordinates (x, y, z):
r2 = ∂2
∂x2 + ∂2
∂y2 + ∂2
∂z2 ;
–
In cylindrical coordinates (r, θ, z):
r2 = 1
r
∂
∂r
r ∂
∂r
□
(
+ 1
r2
∂2
∂θ2 + ∂2
∂z2 ;
–
In spherical coordinates (r, θ, ϕ):
r2 = 1
r2
∂
∂r
r2 ∂
∂r
□
(
+
r2 sin θ
∂
∂θ
sin θ ∂
∂θ
□
(
+
r2 sin2θ
∂2
∂ϕ2 :

#### 7.1.2.2 Conditions of uniqueness

Eqs. (7.6)–(7.8) are solved only if they are provided by appropriate initial and boundary
conditions including geometry (shape, size of the body); physical characteristics
(thermal properties, heat source distribution qV (x, y, z, τ)); initial conditions
(temperature distribution); boundary conditions (processes at the borders, in general,
the conjugate conditions of temperature fields).
There are three kinds of boundary conditions given by:
I. Temperature distribution at the borders;
II. Heat flux distribution (otherwise the temperature gradient distribution); and
III. Heat exchange conditions with the environment (i.e., the ambient temperature and heat
transfer coefficient). This boundary condition can be represented as
−λ∂T
∂n = α Tw −Tf
□
□
:
(7.10)
Solutions of stationary heat conduction problems for simple geometry are straightforward
and are found in basic textbooks.

### 7.1.3 Steady-state process

#### 7.1.3.1 Bodies of simple form in one-dimension

This section displays analytical solutions obtained rather simply by integrating
one-dimensional form of Eq. (7.8) with appropriate boundary conditions and initial
conditions.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 367 (PDF 11) -->
#### 7.1.3.2 Plane wall

Given the wall thickness 2δ, internal volumetric heat source qV, the thermal
conductivity λ, and the same heat transfer coefficient α on the boundaries at □δ:
□λ dT
dx
□
(
= α Tw −Tf
□
□
,
where TW is the wall surface temperature and Tf the fluid bulk temperature, the
equation to solve is:
dT2
dx2 + qV
λ = 0,
and its solution is given by:
T x
ð Þ = Т f + qvδ
α + qvδ2
2λ
1− x
δ
□ □2
:
(7.11)
The maximum temperature is at x=0:
Tmax = Тf + qVδ
α + qVδ2
2λ
(7.12)

#### 7.1.3.3 Cylindrical wall

For an annular body of the inner diameter r1 and outer diameter r2 with constant
thermal conductivity, the equation to solve is:
r
∂
∂r
r∂T
∂r
□
(
+ qV
λ = 0
Integrating previous equation twice, we have:
Т rð Þ = −qVr2
4λ + C1 ln r + C2:
(7.13)
Constants C1 and C2 are determined from the boundary conditions. For example, if the
heat is removed through the outer surface of the cylinder by the coolant of bulk
temperature T2, the boundary conditions
At r = r1, q00 = 0 and dT
dr = 0; and
At r = r2,
−λdТ
dr
r2
= −α ТW2 −Т2
ð
Þ,

<!-- page 368 (PDF 12) -->
give the following result:
C1 = qVr2
2λ ; C2 = Т 2 + qVr2
2α + qVr2
4λ −qV
2α
r2
r2
−qVr2
2λ
ln r2:
(7.14)
As a consequence, we have:
TW2 = T r2
ð Þ = Т2 + qVr2
2α
1−
r1
r2
□
(2
"
, and
Т rð Þ = TW2 + qVr2
4λ
1−r2
r2
□
(
+ qVr2
4λ
ln
r
r2
□ (2
:
Since the linear heat rate q0 = qVπ r2
2 −r2
, the maximum temperature T(r) is at r=r1:
Tmax = Т r1
ð Þ = TW2 + q0
4πλ 1− ln r2=r1
ð
Þ2
r2=r1
ð
Þ2 −1
"
:
(7.15)
Note that the maximum temperature of solid cylinder is at the centerline given by
ðTCL
TW2
λdT = q0
4π and for the constant thermal conductivity, Tmax = Т CL = TW2 + q’
4πλ.
Eq. (7.15) suggests that, for the same linear heat rate, the highest temperature of
the annular pellet is lower than that of the solid fuel pellet by the factor
1− ln r2=r1
ð
Þ2
r2=r1
ð
Þ2 −1
.

#### 7.1.3.4 Sphere

In case of spherical geometry, assuming no angular dependency of the thermal
conditions, the differential equation is:
r2
d
drr2 dT
dr + qV
λ = 0:
(7.16)
The solution is T rð Þ = −qVr2
6λ + C1
r + C2, and from the boundary conditions at
r=0, dT/dr=0; and at r = r0, −λdT=dr = α Tw −Tf
□
□
, we have C1=0; and
C2 = Tf + qVr0
α + r0
2λ
□
(
.
Therefore,
the
maximum
temperature
is
Tf + qVr0
α + r0
2λ
□
(
= Tf + qVd
α + d
4λ
□
(
at r = 0. d is the diameter of the sphere
and the temperature difference between the surface to the sphere center is obviously
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 369 (PDF 13) -->
ΔT = T r = 0
ð
Þ−Tw = qVr2
6λ = qVd2
24λ :
(7.17)
And the heat flux at the surface is: q = qVd
6 .

#### 7.1.3.5 Critical diameter of thermal isolation

The heat flow through the pipe wall with thermal insulation can be written as
ql = klπ Tf1 −Tf2
□
□
(W/m),where Tf1 and Tf2 are temperaturesof the coolant onboth side
of the tube wall. With the subscripts i, 1, and 2 referring to the insulation, inner, and outer
boundaries of the cylinder, respectively, di, d1, and d2 are the diameters and α1 and α2 the
heattransfercoefficients.Then,withdi−d2thethicknessoftheinsulatorwrappedaround
the cylinder, the overall linear heat transfer coefficient kl can be calculated as follows:
kl
=
α1d1
+ 1
2λ ln d2
d1
+ 1
2λi
ln di
d2
+
α2di
W= mK
ð
Þ
ð
Þ:
(7.18)
From Eq. (7.18) it is clear that an increase in the diameter of the thermal insulation (di)
increases the thermal resistance of the layer
2λi
ln di
d2
□
(
and decreases the thermal
resistance of the convection at the outer surface, i.e., to the environment
α2di
□
(
.
Consequently, there exists a critical value of di that gives the smallest total thermal
resistance (1/kl) and therefore the highest heat transfer rate. A schematic view of this
behavior is shown in Fig. 7.5. This diameter di is called as the critical diameter di,cr or
the critical thickness of insulation (di,cr−d2). It is obtained by solving ∂(1/kl)/∂di=0:
∂
∂di
2λi
ln di
d2
+
α2di
□
(
=
2λidi
−
α2d2
i
= 0:
(7.19)
d2
ql
d3
dcr
d3ef
Fig. 7.5 Dependence of thermal losses on a thickness of insulation imposed on a tube (d3=di).

<!-- page 370 (PDF 14) -->
From Eq. (7.19), we have
di, cr = 2λi
α2
,
(7.20)
that says the Biot number Bicr = αdi,cr
λi
= 2. With di<di,cr, the thermal insulator
loses its role, i.e., the heat transfer rate of insulated pipe will be more than that
from the same pipe without insulation, while the thicker insulation than that of the
critical diameter (di>di,cr) results in the less heat transfer rate than that from the same
pipe without insulation but the increase in the outer insulation surface area will reduce
the thermal resistance, i.e., increasing the convective heat transfer, which is preferable
for the electrical insulation of wires (Ingersoll et al., 1954; Zvetkov and
Grigor’ev, 2005).

#### 7.1.3.6 Temperature dependence of thermal conductivity

The nuclear reactor fuel (UO2) temperature under normal operating conditions may
vary in the range 500–2000°C. In this range, the thermal conductivity of UO2 changes
about twice and is described by a nonlinear function of temperature (Fig. 7.6). Therefore
, it is necessary to account for this temperature dependency λ(T) in calculations
(Kirillov and Bogoslovskaya, 2000; Kirillov, 2008). The approximate equation in
one-dimension under stationary conditions to solve is:
d
dx λ Т
ð ÞdТ
dx
= −qV:
(7.21)
The solution of this equation is simplified with the introduction of the Kirchhoff
integral for the variable thermal conductivity, which has the dimension (W/m):
T, K
L (T)
l (T)
12,000
Fig. 7.6 Dependency of λUO2 and
ΛUO2 (Eq. 7.22) on temperature.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 371 (PDF 15) -->
Λ Т
ð Þ =
ðT
λ Т
ð ÞdТ:
(7.22)
Note that dΛ=dТ = λ Т
ð Þ and dΛ
dx = dΛ
dТ
dТ
dx = λ Т
ð ÞdТ
dx. Substituting this expression in
Eq. (7.22), we obtain:
d2Λ
dx2 = −qV:
(7.23)
The fuel temperature calculation scheme is shown in Fig. 7.7.
Integrated thermal conductivity corresponding to the maximum temperature is
given by the equation:
Λ0 = Λw + ΔΛ W=m
ð
Þ
(7.24)
where Λw is the integrated thermal conductivity at the surface, ΔΛ is the value of
which depends on the geometry and the volumetric heat source qV (W/m3) (see
Table 7.2).
Tmax
Tmax
T0
Tf
dw
ΔTa
T
T
L(T)
4p
ql
Fig. 7.7 Scheme of
calculation of Maximum
fuel pin temperature: 1-fuel,
2-gas gap, 3-cladding.
Table 7.2 Variation of integral thermal conductivity of fuel
in different geometry
Geometry
ΔΛ (W/m)
1.
Flat plate fuel (qV, W/m3) with thickness 2δ. The surface temperatures
on both sides are the same and the maximum temperature in the center
of the plate.
qVδ2
2.
Cylindrical fuel rod with linear heat rate (q0, w/m).
q0/4π
3.
Spherical fuel of radius R with volumetric heat source (qV, W/m3).
qVR2/6

<!-- page 372 (PDF 16) -->
### 7.1.4 Transient heat conduction

#### 7.1.4.1 Heating (cooling) of body

Transient heat conduction processes are divided into two groups (Ingersoll et al.,
1954; Lykov, 1961, 1978):
(1) Body tends to become thermally equilibrium with the environment when it is heated
(cooled). The heat exchange with the environment is carried out according to the Newton’s
law (Figs. 7.8 and 7.9). A special case is the process α⃗∞, when the surface temperature is
ambient temperature.
(2) The body temperature undergoes regular periodic changes.
Nondimensional form of the differential equation that describes the time-dependent
thermal conduction is as follows:
∂θ
∂τ = a ∂2θ
∂r2 + n
r
∂θ
∂r
□
(
,
(7.25)
T
t
t
T
TH
T0
T0
TH
(A)
(B)
Fig. 7.8 (A) Heating and
(B) cooling of the body of arbitrary
shape in medium with constant
temperature T0: — surface
temperature; - - - temperature
inside the body.
T
x
w
TΠOB
t1
t2>t1
T0
Fig. 7.9 Heating of semiinfinite body: T0 is the initial temperature; TW is the surface
temperature; 1, 2 denote different time.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 373 (PDF 17) -->
where θ ≡ T −Tf
T0 −Tf
; T0 is the initial temperature of the body; Tf the ambient temperature
; n=0, 1, 2 designate an infinite plate, cylinder, and sphere, respectively. The
dimensionless temperature field is determined by the Biot number (Bi = αl=λ) where
l is the characteristic dimensions of bodies, the Fourier number (Fo = aτ=l2), the body
properties (a and λ), and the dimensionless coordinate ξ:
θ =
X
∞
n=1
An · U μnξ
ð
Þexp −μ2
n · Fo
□
□
,
(7.26)
where μn is the roots of the characteristic equation μ=μ(Bi).
7.1.4.2
Heating and cooling of body at (Bi≪1)
A small value of Biot number Bi = αl=λ means any small l, or high thermal conductivity
. In this case, the temperature inside the body is practically uniform:
θ = Т −Т f
Т 0 −Тf
= exp − n + 1
ð
ÞBi · Fo
½
□,
(7.27)
where T0 is the initial temperature of the body; Tf the ambient temperature; n=0, 1, 2
designate an infinite plate, cylinder, and sphere, respectively.
The time for cooling (and heating) bodies to the temperature θ is given by:
τ = K ln θ=Bi,
(7.28)
where K=δ2/a for a plate; K=R2/2a for a cylinder, K=R2/3a for a sphere. If the
plate, cylinder, and a sphere are of the same characteristic dimension, then a
cylinder is heated (cooled) in two times, and the sphere three times faster than
the plate, which corresponds to the ratio of surface area to volume of bodies
(1:2:3).
7.1.4.3
Heating and cooling of body at (Bi≫1)
Bi = αl=λ≫1 suggests that the body has a low thermal conductivity, and a sufficiently
high heat transfer coefficient can be assumed to the environment. In this case the body
surface temperature will be close to the ambient temperature. Correlations for the
calculation of a dimensionless temperature in the middle of the bodies and the heating
time up to a certain temperature θm are given in Table 7.3.

#### 7.1.4.4 Heating and cooling of the finite body

On the surface of a semiinfinite body (x=0), the temperature of surface Ts is assumed
equal to the temperature T0 at the time τ=0. Then the time-dependent temperature
field in the body for τ>0 is described by the relation:

<!-- page 374 (PDF 18) -->
θ x, τ
ð
Þ = T x, τ
ð
Þ−Ts
T0 −Ts
= 1−erf
x
ffiffiffiffi
aτ
p
□
(
:
(7.29)
where erf
x
ffiffiffiffi
aτ
p
□
(
is the error function.
The heat flux on the surface of the body varies as:
q 0, τ
ð
Þ = λ Т 0 −Тs
ð
Þ
ffiffiffiffiffiffiffi
πaτ
p
:
(7.30)
The heat flux through the plane (x>0), parallel to the surface of the semiinfinite
body, is:
q x, τ
ð
Þ = 2λ Т 0 −Тs
ð
Þ
ffiffiffiπ
p
exp
х2
4aτ
□
(
:
(7.31)
The total amount of heat passing through the surface between the time τ1 and τ2, is
equal to:
Q =
ðτ2
τ1
q x, τ
ð
Þdτ = 2λ Т 0 −Тs
ð
Þ
ffiffiffiffiffi
πa
p
ffiffiffiffi
τ2
p
−
ffiffiffiffi
τ1
p
ð
Þ:
(7.32)

#### 7.1.4.5 Surface temperature at two bodies contact

Assume two infinite bodies (1, 2) of an initial temperature T1>T2, properties λ1, λ2, a1,
a2, are in contact each other. The temperature at the contact location is assumed Tc
(T1>Tc>T2). Then the heat flow from the body 1 to the contact position is, with
b≡
ffiffiffiffiffiffiffiffiffi
ρcpλ
p
:
q1 = λ1 T1 −Tc
ð
Þ
ffiffiffiffiffiffiffiffiffi
πa1τ
p
=
ffiffiffiffi
b1
p
T1 −Tc
ð
Þ
ffiffiffiffiffi
πτ
p
(7.33)
Table 7.3 Correlations for dimensionless temperature in the middle
of bodies and heating time at Bi≫1
Shape of
the body
Dimensionless temperature at the
middle of the body, θ
Time to heat up to the
dimensionless temperature θm
Infinite
plate
θ = 1:27e−2:47Fo
τ =
δ2
2:47a ln θm
Infinite
cylinder
θ = 1:6e−5:79Fo
τ = R2
5:79a ln θm
Sphere
θ = 2:0e−9:87Fo
τ = R2
9:87a ln θm
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 375 (PDF 19) -->
which equals to the heat flow from the contact points to the body 2:
q2 = λ2 Tc −T2
ð
Þ
ffiffiffiffiffiffiffiffiffi
πa2τ
p
=
ffiffiffiffi
b2
p
Tc −T2
ð
Þ
ffiffiffiffiffi
πτ
p
:
Hence we obtain the temperature at the contact point as: Tc =
ffiffiffiffi
b1
p
T1 +
ffiffiffiffi
b2
p
T2
ffiffiffiffi
b1
p
+
ffiffiffiffi
b2
p
:

#### 7.1.4.6 Regular thermal regime

If the dimensionless temperature profile does not change in time, we call this unsteady
heat conduction process “regular thermal regime” according to Kondrat’ev (1954)
and its generalization in Kudryashev and Zhemkov (1963) and Zvetkov and
Grigor’ev (2005). The temperature fields in the bodies of various shapes (sheet, cylinder
, sphere, etc.), which are cooled in an environment at constant temperature with
the constant heat transfer coefficient at the surface, can be represented by a series:
ϑ = T0 −T x, y, z, τ
ð
Þ
½
□= T0 −Tf
□
□
=
X
n
An Bi
ð
ÞΦ x, y, z, Bi
ð
Þe−μ2Fo,
where Fo = aτ=l2. T0 and Tf are the initial body temperature and the ambient temperature
. Cooling process of the body can be grouped into two stages. The first stage is
characterized by the influence of the initial temperature distribution, when the rate of
temperature change is different in different parts of the body. The second stage begins
with the moment when the cooling rate does not depend on the initial conditions and
determined only by the conditions of heat transfer at the interface, the physical properties
of the body, its geometry and dimensions. In this case, the temperature field is
described by:
θ
θ0
= AΦ x, y, z
ð
Þe−mτ,
(7.34)
where θ≡T x, y, z, τ
ð
Þ−Tf ; θ0 ≡T x, y, z, 0
ð
Þ−Tf ; and m = μ2
1a=l2. 1
θ
∂θ
∂τ = −m is the
rate of cooling and indicates that the relative rate of temperature change does not
depend on time or space, and is a constant. In Fig. 7.10 the time dependency of ln θ =
f τð Þ is shown at two points of the body (x1,x2). The rate of cooling is found by the
slope of the line: m = −tan ϕ =
ln θ1 − ln θ2
ð
Þ= τ2 −τ1
ð
Þ.

#### 7.1.4.7 Periodic changes of temperature

Assume a boundary condition of the surface temperature of the semiinfinite body is
prescribed as tw = tm cos ωτ
ð
Þ, where tm is the amplitude; ω = 2π=T is the angular frequency
; and as x ⃗ ∞the temperature t ⃗ 0. Note that t is temperature to distinguish
from the period of oscillation T.

<!-- page 376 (PDF 20) -->
The solution of the time-dependent diffusion equation ∂t
∂τ = a ∂2t
∂x2 under the above
boundary conditions is given by the temperature wave:
t = tm exp
−х
ffiffiffiffiffi
ω
2a
r
□
(
· cos
ωτ −х
ffiffiffiffiffi
ω
2a
r
□
(
:
(7.35)
The lower the temperature fluctuation frequency (longer period), the larger the oscillation
amplitude at a given point of the body.
The heat flux on the surface will change over time according to the Fick’s law:
q = −λ∂t
∂x
x=0
= tmb
ffiffiffiω
p cos ωτ + π
□
□
,
(7.36)
where b = λffiffia
p =
ffiffiffiffiffiffiffiffiffi
ρcpλ
p
. The amount of heat diffusing into the environment in half a
period T/2 through the unit surface area is found to be:
Q =
ðT=2
qdτ = tmb
ffiffiffiffiffi
2T
π
r
:
(7.37)
The method of temperature waves is used to measure the thermal diffusivity. If we
measure the delay of the wave Δτ at a depth x, then, knowing the period T, it is easy
to determine a (thermal diffusivity).

### 7.1.5 Thermal conductivity of composite and dispersed media

Composites, laminates, fibrous, granular materials, dispersion media are frequently
encountered in engineering. In the simplest case, e.g., a two-component system composed
of continuous phase matrix and inclusions with different thermal properties
x=0
Inq1
Inq2
Inq
x=1
t1
t2
t
j
j
Fig. 7.10 Schematics of dimensionless temperature vs time. Stage I: the initial unordered mode;
Stage II: regular thermal regime.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 377 (PDF 21) -->
(Chudnovsky, 1954. Ingersoll et al., 1954; Kaviany, 2002; Lykov, 1967, 1978;
Odelevsky, 1951).
Let’s denote volume fraction of one inclusion by φ and its thermal conductivity by
λ0. The continuous medium, such as gas, liquid, or solid in which a disperse phase is
distributed, is called as the dispersion medium. For instance, filled with solid particles,
a liquid medium, or a gas is referred to as the dispersion medium. Heat transfer takes
place in this dispersed medium by: (1) the thermal conduction inside an individual
particle; (2) conduction through the particles contact; (3) conduction in the continuous
medium; (4) conduction through the contact of the medium with the particles; (5) convection
heat transfer by gas and steam between the particles; and (6) the radiation from
particle to particle.
Calculation of the individual processes and their additional combination is feasible
only when one or two processes are crucial. Otherwise, such an approach requires clarification
of many difficult circumstances to be taken into account, knowledge on the
microscopic structure and its characteristics of the particle material and the continuous
medium, the processes of mutual influence on each other, etc.
Another approach is regarded as a quasihomogeneous dispersion medium with
some effective features (mixture density, effective thermal conductivity, etc.), which
is applicable to the heat transport equation. Then, the thermal characteristics (λ, a, ρ,
cp, etc.) are functions of the temperature, porosity, time coordinates (Yang and
Nakayama, 2010; Dul’nev and Zarichniak, 1974; Dul’nev and Novikov, 1991;
Fedotovsky, 1994; Kaviany, 2002). Two limiting cases are shown in Fig. 7.11.
If the ratio of the conductivity of the inclusions λ0 to that of the matrix (continuous
phase) λ is much smaller than unity, i.e., λ0/λ≪1, the greatest effect is achieved in the
insulation case of transverse heat flow (Fig. 7.11A). Heat conduction calculation can
be carried out by the method of multilayer walls, for the known geometry, and using
the effective thermal conductivity of the array (λeff) defined with the volume fraction
of inclusions (φ) and the thermal conductivity (λ and λ0):
λeff
= 1
λ 1−φ
ð
Þ + 1
λ0
φ:
(7.38)
In the case of λ0/λ≪1, the least insulation effect is observed obviously at the
longitudinal arrangement (Fig. 7.11B). In this case,
l
l0
q
q
(A)
(B)
Fig. 7.11 Two limiting arrangements of
continuous phase matrix and inclusions
with different thermophysical
properties: (A) transverse;
(B) longitudinal.

<!-- page 378 (PDF 22) -->
λeff = λ 1−φ
ð
Þ + λ0φ:
(7.39)
Bi-component regular structure system of spheres may be provided in the cubic,
tetrahedral (hexagonal), or random packing arrangement (Fig. 7.12). The porosity
of these structures, i.e., 1−φ is 0.4764 for the cubic and 0.2595 in the hexagonal
close-packed structure.
The effective thermal conductivity of the dispersion medium with the spherical
inclusions is discussed in Meredith and Tobias (1961), Dul’nev and Zarichniak
(1974), Fedotovsky (1994), Yamada and Ota (1980) and can be represented by the
formula:
λeff
λ = 1−φ
ð
Þ + λ0=λ
ð
Þ 1 + φ
ð
Þ
1 + φ
ð
Þ + λ0=λ
ð
Þ 1−φ
ð
Þ,
(7.40)
where λ and λ0 are the thermal conductivity of the matrix and inclusions; φ is the
volume fraction of inclusions. The formula is valid for φ=0–0.5.
Similar results will give the formula of Maxwell-Aikin:
λeff
λ = 2 1−φ
ð
Þ + λ0=λ
ð
Þ 1 + 2φ
ð
Þ
2 + φ
ð
Þ + λ0=λ
ð
Þ 1−φ
ð
Þ :
(7.41)
Rather new formula is found in more recent publication in Kaviany (2002) for
spherical inclusions in the matrix thermal conductivity λ:
λeff
λ =
1− 6φ=π
ð
Þ1=3 · Fi γð Þ
,
(7.42)
where γ =
9πφ2
□
(1=3
λ=λ0
1−λ=λ0
for φ<0.3. Function F(γ) is different for different
relationships λ/λ0. When λ/λ0<1, e.g., with the ceramic, metal inclusion:
F1 γð Þ = 1−
γ
2 γ + 1
ð
Þ1=2 ln γ + 1
ð
Þ1=2 + 1
γ + 1
ð
Þ1=2 −1
; and for λ/λ0>1, e.g., examples with gases
or low conductivity inclusion in highly conducting matrix:
(A)
(B)
(C)
Fig. 7.12 Regular packing of spheres: (A) cubic; (B) hexagonal; (C) random.
Thermal Hydraulics in Water-Cooled Nuclear Reactors
