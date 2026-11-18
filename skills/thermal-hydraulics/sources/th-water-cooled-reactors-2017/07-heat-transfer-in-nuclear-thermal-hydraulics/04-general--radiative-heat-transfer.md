# General: — Radiative heat transfer
<!-- source PDF pages 43-55 -->

<!-- page 399 (PDF 43) -->
(Zhao et al., 1990). This is achieved by coating the surface with the Cu-Cr-N 0.9 mm
thick alloy layer. The coating is carried out by the ion implantation of Cr and N so that
the crystal structure of the surface layer of copper is transformed into amorphous.
The thermal resistance of the coating has become negligible and the heat transfer
coefficient is 20–40 times higher than that for the film condensation.

## 7.3 Radiative heat transfer

### 7.3.1 Basic principles

Thermal radiation is a portion of the process of energy propagation by means of electromagnetic
waves. When it is in thermodynamic equilibrium with a substance, we
call it an equilibrium radiation. The radiation results from changes in electronic, vibrational
, and rotational states of the atoms-molecules and the emission of the radiant
energy takes place as a result of irregular deceleration of charged particles (electrons,
ions) in the media. The reverse process is then what occurs when radiant energy
impinges on a solid surface and causes its temperature rise (absorption).
From a corpuscular point of view, the radiant energy is emitted and absorbed in
discrete forms of the electromagnetic waves, which could be described as if particles
with mass zero and charge zero, i.e., photons are carrying energy with the speed of
light c. The photon energy is hν, where h = 6:626□10−34Js is the Planck constant,
ν is the frequency of an electromagnetic wave. Note that the photon has momentum
hν/c. The wavelength λ, characterizing an electromagnetic wave, is related to its frequency
ν by the equation c = νλ. The speed of light c = c0 (=299,792,458 m/s exactly)
in vacuum, c 	 c0 in gases, and in other media c < c0. The ratio n = c=c0 is refractive
index. The frequency does not change when the electromagnetic wave passes through
from one medium to another, but the wavelength because the light speed changes. Distribution
of radiation energy per frequency (or wavelength) is radiation spectrum.
The spectrum of equilibrium radiation is independent of the nature of the substance
and determined by Planck’s law of radiation. Thermal radiation field in the electromagnetic
spectrum covers a range of wavelengths□10−7–10−4 m (see Fig. 7.30),
i.e., in the visible and infrared regions (Hackford, 1960). The visible part of the spectrum
covers a wavelength of 0.40–0.76 μm. The infrared region of the spectrum consists
of a near-infrared region (0.76–25 μm) and the far infrared region (25–1000 μm).
A main portion of the thermal radiation energy falls on the wavelengths region
of 0.76–15 μm, i.e., lies in the near infrared. Radiation in the visible region of the
spectrum is significant only at very high temperatures.
Thermal radiation can be viewed as a surface phenomenon because thin surface
layers (−0.001 to 1 mm) on the body are involved in the radiative heat transfer.
Bodies can radiate energy of all wavelengths λ = 0−∞(a continuous spectrum) or
selectively to a specific wavelength range (selective spectrum). With a change in temperature
, not only the intensity but also structure of the radiation (spectrum) varies.
There are monochromatic and full (integral) radiation modes. Monochromatic
radiation corresponds to that of a narrow wavelength range λ □ λ + dλ
ð
Þ.

<!-- page 400 (PDF 44) -->
Integral radiation (full spectrum) is associated with the total radiant energy emitted
from a body Q (W); in the entire wavelength range 0<λ<∞, the integral flux density
of the (hemispherical) radiation, i.e., the radiation flux emitted from the unit area per
unit time we call emittance (or emissive power) E = dQ=dA (W/m2). Thus Q =
ð
A
EdA.
Emittance in an infinitesimal range of wavelengths divided by this interval is called
the spectral density of radiation flux (spectral or monochromatic emittance):
Jλ = dE=dλ (W/m3).
The amount of energy, emitted per unit time in the angular direction ψ the elementary
area dA, per unit solid angle ω and per unit area of the projection onto a plane
perpendicular to the direction of radiation, is called the brightness (intensity) of
radiation:
I = d2Q
dωdAn
= d
dω
cos ψ
dQ
dA
□
(
= dEn
dω , with dAn ≡dA cos ψ and En = dQ
dAn
:
(7.69)
dI
dλ = Iλ is called the spectral brightness.
Thermal radiation energy impinging on the body can be absorbed, reflected, or can
pass through the body:
QA + QR + QD = Q, thus QA
Q + QR
Q + QD
Q = 1 or A + R + D = 1,
(7.70)
Radiowaves
γ-rays
–12
–10
1 A
1μm
1cm
1 m
1 km
–8
–6
–4
–2
Infrared radiation
10–6
10–7
10–5
10–4
Ultraviolet radiation
Thermal
radiation
X-rays
Ig(l)
l, m
Cosmic rays
Visible
light
Fig. 7.30 Portion of the thermal radiation in the electromagnetic spectrum.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 401 (PDF 45) -->
where A, R, and D correspond to the absorbance, reflectance, and transmittance (transparency
) of the material body. Here note that A is a fraction of absorption and should
be distinguished from the area A in m2. Particular cases of this equation leads us to
concepts of ideal bodies, i.e.,
A=1; R=D=0—absolutely blackbody;
D=1; A=R=0—completely transparent;
R=1; A=D=0—absolutely mirror.
Dry air, mono- and di-atomic gases at temperatures below 3000 K can be regarded as
transparent (diathermic).
Most of the solids are opaque, so that D=0 and A+R=1. In this case, the reflectivity
and absorptivity of the body are interconnected. A blackbody does not exist, and
usually A<1 (gray body). In general, the absorbance depends on the wavelength.
Such substances show selective absorption (see Fig. 7.31). Classification of different
types of radiation is shown in Fig. 7.32. There, E is the own radiation; Einc is the
incident of radiation on the body; Eabs=AEinc is the absorption of radiation;
Eref = (1−A)Einc is the reflected radiation. A sum of the own and reflected radiations
is called the effective radiation Eeff = E+Eref = E+(1−A)Einc. It is noted that Eabs,
Eref, and Eeff are linear functions of Einc. Properties (spectral content) of their own
and the reflected radiations may be different.
l
0.5
1.0
Al
Fig. 7.31 Absorption of different material bodies: — ideal blackbody; - - - gray body;
-·-·-· selective absorption body.
E
I
I
II
II
Eref =(1–A)Einc
Eabs= AEinc
Einc
Eeff
Fig. 7.32 Classification of different
types of radiation; I and II are the layers
infinitesimally close to the surface.

<!-- page 402 (PDF 46) -->
Thermal radiation flux can be given from the heat balance. For the plane I-I
(Fig. 7.32), we have:
qres = E−Eabs = E−A · Einc,
(7.71)
For the plane II-II in Fig. 7.32:
qres = Eeff −Einc,
(7.72)
By eliminating Einc from these equations yields:
Eeff = qres 1− 1
A
□
(
+ E
A
or
qres =
E
1−A−
A
1−AEeff :
(7.73)
More discussions on radiation heat transfer are provided in many monographs and text
books, e.g., by Adrianov (1972), Blokh (1962), Cess (1964), Klimenko and Zorin
(2001), Spalding and Taborek (1983), and Sparrow and Cess (1978).

### 7.3.2 Laws of thermal radiation

Thermal radiation laws apply to the equilibrium radiation of blackbody.2 When all the
bodies that are involved in the system take the same temperature, qres = 0 and the radiation
is called as equilibrium (black). A heated blackbody emits photons, the spectrum
of which depends only on the temperature. In the case of a gray body, radiation spectrum
depends, besides the wavelength, on physical properties and surface conditions
of the body, and can only be determined experimentally.
7.3.2.1
Planck’s law (Fig. 7.33)
Spectral distribution of the radiation flux of a blackbody is expressed by a function of
the wavelength and temperature.
J0λ =
C1
λ5 eC2=λT −1
ð
Þ,
(7.74)
where C1—first radiation constant; C2—second radiation constant, λ—wave length
(m); T—absolute temperature (K). All the fundamental constants are shown in
Table 7.4.
2Values characterizing the blackbody radiation will be designated by the subscript 0.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 403 (PDF 47) -->
Another expression for this law is using λ=nc0/ν:
J0ν =
2πh2n2ν3
c2
0 ehν=kT −1
ð
Þ,
(7.75)
where h is the Planck’s constant; k is the Boltzmann constant; c0 is the speed of light in
vacuum and n = c=c0 is the refractive index of the medium.
With the Stefan-Boltzmann constant σ, the law in the form of:
J0λ
σn3T5 =
C1=σ
nλT
ð
Þ5 eC2=nλT −1
ð
Þ
,
(7.76)
Jl·10–9, W/m3
l, μm
T= 1400°C
Fig. 7.33 Graphical representation of the Planck’s law.
Table 7.4 Fundamental constants in the law of radiation
Planck’s constant
h
6.6260□10−34
J/s
Boltzmann constant
k
1.38066□10−23
J/K
Speed of light in vacuum
c0
2.99792□108
m/s
Stefan-Boltzmann constant
σ0 = 2k4π5
15h3c2
5.6705□10−8
W/(m2 K4)
First constant of radiation
C1 = 2πhc2
3.7418□10−10
W m2
Second constant of radiation
C2 = hc0
k
1.4388□10−2
m K

<!-- page 404 (PDF 48) -->
leads to a conclusion that J0λ/(σn3T5) is a function of only one variable nλT.
Two limiting cases of the Planck’s law are in the following:
(1) with λT≫C2 (or hν≪kT), i.e., at high temperatures or long wavelengths λT > 1:4□10−2
(m K)
J0λ = C1
C2
· T
λ4 = С3 · T
λ4 ,
where C3=2.60110−8 W m/K. This expression is known as the Rayleigh-Jeans law.
(2) with λT≪C2 (or hν≫kT), i.e., at low temperatures or short wavelengths λT < 1:4□10−2
(m K), the Planck’s law becomes the Wien’s law:
J0λ = C1
λ5 e−C2=λT:
(7.77)
The position of maximum of the radiation intensity is obtained from Eq. (7.74),
equating dJλ/dλ zero. As a result,
λT
ð
Þmax = 2:8978□10−3 mK
ð
Þ or hνmax=kT = 2:8214:
(7.78)
These expressions are called the Wien’s displacement law. For example, maximum
solar emission is observed at λmax = 0:475□10−6m, which suggests that the sun’s
surface temperature is about 6100 K.
Maximum radiation intensity corresponding to the wavelength is determined from
the relation:
Jmax
0λ
= С4T5,
(7.79)
with C4=1.33□10−5 W/(m3 K5).
Stefan-Boltzmannlaw:Atotal amountofenergyradiatedbyablackbodyper unittime
per unit area in the entire range of wavelengths (frequencies), i.e., the total blackbody
radiationfluxisobtainedbyanintegralofspectraldistributionofPlanck’slaw,Eq.(7.74):
E0 T
ð Þ =
ð∞
Jλdλ =
ð∞
C1
λ5 eC2=λT −1
ð
Þdλ = E0 = σ0T4,
(7.80)
where σ0 = 2π5k4
15c2
0h3 = C1
π
C2
□
(4
=5.67□10−8 W/(m2 K4) is the Stefan-Boltzmann
constant (radiation constant of absolute blackbody).
For gray bodies, own radiation is proportional to the fourth power of the
temperature. Then the Stefan-Boltzmann law takes the following form:
E = εE0 = εσ0T4:
(7.81)
where ε = E=E0 is the thermal emissivity (integral emissivity or emissivity).
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 405 (PDF 49) -->
Kirchhoff’s law establishes a relationship between emittance and absorbance of
any material (gray and black) bodies in thermodynamic equilibrium. The ratio of
emittance (E) of the gray body to its dimensionless coefficient of absorption A given
by Eq. (7.70) is constant for a given temperature and equal to the emittance of the
blackbody:
E=A = E0 = f T
ð Þ:
(7.82)
Because E=E0 = ε, the essence of Kirchhoff’s law reduces to the statement that, in
thermodynamic equilibrium, absorbance and the thermal emissivity of the surface
are numerically equal: i.e.,
A = ε:
(7.83)
For majority of the surfaces encountered in engineering processes, the temperature
dependence of ε(T) is weak in general. Detailed characterization of the radiating
surface is a spectral thermal emissivity:
ελ = Jλ T
ð Þ
J0λ T
ð Þ or εν = Jν T
ð Þ
J0ν T
ð Þ
(7.84)
which is a ratio of the spectral radiation flux of the material to that of the
blackbody.
The emissivity of some materials of nuclear engineering is shown in the following:
UO2
ελ=1−0.16 exp[−3.79□10−4(T−3120)−3.27□10−7(T−3120)2] for
λ=0.65 μm; T in K
PuO2
ε=0.548+1.65□10−4 T, where ε is the hemispherical emissivity; T in K
Alloy E-110
ε=0.167–0.184 for T=80–200°C
Alloy E-110
ε=0.167–0.184 for T=80–200°C
Alloy E-635
ελ=1.02+3□10−4 T for λ=0.65 μm; T in K
ZrO2
ελ=0.48–0.50
Corium (core melt) ε=0.85 for Tm.p.=2850 K, where ε is the integrated emissivity
(Harding et al., 1989).
Lambert’s cosine law determines the distribution of radiant intensity of a
blackbody in directions. The radiation flux per unit area in a certain direction (Eψ)
is proportional to the radiation flux in a direction normal to the surface (En) and
the cosine of the angle (ψ) between two directions:
Eψ = En cos ψ:
(7.85)
When the radiation obeys Lambert’s law, the brightness does not depend on the direction
. Fig. 7.34 shows a qualitative distribution of the relative emittance of different
bodies in all directions.

<!-- page 406 (PDF 50) -->
A body, that obeys Lambert’s law, is called the diffuse emitter, while the radiation
of actual solid materials obeys Lambert’s law only partially. Metals exhibit a maximum
emission intensity at ψ =40–80 degrees, i.e., observed from the surface at a considerable
angle. Dielectrics give the greatest intensity of radiation in the normal
direction in the range ψ =0–60 degrees and low value in the range of high angles ψ.
In radiation characteristics of actual bodies, a conventional temperature is introduced
along with the degree of blackness (thermal emissivity) as shown in the
following.
Radiation temperature (Trad) is a conventional temperature of a blackbody for the
same radiation flux as that from the body under consideration: E0 Trad
ð
Þ = E T
ð Þ. From
the Stefan-Boltzmann law σ0T4
rad = εσ0T4. Therefore
Trad = T
ffiffiε
4p :
(7.86)
Color temperature (Tc) is a conventional blackbody temperature at which the ratio of
the spectral intensities at two wavelengths (colors) is the same as that of the considered
body J0λ1
J0λ2
= Jλ1
Jλ2
. Using the Wien’s law, we obtain:
Tc
= 1
T − ln ελ1=ελ2
ð
Þ
C2
λ1
− 1
λ2
□
(:
(7.87)
Bright temperature (Tb) is determined by equating the brightness of blackbody and the
body under consideration I0λ Tb
ð
Þ = Iλ T
ð Þ, i.e.,
Tb
= 1
T −λ ln ελ
C2
:
(7.88)
Relations linking Trad, Tc, and Tb with T are the basis of the methods to measure high
temperatures by optical methods (pyrometers—radiant color luminance).
e= 1
n
Fig. 7.34 The distribution of the relative emittance of different bodies depending on the
direction: 1—blackbody; 2—gray body; 3—oxidized metals, dielectrics, wood, paper;
4—polished metals.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 407 (PDF 51) -->
### 7.3.3 Radiation characteristics

In describing the radiative properties of actual bodies, the use is made of relative
dimensionless quantities and properties in linking real and ideal bodies.
Relative emissivity ε (thermal emissivity) is a ratio of the real radiation surface
energy of to that of an ideal blackbody at a same temperature and other conditions
being equal.
Absorptivity A is a ratio of the energy absorbed by the surface to the energy
absorbed by the blackbody irradiated by a same incident radiation flux, and other conditions
being equal.
Reflectivity R is a ratio of the energy reflected by the surface to the energy reflected
by ideally reflecting (mirror) surface irradiated by the same incident radiation flux and
other conditions being equal.
Transmissivity D (transparency) of the material is a ratio of the energy transmitted
through the material to the incident radiation energy.
In practice, it is more convenient to work with the averaged radiation properties
over all directions. Thus, considering the energy emitted by the element of the body
surface into all directions over that element suggests a hemispherical emittance or the
degree of blackness. Depending on whether it is over an entire range or a narrow range
of wavelengths, we have the total (integral) or monochromatic (spectral) hemispherical
emissivity. Similarly, corresponding radiation properties are defined for reflectivity
and absorptivity of the surface.
Radiation characteristics of real bodies depend on the wavelength of the radiation,
surface temperature, and the direction of the emitted or the incident radiation. The
surface, which has the same emissivity and absorbance at all wavelengths refers to
gray bodies: ελ = const and Aλ = const. The gray body is an idealized concept just
because at the real bodies, these radiation properties are dependent on the wavelength.
Integral emissivity of metals is
ε = 0:576
ffiffiffiffiffiffiffi
ρeT
p
−0:124ρeT:
(7.89)
Here ρе is the electrical resistivity (Ωcm); T in K.
Spectral emission of pure metals in a short wavelength region of the spectrum
(λ<0.5 μm) is more than half of the blackbody radiation at the same temperature.
When λ>1 μm, the spectral emissivity of most metals	0.05–0.1. For example, to
improve the thermal insulation properties, the walls of cylinders, flasks, and Dewar
vessels are coated by silver (ε = 0:02−0:03) or aluminum (ε = 0:04−0:06).
Water and ice have a higher emissivity for the longwave thermal radiation. Monoand
di-atomic gases (He, H2, N2, etc.) are practically transparent to the thermal radiation
, i.e., neither absorb nor emit radiation. Tri-atomic gases (H2O, CO2, SO2, NO2,
etc.) have high emissivity and absorptivity. They absorb and emit at specific intervals
(bands) of wavelengths and transparent at the remaining of the spectrum.
Emission from gas deviates from the fourth power law. For example:
ECO2 = 3:5□10−7 pl
ð Þ0:33T3:5; EH2O = 3:5□10−6p0:8l0:6T3 where p is the partial pressure
and l is the path length along the propagation. However, in engineering

<!-- page 408 (PDF 52) -->
applications, we use the fourth power law, for the sake of convenience, and the
deviation is taken care of by the relative emissivity of gas:
E = ε T, pl
ð
Þσ0T4:
(7.90)
ε(T,pl) are given in the form of graphs for each gas. Issues related to the radiation heat
transfer in high temperature gases are discussed in detail in Golovnyov et al. (1984).
Reflectivity of the body (R = 1−ε) depends on directions of the incident and
reflected radiation (Kitzel’, 1973). Extreme cases of reflections from surfaces are diffuse
and specular reflection. A diffuse surface reflects the incident beam so that the
intensity of reflected radiation is the same for all the reflection angles (Fig. 7.35).
A specular surface reflects the beam at the same angle just in the same way as a mirror
does. The surface is a mirror when its roughness is much smaller than the wavelength
of the incident beam. Thus, the same surface can become diffuse or mirror, depending
on the incident radiation wavelength.
Fig. 7.36 shows the dependence of the reflection coefficient of the paint at different
angles of incident and reflected radiation.
(A)
(B)
(C)
q
q
Fig. 7.35 Types of reflective surfaces: (A) diffuse; (B) actual; (C) specular. 1—Reflectance for
short wavelength; 2—reflectance for long wavelength; 3—integrated reflectance (over all
wavelength).
Fig. 7.36 Dependence of the brightness coefficient of the coatings on the angles between
incident and reflection beams: a—white shiny surface; b—black matte finish.
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 409 (PDF 53) -->
White (color) materials can have a high reflection coefficient for short-wave
radiation and are “black” for the longwave. Due to the selectivity of reflectance
bodies, the latter depends essentially on the temperature of the incident radiation
source.
Transparency (transmissivity) of the bodies for thermal radiation may be visible
even for relatively thick layers. It is so-called greenhouse effect due to the high transparency
glass for shortwave solar radiation and extremely low opacity to the longwave
infrared radiation. Bodies that are completely opaque in the visible spectrum at normal
temperatures can be transparent to the thermal radiation at high temperatures (e.g.,
porcelain, BeO, etc.).

### 7.3.4 Radiation heat transfer between bodies

First let’s consider the heat exchanges between two parallel plates of infinite length (1)
and (2), which are separated by infinite transparent medium. Calculation of radiation
heat transfer is carried out according to the formula:
q1,2 = σ0εred T4
1 −T4
□
□
:
(7.91)
where εred =
ε1
+ 1
ε2
−1
□
(−1
is the reduced emissivity of the system; ε1. ε2 are the
surface emissivity; T1 and T2 are the surface temperatures (K).
The total amount of heat transferred from surface 1 to surface 2 is:
Q = q1,2A = σ0εred T4
1 −T4
□
□
A:
(7.92)
Here, A is the surface area (m2).

#### 7.3.4.1 Arbitrary arrangement of two surfaces

The geometry of the system is taken into account by means of integral angular
radiation coefficients (irradiance coefficients). The angular coefficient determines
the amount of diffusely distributed radiation energy, which is transferred from one
surface to another. The physical meaning of the angular coefficient can be understood
by the following example. The radiation flux leaving the surface 1, is evenly distributed
over the surface of hemisphere. In this space over the surface 1, the other surface
2 is located with a certain area which makes a solid angle φ12. Then, this angle
determines the portion of the radiant energy that falls from the surface 1 to surface
2: φ12 = Q1⃗2
Q1
and φ21 = Q2⃗1
Q2
. The first subscript refers to the emitting surface
and the second to the irradiated surface. The angular coefficients φ possess the
reciprocity with the exposed area A:
φ12 · A1 = φ21 · A2:
(7.93)

<!-- page 410 (PDF 54) -->
The angular coefficient is dimensionless (φ<1), reflecting the purely geometrical
features of the placement of the two bodies in space. There are graphic-analytical
and experimental methods for determining the angular coefficients.
When the surface area receiving the heat is small, corresponding angular coefficient
is also small. In a closed system, all the radiation energy originating from
any surfaces is distributed over the rest of the surfaces of the system so that
Xn
j=1φij = 1, where n is the number of surfaces, forming a closed system.
The heat flow between two gray bodies with temperatures T1 and T2 in accordance
with the Stefan-Boltzmann law Q12 = σ0 T4
1A1φ12 −T4
2A2φ21
or using the property of
reciprocity,
Q12 = σ0 T4
1 −T4
□
□
A1φ12 = σ0 T4
1 −T4
□
□
A2φ21:
(7.94)
Full radiant flux for a system consisting of a gray body is given by:
Q12 = σ0εred T4
1 −T4
□
□
A1φ12:
(7.95)
where εred =
1 + φ12
ε1
−1
□
(
+ φ21
ε2
−1
□
( is called as a reduced degree of
blackness of a pair of bodies and is an optical and geometrical parameter.
The value of A1□φ12=H12 is called the mutual radiation surface of bodies. Q12
are in (W).

#### 7.3.4.2 Heat transfer between body and shell

Assume one body is in a cavity of another body and their sizes are given. With
the surface areas (A1, A2) and temperature (T1, T2) being given and noting the
absorption coefficients can be set equal to the emissivity (ε1 and ε2), then the calculation
of an amount of heat transmitted from one surface (1) to the other surface (2)
will be:
Q12 = σ0 T4
1 −T4
□
□
A1
ε1
+
ε2
−1
□
(A1
A2
:
(7.96)
If the surface area of the body in the cavity is much less than the surface of the shell
(A1≪A2) or ε2 = 1, Eq. (7.96) takes the form:
Q12 = σ0ε1 T4
1 −T4
□
□
A1:
(7.97)
If A1 ffiA2 we will arrive at the parallel plate formula, Eq. (7.92).
Many other specific problems and solutions are found in Siegel and
Howell (1981).
Thermal Hydraulics in Water-Cooled Nuclear Reactors

<!-- page 411 (PDF 55) -->
### 7.3.5 Heat transfer in absorbing and emitting environments

Electromagnetic wave, as it passes through a medium, interacts with the particles of the
medium and undergoes scattering and absorption processes. Interactions of the wave
occur with the molecules or atoms with different structure, solid particles or liquid droplets
in gases. The medium may have its own emission sources; In addition, the radiation
also causes some brightness of scattering medium. The radiation energy being absorbed
is turned into heat, changes the thermal state of the medium and will be re-emitted.
The overall change in spectral density of the radiation flux over a spatial length dx
due to the incident radiation Jλ and its own intrinsic Iλs is expressed by the equation:
dJλ = −βλJλdx + ελI0λsdx:
(7.98)
where βλ = βA
λ + βS
λ is the spectral attenuation coefficient of radiation due to absorption
(βλ
A) and due to scattering (βλ
S); ελ is the spectral emissivity of thermal radiation of the
medium.
If its own intrinsic radiation of the medium is much less than the attenuation of the
incident radiation, i.e., ελIλs≪βλJλ, the transport equation becomes: dJλ
Jλ
= −βλJλdx.
From this we have JS
λ
JA
λ
= exp
−
ðs
βλdx
□
(
; JA
λ −JS
λ
Ja
λ
= 1− exp
−
ðs
βλdx
□
(
= Aλs,
where Aλs signifies the absorption (and scattering) ability of the layer of thickness
s for the beam of wavelength λ. The ratio generally depends on the physical properties
of the medium (absorption and scattering, the concentration of the absorbing
substance, wavelength, temperature, thickness, etc.).
Effect of concentration of absorbing material in the medium on the optical properties
is established in the first approximation by the Bouguer-Beer law, in which the
relative attenuation of the beam of rays is proportional to the volume concentration of
the absorbing substance μ.
Absorption ability or absorptivity of such a medium can be determined by the
formula:
Aλ = 1− exp −βλμs
ð
Þ:
(7.99)
This law holds only approximately for monochromatic radiation of low concentrations
. Deviations from the law are caused by the interactions among the particles
or molecules of absorbing materials. For nonmonochromatic radiation and for high
concentrations of absorbing substances, the absorption coefficient depends on the
concentration and length of the beam path.
The value given by
Lλ =
ðs
βλdx
(7.100)
is called as the optical thickness of the medium. If the absorption coefficient
does not vary in distance, then Lλ = βλs =
s
1=βλ
. Here s is the characteristic
