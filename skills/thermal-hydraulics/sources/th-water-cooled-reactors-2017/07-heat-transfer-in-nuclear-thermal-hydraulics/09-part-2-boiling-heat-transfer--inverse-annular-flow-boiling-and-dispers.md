# Part 2: Boiling Heat Transfer — Convective boiling heat transfer in channels — Inverse-annular flow boiling and dispersed-annular flow film boiling
<!-- source PDF pages 106-113 -->

<!-- page 462 (PDF 106) -->
(downstream of the film dry-out point) where the liquid droplets are distributed in the
vapor core flow.
Structure of two-phase flow in the postminimum heat flux region is stable and most
of the liquid phase decays into droplets toward the downstream region and the
flow becomes dispersed which is a dominant flow regime in the heat transfer crisis.
Higher surface temperature in this zone is due to the fact that the superheated vapor is
primarily in contact with the wall.

### 7.8.7 Inverse-annular flow boiling and dispersed-annular flow film boiling

There are few reliable guidelines for calculation of the inverse-annular mode heat
transfers. A large number of semiempirical models have been developed, most of
which are very complicated. It is difficult to check many of the parameters used in
these models match the final results from the individual experimental data and their
validity of generalization has not been yet demonstrated. Furthermore, the experimental
data do not always provide sufficient accuracy, which are adopted with the
background of the models often facing a difficulty for justification.
The heat transfer in the film boiling of the subcooled liquid region is made up of
three mechanisms:
(1) convective heat transfer from the heated surface by the vapor flow convection in the vapor
film along the surface;
(2) conduction and laminar convection heat transfer from the vapor film to the vapor-liquid
interface; and
(3) thermal radiation.
The heat transfer in the dispersed-annular flow mode, which appears most often in the
superheated zone of high steam quality (x>0.2), generally comprises of the following
components:
(1) convective heat transfer from the wall to the bulk vapor flow;
(2) conduction heat transfer from the wall to the liquid droplets that are in contact with the
thermal boundary layer (dry contact) and that impact the wetted (or not wetted) wall;
(3) radiation heat transfer from the wall to both bulk vapor and liquid droplets;
(4) convective heat transfer by the bulk vapor flow to the suspended droplets in the vapor core.
A majority of the heat is transported by convection. The presence of the superheated
vapor and the liquid droplets at saturation temperature TS, results in the actual vapor
flow quality xa being lower than the equilibrium vapor quality x. Let’s define a degree
of thermodynamic nonequilibrium by the ratio of these two values xa/x=n (□1 in
the dispersed-annular regime). Then the mean temperature and enthalpy of the
superheated vapor in this case is expressed by the relations:
Tv = TS + Δhfg
cp
1−n
ð
Þ
n
= TS + Δhfg
cp
· x−xa
xa
;
⟨hv = hg + Δhfg
1−n
ð
Þ
n
= hg + Δhfg
x−xa
xa
:
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 463 (PDF 107) -->
When the mass flux of the mixture is higher than 1000 kg/(m2 s), the thermodynamic
nonequilibrium will be small and n	1. The nature of the temperature distribution
and the actual vapor quality in the crisis zone is shown in Fig. 7.60. The crisis zone
could be defined as the region where the actual vapor quality x is higher than the
critical steam quality xcr at which departure from nucleate boiling (DNB) would
occur. Heat transfer coefficient is usually referred to as the temperature difference
(Tw −TS).

#### 7.8.7.1 Heat transfer in a dispersed droplets-vapor mixture flow

When the dispersed-annular flow structure changes to the dispersed droplets-vapor
mixture flow in channels, heat transfer can be calculated by taking into account thermal
nonequilibrium of the flow (Sergeev et al., 1985; Sergeev, 2002). There, the
two-phase flow in the crisis region is treated by a homogeneous mixture of superheated
vapor and liquid droplets. It is considered that the heat is transferred by convection
from the heating surface to the vapor, and from the vapor to the droplets
(droplets evaporating on the wall surface; and the radiation heat transfer is neglected).
The heat transfer coefficient from the wall to the vapor and the critical steam quality
(xcr) are assumed to be known.
The method can be applied for flows in pipes, annular channels, and for nuclear fuel
rod bundles with spacer grids with their hydraulic diameter would be 4–20 mm, and
p=1.1–19.6 MPa, ρw = 70−2000kg/(m2 s), q□1 MW/m2, Tw −TS □500°C and
x > xcr □ 0:1.
The variation of actual vapor quality xa in the post-CHF zone in the channel could
be determined by the following differential equation:
Tw
Tw
Tv
T
x
xcr
1.0
x
xe
xa
Fig. 7.60 Temperature behaviors to
the vapor quality and the actual
vapor quality in the crisis zone
(q=const and x>xcr): — thermally
nonequilibrium flow; xa is the actual
quality; - - - thermally equilibrium
flow; xe is the equilibrium quality.
Tv and Tw are the vapor-phase and
wall temperatures.

<!-- page 464 (PDF 108) -->
dxa
dxe
= Cm λg
σρf
PW ρw
ð
Þ2
X
j qPh
ð
Þj
xa 1−xa
ð
Þ xe −xa
xa
□
(n
,
(7.158)
where xe is the thermodynamically equilibrium mass quality; C is an empirical
constant (C=1.5), PW and Ph are the wetting and heating perimeters, respectively,
in m; q is the local heat flux on the jth heat transfer surface (W/m2); ρw is the mass
flux (kg/m2 s); parameters m and n depend on pressure:
for
p<6 MPa:
m = 1149:1−28:2534p + 0:995p2 −1:8421□10−2p3 + 1213□10−4p4, °C;
n = 1:0003 + 4:3389□10−3p−2:5466□10−5p2;
for
p□6 MPa:
m = 864:664−4:0128p, °C;
n = 1:0861 + 8:6654□10−4p + 1:0772□10−5p2,
with the pressure p in bars.
For flows in pipes and rod bundles, C=1.5. For annular channels with one-sided
heating, C=3. For annular channels with two-sided heating, the heat flux to the
vapor at the second surface is assumed to be zero and the constant C=3. In the
downstream of the crisis section, C is assumed to be equal 1.5 (Sergeev et al.,
1985). The “actual” vapor quality distribution xa will be obtained by integration
of Eq. (7.158) for the heat-transfer crisis section, which depends on xcr and
Tv = TS.
For n=1 (highly superheated vapor flows, xa=xe), Eq. (7.158) has an analytical
solution:
xa = 1−
exp −ξ2=2
□
□
B + Φ ξ
ð Þ
ffiffiffiffiffiffiffiffiffiffi
πA=2
p
,
(7.159)
where A = Cmλg
σρf
ρw
ð
Þ2P
X
iqi zð ÞPTi
, B is the constant determined from the condition
x=xcr, ξ =
ffiffiffi
A
p
x−1
ð
Þ, and Φ(ξ) is the probability integral. Eq. (7.159) could be used
for testing the numerical integration scheme of Eq. (7.158).

#### 7.8.7.2 Procedure for calculating heat transfer in the crisis zone

–
by solving the differential equation (7.158) or by the formula (7.159), the actual vapor
quality xa is obtained at a given vapor equilibrium quality xe;
–
then with xe and xa, the enthalpy of superheated vapor is given by ⟨hv = hg + Δhfg
xe −xa
xa
in
a specified section of the channel;
–
with the given enthalpy of superheated vapor and the saturation enthalpy from the steam
table, Tv = TS + m
xe
xa −1
n
determines the superheated steam temperature;
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 465 (PDF 109) -->
–
The wall temperature on the ith heat-transfer surface is calculated by: TW = Tv + qi
α, where α
is the convective heat transfer coefficient to the superheated vapor; Tv is the temperature of
the superheated vapor (K); TW the wall temperature (K).
Thermal properties refer to those at the superheated vapor temperature Tv.

#### 7.8.7.3 Annular channels

Heat transfer coefficient for annular flow channels is obtained from the following
equations (Handbook PTM.24.031.05-72, 1974):
–
when the inner wall of the annular channel is heated:
Nu1 = 0:86Nu d1=d2
ð
Þ−0:16;
–
when the outer wall of the annular channel is heated:
Nu2 = Nu 1−0:14 d1=d2
ð
Þ0:6
h
i
;
–
when the both inner and outer walls are heated:
For the inner wall
Nu*
1 = Nu1= 1 + Nu1θ1 q2=q1
ð
Þ
½
□;
For the outer wall
Nu*
2 = Nu2= 1 + Nu2θ2 q1=q2
ð
Þ
½
□,
where
Nu = 0:023Re0,8Pr0,4 Tv=Tw
□0:5;
θ1 = 32 0:16 d1=d2
ð
Þ
½
□Re−0:88;
θ2 = θ1 · d1=d2;
dh = d2 −d1; Nu = αdh
λ ; Re = ρw
ð
Þxdh
μ
; Pr = ν
α; Nu1 = α1dh
λ ; Nu2 = α2dh
λ . The subscripts 1
and 2 of the thermal properties at Tv refer to the inner and outer walls of the annular channel,
respectively.

#### 7.8.7.4 The rod bundles

Heat transfer coefficient can be represented by (Subbotin et al., 1975):
Nu = CRe0:8Pr0:4,
(7.160)
where C = 0:0165 + 0:02 1− 0:91
P=D
ð
Þ2
"
P
D
□ (0:15
, P/D is the rod pitch to diameter ratio.

#### 7.8.7.5 Heat transfer at the entrance region of a crisis zone

Heat transfer to the superheated vapor flow in the region from the entrance to downstream
of the crisis zone, where the thermal boundary layer is formed approximately
for the length of 15 hydraulic diameters, is calculated by:

<!-- page 466 (PDF 110) -->
Nu = 1:38
dh
Δz
□
(0:12
Nu0,
(7.161)
where Nu0 is the Nusselt number for steady-state heat transfer, and Δz
is the distance from the cross section of the heat-transfer crisis (Isachenko
et al., 1981).

#### 7.8.7.6 Influences of spacer elements

In this section, integration of Eq. (7.158) will be carried out with a new boundary
condition given by Eq. (7.162), which takes into account an increase in the vapor
quality due to an additional amount of evaporation resulting from the interactions
of the flow with the spacer elements (Sergeev et al., 1990):
Δx = 1−x
ð
Þk ΔA=A
ð
Þ,
(7.162)
where (ΔA/A) is an extent of the flow channel area blockage by the spacer, k is the
multiplication factor that depends on the geometry of the spacer and its mode of
settings (0<k<1). For simple spacer elements without swirl enhancing tabs, the
factor k could be given by:
k = 1−ρw=3000
ð
Þ□0:15, for ρw □ 1500kg= m2s
□
□
:
If the calculated vapor quality in the spacer element section by Eq. (7.162) exceeds the
value of the relative enthalpy (quality) at the same location, it is considered that the
difference xa −x
ð
Þ is due to the evaporation of the liquid film, which is formed as a
result of flow interaction with the spacer and covers the heated wall surface on the
segment length:
Δz = G · Δhfg · xa −х
ð
Þ=
X
i qPТi
ð
Þ,
(7.163)
In this spacer region, the heat transfer is calculated using the formulas for boiling, after
which the procedure described above with the solution of Eq. (7.158) is repeated,
starting from the section located at a distance Δz from the spacer, where the flow
is considered to be at thermally equilibrium.
The following takes into account the single-phase flow heat transfer enhancement
by the spacers, suggested by Yao et al. (1982):
Nu=Nu0 = 1 + 5:55 · ΔA=A
ð
Þ2 · e−0:13z=dh,
(7.164)
where Nu0 is Nusselt number in the absence of the spacer; Nu is Nusselt number in the
presence of the spacer; z is the distance from the spacer; and dh is the equivalent
hydraulic diameter of the flow channel.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 467 (PDF 111) -->
#### 7.8.7.7 Consideration of radiation

The total heat transfer by vapor flow convection and radiation to the droplets is
expressed by Sergeev et al. (1990):
qi = α Tw −Tv
□
□
+ σε T4
wi −T4
S
□
□
,
(7.165)
where σ is Boltzmann constant, and ε the reduced emissivity of the blackbody-droplet
system.
The wall temperature is obtained following the above procedure of solving
Eqs. (7.158), (7.165). For the given wall temperature, reduced heat transfer coefficient
is calculated by αi = qi= Twi −TS
ð
Þ.
The unit of various parameters used in the formulas are in the following:
A—W/(m2 K); T—in °C; q—W/m2; p—MPa; h—J/kg; ρw—kg/(m2 s); Δhfg—J/kg;
μ—N s/m2; dh=(d2−d1)—m; d1, d2—m; λ—W/(m K); σ—N/m; ρ—kg/m3.
Range of applicability of the method is as follows:
p=1.1–19.6 MPa;
Tw −Tf □500°C;
ρw=70–2000 kg/(m2 s);
q□1 MW/m2;
xb > xcr □ 0:1; dh=4–20 mm.
Maximum accuracy of calculating α is σ □25%. Mean accuracy for circular tubes with
the uniform and cosine shape heat fluxes is σ □10%.

#### 7.8.7.8 Simplified calculation method

Heat transfer is calculated in circular tubes and annuli by the following formula
(Miropolskii, 1975):
Nug = 0:023
RegPrgW x + ρg
ρf
1−x
ð
Þ
"
(
)0:8
· Y,
where Y = 1−0:1 ρf =ρg −1
□
□0:4
1−x
ð
Þ0:4; Nug = αd=λg, Reg = Gd=μg. The range of
application of the formula is p=4–20 MPa; ρw=1000–2000 kg/(m2 s). For a wider
range of parameters, you may use the formula by Groeneveld (1973):
Nug = 0:00327
Reg x + ρg
ρf
1−x
ð
Þ
"
(
)0:9
PrgW
□
□1:32Y−1:5,
(7.166)
The range of application of the formula given in Table 7.11.
At lower mass flux than 1000 kg/(m2 s), the superheated vapor flow is characterized
by a significant thermodynamic nonequilibrium in the presence of liquid droplets
in the vapor flow stream. In this case, the heat transfer coefficient refers to the

<!-- page 468 (PDF 112) -->
temperature difference (Tw −Tv) instead of (Tw −TS), as is commonly practiced
for thermodynamic equilibrium flow. As a result, Tw = Tv + q=α. The superheat is
calculated from a steam table, knowing ⟨hv:
⟨hv = hg + Δhfg x−xa
ð
Þ=xa,
(7.167)
where x is the equilibrium vapor quality; xa—true vapor mass quality; Δhfg—heat of
vaporization; hg—saturation enthalpy of vapor.

#### 7.8.7.9 Heat transfer in the superheated zone of the helical coil pipes

The helical coil heat exchanger has a number of different features as compared
with a straight tube heat exchangers. For instance, the flow in the helical coil tube
shows the influence of centrifugal force and the heat transfer crisis occurs not uniformly
along the perimeter of the tube. There exists a large variation of the heat
transfer coefficient around the perimeter and, as a result, large temperature gradients
. Nonequilibrium effects at a crisis zone are less than those of the straight
tubes/pipes of identical parameters. With d the tube inner diameter and D the coil
diameter, the calculation formula takes the form (in Handbook, 1983) for
d/D□0.015:
Nu = αd=λg = CRe0:8
m Pr0:8
w z □25%,
where C=0.017 for helical coil tubes; C=0.017(1+3.18d/D) for pipes bent at
90 degrees; z = 1 + y 1−x
ð
Þ, y = 0:5 ρf =ρg −1
□
□0:8
for ρf/ρg□480; y=70 for
480<ρf/ρg<1300. For d/D<0.015
Nu = 0:023Re0:8
m Pr0:8
w
1−0:1
ρf
ρg
−1
!0:4
1−x
ð
Þ0:4
5:
Table 7.11 The range of application of the formula (7.166) for pipes
and annular channels
Parameters
Circular
tube
Annular
channel
Parameters
Circular
tube
Annular
channel
d (mm)
2.5–25
1.5–6.3
q (W/cm2)
12–210
45–225
p (MPa)
6.8–22
3.4–10
Y
0.706–0.975
0.610–0.953
ρw (kg/
(m2 s))
400–5300
800–4100
Prgw
0.88–2.21
0.91–1.22
x
0.1–0.9
0.1–0.9
Nug
95–1700
160–640
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 469 (PDF 113) -->
The formula is based on the experimental data obtained in the steam-water mixture in
the range of Rem=5.4□103 to 4□105; d/D=0.007–0.14; ρw=100–2000 kg/(m2 s);
p=0.1–21.5 MPa; q=0.1–1.1 MW/m2; x=0–1.0.
Another formula for calculating heat transfer is given by:
Nu = Nu0 1 + 0:1
ρf
ρg
−1
!0:4
1−x
ð
Þ
5 x +
ρf
ρg
!
1−x
ð
Þ
"
#0:8
:
There Nu0 is the Nusselt number for a single-phase flow in the coiled pipes.

#### 7.8.7.10 Heat transfer of superheated steam

The magnitude of heat transfer rate to the superheated vapor as well as to the gases is
significantly lower than that to liquids. Therefore, the temperature difference Tw −Tf
becomes significant, which solicits the need to consider the heat transfer coefficients
applicable to a wide spectrum of the physical properties of the flow section.
The calculation of the average heat transfer rate (for l/d□50) in the vapor flow
away from the critical region can be carried out according to the formulae, which take
into account the variation of the physical properties of simplices ρw/ρf or Tv=Tw:
For q□0.5 MW/m2 (Eq. 7.168, Miropolskii, 1975; Eq. 7.169, Lel’chuk and
Elfimov, 1968)
Nu = 0:028Re0:8Pr0:4 ρW=ρv
ð
Þ1:15;
(7.168)
Nu = 0:023Re0:8Pr0:4 Tv=TW
□
□0:5 □10%,
(7.169)
where all the properties are selected on the average temperature basis of the superheated
vapor Tv, Re = ρw
ð
Þxd
μ
, Pr = μcp
λ . These equations are applicable for
ρw=300–1000 kg/(m2 s); p=4–20 MPa. For q>0.5 MW/m2, the heat transfer to
the vapor is obtained based on the arithmetic mean of the results from the last two
Eqs. (7.168), (7.169).
The local heat transfer coefficients for pipes can be found in Petukhov and
Kurganov (1974) and Petukhov (1987):
Nu
Nu0
= exp
−K 0:013f
x=d
□
□
+ 1:18K1:25□10−4 x=d
□
□2
1 + 10−4 x=d
□
□2
"
(
)
,
(7.170)
Here x is the distance from the entrance of test section; K =
qd
λf TNu0
= Tw −Tf
Tf
is the
coefficient characterizing the temperature variation in the flow when the heat flux is
changed.
