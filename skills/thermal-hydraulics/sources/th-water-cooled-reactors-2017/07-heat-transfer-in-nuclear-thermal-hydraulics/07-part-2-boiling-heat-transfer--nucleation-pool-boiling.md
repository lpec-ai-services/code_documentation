# Part 2: Boiling Heat Transfer — Nucleation pool boiling … Film pool boiling
<!-- source PDF pages 77-91 -->

<!-- page 433 (PDF 77) -->
## 7.6 Nucleation pool boiling

### 7.6.1 The mechanisms of the nucleation process

Complete theory of boiling has never been established that takes into account all the
factors affecting the magnitude of the heat transfer. They include primarily physical
properties of the fluid, complex surface conditions (surface roughness, its size distribution
, surface deposits, wettability, surface material properties, etc.). The system of
differential equations and boundary conditions, describing the boiling two-phase
flows, include:
–
Momentum conservation equation for the liquid and vapor phases;
–
Mass continuity equation for the liquid and vapor phases;
–
Energy conservation equation for the liquid and vapor phases;
–
and appropriate initial and boundary conditions including those associating with the
diffusion processes:
–
Thermal and mechanical interactions at the phase interface;
–
Continuity of the energy flow (heat flux) across the phase interfaces; qip = −λ ∂T=∂n
ð
Þip =
wgρgΔhfg where wg is the local vapor-phase velocity on the interface is assumed to be a
speed of evaporation;
–
Equal temperatures at the phase interface.
Mathematical description of physical models of boiling process can only be formal
because of the uncertainties of many factors involved in closure equations, the lack
of accurate boundary conditions, in particular at the interfaces between vapor- and
liquid-phase. Therefore, these relations serve only to establish a kind of generalized
variables, which make processing of experimental data possible. A capillary
constant is often used either as a reference length l =
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
σ=g ρf −ρg
□
□
r
, a quantity
related to the size of critical (minimum) radius of the nucleus of vapor
Rcr =
σTS
Δhfgρg Tw −TS
ð
Þ = 2σT vg −vf
□
□
ΔhfgΔT
·
ρf
ρf −ρg
(Eq. 7.117) (Lykov, 1954). The characteristic
velocity is the speed of evaporation wg = q= Δhfgρg
□
□
under the thermal
equilibrium condition, which determines the vapor volume withdrawn from the unit
interphase surface area per unit volume and per unit time (m/s).
The high heat flux density at boiling is mainly associated with the following two
processes: (1) agitation of liquid steam bubbles near the surface of the heat exchange
(qconv); and (2) intensive evaporation of the micro liquid layer at the bottom of
the vapor bubble (qeva). Thus, q=qconv+qeva.
Formation of one vapor bubble of diameter d0, i.e., the volume V = πd3
0=6
consumes the heat Q1 = ΔhfgρgV = Δhfgρg
πd3
6 . Let the number density of the existing
vaporization centers per unit area be N (m−2), the total heat transfer area A, the

<!-- page 434 (PDF 78) -->
separation frequency fi, the volume of each bubble Vi, then the amount of heat
removed by evaporation of the liquid will be given by:
qeva =
XN
1 Qifi
A
= Δhfgρg
XN
1 fiVi
A
= ΔhfgρgNf ⟨V = ΔhfgρgNπ
6fd0
3:
As the heat flux or temperature difference (ΔT) increases, the number of vaporization
centers grows (N □ q; N □ ΔT3). The average frequency f and the detachment diameter
d0 are virtually independent of q. Therefore, the average production of vaporization
centers under the developed boiling is approximately constant. In the developed
boiling, the fraction of the heat transported by the evaporation (qeva/q) increases as q
increases and approaches to 100%, i.e., q 	 qcr.

### 7.6.2 Influence of various factors on heat transfer in nucleate boiling

The effect of pressure is shown in Fig. 7.45 (Borishanskii, 1961; Borishanskii et al.,
1964). With increasing pressure, the heat transfer coefficient increases, slowly at first
(up to π = p=pcr 	 0:2), then (for π > 0:2) the influence of pressure increases sharply.
The reason for this pressure dependency is explained from the nature of
changes in physical properties of the fluid, i.e., first of all, Δhfg, σ, ρf, and ρg.
Growth of the vapor bubbles at high pressure is explained by the heat transferred
10−3
10−2
10−1
a (W/m2K)
p*
p/pcr
Gorenflo
Nishikawa
Cooper
Calculations for
copper surface, Ra= 0.4 μm
Borishanskij et al. (1964)
Fedders (1971)
Golowin et al. (1963)
Gorodov et al. (1979)
Gremer (2001)
Heieh et al. (1994)
Jamialahmadi et al.
Kang et al. (2000)
Minchenko (1969)
Water; q= 20,000 W/m2
□
Fig. 7.45 The effect of pressure on the heat transfer coefficient of nucleate boiling
(Borishanskii, 1961; Borishanskii et al., 1964): pcr—critical pressure, p*—conditionally
selected pressure, p*=0.03pcr.
Adapted from Feldmann, H., Luke, A., 2008. Nucleate boiling in water for different pressures.
In: International Refrigeration and Air Conditioning Conference. Paper 982.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 435 (PDF 79) -->
from liquid to the vapor bubble through the interface surface in the base layer
(Labuntsov, 1960). An increase in the pressure reduces the surface tension and
the heat of evaporation, facilitating nucleation and growth of the vapor bubbles,
reduction in Rcr, and the growing number of vaporization centers. At low pressures
(π = p=pcr <5□10−4, p<0.01 MPa), boiling initiation becomes difficult,
expanding the convective heat transfer region, decreasing the bubble detachment
frequency and increasing Rcr.
Influence of the surface roughness on the heat transfer is evaluated based on the
information on active centers of vaporization (cavities), including the number density,
and not only the value of the protrusions and depressions, but their size distribution
and even the shape of cavities. In general, with an increase in the surface roughness for
the same heat flux, we have less wall superheat, i.e., an increase in heat transfer. However
, this observation is not universal. Depending on the size and shape distributions
of the cavities (caverns), the boiling curve vary. For example, Fig. 7.46B shows boiling
curves for cavities of the normal distribution of sizes, of an equal size, and for a
specially selected distribution of cavities in size. Thus you can control the shape of the
boiling curve (i.e., the flux) with new technology of production of special surfaces
with cavities and hollows (Fig. 7.46).
The presence of impurities in the water causes deposits on the heating surface,
changing the surface roughness, which, on the one hand, leads to formation of new
cavities and, consequently, to increase the heat transfer coefficient. On the other
hand, the additional thermal resistance of these deposits reduces the heat transfer
coefficient. In practice, however, due to the variety of operating conditions,
it is difficult to estimate the thickness and thermal conductivity of the deposits.
Thus, we rely on the thermal resistance of the deposits provided from industry
experience.
In the context that follows, the formulas are listed which are suitable for smooth
surfaces with no deposits. During boiling, the surface deposits should be considered
q
lgΔT
(Tw–Ts), K
kW/m2
log q
(A)
(B)
Fig. 7.46 Influence of surface roughness on the boiling curve: (A) □⃗ l⃗□⃗□—increase
roughness; (B) for the normal distribution of the cavity sizes; - - - all cavities of the same size;
-·-·- for cavities of specially selected size distribution.

<!-- page 436 (PDF 80) -->
as a sediment layer with thermal resistance. In this case, 1=α = 1=αр + R, where αp is
the heat transfer coefficient that can be obtained according to the equations to be
shown in the following; and R is the thermal resistance of the deposits.
Material thermal properties and thickness of the heat-transfer wall may affect
effective heat transfer coefficient. The reason for this lies in the unsteady heat conduction
that develops in the vicinity of the cavity center of vaporization. If the wall
material has high thermal conductivity and high heat capacity cp, it would facilitate the
influx of heat of vaporization to the cavity centers and provides a high heat transfer
rate. It is noted that, when the deposits layer is thick (δ>1 mm), which is not unusual
in normal industrial operations, the boiling heat transfer rate does not practically
depend on the material and its conditions but is greatly influenced by the surface
roughness and the presence of low conduction deposits on it. It is also noted that
the heat transfer coefficient of the nucleate boiling in a large volume is essentially
independent of the orientation of the heat-transfer surface, if the detachment of steam
bubbles is ensured on the surface at any angles.
Modeling of boiling heat transfer of pure liquid and binary mixtures generally
includes the following processes (Balakrishnan, 1998):
1. Micro-convection in the boundary layer due to an increase in bubbles at the heating surface;
2. The flow of fluid as a result of growth and detachment of the bubble, flow of the cold liquid
toward the heating surface;
3. Transient heat conduction in a cooling fluid as it gets warm;
4. Vaporization of the micro layer during the bubble growth;
5. Agitation of the liquid layer due to the bubble growth, bubble detachment and the “cold”
flow to the surface;
6. Turbulence generated by natural convection in the region adjacent to the center of
evaporation, where there is no evaporation.
Heat transfer in the binary mixtures is usually more intense than in the pure liquids, for
easier evaporation of the volatile component.
Thus, the pool boiling process in a large volume is associated with the active effects
of vapor bubbles and the rate of heat transfer that can be considered as a sum of four
components:
(1) Micro-convection occurring near the surface during the growth and detachment of the vapor
bubbles;
(2) Evaporation of the liquid layer underneath the vapor bubbles, taking into account the
transfer of the latent heat of vaporization to inside the vapor bubble;
(3) Natural convection in the large volume;
(4) Thermo capillary flow (Marangoni flow).
The last component is connected to a longitudinal movement along the surface, which
is caused by a temperature gradient and the surface tension at the liquid-vapor interface
. It does not play a big role in the boiling at the saturation temperature, but essentially
at high subcooling. In most of simple models of boiling heat transfer, the heat
flux appears to be a sum of only two heat fluxes associating with the convection (qconv)
and evaporation (qeva): q=qconv+qeva.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 437 (PDF 81) -->
### 7.6.3 Estimate correlations

Heat transfer in the developed boiling region is calculated on the clean surface in a
large volume of water by the following heat transfer coefficient:
α = 4:34q0:7 p0:14 + 1:35□10−2p2
□
□
,
(7.121)
where q is expressed in W/m2; p in MPa; α in W/(m2 K). The range of applicability of
Eq. (7.121) will be: p=0.1–20 MPa; q<0.4 MW/m2. The equation is applicable at
temperatures from the subcooled to saturation range. Temperature difference in this
case is defined as a difference between the surface temperature and the saturation temperature
. Dependence of the heat transfer coefficient on the saturation temperature of
water is expressed empirically by the following equation:
α = 10:45q0:7 3:3−0:0113 TS −373
ð
Þ
½
□−1,
(7.122)
where TS is in K. The same applicability range for Eq. (7.121) is applied. Assuming
that the same boiling heat transfer process can be determined by the flow internal
mechanisms, Labuntsov (1960) proposed a correlation:
Nu = CRenPr1=3,
(7.123)
where Nu = αl
λf
; Re = wl
νf
=
ql
νf Δhfgρg
since w =
q
Δhfgρg
; Pr is the Prandtl number of the
liquid; and l≡ cpf ρf σTS
Δhfgρg
□
□2.
To calculate the heat transfer during the nucleate boiling in a large volume, the
following fairly simple equation could be used (Minchenko, 1960):
Nu = 0:55 PeKp
□
□0:7RenPr1=3,
(7.124)
where
Nu = αl
λf
;
Pe = RePr =
ql
νf Δhfgρg
νf
α =
ql
Δhfgρgα;
Kp =
p
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
σg ρf −ρg
□
□
r
;
and
l =
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
σ
g ρf −ρg
□
□
s
.
More widely used correlation is by Rohsenow (1952), based on the idea that the
heat transfer coefficient of boiling mainly depends on the degree of turbulence in
the boundary layer and the increasing uprising steam bubbles (i.e., the main component
of the heat flux is contributed by the convection). Then,
Nu = Csf RemPrn,

<!-- page 438 (PDF 82) -->
where Csf is the coefficient that depends on the thermal properties of the fluid at
a temperature of saturation and surface conditions. Another form of the equation is:
RePr
Nu = cpΔT
Δhfg
= Csf
q
Δhfgμ
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
σ
g ρf −ρg
□
□
s
0:33
cpμ
λ
□
□n
,
where ΔT = Tw −TS. For water at TS=100–350°C, q=3–3200 kW/m2; n=1;
Csf=0.013–0.015. For low pressure Csf=0.007–0.008 as shown in Pioro (1999);
for hydrocarbons, freon, Csf is widely spread in 0.0014–0.0018.

### 7.6.4 On the hydrodynamic theory of similarity of boiling heat transfer

Thermodynamic similarity principle provides a formula for the heat transfer coefficient
of the boiling up to a constant coefficient, which is determined experimentally
and is a constant for thermodynamically similar liquids. Similitude substances based
on this principle were first suggested and applied to the problems of heat transfer and
the crisis at boiling by Novikov (1961) and developed further by Borishanskii et al.
(1964, 1973). Since the boiling heat transfer coefficient is a function of the developed
heat flux and physical properties of liquid and vapor, its first approximation could be
represented as a product of powers of these values:
α □ qnrn1σn2λn3μn4…
(7.125)
On the saturation line any physical parameter is determined depending on the form
given by:
χi =
M
g
□
(m1i
Tm2i
cr pm3i
cr Rm4ifi
p
⟨pcr
□
(
,
(7.126)
Therefore, the formula (7.125) takes the form:
α = qn M
g
□
(m1
Tm2
cr pm3
cr Rm4F1
p
pcr
□
(
:
(7.127)
A number of experiments have shown and established that α□q2/3. Therefore in order
for the R.H.S. of Eq. (7.127) to have the dimension of the heat transfer coefficient,
m1=−1/6; m2=−5/6; m3=1/3; m4=1/6. Thus, the final form is:
α = B gR
M
□
(1=6
p1=3
cr T−5=6
cr
q2=3F2
p
pcr
□
(
:
(7.128)
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 439 (PDF 83) -->
The magnitude B and the function F2 are determined from experiments. Estimates of
the heat transfer coefficients for the boiling, for which there are no direct measurements
, can be performed using the following equation:
α = 882p1=3
к T−5=6
к
M−1=6π0:1 1 + 4:65π1:13
□
□
q2=3,
(7.129)
where π =p/pcr.

### 7.6.5 Boiling on a coated porous surface

Fig. 7.47 shows that the use of porous coating of the high permeability and high thermal
conductivity layer allows significantly increasing the heat transfer coefficient of
nucleate boiling and critical heat flux, where the boiling initiates on the porous surface
at a lower heat flux (A) than on the smooth surface (A0). In the figure, the boiling curve
2 is for the coated surface and the line 1 for a smooth surface. The position of the curve
2 has a large uncertainty and may shifts by tens and hundreds degrees (temperature)
depending on the characteristics of the porous structure. At complicated exhalation of
the vapor from the capillary-porous structure, and with a decrease in the heat flux, the
boiling curve can be represented by BFE (line 3). Heat transfer coefficient on the line 3
is determined by the thermal resistance of the porous coating, i.e., α	λs/δ, where λs is
the thermal conductivity, δ is the thickness of the porous layer.
The physical model of the heat transfer at boiling on the capillary-porous surface is
shown in Fig. 7.48.
D
D□
C□
A□
C
F
B
lg q
A
A□
E
H
θ
lg(Tw-Ts)
Fig. 7.47 Generalized boiling curves by Borishanskii et al. (1973): 1—to a smooth surface;
2—on the surface of a capillary-porous coating.
Data from Kovalev, S.A., Solovev, S.L., 1989. Evaporation and Condensation in Heat Pipes,
Nauka, Moscow (in Russian); Kovalev, S.A., Solovev, S.L., Ovodkov, O.A., 1985. Liquid
boiling on porous surfaces. In: Proc. of School – Seminar: Heat and Mass Transfer Processes at
Two-Phase Changes and at Two- Phase Flows, pp. 26–38 (in Russian); Kovalev, S.A.,
Solovev, S.L., Ovodkov, O.A., 1987. Liquid Boiling on Porous Surfaces. Heat Trans. Sov. Res.
19 (1), 109–120.

<!-- page 440 (PDF 84) -->
Modeling is based on a phasic description of the motion and heat transfer in a
porous layer. We assume a stable stationary regime of evaporation inside the
capillary-porous structure, vapor and liquid flows move along separate channels,
the heat is transferred by heat conduction through the skeleton of the porous coating
to the liquid meniscus where the main evaporation takes place, the liquid
completely wets the porous material of the coating, and the contact angle θ equals
zero. Results from numerical experiments are presented by Soloviev (1998) for
different characteristics of the capillary-porous structure. The capillary-porous
surfaces boiling under the forced convection cooling conditions is discussed in
Section 7.8.5.

### 7.6.6 Bulk boiling in tubes

Boiling process is often used in design of heat exchangers and steam generators in
vertical or horizontal pipes. Typical examples are PWR steam generators and heat
exchangers for passive heat removal systems. In many cases, the temperature
difference ΔT = Tw −TS is small and does not exceed 20–30 K.
Fig. 7.48 Heat transfer model with liquid boiling on the capillary-porous surface (from
Soloviev, 1998). (A) phasic motion in the porous structure; (B) pressure changes in the thickness
of the porous layer 0<x<δ; (C) in the—horizontal section x1—x1 porous structure;
(D) temperature variation of the skeleton of the porous coating thickness 0<x<δ.
1—vapor; 2—liquid; 3—dried layer; 4—saturation.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 441 (PDF 85) -->
7.6.6.1
Low pressure condition (0.1–0.3 MPa)
In this pressure range, there are two major heat exchange mechanisms: first, heat
transfer increase due to the liquid-phase turbulence and vapor bubbles generation
(for q<50 kW/m2); second, heat exchange deterioration due to the formation of large
vapor bubbles conglomerate covering the heated wall surface with q>50 kW/m2.
Based on the review of publications until 1997 by Parlatan and Rohatgi (1997) for
all models of vertical tube heat exchangers, simple correlations of the pool boiling
heat transfer coefficients are recommended, that are easy to use in codes for nuclear
system safety analysis and subchannel analysis:
q = AΔTb
S,
(7.130)
where q is in W/m2; ΔT = Tw −TS in K. Modes of boiling, wall superheating with
respect to the saturation temperature ΔT, A, and b are provided in Table 7.7.
Nucleate boiling heat transfer under the atmospheric pressure conditions (0.1 MPa)
attracts attentions in passive heat removal systems design. A study by Moon et al.
(1998) shows the heat transfer coefficient for the vertical and horizontal tubes that
depend on the surface roughness Δ:
α = С · ΔTm
S · Δn · dk,
(7.131)
where α is in kW/m2 K; ΔTS in K; Δ in nm (10−9 m); d is the tube diameter in mm
(Table 7.8).
Table 7.7 Coefficients in Eq. (7.130)
Mode
ΔTS (K)
A (W/
m2 Kb)
b
Free convection
ΔTS□3
1.333
Transitional regime from single-phase
convection to nucleate boiling
3□ΔTS□6
1.52
Nucleate boiling
6□ΔTS□22
52.4
3.058
22□ΔTS□30
1.44
Transition boiling
30□ΔTS□70
5.58□1012
−4.555
Film boiling
70□ΔTS□400
0.75
Table 7.8 Coefficients in Eq. (7.131)
Pipe arrangement
C
m
n
k
Horizontal
0.015
4.508
0.084
−1.318
Vertical
0.024
3.862
0.672
−1.658

<!-- page 442 (PDF 86) -->
Eq. (7.131) is applicable
for the range of
d=9.7–25.4 mm; roughness
Δ=15.1–60.9 nm; p at 0.1 MPa.
Surface roughness is substantially more effective for vertical pipes than for horizontal
pipes, although in both cases an increase in roughness causes an increase in heat
transfer coefficients. Instead of Eq. (7.131), you could use less precise but simpler
empirical relationship:
α = 0:266q0:812 □25%,
(7.132)
where α is in kW/m2 K and q in kW/m2.
7.6.6.2
High pressure region (p>0.3 MPa)
Under high-pressure conditions, heat transfer coefficients are quite high (2.5□104 to
2.5□105 W/m2 K). Many different authors recommended a number of formulas
for a pool boiling. For instance, see IAEA TECDOC 1203 (2001). Perhaps the
formula by Rassokhin (1980) is one of the most preferred, giving some leeway for
calculation:
α = 5:51q2=3p0:25 for 0:1 < p < 8МPа;
(7.133)
α = 0:58q2=3p1:33 for 8 < p < 20МPа;
(7.134)
where q is in W/m2 and p in MPa.

#### 7.6.6.3 Effect of oxide films and deposits on the outer surface of the pipe

Oxide films and deposits formed on the tube surfaces reduce the heat transfer
coefficient. Determination of the composition and structure of deposits, and taking
into account the impact of these factors are a complicate task. Oxide films are
usually composed of hematite (Fe2O3) or magnetite (Fe3O4). The formation of oxide
films on the surface of the pipe is subject to the law (Glebov et al., 1983; Man’kina,
1977):
M = A exp −B=T
ð
Þτc,
(7.135)
where M is in g/m2, T in K and τ in h. A, B, and C in Eq. (7.135) are found in Table 7.9.
The thermal conductivity of hematite (Fe2O3) and magnetite (Fe3O4) can be
described by the following:
λ Fe2O3
ð
Þ = 13:215−0:375 · 10−1T + 0:379 · 10−4T2;
(7.136)
λ Fe3O4
ð
Þ = 4:133−0:852□10−2T + 0:757 · 10−5T2;
(7.137)
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 443 (PDF 87) -->
where λ is in W/(m K) and T in °C. Deposits usually consist of two layers: (1) firmly
adjoining the surface; and (2) outer and more porous. They differ in their composition
and porosity:
Layer
(1)
(2)
Density (g/cm3)
4.4–4.7
1–4
Chemical composition at pH 9
Porosity (%)
Fe3O4
Fe3O4
20–75
Chemical composition at pH 9
Porosity (%)
Fe2O3
Fe3O4
More details about the influence of deposits on heat transfer coefficient for steam
generators are found in Trunov et al. (2001) for PGV-1000 of VVER.

## 7.7 Film pool boiling

### 7.7.1 Stationary film boiling

In the film boiling mode, the liquid is separated by the vapor film from the heating
surface. The intensity of heat transfer is determined by convection, while at high temperature
environment, by ΔT=Tw−TS and radiation heat transfer through the vapor
film. Mechanisms of vapor detachment out of the cavity on the wall surface is related
to the thickness and the vapor film flow mode (laminar wave, turbulent, mixed).
Therefore, the configuration and orientation of the heating surface, and the physical
properties of liquid and vapor have certain importance in the gravity field. Theoretical
analysis of the film boiling is simplified as compared with the analysis of nucleate
boiling, because the process takes place only at the interface of the two phases and
is in quite ordered a pattern. However, analysis of instability of the vapor film boundaries
and the presence of irregular waves is suitable only for qualitative assessment,
which is helpful in understanding the physical picture of the phenomenon, but cannot
give quantitative results.
Table 7.9 Coefficients for Eq. (7.135)
pH
Type of steel
A
B
C
7.8
High-chromiuma
3.91□106
0.25
Austeniteb
0.38
9–10.5
High-chromiuma
6.57□105
0.26
Austeniteb
0.41
aC—0.12; Cr—1; Mo; V.
bC—0.12; Cr—18; Ni—12; Ti.

<!-- page 444 (PDF 88) -->
In this boiling regime, a total heat flux can be represented by a sum of convective
(qc) and radiation (radiant) (qr) of the heat transfer: q=qc+qr. If the heat transfer
coefficient refers to the temperature difference (Tw−TS), then the total heat transfer
coefficient of the film boiling is determined to a first approximation, by the sum of
convection (αc) and radiation (αr) components:
α = αc + αr,
(7.138)
where αr = εl · 5:66 · 10−8 T4
w −T4
S
□
□
= Tw −TS
ð
Þ, W/m2К; εl = 1= 1=εw + 1=εS −1
ð
Þ is
the reduced emissivity; εw	0.75 is the surface emissivity, εS = 1 is the emissivity
of the water surface.
The convective heat transfer coefficient αc of the film boiling of saturated water
and other liquids is from the empirical relation by Klimenko (1984):
Nu = CArmPrnf K
ð Þ□25%,
(7.139)
where
Nu = αδ=λg;
Ar = gδ3 ρf =ρg −1
□
□
= νg
□
□2;
Pr = νg=ag;
K = Δhfg=cpgΔT;
b =
ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
σ=g ρf −ρg
□
□
r
.
σ, Δhfg, and ρf are evaluated at the saturation temperature TS, and other material
properties are determined and an average temperature of vapor is given by
T = TS + Tw + TS
ð
Þ=2. C, m, n, and the form of the function f (K) in the equation are
given in Table 7.10.
Eq. (7.139) gives an average value of the heat transfer coefficient across the flat
wall surface. On the curved surfaces, the local values of α may differ by 20%–30%.

### 7.7.2 Rapid cooling of very hot bodies (hardening modes)

When a heated solid metal body is immersed into cold water, there is a series of
rapid-mode cooling called quenching that changes the characteristics of metals: hardening
steels in order to acquire special steel structure, hardness, and other characteristics
; production of aluminum; hardening aluminum alloys, and so on. Knowledge of
these processes is necessary for the evaluation of residual stress and fatigue.
For nuclear reactor safety, investigation of similar phenomena is important for the
analysis and calculation of the reactor core cooling in the event of accidents.
In metallurgical process errors with heat transfer calculations may be corrected
quite easily, conducting repeated “integrated” experiments and applying appropriate
corrections. However, in the nuclear power reactor it is difficult to do so or, in many
cases, impossible. Therefore, the importance of the calculation of such events cannot
be overestimated for the nuclear power industry. Rapid cooling of hot objects in the
water involves several modes of heat transfer, which replace one another, i.e., modes
of the film boiling, nucleate boiling, convection (forced and natural), and the thermal
conduction. As shown in Section 7.1.4, a boiling curve has three characteristic
points: (1) the minimum film boiling temperature or Leidenfrost temperature
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 445 (PDF 89) -->
Table 7.10 Data necessary for Eq. (7.139)
The shape and orientation of
the surface
Size δ
Range of applicability
C
m
n
f(К)
Sphere
Diameter D
D/b□6
3□104<ArD<2□107
0.70
1/4
1/3
1.0 for К□1.4;
0.92 for К1/4>1.4
ArD>2□107
0.175
1/3
1/3
1.0 for К□1.6;
0.85 for К1/3>1.6
Horizontal cylinder
Diameter D
D/b□2
ArD<2□107
0.64
1/4
1/3
1.0 for К□1.2;
0.96 for К1/4>1.2
ArD>2□107
0.16
1/3
1/3
1.0 for К□1.4;
0.89 for К1/3>1.4
Horizontal flat surface
l=2πb
D*/b□31
ArD<1□108
0.19
1/3
1/3
1.0 for К□1.4;
0.89 for К1/3>1.4
ArD>1□108
0.0086
1/2
1/3
1.0 for К□2.0;
0.71 for К1/2>2.0
Vertical surface
Length l
ArL>2□107
For cylinders D/b□1.8
0.20
1/3
1/3
1.0
D—the characteristic size of the flat surface (disc diameter, the width of the tape, etc.).

<!-- page 446 (PDF 90) -->
TL (TMFB or TLFP); (2) the surface temperature corresponding to the critical heat flux
(qcr) Tc; and (3) the onset boiling point Tb for water under normal conditions (0.1 MPa,
20°C). Consider at this point again the boiling curve (Fig. 7.49) in a large volume.
A hot rod, submerged in cold water, will not be wetted by water due to the
blanketing by the low conductivity vapor around the rod surface. Heat is transferred
to the water from the hot surface by radiation (QR) and vapor-phase thermal conduction
(Qλ). Heat flow (Qλ) through a continuous vapor film is determined by the temperature
difference (Tw −Tf ). The contribution of radiation decreases rapidly as the
QR □ T4
w.
1. If the water is heated at the contact with the hot body to TS (Tf	10–20°C), the vapor bubbles
generated at the interface with the liquid surface quickly condense, providing a stable thin
film of vapor (no bubbles!) (Fig. 7.50A).
lg q
TL
Tc
Tb
ΔT
Fig. 7.49 Boiling curve in a large
volume of water (0.1 MPa). Regions of
various modes of heat transfer: 1—free
convection; 2—undeveloped boiling;
3—developed boiling; 4—transition
boiling (from bubbly to film); 5—film
boiling; Tb—initial boiling point;
Tc—wall surface temperature
corresponding to the critical heat flux
qcr; TL—Leidenfrost temperature
(minimum film boiling temperature
TMFB).
Fig. 7.50 Cooling mode of a hot rod (0.1 MPa). (A) Thin film of vapor. Quiet and rapid cooling.
(B) Wetting front movement; explosive boiling. (C) Film mode with blanketing and bubbly
mode. Slow cooling.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 447 (PDF 91) -->
2. For water temperature at about Tf	35–40°C; at the bottom of the rod, there is the film boiling
; near the liquid level, an intensive transitional or nucleate boiling, driving to the rapid
formation of large quantities of steam (explosive boiling) and then a sharp cooling of the rod
(Fig. 7.50B).
3. For water temperature close to TS (Tf	80–90°C), film boiling regime is realized covered
with the thick vapor film. As cooling of the rod proceeds to the transition, then the bubbly
boiling regime prevails (Fig. 7.50C).
4. The transition boiling regime is realized for the surface temperatures from TS to Tc (temperature
corresponding to the critical heat flux).
5. For T<Tc, the bubbly mode becomes dominant with intensive heat removal, which is then
replaced by the natural or forced convection mode of cooling.
Below is a calculation flow of hot body cooling immersed in water. This referenced
scheme is in accordance with the modified code RELAP5/MOD2 and CFX4.4 (Yeoh
and Tu, 2002) in the quasiapproximation.
The total amount of heat (Q) is assumed to consist of four components:
QR—heat dissipation by radiation from the body to the water;
Qλ—heat removal by conduction to the vapor;
Qe—heat, withdrawn through liquid evaporation; and
Qc—heat, allocated to turbulent convection.
Q = QR + Qλ + Qe + Qc:
(7.140)
The individual components are calculated as follows:
1. The amount of heat transferred by radiation:
QR = ε1,2σ0 T4
w −T4
f
□
□
F,
(7.141)
where Tw and Tf are temperatures of the body and fluid; σ0=5.668□10−8 W/(m2 K4); ε1,2 is
the emissivity of the surface of the body system (ε1) and of the water (ε2). F—body surface
area (m2).
2. The amount of heat transferred by conduction through the vapor layer to the water:
Qλ =
2ffiffiffiπ
p
ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
λf ρf cpf
q
ffiffi
f
p
Tw −Tf
□
□
F1,
(7.142)
where f is the frequency of the bubble formation (Kocamustafaogullari and Ishii, 1995) given
by:
f = 1:18
d
σgΔρ
ρf
□
□2
"
#0:25
;
(7.143)
d is the detachment diameter of vapor bubble,
d = 2:42□10−5p0:709a
ffiffiffiffiffiffi
bΦ
p
;
(7.144)
