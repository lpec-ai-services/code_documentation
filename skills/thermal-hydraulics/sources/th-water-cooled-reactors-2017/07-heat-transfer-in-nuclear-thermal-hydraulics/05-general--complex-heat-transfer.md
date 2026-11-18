# General: — Complex heat transfer
<!-- source PDF pages 56-63 -->

<!-- page 412 (PDF 56) -->
length, e.g., the layer thickness, and 1/βλ can be regarded as the mean free path
of photons. If βλ is large (shorter mean-free-path), penetration depth is small,
while for small βλ (longer mean-free-path) the penetration depth is deep. In this
way, the optical thickness is the ratio of the characteristic dimensions of the
length of the radiation penetration. When the optical thickness Lλ≫1, the
medium is said optically thick (the characteristic size of the system is significantly
larger than the mean photon path length). If Lλ≪1 the medium is called
optically thin and if Lλ ⃗ 0 the medium is not involved in heat exchange (transparent
or diathermic medium).
Engineering calculation methods of radiative heat transfer often use the effective
thickness of the emitting layer (leff). For a medium with a volume V and a small optical
thickness (Lλ≪1)
leff = 4V
A :
(7.101)
Here A is the surface area.
In many practical situations we encounter, we find Eq. (7.101) often overestimates
the optical thickness of layers l. Therefore, we decided to use formula
leff = 3:6V
A ,
(7.102)
which reflects a real balance between the effective values leff and the equivalent
thickness layer l0 (Blokh, 1991).
Effect of optical layer thickness L on the effective thickness l is accounted for as
follows:
leff = 3:6V
A
Le−L
L + e−L + Le−L −1:
(7.103)
For L=0, the effective thickness of the layer leff becomes l0 and defined by
Eq. (7.102).

## 7.4 Complex heat transfer

### 7.4.1 The complex heat transfer and basic principles of calculation

Two or more heat transfer mechanisms often act simultaneously, for example:
thermal
conduction
and
radiation
(λ-r),
convection
and
radiation
(c-r),
convection-conduction (c-λ), or even all three together. The usual method of complex
heat transfer calculations is a summation of the heat fluxes of each heat
exchange mechanism:
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 413 (PDF 57) -->
q = qλ + qc
q = qc + qr
q = qλ + qc + qr
(7.104)
The approach is valid only if each mechanism shown on the right-hand-side of the
equation does not affect the other(s), i.e., if there is no interactions among them. This
usually occurs when a magnitude of one component of the heat flux is significantly
different from the other(s) (€Ozisik, 1973; Kokorev and Kharitonov, 1986)
There are two types of interaction effects of concern:
1. The effect of radiation in an absorbing medium appears in the similar form of the heat
sources or sinks in the heat conduction or convection. This problem becomes nonlinear;
2. The interaction of radiation can change the boundary conditions.
A special case of complex heat transfer is the simultaneous transport of heat by
radiation (qr) and directional flow of electron flows direction that are emitted from
a heated surface (cathode) to the other, colder (anode) surface (qe):
q = qr + qe
(7.105)

### 7.4.2 Radiation heat transfer between flow of emitting gas and wall

#### 7.4.2.1 Radiation and conduction

We now consider here a stationary system involving the absorption and conduction by
the gas medium. The problem is characterized by the following parameters: optical
thickness of the medium (L, see Section 7.3.5); emissivity of the surfaces (ε1 and ε2);
relative temperature of the cold surface to the hot surface (θ = T2=T1) and the parameter
N =
λa
4σ0T3
, where λ is the thermal conductivity of the gas; a is the gas absorption coefficient
; and σ0 is Stefan-Boltzmann constant. The parameter N characterizes the interaction
intensity of heat transfers by conduction and radiation: if N ⃗ ∞(T1 at lower
temperature), heat is transferred only by thermal conductivity; if N ⃗ 0 (at higher temperature
T1), heat is transferred only by radiation.
Here are two extreme cases:
–
Optically thin gas layer (L ⃗ 0). The radiation heat is not absorbed by the gas but practically
by every surface element of the medium that interacts with the radiation coming directly
from the boundary surfaces. The total heat flux will be given, with qr = αr T1 −T2
ð
Þ and
qλ = αλ T1 −T2
ð
Þ, by q = qr + qλ = αr + αλ
ð
Þ T1 −T2
ð
Þ, which is also written as:
q = εredσ0 T4
1 −T4
□
□
+ λ
δ T1 −T2
ð
Þ:
(7.106)
The first term on the right-hand-side of Eq. (7.106) is Eq. (7.91) with the reduced emissivity
defined in Section 7.3.4.

<!-- page 414 (PDF 58) -->
–
Optically thick gas layer (L ⃗ ∞). The radiation heat is readily absorbed by the gas. Radiation
properties of the surfaces affect only the layers of gas within a distance much smaller
than the size of the system. In this case, the radiation heat transfer approaching the diffusion
process, the analogy with the thermal conductivity of the gas can be made. The heat flux is
expressed by:
q = 4
σ0
aλ T4
1 −T4
□
□
+ λ
δ T1 −T2
ð
Þ:
(7.107)
In general, the radiation beam penetrates the surface of the medium volume and is
partially absorbed. This affects the temperature distribution within the volume and
thus changes the thermal conductivity under the heat transfer conditions. This is
the most complicated case, and the total heat flux q cannot be obtained readily by
adding qλ and qr because of their strong interconnected behaviors.
The temperature level of the nuclear fuel depends on the thermal conductance λ/δ at
a radial clearance δ between the fuel pellet and cladding as it determines the temperature
drop. The value λ/δ depends on the design of fuel element (cladding diameter,
gap, etc.), the properties of the cladding and fuel materials, surface conditions (roughness
, coatings, presence of the oxide films), properties of the fission gas and fill-in gas,
its pressure, and the metallurgical and many other processes occurring in the fuel
during irradiation (Fig. 7.37).
The radiation heat flux is estimated by qr = αr T1 −T2
ð
Þ, where αr is the gap thermal
conductance given by:
αr = εred4σ0T3,
(7.108)
T2
T1
e1
e2
d
Fig. 7.37 Calculation of complex heat transfer in the gaseous fuel rod gap.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 415 (PDF 59) -->
where εred =
ε1
+ 1
ε2
−1
□
(−1
and T = Т1 + Т 2
is the average temperature in the gap
region.
For a temperature of the inner surface of cladding 350–700°C and the temperature
difference in the gap 600–700°C, you may find αr	50–150 W/(m2 K), i.e., the heat
transfer by radiation under the operating conditions is in most cases less than 10% of
the total heat flux. In evaluating the gap conductance, it is important to take into
account the changes in many parameters over the nuclear reactor operation period,
including the gap size, thermal conductivity of the gas in the gap, and the mass transfer
of fuel due to evaporation/condensation.

#### 7.4.2.2 Radiation and convection

Consider we have both radiation and convection in practical engineering problems.
In most cases, the two heat fluxes are assumed to be independent and dealt with
separately: q = qr + qc. This assumption is accurate enough if one of the two heat
fluxes is significantly smaller than the other.
Sometimes there are cases where three mechanisms of heat transfer (heat conduction
, convection, and radiation) are to be considered. An example is the heat transfer
through an insulated circular pipe with an outer diameter of the insulation d2, heat
transfer coefficient αc by convection and αr by radiation to the environment
(Fig. 7.38). Temperatures on the insulation surfaces are T1i and T2i. The heat flow from
the unit length q0 (W/m) will be equal to:
q0 =
π T1i −T2i
ð
Þ
α1d1
+ 1
2λw
ln d
d1
+ 1
2λi
ln d2
d + 1
αd2
:
(7.109)
Ra1
Rw
d1
d
d2
Ri
Rr
qr
qcon,a2
Ra2
Fig. 7.38 Calculation of heat transfer
from the coolant through a conduit with
insulation: its equivalent electric circuit
diagram.

<!-- page 416 (PDF 60) -->
Thermal resistance of the heat transfer inside the pipe is 1/(α1d1) and the thermal
resistance of the pipe wall
2λw
ln d=d1
ð
Þ can be neglected for simplicity. Thermal
resistance of the heat transfer at the outer insulation surface is due to the radiation from
the insulation surface and the convection:
α =
αr T2i
ð
Þ + 1
αc
;
(7.110)
therefore, three parameters in two Eqs. (7.109), (7.110), i.e., q0 the linear heat rate of
the insulated pipe, αr the radiation heat transfer coefficient with the surface insulation,
and T2i the surface temperature of the insulation are depending on each others. With
the ambient temperature to be provided, the problem is solved by the successive
approximation.

### 7.4.3 Contact heat transfer

#### 7.4.3.1 Contact resistance

Nuclearfuelelementsusuallytaketheformofthefuelpelletsinsidethecladding,where
with a gap between them the mechanical contacts are assumed. The thermal conductance
of such contact is of the order of 103–104 W/(m2 K). When the heat flux is
□106 W/m2 and a temperature difference across the contact could be a hundred degrees
or more. However, as noted in Section 7.4.2, radiation heat transfer hardly affects this
temperature difference. For more information, see Holm (1967), Shvetz and Dyban
(1964), Shlykov (1965), Shlykov et al. (1977), and Kharitonov et al. (1973).
Thermal contact resistance plays an important role in problems of semiconductor
thermoelectric generators, thermionic converter of nuclear energy into electrical
energy, in devices operating in the vacuum of space. For example, see Clausing
and Chao (1965) and Fried and Costello (1962).
Conventional nuclear reactor fuel materials are metal alloys, oxides, carbides,
nitrides, uranium, and plutonium metals
(Boeschofen, 1955; Miller, 1962;
Avduevsky and Koshkin, 1992; €Ozisik, 1973; Popov, 1977; Spiridonov et al.,
1974; Rapier et al., 1963; Waltar and Reynolds, 1981). The thermal contact resistance
between the metallic cladding and the ceramic fuel (UO2, UC, UN, etc.) is particularly
a difficult issue (Miller, 1962) for the following reasons: first, the ceramic fuel does
not come into close contact (i.e., plane mode) with the cladding inner surface; second,
because of the ceramics’ poor thermal conductivity and high hardness, the conductivity
of the actual contact points may be small.

#### 7.4.3.2 Rough surfaces

Actual contact area between two solid surfaces is essential information to evaluate
contact resistance (Dyomkin, 1962; Dyl’nev, 1963; D’iachenko et al., 1963;
Kaganer and Zukova, 1966; Miller, 1962; Bahrami et al., 2006). The contact
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 417 (PDF 61) -->
resistance is a relative concept, because the actual surface roughness and waviness of
the contact surfaces between solids are of a discrete nature. Some of the heat goes
through the contact spots of solids and other through the gaseous gaps. Since the thermal
conductivity of the contact spots is higher than that of the gaseous medium in the
gap, the heat flow streamlines are highly congested toward these local spots with the
thermal contact resistance R = ΔT=q, where ΔT is the temperature difference at
the contact position.
For many surfaces encountered in engineering practice, a population density of the
contact points, therefore, a degree of concentration of lines of the heat flow, has a definite
influence on the thermal contact resistance (see Fig. 7.39A; Latyev et al., 1974).
Inverse of the thermal contact resistance 1/R is the thermal conductance (=α) of
the contact. The total contact resistance is made up of two resistances in parallel—
one of the gaseous medium in the gap (Rg) and the other of the mechanical contact
spots (Rm):
R = 1
Rg
+ 1
Rm
,
(7.111)
where Rg is determined by the gap width and conductivity λg of the medium
filling the gap; Rm is the actual contact resistance based on the contraction of the
heat flow streamlines. When the gap is 20 μm wide and filled with air,
Rg = δ
λ = 20□10−6
3:2□10−2 = 6:2□10−4 (m2 K/W). It is noted that this resistance is equivalent
to the resistance of ST-3 steel plate of thickness 33 or 150 mm thick aluminum.
Eq. (7.111) is rewritten in terms of the thermal conductance (αg and αm) and the
fraction of actual contact area S to the total surface area η=S/A:
α = αg 1−η
ð
Þ + αmη,
(7.112)
(A)
(B)
ΔTc
ΔTc= 0
(C)
Fig. 7.39 Heat flow line (—) and isotherms (- - -) at the contact between two plates (A);
temperature distribution in an ideal location (B); and real (C) at the contact.

<!-- page 418 (PDF 62) -->
η and S depend on the characteristics of roughness and waviness of the surfaces, their
mechanical properties, compression force and other parameters.
In calculations, it is usually assumed that the actual contact area S formed by a plurality
of circular spots of radius a, in which the heat flow streamlines are “pulled
together” (Fig. 7.39A). The corresponding additional thermal resistance associated
with the curvature of the heat flow streamlines is taken into account by introducing
a correction factor ψt.
If the mean free path of the gas molecules in the gap is commensurable with size of
the gap, the gas may not be regarded as a continuous medium. Then, the discreteness
of gas properties leads the temperature, instead of a linear profile, to have a distribution
in the planar gap region, resulting in a temperature drop (jump) as shown
in Fig. 7.39C. To characterize this distortion, we introduce a concept length of “a
temperature jump” (ΔT1+ΔT2), which is equivalent to an increase in the thickness
of gas layer (l1+l2). The length of a temperature jump would be l 	 ‘=ξ, where ‘ is
a mean free path length of the molecules, ξ is the accommodation coefficient
(see below).
In view of the above effect, the thermal resistance at the gas gap can be written as:
Rg = 1
αg
= δe
λ + l1 + l2
λ
= δe
λ + 1
α*
,
(7.113)
where α* = ξe
γ + 1
γ −1 · p
ffiffiffiffiffiffiffiffiffiffiffiffi
k
2πMT
r
; γ = cp
cv
; p is the pressure (Pa); k is Boltzmann constant
(=1.38□10−23 J/K); T is the temperature (K); M is the molecular mass of the gas; ξe is
the equivalent accommodation coefficient associated with the accommodation
coefficients on the surfaces 1 and 2 by the relation 1/ξe=1/ξ1+1/ξ2−1.

#### 7.4.3.3 Accommodation factor

Accommodation coefficient characterizes the energy transfer efficiency of the
gas molecules to the surface and depends on the nature of the gas and the surface material
. The higher the molecular weight of the gas, the higher the accommodation
coefficient:
ξ =
μ
2 1 + μ
ð
Þ,
(7.114)
where μ≡Mg=MW is the ratio of atomic (molecular) mass of the gases and the surface
material.
The amount of heat conduction through the gas layer between the fuel pellet and
cladding in the nuclear fuel rods are not strongly dependent on the composition of the
gas (Fenech and Rohsenow, 1963). Thickness of the gas layer, in which the temperature
jump is observed at the boundary of gas and solid body, is given by δg 	 ‘=ξ,
where ‘ is the mean free path, ξ is the accommodation coefficient, the fraction of
the molecular energy that is exchanged with the wall per one collision.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 419 (PDF 63) -->
Thermal conductivity at the gap, then, may be given by:
α □ λ
δg
= λξ
l :
(7.115)
From λ □ 1=
ffiffiffiffiffiffi
Mg
p
, ξ □
ffiffiffiffiffiffi
Mg
p
, where Mg is the atomic mass of the gas in the gap, we
can see that α is weakly dependent on the type of gas. The heat transfers through
the actual contact point and even due to radiation reduce the effect of this dependence.
However, as the burnup increases and hence the pressure in the fuel element, this
relationship given by Eq. (7.115) may be slightly modified as indicated in the next
table:
Gas
He
Ne
Ar
Kr
Xe
λξ (MW/m K)
4.6
3.2
4.0
3.1
4.1
α (kW/m2 K)
1.5
2.0
3.4
2.9
4.0
The thermal resistance R (in Eq. 7.111) decreases with increasing contact pressure of
the contact surfaces. While at low contact pressures and temperatures, almost 80% of
the heat is passing through a gas layer, at high temperatures and high contact
pressures, more than 90% of the heat goes through the contact points.
Taking into account the factors mentioned just above, the relationship of the
contact conductivity Eq. (7.112) can be written as:
α = λ
δe
1−η
ð
Þ +
πa2Rψtψk
η,
(7.116)
where λ is the thermal conductivity of the medium in the gap; R is the thermal resistance
of an ideal contact between two infinite surfaces; δe =
A
ð
A
dA
δ A
ð Þ + 2lт
is an equivalent
thickness of the gap based on the lengths of the temperature jump;
ð
A
dA
δ A
ð Þ + 2lт
	 h1 + h2
□
□
+ 2lт; h1 and h2 are the average height of roughness; lт—the
length of temperature jump; ψk—correction factor taking into account tapering the
roughness; a—the average radius of the contact points.
Data evaluation and modeling the equivalent gap are controversial, due to the influences
of the distribution function of height and shape of roughness. The equivalent gap
may be defined by profilogram surface.
The complexity of calculating the contact heat transfer with Eq. (7.116) is associated
with many difficulties in determining the quantities involved among the relationship
(δe, η, a, ψt, ψk).
There are two popular theories (models) for the contact resistance. One theory
suggests an elastic deformation of roughness elements on the contact surfaces. Other
is their plastic deformation. For further reading, see McWald and Marschall (1993),
