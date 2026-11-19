# 6 Fuel Burnup — 6.3 Fertile-to-Fissile Conversion and Breeding … 6.8 Utilization of Uranium Energy Content
<!-- source PDF pages 241-259 -->

<!-- page 217 (PDF 241) -->
If the reactor is shut down for 6 h and then restarted, the xenon reactivity
worth that must be compensated is, from Eqs. (6.16) and (6.21), ρXe(t = 6 h) ≈ σX
a X
(t = 6 h)/νΣf = (0.634Xeq + 0.367Ieq) × σX
a /νΣf = 0.0171 + 0.04 = 0.0571Δk/k. The
largest contribution to the xenon worth at 6 h after shutdown clearly comes from
buildup of xenon from the decay of the iodine concentration at shutdown at a
faster rate than the resulting xenon decays.

## 6.3 Fertile-to-Fissile Conversion and Breeding

### Availability of Neutrons

The transmutation–decay processes depicted in Fig. 6.1 hold out the potential for
increasing the recoverable energy content from the world’s uranium and thorium
resources by almost two orders of magnitude by converting the fertile isotopes
238U and 232Th, which only fission at very high neutron energies, into fissile
isotopes, 239Pu and 241Pu in the case of 238U, and 233U in the case of 232Th, which
have large fission cross sections for thermal neutrons and substantial fission cross
sections for fast neutrons. The rate of transmutation of fertile-to-fissile isotopes
depends on the number of neutrons in excess of those needed to maintain the
chain fission reaction that are available. In the absence of neutron absorption by
anything other than fuel and in the absence of leakage, the number of excess
neutrons is η − 1. The quantity η is plotted in Fig. 6.8 for the principal fissile
isotopes.
The fertile-to-fissile conversion characteristics depend on the fuel cycle and
the neutron energy spectrum. For a thermal neutron spectrum (E < 1 eV), 233U
has the largest value of η of the fissile nuclei. Thus, the best possibility for
fertile-to-fissile conversion in a thermal spectrum is with the 232Th–233U fuel
cycle. For a fast neutron spectrum (E > 5 × 104 eV), 239Pu and 241Pu have the
largest values of η of the fissile nuclei. The LMFBR, based on the 238U–239Pu
fuel cycle, is intended to take advantage of the increase of η49 at high neutron
energy.

### Conversion and Breeding Ratios

The instantaneous conversion ratio is defined as the ratio of the rate of creation of
new fissile isotopes to the rate of destruction of fissile isotopes. When this ratio is
greater than unity, it is conventional to speak of a breeding ratio, because the
reactor would then be producing more fissile material than it was consuming.
Average conversion or breeding ratios calculated for reference reactor designs of
various types are shown in Table 6.4.
The values of the conversion ratios for the PWR and BWR are the same because
of design similarities. The HTGR conversion ratio is somewhat higher because of
the higher value of η for 233U than for 235U. The improved conversion ratio for the
CANDU–PHWR is due to the better neutron economy provided by online
refueling and consequent reduced requirements for control poisons to compensate
excess reactivity.

<!-- page 218 (PDF 242) -->
The breeding ratio in an LMFBR can vary over a rather wide range, depending
on the neutron energy spectrum. Achieving a large value of η and hence a large
breeding ratio favors a hard neutron spectrum. However, a softer spectrum is
favored for safety reasons – the lower energy neutrons that are subject to
resonance absorption become more likely to be radiatively captured than to
cause fission as the neutron energy is reduced, as discussed in Chapter 5. The
breeding ratio in a LMFBR depends sensitively on the choice of fuel type and the
fuel volume fraction, as shown in Fig. 6.9.
3.0
2.5
2.0
1.5
1.0
0.5
Pu-239
η
Pu-241
U-233
U-235
Pu-23
U-235
U-235
U-233
Pu-241
0.01
0.1
1.0
ENERGY, eV
4.0
3.5
3.0
2.5
2.0
1keV
1MeV
Pu-239
U-235
U-233
Pu-241
η
1.5
1.0
ENERGY, eV
Fig. 6.8 Parameter η for the principal fissile nuclei. (With permission from Ref. [8]. Copyright
1977, Electric Power Research Institute.)

<!-- page 219 (PDF 243) -->
## 6.4 Simple Model of Fuel Depletion

The concepts involved in fuel depletion and the compensating control adjustment
canbe illustrated bya simplemodelinwhich thecriticalityrequirement is written as
k = ηf =
ηΣF
a(t)
ΣF
a(t) + ΣM
a + Σfp
a (t) + Σc(t) = 1
(6.22)
where ΣF
a is the fuel macroscopic absorption cross section, ΣM
a
the moderator
macroscopic absorption cross section, and ΣC
a the combined (soluble and burnable
Table 6.4 Conversion/Breeding Ratios in Different Reactor Systems
Reactor System
Initial Fuel
Conversion Cycle
Conversion Ratio
BWR
2–4 wt% 235U
238U–239Pu
0.6
PWR
2–4 wt% 235U
238U–239Pu
0.6
PHWR
Natural U
238U–239Pu
0.8
HTGR
≈5 wt% 235U
232Th–233U
0.8
LMFBR
10–20 wt% Pu
238U–239Pu
1.0–1.6
Source: Data from Ref. [1]; used with permission of Taylor & Francis/Hemisphere Publishing.
Fig. 6.9 LMFBR breeding ratios as a function of fuel type and fuel volume fraction. (With
permission from Ref. [9]. Copyright 2011, Y. I. Chang.)

<!-- page 220 (PDF 244) -->
poisons plus control rod) control absorption cross section. Assuming that the reactor
operates at constant power νΣF
f (t)ϕ(t) = νΣF
f (0)ϕ(0) and that η = νΣF
f =ΣF
a is constant
in time, the fuel macroscopic absorption cross section at any time is
ΣF
a(t) = NF(t)σF
a = σF
a NF(0) − ϵσF
a
R t
0 NF(t´)ϕ(t´)dt´
h
i
= NF(0)σF
a[1 − ϵϕ(0)σF
at]
(6.23)
The neutron flux is related to the beginning-of-cycle neutron flux by
ϕ(t) =
ϕ(0)
1 − ϵσF
aϕ(0)t
(6.24)
where ϵ < 1 is a factor that accounts for the production of new fissionable nuclei
via transmutation–decay.
The fission product cross section is the sum of the equilibrium xenon and
samarium cross sections constructed using Eqs. (6.16) and (6.10), respectively,
and an effective cross section for the other fission products,
Σfp´ = σfp´γfp´Σf (t)ϕ(t)t = σfp´γfp´Σf (0)ϕ(0)t
(6.25)
which accumulate in time from fission with yield γfp´. The quantity γfp´σfp´ is about
40–50 barns per fission. Using these results, Eq. (6.22) can be solved for the value
of the control cross section that is necessary to maintain criticality:
Σc(t) = (η − 1)ΣF
a(0) 1 − σF
aϵϕ(0)t

− ΣM
a − (γTe + γXe)Σf (0)ϕ(0)
λX=σX
a + ϕ(t)
− γNdΣf (0)[1 − ϵσF
aϕ(0)t] − σfp´γfp´Σf (0)ϕ(0)t
(6.26)
The soluble poison will be removed by the end of cycle, and the burnable poisons
should be fully depleted by that time. Thus, the lifetime, or cycle time, is the time
at which the reactor can no longer be maintained critical with the control rods
withdrawn as fully as allowed by safety considerations. This minimum control
cross section is small, and we set it to zero. The end-of-cycle time can be
determined from Eq. (6.26) by setting ΣC
a = 0 and solving for tEOC:
tEOC =
ηρex(1 + α) − (γTe + γXe)ϕ(0)σX
a =λX − γNd
[(η − 1)(1 + α)σF
a − γNdσF
a + γfp´]ϕ(0)
;
ϕ(t) □ λX
σX
a
ηρex(1 + α) − (γTe + γXe + γNd)
[(η − 1)(1 + α)σF
a − (γTe + γXe + γNd)σF
a + γfp´σfp´]ϕ(0) ; ϕ(t) □ λX
σX
a
>
>
>
>
<
>
>
>
>
:
(6.27)
where α is the capture-to-fission ratio for the fuel, and
ρex ≡ k1(0) − 1
k1(0)
(6.28)
is the excess reactivity at beginning-of-cycle without xenon, samarium, fission
products, or control cross section. The initial control cross section (including

<!-- page 221 (PDF 245) -->
soluble and burnable poisons) must be able to produce a negative reactivity
greater than ρex. It is clear from Eq. (6.27) that the cycle lifetime is inversely
proportional to the power, or flux, level.

## 6.5 Fuel Reprocessing and Recycling

A substantial amount of plutonium is produced by neutron transmutation of 238U
in LWRs. About 220 kg of fissionable plutonium (mainly 239Pu and 241Pu) is
present in the spent fuel discharged from an LWR at a burnup of 45 GWd/T. The
spent fuel can be reprocessed to recover the plutonium (and remaining enriched
uranium) for recycling as new fuel.

### Composition of Recycled LWR Fuel

The potential energy content of the fissile and fertile isotopes remaining in spent
reactor fuel (Table 6.2) constitutes a substantial fraction of the potential energy
content of the initial fuel loading, providing an incentive to recover the uranium
and plutonium isotopes for reuse as reactor fuel. The recycled plutonium
concentrations calculated for successive core reloads of a PWR are shown in
Table 6.5. The initial core loading and the first reload were slightly enriched UO2.
The plutonium discharged from the first cycle was recycled in the third cycle, that
discharged from the second cycle was recycled in the fourth cycle, and so on, in
separate mixed oxide (MOX) UPuO2 pins. The proportion of MOX increases
from about 18% in the second reload to just under 30% in the sixth and
subsequent reloads, for which reloads the plutonium recovered from spent
Table 6.5 Plutonium Concentrations in a PWR Recycling Only Self-Generated
Plutonium (wt%)
Loading:
Recycle:
235U in UO2
2.14
3.0
3.0
3.0
3.0
3.0
3.0
Pu in MOX
–
–
4.72
5.83
6.89
7.51
8.05
MOX of fuel
–
–
18.4
23.4
26.5
27.8
28.8
235U discharged
0.83
–
–
–
–
–
–
Discharged Pu
239Pu
56.8
56.8
49.7
44.6
42.1
40.9
40.0
240Pu
23.8
23.8
27.0
38.7
29.4
29.6
29.8
241Pu
14.3
14.3
16.2
17.2
17.4
17.4
17.3
242Pu
5.1
5.1
7.1
9.5
11.1
12.1
12.9
Source: Data from Ref. [1]; used with permission of Taylor & Francis/Hemisphere Publishing.

<!-- page 222 (PDF 246) -->
MOX and UO2 fuel is about the same as was loaded into this fuel at beginning-ofcycle
(i.e., the plutonium concentration reaches equilibrium). The percentage of
plutonium in MOX increases from less than 5% on the initial recycle load to about
8% in equilibrium, in order to offset the reactivity penalty.

### Physics Differences of MOX Cores

The use of MOX fuels in PWRs changes the physics characteristics in several
ways. The variation with energy of the cross sections for the plutonium isotopes is
more complex than for the uranium isotopes, as shown in Fig. 6.10. The
absorption cross sections for the plutonium isotopes are about twice those of
the uranium isotopes in a thermal spectrum and are characterized by large
absorption resonances in the epithermal (0.3–1.5 eV) range and by overlapping
resonances. Representative thermal neutron spectra in UO2 and MOX fuel cells
are compared in Fig. 6.11.
Thermal parameters for 235U and 239Pu, averaged over a representative LWR
thermal neutron energy distribution, are given in Table 6.6. Because of the larger
thermal absorption cross section for 239Pu, the reactivity worth of control rods,
burnable poisons, and soluble poisons (PWRs) will be less with MOX fuel than
with UO2, unless the MOX rods can be placed well away from control rods and
burnable poisons. The higher 239Pu fission cross section will lead to greater power
peaking with MOX than with UO2, unless the MOX rods are placed well away
from water gaps.
There are reactivity differences between MOX and UO2. The buildup of 240Pu
and 242Pu with the recycling MOX fuel accumulates parasitic absorbers that
results in a reactivity penalty, as discussed in Section 6.1. The average thermal
ABSORPTION CROSS SECTION (b)
0.001
0.01
2200 m/s
8400 b
235U
239Pu
240Pu
0.1
ENERGY (eV)
1.0
3.0
Fig. 6.10 Thermal absorption cross sections for 235U,239Pu and 240Pu. (With permission from
Ref. [5]. Copyright 1990, American Nuclear Society.)

<!-- page 223 (PDF 247) -->
value of η is less for 239Pu than for 235U, which requires a larger fissile loading to
achieve the same initial excess reactivity with MOX as with UO2. Furthermore,
the temperature defect is greater for MOX because of the large low-energy
resonances in 239Pu and 240Pu shown in Fig. 6.10. However, the reactivity decrease
with burnup is less for MOX than for UO2, because of the lower η for 239Pu than
for 235U, and because of the transmutation of 240Pu into fissionable 241Pu, so that
less excess reactivity is needed.
Φ(E)
10-1
Pu-Rod
U-Rod
Burnup 0 MWd/t
Burnup 29000 MWd/t
10-2
10-3
10-2
10-1
E.eV
Fig. 6.11 Thermal neutron spectra in UO2 and MOX PWR fuel cells. (With permission from
Ref. [4]. Copyright 1995, Nuclear Energy Agency, Paris.)
Table 6.6 Thermal Parameters for 235U and 239Pu in a LWR
Parameter
235U
239Pu
Fission cross section σf (barns)
Absorption cross section σa (barns)
Nu-fission to absorption η
2.07
1.90
Delayed neutron fraction β
0.0065
0.0021
Generation time Λ (s)
4.7 × 10−5
2.7 × 10−5
Source: Data from Ref. [5]; used with permission of American Nuclear Society.

<!-- page 224 (PDF 248) -->
The delayed neutron fractions for 239Pu, 241Pu, and 235U are in the ratio 0.0020/
0.0054/0.0064, which means that the reactivity insertion required to reach prompt
criticalrunawayconditionsislessforMOXthanforUO2byafactorthatdependson
the 239Pu/241Pu/235U ratio. As the 241Pu builds up with repeated recycle, the
difference between MOX and UO2 decreases. The neutron generation time is also
shorter for MOX than for UO2, so that any prompt supercritical excursion would
have a shorter period. The fission spectrum neutrons are more energetic for 239Pu
than for 235U. On the other hand, because of the large epithermal absorption
resonances in the plutonium isotopes, the moderator andfuel Doppler temperature
coefficients of reactivity tend to be more negative for MOX cores than for UO2
cores. Accumulation of actinides, which are strong emitters of energetic alpha
particles, leads to higher radioactive decay heat removal requirements with MOX.
These considerations would tend to limit the MOX fraction in a reload core.
The yield of 135Xe is about the same for the fission of plutonium as for the
fission of uranium. Due to the higher thermal absorption cross section of the
plutonium isotopes, the excess reactivity needed to start up at peak xenon
conditions and the propensity for spatial flux oscillations driven by xenon
oscillations (Chapter 16) are less in a MOX than a UO2 core.
For plutonium recycle in other reactor types, similar types of physics considerations
would enter. However, the different relative values of η for 235U and 239Pu
in different spectra (e.g., the epithermal spectrum of a HTGR and the fast
spectrum of a LMFBR) would lead to different conclusions about reactivity
penalties. In fact, LMFBRs have been designed from the outset with the concept of
switching from 235U to 239Pu as the latter was bred.

### Physics Considerations with Uranium Recycle

Although it is relatively straightforward to separate uranium from other chemically
distinct isotopes, it is impractical to separate the various uranium isotopes
from each other in the reprocessing step. So recycling uranium means recycling
all of the uranium isotopes, some of which are just parasitic absorbers and another
of which leads through subsequent decay to the emission of an energetic gamma.
Two isotopes present in relatively small concentrations in fresh fuel (234U and
236U) necessitate adding 235U to enrich reprocessed uranium to a higher enrichment
than is required with fresh uranium fuel. Uranium-234 has a large
absorption resonance integral and, while only a tiny fraction in natural uranium,
will tend to be enriched along with 235U. Uranium-236 is produced by neutron
capture in 235U and by electron capture in 236Np, as shown in Fig. 6.4, and is a
parasitic neutron absorber with a significant capture resonance integral. Reprocessed
uranium is made difficult to handle by the decay product 208Ti, which emits
a 2.6-MeV gamma with t1/2 = 3.1 min. This radioisotope is produced by a series of
alpha decays of 232U, which is produced by the chain shown in Fig. 6.4.

### Physics Considerations with Plutonium Recycle

The same type of difficulties exists for plutonium reprocessing as discussed for
uranium – all of the plutonium isotopes must be recycled. Plutonium-236 decays into
232U, which leads to the emission of a 2.6-MeV gamma, as described already.

<!-- page 225 (PDF 249) -->
Plutonium-238 is produced through neutron transmutation of 237Np; it alpha decays
witht1/2= 88yearsandconstitutesalargeshutdownheatsourceifpresentinsufficient
quantity.Plutonium-240hasanenormouscaptureresonanceintegral.Both 238Pu and
240Pu contribute a large spontaneous fission neutron source. Plutonium-241, while
having a large fission cross section, also decays into 241Am, which has a large thermal
capture cross section and a large capture resonance integral. Americium-241 also
decays into daughter products that are energetic gamma emitters. Stored plutonium
loses its potency as a fuel over time because of the decay of 241Pu into 241Am.
Plutonium from spent LWR fuel at a typical burnup of about 35,000MWd/T must be
utilized within 3 years after discharge or it will be necessary to reprocess it again to
remove the 241Am and daughter products.

### Reactor Fueling Characteristics

Nuclear fuel cycles with plutonium recycle have been studied extensively (e.g.,
Ref. [4]). Representative equilibrium fueling characteristics for LWRs operating
on the 238U–239Pu and 232Th–233U fuel cycles and for a LMFBR operating on the
238U–239Pu fuel cycle are shown in Table 6.7. Fuel is partially discharged and
replenished each year (annual discharge and annual reload), requiring a net
amount of new fuel (annual makeup) from outside sources. In the absence of
reprocessing and recycling, the annual reload would have to be supplied from
outside sources. The LMFBR produces more fuel than it uses and could provide
the extra fuel needed by the LWRs from the transmutation of 238U if LMFBRs and
LWRs were deployed in the ratio of about 7:5.

## 6.6 Radioactive Waste

### Radioactivity

The actinides produced in the transmutation–decay of the fuel isotopes and the
fission products are the major contributors to the radioactive waste produced in
Table 6.7 Representative Fueling Characteristics of 1000-MWt Reactors
Reactor Type
Characteristic
LWR
LWR
LMFBR
Fuel cycle
232Th–233U
238U–239Pu
238U–239Pu
Conversion ratio
0.78
0.71
1.32
Initial core load (kg)
1,580
2,150
3,160
Burnup (MWd/T)
35,000
33,000
100,000
Annual reload (kg)
1,000
1,480
Annual discharge (kg)
1,690
Annual makeup (kg)
(−210)
Source: Data from Ref. [10]; used with permission of International Atomic Energy Agency.

<!-- page 226 (PDF 250) -->
nuclear reactors, although activated structure and other materials are also
present. The activity per ton of fuel for representative LWR and LMFBR
discharges are given in Table 6.8. The fission products account for almost the
entire radioactivity of spent fuel at reactor shutdown, but because of their short
half-lives, this radioactivity level decays relatively quickly. In fact, the radioactivity
of the spent fuel decreases substantially within the first 6 months after removal
from the reactor, as shown in Table 6.8. The more troublesome fission products
from the waste management point of view are those with long half-lives like 99Tc
(t1/2 = 2.1 × 105 years) and 129I (t1/2 = 1.59 × 107 years) and those that are gamma
emitters, such as 90Sr and 137Cs, which produce substantial decay heating. The
actinides constitute a relatively small part of the total radioactivity at reactor
shutdown but become relatively more important with time because of the longer
half-lives of 239Pu and 240Pu and dominate the radioactivity of spent fuel after
about 1000 years.

### Hazard Potential

A simple, but useful, measure of the hazard potential of radioactive material is the
hazard index, defined as the quantity of water required to dilute the material to
the maximum permissible concentration for human consumption. The hazard
index for spent LWR fuel is plotted against time after shutdown in Fig. 6.12.
Fission products dominate the hazard index up to about 1000 years after shutdown
, beyond which time the transuranics (actinides) become dominant. Including
the plutonium in the recycled uranium fuel increases the hazard potential
because of the continued buildup of 239Pu and 240Pu. Beyond 1000–10,000 years
after shutdown, depending on burnup, the hazard potential of spent reactor fuel is
less than the hazard potential of uranium ore as it is mined from the earth.

### Risk Factor

In an effort to relate the radioactivity of a given radioisotope to a health hazard,
the number of curies of radiation from a given radioisotope that would cause
cancer (on the average) if swallowed by a person has been estimated and is shown
as the cancer dose per curie (CD/Ci) in Table 6.9. The CD/Ci is not an absolute
measure of the biological hazard of a given amount of radioactive material,
because it does not contain any measure of the probability for a sequence of
events that would result in individual members of a population actually swallowing
exactly the amount of radioisotopes that would produce a cancer, and no
more. However, the CD/Ci can be used to construct a relative measure of the
biological hazard potential. The CD/ton (of heavy metal in the fuel) due to
the radioisotopes in discharged fuel given in Table 6.8 can be multiplied by the
number of tons of heavy metal spent fuel discharged from a reactor to construct a
total cancer dose (TCD). A similar total cancer dose of natural uranium
(TCDNU) as it is mined from the earth can be constructed by multiplying the
Ci/ton for the radioisotopes in natural uranium by the mass of natural uranium
that was required to produce the discharged fuel for which the TCD is calculated.
(Typically, about 5 tons of natural uranium is needed to produce the fuel for a

<!-- page 227 (PDF 251) -->
Table 6.8 Radioactivity of Representative LWR and LMFBR Spent Fuel at Discharge and at
180 Days (LWR) or 30 Days (LMFBR) After Discharge∗
Nuclide
Half-Life t1/2
Radiationsy)
Activity (Ci/tonne Heavy Metal)
LWR Fuel
LMFBR Fuel
Discharge
180 d
Discharge
30 d
3H
12.3 y
β
5.744 × 102
5.587 × 102
1.648 × 103
1.640 × 103
85Kr
10.73 y
β, γ
1.108 × 104
1.074 × 104
1.473 × 104
1.466 × 104
89Sr
50.5 d
β, γ
1.058 × 106
9.603 × 104
1.333 × 106
8.939 × 105
90Sr
29.0 y
β, γ
8.425 × 104
8.323 × 104
9.591 × 104
9.572 × 104
90Y
64.0 h
β, γ
8.850 × 104
8.325 × 104
1.214 × 105
9.572 × 104
91Y
59.0 d
β, γ
1.263 × 106
1.525 × 105
1.794 × 106
1.269 × 106
95Zr
64.0 d
β, γ
1.637 × 106
2.437 × 105
3.215 × 106
2.340 × 106
95Nb
3.50 d
β, γ
1.557 × 106
4.689 × 105
3.149 × 106
2.954 × 106
99Mo
66.0 h
β, γ
1.875 × 106
3.780 × 10−14 4.040 × 106
2.108 × 103
99mTc
6.0 h
γ
1.618 × 106
3.589 × 10−14 3.487 × 106
2.002 × 103
99Tc
2.1 × 105 y
β, γ
1.435 × 101
1.442 × 101
3.278 × 101
3.293 × 101
103Ru
40.0 d
β, γ
1.560 × 106
6.680 × 104
4.617 × 106
2.730 × 106
106Ru
369.0 d
β, γ
4.935 × 105
3.519 × 105
2.248 × 106
2.125 × 106
103mRh
56.0 min
γ
1.561 × 106
6.686 × 104
4.619 × 106
2.733 × 106
111Ag
7.47 d
β, γ
5.375 × 104
3.005 × 10−3
2.294 × 105
1.422 × 104
115Cd
44.6 d
β, γ
1.483 × 103
9.042 × 101
7.041 × 103
4.418 × 103
125Sn
9.65 d
β, γ
1.081 × 104
2.624 × 10−2
3.404 × 104
3.946 × 103
124Sb
60.2 d
β, γ
4.147 × 102
5.219 × 101
2.329 × 103
1.649 × 103
125Sb
2.73 y
β, γ
9.525 × 103
8.498 × 103
5.251 × 104
5.171 × 104
125mTe
58.0 d
γ
1.976 × 103
2.031 × 103
1.121 × 104
1.144 × 104
127mTe
109.0 d
β, γ
1.384 × 104
4.595 × 103
4.969 × 104
4.265 × 104
127Te
9.4 h
β, γ
9.920 × 104
4.500 × 103
3.247 × 105
4.308 × 104
129mTe
33.4 d
β, γ
8.508 × 104
2.041 × 103
2.316 × 105
1.249 × 105
129Te
70.0 min
β, γ
3.211 × 105
1.296 × 103
8.454 × 105
7.932 × 104
132Te
78.0 h
β, γ
1.486 × 106
3.159 × 10−11 3.473 × 106
5.783 × 103
129I
1.59 × 107 y
β, γ
3.219 × 10−2 3.268 × 10−2
1.033 × 10−1 1.040 × 10−1
131I
8.04 d
β, γ
1.028 × 106
1.933 × 10−1
2.602 × 106
2.020 × 105
132I
2.285 h
β, γ
1.511 × 106
3.254 × 10−11 3.546 × 106
5.956 × 103
133Xe
5.29 d
β, γ
2.098 × 106
1.612 × 10−4
4.414 × 106
1.076 × 105
134Cs
2.06 y
β, γ
2.718 × 105
2.303 × 105
8.283 × 104
8.058 × 104
(continued )

<!-- page 228 (PDF 252) -->
PWR.) The risk factor is then defined as RF TCD/TCDNU, which may be
interpreted as the ratio of the number of cancers that would be caused by
individual members of a population swallowing all of the discharged fuel in
portions just sufficient to produce a cancer (on average) to the number of cancers
that would be caused by individual members of a population swallowing 5 tons of
natural uranium in portions just sufficient to produce a cancer (on average). The
advantage of the risk factor is that the highly uncertain probability of ingestion of
Table 6.8
(Continued )
Nuclide
Half-Life t1/2
Radiationsy)
Activity (Ci/tonne Heavy Metal)
LWR Fuel
LMFBR Fuel
Discharge
180 d
Discharge
30 d
136Cs
13.0 d
β, γ
6.962 × 104
4.719 × 100
2.577 × 105
5.204 × 104
137Cs
30.1 y
β, γ
1.115 × 105
1.102 × 105
2.522 × 105
2.518 × 105
140Ba
12.79 d
β, γ
1.953 × 106
1.133 × 102
3.636 × 106
7.153 × 105
140La
40.23 h
β, γ
2.019 × 106
1.303 × 102
3.698 × 104
8.238 × 105
141Ce
32.53 d
β, γ
1.784 × 106
3.876 × 104
3.730 × 106
1.979 × 106
144Ce
284.0 d
β, γ
1.229 × 106
7.925 × 105
2.148 × 106
1.996 × 106
143Pr
13.58 d
β
1.657 × 106
1.887 × 102
3.044 × 106
7.349 × 105
147Nd
10.99 d
β, γ
7.902 × 105
9.278 × 100
1.513 × 106
2.283 × 105
147Pm
2.62 y
β, γ
1.031 × 105
9.859 × 104
6.344 × 105
6.353 × 105
149Pm
53.1 h
β, γ
3.919 × 105
1.326 × 10−19 9.842 × 105
8.451 × 101
151Sm
93.0 y
β+, β−, γ
8.658 × 102
8.696 × 102
9.693 × 103
9.703 × 103
152Eu
13.4 y
β+, β−, γ
7.838 × 100
7.635 × 100
4.759 × 101
4.738 × 101
155Eu
4.8 y
β, γ
2.540 × 103
2.365 × 103
4.305 × 104
4.255 × 104
160Tb
72.3 d
β, γ
1.418 × 103
2.525 × 102
4.880 × 103
3.661 × 103
239Np
2.35 d
β, γ
2.435 × 107
2.050 × 101
5.990 × 107
8.727 × 103
238Pu
87.8 y
α, γ
2.899 × 103
3.021 × 103
2.770 × 104
2.820 × 104
239Pu
2.44 × 104 y
α, γ, SF
3.250 × 102
3.314 × 102
6.247 × 103
6.263 × 103
240Pu
6.54 × 103 y
α, γ, SF
4.842 × 102
4.843 × 102
8.323 × 103
8.323 × 103
241Pu
15.0 y
α, β, γ
1.098 × 105
1.072 × 105
7.280 × 105
7.252 × 105
241Am
433.0 y
α, γ, SF
8.023 × 101
1.657 × 102
9.091 × 103
9.186 × 103
242Cm
163.0 d
α, γ, SF
3.666 × 104
1.717 × 104
8.467 × 105
7.489 × 105
244Cm
17.9 d
α, γ
2.772 × 103
2.720 × 103
8.032 × 103
8.007 × 103
∗Calculated with ORIGEN (Ref [3].).
y)
α: alpha particle; β: electron; γ: gamma ray; SF: spontaneous fission.

<!-- page 229 (PDF 253) -->
radioisotopes is normalized out by being treated in the same (highly questionable)
way in the numerator (TCD) and denominator (TCDNU), so that RF is a measure
of the relative cancer potential of spent fuel and of the natural uranium from
which it was produced.
FISSION PRODUCT
AGE OF WASTES, y
HAZARD INDEX, m3 WATER
TRANSURANICS:
1) PLUTONIUM RECYCLE
2) URANIUM
    RECYCLE
URANIUM
ORE
STRUCTURAL
MATERIAL
ACTIVATION
Fig. 6.12 Hazard index for spent LWR fuel as a function of time since reactor shutdown.
(With permission from Ref. [11]. Copyright 1977, Woods Hole Oceanographic Institute.)
Table 6.9 Cancer Dose per Curie for Radioisotopes Present in Spent Fuel∗
Isotope
Toxicity Factor (CD/Ci)
Half-Life (years)
Toxicity Factor (CD/g)
Actinides and Their Daughters
210Pb
455.0
22.3
3.48 × 104
223Ra
15.6
0.03
7.99 × 105
226Ra
36.3
1.60 × 103
3.59 × 101
227Ac
1185.0
21.8
8.58 × 104
229Th
127.3
7.3 × 103
2.72 × 101
230Th
19.1
7.54 × 104
3.94 × 10−1
231Pa
372.0
3.28 × 104
1.76 × 10−1
234U
7.59
2.46 × 105
4.71 × 10−2
235U
7.23
7.04 × 108
1.56 × 10−5
(continued )

<!-- page 230 (PDF 254) -->
Table 6.9
(Continued )
Isotope
Toxicity Factor (CD/Ci)
Half-Life (years)
Toxicity Factor (CD/g)
236U
7.50
2.34 × 107
4.85 × 10−4
238U
6.97
4.47 × 109
2.34 × 10−6
237Np
197.2
2.14 × 106
1.39 × 10−1
238Pu
246.1
87.7
4.22 × 103
239Pu
267.5
2.41 × 104
1.66 × 101
240Pu
267.5
6.56 × 103
6.08 × 101
242Pu
267.5
3.75 × 105
1.65 × 100
241Am
272.9
9.36 × 102
242 mAm
267.5
2.80 × 104
243Am
272.9
7.37 × 103
5.45 × 101
242Cm
6.90
0.45
2.29 × 104
243Cm
196.9
29.1
9.96 × 103
244Cm
163.0
18.1
1.32 × 104
245Cm
284.0
8.5 × 103
4.88 × 101
246Cm
284.0
4.8 × 103
8.67 × 101
Short-Lived Fission Products
90Sr
16.7
29.1
2.28 × 103
90Y
0.60
7.3 × 10−3
3.26 × 105
137Cs
5.77
30.2
4.99 × 102
Long-Lived Fission Products
99Tc
0.17
2.13 × 105
2.28 × 10−3
129I
64.8
1.57 × 107
1.15 × 10−2
93Zr
0.095
1.5 × 106
2.44 × 10−4
135Cs
0.84
2.3 × 106
9.68 × 10−4
14C
0.20
5.73 × 103
8.92 × 10−1
59Ni
0.08
7.6 × 104
6.38 × 10−3
63Ni
0.03
1.70 × 100
126Sn
1.70
1.0 × 105
4.83 × 10−2
Source: Data from Ref. [4]; used with permission of Nuclear Energy Agency, Paris.
∗The toxicity factors are constructed using the methodology described by Bernard L. Cohn, “Effects of
the ICRP Publication 30 and the 1980 BEIR Report of Hazard Assessments of High Level Waste,”
Health Phys. 42 (2) 133–143 (1982) with the following data: ICRP Publication 30, Part 4, 88, 19, and
BEIR III, 80, 19. The factors stand for the fatal cancer doses per gram of isotope injected orally. They
denote the hazard of the material rather than the risk because they do not include any account of
pathway attenuation processes, but simply assume oral ingestion.

<!-- page 231 (PDF 255) -->
The risk factor is plotted for a typical spent fuel loading from a LWR in
Fig. 6.13. The short-lived fission products are dominant in the decades following
discharge, but the fission product activity becomes negligible relative to the
actinide activity after about 200–300 years. The potential α-toxicity of the
actinide concentration is dominated by 241Am over the first 5000 years, then by
240Pu up to about 100,000 years, and thereafter by 237Np. Note that when the
risk factor becomes less than unity, the cancer potential of the spent fuel is less
than the cancer potential of the natural uranium ore from which it was
originally made.
The long-term potential α-toxicity of spent fuel can be reduced dramatically by
recycling the fuel. Figure 6.14 illustrates risk factor for the same LWR fuel as in
Fig. 6.13, but now with the Pu, Am, and Np recycled to 99.5% annihilation. After
about 200–300 years, the potential α-toxicity of the spent fuel is less than that of
the natural uranium from which it was originally produced. As discussed in
Section 6.8, repeatedly recycling the spent fuel to 99.5% annihilation may be
feasible, from neutron balance considerations, in a fast spectrum reactor, but does
not appear to be feasible in a thermal reactor.
10-1
10-2
10-3
Risk factor
Total (fission products)
Total (actinides)
244Cm
241Am
243Am
240Pu
238Pu
229Th
237Np
Time, y
Fig. 6.13 Risk factor for LWR spent fuel without recycle. (With permission from Ref. [12].
Copyright 1986, Elsevier Science Publishers.)

<!-- page 232 (PDF 256) -->
## 6.7 Burning Surplus Weapons-Grade Uranium and Plutonium

### Composition of Weapons-Grade Uranium and Plutonium

With the reduction in nuclear weapons worldwide, surplus highly enriched,
weapons-grade uranium and plutonium become available for use as fuel in
nuclear reactors. The composition of typical weapons-grade uranium and plutonium
is compared with the composition of reactor-grade uranium and plutonium
in Table 6.10. Reactor-grade here refers to the typical enriched uranium used in
LWRs and the plutonium composition created by transmutation in LWR fuel.
Although it is feasible to de-enrich the weapons-grade uranium, the weaponsgrade
plutonium would be used as is.

### Physics Differences Between Weapons- and Reactor-Grade Plutonium-Fueled Reactors

There are some similarities and some important differences between using weaponsand
reactor-grade plutonium in an LWR designed for low-enrichment uranium fuel.
10-1
10-2
10-3
Risk factor
Total (fission products)
Total (actinides)
244Cm
241Am
243Am
240Pu
232Pu
237Np
Time, y
Fig. 6.14 Risk factor for LWR spent fuel with 99.5% recycle of Pu, Am, and Np.
(With permission from Ref. [12]. Copyright 1986, Elsevier Science Publishers.)

<!-- page 233 (PDF 257) -->
The delayed neutron fractions for thermal fission of 239Pu, 241Pu, and 235U are in the
ratio 0.0021:0.0049:0.0065. Because the delayed neutron fraction is smaller in 239Pu
thanin 235U,thesubprompt-criticalreactivityrangeismuchlessforplutonium-fueled
reactors than for uranium-fueled reactors, as discussed in Section 6.5; and because the
delayed neutron fraction is much smaller in 239Pu than in 241Pu, reactors fueled with
weapons-grade plutonium will have an even smaller subprompt-critical reactivity
range than reactors fueled with reactor-grade plutonium.
The large resonance integral of 240Pu contributes a significant negative Doppler
coefficient when reactor-grade plutonium is used, but which is absent when
weapons-grade plutonium is used. Similarly, the use of weapons-grade uranium
with the low 238U content would substantially reduced the negative 238U Doppler
coefficient relative to the use of reactor-grade uranium. A resonance absorber,
such as tungsten, can be added to weapons-grade fuel in order to recover part of
the negative Doppler coefficient. Calculated Doppler coefficients for a standard
LWR UO2 lattice with reactor-grade uranium and for various combinations of
UO2ZrO2 and W with weapons-grade uranium and plutonium are given in
Table 6.11. Because of the higher fission cross section and higher value of η for
Table 6.10 Composition of Weapons- and Reactor-Grade Uranium and Plutonium (wt%)
Weapons-
Grade Pu
Reactor-
Grade Pu
Weapons-
Grade U (HEU)
Reactor-
Grade U (LEU)
Natural U
238Pu
0.01
1.30
234U
0.12
0.025
0.0057
239Pu
93.80
60.30
235U
94.00
3.500
0.7193
240Pu
5.80
24.30
238U
5.88
96.475
99.2750
241Pu
0.13
5.60
242Pu
0.02
5.00
241Am
0.22
3.50
Source: Data from Ref. [13]; used with permission of National Academy Press.
Table 6.11 Fuel Doppler Temperature Coefficients of Reactivity with Weapons-Grade
Plutonium
Composition
Δk/k (×10 −5)
R-G UO2 (3% 235U)
−2.4720
W-G UO2-ZrO2 (0.6% UO2)
−0.0017
W-G UO2-ZrO2 +W (3%UO)
−1.0357
W-G MOX-ZrO2 (2.7% UO2, 0.3% PuO2)
−0.9588
W-G PuO2-ZrO2 (0.34% PuO2)
−0.0009
W-G PuO2-ZrO2 + W (3% PuO2)
−1.2003

<!-- page 234 (PDF 258) -->
239Pu than for 235U in a fast neutron spectrum, weapons-grade plutonium fuel
projects superior performance to uranium fuel in fast breeder reactors.

## 6.8 Utilization of Uranium Energy Content

Only about 1% of the energy content of the uranium used to produce the fuel is
extracted (via fission) in a typical LWR fuel cycle. About 3% of the energy content
of the mined uranium is stored as tails from the original uranium fuel production
process, and about 96% remains in the depleted uranium from the enrichment
process and in the discharged spent fuel in the form of uranium, plutonium, and
higher actinide isotopes. With continued reprocessing and recycling of spent fuel
and depleted uranium, there is the possibility of recovering much of this
remaining energy. The projected worldwide consumption of uranium based
on the LWR once-through fuel cycle is shown in Fig. 6.15.
To fully consume the initial uranium feedstream, for each transuranic atom
fissioned there must be one neutron released to sustain the chain reaction and one
neutron available for capture in 238U (or 240Pu) to produce 239Pu (or 241Pu) to
replace the fissioned atom. There is, of course unavoidable parasitic capture in
fission products, structure, and the transuranic elements. The continued recycling
of spent fuel would lead, after long exposure, to equilibrium distributions of
the transuranic isotopes in the recycled fuel, as shown for thermal and fast
neutron spectra in Table 6.12. (Note that these concentrations could be altered by
blending spent fuels from different numbers of recycles.)
The number of neutrons per fission lost to parasitic capture in the transuranics
can be estimated from their capture and fission probabilities, which are shown in
Fig. 6.16 for typical LWR and LMR spectra. For the equilibrium distribution of
Table 6.12, the number of neutrons per fission lost to parasitic capture is typically
about 0.25 in a fast neutron spectrum and 1.25 in a thermal neutron spectrum. This
means that a minimum (not accounting for parasitic capture in fission products,
Cumulative Natural U
(Million Tonnes)
Year
Fast Reactors
Introduced 2050
Fast Reactors
Introduced 2030
LWR Once Through
Speculative Resources
Known
Resources
Fig. 6.15 Worldwide uranium resource utilization.

<!-- page 235 (PDF 259) -->
control elements, and structure or leakage) number of neutrons released per fission
to maintain the chain reaction and transmute a fertile isotope into a fissionable
isotope to replace each fissioned isotope is 2.25 for the LWR spectrum and 3.25 for
theLMRspectrum.Physically, more neutronsarewastedtransmutinga transuranic
nuclide into another transuranic nuclide in a thermal spectrum than in a fast
spectrum. Since 2.5 < η ≪3.25, total energy extraction by repeated recycling in a
thermal reactor is not possible, but it may be in a fast reactor.
The projected uranium utilization of LWRs together with fast breeder reactors
that would transmute the nonfissile 238U into fissile 239Pu for burning in the LWRs
is compared with the utilization of LWRs operating on the once-through cycle in
Fig. 6.15. Clearly, the early deployment of fast breeder reactors is essential if nuclear
power is to achieve its potential in meeting the world’s growing energy demands.
Table 6.12 Equilibrium Distribution of Transuranic Isotopic Masses (%) for Continuously
Recycled Fuel in Thermal and Fast Reactor Neutron Spectra
Isotope
Thermal Reactor Spectrum
Fast Reactor Spectrum
237Np
5.51
0.75
238Pu
4.17
0.89
239Pu
23.03
66.75
240Pu
10.49
24.48
241Pu
9.48
2.98
242Pu
3.89
1.86
241Am
0.54
0.97
242Am
0.02
0.07
243Am
8.11
0.44
242Cm
0.18
0.40
243Cm
0.02
0.03
244Cm
17.85
0.28
245Cm
1.27
0.07
246Cm
11.71
0.03
247Cm
0.75
2. × 10−3
248Cm
2.77
6. × 10−4
249Bk
0.05
1. × 10−5
249Cf
0.03
4. × 10−5
250Cf
0.03
7. × 10−6
251Cf
0.02
9. × 10−7
252Cf
0.08
4. × 10−8
Source: Data from Ref. [14].
