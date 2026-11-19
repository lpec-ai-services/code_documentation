# 6 Fuel Burnup — 6.1 Changes in Fuel Composition … 6.2 Samarium and Xenon
<!-- source PDF pages 221-240 -->

<!-- page 197 (PDF 221) -->
# 6 Fuel Burnup

The long-term changes in the properties of a nuclear reactor over its lifetime are
determined by the changes in composition due to fuel burnup and the manner in
which these are compensated. The economics of nuclear power is strongly
affected by the efficiency of fuel utilization to produce power, which in turn is
affected by these long-term changes associated with fuel burnup. In this chapter
we describe the changes in fuel composition that take place in an operating
reactor and their effects on the reactor, the effects of the samarium and xenon
fission products with large thermal neutron cross sections, the conversion of
fertile material to fissionable material by neutron transmutation, the effects of
using plutonium from spent fuel and from weapons surplus as fuel, the production
of radioactive waste, the extraction of the residual energy from spent fuel, and
the destruction of long-lived actinides.

## 6.1 Changes in Fuel Composition

The initial composition of a fuel element will depend on the source of the fuel. For
reactors operating on the uranium cycle, fuel developed directly from natural
uranium will contain a mixture of 234U, 235U, and 238U, with the fissile 235U
content varying from 0.72% (for natural uranium) to more than 90%, depending
on the enrichment. Recycled fuel from reprocessing plants will also contain the
various isotopes produced in the transmutation–decay process of uranium.
Reactors operating on the thorium cycle will contain 232Th and 233U or 235U,
and if the fuel is from a reprocessing plant, isotopes are produced in the
transmutation–decay process of thorium.
During the operation of a nuclear reactor a number of changes occur in the
composition of the fuel. The various fuel nuclei are transmuted by neutron
capture and subsequent decay. For a uranium-fueled reactor, this process
produces a variety of transuranic elements in the actinide series of the periodic
table. For a thorium-fueled reactor, a number of uranium isotopes are produced.
The fission event destroys a fissile nucleus, of course, and in the process produces
two intermediate mass fission products. The fission products tend to be neutron
rich and subsequently decay by beta or neutron emission (usually accompanied by
gamma emission) and undergo neutron capture to be transmuted into a heavier
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 198 (PDF 222) -->
isotope, which itself undergoes radioactive decay and neutron transmutation, and
so on. The fissile nuclei also undergo neutron transmutation via radiative capture
followed by decay or further transmutation.

### Fuel Transmutation–Decay Chains

Uranium-235, present 0.72% in natural uranium, is the only naturally occurring
isotope that is fissionable by thermal neutrons. However, three other fissile
(fissionable by thermal neutrons) isotopes of major interest as nuclear reactor
fuel are produced as the result of transmutation–decay chains. Isotopes that can be
converted to fissile isotopes by neutron transmutation and decay are known as
fertile isotopes. 239Pu and 241Pu are products of the transmutation–decay chain
beginning with the fertile isotope 238U, and 233U is a product of the transmutation–
decay chain beginning with the fertile isotope 232Th. These two transmutation–
decay chains are shown in Fig. 6.1. Isotopes are in rows with horizontal arrows
232Th
233Th
234Th
7.4
233Pa
234Pa
4.1
232U
233U
234U
235U
236U
5.1
237U
24.1 d
22.3 min
237No 170
6.75 d
1.17 min
6.69 h
27 d
238U
239U
240U
238No
239No
240No
238Pu
239Pu
240Pu
2.7
241Pu
242Pu
243Pu
14.1 h
23.5 min
243Am 78
4.96 h
241Am 600
14.4 y
7.2 min
62 min
2.35 d
2.12 d
XX
XX
(n, 2n)·REACTION (E ≥ 6 MeV)
(n, γ)·REACTION
β-DECAY
FISSION
THERMAL CROSS SECTION (BARNS)
HALF-LIFE
CROSS SECTIONS AND HALF-LIVES
FROM CHART OF THE NUCLIDES (1989)
α-DECAY HALF-LIVES ARE ALL ≥ 10 Y
YY
K
E
Y
XX
YY
Fig. 6.1 Transmutation–decay chains for 238U and 232Th. (With permission from Ref. [1].
Copyright 1992, Taylor & Francis.)

<!-- page 199 (PDF 223) -->
representing (n, γ) transmutation reactions, with the value of the cross section (in
barns) shown. Downward arrows indicate β-decay, with the half-lives shown.
Thermal neutron fission is represented by a dashed diagonal arrow, and the thermal
cross section is shown. (Fast fission also occurs but is relatively less important in
thermal reactors.) Natural abundances, decay half-lives, modes of decay, decay
energies, spontaneous fission yields, thermal capture and fission cross sections
averagedover a Maxwelliandistributionwith kT = 0.0253 eV(σth), infinite-dilution
capture and fission resonance integrals (RIs), and capture and fission cross sections
averaged over the fission spectrum (σχ) are given in Table 6.1.

### Fuel Depletion–Transmutation–Decay Equations

Concentrations of the various fuel isotopes in a reactor are described by a coupled
set of production–destruction equations. We adopt the two-digit superscript
convention for identifying isotopes in which the first digit is the last digit in the
atomic number and the second digit is the last digit in the atomic mass. We
represent the neutron reaction rate by σnm
x φnnm, although the actual calculation
may involve a sum over energy groups of such terms.
For reactors operating on the uranium cycle, the isotopic concentrations are
described by
@n24
@t
= −σ24
a ϕn24
@n25
@t
= σ24
γ ϕn24 − σ25
a ϕn25
@n26
@t
= σ25
γ ϕn25 − σ26
a ϕn26 + λ36
ec n36
@n27
@t
= σ26
γ ϕn26 + σ28
n;2nϕn28 − λ27n27
@n28
@t
= −σ28
a ϕn28
@n29
@t
= σ28
γ ϕn28 − (λ29 + σ29
a ϕ)n29
@n36
@t
= σ37
n;2nϕn37 − (λ36 + σ36
a ϕ)n36
@n37
@t
= λ27n27 − σ37
a ϕn37
@n38
@t
= σ37
γ ϕn37 − (λ38 + σ38
a ϕ)n38
@n39
@t
= λ29n29 − (λ39 + σ39
a ϕ)n39
@n48
@t
= λ38n38 − σ48
a ϕn48
@n49
@t
= λ39n39 − σ49
a ϕn49 + σ48
γ ϕn48
@n40
@t
= σ49
γ ϕn49 − σ40
a ϕn40 + σ29
γ ϕn29 + σ39
γ ϕn39

<!-- page 200 (PDF 224) -->
@n41
@t
= σ40
γ ϕn40 − (λ41 + σ41
a ϕ)n41
@n42
@t
= σ41
γ ϕn41 − σ42
a ϕn42
@n43
@t
= σ42
γ ϕn42 − (λ43 + σ43
a ϕ)n43
@n51
@t
= λ41n41 − (λ51 + σ51
a ϕ)n51
@n52
@t
= σ51
γ ϕn51 − σ52
a ϕn52
@n53
@t
= λ43n43 − σ53
a ϕn53 + σ52
γ ϕn52
(6.1)
With respect to Fig. 6.1, a few approximations have been made in writing Eqs. (6.1).
Theneutron capture in 239U to produce 240U followed by thedecay (t1/2= 14 h) into
240Np and the subsequent decay (t1/2 = 7 min) into 240Pu is treated as the direct
production of 240Pu by neutron capture in 239U, and the production of 240Np by
neutron capture in 239Np followed by the subsequent decay (t1/2= 7 min) of 240Np
into 240Pu is treated as the direct production of 240Pu by neutron capture in 239Np.
These approximations have the beneficial effect for numerical solution techniques
of removing short timescales from the set of equations, without sacrificing
information of interest on the longer timescale of fuel burnup.
For reactors operating on the thorium cycle, the isotopic concentrations are
described by
@n02
@t
= −σ02
a ϕn02
@n03
@t
= σ02
γ ϕn02 − (λ03 + σ03
a ϕ)n03
@n13
@t
= λ03n03 − (λ13 + σ13
a ϕ)n13
@n22
@t
= −(λ22 + σ22
a ϕ)n22
@n23
@t
= σ22
γ ϕn22 + λ13n13 − σ23
a ϕn23
@n24
@t
= σ23
γ ϕn23 + σ13
γ ϕn13 − σ24
a ϕn24
(6.2)
@n25
@t
= σ24
γ ϕn24 − σ25
a ϕn25
@n26
@t
= σ25
γ ϕn25 − σ26
a ϕn26
@n27
@t
= σ26
γ ϕn26 − (λ27 + σ27
a ϕ)n27
@n37
@t
= λ27n27 − σ37
a ϕn37

<!-- page 201 (PDF 225) -->
Table 6.1 Cross Section and Decay Data for Fuel Isotopes
Isotope
Abundance (%)
t1/2
Decay
Mode
Energy
(MeV)
Spontaneous
Fission
Yield (%)
σth
γ (barns)
σth
f (barns)
RIγ (barns)
RIf (barns)
σχ
γ (barns)
σχ
f (barns)
232Th
1.41 × 1010 y
α
4.1
<1 × 10−9
–
–
0.09
0.08
233Th
–
22.3 m
β
1.2
–
0.09
0.11
234Th
–
24.1 d
β
0.27
–
–
–
0.11
0.04
233Pa
–
27.0 d
β
0.57
–
–
–
0.28
0.33
234Pa
–
6.7 h
β
2.2
–
–
–
–
–
–
–
232U
–
68.9 y
α
5.4
–
0.03
2.01
233U
–
1.59 × 105 y
α
4.9
<6 × 10−9
0.07
1.95
234U
0.0057
2.46 × 105 y
α
4.9
1.7 × 10−9
0.22
1.22
235U
0.719
7.04 × 108 y
α
4.7
7.0 × 10−9
0.09
1.24
236U
–
2.34 × 106 y
α
4.6
9.6 × 10−8
0.11
0.59
237U
–
6.75 d
β
0.52
–
0.93
0.74
238U
99.27
4.47 × 109 y
α
4.3
5 × 10−5
0.07
0.31
239U
–
23.5 m
β
1.3
–
–
−
–
−
–
–
240U
–
14.1 h
β
0.39
–
–
−
–
−
–
–
236Np
–
1.54 × 105 y
ec∗
0.94
–
0.19
1.92
β∗
0.49
–
–
−
–
–
–
–
237Np
–
2.14 × 106 y
α
5.0
<2 × 10−10
0.17
1.33
(continued )

<!-- page 202 (PDF 226) -->
Table 6.1
(Continued )
Isotope
Abundance (%)
t1/2
Decay
Mode
Energy
(MeV)
Spontaneous
Fission
Yield (%)
σth
γ (barns)
σth
f (barns)
RIγ (barns)
RIf (barns)
σχ
γ (barns)
σχ
f (barns)
238Np
–
2.12 d
β
1.3
–
0.11
1.42
239Np
–
236 d
β
0.72
–
–
–
0.19
1.46
240Np
–
–
–
–
–
–
–
–
–
–
–
236Pu
–
2.86 y
α
5.9
1.4 × 10−7
0.15
2.08
237Pu
–
ec∗
0.22
–
–
−
–
−
–
–
238Pu
–
87.7 y
α
5.6
1.9 × 10−7
0.10
1.99
239Pu
–
2.41 × 104 y
α
5.2
3 × 10−10
0.05
1.80
240Pu
–
6.56 × 103 y
α
5.3
5.7 × 10−6
0.10
1.36
241Pu
–
14.4 y
β
0.02
<2 × 10−14
0.12
1.65
242Pu
–
3.73 × 105 y
α
5.0
>5.5 × 10−4
–
–
0.09
1.13
241Am
–
432 y
α
5.6
4 × 10−10
0.23
1.38
Source: Brookhaven National Laboratory Nuclear Data Center, http://www.dne.bnl.gov/CoN/index.html.
∗87.3% electron capture, 12.5% β.

<!-- page 203 (PDF 227) -->
Another short timescale elimination approximation that neutron capture in 233Pa
leads directly to 234U has been made.

### Example 6.1 Depletion of a Pure 235U-Fueled Reactor

As an example of the
nature of the solution of the equations above, consider the hypothetical case of a
reactor initially fueled with pure 235U which operates for 1 year with a constant
neutron flux of 1014 n/cm2□s. The solution of the second of Eqs. (6.1) is n25(t) =
n25(0) exp(−σ25
a ϕt), where at the end of 1 year, σ25
a ϕt = (594 □ 10−24 cm2) □ (1 □
1014=cm2 ? s) □ (3:15 □ 107 s) = 1:87 and n25(t) = 0.154n25(0). The number of
atoms that have fissioned in this 1 year is (n(1)− n(0))× [σf/(σf + σγ)]= [0.846
n25(0)](507/594) = 0.722n25(0). Each fission event releases 192.9 MeV of recoverable
energy, so the total recoverable fission energy release is [0.722n25(0) fissions] ×
(192.9 MeV/fission) × (1.6× 10−19 MJ/MeV)= 2.23× 10−17 × n25(0) MJ. If the initial
core loading is 100 kg of 235U, this corresponds to (2.23 × 10−17) × (105/235) × (6.02
× 1023) = 0.95 × 109 MJ = 1.1 × 104 MWd of recoverable fission energy.
Neglecting the production of 236U by electron capture decay of 236Np, the
solution for n25(t) can be used to solve the third of Eqs. (6.1) to obtain
n26(t) = [n25(0)σ25
γ =(σ25
a − σ26
a )][exp(−σ26
a ϕt) − exp(−σ25
a ϕt)].
This
expression
for n26(t) can be used in the fourth of Eqs. (6.1) to obtain a similar, but more
complicated solution for n27(t), since we have assumed that n28 = 0; and so on.

### Fission Products

The fission event usually produces two intermediate mass nuclei, in addition to
releasing two or three neutrons. Interestingly, the fission product masses are not
usually equal to about half the mass of the fissioning species, but are distributed in
mass with peaks at about 100 and 140 amu, as shown in Fig. 6.2. The isotopes
10-1
10-2
235U
239Pu
10-3
MASS NUMBER A
PERCENT FISSION YIELD
Fig. 6.2 Fission yields for 235U and 239Pu.
(From Ref. [2].)

<!-- page 204 (PDF 228) -->
produced by fission tend to be neutron-rich and undergo radioactive decay. They
also undergo neutron capture, with cross sections ranging from a few tenths of a
barn to millions of barns. The general production–destruction equation satisfied
by a fission product species j is
dnj
dt = γjΣf ϕ +
X
i
(λi!j + σi!jϕ)ni − (λj + σj
aϕ)nj
(6.3)
where γj is the fraction of fission events that produces a fission product species j,
λi→j is the decay constant of isotope i to produce isotope j (beta, alpha, neutron,
etc., decay), and σi→j is the transmutation cross section for the production of
isotope j by neutron capture in isotope j. Even though the fission products
undergo transmutation and decay, the total inventory of direct fission products
plus their progeny increases in time as
dnf p
dt =
X
j
dnj
dt =
X
j
γj Σf ϕ
(6.4)

### Solution of the Depletion Equations

The discussed equations can be integrated to determine composition changes
over the lifetime of the reactor core loading if the time dependence of the flux is
known. However, the flux distribution depends on the composition. In practice, a
neutron flux distribution is calculated for the beginning-of-cycle composition and
critical control rod position or soluble boron concentration (PWR), and this flux
distribution is used to integrate the composition equations above over a depletion
-time step, Δtburn. Then the new critical control rod position or soluble boron
concentration is determined (by trial and error) and the flux distribution is
recalculated for use in integrating the production–destruction equations over the
next depletion time step, and so on, until the end of cycle is reached. The
maximum value of Δtburn depends on how fast the composition is changing and
the effect of that composition change on the neutron flux distribution and on the
accuracy of the numerical integration scheme. Excluding, for the moment, the
relatively short timescale phenomena associated with the xenon and samarium
fission products, the timescale of significant composition and flux changes is
typically several hundred hours or more.
The typical process of advancing the depletion solution from time ti, at which
the composition is known, to time ti+1 is (1) determine the multigroup constants
appropriate for the composition at ti, (2) determine the critical control rod
positions or soluble poison concentration by solving the multigroup diffusion
equations for the flux at ti (adjusting the control rod positions or boron
concentration until the reactor is critical), and (3) integrate the various fuel
and fission product production–destruction equations from ti to ti+1. (The
neutron flux solution could be made with a multigroup transport calculation
or with multigroup or continuous energy Monte Carlo calculation, and the
preparation of cross sections could involve infinite media spectra and unit cell
homogenization calculations or could be based on fitted, precomputed

<!-- page 205 (PDF 229) -->
constants.) The integration of the production–destruction equations can be for a
large number of points, using the neutron flux at each point; for each fuel pin,
using the average flux in the fuel pin; for each fuel assembly, using the average flux
over the fuel assembly; and so on.
Assuming that the flux is constant in the interval ti < t < ti+1, the production–
destruction equations can be written in matrix notation as
dN(t)
dt
= A(ϕ(ti))N(t) + F(ϕ(ti));
ti ≤ t ≤ ti+1
(6.5)
The general solution to these equations is of the form
N(ti+1) = exp[A(ti)Δt]N(ti) + A−1(ti)fexp[A(ti)Δt] − 1gF(ti)
(6.6)
In general, the accuracy of the solution depends on Δtburn being chosen so that
(λi + σi
aφ)Δtburn ≪1 for all of the isotopes involved. For this reason, it is
economical to reformulate the physical production–destruction equations to
eliminate short timescale phenomena that do not effect the overall result, as
discussed previously. There exist a number of computer codes that solve the
production–destruction equations for input neutron fluxes (e.g., Ref. [3]).

### Measure of Fuel Burnup

The most commonly used measure of fuel burnup is the fission energy release
per unit mass of fuel. The fission energy release in megawatt-days divided by the
total mass (in units of 1000 kg or 1 tonne) of fuel nuclei (fissile plus fertile) in the
initial loading is referred to as megawatt-days per tonne (MWd/T). An
equivalent unit is MWd/kg −10−3 MWd/T. For example, a reactor with
100,000 kg of fuel operating at 3000 MW power level for 1000 days would
have a burnup of 30,000 MWd/T.
For LWRs, the typical fuel burnup is 30,000–50,000 MWd/T. Fuel burnup in
fast reactors is projected up to be about 100,000–150,000 MWd/T.

### Fuel Composition Changes with Burnup

The original fissionable isotope (e.g., 235U) naturally decreases as the reactor
operates. However, the neutron transmutation of the fertile isotope (e.g., 238U)
produces the fissionable isotope 239Pu, which in turn is transmuted by neutron
capture into 240Pu and higher actinide isotopes. The buildup of the various Pu
isotopes as a function of fuel burnup for a typical LWR is shown in Fig. 6.3.
Compositions of spent fuel discharged from representative LWR and LMFBR
designs are given in Table 6.2. The units are densities (cgs units) times 10−24,
which allows construction of macroscopic cross section upon multiplication by
the microscopic cross section in barns. The composition for the average
enrichment and burnup of PWR spent fuel is shown in the first column for
fuel discharged before 1995 and in the second column for fuel discharged after
1995.

<!-- page 206 (PDF 230) -->
### Reactivity Effects of Fuel Composition Changes

There are a variety of reactivity effects associated with the change in fuel
composition. The fission of fuel nuclei produces two negative reactivity effects;
the number of fuel nuclei is reduced and fission products are created, many of
which have large neutron capture cross sections. The transmutation–decay chain
of fertile fuel nuclei of a given species produces a sequence of actinides (uraniumfueled
reactor) or uranium isotopes (thorium-fueled reactor), some of which are
fissile. The transmutation of one fertile isotope into another nonfissile isotope can
have a positive or negative reactivity effect, depending on the cross sections for
the isotopes involved, but the transmutation of a fertile isotope into a fissile
isotope has a positive reactivity effect. Depending on the initial enrichment, the
transmutation–decay process generally produces more fissile nuclei than are
destroyed early in the cycle, causing a positive reactivity effect, until the concentration
of transmuted fissile nuclei comes into equilibrium.
The buildup of 239Pu early in life of a uranium-fueled reactor produces a large
positive reactivity effect that may be greater than the negative reactivity effect of
10-1
Mass [g/kg HM initial]
Burnup [MWd/kg HM]
239Pu
240Pu
241Pu
242Pu
238Pu
Fig. 6.3 Buildup of Pu isotopes in 4 wt% enriched UO2 in an LWR. (With permission from
Ref. [4]. Copyright 1995, Nuclear Energy Agency, Paris.)

<!-- page 207 (PDF 231) -->
235U depletion and fission product buildup. For thermal reactors, η49 < η25, so the
buildup of 239Pu must exceed the burnup of 235U in order for a positive reactivity
effect. For fast reactors, η49 > η25 for neutron energies in excess of about 10 keV,
and there can be an initial positive reactivity effect even if the decrease in 235U is
greater than the buildup of 239Pu. However, the 239Pu concentration will saturate
at a value determined by the balance between the 238U transmutation rate and the
239Pu depletion rate, at which point the continued depletion of 235U and buildup
of fission products produce a negative reactivity effect that accrues over the
lifetime of the fuel in the reactor.

### Compensating for Fuel-Depletion Reactivity Effects

The reactivity effects of fuel depletion must be compensated to maintain
criticality over the fuel burnup cycle. The major compensating elements are
Table 6.2 Heavy Metal Composition of Spent UO2 Fuel at Discharge∗
Reactor Type
LWR
LWR
LMFBR
LMFBR
Initial enrichment (wt %)
3.13
4.11
Power (MW/MTU)
21.90
27.99
54.76
54.76
Burnup (GWd/T)
Actinides (1 × 1024 cm−3)
234U
3.92 × 10−6
4.51 × 10−6
3.37 × 10−5
2.88 × 10−5
235U
1.92 × 10−4
1.72 × 10−4
2.17 × 10−3
1.37 × 10−3
236U
8.73 × 10−5
1.23 × 10−4
4.58 × 10−4
5.62 × 10−4
237U
y)
2.48 × 10−7
5.71 × 10−7
7.89 × 10−7
238U
2.12 × 10−2
2.08 × 10−2
1.63 × 10−2
1.53 × 10−2
237Np
1.01 × 10−5
1.64 × 10−5
5.11 × 10−5
1.01 × 10−4
239Np
1.25 × 10−6
1.55 × 10−6
2.93 × 10−6
3.16 × 10−6
238Pu
3.36 × 10−6
6.56 × 10−6
3.84 × 10−6
1.20 × 10−5
239Pu
1.23 × 10−4
1.23 × 10−4
1.04 × 10−3
1.36 × 10−3
240Pu
4.05 × 10−5
4.28 × 10−5
7.83 × 10−5
1.71 × 10−4
241Pu
3.44 × 10−5
4.07 × 10−5
2.60 × 10−6
8.37 × 10−6
242Pu
1.05 × 10−5
1.69 × 10−5
y)
4.70 × 10−7
241Am
1.45 × 10−6
1.62 × 10−6
1.50 × 10−7
6.87 × 10−7
243Am
2.12 × 10−6
4.46 × 10−6
y)
y)
242Cm
3.71 × 10−7
5.66 × 10−7
y)
y)
244Cm
4.81 × 10−7
1.39 × 10−6
y)
y)
∗Calculated with ORIGEN (Ref [3]).
y) <0.001%.

<!-- page 208 (PDF 232) -->
the control rods, which can be inserted to compensate positive depletion
reactivity effects and withdrawn to compensate negative depletion reactivity
effects. Adjustment of the concentration of a neutron absorber (e.g., boron in
the form of boric acid) in the water coolant is another means used to compensate
for fuel-depletion reactivity effects. Soluble poisons are used to compensate fueldepletion
reactivity in PWRs but not in BWRs, because of the possibility that they
will plate out on boiling surfaces. Since a soluble poison introduces a positive
coolant temperature reactivity coefficient because an increase in temperature
decreases the density of the soluble neutron absorber, the maximum concentration
(hence the amount of fuel depletion reactivity that can be compensated) is
limited.
Burnable poisons (e.g., boron, erbium, or gadolinium elements located in the
fuel lattice), which themselves deplete over time, can be used to compensate the
negative reactivity effects of fuel depletion. The concentration of burnable poison
can be described by
dnbp
dt = −f bpnbpσbpϕ
(6.7)
where fbp is the self-shielding of the poison element (i.e., the ratio of the neutron
flux in the poison element to the neutron flux in the adjacent fuel assembly). The
poison concentration is chosen so that the spatial self-shielding of the poison
elements is large enough (fbp ≪1) early in the burnup cycle to shield the poison
from neutron capture, and the neutron capture rate remains constant in time.
After a certain time, the concentration of the poison nuclei is sufficiently reduced
that fbp increases and the poison burns out, resulting in an increasing reactivity. If
the poison starts to burn out at about the same time that the overall fuel depletion
reactivity effect starts to become progressively more negative (i.e., when the 239Pu
concentration saturates), the burnout of the poison will at least partially compensate
the fuel-depletion reactivity decrease.

### Reactivity Penalty

The buildup of actinides in the 238U transmutation–decay process introduces a
fuel reactivity penalty because some of actinides act primarily as parasitic
absorbers. While 239Pu and 241Pu are fissionable in a thermal reactor, and 240Pu
transmutes into 241Pu, 242Pu transmutes into 243Pu with a rather small cross
section, and 243Pu has a rather small fission cross section, so that 242Pu is
effectively a parasitic absorber that builds up in time. The 243Am also accumulates
and acts primarily as a parasitic absorber. Whereas the 243Am, which is
produced by the decay of 243Pu, can be separated readily, it is difficult to
separate the different plutonium isotopes from each other, so the negative 242Pu
reactivity effect is exacerbated if the plutonium is recycled with uranium. A
similar problem arises with the 236U produced by radiative capture in 235U, as
shown in Fig. 6.4, which is difficult to separate from 235U, and with 237Np, which
is produced by transmutation of 236U into 237U followed by beta decay. The
237Np can be separated readily, however, and does not need to accumulate in
recycled fuel.

<!-- page 209 (PDF 233) -->
End-of-cycle reactivity penalties calculated for the recycle of BWR fuel are
shown in Table 6.3 after one, two, and three cycles. It was assumed that the 237Np
and 243Am were removed between cycles, but there was a cycle-to-cycle increase
in the 237Np and 243Am reactivity penalties due to the accumulation of 236U and
242Pu, respectively.

### Effects of Fuel Depletion on the Power Distribution

Fuel depletion and the compensating control actions affect the reactor power
distribution over the lifetime of the fuel in the core. Depletion of fuel will be
greatest where the power is greatest. The initial positive reactivity effect of
depletion will then enhance the power peaking. At later times, the negative
reactivity effects will cause the power to shift away to regions with higher kinfinity.
Any strong tendency of the power distribution to peak as a result of fuel depletion
must be compensated by control rod movement. However, the control rod
585 b
(n,fis)
(n,fis)
(n,fis)
(n,γ)
(n,γ)
(n,γ)
(n,2n)
(n,2n)
110 b
37.5 b
45 mb
3.9 mb
238 b
270 b
2.85 yr
80 b
235U
236U
236Np
237Np
238Np
236Pu
237U
232U
238U
EC
6.75 d
22 hr
22 hr
43%
57%
β–
α
β–
Fig. 6.4 235U neutron transmutation–decay chain. (With permission from Ref. [5]. Copyright
1990, American Nuclear Society.)
Table 6.3 Reactivity Penalties with Recycled BWR Fuel (% Δk/k)
End of Cycle
236U
237Np
242Pu
243Am
0.62
0.13
0.65
0.36
0.90
0.59
1.53
0.57
1.12
0.73
2.04
0.89
Source: Data from Ref. [6].

<!-- page 210 (PDF 234) -->
movement to offset fuel depletion reactivity effects itself produces power peaking;
the presence of the rods shields the nearby fuel from depletion and when the rods
are withdrawn, the higher local k∝causes power peaking. Similarly, burnable
poisons shield the nearby fuel, producing local regions of higher k∝and power
peaking when they burn out. Determination of the proper fuel concentration
zoning and distribution of burnable poisons and of the proper control rod motion
to compensate fuel depletion reactivity effects without unduly large power
peaking is a major nuclear analysis task.

### In-Core Fuel Management

At any given time, the fuel in a reactor core will consist of several batches that
have been in the core for different lengths of time. The choice of the number of
batches is made on the basis of a trade-off between maximizing fuel burnup and
minimizing the number of shutdowns for refueling, which reduces the plant
capacity factor. At each refueling, the batch of fuel with the highest burnup is
discharged, the batches with lower burnup may be moved to different locations,
and a fresh or partially depleted batch is added to replace the discharged batch.
The analysis leading to determination of the distribution of the fuel batches
within the core to meet the safety, power distribution, and burnup, or cycle
length constraints for fuel burn cycle is known as fuel management analysis.
Although fuel management may be planned in advance, it must be updated
online to adjust to higher or lower capacity factors than planned (which result
in lower or higher reactivity than planned at the planned refueling time) and
unforeseen outages (which result in higher reactivity than planned at the
planned refueling time).
Typically, a PWR will have three fuel batches, and a BWR will have four fuel
batches in the core at any given time and will refuel every 12–18 months. A
number of different loading patterns have been considered, with the general
conclusion that more energy is extracted from the fuel when the power distribution
in the core is as flat as possible. In the in–out loading pattern, the reactor is
divided into concentric annular regions loaded with different fuel batches. The
fresh fuel batch is placed at the periphery, the highest burnup batch is placed at
the center, and intermediate burnup batches are placed in between to counter the
natural tendency of power to peak in the center of the core. At refueling, the
central batch is discharged, the other batches are shifted inward, and a fresh batch
is loaded on the periphery. The in–out loading pattern has been found to go too
far in the sense that the power distribution is depressed in the center and peaked
at the periphery. An additional difficulty is the production of a large number of
fast neutrons at the periphery that leak from the core and damage the pressure
vessel.
In the scatter loading pattern, the reactor core is divided into many small
regions of four to six assemblies from different batches. At refueling, the
assemblies within each region with the highest burnup are discharged and
replaced by fresh fuel assemblies. This loading pattern has been found to produce
a more uniform power distribution and to result in less fast neutron leakage than
the in–out pattern.

<!-- page 211 (PDF 235) -->
Since the pressure vessel damage by fast neutrons became recognized as a
significant problem, a number of different loading patterns have been developed
with the specific objective of minimizing neutron damage to the pressure vessel.
These include placement of only partially depleted assemblies at the core
periphery, placement of highly depleted assemblies near welds and other critical
locations, using burnable poisons in peripheral assemblies, replacing peripheral
fuel assemblies with dummy assemblies, and others.
Better utilization of resources argues for the highest possible fuel burnup
consistent with materials damage limitations, and a new higher enrichment fuel
has been developed that can achieve burnups of up to 50,000 MWd/T in LWRs.
The higher fuel burnup produces more actinides and fission products with large
thermal neutron cross sections, which compete more effectively with control rods
for thermal neutrons and reduces control rod worth, and which produces larger
coolant temperature reactivity coefficients. The higher enrichment higher burnup
fuel also provides the possibility of longer refueling cycles, which improves plant
capacity factor and reduces power costs.

## 6.2 Samarium and Xenon

The short-term time dependence of two fission product progeny, 149Sm and
135Xe, which have very large absorption cross sections, introduces some interesting
reactivity transients when the reactor power level is changed.

### Samarium Poisoning

Samarium-149 is produced by the beta decay of the fission product 149Nd, as
described in Fig. 6.5. It has a thermal neutron absorption cross section of 4 × 104
barns and a large epithermal absorption resonance. The 1.7-h half-life of 149Nd is
sufficiently short that 149Pm can be assumed to be formed directly from fission in
writing the production–destruction equations for 149Sm:
dP
dt = γNdΣf ϕ − λPP
dS
dt = λPP − σS
aϕS
(6.8)
where P and S refer to 149Pm and 149Sm, respectively. These equations have the
solution, for constant ϕ,
P(t) = γNdΣf ϕ
λP
(1 − e−λPt) + P(0)e−λPt
S(t) = S(0)e−σS
aϕt + γNdΣf
σS
a
(1 − e−σS
aϕt)
− γNdΣf ϕ − λPP(0)
λP − σS
aϕ
(e−σS
aϕt − e−λPt)
(6.9)

<!-- page 212 (PDF 236) -->
At the beginning of life in a fresh core, P(0) = S(0) = 0, and the promethium and
samarium concentrations build up to equilibrium values:
Peq = γNdΣf ϕ
λP
;
Seq = γNdΣf
σS
a
(6.10)
The equilibrium value of 149Pm depends on the neutron flux level. However, the
equilibrium value of 149Sm is determined by a balance between the fission
production rate of 149Pm and the neutron transmutation rate of 149Sm, both
of which are proportional to the neutron flux, and consequently, does not depend
on the neutron flux level. The time required for the achievement of equilibrium
concentrations depends on ϕ, σS
a, and λP. For typical thermal reactor flux levels
(e.g., 5 × 1013 n/cm2 □ s), equilibrium levels are achieved in a few hundred hours.
When a reactor is shut down after running sufficiently long to build up
equilibrium concentrations, the solutions of Eqs. (6.9) with P(0) = Peq, S(0) = Seq,
150Sm
40 × 103 b
149Nd
1.7 h
(a)
(c)
β-
149Pm
149Sm
53 h
β-
(n,γ)
233U
235U
239Pu
(b)
FISSILE
NUCLIDE
0.0066
0.0113
0.0190
γNd
SAMARIUM-149 CONCENTRATION (at/cm3)
TIME, h
SHUTDOWN
INITIAL STARTUP
1.0 × 1016
0.5 × 1016
RESTART
Fig. 6.5 Characteristics of 149Sm under representative LWR conditions. (a) Transmutation–
decay chain. (b) Fission yields. (c) Time dependence. (With permission from Ref. [1].
Copyright 1992, Taylor & Francis/Hemisphere Publishing.)

<!-- page 213 (PDF 237) -->
and ϕ = 0 are
P(t) = Peqe−λPt
S(t) = Seq + Peq(1 − e−λPt) ! Seq + Peq
(6.11)
indicating that the 149Sm concentration will increase to Seq + Peq as the 149Pm
decays into 149Sm with time constant 1/λP = 78 h. If the reactor is restarted, the
149Sm burns out until the 149Pm builds up; then the 149Sm returns to its
equilibrium value. This time dependence of the samarium concentration is
illustrated in Fig. 6.5.
The perturbation theory estimate for the reactivity worth of 149Sm is
ρ(t)
Sm = − S(t)σS
a
Σa
(6.12)
which for the equilibrium concentration becomes
ρeq
Sm = − γNdΣf
σS
a
σS
a
Σa
= −γNd Σf
Σa
= − γNd
ν
(6.13)
where we have used the approximation that k ≈ νΣf/Σa = 1. For a 235U-fueled
reactor, ρeq
Sm ≈ 0:0045.

### Xenon Poisoning

Xenon-135 has a thermal absorption cross section of 2.6 × 106 barns. It is
produced directly from fission, with yield γXe, and from the decay of 135I, which
in turn is produced by the decay of the direct fission product 135Te, with yield γTe,
as indicated in Fig. 6.6. The production–destruction equations may be written,
with the assumption that 135I is produced directly from fission with yield γTe,
dI(t)
dt
= γTeΣf ϕ − λII
dX(t)
dt
= γXeΣf ϕ + λII − (λX + σX
a ϕ)X
(6.14)
These equations have the solutions
I(t)
= γTeΣf ϕ
λI
(1 − e−λIt) + I(0)e−λIt
X(t) = (γTe + γXe)Σf ϕ
λX + σX
a ϕ
1 − e−(λX+σX
a ϕ)t
h
i
+ γTeΣf ϕ − λII(0)
λX − λI + σX
a ϕ
e−(λX+σX
a ϕ)t − e−λIt
h
i
+ X(0)e−(λX+σX
a ϕ)t
(6.15)

<!-- page 214 (PDF 238) -->
When the reactor is started up from a clean condition in which X(0) = I (0) = 0, or
the reactor power level is changed, the 135I and 135Xe concentrations approach
equilibrium values
Ieq = γTeΣf ϕ
λI
;
Xeq = (γTe + γXe)Σf ϕ
λX + σX
a ϕ
(6.16)
136Xe
2.6 × 106 b
2.3 × 106 y
3 × 1015
2 × 1015
1 × 1015
135Te
γ(135Te)
γ(135Xe)
19 s
(a)
(c)
β-
135I
135Xe
6.6 h
FISSION
β-
9.1 h
β-
135Cs
135Ba
135Xe CONCENTRATION at/cm3
β-
(n,γ)
233U
235U
239Pu
(b)
FISSILE
NUCLIDE
0.051
0.061
0.055
0.003
TIME FROM INITIAL STARTUP, h
INITIAL STARTUP
SHUTDOWN
RESTART
Fig. 6.6 Characteristics of 135Xe under representative LWR conditions: (a) transmutation–
decay chain; (b) fission yields; (c) time dependence. (With permission from Ref. [1]. Copyright
1992, Taylor & Francis/Hemisphere Publishing.)

<!-- page 215 (PDF 239) -->
with time constants 1/λI = 0.1 h and 1/(λX + σX
a φ) ≈ 30 h, respectively. The
perturbation theory estimate of the reactivity worth of equilibrium xenon is
ρeq
Xe = − σX
a (γTe + γXe)Σf ϕ
Σa(λX + σX
a ϕ)
' −
γTe + γXe
ν(1 + λX=σX
a ϕ)
= −
0:026
1 + (0:756 □ 1013)=ϕ
(6.17)

### Peak Xenon

When a reactor is shut down from an equilibrium xenon condition, the iodine and
xenon populations satisfy Eqs. (6.15) with I(0) = Ieq, X(0) = Xeq, and ϕ = 0:
I(t)
= Ieqe−λIt
X(t) = Xeqe−λXt + Ieq
λI
λI − λX (e−λXt − e−λIt)
(6.18)
If ϕ > (γX/γTe)(λX=σX
a ), the xenon will build up after shutdown to a peak value at
time
tPk =
λI − λX ln
λI=λX
1 + (λX=λI)(λI=λX − 1)(Xeq=Ieq)
(6.19)
and then decay to zero unless the reactor is restarted. For 235U- and 233U-fueled
reactors, ϕ > 4 × 1011 and 3 × 1012 n/cm2 □ s, respectively, is sufficient for an
increase in the xenon concentration following shutdown. Typical flux values (e.g.,
5 × 1013 n/cm2 □ s) in thermal reactors are well above these threshold levels, and
for typical flux values, Eq. (6.19) yields a peak xenon time of ≈11.6 h. If the reactor
is restarted before the xenon has entirely decayed, the xenon concentration will
initially decrease because of the burnout of xenon and then gradually build up
again because of the decay of a growing iodine concentration, returning to values
of Ieq and Xeq for the new power level. This time dependence of the xenon
concentration is illustrated in Fig. 6.6.

### Effect of Power-Level Changes

When the power level changes in a reactor (e.g., in load following), the xenon
concentration will change. Consider a reactor operating at equilibrium iodine
Ieq(ϕ0) and xenon Xeq(ϕ0) at flux level ϕ0. At t = t0, the flux changes from ϕ0 to ϕ1.
Equations (6.15) can be written as
I(t)
= Ieq(ϕ1) 1 − ϕ1 − ϕ0
ϕ1
e−λIt

X(t) = Xeq(ϕ1) 1 − ϕ1 − ϕ0
ϕ1
λX
λX + σX
a ϕ0
e−(λX+σX
a ϕ1)t

+
γTe
γTe + γXe
λX + σX
a ϕ1
λX − λI + σX
a ϕ1
e−λIt − e−(λX+σX
a ϕ1)t
h
i
(6.20)

<!-- page 216 (PDF 240) -->
The xenon concentration during a transient of this type is shown in Fig. 6.7.
The perturbation theory estimate for the reactivity worth of xenon at any time
during the transient discussed above is
ρXe(t) = − σX
a X(t)
Σa
' − σX
a X(t)
νΣf
(6.21)

### Example 6.2 Xenon Reactivity Worth

As an example of xenon buildup,
consider a 235U-fueled reactor that has operated at a thermal flux level of 5 × 1013
cm−2 s−1 for 2 months such that equilibrium xenon and iodine have built in to the
levels given by Eqs. (6.16). Using σX
a = 2:6 □ 10−18cm2, tI
1=2 = 9:1 h; λ = ln 2=t1=2,
λ = ln 2/t1/2, γTe = 0.061, and γXe = 0.003, the equilibrium values of xenon and
iodine are Xeq = 0.0203 × 1018Σf cm−3 and Ieq = 0.1051 × 1018Σf cm−3. The
reactivity worth of equilibrium xenon is ρeq
Xe ≈ σX
a Xeq=Σa ≈ 0:022Δk=k, where
the approximate criticality condition νΣf ≈ Σa has been used.
ϕ(t)
t0
t1
t
ϕ0
ϕ0
ϕ1
I(t)
t0
t1
t
I∞0
I∞0
I∞1
X(t)
t0
t1
t
X∞0
X∞0
X∞1
Fig. 6.7 Xenon concentration following power-level changes. (With permission from Ref. [7].
Copyright 1976, John Wiley & Sons.)
