# 1 Neutron–Nuclear Reactions — 1.4 Summary of Cross Section Data … Problems
<!-- source PDF pages 48-56 -->

<!-- page 23 (PDF 48) -->
regular structure, as graphite does, the neutron will be diffracted and the energy
dependence of the cross section will reflect the neutron energies corresponding to
multiples of interatomic spacing. For sufficiently small energies, diffraction
becomes impossible and the cross section is once again insensitive to neutron
energy.

## 1.4 Summary of Cross Section Data

### Low-Energy Cross Sections

The low-energy total cross sections for several nuclides of interest in nuclear
reactors are plotted in Fig. 1.28. Gadolinium is sometimes used as a “burnable
Fig. 1.28 Low-energy absorption (fission + capture) cross sections for several important
nuclides. (With permission from Ref. [3]. Copyright 1976, Wiley.)

<!-- page 24 (PDF 49) -->
poison,” and xenon and samarium are fission products with large thermal cross
sections.

### Spectrum-Averaged Cross Sections

Table 1.3 summarizes the cross section data for a number of important nuclides in
nuclear reactors. The first three columns give fission, radiative capture, and elastic
scattering cross sections averaged over a Maxwellian distribution with T = 0.0253
eV, corresponding to a representative thermal energy spectrum. The next two
columns give the infinite dilution fission and radiative capture resonance integrals
, which are averages of the respective resonance cross sections over a 1/E
spectrum typical of the resonance energy region in the limit of an infinitely dilute
concentration of the resonance absorber. The final five columns give cross
sections averaged over the fission spectrum.
Table 1.3 Spectrum-Averaged Thermal, Resonance, and Fast Neutron Cross Sections (barns)
Nuclide
Thermal Cross Section
Resonance Cross
Section
Fission Spectrum Cross Section
σf
σγ
σel
σf
σγ
σf
σy
σel
σin
σn,2n
233U92
11.9
1.9
0.07
4.4
1.2
4 × 10−3
235U92
15.0
1.2
0.09
4.6
1.8
12 × 10−3
239Pu94
7.8
1.8
0.05
4.4
1.5
4 × 10−3
241Pu94
11.1
1.6
0.12
5.2
0.9
21 × 10−3
232Th90
–
6.5
13.7
–
0.08
0.09
4.6
2.9
14 × 10−3
238U92
–
2.4
9.4
0.31
0.07
4.8
2.6
12 × 10−3
240Pu94
0.05
1.5
8.9
1.4
0.09
4.3
2.0
4 × 10−3
242PU94
–
16.8
8.3
5.6
1.1
0.09
4.8
1.9
7 × 10−3
1H1
–
0.29
20.5
–
0.15
–
4 × 10−5
3.9
–
–
2H1
–
5 × 10−4
3.4
–
3 × 10−4
–
7 × 10−6
2.5
–
–
10B5
–
2.1
–
0.22
–
8 × 10−5
2.1
0.07
–
12C6
–
0.003
4.7
–
0.002
–
2 × 10−5
2.3
0.01
–
16O8
–
2 × 10−4
3.8
–
6 × 10−4
–
9 × 10−5
2.7
–
–
23Na11
–
0.47
3.0
–
0.31
–
2 × 10−4
2.7
0.5
–
56Fe26
–
2.5
12.5
–
1.4
–
3 × 10−3
3.0
0.7
–
91Zr40
–
1.1
10.6
–
6.9
–
0.01
5.0
0.7
–
135Xe54
–
2.7 × 106
3.8 × 105
–
7.6 × 103
–
0.01
4.9
1.0
–
149Sm62
–
6.0 × 104
–
3.5 × 103
–
0.22
4.6
2.2
–
157Gd64
–
1.9 × 103
–
–
0.11
4.7
2.2
11 × 10−3
Source: Data from www.nndc.bnl.gov/.

<!-- page 25 (PDF 50) -->
### Example 1.1 Calculation of Macroscopic Cross Section

The macroscopic
cross section Σ = Nσ, where N is the number density. The number density is related
to the density ρ and atomic number A by N = (ρ/A) N0, where N0 = 6.022 × 1023 is
Avogadro’s number, the number of atoms in a mole. For a mixture of isotopes
with volume fractions υi, the macroscopic cross section is Σ = Σiυi(ρ/A)iN0σi;
for example, for a 50:50 vol% mixture of carbon and 238U, the macroscopic thermal
absorption cross section is Σa = 0.5(ρC/AC)N0σaC + 0.5(ρU/AU)N0σaU = 0.5(1.60 g/
cm3 per 12 g/mol)(6.022 × 1023 atom/mol)(0.003 × 10−24 cm2) + 0.5(18.9 g/cm3
per 238 g/mol)(6.022 × 1023 atom/mol)(2.4 × 10−24 cm2) = 0.0575 cm−1.

## 1.5 Evaluated Nuclear Data Files

Published experimental and theoretical results on neutron–nuclear reactions are
collected by several collaborating nuclear data agencies worldwide. Perhaps the
most comprehensive computerized compilation of experimental data is the
EXFOR computer library (Ref. [4]). The computerized card index file CINDA
(Ref. [5]), which contains comprehensive information on measurements, calculations
, and evaluations of neutron–nuclear data, is updated annually. The
plethora of sometimes contradictory nuclear data must be evaluated before it
can be used confidently in reactor physics calculations. Such evaluation consists
of intercomparison of data, use of data to calculate benchmark experiments,
critical assessment of statistical and systematic errors, checks for internal
consistency and consistency with standard neutron cross sections, and the
derivation of consistent preferred values by appropriate averaging procedures.
Several large evaluated nuclear data files are maintained: (1) United States
Evaluated Nuclear Data File (ENDF/B), (2) Evaluated Nuclear Data Library of
the Lawrence Livermore National Laboratory (ENDL), (3) United Kingdom
Nuclear Data Library (UKNDL), (4) Japanese Evaluated Nuclear Data Library
(JENDL), (5) Karlsruhe Nuclear Data File (KEDAK), (6) Russian (formerly Soviet)
Evaluated Nuclear Data File (BROND), and (7) Joint Evaluated File of NEA
Countries (JEF). Processing codes are used to convert these data to a form that can
be used in reactor physics calculations, as discussed in subsequent chapters.

## 1.6 Elastic Scattering Kinematics

Consider a neutron with energy EL = 1
2 mv 2
L in the laboratory (L) system incident
upon a stationary nucleus of mass M. Since only the relative masses are important
in the kinematics, we set m = 1 and M = A. It is convenient to convert to the CM
system, as indicated in Fig. 1.29, because the elastic scattering event is usually
isotropic in the CM system.
The velocity of the CM system in the L system is
vCM =
1 + A vL + AVL
) =
vL
1 + A
(1.13)

<!-- page 26 (PDF 51) -->
and the velocities of the neutron and the nucleus in the CM system are
vc = vL − vCM =
A
A + 1 vL
vc = −vCM =
−1
A + 1 vL
(1.14)
The energy of the neutron in the CM system, Ec, is related to the energy of the
neutron in the laboratory, EL, by
Ec = 1
2 v2
c + 1
2 AV 2
c =
A
A + 1
2 v2
L =
A
A + 1 EL
(1.15)

### Correlation of Scattering Angle and Energy Loss

From consideration of conservation of momentum and kinetic energy, it can be
shown that the speeds of the neutron and the nucleus in the center-of-mass
system do not change during the scattering event:
v´
c = vc =
A
A + 1 vL
(1.16)
V ´
c = V c =
−1
A + 1 vL
Neutron
vL
vC
VC
θL
θC
v'L
v'C
V'L
V'C
vCM
m
M
COM
LAB – Before
LAB – After
CM – Before
CM – After
Scattering
angle – LAB
system
Scattering
angle – CM
system
Target
nucleus
Fig. 1.29 Scattering event in laboratory and CM systems. (With permission from Ref. [3].
Copyright 1976, Wiley.)

<!-- page 27 (PDF 52) -->
With reference to Fig. 1.30, the scattering angles in the laboratory and CM
systems are related by
tan θL =
v´c sin θc
vCM + v´c cos θc
=
sin θc
(1=A) + cos θc
(1.17)
The law of cosines yields
cos π − θc
) = (v´c)2 + (vCM)2 − (v´L)2
2vCMv´c
(1.18)
which may be combined with Eqs. (1.13) and (1.16) to obtain a relationship
between the incident and final energies of the neutron in the laboratory system
and the scattering angle in the CM system:
2 m v´
L
)2
2 m vL
)2 ≡ E´L
EL
= A2 + 1 + 2A cos θc
(A + 1)2
= 1 + α
) + 1 − α
) cos θc
(1.19)
where α ≡ A − 1
)2= A + 1
)2.

### Average Energy Loss

Equation (1.19) states that the ratio of final to incident energies in an elastic
scattering event is correlated to the scattering angle in the CM system, which, in
turn, is correlated via Eq. (1.17) to the scattering angle in the laboratory system.
The maximum energy loss (minimum value of E´L=EL) occurs for θc = π (i.e.,
backward scattering in the CM system), in which case E´L = αEL. For hydrogen
(A = 1), α = 0 and all of the neutron energy can be lost in a single collision. For
other nuclides, only a fraction (1 − α) of the neutron energy can be lost in a single
collision, and for heavy nuclides (α →1) this fraction becomes very small.
The probability that a neutron scatters from energy EL to within a differential
band of energies dE´L about energy E´L is equivalent to the probability that a
neutron scatters into a cone 2π sin θcdθc about θc:
σs EL
)P EL ! E´
L
)dE´
L = −σCM EL; θc
)2π sin θcdθc
(1.20)
where the negative sign takes into account that an increase in angle corresponds
to a decrease in energy, σs is the elastic scattering cross section, and σCM(θc) is the
V'L
VCM
θC
θL
|VC| = |V'C|
Fig. 1.30 Relation between laboratory and CM scattering angles. (With permission from
Ref. [3]. Copyright 1976, Wiley.)

<!-- page 28 (PDF 53) -->
cross section for scattering through angle θc. Using Eq. (1.19) to evaluate
dE´L=dθc, this becomes
P EL ! E´
L
) =
4πσCM EL; θc
)
1 − α
)ELσs EL
) ;
αEL ≤ E´
L ≤ EL
0;
otherwise
<
:
(1.21)
Except for very high energy neutrons scattering from heavy mass nuclides, elastic
scattering in the CM is isotropic, σCM(θc) = σs/4π. In this case, Eq. (1.21) may be
written as
σs EL ! E´L
) ≡ σs EL
)P EL ! E´L
) =
σs EL
)
1 − α
)EL
;
αEL ≤ E´
L ≤ EL
= 0;
otherwise
(1.22)
The average energy loss in an elastic scattering event may be calculated from
ΔEL
h
i ≡ EL − ∫
EL
αEL
dE´
LE´
LP EL ! E´
L
) = 1
2 1 − α
)EL
(1.23)
and the average logarithmic energy loss may be calculated from
ξ ≡ ∫
EL
αEL
dE´L ln
EL
E´L

P EL ! E´L
)
= 1 +
α
1 − α ln α = 1 − A − 1
)2
2A
ln A + 1
A − 1

(1.24)
The number of collisions, on average, required for a neutron of energy E0 to be
moderated to thermal energies, say 1 eV, can be estimated from
no: collisions
h
i ' ln E0 eV
)=1:0

ξ
(1.25)
The results are shown in Table 1.4 for E0 = 2 MeV.
Table 1.4 Number of Collisions, on Average, to Moderate a Neutron from 2 MeV to 1 eV
Moderator
ξ
Number of Collisions
ξΣs/Σa
H
1.0
–
D
0.725
–
H2O
0.920
D2O
0.509
He
0.425
Be
0.209
C
0.158
Na
0.084
Fe
0.035
238U
0.008
0.0092

<!-- page 29 (PDF 54) -->
The parameter ξ, which is a measure of the moderating ability, decreases with
nuclide mass, with the result that the number of collisions that are needed to
moderate a fast neutron increases with nuclide mass. However, the effectiveness
of a nuclide (or molecule) in moderating a neutron also depends on the relative
probability that a collision will result in a scattering reaction, not a capture
reaction, which would remove the neutron. Thus, the parameter ξΣs/Σa, referred
to as the moderating ratio, is a measure of the effectiveness of a moderating
material. Even though H2O is the better moderator in terms of the number of
collisions required to thermalize a fast neutron, D2O is the more effective moderator
because the absorption cross section for D is much less than that for H.
Note that the symbol ξ conventionally used to define the average logarithmic
energy loss in Eq. (1.24) is the same symbol conventionally used in Eq. (1.7) in
defining a parameter for the resonance cross section. We stick with this
conventional usage and hope that it will be clear from the context which
definition is meant – Eq. (1.24) for neutron “scattering” and neutron flux
calculations and Eq. (1.7) for “resonance” cross section calculations.

### Example 1.2 Moderation by a Mixture

The moderating parameters for a
mixture of isotopes is constructed by weighting the moderating parameters of
the individual isotopes by their concentrations in the mixture. For example, in a
mixture of 12C and 238U the average value of ξΣs = NCξCσsC + NUξUσsU =
NC(0.158) (2.3 × 10−24 cm2) + NU (0.008)(4.8 × 10−24 cm2), where the fission
spectrum range elastic scattering cross sections of Table 1.3 have been
assumed to hold also in the slowing-down range. The total absorption cross
section is Σa = NCσaC + NUσaU = NC(0.002 × 10−24 cm2) + NU(280 × 10−24 cm2)
in the slowing-down range, where the resonance range cross sections from
Table 1.3 have been used.

## References

1 H. CEMBER, Introduction to Health Physics, 3rd ed., McGraw-Hill, New York
(1996).
2 L. J. TEMPLIN, ed., Reactor Physics Constants, 2nd ed., ANL-5800, Argonne
National Laboratory, Argonne, IL (1963).
3 J. J. DUDERSTADT and L. G. HAMILTON, Nuclear Reactor Analysis, Wiley, New York
(1976), Chap. 2.
4 A. CALAMAND and H. D. LEMMEL, Short Guide to EXFOR, IAEA-NDS-1, Rev. 3,
International Atomic Energy Agency, Vienna (1981).
5 CINDA: An Index to the Literature on Microscopic Neutron Data, International
Atomic Energy Agency, Vienna; CINDA-A, 1935–1976 (1979); CINDA-B,
1977–1981 (1984); CINDA-89 (1989).

## Further Readings

CULLEN D. E., “Nuclear Cross Section Preparation,” in Y. Ronen, ed., CRC Handbook
of Nuclear Reactor Calculations I, CRC Press, Boca Raton, FL (1986).

<!-- page 30 (PDF 55) -->
HONECK H. C., ENDF/B: Specifications for an Evaluated Data File for Reactor
Applications, USAEC report BNL-50066, Brookhaven National Laboratory,
Upton, NY (1966).
KAPLAN I., Nuclear Physics, 2nd ed., Addison-Wesley, Reading, MA (1963).
KIKUCHI Y.,“JENDL-3 Revision 2: JENDL 3-2,” Proc. Int. Conf. Nuclear Data for
Science and Technology, Gatlinburg, TN, Vol. 2 (1994), p. 685.
KNIEF R. A., Nuclear Engineering, Taylor & Francis, Washington, DC (1992).
NORDBORG C. and SALVATORES M.,“Status of the JEF Evaluated Nuclear Data Library,”
Proc. Int. Conf. Nuclear Data for Science and Technology, Gatlinburg, TN, Vol. 2
(1994), p. 680.
ROUSSIN R. W., YOUNG P.G., and MCKNIGHT R.,“Current Status of ENDF/B-VI,” Proc.
Int. Conf. Nuclear Data for Science and Technology, Gatlinburg, TN, Vol. 2
(1994), p. 692.
ROWLANDS J. L. and TUBBS N.,“The Joint Evaluated File: A New Nuclear Data Library
for Reactor Calculations,” Proc. Int. Conf. Nuclear Data for Basic and Applied
Science, Santa Fe, NM, Vol. 2 (1985), p. 1493.
SCHMIDT J. J., “Nuclear Data: Their Importance and Application in Fission Reactor
Physics Calculations,” in D. E. Cullen, R. Muranaka, and J. Schmidt, eds., Reactor
Physics Calculations for Applications in Nuclear Technology, World Scientific,
Singapore (1990).

## Problems

### 1.1

Demonstrate that the speeds of the neutron and nucleus in the CM system
do not change in an elastic scattering event by using conservation of
momentum and kinetic energy.

### 1.2

Estimate the probability that a 1-MeV neutron will be moderated to
thermal without being captured in a mixture of uranium and water with
NH/NU = 1:1. Repeat for a 1:1 mixture of uranium and carbon.

### 1.3

Neutrons are slowed down to thermal energies in a 1:1 mixture of H2O and
4% enriched uranium (4%235U, 96%238U). Estimate the thermal value of
η = νσf/(σc + σf). Repeat the calculation for a mixture of (2%235U, 2%239Pu,
96%238U).

### 1.4

Estimate the probability that a fission neutron will have a scattering
collision with H2O in the mixtures of Problem 1.3.

### 1.5

Calculate the average energy loss for neutrons at 1-MeV, 100-keV, 10-keV,
and 1-keV scattering from carbon. Repeat the calculation for scattering
from iron and from uranium.

### 1.6

Repeat Problem 1.5 for scattering from hydrogen and sodium.

<!-- page 31 (PDF 56) -->
### 1.7

Calculate the moderating ratio and the average number of collisions
required to moderate a fission neutron to thermal for a 1:1 mixture of
12C–238U. Repeat for a 10:1 mixture.

### 1.8

Calculate the thermal absorption cross section for a 1:1 wt% mixture of
carbon and 4% enriched uranium (e.g., 4% 235U, 96% 238U).

### 1.9

Derive Eq. (1.21) from Eqs. (1.20) and (1.19).

### 1.10

Calculate the average number of scattering events required to moderate a
neutron’s energy from above the resonance range to below the resonance
range of 238U for carbon, H2O and D2O moderators.
