# Nomenclature
<!-- source PDF pages 1-6 -->

<!-- page 167 (PDF 1) -->
D. Bestion, C. Morel
Atomic Energy Commission, Grenoble, France
Abstract
Any investigation of a nuclear thermal-hydraulic issue either by hand calculations or
using more or less sophisticated simulation tools requires first a difficult selection of
the right degree of simplification of equations depending on the situation and on the
expected accuracy and reliability of the solution. An effort is made to present the subject
in steps of increasing difficulty and to show differences and similarities between balance
equations in system thermal-hydraulics and in computational fluid-dynamics. This may
help the reader to find his own path toward the understanding of the complex nuclear
thermal-hydraulics. Attention is drawn on the physical assumptions and simplifications
used in the derivation of equations and on the resulting limitations of the predictive
capabilities. The chapter gives a picture of the available models with an evaluation of
the predictive capabilities, the limitations, and the maturity of each model.
Nomenclature
Acronyms
BWR
boiling water reactor
CFD
computational fluid dynamics (numerical solution of 3-D equations of fluid
dynamics)
CHF
critical heat flux
CMFD
computational multifluid dynamics (numerical solution of 3-D equations for
multiphase or multifluid flow)
DES
detached eddy simulation
EVET
equal velocity equal temperature
HEM
homogeneous equilibrium model
IA
interfacial area concentration
ITM
interface tracking method
IRT
interface reconstruction technique
LBLOCA
large break loss of coolant accident
LES
large eddy simulation
LEIS
large-eddy and interface simulation
PDE
partial differential equation
PWR
pressurized water reactor
RANS
Reynolds average Navier-Stokes
RHS
right-hand side
TIA
transport of interfacial area
UVUT
unequal velocity unequal temperature
VLES
very large eddy simulation
Thermal Hydraulics in Water-Cooled Nuclear Reactors. http://dx.doi.org/10.1016/B978-0-08-100662-7.00005-1
© 2017 Elsevier Ltd. All rights reserved.

<!-- page 168 (PDF 2) -->
Symbols latin
A
surface (m2)
A
cross-sectional area of a duct (m2)
ai
interfacial area concentration (m−1)
C
wall contour in a cross section of a duct
Cs
pressure wave (sound) celerity (m/s)
Cp
heat capacity at constant pressure (J/kg/K)
Cd
drag coefficient
Cf
friction coefficient
Ci
interface contour in a cross section of a duct
Ck
wall contour in a cross section of a duct in contact with phase k
Cα
void wave celerity (m/s)
Cμ
turbulent viscosity coefficient
D
diameter (m)
D
mass diffusivity (m2/s)
Dh
hydraulic diameter (m)
F
⃗
specific external forces (usually limited to gravity: F
⃗= ρ g
⃗) (N/m3)
Fik
interfacial momentum transfer to phase k per unit volume (N/m3)
g
⃗
gravity acceleration vector (m/s2)
gi
gravity acceleration vector components (m/s2)
gz
gravity acceleration projected along Oz
⃗
axis (m/s2)
G
mass flux (kg/m2/s)
Gk
mass flux of phase k (kg/m2/s)
h
specific enthalpy (J/kg)
hk
specific enthalpy of phase k (J/kg)
hksat
specific saturation enthalpy of phase k (J/kg)
hlv
latent heat (J/kg)
Hk
time- and/or space-averaged specific enthalpy of phase k (J/kg)
jk
local superficial velocity of phase k (m/s)
J
diffusive flux
Jk
t
turbulent flux of ψk
Jk
area-averaged superficial velocity of phase k (m/s)
k
turbulent kinetic energy (m2/s2)
_M
mass flowrate (kg/s)
_m
mass flux (kg/m2/s)
_Mk
mass flowrate of phase k (kg/s)
Mik
interfacial force per unit volume (N/m3)
Mik
D
drag force per unit volume (N/m3)
Mik
L
lift force per unit volume (N/m3)
Mik
AM
added mass force per unit volume (N/m3)
Mik
TD
turbulent dispersion force per unit volume (N/m3)
n
⃗
k
unit vector normal to interface-oriented outside phase k
Nu
Nusselt number
p
pressure (Pa)
P
space-time averaged mixture pressure (Pa)
Pr
Prandtl number

<!-- page 169 (PDF 3) -->
q
⃗
heat flux vector (W/m2)
qj
conduction heat flux vector components (W/m2)
qext
volumetric external energy source, e.g., due to radiation (W/m3)
qk
⃗
heat flux vector in phase k (W/m3)
qkj
conduction heat flux vector components in phase k(W/m2)
qik
heat flux per unit volume from interface to phase k (W/m3)
qidl
heat flux per unit volume from interface to droplet (W/m3)
qivdl
heat flux per unit volume from vapor to interface of droplet (W/m3)
qicl
heat flux per unit volume from interface to continuous liquid (W/m3)
qivcl
heat flux per unit volume from vapor to interface of continuous liquid (W/m3)
qkj
t
turbulent heat diffusion vector components in phase k (W/m2)
qw
wall heat flux (W/m2)
qwk
wall heat flux to phase k (W/m2)
Q
volume flowrate (m3/s)
Qk
volume flowrate of phase k (m3/s)
Qik
interface-to-phase k interfacial energy transfer rate per unit volume (W/m3)
Re
Reynolds number
Rk
surface fraction of phase k (in 1-D equations)
Rij
Reynolds stress tensor
s
specific entropy (J/K/kg)
t
time (s)
T
temperature (K)
T
stress tensor (KPa)
u
specific internal energy (J/kg)
v
⃗
velocity vector (m/s)
vj
velocity vector components (m/s)
vk
⃗
velocity vector in phase k (m/s)
vk,j
velocity vector components for phase k (m/s)
v
⃗
ni
component of velocity of interface normal to the interface
V
volume (m3)
V
time- and/or space-averaged velocity (m/s)
Vk
time- and/or space-averaged velocity of phase k (m/s)
Vidl
interfacial axial velocity at continuous liquid interface (m/s)
Vicl
interfacial axial velocity at continuous liquid interface (m/s)
Yk
mass concentration of species k
Symbols greek
αk
space-time fraction of phase k
β
added mass coefficient
γ
slip ratio
δ32
Sauter mean diameter
εk
local time fraction of phase k
ε
dissipation rate (m2/s3=W/kg)
λ
heat conductivity (W/m2/K)
μ
dynamic viscosity (kg/s/m)

<!-- page 170 (PDF 4) -->
ν
kinematic viscosity (m2/s)
Γik
interface-to-phase k interfacial mass transfer rate per unit volume (kg/m3/s)
Γvcl
interfacial mass transfer rate per unit volume from continuous liquid to vapor (kg/m3/s)
Γvdl
interfacial mass transfer rate per unit volume from dispersed liquid to vapor (kg/m3/s)
Γd
mass transfer rate per unit volume by droplet deposition (kg/m3/s)
Γe
mass transfer rate per unit volume by droplet entrainment (kg/m3/s)
σ
surface tension (N/m)
ρ
density (kg/m3)
ρk
density of phase k (kg/m3)
ρm
mixture density (kg/m3)
σ
surface tension (N/m)
τij
viscous stress tensor components (Pa)
τwk
wall friction force applied to phase k (Pa)
ϕ
porosity
ϕ
volumetric source of ψ
χ f
fluid characteristic (or indicator) function
ψ
specific quantity
χ k
phase characteristic (or indicator) function
Symbols other scripts
T
viscous stress tensor components (Pa)
Subscripts and superscripts
AM
relative to the added mass force
c
relative to continuous field
cl
relative to continuous liquid field (in a 3-field 2-phase flow of a fluid with its vapor)
dl
relative to dispersed liquid field (in a 3-field 2-phase flow of a fluid with its vapor)
d
relative to dispersed field
cl
relative to continuous liquid
dl
relative to dispersed liquid
D
relative to drag force
f
relative to liquid phase in a gas-liquid two-phase flow
g
relative to gas phase in a gas-liquid two-phase flow
k
relative to phase k or field k
i
relative to interface
i
ith component
j
jth component
ki
relative to phase k or field k at interface
k
relative to wall
l
relative to liquid phase (in a two-phase flow of a fluid with its vapor)
L
relative to lift force
m
relative to a mixture
sat
relative to a saturation

<!-- page 171 (PDF 5) -->
S
relative to a surface
t
relative to turbulence
TD
relative to turbulent dispersion force
v
relative to vapor phase (in a two-phase flow of a fluid with its vapor)
x,y,z
coordinates
z
curvilinear abscissa
Double averaged quantities in single-phase flow
ϱ ≜bρ = ρ
h iS
space-time averaged density
P≜b⟨p = ⟨p
h iS
space-time averaged pressure
V≜vz⟩= ρvz
h
iS
ρ
h iS = ρ evz
h
iS
ρ
h iS
mass-weighted space-time velocity
H≜⟨h⟩= ρ⟨h
□
□S
ρ
h iS =
ρeh
D
ES
ρ
h iS
mass-weighted space-time enthalpy
Double averaged quantities in two-phase flow
ϱk≜c
ρk
k =
χkρk
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
P≜αv Pv + αl Pl
space-time mixture average pressure
Vk≜vzk⟩k≜χkρkvzk
h
iS
χkρk
h
iS = χkρkvzk
h
iS
αk c
ρk
k
mass-weighted space-time phase average velocity
jk≜χkvzk = εk⟨vk
zk
local time phase averaged superficial velocity
j≜jv + jl
local time mixture-averaged superficial velocity
Jk≜jk
h iS = εk⟨vk
zk
□
□S
space-time phase average superficial velocity
Jk≜Jv + Jl
space-time mixture average superficial velocity
Vk≜Jk
αk
= χkvzk
h
iS
χk
h
iS
space-time phase average velocity
Gk≜αkϱkVk = χkρkvzk
h
iS
phase mass flux
G≜Gv + Gl
mixture mass flux
Hk≜hk⟩k
=
χkρkhk
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
mass flux-weighted space-time phase average enthalpy
H
z}|{
m≜GvH
z}|{
v + GlH
z}|{
l
G
mass flux-weighted space-time mixture average enthalpy

<!-- page 172 (PDF 6) -->
x≜αvϱv
ϱm
static quality
X≜Gv
G
dynamic quality
Xth = H
z}|{
m −hlsat
hvl
thermodynamic quality (or equilibrium quality)
Non-dimensional quantities
Bo
Bond number (E€otwos)
Bo = gΔρL2
σ
Fr
Froude number
Fr =
vffiffiffiffiffiffi
gD
p
Jk*
non-dimensional superficial velocity of phase k (m/s2)
Jk* =
ffiffiffiffi
ρk
p
Jk
ffiffiffiffiffiffiffiffiffiffiffi
gΔρD
p
Kk
Kutateladze number for phase k
Kk =
ffiffiffiffi
ρk
p
Jk
gΔρσ
ð
Þ
1□
Re
Reynolds number
Re = vD
ν
We
Weber number
We = ρΔV2L
σ
Operators
r
gradient operator
r:
divergence operator
r2 = Δ
Laplacian operator
A
⃗ B
⃗
dyadic product of vectors (=tensor)
A
⃗ · B
⃗
scalar product of vectors (=scalar)
A:B
double-dot product of 2 tensors (=scalar)
tT
transpose tensor
Time averaging operators
⟨f≜1
T
ð
T
f dt
time averaging
ef≜ρf =ρ
mass-weighted time averaging
⟨f k≜χkfk=χk
phase time averaging
ef k
k≜χkρkfk
χkρk
= εkρkfk
εkρk
k = ρkfk
k
ρk
k
phase mass-weighted time averaging
