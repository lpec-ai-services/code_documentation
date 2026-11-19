# 2 Neutron Chain Fission Reactors
<!-- source PDF pages 57-66 -->

<!-- page 33 (PDF 57) -->
# 2 Neutron Chain Fission Reactors

## 2.1 Neutron Chain Fission Reactions

Since two or three neutrons are released in every neutron-induced fission
reaction, the possibility of a sustained neutron chain reaction is obvious, as
illustrated in Fig. 2.1. To sustain a fission chain reaction, one or more of the
neutrons produced in the fission event must, on average, survive to produce
another fission event. There is competition for the fission neutrons in any
assembly – some will be absorbed in fuel nuclides as radiative capture events
rather than fission events, some will be absorbed by nonfuel nuclides, and some
will leak out of the assembly. A scattering event does not compete for a neutron
because the scattered neutron remains in the assembly and available for causing a
fission event, but a scattering event does change a neutron’s energy and thus,
because the various cross sections are energy dependent, does change the relative
likelihood of the next collision being a fission event.

### Capture-to-Fission Ratio

The fission cross sections for the fissile nuclides increase approximately as 1/υ
with decreasing neutron energy, but then so do the capture cross sections of the
fissile nuclides. The probability that a neutron that is captured in a fissile nuclide
causes a fission is just σf/(σf + σγ) = 1/(1 + σγ/σf) = 1/(1 + α), where α ≡ σγ/σf is
referred to as the capture-to-fission ratio. The capture-to-fission ratio for the
principal fissile nuclides decreases as the neutron energy increases. For high
neutron energies, the fission probability, which varies as (1 + α)−1, is larger for
239Pu than for 235U or 233U, but the situation is reversed for low-energy thermal
neutrons.

### Number of Fission Neutrons per Neutron Absorbed in Fuel

The product of the fission probability for a neutron absorbed in the fuel and the
average number of neutrons released per fission, η ≡ νσf/(σf + σγ) = ν/(1 + α),
provides a somewhat better characterization of the relative capabilities of the
Nuclear Reactor Physics, Third Edition. Weston M. Stacey.
2018 Wiley-VCH Verlag GmbH & Co. KGaA. Published 2018 by Wiley-VCH Verlag GmbH & Co. KGaA.

<!-- page 34 (PDF 58) -->
various fissile nuclides to sustain a fission chain reaction. This quantity is plotted
in Fig. 2.2 for the principal fissile nuclides. For high neutron energies, η is larger
for 239Pu than for 235U or 233U, but the situation is reversed for low-energy
thermal neutrons.

### Neutron Utilization

The probability that a neutron is absorbed in a fuel nuclide instead of being
absorbed in another nuclide or leaking from the assembly is
absorb fissile
absorb fissile + absorb nonfissile + leak
= absorb fissile
absorb total
(1 + leak=absorb total) ≡ f PNL
(2.1)
where f is the fraction of the absorbed neutrons that are absorbed in the fuel
nuclides, or the utilization:
f =
Nfisσfis
a
Nfisσfis
a + Notherσother
a
(2.2)
and PNL refers to the nonleakage probability. Since the absorption cross section,
σa = σf + σγ, is much greater for thermal neutrons than for fast neutrons for the
fissile nuclides, but comparable for fast and thermal neutrons for the nonfissile
fuel nuclides and for structural nuclides, the utilization for a given composition is
much greater for thermal neutrons than for fast neutrons (and, in fact, is usually
referred to as the thermal utilization).
Fig. 2.1 Schematic of a fission chain reaction. (With permission from Ref. [1]. Copyright 1976,
Wiley.)

<!-- page 35 (PDF 59) -->
### Fast Fission

The product ηf is the number of neutrons produced, on average, from the fission
of fissile nuclides for each neutron absorbed in the assembly. There will also be
neutrons produced by the fission of the nonfissile fuel nuclides, mostly by fast
neutrons. Defining the fast fission factor ε ≡ total fission neutron production rate/
fission neutron production rate in fissile nuclides, ηfε is the total number of fission
neutrons produced for each neutron absorbed in the assembly, and ηfεPNL is the
U-233
U-235
Pu-239
Pu-241
U-235
Pu-239
1 keV
1 MeV
1.0
1.5
2.0
2.5
3.0
3.5
4.0
0.01
0.1
1.0
Env (E), eV / cm2 s
Env (E), eV / cm2 s
0.5
1.0
1.5
2.0
2.5
3.0
U-233
U-233
U-235
Pu-241
Pu-23
U-235
Pu-241
η
η
Fig. 2.2 η for the principal fissile nuclides. (With permission from Ref. [2]. Copyright 1977,
Electric Power Research Institute.)

<!-- page 36 (PDF 60) -->
total number of fission neutrons produced, on average, for each neutron introduced
into the assembly by a previous fission event.

### Resonance Escape

The parameters ηfε must be evaluated by averaging over the energy of the
neutrons in the assembly, of course. When the neutron population predominantly
consists of thermal neutrons, the thermal spectrum-averaged cross sections given
in Table 1.3 may be used to estimate η and f, and the cross sections averaged over
the fission spectrum may be used in estimating ε, which should now also include
fast fission in the fissile nuclides. In this case, it is necessary to take into account
separately the capture of fission neutrons while they are slowing down to the
thermal energy range, predominantly by the capture resonances of the fuel
nuclides. The probability that a neutron is not captured during the slowingdown
process is referred to as the resonance escape probability and denoted p.
This competition for neutrons is schematically illustrated in Fig. 2.3 (leakage is
neglected).
pfηε FISSION
NEUTRONS
pfη(ε–1)
NEUTRONS
FROM FAST
FISSION
pfη/ν NEUTRONS
CAUSE THERMAL
FISSION
pfη NEUTRONS
FROM THERMAL
FISSION
FAST
RESONANCE
THERMAL
ν
NEUTRONS
PER
FISSION
THERMAL
FISSION
p NEUTRONS
REACH THERMAL
ENERGIES
1 INITIAL
FISSION
NEUTRON
RESONANCE
ABSORPTION
FAST
FISSION
NONFUEL
ABSORPTION
pf NEUTRONS
ABSORBED
NONFISSION
ABSORPTION
IN FUEL
IN FUEL
Fig. 2.3 Neutron balance in a thermal neutron fission assembly. (With permission from
Ref. [3]. Copyright 1992, Taylor & Francis.)

<!-- page 37 (PDF 61) -->
## 2.2 Criticality

### Effective Multiplication Constant

The product ηfεpPNL is the total number of fission neutrons produced, on
average, by one fast neutron from a previous fission event. This quantity is
referred to as the effective multiplication constant of the assembly:
k = ηf εpPNL ≡ k1PNL
(2.3)
where k1 refers to the multiplication constant of an infinite assembly with no
leakage.
If exactly one neutron, on average, survives to cause another fission, a condition
referred to as criticality (k = 1), the neutron population in the assembly will
remain constant. If less than one neutron, on average, survives to produce another
fission event, a condition referred to as subcriticality (k < 1), the neutron
population in the assembly will decrease. If more than one fission neutron, on
average, survives to cause another fission, a condition referred to as supercriticality
(k > 1), the neutron population in the assembly will increase. The
effective multiplication constant depends on the composition (k1) and size (PNL)
of an assembly and on the arrangement of the materials within the assembly (f and
p). The composition affects k both by the relative number of nuclides of different
species that are present and by the determination of the neutron energy
distribution, which determines the average cross sections for each nuclide.
The arrangement of materials determines the spatial neutron distribution and
hence the relative number of neutrons at the locations of the various nuclides.
The fissile nuclide 235U is only 0.72% of natural uranium. Fuel enrichment to
achieve a higher fissile content, hence larger value of f, is a major means of
increasing the multiplication constant. The number of fission neutrons produced
for each neutron absorbed in fissile material, η, is significantly larger for fast
neutrons than for thermal neutrons because the capture-to-fission ratio is smaller
and the number of neutrons per fission is larger. On the other hand, for a given
fuel enrichment, the utilization, f, is greater for thermal neutrons than for fast
neutrons because the absorption cross section is much greater for thermal
neutrons than for fast neutrons for the fissile nuclides, but comparable for
fast and thermal neutrons for the nonfissile fuel nuclides and for structural
nuclides. On the whole, the amount of fissile material necessary to achieve a given
value of the multiplication constant is substantially less in a fast neutron spectrum
than in a thermal neutron spectrum.

### Effect of Fuel Lumping

Lumping the fuel rather than distributing it uniformly can have a significant
effect on the multiplication constant. For example, if natural uranium is
distributed uniformly in a graphite lattice, the values of the various parameters
are η ≈ 1.33, f ≈ 0.9, ε ≈ 1.05, and p ≈ 0.7, yielding k1 ≈ 0.88 (i.e., the assembly is
subcritical). If the fuel is lumped, the strong resonance absorption at the

<!-- page 38 (PDF 62) -->
exterior of the fuel elements reduces the number of neutrons that reach the
interior of the fuel elements, increasing the resonance escape probability to
p ≈ 0.9. Lumping the fuel also reduces the thermal utilization f, for the same
reason, but the effect is not so significant. Lumping the fuel was the key to
achieving criticality (k = 1) in the first graphite-moderated natural uranium
reactors and is crucial in achieving criticality in present-day D2O-moderated
natural uranium reactors.

### Leakage Reduction

The multiplication constant can be increased by reducing the leakage, most of
which is due to fast neutrons. This can be done simply by increasing the size. The
leakage can also be reduced by choosing a composition that moderates the
neutrons quickly before they can travel far or by surrounding the assembly with a
material with a large scattering cross section (e.g., graphite), which will reflect
leaking neutrons back into the assembly.

### Example 2.1 Effective Multiplication Factor for a PWR

For a typical pressurized
water reactor (PWR), the various parameters are η ≈ 1.65, f ≈ 0.71, ε ≈ 1.02,
and p ≈ 0.87, yielding k1 ≈ 1.04. The nonleakage factors for fast and thermal
neutrons are typically 0.97 and 0.99, yielding k ≈ 1.00.

## 2.3 Time Dependence of a Neutron Fission Chain Assembly

### Prompt Fission Neutron Time Dependence

If there are N0 fission neutrons introduced into an assembly at t = 0, and if l is
the average time required for a fission neutron to slow down and be absorbed or
leak out, l =
vΣf υ, the number of neutrons, on average, in the assembly at time
t = l is (k)N0. Continuing in this fashion, the number of neutrons in the
assembly at time t = ml (m integer) is (k)mN0. The quantity l is typically
≈10−4 s for assemblies in which the neutrons slow down to thermal before
causing another fission, and is typically ≈10−6 s for assemblies in which the
fission is produced by fast neutrons. For example, a 1
2% change in absorption cross
section, which could be produced by control rod motion, causes an approximately
0.005 change in k. The neutron population after 0.1 s in a thermal assembly
(0.1 s = 103l), in which k = 1.005, would be N(0.1) = (1.005)1000N0 ≈ 150N0. In a
thermal assembly with k = 0.995, the neutron population after 0.1 s would be N
(0.1) = (0.995)1000 N0 ≈ 0.0066N0.
An equation governing the neutron kinetics described above is
dN t( )
dt
= k − 1
l
N t( ) + S t( )
(2.4)
which simply states that the time rate of change of the neutron population is equal
to the excess of neutron production (by fission) minus neutron loss by absorption

<!-- page 39 (PDF 63) -->
or leakage in a neutron lifetime plus any external source that is present. For a
constant source, Eq. (2.4) has the solution
N t( ) = N 0
( )e k−1
)t=l +
Sl
k − 1 e(k−1)t=l − 1
h
i
(2.5)
which displays an exponential time behavior. Using the same example as above,
with the source set to zero, leads to N(0.1) = N(0) exp(5.0) = 148N(0) for k = 1.005
and N(0.1) = N(0) exp(−5.0) = 0.00 677N(0) for k = 0.995.

### Source Multiplication

Equation (2.4) does not have a steady-state solution for k > 1 and does not have
a unique steady-state solution for k = 1. However, for k < 1, the asymptotic
solution is
Nasymptotic = lS0
1 − k
(2.6)
This equation provides a method to measure the effective multiplication factor k
when k < 1 by measuring the asymptotic neutron population that results from
placing a source S0 in a multiplying medium.

### Effect of Delayed Neutrons

It would be very difficult, if not impossible, to control a neutron fission chain
assembly that responded so dramatically to a 1
2% change in absorption cross
section. Fortunately, a small fraction (β ≈ 0.0075 for 235U-fueled reactors) of the
fission neutrons is delayed until the decay (λ ≈ 0.08 s−1) of the fission fragments.
For an assembly that was critical prior to t = 0, the equilibrium concentration of
such delayed neutron precursor fission fragments is found from the balance
equation:
dC0
dt = 0 = βvNf σf υN0 − λC0 = β
l N0 − λC0
(2.7)
where Nf is the density of fuel nuclei, N0 is the neutron population, and C0 is the
population of delayed neutron precursor fission fragments.
When the 1
2% change in cross section occurs at t = 0, the multiplication of the
prompt neutrons after 0.1 s (1000l) is [(1 − β)k]1000. During each multiplication
interval l, there is a source λlC of delayed neutrons from the decay of fission
fragments. This source results in (1 − β)kλlC neutrons in the following multiplication
interval, [(1 − β)k]2λlC neutrons in the second following multiplication
interval, and so on. There is such a delayed neutron source in each of the 1000
multiplication intervals in our example. To simplify the problem, we assume that
the fission fragment concentration does not change (i.e., C = C0). Thus, the

<!-- page 40 (PDF 64) -->
number of neutrons after 0.1 s (1000l) is
N 1000l
) =
1 − β
)k
[
]mN0 + λlC0 1 − β
)k
[
]m−1 + λlC0 1 − β
)k
[
]m−2
+ ∙∙∙+ λlC0 1 − β
)k + λlC0
=
1 − β
)k
[
]mN0 + λlC0
1 − k 1 − β
[
]
)m−1
1 − k 1 − β
)
=
1 − β
)k
[
]m 1 −
β
k 1 − β
) 1 − k 1 − β
)
[
]

+
β
1 − k 1 − β
)

N0
(2.8)
where Eq. (2.7) has been used in the last step. Evaluating this expression for
k = 1.005 yields N(t = 0.1 s) = 3.03N0, instead of the 150N0 found without taking
the delayed neutrons into account. If we had taken into account the changing
fission fragment population, we would have found a slightly larger number.
Nevertheless, the fact that some of the neutrons emitted in fission are delayed
results in a rather slow and hence controllable response of a neutron chain fission
reacting assembly, provided that (1 − β) k < 1.

## 2.4 Classification of Nuclear Reactors

### Physics Classification by Neutron Spectrum

From the physics viewpoint, the main differences among reactor types arise from
differences in the neutron energy distribution, or spectrum, which causes differences
in the neutron–nuclear reaction rates and the competition for neutrons. The
first level of physics classification categories are then thermal reactors and fast
reactors, corresponding to the majority of the neutron–nuclear reactions involving
neutrons in the thermal energy range (E < 1 eV) and to the majority of the neutron–
nuclear reactions involving neutrons in the fast energy range (E > 1 keV), respectively
. Representative neutron spectra for thermal (LWR) and fast (LMFBR) reactor
cores are shown in Fig. 2.4.
There are important physics differences among the different thermal reactors
and among the different fast reactors, but these differences are not so great as
the physics differences between a thermal reactor and a fast reactor. The
capture-to-fission ratio, α, is lower and the number of neutrons produced
per fission, ν, is larger in fast reactors than in thermal reactors. This generally
results in a larger value of k for a given amount of fuel in a fast reactor than in a
thermal reactor, or, more to the point, a smaller critical mass of fuel in a fast
reactor than in a thermal reactor. Because of the larger neutron–nuclear
reaction rates for thermal neutrons than for fast neutrons, the mean distance
that a neutron travels before absorption is greater in a fast reactor than in a
thermal reactor. This implies that the detailed distribution of fuel, coolant, and
control elements has a much greater effect on the local competition for neutrons
in a thermal reactor than in a fast reactor and that the neutron populations in the
different regions of the core are more tightly coupled in a fast reactor than in a
thermal reactor.

<!-- page 41 (PDF 65) -->
### Engineering Classification by Coolant

The neutron spectrum is determined primarily by the principal neutron moderating
material present, and in many cases this material is the coolant. Because
the heat transport system is such a major aspect of a nuclear reactor, it is also
common to classify reactors according to coolant. Water-cooled reactors, such as
the pressurized water (PWR) and boiling water (BWR) reactors, which use H2O
coolant, and the pressurized heavy water reactor (PHWR), which uses D2O
coolant, have thermal neutron spectra because of the excellent moderating
properties of hydrogen. Since gas is too diffuse to serve as an effective moderator,
gas-cooled reactors can be either thermal or fast, depending on whether or not a
moderator, commonly graphite, is included. The early Magnox and subsequent
advanced gas reactors (AGRs) are cooled with CO2, and the advanced hightemperature
gas-cooled reactor (HTGR) is cooled with helium; all are moderated
with graphite to achieve a thermal spectrum. Designs have been developed for a
helium-cooled reactor without graphite, which is known as the gas-cooled fast
reactor (GCFR). The pressure tube graphite-moderated reactor (PTGR) is cooled
with pressurized or boiling water in pressure tubes, but it is necessary to include
graphite to achieve a thermal spectrum. The molten salt breeder reactor (MSBR)
employs a molten salt fluid that acts as both the fuel and the primary coolant loop,
and is moderated by graphite to achieve a thermal spectrum. The advanced
liquid-metal reactor (ALMR) and the liquid-metal fast breeder reactor (LMFBR)
are cooled with sodium, which is not a particularly effective moderator, and the
neutron spectrum is fast.
Fig. 2.4 Representative fast (LMFBR) and thermal (LWR) reactor neutron energy distributions.
Flux ≡ nv. (With permission from Ref. [3]. Copyright 1992, Taylor & Francis.)

<!-- page 42 (PDF 66) -->
## References

1 J. J. DUDERSTADT and L. J. HAMILTON, Nuclear Reactor Analysis, Wiley, New York
(1976).
2 N. L. SHAPIRO et al., Electric Power Research Institute Report, EPRI-NP-359,
Electric Power Research Institute, Palo Alto, CA (1977).
3 R. A. KNIEF, Nuclear Engineering, 2nd ed., Taylor & Francis, Washington, DC
(1992).

## Further Readings

BELL G. I. and GLASSTONE S., Nuclear Reactor Theory, Van Nostrand Reinhold,
New York (1970).
GLASSTONE S. and EDLUND M. C., Nuclear Reactor Theory, D. Van Nostrand,
Princeton, NJ (1952).
HENRY A. F., Nuclear-Reactor Analysis, MIT Press, Cambridge, MA (1975).
LAMARSH J. R., Introduction to Nuclear Reactor Theory, 2nd ed., Addison-Wesley,
Reading, MA (1983).
MEGHREBLIAN R. V. and HOLMES D. K., Reactor Analysis, McGraw-Hill, New York
(1960), pp. 160–267 and 626–747.
WEINBERG A. M. and WIGNER E. P., The Physical Theory of Neutron Chain Reactors,
University of Chicago Press, Chicago (1958).

## Problems

2.1 Calculate and plot the thermal value of η for a uranium-fueled reactor as a
function of enrichment (e.g., percentage 235U in uranium) over the range
0.07–5.0%.
2.2 Calculate the thermal utilization in a homogeneous 50:50 vol% mixture of
carbon and natural uranium. Repeat the calculation for 4% enriched uranium.
