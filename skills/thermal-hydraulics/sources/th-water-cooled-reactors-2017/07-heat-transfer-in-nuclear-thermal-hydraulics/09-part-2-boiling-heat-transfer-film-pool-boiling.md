# Part 2: Boiling Heat Transfer — Film pool boiling
<!-- source PDF pages 87-91 -->

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
