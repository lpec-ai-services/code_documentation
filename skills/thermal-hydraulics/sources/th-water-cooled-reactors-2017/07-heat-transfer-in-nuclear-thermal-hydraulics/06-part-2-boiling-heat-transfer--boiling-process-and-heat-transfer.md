# Part 2: Boiling Heat Transfer — Boiling process and heat transfer
<!-- source PDF pages 64-76 -->

<!-- page 420 (PDF 64) -->
Rapier et al. (1963), Sanderson (1961), Yovanovich (1986, 1998), Yovanovich and
Marotta (2003), Skipper and Wootton (1958), and Skipper (1958).
The final word, as always, experimental results play crucial roles in this area.
Part 2: Boiling Heat Transfer
In this second half of this chapter, we concentrate on boiling heat transfer phenomena
first focusing on nucleate and film boiling in a nonflowing system, i.e., in a pool
of a large volume, and then on convective boiling in channels, focusing on the fundamental
aspects of heterogeneous nucleation and heat transfers, i.e., boiling
two-phase flow heat transfer from the heated surface to fluids. It is designed again
for professionals as well as for students, being aimed at helping readers to better
understand the phenomena and at providing the basis on which physical modeling
of the phenomena is to be made for the system safety analysis and subchannel
analysis of nuclear reactors.

## 7.5 Boiling process and heat transfer

### 7.5.1 Advantages of the boiling process

Boiling is a process of evaporation of the bulk liquid. The main advantage of using a
boiling process in nuclear engineering is due to a fact that quite high heat fluxes are
achieved without increasing significantly the surface temperature. Mechanisms of
heat removal from the heated surface is associated with conduction, liquid- and
vapor/gas-phase convection, phase change of liquid into vapor with the latent heat
of vaporization, and radiation. The liquid-phase motion near the surface is largely
determined by the dynamics of growth of vapor bubbles. The bubble dynamics is associated
with the temperature field in the region surrounding the vapor bubble; and the
temperature field is a result of interaction with the bubble dynamics itself. The number
of nucleation sites is determined by the conditions at the surface (surface roughness,
wettability, etc.). A large number of governing parameters (geometry, properties of
the liquid, vapor, surface properties, and the boundary conditions of each phase) complicate
the theoretical analysis of the boiling process. The intensity of the boiling heat
transfer will be dependent on many factors difficult to control (surface roughness, the
amount of dissolved gases in the liquid, wettability, etc.), which cannot be fully taken
into account in theory and experiment.
There are at least three reasons for the heat transfer enhancement in the boiling.
First, the strong turbulence agitation to the boundary layer at the expense of growth
and separation of vapor bubbles. Second, the heat transfer by evaporation of the liquid
microlayer at the bottom of the vapor bubble. Third, the transfer of the latent heat of
vaporization into the growing vapor bubble. The absence of a closed mathematical
description of the process of boiling heat transfer and an abundance of factors
influencing the process make choices of generalized variables rather arbitrary. Correlations
obtained as a result of processing and synthesis of experimental data are
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 421 (PDF 65) -->
inevitably semiempirical, and able to describe only a certain average level of the heat
transfer.
… The fact of the successful approximation …. Experimental data of some empirical
formula does not give grounds for approval of the true extent of influences of various
properties on the heat transfer during boiling
(Labuntsov, 1972)

### 7.5.2 Onset condition of boiling on a heated surface

Formation of the vapor phase in a volume of liquid is due to density fluctuations
caused by the random motion of molecules.
For a spherical bubble to stay in a volume of liquid and not to collapse under the
forces of surface tension, the pressure therein must be greater than the pressure of the
surrounding fluid, and its size must be larger than a certain critical radius Rcr. This
value is calculated from the Laplace’s pressure Δp1 = 2σ=R, and Thomson modification
, taking into account the change in the vapor pressure of the concave curved
surface of radius R compared with a flat surface: Δp2 = 2σ
R ·
ρg
ρf −ρg
. A sum of pressure
differences Δp = Δp1 + Δp2 must comply with the Clausius-Clapeyron equation:
Δp
ΔT =
Δhfg
T vg −vf
□
□. Hence the critical (minimum) radius of the nucleus Rcr of the vapor
can be obtained from:
Rcr = 2σT vg −vf
□
□
ΔhfgΔT
ρf
ρf −ρg
:
(7.117)
For ρg≪ρf or vf ≪vg
□
□
, we have
Rcr
2σTS
ΔhfgρgΔT = 2σℜT2
S
ΔhfgpΔT , with p = ρgℜTS, ℜ: gas constant:
(7.118)
Required wall superheating can be obtained for the formation of a vapor bubble of
radius R by:
Tw −TS = ΔT
2σTS
ΔhfgρgR = 2σℜT2
S
ΔhfgpR:
(7.119)
This equation can be used for the subcooled liquid to its saturation temperature TS
(Hahne et al., 1990).
Boiling begins on the heated surface where the surface is at an excess temperature
and the liquid at saturation. The birth of a vapor bubble on a solid surface takes place at
the nucleation centers where the surface energy for the vapor formation is lowest.

<!-- page 422 (PDF 66) -->
Usually this recess is portions with weak molecular adhesion between liquid and solid.
For the vapor bubble formation to occur on the surface, also a certain degree of superheating
of the liquid above the saturation temperature is required. It depends on the
purity of the liquid and the presence of vaporization centers, i.e., surface conditions.
The centers of vaporization—cavities on the surface, are filled with gas or vapor.
Under ideal conditions, superheat in the bubble of radius R is described by the classical
theory:
ΔTS = Tg −TS = pTS vg −vf
□
□
Δhfg
ln
1 + 2σ
pR
□
(
:
Typically, for 2σ
pR<<1,
ln 1 + 2σ
pR
□
(
ffi2σ
pR with sufficient precision. R may be
regarded as the maximum radius of the cavity—the center of vaporization
would be 0.2–0.4 μm. Superheating ΔTw and the surface heat flux corresponding to
the beginning boiling (qbb
3) in general can be calculated by the relationships:
ΔTw = Tw −TS =
pTS vg −vf
□
□
ΔhfgRe0:2Pr0:5 p=pcr
ð
Þ;
and
qbb = α Tw −Tf
□
□
= α
TS −Tf
□
□
+ ΔTw
,
where the heat transfer coefficient α can be obtained from single-phase convective
heat transfer correlations.
Size of the vapor embryos depends on the surface roughness and wettability
conditions. The number and size of nucleation sites define the boiling initiation.
If the nucleation sites are many and large, the boiling initiation requires small
superheating. Good wettability liquid fills the surface cavity and the excess temperature
rise of the surface temperature over saturation, i.e., (Tw −TS) must
be higher than in the case of poor wettability fluid. Good wettability fluid
leads to hysteresis phenomena during boiling—a significant increase in the
surface temperature before boiling and its subsequent decline from the start of
boiling.
For good wettability liquids which begin to boil as the steam embryo of the critical
radius:
Rcr = 2σλf TS vg −vf
□
□
qΔhfg
0:5
,
3bb: beginning of boiling.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 423 (PDF 67) -->
a recommended correlation for the amount of wall surface superheat is:
Tw −TS = 2σ
Rm
TS vg −vf
□
□
Δhfg
,
where Rm is the radius of the largest cavity (Rm<Rcr).
The heat flux corresponding to the beginning boiling (qbb):
qbb = α
TS −Tf
□
□
+
2σ
Rm
□
(TS vg −vf
□
□
Δhfg
:
Magnitude of 2σ/Rm, for example for water at 0.1 MPa (σ □60 mN/m) and
Rm	0.4 μm, is 1.5□103 Pa. With good wettability of surfaces and without impurity
(e.g., liquid metals, liquids with low surface tension, and the like), the high superheating
is usually realized. Under these conditions, growth rate of the vapor volume
is limited by (Gavrilov, 1999):
R =
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
6Mcf
k
ρf
ρg
aτ
s
,
(7.120)
where M is the molecular weight; k=1.38□10−23 J/K is Boltzmann constant; a is the
thermal diffusivity in m2/s; cf is the specific heat capacity of the liquid in J/(kg K)
and the time τ is in s. Eq. (7.120) implies that the growth rate is independent of the
magnitude of superheating.
In general, the interface velocity is determined by solving Rayleigh’s equation,
transient energy and mass conservation equations simultaneously, considering the
energy-mass balance conditions at the interface.

### 7.5.3 Types of boiling

Depending on the heat flux and other factors of the wall surface, vapor bubbles or a
continuous layer of vapor is formed, which is accordingly called bubbly or film boiling
. In the nucleate boiling, the liquid is in direct contact with the nucleation site on the
surface. In the film boiling, the vapor layer separates the liquid from much of
the heated wall surface. The vapor layer covering the heated wall surface transfers
the heat by conduction and reduces the heat transfer rate by many times, so a transition
from the nucleate boiling to the film boiling takes place at a constant heat flux and may
be accompanied by a sharp increase in the surface temperature of the heating wall
(heat transfer crisis or burnout, or simply “crisis”).
Various types of boiling are classified as follow:
–
By the nature of the boiling—nucleate boiling and film boiling;
–
The type of convection—the boiling under natural convection (in a large volume), and
forced convection;

<!-- page 424 (PDF 68) -->
–
Magnitude of the average fluid temperature (Tf ) relative to the saturation temperature
(TS)—subcooled boiling if Tf < TS; liquid temperature close to the saturation temperature
(Tf 	 TS)
–
On the surfaces—horizontal, vertical, inclined;
–
The nature of the boiling—developed, developing, or undeveloped and unstable.
Nucleate boiling is developed for a large number of nucleation sites and undeveloped
for a small number of nucleation sites. In the latter case, a large proportion of the heat
is removed by the single-phase liquid flow convection. The boiling process becomes
unstable, if the nucleate boiling regime is replaced by a liquid-phase random natural
convection, and then back to nucleate boiling again.

### 7.5.4 Boling curve

Dependence of the heat flux on the temperature difference (Tw −TS) is the boiling
curve (Fig. 7.40), originally proposed by Nukiyama (1934). With increasing the temperature
difference, the heat flux reaches a maximum and then decreases and increases
again (curve ABB0C0CDE). On this curve, you can highlight areas of different modes
of heat transfer and the characteristic points (see Fig. 7.40).
For the region of free convection (ABK), the heat transfer coefficient α □ ΔТm,
typically with m=1/4 for the laminar region and m=1/3 for turbulent flow regime.
Consequently, q = α · ΔТ □ ΔТ5=4□4=3. At point B, boiling begins on the surface. If the
temperature of the liquid in a volume is lower than TS, the bubbles within the liquid
condense. If the fluid temperature is equal to TS, the bubbles will rise to the liquid
surface without condensing.
In region 2 (BB0) with increasing heat flux or temperature difference increases the
number of nucleation sites and increases the heat transfer rate, although still a
log q
log(Tw –Ts)
A B
D
K
C
C□
B□
E
Fig. 7.40 Boiling curve for a large volume (Nukiyama curve). Different modes of heat transfer:
1—gravitational convection; 2—undeveloped boiling; 3—developed boiling; 4—boiling
transition (from bubble to film); 5—film boiling; \\\\\—region stable boiling. Typical modes:
AB—natural (free) convection; B—beginning of nucleate boiling; B0—beginning of the
developed nucleate boiling; C—point of crisis; D—Leidenfrost point; C0—point of deviation
from the mode of nucleation.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 425 (PDF 69) -->
considerable amount of heat removed by convection. With further increase in q or the
number of nucleation sites continuously increases, an increasing portion of the heat is
removed by evaporation.
In the region (B0C0), q □ ΔТ3□4; Point C0 corresponds to the deviation from the
nucleate boiling regime; and the point C is reached the maximum heat flux, called
critical heat flux because further (even slight) increase in the q results in a dramatic
increase in the wall surface temperature according to the line (C–E). If the surface
temperature can be controlled, it will lead to an increase in vapor blanketing the surface
and the heat flux decreases (CD). For the vapor flowing along the surface,
it requires a significantly higher wall surface temperature (DE) to achieve the same
heat flux of the nucleate boiling.
In the region of sustainable film boiling, the heat is transferred from the heated wall
through the vapor by the evaporation of a thin liquid layer, steam convection, and radiation
. The contribution of the radiation increases with ΔТ. In the region (DE) q □ ΔТ3.
Influences of various factors on the boiling curve for pool boiling is illustrated
qualitatively by a series of charts as illustrated in Fig. 7.41 (Chai and Shoji, 2001;
Shoji, 1998; Soloviev, 1998).
The boiling curve shifts to the right with the increase in the system pressure and the
heat transfer coefficient increases with the pressure in the nucleate and film boiling
regime (A). At very low pressures (Rcr is large), there is a delay to start boiling in
the process of natural convection that requires more fluid to superheated (Tw −TS).
After the boiling initiation, this superheating will be reduced. With a reduction in
Effect of pressure P3> P2> P1
Hysteresis at low pressure:
NC—Natural convection;
NB—Nucleate boling
      Effect of porous coating
1—Smooth surface;
2—Coated surface
Influence of gas content:
       degassed water;
       sparkling water
Effect of sedimentation:
       clean surface;
       surface with sediments
(B)
(C)
(E)
(A)
(D)
(F)
NB
lg q
P1
P2
P3
lg q
lg q
lg q
lg q
lg q
E
F
C
H
B
D□
A□
A
G
D
lg ΔT
lg ΔT
lg ΔT
lg ΔT
lg ΔT
lg ΔT
NC
Influence of surface roughness:
smooth;        rough
Fig. 7.41 Influence of various factors on the process of the boiling (boiling curve) in bulk fluids.

<!-- page 426 (PDF 70) -->
the heat flux, a transition can occur from nucleate boiling (NB) again to the natural
convection (NC)—hysteresis phenomenon (Fig. 7.41B). At sufficiently high heat
flux with increasing surface superheating, a possible transition could take place from
nucleate to film boiling, bypassing the transition boiling regime. On the other
hand, with a decrease in the film boiling surface (or reduction of the heat flux), the
system can switch to the nucleate boiling regime, also bypassing the transitional
regime—hysteresis II.
Issues related to the transition boiling regime have been studied in the last decades
intensively (Gavrilov, 1999; Haddad and Cheung, 1998; Klimenko and Snytin, 1988),
although a satisfactory understanding of the process has not yet been reached.
Fig. 7.41C schematically shows a difference of the boiling curve on a smooth surface
and a porous surface coating. On the porous surface, boiling occurs at lower heat flux
density (A) than on the smooth surface (A0). If the coating has high permeability and
high thermal conductivity, then the boiling curve would be ABCD. If the vapor
encounters resistances in coming out of the porous structure, the process while reducing
the q is on the line DH or EFG. One of the reasons for the observed hysteresis is
due to a difficulty for the liquid to penetrate from the small pores into the large space.
In this case, the heat transfer coefficients at EFG line is determined from thermal resistance
of the porous coating δ/λ. This mode of nucleate boiling is considered to have the
vapor film inside the porous layer. With low permeability porous coating, a transition
to the film boiling is observed with the vapor available on the BF line at q<qcr. The
position of the curve (2) depends on the coating thickness, permeability, thermal conductivity
. Data in some areas of the curve (2) for coatings can be found in industrial
practices. An overview and the method of heat transfer calculation at boiling on the
porous surfaces is found in Soloviev (1998).
The presence of surface roughness increases the heat transfer rate (Fig. 7.41D). The
presence of gas in the liquid enhances boiling at low heat fluxes and the heat transfer
during the nucleate boiling (Fig. 7.41E). Effects of deposits (e.g., corrosion products)
typically come from the low thermal conductivity of the deposits, resulting in an
increase ΔT and the boiling curve to shift to the right (Fig. 7.41F).
Bubbly boiling structure on a horizontal surface will change as the heat flux
increases from single large steam bubbles to vapor mushroom formations (Gertner,
1965) (see Fig. 7.42).

#### 7.5.4.1 Minimum film boiling temperature

On the boiling curve illustrated in Fig. 7.43, point D, corresponding to the minimum
heat flux qmin and temperature Tmin, it is called the Leidenfrost point or minimum film
boiling temperature TMFB. Various names have been given to the TMFB including
rewetting temperature, quench temperature, Leidenfrost temperature, film boiling collapse
temperature and others. Heat transfer characteristics in the vicinity of the TMFB
point are important in assessing the cooling process of the heated surfaces (hardening
treatment by quenching) and in evaluating the ECCS for LOCA. This point separates
the transition boiling and film boiling modes: in the region T>TMFB the liquid ceases
to wet the heated surface. A conventional technique to define TMFB is associated with
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 427 (PDF 71) -->
Fig. 7.42 Boiling curve and vapor bubble structure depending on heat flux: I—individual
bubbles region; II—the first transition region; III—mushroom region; IV—the second transition
region.
F
A
D
E
B
C
E□
qA
T
Th
TA
Tmin
qmin
qmax
q, BT/M2
Fig. 7.43 Boiling curve: AF—film boiling; CE0—transition boiling from nucleate to film
boiling; EDA—transition from film boiling; EE0—heat flux jump with improved wetting;
TA, qA—temperature and heat flux in the presence of liquid contact; C initiation of transition
boiling.

<!-- page 428 (PDF 72) -->
the measurement of the lifetime (evaporation) τ of drops on the hot surface heated up
to Tw. Fig. 7.44 shows a comparison of the curve τ=f(Tw) as if it were inverted
boiling curve.
It is well known that the mode of liquid contact with the heated surface is
dependent not only on the temperature, but also on the liquid-wall interface conditions
(surface smoothness, surface roughness, surface geometry, subcooling,
surface tension, boundary conditions, etc.). It is noted that, in Fig. 7.43, the
deterioration of the wettability will shift the beginning of film boiling to TE
(<Tmin) while improved wettability to TA (>Tmin), where EDA is the transition
region to the film boiling regime and the region AF is the mode of pure film
boiling.
Trying to take into account the thermal properties of the heated surface and the
wettability conditions of the liquid-solid system, Baumeister and Simon (1973)
arrived at the following semiempirical expression:
Tmin = Tf +
0:844Tcr 1− exp
−0:016
ρs=Ms
ð
Þ1:33=σ
h
i 0:5
□
(
−Tf
□
□
exp 3:066□106β
□
□
erfc 1758
ffiffiffiβ
p
ð
Þ
□−1,
where the subscript s refers to the surface material; β = 1= ρscpsλs
□
□
; σ is the surface
tension; Ms is the atomic weight of the surface materials; λs is the thermal conductivity
; ρs is the density; cps is the specific heat of the material. It is logical to assume that
the influence of ΔTsub (subcooling) on Tmin will be similar to the effect on the critical
heat flux qcr, i.e., qcr 	 q0 + ΔTsub. Experiments were carried out with the hot spheres
(1–100 mm in diameter) that are immersed in various fluids (water, Freon, sodium,
Fig. 7.44 (A) Boiling curve at saturation temperature and (B) liquid droplets evaporation time
on a heated surface: 1—nucleate boiling initiation; 2—critical heat flux; 3—minimum heat flux
(Leidenfrost point); 4—separated bubbles; 5—jets and steam column mode; 6—single-phase
convection mode; 7—bubble-film coexisting boiling regime; 8—transition boiling regime;
9—film boiling regime; 10—vapor layer; τ—the evaporation of droplets.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 429 (PDF 73) -->
etc.) by many researchers. For water, obtained empirical relationships are summarized
by the formula:
Tmin °C
ð
Þ = A + BΔTsub,
where A=200–220°C; B=6.3–8. Quenching cooling mode at high ΔTsub will lead to
a sudden achievement of higher wettability resulting in a jump in the heat flux. It is
commonly accepted that during the initial stages of the drop-surface contact, the interface
temperature between the liquid and solid is dictated by the thermal properties of
the liquid and solid as well as by their initial temperatures. This interface temperature
Ti is given by the solution to the one-dimensional energy equation with semiinfinite
body boundary conditions (Eckert and Drake, 1972):
Ti =
λρcp
□
□0:5
s T0 + λρcp
□
□0:5
f Tf
h
i
=
λρcp
□
□0:5
s
+ λρcp
□
□0:5
f
h
i
:
The limiting temperature at which the initial contact can stay nonequilibrium or
metastable, i.e., superheating of a liquid above its boiling point, between the liquid
and the drop surface, is the homogeneous nucleation temperature Thn. A detailed theory
of this process was developed and reported by Skripova (1972). An empirical relationship
for Thn is established by Ramilison and Lienhard (1988):
Thn = Tcr 0:923 + 0:077 Ts=Tcr
ð
Þ9
h
i
:
It is necessary to distinguish between Thn (≡Tlim) and Tmin (=TMFB). Tlim (≡Thn) is
determined purely by the thermodynamic conditions. Tmin is affected by not only thermodynamic
factors, but also by many other factors such as actual fluid periodical contacts
with the wall, insulation of the surface, etc. Experimental data indicate that the
pressure is an important parameter for thermophysical properties of the fluid, surface
tension, contact angle, and surface material which can play an important role in
determining Tmin.
In accordance with Klimenko and Snytin (1988):
Tmin −Ts
Tlim −Ts
= ΔTmin
ΔTlim
= 8:2 + 4
ρcλ
ð
Þf
ρcλ
ð
ÞW
+ 60
ρcλ
ð
Þf
1=2
ρcλ
ð
ÞW
!
"
· f
ρf
ρg
!
,
where f ρf =ρg
□
□
=
ρf =ρg
□
□−0:52
for
ρf =ρg
□
□
< 360;
0:047
for
ρf =ρg
□
□
> 360:
>
<
>
:
This
relationship
is
obtained
in
the
range
of
p=pcr = 9□10−4 −0:95;
ρcλ
ð
Þf = ρcλ
ð
ÞW = 6:7□10−5 −4:9; and ρf =ρg = 1:9−7550.
A detailed overview of the temperature Tmin is available in Bernardin and Mudawar
(1999), which is excerpted in Table 7.5. It shows the diversity of mechanisms related
to the Leidenfrost phenomena.

<!-- page 430 (PDF 74) -->
Table 7.5 Possible mechanisms of the Leidenfrost phenomenon (Bernardin and Mudawar, 1999)
Model
Pictorial description
Relevant correlations
Hydrodynamic instability
ld
Most dangerous wavelength: λd = 2π
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
3σf
g ρf −ρg
□
□
v
u
u
t
Metastable liquid mechanical
stability
P
Isotherm
Saturation
curve
Vapor
spinodal
Unstable
region
Liquid spinodal
v
Mechanistic stability condition
∂p
∂ν
□
(
T
= 0
Spinoidal or liquid superheat limit: (using van der Waals equations)
p/pcr≪1 Thn=0.844 Tcr
Metastable liquid-kinetic
stability
Homogeneous nucleation limit
J = Nf
3σ
πm
□
(0:5
exp
−16πσ3
3kbTf ηρsatTf −pf
□2
(
)
;
η = exp
νf ρf −ρsat Tf
□
□
RTf
(
)
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 431 (PDF 75) -->
Thermomechanical effect
Liquid
flow
Nucleate
boiling
Incipience
CHF
LFP
Transition
boiling
Film
boiling
Energy balance for Section D
hg Tg
□
□
−hf Tleid
ð
Þ = 0:5 νg Tg
□
□
−νf Tleid
ð
Þ
□ psat Tleid
ð
Þ−psat Tg
□
□
Wettability-contact angle
Ts
q
Contact angle temperature dependence
cos θ=1+C(Tc−T)m
Wettability-surface adsorption
Continuous
monolayer
Discontinuous
monolayer
Monolayer molecular surface coverage temperature dependence
Г
Г0
=
exp
Q0
RTi
□
(
2πMRT
ð
Þ0:5Г 0
NaPr0
"
+ exp
Q0
RTi
□
(

<!-- page 432 (PDF 76) -->
Two theories have been proposed for the analytical prediction of the minimum film
boiling temperature. One theory says that the minimum temperature is a thermodynamic
property of the fluid (i.e., maximum liquid temperature) and thus is primarily
a function of pressure. The other theory suggests that rewetting commences due to
hydrodynamic instabilities which depend on the velocities, densities, and viscosities
of both phases as well as the surface tension at the liquid-vapor interface (IAEA
TECDOC, 1203, 2001).
Duringfast transitions,where insufficient time is available to fully develop the hydrodynamic
forces, rewetting is expected to be thermodynamically controlled, while for
low flows andlow pressures,wheresufficienttimeisavailableandthevolumetricexpansion
of the fluid near the wall is large, rewetting is more likely to be hydrodynamically
controlled. Once rewetting has occurred locally, the rewetting front can then propagate
at a rate which is primarily controlled by axial conduction. These theories can be modified
to include the thermal properties of the surface (IAEA TECDOC, 1203, 2001).

#### 7.5.4.2 Leidenfrost temperature

The evaporation of superheated droplets on the surface depends on the temperature.
Thus, a drop of the radius of 2 mm on the brass plate evaporates over the time:
at□100°C—35 s; at□170°C—a few seconds (the first critical temperature);
at□240°C—130 s (the second critical temperature—the temperature of the Leidenfrost);
at□500°C—60 s (spheroidal state).
In the last case, the drop is separated from the heated surface and floating on the
superheated vapor layer; for estimates the following can be used:
Tmin = 27=32
ð
ÞTcr,
where Tcr—thermodynamic critical temperature in K (see Table 7.6).
Table 7.6 Leidenfrost temperature TLFP for saturated fluids that are
in contact with the smooth clean surfaces at atmospheric pressure
(Soloviev, 1998)
Liquid
Test conditions
TLFP (K)
Sodium
Tantalum sphere in bulk
Potassium
Tantalum plate and drop
Stainless steel plates in a large volume
Mercury
Tantalum plate and drop
Copper plate and drop
Water
Aluminum and drop
Platinum wire in a bulk water
Nitrogen
Sphere of the copper in a bulk
Sphere of Teflon in a bulk
Thermal Hydraulics in Water-Cooled Nuclear Reactors
