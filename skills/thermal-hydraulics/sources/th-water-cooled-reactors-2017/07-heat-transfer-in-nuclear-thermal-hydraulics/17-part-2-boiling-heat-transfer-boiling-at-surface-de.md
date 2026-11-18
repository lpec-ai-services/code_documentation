# Part 2: Boiling Heat Transfer — Boiling at surface deposition
<!-- source PDF pages 114-118 -->

<!-- page 470 (PDF 114) -->
Nu0 = Nu∞εl, where εl = 1 +
0:48 1 + 3600= Re
ffiffiffiffiffiffiffi
x=d
p
□
□
h
i
x=d
ð
Þ0:25
e−0:17x=d;
(7.171)
Nu∞=
ξ=8
ð
ÞRePr
1 + 900=Re + 12:7
ffiffiffiffiffiffiffi
ξ=8
p
Pr2=3 −1
ð
Þ
; and
(7.172)
ξ = 1:82 ln Re=8
ð
Þ
½
□−2:
(7.173)
For Pr=0.65–1 good results are obtained by a simple formula:
Nu∞= 0:0225Re0:8
f Pr0:6
f
□2%
(7.174)
Eq. (7.170) can be rewritten as:
Tw
Tf
= 1 + K exp
K 0:013f
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
(7.175)
which allows you to immediately calculate the local wall temperature for q, d, G, Tf.
Eq. (7.175) can be simplified for x/d>50, in which f (x/d)=1:
Tw
Tf
= 1 + K exp K 0:013 + 1:4K
½
□
f
g
(7.176)

## 7.9 Boiling at surface deposition

### 7.9.1 Key processes and mechanisms

The deposits on the surfaces of the fuel elements and the steam generators are due to
impurities, which enter the water mainly
(1) with suction of cooling water in the condensers;
(2) with compensate water to recover the losses due to leakages of water and steam and due to
blowdown of the steam generator;
(3) with impurities introduced into the water loop for adjusting changes in the water level;
(4) as the corrosion products of equipment components;
(5) in the form of fission products and particles of nuclear fuel (with infringement of hermetic
fuel cladding tightness).
The deposits formed on the steam-generator tube surfaces are called scales. They differ
in chemical-phase composition and structure. In the energy sector, the following
types of scale (as the dominant component) are representative: (1) calcium and magnesium
; (2) iron oxide; (3) iron phosphate; (4) ferromagnetic and aluminosilicate; and
(5) copper.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 471 (PDF 115) -->
There are two mechanisms of deposits formation on the surface during boiling:
first—connected with the processes of crystallization of impurities that fall from a
supersaturated solution of water; and second—sticking to the surfaces of the colloid
or particulate solids (or sludge crud5). A result of the first mechanism is the formation
of a dense layer of the solid phase and little porous surface. The second provides a
formation of sufficiently loose sticky layer between itself and the particles surface.
These particles may come off into the fluid flow and fall back again onto the surfaces,
depending on the hydraulic and temperature conditions in a different part of the circuit
. In nuclear power plant (NPP) systems, formation, entrainment, and migration of
the particles which are sparingly soluble corrosion products, along the coolant circulation
systems determine to a large extent the radiation dose distribution at the NPP
(e.g., Voronov et al., 2006; British Nuclear Energy Society, 2000).
Deposits of corrosion products in nuclear power circuits are in many cases poorly
soluble even in concentrated acids and alkalis. One reason for this is the deep hydration
precipitation at high temperatures and pressures. Another reason is the presence in
the sediments of the metal silicates. Silicic acid enters the coolant circuit from the feed
water or structural materials (for steels 1H18N10 type, Si content may be up to 1%).
During the circuit loop operation, usually 20%–80% of the metal is corroded in the
circulating water. The intensity of the deposits and their physico-chemical properties
are dependent on the concentration of impurities (e.g., iron oxide) and dispersion spectrum
of particle sizes. Most of the particles (65%–80%) have a size of 0.9–1.3 μm. The
precipitation of iron oxides cannot be described simply by a single system, since there
exist the processes of different nature at the same time. For example, the results of
industrial research show that the formation time of iron oxides in the boiler tubes
is subject to:
M = A exp
−B
T
□
(
τc,
(7.177)
where M is in g/m2; T is in K; τ is in hours. The constants A, B, and C in this formula
depend on the steel grade and the water pH (Table 7.12).
In modern power plants, which are constructed with different grades of steel, strict
water quality control is required. There the basic substances dissolved in water are
primarily iron compounds in the form of magnetite (Fe3O4) and hematite (Fe2O3).
Since the solubility of magnetite in water is higher than in vapor, the magnetite aerosol
formation will be prompted out of its solution in the vapor environment. Individual
particles (aerosols) of magnetite are in a shape of sphere with a diameter of
0.1–0.5 μm, which are easily stick together, forming deposits on the porous surface.
The deposits form two layers (Fig. 7.61) on the surface. The inner layer has a dense
structure. It is formed by oxidation of the steel surface and its thickness varies parabolically
with time. The outer, thicker layer, has a loose structure and is formed due to
5crud—chalk river unidentified deposit.

<!-- page 472 (PDF 116) -->
deposits at boiling of flowing water. Some characteristics of the layers are shown in
Table 7.13.
Hereafter we focus on the influences of this surface deposition onto the heat
transfer.
A characteristic feature of typical layer of deposited materials is the presence of
large porous openings (“steam trunks” about 5 μm), the density of such holes reaches
5000 pores/mm2. This structure provides a so-called “wicks boiling” (see Fig. 7.62).
The dissolved substances in water (compounds of Cr, Ni, Mn, Zr, Cu, Al, and
others) form thick solid structures which are stronger magnetite but can be peeled
off from the surface at the cyclic temperature changes. The porosity of the magnetite
Table 7.12 Constants A, B, and C in Eq. (7.177)
pH
Steel grade
A
B
C
pH 7–8
12X1M[Fcy]
3.91□106
0.25
12X18H12T
0.38
pH 9–10.5
12X1M[Fcy]
6.57□105
0.26
12X18H12T
0.41
d2
d1
Fig. 7.61 Two layers of the deposits on the surface (internal—δ1 and external—δ2).
Table 7.13 Characteristics of Layers 1 and 2
pH
Characteristics
pH 9
Density (g/cm3)
4.4–4.7
1–4
Chemical composition
Fe3O4
Fe3O4
Porosity (%)
20–75
pH 7
Chemical composition
Fe2O3
Fe3O4
Porosity (%)
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 473 (PDF 117) -->
scale is □65%–70%, and “steam channels” occupy□10%. When pores are filled with
other compounds the process of matchlock boiling abates. It is noted that a majority of
the heat transfer in this case is carried out by the thermal conduction through the layer,
which causes an increase in the heated surface temperature (while maintaining the
values of heat flux).

### 7.9.2 Composition and thermal conductivity of the sediments

The water may be present ferrous iron compound constituting FeO, compounds containing
di- and trivalent iron forming Fe3O4, ferric compounds, turning into Fe2O3.
The main parameters that determine the shape of the iron oxides are pH value of
pH, temperature and redox potential of the system.
At a temperature□400°C, thermodynamically stable oxide is magnesia. Under the
condition of the high oxidation potential (high oxygen concentration) and higher temperature
, the stable oxides may be hematite or its hydrated forms.
Theoretical density of the magnetite Fe3O4 is 5180 g/cm3, and the density of
the outer (loose) layer is 1.25–4.1 g/cm3, which corresponds to the porosity of
75%–20%.
The thermal conductivity of porous sediments can be approximated by the
following:
3 4
p2
p1
Fig. 7.62 Model Macbeth—flow circulation in the deposits with high rate of evaporation
of the readily soluble compounds in vapor sediments: 1—the flow of water under pressure p1;
2—exit of steam “steam trunks or steam pipe” with pressure p2 as a result of consistent
formation and the separation of the vapor bubbles; 3—capillary channels (wicks), sucking
liquid to the bottom of the “steam pipe”; 4—the thickness of the sludge sediments; 5—the
surface of the metal; 6—heat flux direction.

<!-- page 474 (PDF 118) -->
–
at the location perpendicular to the direction of the heat flux 1
λ = 1−φ
λ1
+ φ
λ2
, where λ1, λ2 are
thermal conductivity of the sediments in the pores and φ is the porosity.
–
at the location parallel to the direction of the heat flux (usual direction)
λ =
λ1ν 1−ϕ 1−ν
ð
Þ
½
□
νA + 1−A
ð
Þ 1−ϕ 1−ν
ð
Þ
½
□ ν + ϕ 1−ν
ð
Þ
½
□,
(7.178)
where ν=λ1/λ2, A is the empirical coefficient and is 0.94.
A more sophisticated method is described in Chudnovskaya et al., 1978, where the
thermal conductivity of the compounds of hematite (Fe2O3) and magnetite (Fe3O4)
is given by:
λ = 13:215−0:375□10−1T + 0:379□10−4T2 for Fe2O3
(7.179)
λ = 4:133−0:852□10−2T + 0:757□10−5T2 for Fe3O4
(7.180)
where λ in W/(m K), and T in °C.

### 7.9.3 Effects of deposits on the flow resistance and heat transfer coefficient

The sediments on the surface of the flow circuit leads to: (1) reduction in the
cross-sectional flow area of the channels, which becomes particularly noticeable
for channels of a small hydraulic diameter; (2) increase in the surface roughness. Both
effects are not difficult to be taken into account in the calculation of hydraulic resistance
, if the thickness of the deposits and the roughness are known although it is
difficult to predict in advance such parameters due to the large number of factors that
associate with them. Therefore, it is usual to rely on special experiments, empiricism,
or industrial experience.
If the heat flux (q) and the heat transfer coefficient for a “clean” environment α0 are
specified, we can calculate the temperature of the outer surface of the heat-wall:
Tw = Tf + q=α0,
where Tf is the average temperature of the bulk coolant.
For the surface conditions with deposits, we have similar relationship:
Tw = Tf + qR, where R = 1
K = 1
α + δ
λ is the total thermal resistance at the surface, consisting
of two parts (heat transfer resistance 1/α and thermal resistance of sediments
δ/λ). There δ and λ are the thickness and thermal conductivity of scale, respectively; α
is the coefficient of heat transfer from the surface of the scale to the flowing liquid.
If we keep in mind the roughness of the surface sediments and the ability to “wick
boiling” layer (see above), we should assume α>α0. Take into account α=α0, then
we obtain higher values of Tw, which can go to conservative calculations.
Thermal Hydraulics in Water-Cooled Nuclear Reactors
