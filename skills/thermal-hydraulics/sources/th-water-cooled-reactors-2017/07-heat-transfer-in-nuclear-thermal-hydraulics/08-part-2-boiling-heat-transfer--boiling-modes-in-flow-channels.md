# Part 2: Boiling Heat Transfer — Convective boiling heat transfer in channels — Boiling modes in flow channels … Heat transfer in film boiling, and superheated vapor flow in channels
<!-- source PDF pages 92-105 -->

<!-- page 448 (PDF 92) -->
p—pressure; b =
TS −Te
2 1−ρg=ρf
□
□ is the coefficient taking into account the effect of pressure
and subcooling; Φ =
we=0:61
ð
Þ0:47 for we □ 0:61m=s
1:0
for we < 0:61m=s
□
is the coefficient reflecting the
effectsofthedetachmentspeedanddiameterd;we—velocityofthewater;F1 = n πd4=4
□
□
isthe
fraction of the surface projected by the vapor bubbles; n—number of vapor bubbles on the unit
surface: n = 1
d2
2σTS
TW −TS
ð
ÞρgΔhfg
"
#−4:4
f ρ*
ð
Þ, where ρ* = ρf −ρg
□
□
=ρg = ρf =ρg
□
□
−1; Δhfg
is
the
heat
of
vaporization;
f ρ*
ð
Þ = 2:157□10−7 ρ*
ð
Þ−3:2 1 + 0:0049ρ*
ð
Þ4:13;
and
a =
q−αf Tw −Te
ð
Þ
□1=2λ
2c1=3Δhfg
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
πλf = ρf cpf
□
□
q
ρg
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
λWρWcpW
λf ρf cpf
s
; c = Δhfgμf cp=0:013Δhfg · Pr1:7
□3
σ=Δρg
ð
Þ0:5
.
3. The amount of heat used for the evaporation:
Qe = nf π
6d3
□
□
Δhfgρg:
(7.145)
4. The amount of heat being carried by turbulent flow natural convection:
Qc = St · ρf cpf we Tw −Tf
□
□
1−F1
ð
Þ:
(7.146)
From experiment Tw=f(τ)—the transient surface temperature measurement enables
calculation of the heat transfer coefficient α=f(τ), due to α □ ∂ Tw −Tf
□
□
∂τ
. Qualitatively
, a variation of the heat transfer coefficient is shown in Fig. 7.51 (Gilles
et al., 2002).

## 7.8 Convective boiling heat transfer in channels

### 7.8.1 Boiling modes in flow channels

Different types of flow regimes and modes of heat transfer in a vertical heated tube are
shown in Figs. 7.52 and 7.53. Fig. 7.52 shows the flow conditions and heat transfer
modes in a uniformly heated tube (q=const). The figure has been cited in many
reports and books on two-phase flow and heat transfer (e.g., Wallis, 1972;
Mandhane et al., 1974; Butterworth and Hewitt, 1977), which was adopted originally
from Tong (1965). Fig. 7.52 is from its second edition by Tong and Tang (1997), and is
self-explanatory, as it contains all the necessary information in the figure.
Fig. 7.53 shows a change in the flow patterns of two-phase flow in a long pipe with
increasing heat flux from left to right, with the fluid inlet temperature and mass
flow rate and the system pressure constant. In the single-phase flow region (region
1), while the liquid on the wall surface may be heated up to the saturation temperature,
the wall temperature is still below the value required for vaporization in the presence
of the convective heat transfer. Just downstream of the region 1, the fluid at the wall
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 449 (PDF 93) -->
becomes superheated such that evaporation occurs in the micro cavity centers,
although the bulk flow is still subcooled, i.e., below the saturation temperature. This
is an area of nucleate boiling of the subcooled liquid (2a). The difference between the
saturation temperature and the mass-average temperature of the liquid is called subcooling
TS −Tf = ΔTsub. The upper boundary of the region 2a in Fig. 7.53 corresponds
to the vapor quality x=0. This portion of the liquid is heated to the saturation temperature
so that the average liquid-vapor flow enthalpy is equal to that of saturated
liquid (hf,sat). In the nucleate boiling of the saturated liquid region (2b) as well as
in the subcooled boiling region, equilibrium steam quality (or relative enthalpy) at
a distance z is determined by the heat balance x zð Þ = h zð Þ−hf,sat
=Δhfg where
h(z) is the mixture enthalpy and Δhfg is the latent heat. With this definition, it may
have a negative or positive value.
With increasing steam quality, plug or slug flow regime prevails (region 2c). The
upper boundary of this region is in transition to the dispersed-annular flow regime
(region 3) where there is a change in the mechanism of heat transfer. There the process
of boiling is mostly replaced by evaporation. While the boiling can be observed within
a thick liquid film, the bubble generation in the thin liquid film is usually suppressed
and the process of heat transfer cannot be referred to as boiling. The heat is transferred
by the convection from the wall to the interface between liquid and the vapor core
where evaporation takes place. The upper boundary of the region 3 in Fig. 7.53 corresponds
to the complete evaporation of the liquid film and there dominates a
a
Tw,°C
t, s
t, s
Fig. 7.51 Dependence of Tw(τ) and α(τ): 1—film boiling mode; 2—bubbly mode;
3—convective cooling mode.

<!-- page 450 (PDF 94) -->
“Dryout”
Fluid temp
Wall and fluid
temp variation
Flow
patterns
Heat transfer
regions
Vapor
core temp
Wall
temp
Drop
flow
 Singlephase

vapor
Convective
heat transfer
to vapor
Liquid deficient
region
Fluid temp
Subcooled boiling
Slug
flow
Bubbly
flow
Annular
flow
Liquid
core temp
Wall temp
Sat temp
Singlephase

liquid
Convective
heat transfer
to liquid
Saturated
nucleate
boiling
Forced
convective heat
transfer thro
liquid flim
Annular
flow with
entrainment
Fluid
temp
x=0
x=1
H
G
E
F
D
A
B
C
Fig. 7.52 Flow patterns and modes of heat exchange (q=const) (Tong and Tang, 1997).
Regions of heat transfer in convective boiling in a heated channel with constant heat flux; the
regions A–H are further described in Fig. 7.54.
From Ahmada, M., et al., 2013. Phenomenological modeling of critical heat flux: the GRAMP
code and its validation. Nucl. Eng. Des. 254, 280–290.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 451 (PDF 95) -->
dispersed flow mode with gradual evaporation of droplets in the superheated steam
(region 4), which shifts into the single-phase vapor flow convection mode—region 5.
At the location of the film dry-out, the heat transfer coefficient drops sharply where
with the high heat flux the wall surface temperature may reach unacceptable values
(burnout, crisis). This heat flux is called critical heat flux (qcr). The line between the
areas 3 and 4 corresponds to the critical heat flux associated with the dry-out of the
liquid film.
When q>qcr, the mechanism of the heat transfer varies depending on the boiling
regime, i.e., either DNB, the formation of a conglomerate of bubbles of steam
shielding the surface of the bulk liquid from the heated wall, or the boiling transition
(BT), the liquid film dry-out. Film boiling under the forced convection mode is basically
similar to that observed in the pool boiling. Heated surface is covered with a
vapor film that is of low heat conduction through which the heat must be transferred.
Dependency of the two-phase forced convection heat transfer regimes on the quality
(vertical axis) and heat flux (horizontal axis) is shown in Fig. 7.54 (taken from
Collier and Thome, 1980).
It should be borne in mind that, in Fig. 7.54, the equilibrium quality x reflects only
qualitatively the border areas. Therefore, when x>1 (area 6) a thermodynamically
nonequilibrium vapor flow is possible in the presence of liquid droplets. Then the
boundary between the regions 9 and 6 moves to the right.
Since the void fraction (φ) in the flow determines the flow and heat transfer modes,
it is advisable to consider the actual steam quality that takes into account the nature of
Fig. 7.53 Different flow patterns of two-phase flow in a long pipe (constant: pressure, mass
flow rate, inlet enthalpy) by Hewitt and Hall Taylor (1972): 1—single-phase liquid flow;
2—bubbly, slug; 3—annular-dispersed; 4—mist; 5—single-phase vapor flow.

<!-- page 452 (PDF 96) -->
the change in φ along the channel (for example, q=const), instead of the equilibrium
steam quality xe, as depicted in Fig. 7.55.
First, vapor bubbles appear at the location “ib.” Moving through, or migrating away
from the thin boundary layer near the wall surface, the vapor bubbles condense in a
bulk of highly subcooled liquid. Here, the void fraction is low, because the growth of
bubble layer is limited by the high level subcooling. As a result, the subcooling
decreases in the flow core and gradually attains the conditions under which the rate
of vapor generation exceeds that of vapor condensation in the stream. From this point
the void fraction begins to increase rapidly, which is considered the beginning of the
vapor generation—nvg (net vapor generation).
The equilibrium quality can be zero (xe=0) in the nucleate boiling (beginning)
region even with significantly high values of the void fraction (φ≫0). Thus, this
mode is under thermodynamically nonequilibrium condition, i.e., where the flow contains
a significant amount of vapor (by volume) in the subcooled liquid as a whole.
A simple calculation assumes that the undeveloped surface boiling starts in the section
in which the surface temperature is saturation temperature TS. Then a magnitude of the
relative enthalpy xib = Δh=Δhfg (i.e., quality) can be evaluated by the convective heat
transfer coefficients αc:
[A]
Single-phase
flowRegion A
Subcooled
nucleate
boiling
Region B [B]
Regions
C and D
Saturated
nucleate
boiling
Two-phase
FC heat transfer
Regions E and F
Liquid
deficient
Region G
Superheated
vapor forced
convection
Region H
Subcooled
Saturated
Superheat
Saturated
film boiling
q
[D]
[C]
x = 0
x = 1
x
Subcooled
film boiling
Fig. 7.54 Heat transfer regions in forced convection; Regions A—H in Fig. 7.52.
1—Single-phase fluid flow; 2—subcooled nucleate boiling (Tf<Ts); 3—saturated nucleate
boiling Tf=Ts; 4—two-phase forced convection heat transfer; 5—liquid deficient region
(degraded heat transfer); 6—superheated vapor forced convection; 7—subcooled film boiling
(Tf<Ts); 8—saturated film boiling Tf=Ts; 9—liquid deficient and heat transfer crisis;
[A]—subcooled CHF by DNB; [B]—saturated CHF by DNB (Tf=Ts); [C]—typical burnout
locus; [D]—CHF by film dry-out.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 453 (PDF 97) -->
–
For longitudinal flow inside and outside a tube or pipe, xib = Δh=Δhfg = −qcp= αcΔhfg
□
□
since Δh = −q cp=αc
□
□
, where q is the heat flux, cp is the heat capacity, αc is calculated
on the basis of the formulas for the single-phase convective heat transfer, Δhfg the latent
heat; and
–
For transverse flow across tube bundles, xib = −6:17Re0:18qcp= αcΔhfg
□
□
, where Reynolds
number (Re) is calculated from the velocity at the narrow gap; αc is the convective heat
transfer coefficient for cross-flows in the bundle.
Recently proposed method of calculating the heat transfer in the boiling channels
consists of the following three modes (Kandlikar, 1990, 1991, 1998):
–
Partial (or undeveloped) boiling at qualities xib < x < xdnb (region 2 in Fig. 7.55) where xib
corresponds to the quality at beginning of nucleate boiling and xdnb the developed nucleate
boiling;
–
Fully developed boiling at x > xdnb (region 3 in Fig. 7.55);
–
Mode of a high steam quality for x > xnvg, starting from the point of beginning net vapor
generation (xnvg) where
Distance from the inlet (z)
Flow rw
Uniform heat flux q
ib
nvg
dnb
Quality (x)
xe=xa
zEq
zdnb
zxe=0
zib
xa
xe
xe=0
x=0
Fig. 7.55 Vapor quality, flow conditions and heat transfer. xa—actual vapor quality;
xe—equilibrium quality; 1—single-phase flow forced convection; 2—nucleate boiling
(developing); 3—developed nucleate boiling; 4—subcooled boiling; 5—saturated boiling
(thermally equilibrium for z > zEQ). ib—incipient boiling initiation; nvg—net vapor generation;
dnb—developed nucleate boiling; zxe =0—distance from the heated section inlet to the point
xe = 0 at which saturated nucleate boiling to begin, but the liquid is still below the saturation
temperature. zEq—distance to the point of xa = xe where all the liquid is at the saturation
temperature.
FiguremodifiedbasedonCollier,J.G.,1981.ConvectiveBoilingandCondensation.McGraw-Hill,
New York.

<!-- page 454 (PDF 98) -->
xnvg = −0:0022 qd=Δhfgρf λf
□
□
BoRePrf for RePrf < 7□104;
xnvg = −154Bo
for RePrf > 7□104:
Here, Bo = q= Δhfgw
□
□
; d is the pipe diameter; Re and Prf are for liquid-phase. Points
“dnb (developed nucleate boiling)” and “nvg (net vapor generation)” are sufficiently
close to each other. While these techniques are not yet widely used, the logic and
additional studies may allow us to abandon the simplified representations.

### 7.8.2 Onset of subcooled nucleate boiling

The flow regimes and temperature change along the inner surface of a circular pipe for
a uniform heat flux distribution were shown in Fig. 7.52. The mean liquid-phase temperature
varies linearly along the heated length in the convective region away from the
inlet according to the heat balance. Also, the wall temperature along the inner surface
of the pipe varies linearly: Tw zð Þ = Tf + q=αc where αc is the single-phase flow heat
transfer coefficient. At a certain wall superheating of Tw zð Þ−TS = ΔTob, the water
begins to boil on the surface. The subscript ob designates the onset of nucleate boiling.
The magnitude of the wall superheating could be found by the following empirical
relation in Petukhov and Shilov (1987):
Tw −TS = 22:65q0:5 exp −p=8:7
ð
Þ,
(7.147)
where q is in MW/m2 and p in MPa. The range of application of the formula (7.147)
is:
d=3.6–5.7 mm;
p=0.7–17 MPa;
Tf =115–340°C;
G=11–104 kg/(m2 s);
q<12 MW/m2.
In the case of flows in narrow annular channels, the onset of surface boiling occurs
with the wall-superheat determined by the formula:
Tw −TS = 20:7qp0:43d0:23
e
=w0:
(7.148)
Here de is the equivalent hydraulic diameter (mm); w0 the flow velocity (m/s); q is the
heat flux (MW/m2); p the pressure (MPa). Onset of the surface boiling is related to the
flow enthalpy at onset of boiling hob, which is determined from the equation (Tarasova
and Orlov, 1964):
hf −hob = 0:3q1:1d0:2
e G−0:9 ρg=ρf
□
□0:3
□15%,
(7.149)
where h is the enthalpy (kJ/kg); q the heat flux (MW/m2); de the equivalent hydraulic
diameterofthechannel(m);Gisthemassflowrate(kg/m2/s).Theformulaisapplicable
to the range: p=4.9–19.6 MPa; G=1300–11,000 kg/(m2 s); q=0.43–1.3 MW/m2;
de=2.9–6.3 mm.
The enthalpy at the beginning of the surface boiling can be calculated through the
vapor quality (xob<0):
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 455 (PDF 99) -->
hf −hob = −Δhfgxob,
where
xob = −0:49Re0:7
1 Re−0:3
π0:15;
Re1 = qdσ=Δhfgμf ;
Re2 = Gdσ=μf
with
dσ≡
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
σ=g ρf −ρg
□
□
r
; and π = p=pcrt where pcrt is the critical pressure. In general,
the subcooling at the boiling initiation can be found approximately by the equation
ΔTS = TS −Tf = q 1=αc −1=αb
ð
Þ, where αc and αb are the heat transfer coefficients
in single-phase flow convection and developed boiling, respectively. In the presence
of deposits on the surface having the thermal resistance R (m2 K/W), the value of
subcooling at the start of boiling will be equal to ΔTS = q 1=αc −1=αb + R
ð
Þ.

### 7.8.3 Subcooled boiling, developing region

Heat transfer in the channels under the conditions of undeveloped subcooled boiling of
water, corresponding to the region 2 in Fig. 7.55, is calculated by the formula:
α
α0
=
1 + α0
αc
−TS −Tf
q
□
(
−3=2
(
)2=3
where α0 is calculated by the formulae given in Section 7.6 for pool boiling in a large
volume; αc is the single-phase flow convective heat transfer coefficient.
7.8.3.1
Features of subcooled boiling at low pressures
(0.1–1.0 MPa) (Wadekar, 1990)
Subcooled boiling at low pressures is characterized by large specific vapor volumes
and, hence, high velocities. In this situation, the saturation temperature decreases
toward the downstream region of the channel in accordance to the decrease in pressure
; and in the stabilized convective heat transfer section (with q=const), it increases
in accordance to the increase in the average bulk liquid temperature.
Fig. 7.56A shows axial temperature profile for the onset of boiling of flows with the
subcooled bulk liquid. In this figure, after the surface temperature reaching the desired
superheat (point A), the subcooled liquid water starts boiling and the surface temperature
decreases rapidly because of the high heat transfer coefficients. With an increase
in the mass flux (Fig. 7.56B), the boiling is suppressed and the surface temperature
decreases (AB). After the point B the surface temperature Tw is observed to rise
(up to Point C) in accordance with increase in the bulk fluid temperature Tf . This indicates
that while the true vapor quality does not change, the two TW peaks appear.
Fig. 7.56C shows a wavy surface temperature profile, which should be corresponding
to TS changes along the length of the channel.
Boiling flow heat transfer in a vertical pipe with subcooling has other features
(Dougherty et al., 1990). If there is no boiling, the heat transfer coefficient αi at
the pipe inlet can be found from the correlation:

<!-- page 456 (PDF 100) -->
Nu = αid
λf
= 0:166Re0:66Pr0:33 μf =μw
□
□0:14:
The heat transfer coefficient for the flow of subcooled (x=−0.3□0) fluid is given by:
α=αi = 4:13 + 53:89x + 381:38x2 + 1257x3 + 1572:7x4:
From this it follows that when x=0, α=4.13αi; at x=−0.1, α=1.44αi; at x=−0.2,
α=1.04αi.

### 7.8.4 Developed boiling in channels in subcooled to saturated region

The heat transfer coefficient of the forced flow boiling is influenced mainly by two
processes—convection and boiling. It is well understood that the former process
can suppress the latter. There, a magnitude of the heat transfer coefficient can be similar
to that of the convection heat transfer coefficient αc at low heat flux and high
velocity, and the pool boiling heat transfer coefficient α0 at high heat flux and
moderate velocity.
The method proposed by Kutateladze (1979) allows you to take into account the
influences of the flow velocity and heat flux without relying on complicated criteria.
First, heat transfer rates α0 at boiling and αc for turbulent flow convection of the liquid
Fig. 7.56 Boiling onset with different wall temperature peaks (Wadekar, 1993). Temperatures:
□—wall; □—the average flow; l—saturation; - - - calculated temperature profile.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 457 (PDF 101) -->
at TS are compared. That is, depending on the ratio α0/αc the following equations are to
be used:
α0=αc < 0, α = αc;
(7.150)
0:5 < α0=αc < 3, α=αc =
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 + Cα=αc
ð
Þ2
q
;
(7.151)
α0=αc > 3, α = α0 or α = 0:9α0:
(7.152)
Here α is the heat transfer coefficient for the considered mode, αc is the convective
heat transfer coefficient calculated according to the formulae. In Eq. (7.151), C
is a function of p and, for p<15 MPa, is 0.8–0.9. According to Kutateladze,
Eq. (7.152) is applicable to the nucleate boiling of water at TS and to the subcooled
boiling. Eqs. (7.150)–(7.152) are applicable for p=2–20 MPa and are accurate within
□35%. A similar approach is found in Wadekar (1990).
Instead of the formula (7.151), Yagov et al. (1998) recommended a formula that
gives the best agreement with experiment for the case of boiling in a large volume
of water:
α=αc =
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
α0=αc
ð
Þ3 + 1 + ΔTS=ΔT
ð
Þ3
3q
;
(7.153)
ΔTS = TS −Tf ; ΔT = Tw −Tf :
When a two-phase mixture flows in a pipe or annular channel, heat transfer coefficients
are calculated according to the formula obtained in CKTI4 by Borishanskii
et al. (1973) and Handbook (1986):
α = α1
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
1 + 7□10−9 Δhfgρf Jcм
q
□
(3=2 0:7α0
α1
□
(
s
,
(7.154)
where α1 =
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
α2
c + 0:7α0
ð
Þ2
q
, αc is the heat transfer coefficient of single-phase flow at
the velocity w0 in a pipe or channel; α0 is the heat transfer coefficient of the pool boiling;
JCM = Jf0 + Jg0 isthemixturevolumetricfluxwhereJf0 = G 1−x
ð
Þ=ρf and Jg0 = Gx=ρg;
x is the mass quality. The range of application for water is p=0.2–17 MPa;
Jcм=1–300 m/s; q=0.08–6 MW/m2.
Influence of the mixture velocity becomes notable, when the following relation is
true:
Δhfgρf JCM=q
□
□
· 0:7α0=α1
ð
Þ4=3 > 5□104. In this case the heat transfer coefficient
is in proportion to the mass flux to the 0.8th power, i.e., α □ W0:8. At lower values
4Former CKTI, Central Boiler and Turbine Institution in Russia (http://english.ckti.ru/about.html),
Currently, I.I.Polzunov Scientific and Development Association on Research and Design of Power
Equipment.

<!-- page 458 (PDF 102) -->
of this combination α □ q0:7 and does not depend on Jсм and then α = α1 (see
Fig. 7.57).
It would be sufficient to use a simple formula for evaluating the boiling heat
transfer of different fluids as proposed by Borishanskii et al. (1973):
α=αc = F;
(7.155)
F = 3:2Y + 1; Y = x= 1−x
ð
Þ
½
□0:75 pc=p
ð
Þ0:375M0:125,
where M is molecular mass. The limit of applicability is Y=1–20. Accuracy will be
for F<1, □35%; for F=0, □20%; at F=40, □5%.

### 7.8.5 Boiling on porous structures under forced convection conditions

#### 7.8.5.1 Subcooled boiling on a capillary-porous surfaces

The concept of the process of subcooled boiling subcooled for this case is presented in
Soloviev (1998).
Depending on the magnitude of the heat flux and degree of subcooling, there are
three modes of heat transfer: (1) microtube mode, (2) bubble roughness mode, and (3)
bubbly surface roughness mode (see Fig. 7.58). Calculation of the heat transfer coefficient
for the mode 2 can be made by the method proposed by Avdeev (1982, 1985):
α = ρf wcp
5:67 ln D=d
ð
Þ + 4:92
½
□ 5:67 ln D=d
ð
Þ−3:58
½
□
f
g−1 □30%,
(7.156)
where D is the channel diameter, d is the bubble diameter, defined by the formula:
d = 1:24dsε−1:18
ffiffiffiffiffiffiffiffiffiffi
ql=qc
p
,
where ds is the pore diameter; ε is the porosity; ql and qc are heat flux associated with
evaporation and convection given by:
a/a1
0.5
104 5×104 105
(Δhfg p□JCM/q) × (0.7a0/ a1)4/3
Fig. 7.57 Heat transfer in
two-phase flow in channels.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 459 (PDF 103) -->
ql =
ðδ
αg TW −Tg x
ð Þ
dx; qc = αc TS −Tf
□
□
Heat transfer for the mode 3 can be determined by the following (Avdeev, 1982,
1985):
α = ρf wcp
5:67 ln D=d
ð
Þ + 4:92
½
□ 5:67 ln D=d
ð
Þ + 7:08
½
□
f
g−1 □30%,
(7.157)
where d is the detachable bubble diameter (see above).

### 7.8.6 Heat transfer in film boiling, and superheated vapor flow in channels

Film boiling heat transfer has been extensively investigated during the last half century
. Excellent reviews are found in text books by Tong (1965), Tong and Tang
(1997), Collier and Thome (1980), Delhaye et al. (1981), Butterworth and Hewitt
(1977), a handbook by Hetsroni (1982), and articles by Ganic and Rohsenov
Fig. 7.58 Subcooled liquid boiling
model at the capillary-porous
surfaces. Mode 1—microtube
mode, in which heat is transferred
from the surface through pores that
act as heat pipes (evaporation occurs
at the base and condensation at the
top); Mode 2—bubble roughness
mode, in which at the outer
boundary of the porous layer formed
stationary steam bubbles on top of
which there is a vapor condensation;
Mode 3—bubbly surface roughness
mode, in which at the outer
boundary of the porous layer, the
stationary bubbles are formed and
condense on the top.

<!-- page 460 (PDF 104) -->
(1977), Mayinger and Langer (1978), Tong (1978), Sergeev (1978, 1987, 2007),
Groeneveld and Snoek (1986), Groeneveld (1992), Yadigaroglu and Andreani
(1989), Sakurai (1990), Andreani and Yadigaroglu (1989, 1994), and in the proceedings
of the 1st International Symposium on Fundamental Aspects of Post-CHF Heat
Transfer (1984). A good summary of the literature survey is given in (published in
2001 in the context of the IAEA’s Coordinated Research Project on Thermohydraulic
Relationships for Advanced Water Cooled Reactors (IAEA TECDOC, 1203, 2001)).
In the context that follows in this section, we discuss on a number of two-phase
flow heat transfer regions depicted previously in Fig. 7.54 by region 5—liquid deficient
region (degraded heat transfer), region 6—superheated vapor forced convection,
region 7—subcooled film boiling (Tf < TS), region 8—Saturated film boiling Tf = TS,
and region 9—liquid deficient and heat transfer crisis; in Fig. 7.53 by region
3—dispersed-annular, region 4—mist and region 5—single-phase superheated vapor;
and in Fig. 7.52 by region G (liquid deficient) and region H (super heated vapor).
In boiling two-phase flows in a heated channel, a drastic deterioration of heat transfer
(heat transfer crisis) may occur, which shows an increase in temperature on the
heat-transfer surface, or reduction in the heat flux q. The heat transfer mode between
the onset location of the crisis and its downstream region where the flow becomes
single-phase superheated vapor flow is called as film boiling. In this regime, at a constant
heat flux, an increase in the surface temperatures is observed and the offset of the
crisis in the region of low steam quality with increasing q (see Fig. 7.59).
The film boiling is characterized by an aggravated mode, temperature fluctuations
due to the variable surface contact modes of liquid and vapor. This regime is
implemented in the steam generator but is to be avoided in the case of nuclear fuel
rod bundle cooling. Nevertheless, some experiments show that a short-term operation
of fuel rods in such a regime under certain parameters is possible if the excess temperature
of the fuel cladding surface and the amplitude of the oscillations do not
exceed permissible limits. From this point of view, perhaps a more accurate
Tw°C
0.4
0.6
0.8
1.0
1.2
1.4
q = 230
kW/m2
x
Fig. 7.59 Wall temperature dependence on
the vapor quality and heat flux at
ρw=1400 kg/(m2 s); p=9.8 MPa.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 461 (PDF 105) -->
calculation of heat transfer is necessary. The temperature jump at a crisis decreases
with increasing mass flow rate and pressure, and increases with increasing heat flux.
Two-phase flow structure in this region is different depending on the nature of the
crisis, i.e., DNB ([A] in Fig. 7.54) or film dry-out ([D] in Fig. 7.54).
If a crisis occurs in the subcooled two-phase flow, or two-phase flow of low steam
quality, i.e., due to DNB, the realized two-phase flow mode is called as “inverted
annular flow” where the superheated vapor flow flowing along the wall separates
the subcooled layer from the wall. The inverse-annular flow regime is preceded by
the transition boiling section in the upstream region which is bounded by the DNB
point (CHF) and the quench front or the minimum heat flux of the film boiling on
the boiling curve.
As described in Section 7.5.4 on the boiling curve in the pool boiling, the location
of the minimum film boiling temperature (TMFB) separates the high temperature
region of the inefficient film boiling or vapor cooling, from the lower-temperature
region of more efficient transition boiling region. Thus it provides a limit to application
of the transition boiling and film boiling correlations. TMFB also represents a temperature
boundary beyond which surface properties and surface conditions generally
do not affect the heat transfer. Wettability or contact angle although important in
nucleate and transition boiling, are not applicable in the film boiling regime, and
the conduction along the surface becomes less important when nucleate and film
boiling no longer occur one-by-one.
It is noted that, while the critical heat flux has been extensively studied and can be
predicted fairly well by a variety of correlations, the minimum heat flux under forced
convective conditions has undergone less investigation. There is no general consensus
on the effect of the various system parameters on TMFB under the conditions but it
should be affected by flow, pressure, fluid properties, and heated surface conditions
in the same way as in the pool boiling described in Section 7.5.4.
In the “dispersed-annular flow” regime, the crisis is usually associated with the
liquid film dry-out on the heated surface. In this case, the heated wall is cooled by
the vapor flow, which is superheated while flowing along the channel. In this vapor
flow region, liquid droplets exist and gradually evaporate exchanging heat with the
superheated vapor.
In general, the dispersed two-phase flow in this zone is in thermally nonequilibrium
, and the wall surface temperature is determined by several processes:
the convective heat transfer by the vapor flow, radiation, and evaporation of the
droplets. The actual flow parameters depend on the evaporation of droplets and
heat-transfer area in the vapor flow, whose temperature may exceed the saturation
temperature. In simple calculations, thermal equilibrium between liquid and vapor
phases is often assumed. There the boundary between this region and a superheated
vapor flow region of the channel is considered where the equilibrium steam quality
x=1.
Depending on the operating conditions and the channel geometry, the flowing
vapor in the post-CHF zone may be superheated in the inverse-annular regime where
the liquid is separated from the heated surface by the vapor film (downstream of the
DNB point and the transition boiling region), or in the dispersed-annular flow regime
